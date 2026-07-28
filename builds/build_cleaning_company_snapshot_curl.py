#!/usr/bin/env python3
"""Build Cleaning Company GHL snapshot using curl transport.
Python urllib gets blocked by LeadConnector/Cloudflare on this host; curl succeeds.
"""
import json, os, subprocess, time
from datetime import datetime
from pathlib import Path

BASE = "https://services.leadconnectorhq.com"
LOCATION_ID = "qxs3X4jCYse1W18z5H3k"
TOKEN = "pit-3ecbb243-76a6-4d43-9d5e-825eb8ac4c0d"
LOG_PATH = Path("/home/maximus/.openclaw/workspace/builds/cleaning-company-snapshot-build-log.md")
IDS_PATH = Path("/home/maximus/.openclaw/workspace/builds/cleaning-company-snapshot-ids.json")

BUILD = {"locationId": LOCATION_ID, "builtAt": datetime.now().isoformat(), "customFields": [], "pipelines": [], "calendars": [], "tags": [], "errors": []}

def curl(method, path, body=None, version="2021-07-28"):
    cmd = ["curl", "-sS", "-w", "\n%{http_code}", "-X", method, BASE + path,
           "-H", f"Authorization: Bearer {TOKEN}", "-H", f"Version: {version}", "-H", "Content-Type: application/json"]
    if body is not None:
        cmd += ["-d", json.dumps(body)]
    out = subprocess.check_output(cmd, text=True)
    raw, code = out.rsplit("\n", 1)
    try: data = json.loads(raw) if raw.strip() else {}
    except Exception: data = {"raw": raw}
    return int(code), data

def get(path, version="2021-07-28"):
    cmd = ["curl", "-sS", "-w", "\n%{http_code}", BASE + path,
           "-H", f"Authorization: Bearer {TOKEN}", "-H", f"Version: {version}"]
    out = subprocess.check_output(cmd, text=True)
    raw, code = out.rsplit("\n", 1)
    try: data = json.loads(raw) if raw.strip() else {}
    except Exception: data = {"raw": raw}
    return int(code), data

def opts(vals): return [{"label": v} for v in vals]

CUSTOM_FIELDS = [
    ("Lead Source", "SINGLE_OPTIONS", ["Google", "Facebook", "Instagram", "Website", "Referral", "Walk-In", "Phone Call", "Repeat Customer", "Property Manager", "Realtor", "Airbnb Host", "Commercial Referral"]),
    ("Cleaning Type", "SINGLE_OPTIONS", ["Residential Standard", "Residential Deep Clean", "Move-In / Move-Out", "Airbnb / Short-Term Rental Turnover", "Commercial / Office", "Post-Construction", "Recurring Maintenance", "One-Time Clean", "Window / Add-On", "Other"]),
    ("Service Frequency", "SINGLE_OPTIONS", ["One-Time", "Weekly", "Bi-Weekly", "Monthly", "As Needed", "Turnover Schedule", "Commercial Contract"]),
    ("Property Type", "SINGLE_OPTIONS", ["House", "Apartment / Condo", "Townhouse", "Office", "Retail", "Salon / Spa", "Daycare", "Restaurant", "Airbnb / STR", "Post-Construction Site", "Other Commercial"]),
    ("Bedrooms", "NUMERICAL", None),
    ("Bathrooms", "NUMERICAL", None),
    ("Approx Square Footage", "NUMERICAL", None),
    ("Pets On Site", "RADIO", ["Yes", "No"]),
    ("Access Instructions", "LARGE_TEXT", None),
    ("Priority Areas", "LARGE_TEXT", None),
    ("Special Instructions", "LARGE_TEXT", None),
    ("Preferred Service Date", "DATE", None),
    ("Quote Amount", "MONETORY", None),
    ("Recurring Plan Price", "MONETORY", None),
    ("Deposit Paid", "RADIO", ["Yes", "No", "Not Required"]),
    ("Cleaner Assigned", "TEXT", None),
    ("Review Requested", "RADIO", ["Yes", "No"]),
    ("Review Received", "RADIO", ["Yes", "No"]),
    ("Referral Requested", "RADIO", ["Yes", "No"]),
    ("Recurring Client", "RADIO", ["Yes", "No"]),
    ("Last Service Date", "DATE", None),
    ("Next Service Date", "DATE", None),
    ("Airbnb Checkout Time", "TEXT", None),
    ("Airbnb Next Check-In Time", "TEXT", None),
]
PIPELINES = {
    "Cleaning - New Leads": ["New Inquiry", "Auto Reply Sent", "Needs More Info", "Quote Requested", "Quote Sent", "Follow-Up Active", "Booked", "Cold Lead", "Lost / Not Now"],
    "Cleaning - Bookings": ["Booked", "Confirmed", "Cleaner Assigned", "In Progress", "Completed", "Invoice Sent", "Paid", "Review Requested"],
    "Cleaning - Recurring Clients": ["Recurring Quote Requested", "Recurring Proposal Sent", "Active Weekly", "Active Bi-Weekly", "Active Monthly", "At Risk", "Paused", "Cancelled"],
    "Cleaning - Airbnb Turnovers": ["New Turnover Request", "Timing Confirmed", "Turnover Scheduled", "Cleaner Assigned", "Completed", "Issue Reported", "Recurring Turnover Offered", "Recurring Turnover Active"],
    "Cleaning - Commercial Leads": ["New Commercial Inquiry", "Walkthrough Booked", "Walkthrough Completed", "Proposal Sent", "Follow-Up Active", "Contract Won", "Active Account", "Lost / Not Now"],
}
CALENDARS = [
    ("Residential Cleaning", 120, "Standard residential cleaning, recurring home cleans, and one-time home service."),
    ("Deep Cleaning / Move-Out Cleaning", 240, "Deep cleans, move-in/move-out cleans, and heavy one-time cleaning jobs."),
    ("Commercial Walkthrough / Quote Call", 30, "Commercial cleaning quote calls and walkthrough appointments."),
    ("Airbnb Turnover Cleaning", 180, "Short-term rental turnover cleaning appointment window."),
    ("Post-Construction Walkthrough", 30, "Post-construction cleaning walkthrough and quote appointment."),
]
TAGS = ["new-lead", "quote-requested", "cleaning-booked", "customer-active", "cold-lead", "recurring-client", "recurring-interest", "recurring-upsell-sent", "review-requested", "review-received", "referral-requested", "service-residential-cleaning", "service-deep-cleaning", "service-move-in-out", "service-commercial-cleaning", "service-airbnb-turnover", "service-post-construction", "service-recurring-cleaning", "service-one-time-cleaning", "airbnb-turnover-booked", "recurring-turnover-interest", "commercial-cold-lead", "post-construction-lead", "no-show", "cancelled", "facebook-lead", "google-lead", "website-lead", "referral-lead", "phone-lead", "urgent-clean", "needs-quote", "quote-sent", "invoice-sent", "paid", "service-complete"]

