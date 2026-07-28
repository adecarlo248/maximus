#!/usr/bin/env python3
"""Build Cleaning Company GHL snapshot infrastructure.

Location: qxs3X4jCYse1W18z5H3k
Sub-account: Cleaning company

Creates: custom fields, pipelines/stages, calendars, tags, and a build log.
Does NOT create workflows — GHL public API generally does not expose workflow creation.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

BASE = "https://services.leadconnectorhq.com"
LOCATION_ID = "qxs3X4jCYse1W18z5H3k"
TOKEN = os.environ.get("GHL_TOKEN") or "pit-3ecbb243-76a6-4d43-9d5e-825eb8ac4c0d"
LOG_PATH = Path("/home/maximus/.openclaw/workspace/builds/cleaning-company-snapshot-build-log.md")
IDS_PATH = Path("/home/maximus/.openclaw/workspace/builds/cleaning-company-snapshot-ids.json")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Version": "2021-07-28",
}
CAL_HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Version": "2021-04-15",
}

BUILD = {
    "locationId": LOCATION_ID,
    "builtAt": datetime.now().isoformat(),
    "customFields": [],
    "pipelines": [],
    "calendars": [],
    "tags": [],
    "errors": [],
}


def request(method, path, body=None, headers=None, timeout=30):
    url = BASE + path
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers or HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(raw)
        except Exception:
            parsed = {"raw": raw}
        return e.code, parsed


def get(path):
    return request("GET", path)


def post(path, body, headers=None):
    return request("POST", path, body, headers=headers)


def safe_options(values):
    return [{"label": v} for v in values]


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
    "Cleaning - New Leads": [
        "New Inquiry", "Auto Reply Sent", "Needs More Info", "Quote Requested", "Quote Sent", "Follow-Up Active", "Booked", "Cold Lead", "Lost / Not Now",
    ],
    "Cleaning - Bookings": [
        "Booked", "Confirmed", "Cleaner Assigned", "In Progress", "Completed", "Invoice Sent", "Paid", "Review Requested",
    ],
    "Cleaning - Recurring Clients": [
        "Recurring Quote Requested", "Recurring Proposal Sent", "Active Weekly", "Active Bi-Weekly", "Active Monthly", "At Risk", "Paused", "Cancelled",
    ],
    "Cleaning - Airbnb Turnovers": [
        "New Turnover Request", "Timing Confirmed", "Turnover Scheduled", "Cleaner Assigned", "Completed", "Issue Reported", "Recurring Turnover Offered", "Recurring Turnover Active",
    ],
    "Cleaning - Commercial Leads": [
        "New Commercial Inquiry", "Walkthrough Booked", "Walkthrough Completed", "Proposal Sent", "Follow-Up Active", "Contract Won", "Active Account", "Lost / Not Now",
    ],
}

CALENDARS = [
    ("Residential Cleaning", 120, "Standard residential cleaning, recurring home cleans, and one-time home service."),
    ("Deep Cleaning / Move-Out Cleaning", 240, "Deep cleans, move-in/move-out cleans, and heavy one-time cleaning jobs."),
    ("Commercial Walkthrough / Quote Call", 30, "Commercial cleaning quote calls and walkthrough appointments."),
    ("Airbnb Turnover Cleaning", 180, "Short-term rental turnover cleaning appointment window."),
    ("Post-Construction Walkthrough", 30, "Post-construction cleaning walkthrough and quote appointment."),
]

TAGS = [
    "new-lead", "quote-requested", "cleaning-booked", "customer-active", "cold-lead",
    "recurring-client", "recurring-interest", "recurring-upsell-sent", "review-requested", "review-received", "referral-requested",
    "service-residential-cleaning", "service-deep-cleaning", "service-move-in-out", "service-commercial-cleaning", "service-airbnb-turnover", "service-post-construction", "service-recurring-cleaning", "service-one-time-cleaning",
    "airbnb-turnover-booked", "recurring-turnover-interest", "commercial-cold-lead", "post-construction-lead",
    "no-show", "cancelled", "facebook-lead", "google-lead", "website-lead", "referral-lead", "phone-lead", "urgent-clean", "needs-quote", "quote-sent", "invoice-sent", "paid", "service-complete",
]


def existing_names():
    names = {"fields": set(), "pipelines": set(), "calendars": set(), "tags": set()}

    _, fields = get(f"/locations/{LOCATION_ID}/customFields")
    for f in fields.get("customFields", []):
        names["fields"].add(f.get("name"))

    _, pipelines = get(f"/opportunities/pipelines?locationId={urllib.parse.quote(LOCATION_ID)}")
    for p in pipelines.get("pipelines", []):
        names["pipelines"].add(p.get("name"))

    _, calendars = get(f"/calendars/?locationId={urllib.parse.quote(LOCATION_ID)}")
    for c in calendars.get("calendars", []):
        names["calendars"].add(c.get("name"))

    _, tags = get(f"/locations/{LOCATION_ID}/tags")
    for t in tags.get("tags", []):
        names["tags"].add(t.get("name"))

    return names


def create_custom_fields(existing):
    for name, data_type, opts in CUSTOM_FIELDS:
        if name in existing["fields"]:
            BUILD["customFields"].append({"name": name, "status": "skipped-existing"})
            continue
        body = {"name": name, "dataType": data_type}
        if opts:
            body["options"] = safe_options(opts)
        status, res = post(f"/locations/{LOCATION_ID}/customFields", body)
        rec = {"name": name, "statusCode": status}
        if status in (200, 201):
            cf = res.get("customField") or res
            rec["id"] = cf.get("id") if isinstance(cf, dict) else None
        else:
            rec["error"] = res
            BUILD["errors"].append({"customField": name, "status": status, "response": res})
        BUILD["customFields"].append(rec)
        time.sleep(0.1)


def create_pipelines(existing):
    for pipeline_name, stages in PIPELINES.items():
        if pipeline_name in existing["pipelines"]:
            BUILD["pipelines"].append({"name": pipeline_name, "status": "skipped-existing"})
            continue
        status, res = post("/opportunities/pipelines", {"name": pipeline_name, "locationId": LOCATION_ID})
        prec = {"name": pipeline_name, "statusCode": status, "stages": []}
        if status not in (200, 201):
            prec["error"] = res
            BUILD["errors"].append({"pipeline": pipeline_name, "status": status, "response": res})
            BUILD["pipelines"].append(prec)
            continue
        pipeline = res.get("pipeline") or res
        pid = pipeline.get("id")
        prec["id"] = pid
        for i, stage_name in enumerate(stages):
            s_status, s_res = post(f"/opportunities/pipelines/{pid}/stages", {"name": stage_name, "position": i})
            srec = {"name": stage_name, "position": i, "statusCode": s_status}
            if s_status in (200, 201):
                stage = s_res.get("stage") or s_res
                srec["id"] = stage.get("id") if isinstance(stage, dict) else None
            else:
                srec["error"] = s_res
                BUILD["errors"].append({"stage": stage_name, "pipeline": pipeline_name, "status": s_status, "response": s_res})
            prec["stages"].append(srec)
            time.sleep(0.1)
        BUILD["pipelines"].append(prec)
        time.sleep(0.2)


def create_calendars(existing):
    for name, duration, description in CALENDARS:
        if name in existing["calendars"]:
            BUILD["calendars"].append({"name": name, "status": "skipped-existing"})
            continue
        body = {
            "name": name,
            "locationId": LOCATION_ID,
            "description": description,
            "slotDuration": duration,
            "slotInterval": duration,
            "isActive": True,
            "autoConfirm": True,
            "calendarType": "event",
        }
        status, res = post("/calendars/", body, headers=CAL_HEADERS)
        rec = {"name": name, "durationMinutes": duration, "statusCode": status}
        if status in (200, 201):
            cal = res.get("calendar") or res
            rec["id"] = cal.get("id") if isinstance(cal, dict) else None
        else:
            rec["error"] = res
            BUILD["errors"].append({"calendar": name, "status": status, "response": res})
        BUILD["calendars"].append(rec)
        time.sleep(0.15)


def create_tags(existing):
    for name in TAGS:
        if name in existing["tags"]:
            BUILD["tags"].append({"name": name, "status": "skipped-existing"})
            continue
        status, res = post(f"/locations/{LOCATION_ID}/tags", {"name": name})
        rec = {"name": name, "statusCode": status}
        if status in (200, 201):
            tag = res.get("tag") or res
            rec["id"] = tag.get("id") if isinstance(tag, dict) else None
        else:
            rec["error"] = res
            BUILD["errors"].append({"tag": name, "status": status, "response": res})
        BUILD["tags"].append(rec)
        time.sleep(0.05)


def write_log():
    good_fields = [x for x in BUILD["customFields"] if x.get("statusCode") in (200, 201)]
    good_pipes = [x for x in BUILD["pipelines"] if x.get("statusCode") in (200, 201)]
    good_cals = [x for x in BUILD["calendars"] if x.get("statusCode") in (200, 201)]
    good_tags = [x for x in BUILD["tags"] if x.get("statusCode") in (200, 201)]

    lines = []
    lines.append("# Cleaning Company Snapshot Build Log")
    lines.append("")
    lines.append(f"**Location ID:** `{LOCATION_ID}`")
    lines.append("**Sub-account:** Cleaning company")
    lines.append(f"**Built:** {BUILD['builtAt']}")
    lines.append("")
    lines.append("## Research / Setup Strategy")
    lines.append("")
    lines.append("Cleaning companies need fast quote response, tight appointment prep, recurring client conversion, review/referral capture, and separate handling for deadline-based work like move-in/move-out, Airbnb turnovers, commercial walkthroughs, and post-construction cleaning.")
    lines.append("")
    lines.append("Core segments this snapshot supports:")
    lines.append("- Residential standard cleaning")
    lines.append("- Deep cleaning")
    lines.append("- Move-in / move-out cleaning")
    lines.append("- Airbnb / short-term rental turnover cleaning")
    lines.append("- Commercial cleaning")
    lines.append("- Post-construction cleaning")
    lines.append("- Recurring weekly / bi-weekly / monthly cleaning")
    lines.append("")
    lines.append("## Created via API")
    lines.append("")
    lines.append(f"- Custom fields created: {len(good_fields)}")
    lines.append(f"- Pipelines created: {len(good_pipes)}")
    lines.append(f"- Calendars created: {len(good_cals)}")
    lines.append(f"- Tags created: {len(good_tags)}")
    lines.append(f"- Errors: {len(BUILD['errors'])}")
    lines.append("")
    lines.append("## Custom Fields")
    lines.append("")
    for f in BUILD["customFields"]:
        lines.append(f"- {f.get('name')} — {f.get('id', f.get('status', f.get('statusCode')))}")
    lines.append("")
    lines.append("## Pipelines")
    lines.append("")
    for p in BUILD["pipelines"]:
        lines.append(f"### {p.get('name')} — `{p.get('id', p.get('status', p.get('statusCode')) )}`")
        for s in p.get("stages", []):
            lines.append(f"- {s.get('position')}. {s.get('name')} — `{s.get('id', s.get('statusCode'))}`")
        lines.append("")
    lines.append("## Calendars")
    lines.append("")
    for c in BUILD["calendars"]:
        lines.append(f"- {c.get('name')} ({c.get('durationMinutes')} min) — `{c.get('id', c.get('status', c.get('statusCode')) )}`")
    lines.append("")
    lines.append("## Tags")
    lines.append("")
    for t in BUILD["tags"]:
        lines.append(f"- {t.get('name')} — `{t.get('id', t.get('status', t.get('statusCode')) )}`")
    lines.append("")
    lines.append("## Manual Configuration Required")
    lines.append("")
    lines.append("GHL API limitations mean these still need manual setup in the UI:")
    lines.append("- Assign calendars to users/team members")
    lines.append("- Set calendar availability / business hours")
    lines.append("- Add calendar confirmation/reminder settings if not using workflow reminders")
    lines.append("- Enable native Missed Call Text Back on the phone number")
    lines.append("- Build automations manually using `builds/cleaning-service-ai-builder-prompts.md`")
    lines.append("- Connect Google Business Profile / review link")
    lines.append("- Connect payment/invoicing if needed")
    lines.append("")
    if BUILD["errors"]:
        lines.append("## Errors")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(BUILD["errors"], indent=2))
        lines.append("```")
        lines.append("")
    else:
        lines.append("## Errors")
        lines.append("")
        lines.append("None.")
        lines.append("")
    LOG_PATH.write_text("\n".join(lines), encoding="utf-8")
    IDS_PATH.write_text(json.dumps(BUILD, indent=2), encoding="utf-8")


def main():
    print("Inspecting existing GHL assets...")
    existing = existing_names()
    print({k: len(v) for k, v in existing.items()})

    print("Creating custom fields...")
    create_custom_fields(existing)
    print("Creating pipelines and stages...")
    existing = existing_names()
    create_pipelines(existing)
    print("Creating calendars...")
    existing = existing_names()
    create_calendars(existing)
    print("Creating tags...")
    existing = existing_names()
    create_tags(existing)
    print("Writing build log...")
    write_log()

    print(json.dumps({
        "customFields": len([x for x in BUILD["customFields"] if x.get("statusCode") in (200, 201)]),
        "pipelines": len([x for x in BUILD["pipelines"] if x.get("statusCode") in (200, 201)]),
        "calendars": len([x for x in BUILD["calendars"] if x.get("statusCode") in (200, 201)]),
        "tags": len([x for x in BUILD["tags"] if x.get("statusCode") in (200, 201)]),
        "errors": len(BUILD["errors"]),
        "log": str(LOG_PATH),
        "ids": str(IDS_PATH),
    }, indent=2))


if __name__ == "__main__":
    main()
