#!/usr/bin/env python3
"""
GC Snapshot Builder — General Contractor GHL Sub-Account Setup
Location: Dmsp8q1GLGI9B32BzvO7
"""

import requests
import json
import time

GHL_TOKEN = "pit-074edc89-4478-41f4-b40e-a82d1bfbe072"
LOCATION_ID = "Dmsp8q1GLGI9B32BzvO7"

HEADERS_V2021_07 = {
    "Authorization": f"Bearer {GHL_TOKEN}",
    "Version": "2021-07-28",
    "Content-Type": "application/json"
}

HEADERS_V2021_04 = {
    "Authorization": f"Bearer {GHL_TOKEN}",
    "Version": "2021-04-15",
    "Content-Type": "application/json"
}

BUILD_LOG = {
    "custom_fields": [],
    "pipelines": [],
    "calendars": [],
    "tags": [],
    "errors": []
}

def log(msg):
    print(msg)

def err(msg):
    print(f"ERROR: {msg}")
    BUILD_LOG["errors"].append(msg)

def post(url, payload, headers=None, label=""):
    if headers is None:
        headers = HEADERS_V2021_07
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code in (200, 201):
        log(f"  ✓ {label}")
        return r.json()
    else:
        err(f"{label} → {r.status_code}: {r.text[:200]}")
        return None

def create_custom_field(name, dataType, options=None):
    payload = {
        "locationId": LOCATION_ID,
        "name": name,
        "dataType": dataType,
        "model": "contact"
    }
    if options:
        payload["options"] = [{"label": o, "value": o.lower().replace(" ", "_").replace("/", "_").replace("-", "_").replace("+", "plus").replace("$", "").replace(",", "")} for o in options]
    
    url = f"https://services.leadconnectorhq.com/locations/{LOCATION_ID}/customFields"
    r = requests.post(url, json=payload, headers=HEADERS_V2021_07)
    if r.status_code in (200, 201):
        data = r.json()
        field_id = data.get("customField", data).get("id", "unknown")
        log(f"  ✓ Custom field: {name} ({dataType}) → {field_id}")
        BUILD_LOG["custom_fields"].append({"name": name, "type": dataType, "id": field_id})
        return field_id
    else:
        err(f"Custom field '{name}' → {r.status_code}: {r.text[:200]}")
        return None

def create_pipeline(name, stages):
    payload = {
        "locationId": LOCATION_ID,
        "name": name,
        "showInFunnel": True,
        "showInPieChart": True,
        "useOpportunityProbability": False,
        "stages": [
            {
                "name": s,
                "showInFunnel": True,
                "showInPieChart": True,
                "position": i,
            }
            for i, s in enumerate(stages)
        ]
    }
    url = "https://services.leadconnectorhq.com/opportunities/pipelines"
    r = requests.post(url, json=payload, headers=HEADERS_V2021_07)
    if r.status_code in (200, 201):
        data = r.json()
        pipe_id = data.get("pipeline", data).get("id", "unknown")
        log(f"  ✓ Pipeline: {name} → {pipe_id}")
        stage_map = {}
        for s in data.get("pipeline", data).get("stages", []):
            stage_map[s["name"]] = s["id"]
        BUILD_LOG["pipelines"].append({
            "name": name,
            "id": pipe_id,
            "stages": stage_map
        })
        return pipe_id, stage_map
    else:
        err(f"Pipeline '{name}' → {r.status_code}: {r.text[:200]}")
        return None, {}