def existing_names():
    names = {"fields": set(), "pipelines": set(), "calendars": set(), "tags": set()}
    _, d = get(f"/locations/{LOCATION_ID}/customFields")
    names["fields"] = {x.get("name") for x in d.get("customFields", [])}
    _, d = get(f"/opportunities/pipelines?locationId={LOCATION_ID}")
    names["pipelines"] = {x.get("name") for x in d.get("pipelines", [])}
    _, d = get(f"/calendars/?locationId={LOCATION_ID}")
    names["calendars"] = {x.get("name") for x in d.get("calendars", [])}
    _, d = get(f"/locations/{LOCATION_ID}/tags")
    names["tags"] = {x.get("name") for x in d.get("tags", [])}
    return names

def create_field(name, typ, options, existing):
    if name in existing["fields"]:
        BUILD["customFields"].append({"name": name, "status": "skipped-existing"}); return
    body = {"name": name, "dataType": typ}
    if options: body["options"] = opts(options)
    code, res = curl("POST", f"/locations/{LOCATION_ID}/customFields", body)
    rec = {"name": name, "statusCode": code}
    if code in (200,201): rec["id"] = (res.get("customField") or res).get("id")
    else: rec["error"] = res; BUILD["errors"].append({"customField": name, "status": code, "response": res})
    BUILD["customFields"].append(rec); time.sleep(.12)

def create_pipelines(existing):
    for pname, stages in PIPELINES.items():
        if pname in existing["pipelines"]:
            BUILD["pipelines"].append({"name": pname, "status": "skipped-existing"}); continue
        code, res = curl("POST", "/opportunities/pipelines", {"name": pname, "locationId": LOCATION_ID})
        prec = {"name": pname, "statusCode": code, "stages": []}
        if code not in (200,201):
            prec["error"] = res; BUILD["errors"].append({"pipeline": pname, "status": code, "response": res}); BUILD["pipelines"].append(prec); continue
        pid = (res.get("pipeline") or res).get("id"); prec["id"] = pid
        for i, sname in enumerate(stages):
            scode, sres = curl("POST", f"/opportunities/pipelines/{pid}/stages", {"name": sname, "position": i})
            srec = {"name": sname, "position": i, "statusCode": scode}
            if scode in (200,201): srec["id"] = (sres.get("stage") or sres).get("id")
            else: srec["error"] = sres; BUILD["errors"].append({"stage": sname, "pipeline": pname, "status": scode, "response": sres})
            prec["stages"].append(srec); time.sleep(.12)
        BUILD["pipelines"].append(prec); time.sleep(.2)

