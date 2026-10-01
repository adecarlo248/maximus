#!/usr/bin/env python3
"""
GC Snapshot Builder Phase 2 — Fix custom fields + create calendars
"""

import requests
import json
import time

GHL_TOKEN = "pit-074edc89-4478-41f4-b40e-a82d1bfbe072"
LOCATION_ID = "Dmsp8q1GLGI9B32BzvO7"

HEADERS = {
    "Authorization": f"Bearer {GHL_TOKEN}",
    "Version": "2021-07-28",
    "Content-Type": "application/json"
}

HEADERS_CAL = {
    "Authorization": f"Bearer {GHL_TOKEN}",
    "Version": "2021-04-15",
    "Content-Type": "application/json"
}

BUILD_LOG = {
    "custom_fields_fixed": [],
    "calendars": [],
    "errors": []
}

def log(msg):
    print(msg)

def err(msg):
    print(f"ERROR: {msg}")
    BUILD_LOG["errors"].append(msg)

def create_custom_field(name, data_type, options=None):
    payload = {
        "locationId": LOCATION_ID,
        "name": name,
        "dataType": data_type,
        "model": "contact"
    }
    if options:
        payload["options"] = options  # array of strings
    
    url = f"https://services.leadconnectorhq.com/locations/{LOCATION_ID}/customFields"
    r = requests.post(url, json=payload, headers=HEADERS)
    if r.status_code in (200, 201):
        data = r.json()
        field = data.get("customField", data)
        field_id = field.get("id", "unknown")
        log(f"  ✓ {name} ({data_type}) → {field_id}")
        BUILD_LOG["custom_fields_fixed"].append({"name": name, "type": data_type, "id": field_id})
        return field_id
    else:
        err(f"{name} → {r.status_code}: {r.text[:250]}")
        return None

def create_calendar(name, description, slot_duration, slot_buffer=30):
    payload = {
        "locationId": LOCATION_ID,
        "name": name,
        "description": description,
        "slotDuration": slot_duration,
        "slotInterval": slot_duration,
        "slotBuffer": slot_buffer,
        "calendarType": "event",
        "isActive": True,
        "autoConfirm": True,
        "allowReschedule": True,
        "allowCancellation": True,
    }
    url = "https://services.leadconnectorhq.com/calendars/"
    r = requests.post(url, json=payload, headers=HEADERS_CAL)
    if r.status_code in (200, 201):
        data = r.json()
        cal = data.get("calendar", data)
        cal_id = cal.get("id", "unknown")
        log(f"  ✓ Calendar: {name} → {cal_id}")
        BUILD_LOG["calendars"].append({"name": name, "id": cal_id, "slot_duration_mins": slot_duration})
        return cal_id
    else:
        err(f"Calendar '{name}' → {r.status_code}: {r.text[:250]}")
        return None

# ============================================================
# FIX CUSTOM FIELDS — Dropdown fields need SINGLE_OPTIONS
# ============================================================
log("="*60)
log("FIXING CUSTOM FIELDS (Dropdowns + Checkboxes)")
log("="*60)

# Dropdowns using SINGLE_OPTIONS with options as array of strings
dropdowns = [
    ("Lead Source", [
        "Referral", "Real Estate Agent", "Architect/Designer",
        "Google", "Houzz", "Angi", "Repeat Client",
        "Facebook Ad", "Door Knock", "Builder Network"
    ]),
    ("Project Type", [
        "Residential Remodel", "Home Addition", "Custom New Build",
        "Basement Finish", "Kitchen Renovation", "Bathroom Renovation",
        "Commercial TI", "Exterior Renovation", "Garage/Accessory Structure"
    ]),
    ("Project Category", [
        "Residential", "Commercial", "Mixed-Use", "New Construction"
    ]),
    ("Project Budget", [
        "Under $25K", "$25K-$50K", "$50K-$100K", "$100K-$250K",
        "$250K-$500K", "$500K+", "Unknown"
    ]),
    ("Project Timeline", [
        "ASAP", "1-3 months", "3-6 months", "6-12 months",
        "12+ months", "Just Planning"
    ]),
    ("Permit Status", [
        "Not Required", "Applied", "Approved",
        "Inspection Booked", "Passed", "Failed"
    ]),
]

for name, options in dropdowns:
    create_custom_field(name, "SINGLE_OPTIONS", options)
    time.sleep(0.3)

# Checkboxes — CHECKBOX type needs options
log("\nCreating checkbox fields...")
checkboxes = [
    "Permit Required",
    "Architect/Designer Involved",
    "Deposit Paid",
    "Review Requested",
    "Review Received",
]

for name in checkboxes:
    create_custom_field(name, "CHECKBOX", ["Yes", "No"])
    time.sleep(0.3)

# ============================================================
# CALENDARS (without openHours — set manually in GHL UI)
# ============================================================
log("\n" + "="*60)
log("CREATING CALENDARS")
log("="*60)
log("NOTE: openHours must be configured manually in GHL UI")
log("All calendars created with Mon-Fri default slot structure\n")

cals = [
    (
        "Initial Consultation - GC",
        "Free 60-minute project consultation for residential and commercial GC projects. Available Mon-Fri 8am-5pm. Discuss scope, budget, and timeline.",
        60, 30
    ),
    (
        "Site Visit / Assessment",
        "90-minute on-site assessment. Project team walks the property, takes measurements, and reviews scope of work in detail. Available Mon-Fri 8am-4pm.",
        90, 30
    ),
    (
        "Design Review Meeting",
        "60-minute design and planning review for new build and renovation projects. Review drawings, specs, and project details. Available Mon-Fri 9am-4pm.",
        60, 30
    ),
    (
        "Commercial Site Walk",
        "90-minute commercial property site walk for TI projects, office buildouts, retail fit-outs, and commercial renovations. Available Mon-Fri 8am-4pm.",
        90, 30
    ),
]

for name, desc, duration, buffer in cals:
    create_calendar(name, desc, duration, buffer)
    time.sleep(0.5)

# ============================================================
# SUMMARY
# ============================================================
log("\n" + "="*60)
log("PHASE 2 COMPLETE")
log("="*60)
log(f"Custom fields fixed/added: {len(BUILD_LOG['custom_fields_fixed'])}")
log(f"Calendars created: {len(BUILD_LOG['calendars'])}")
log(f"Errors: {len(BUILD_LOG['errors'])}")

with open("/home/maximus/.openclaw/workspace/builds/gc-snapshot-phase2-ids.json", "w") as f:
    json.dump(BUILD_LOG, f, indent=2)

log("Saved to gc-snapshot-phase2-ids.json")

if BUILD_LOG["errors"]:
    log("\nERRORS:")
    for e in BUILD_LOG["errors"]:
        log(f"  - {e}")