def create_calendar(name, description, duration_minutes, slot_duration=None, availability_hours=None):
    if slot_duration is None:
        slot_duration = duration_minutes
    
    payload = {
        "locationId": LOCATION_ID,
        "name": name,
        "description": description,
        "slotDuration": slot_duration,
        "slotInterval": slot_duration,
        "slotBuffer": 30,
        "appointmentPerSlot": 1,
        "calendarType": "event",
        "isActive": True,
        "autoConfirm": True,
        "notifications": [
            {
                "type": "email",
                "shouldSendToContact": True,
                "shouldSendToGuest": False,
                "shouldSendToUser": True,
                "shouldSendToSelectedUsers": False
            }
        ],
        "openHours": [
            {
                "daysOfTheWeek": [1, 2, 3, 4, 5],
                "hours": [
                    {
                        "openHour": 8,
                        "openMinute": 0,
                        "closeHour": 17,
                        "closeMinute": 0
                    }
                ]
            }
        ]
    }
    
    if availability_hours:
        payload["openHours"] = [
            {
                "daysOfTheWeek": [1, 2, 3, 4, 5],
                "hours": [availability_hours]
            }
        ]
    
    url = "https://services.leadconnectorhq.com/calendars/"
    r = requests.post(url, json=payload, headers=HEADERS_V2021_04)
    if r.status_code in (200, 201):
        data = r.json()
        cal_id = data.get("calendar", data).get("id", "unknown")
        log(f"  ✓ Calendar: {name} → {cal_id}")
        BUILD_LOG["calendars"].append({"name": name, "id": cal_id})
        return cal_id
    else:
        err(f"Calendar '{name}' → {r.status_code}: {r.text[:300]}")
        return None

def create_tag(name):
    url = f"https://services.leadconnectorhq.com/locations/{LOCATION_ID}/tags"
    payload = {"name": name}
    r = requests.post(url, json=payload, headers=HEADERS_V2021_07)
    if r.status_code in (200, 201):
        data = r.json()
        tag_id = data.get("tag", data).get("id", "unknown")
        BUILD_LOG["tags"].append({"name": name, "id": tag_id})
        return tag_id
    else:
        err(f"Tag '{name}' → {r.status_code}: {r.text[:200]}")
        return None

# ============================================================
# PHASE 1: CUSTOM FIELDS
# ============================================================
log("\n" + "="*60)
log("PHASE 1: CUSTOM FIELDS")
log("="*60)

custom_fields = [
    # 1
    ("Lead Source", "TEXT_BOX_LIST", [
        "Referral", "Real Estate Agent", "Architect/Designer",
        "Google", "Houzz", "Angi", "Repeat Client",
        "Facebook Ad", "Door Knock", "Builder Network"
    ]),
    # 2
    ("Project Type", "TEXT_BOX_LIST", [
        "Residential Remodel", "Home Addition", "Custom New Build",
        "Basement Finish", "Kitchen Renovation", "Bathroom Renovation",
        "Commercial TI", "Exterior Renovation", "Garage/Accessory Structure"
    ]),
    # 3
    ("Project Category", "TEXT_BOX_LIST", [
        "Residential", "Commercial", "Mixed-Use", "New Construction"
    ]),
    # 4
    ("Project Budget", "TEXT_BOX_LIST", [
        "Under $25K", "$25K-$50K", "$50K-$100K", "$100K-$250K",
        "$250K-$500K", "$500K+", "Unknown"
    ]),
    # 5
    ("Project Timeline", "TEXT_BOX_LIST", [
        "ASAP", "1-3 months", "3-6 months", "6-12 months",
        "12+ months", "Just Planning"
    ]),
    # 6
    ("Permit Required", "CHECKBOX", None),
    # 7
    ("Permit Number", "TEXT", None),
    # 8
    ("Permit Status", "TEXT_BOX_LIST", [
        "Not Required", "Applied", "Approved",
        "Inspection Booked", "Passed", "Failed"
    ]),
    # 9
    ("Architect/Designer Involved", "CHECKBOX", None),
    # 10
    ("Architect Name", "TEXT", None),
    # 11
    ("Estimate Amount", "CURRENCY", None),
    # 12
    ("Contract Amount", "CURRENCY", None),
    # 13
    ("Deposit Paid", "CHECKBOX", None),
    # 14
    ("Deposit Amount", "CURRENCY", None),
    # 15
    ("Current Draw/Milestone", "TEXT", None),
    # 16
    ("Project Manager Assigned", "TEXT", None),
    # 17
    ("Site Foreman", "TEXT", None),
    # 18
    ("Project Start Date", "DATE", None),
    # 19
    ("Project End Date", "DATE", None),
    # 20
    ("Review Requested", "CHECKBOX", None),
    # 21
    ("Review Received", "CHECKBOX", None),
    # 22
    ("Referral Source Name", "TEXT", None),
]