def create_calendars(existing):
    for name, dur, desc in CALENDARS:
        if name in existing["calendars"]:
            BUILD["calendars"].append({"name": name, "status": "skipped-existing"}); continue
        body = {"name": name, "locationId": LOCATION_ID, "description": desc, "slotDuration": dur, "slotInterval": dur, "isActive": True, "autoConfirm": True, "calendarType": "event"}
        code, res = curl("POST", "/calendars/", body, version="2021-04-15")
        rec = {"name": name, "durationMinutes": dur, "statusCode": code}
        if code in (200,201): rec["id"] = (res.get("calendar") or res).get("id")
        else: rec["error"] = res; BUILD["errors"].append({"calendar": name, "status": code, "response": res})
        BUILD["calendars"].append(rec); time.sleep(.15)

def create_tags(existing):
    for name in TAGS:
        if name in existing["tags"]:
            BUILD["tags"].append({"name": name, "status": "skipped-existing"}); continue
        code, res = curl("POST", f"/locations/{LOCATION_ID}/tags", {"name": name})
        rec = {"name": name, "statusCode": code}
        if code in (200,201): rec["id"] = (res.get("tag") or res).get("id")
        else: rec["error"] = res; BUILD["errors"].append({"tag": name, "status": code, "response": res})
        BUILD["tags"].append(rec); time.sleep(.06)

def write_log():
    def ok(arr): return [x for x in arr if x.get("statusCode") in (200,201)]
    lines = [
        "# Cleaning Company Snapshot Build Log", "",
        f"**Location ID:** `{LOCATION_ID}`", "**Sub-account:** Cleaning company", f"**Built:** {BUILD['builtAt']}", "",
        "## Research / Setup Strategy", "",
        "Cleaning companies need fast quote response, tight appointment prep, recurring client conversion, review/referral capture, and separate handling for deadline-based work like move-in/move-out, Airbnb turnovers, commercial walkthroughs, and post-construction cleaning.", "",
        "Core segments supported:",
        "- Residential standard cleaning", "- Deep cleaning", "- Move-in / move-out cleaning", "- Airbnb / short-term rental turnover cleaning", "- Commercial cleaning", "- Post-construction cleaning", "- Recurring weekly / bi-weekly / monthly cleaning", "",
        "## Created via API", "",
        f"- Custom fields created: {len(ok(BUILD['customFields']))}", f"- Pipelines created: {len(ok(BUILD['pipelines']))}", f"- Calendars created: {len(ok(BUILD['calendars']))}", f"- Tags created: {len(ok(BUILD['tags']))}", f"- Errors: {len(BUILD['errors'])}", "",
        "## Custom Fields", ""
    ]
    lines += [f"- {x.get('name')} — `{x.get('id', x.get('status', x.get('statusCode')) )}`" for x in BUILD["customFields"]]
    lines += ["", "## Pipelines", ""]
    for p in BUILD["pipelines"]:
        lines.append(f"### {p.get('name')} — `{p.get('id', p.get('status', p.get('statusCode')) )}`")
        for s in p.get("stages", []): lines.append(f"- {s.get('position')}. {s.get('name')} — `{s.get('id', s.get('statusCode'))}`")
        lines.append("")
    lines += ["## Calendars", ""]
    lines += [f"- {x.get('name')} ({x.get('durationMinutes')} min) — `{x.get('id', x.get('status', x.get('statusCode')) )}`" for x in BUILD["calendars"]]
    lines += ["", "## Tags", ""]
    lines += [f"- {x.get('name')} — `{x.get('id', x.get('status', x.get('statusCode')) )}`" for x in BUILD["tags"]]
    lines += ["", "## Manual Configuration Required", "", "- Assign calendars to users/team members", "- Set calendar availability / business hours", "- Add calendar confirmation/reminder settings if not using workflow reminders", "- Enable native Missed Call Text Back on the phone number", "- Build automations manually using `builds/cleaning-service-ai-builder-prompts.md`", "- Connect Google Business Profile / review link", "- Connect payment/invoicing if needed", ""]
    if BUILD["errors"]:
        lines += ["## Errors", "", "```json", json.dumps(BUILD["errors"], indent=2), "```", ""]
    else: lines += ["## Errors", "", "None.", ""]
    LOG_PATH.write_text("\n".join(lines))
    IDS_PATH.write_text(json.dumps(BUILD, indent=2))

existing = existing_names()
print("Existing", {k: len(v) for k,v in existing.items()})
for f in CUSTOM_FIELDS: create_field(*f, existing)
existing = existing_names(); create_pipelines(existing)
existing = existing_names(); create_calendars(existing)
existing = existing_names(); create_tags(existing)
write_log()
print(json.dumps({"customFields": len([x for x in BUILD['customFields'] if x.get('statusCode') in (200,201)]), "pipelines": len([x for x in BUILD['pipelines'] if x.get('statusCode') in (200,201)]), "calendars": len([x for x in BUILD['calendars'] if x.get('statusCode') in (200,201)]), "tags": len([x for x in BUILD['tags'] if x.get('statusCode') in (200,201)]), "errors": len(BUILD['errors']), "log": str(LOG_PATH), "ids": str(IDS_PATH)}, indent=2))