for field_def in custom_fields:
    name = field_def[0]
    dtype = field_def[1]
    options = field_def[2] if len(field_def) > 2 else None
    
    # Map types to GHL API types
    type_map = {
        "TEXT": "TEXT",
        "TEXT_BOX_LIST": "TEXT_BOX_LIST",
        "CHECKBOX": "CHECKBOX",
        "CURRENCY": "FLOAT",  # GHL uses FLOAT for currency
        "DATE": "DATE",
    }
    
    api_type = type_map.get(dtype, "TEXT")
    create_custom_field(name, api_type, options)
    time.sleep(0.3)

# ============================================================
# PHASE 2: PIPELINES
# ============================================================
log("\n" + "="*60)
log("PHASE 2: PIPELINES")
log("="*60)

# Pipeline 1: GC - Residential Remodel/Addition
log("\nCreating Pipeline 1: GC - Residential Remodel/Addition")
p1_stages = [
    "New Lead",
    "Initial Consult Scheduled",
    "Site Visit Complete",
    "Scope Development",
    "Estimate Sent",
    "Follow-Up Active",
    "Contract Signed / Deposit Paid",
    "Permit Applied",
    "Permit Approved",
    "Construction Started",
    "Framing Complete",
    "Rough-Ins Complete",
    "Drywall/Finishes",
    "Punch List",
    "Substantial Completion",
    "Final Inspection Passed",
    "Final Invoice",
    "Paid in Full",
    "Review + Referral"
]
p1_id, p1_stages_map = create_pipeline("GC - Residential Remodel/Addition", p1_stages)
time.sleep(0.5)

# Pipeline 2: GC - Custom New Build
log("\nCreating Pipeline 2: GC - Custom New Build")
p2_stages = [
    "New Inquiry",
    "Discovery Meeting",
    "Design Phase",
    "Quote Submitted",
    "Contract Signed / Deposit",
    "Permit Applied",
    "Permit Approved",
    "Site Prep",
    "Foundation",
    "Framing",
    "Rough-Ins",
    "Insulation/Drywall",
    "Finishes",
    "Exterior Complete",
    "Final Inspection",
    "Certificate of Occupancy",
    "Final Invoice",
    "Paid",
    "Review + Referral"
]
p2_id, p2_stages_map = create_pipeline("GC - Custom New Build", p2_stages)
time.sleep(0.5)

# Pipeline 3: GC - Commercial / Tenant Improvement
log("\nCreating Pipeline 3: GC - Commercial / Tenant Improvement")
p3_stages = [
    "New Prospect",
    "RFQ/RFP Received",
    "Site Walk",
    "Proposal Submitted",
    "Contract Awarded",
    "Permit Applied",
    "Mobilization",
    "Construction Phase",
    "Inspections",
    "Substantial Completion",
    "Deficiency List",
    "Final Acceptance",
    "Invoice Sent",
    "Paid",
    "Warranty Period"
]
p3_id, p3_stages_map = create_pipeline("GC - Commercial / Tenant Improvement", p3_stages)
time.sleep(0.5)

# Pipeline 4: GC - Lead Triage
log("\nCreating Pipeline 4: GC - Lead Triage")
p4_stages = [
    "New Lead",
    "Qualified",
    "Not Qualified - Nurture",
    "Referred Out",
    "Lost"
]
p4_id, p4_stages_map = create_pipeline("GC - Lead Triage", p4_stages)
time.sleep(0.5)

# ============================================================
# PHASE 3: CALENDARS
# ============================================================
log("\n" + "="*60)
log("PHASE 3: CALENDARS")
log("="*60)

# Calendar 1: Initial Consultation - GC (60 min, Mon-Fri 8am-5pm)
log("\nCreating Calendar 1: Initial Consultation - GC")
cal1_id = create_calendar(
    name="Initial Consultation - GC",
    description="Free 60-minute project consultation. We'll discuss your project goals, budget, and timeline. Available Mon-Fri 8am-5pm.",
    duration_minutes=60,
    availability_hours={"openHour": 8, "openMinute": 0, "closeHour": 17, "closeMinute": 0}
)
time.sleep(0.5)

# Calendar 2: Site Visit / Assessment (90 min, Mon-Fri 8am-4pm)
log("\nCreating Calendar 2: Site Visit / Assessment")
cal2_id = create_calendar(
    name="Site Visit / Assessment",
    description="90-minute on-site assessment. Our project team will walk the property, take measurements, and discuss your scope of work in detail. Available Mon-Fri 8am-4pm.",
    duration_minutes=90,
    availability_hours={"openHour": 8, "openMinute": 0, "closeHour": 16, "closeMinute": 0}
)
time.sleep(0.5)

# Calendar 3: Design Review Meeting (60 min, Mon-Fri 9am-4pm)
log("\nCreating Calendar 3: Design Review Meeting")
cal3_id = create_calendar(
    name="Design Review Meeting",
    description="60-minute design and planning review meeting. We'll go over drawings, specifications, and project details. Available Mon-Fri 9am-4pm.",
    duration_minutes=60,
    availability_hours={"openHour": 9, "openMinute": 0, "closeHour": 16, "closeMinute": 0}
)
time.sleep(0.5)

# Calendar 4: Commercial Site Walk (90 min, Mon-Fri 8am-4pm)
log("\nCreating Calendar 4: Commercial Site Walk")
cal4_id = create_calendar(
    name="Commercial Site Walk",
    description="90-minute commercial property site walk for TI projects, office buildouts, retail fit-outs, and commercial renovations. Available Mon-Fri 8am-4pm.",
    duration_minutes=90,
    availability_hours={"openHour": 8, "openMinute": 0, "closeHour": 16, "closeMinute": 0}
)
time.sleep(0.5)

# ============================================================
# PHASE 4: TAGS
# ============================================================
log("\n" + "="*60)
log("PHASE 4: TAGS")
log("="*60)

tags_to_create = [
    "new-lead",
    "residential-remodel",
    "home-addition",
    "new-build",
    "basement-finish",
    "kitchen-reno",
    "bathroom-reno",
    "commercial-ti",
    "exterior-reno",
    "permit-required",
    "permit-pending",
    "permit-approved",
    "architect-involved",
    "estimate-sent",
    "deposit-paid",
    "contract-signed",
    "construction-active",
    "punch-list",
    "job-complete",
    "review-requested",
    "review-received",
    "referral",
    "referral-source",
    "cold-lead",
    "no-show",
    "google-lead",
    "houzz-lead",
    "real-estate-agent",
    "repeat-client",
    "high-value-lead",
    "change-order-pending",
    "financing-needed"
]

for tag_name in tags_to_create:
    create_tag(tag_name)
    time.sleep(0.2)

# ============================================================
# SUMMARY
# ============================================================
log("\n" + "="*60)
log("BUILD COMPLETE — SUMMARY")
log("="*60)
log(f"Custom Fields created: {len(BUILD_LOG['custom_fields'])}")
log(f"Pipelines created: {len(BUILD_LOG['pipelines'])}")
log(f"Calendars created: {len(BUILD_LOG['calendars'])}")
log(f"Tags created: {len(BUILD_LOG['tags'])}")
log(f"Errors: {len(BUILD_LOG['errors'])}")

# Save build log data as JSON
with open("/home/maximus/.openclaw/workspace/builds/gc-snapshot-raw-ids.json", "w") as f:
    json.dump(BUILD_LOG, f, indent=2)

log("\nRaw IDs saved to gc-snapshot-raw-ids.json")

if BUILD_LOG["errors"]:
    log("\nERRORS ENCOUNTERED:")
    for e in BUILD_LOG["errors"]:
        log(f"  - {e}")
