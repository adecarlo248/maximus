# Garage Door Snapshot — Full Build Log

**Location ID:** `2kw5x1ZAluEpsa48PzYa`
**GHL MCP Server:** `gohighlevel-garage-door-template`
**Build Date:** 2026-07-21
**Status:** ✅ COMPLETE — All resources verified and corrected

---

## STEP 1 — Verification Summary

All core resources were previously created. This subagent verified them, corrected calendar durations to match spec, and produced this log.

### Calendar Corrections Made
- **Scheduled Repair Appointment:** 30 min → **60 min** ✅ fixed
- **Free Estimate - New Door:** 30 min → **45 min** ✅ fixed
- **Annual Tune-Up:** 30 min → **45 min** ✅ fixed
- **Emergency Garage Door Service:** 60 min ✅ already correct

---

## PIPELINES

### 1. Garage Door - Emergency Repair
**Pipeline ID:** `UrihYa07Yi7zRP1ruDax`

| # | Stage Name | Stage ID |
|---|-----------|----------|
| 0 | New Emergency Call | `30426195-1e28-4be0-8d16-145f7e8907ce` |
| 1 | Dispatched | `1105ab07-d111-4e8f-a16e-8630e7074455` |
| 2 | Technician On-Site | `3b98f0af-c2e6-461b-8cda-c4b75bce54a0` |
| 3 | Diagnosis Complete | `2d8f291a-8843-4a69-a4cd-5f443c26dde4` |
| 4 | Repair Approved | `cb84d193-1914-41ea-98c7-74b5f22ef10c` |
| 5 | Work Complete | `8a47d2e8-bc34-44df-b36e-11c774e70159` |
| 6 | Invoice Sent | `f68ff80d-e8dc-400b-a60d-853cb889a0e1` |
| 7 | Paid | `324fd333-0a69-444f-a322-2b80f6f7733e` |
| 8 | Review Requested | `1333c6c5-4674-49b9-9da8-d1b2c9136db6` |
| 9 | Smart Opener Upsell | `d4bbcd58-0b4e-4935-adab-718db545dff5` |

---

### 2. Garage Door - Scheduled Repair
**Pipeline ID:** `seDUUIRmc6MgWZE4Sz4s`

| # | Stage Name | Stage ID |
|---|-----------|----------|
| 0 | New Lead | `28cc8222-462b-4dfd-b2a2-f28928bac6a8` |
| 1 | Appointment Booked | `b2bed15f-d6ee-4e0b-a6fd-f62b20945fc3` |
| 2 | Confirmed | `5ada38d6-8b22-49ff-974a-a5289914a04e` |
| 3 | Technician Dispatched | `c2e391ec-3436-40ee-9712-bc7a53d39a79` |
| 4 | Job Complete | `82e928bd-96db-4175-a6c3-a41651377027` |
| 5 | Invoice Sent | `579a8589-4b6c-4be8-a332-01dd059fc9fe` |
| 6 | Paid | `ef908668-b6eb-44ba-b6dd-575d544ebd9e` |
| 7 | Review Requested | `3469ec15-8f77-4a7e-af2f-9ea8c0753e20` |
| 8 | Upsell Follow-Up | `8f529d41-a490-4459-b39b-f768c5f245d2` |

---

### 3. Garage Door - New Door Installation
**Pipeline ID:** `PNgQO7tquV2R6iLdR2AB`

| # | Stage Name | Stage ID |
|---|-----------|----------|
| 0 | New Inquiry | `cc17f527-7caa-4777-886f-d667d90eccf9` |
| 1 | Free Estimate Scheduled | `0c56dabd-1d37-4c5c-8d16-617006d72a03` |
| 2 | Estimate Complete | `bfd50271-3ae1-4c9c-b32a-24ec25bba31b` |
| 3 | Proposal Sent | `6a07f19c-d361-47cf-86e9-d85822b674e0` |
| 4 | Follow-Up Active | `289a1254-e23e-445e-ba47-0f1eb7a87da4` |
| 5 | Contract Signed | `add8f769-af38-4a7e-828c-3d893dc72d8d` |
| 6 | Material Ordered | `00455cab-9ba4-40af-ac17-4c2f67ca20b0` |
| 7 | Install Scheduled | `f84384d4-e21b-4fd5-84aa-c8a552ff6aac` |
| 8 | Install Complete | `f0866660-0156-4ca1-a2c4-848df7149130` |
| 9 | Invoice Sent | `d2bcdfcd-6cdd-4815-9a27-b37617f4f2bc` |
| 10 | Paid | `452060d9-e4ea-4061-a2f6-52c13cf0ead0` |
| 11 | Review + Referral | `052c56d3-598b-446c-bd42-273cf6e8db0d` |

---

### 4. Garage Door - Commercial
**Pipeline ID:** `eqX77yLlncbxbD3wfiaS`

| # | Stage Name | Stage ID |
|---|-----------|----------|
| 0 | New Prospect | `be93ccd2-3bbe-4793-811c-31ae1cf9ceb9` |
| 1 | Site Assessment | `688c2a4d-1b30-43e1-92da-e20401fd8c27` |
| 2 | Proposal Sent | `85c4ea7b-f37c-4b38-9517-701c3bae221d` |
| 3 | Contract Signed | `58eb5a1a-a4ed-4241-9bb4-5b0592a4f3c7` |
| 4 | Install/Service Scheduled | `56dbd0bf-a6f7-4d61-b37a-d9f44c745c27` |
| 5 | Work Complete | `35ed0fe8-41ce-4c29-b33c-26c95b81c92e` |
| 6 | Invoice Sent | `1f39e3db-3da8-4721-ade2-4f38e5432884` |
| 7 | Paid | `60a2f802-f956-4ab2-8e66-8adf85070900` |
| 8 | Ongoing Service Account | `93da31e5-1f7e-4f4a-adab-5948ff4261b0` |

---

## CALENDARS

| Calendar Name | ID | Duration |
|--------------|-----|----------|
| Emergency Garage Door Service | `UESgvKW5mFZwzUrRMhzQ` | 60 min |
| Scheduled Repair Appointment | `jbAmzR8xc5kQP9T28v9o` | 60 min |
| Free Estimate - New Door | `0cLrNltSUFxazsApECDD` | 45 min |
| Annual Tune-Up | `UYg804IFLyDlKBc9PsDB` | 45 min |

---

## TAGS (30 total)

| Tag Name | Tag ID |
|---------|--------|
| aging-opener-10yr | `xcPiBxr5vH2lzBEl9FSE` |
| aging-opener-15yr | `23QyU9HFd5vEepakXCa3` |
| annual-tune-up | `KdCzfaGxCxY0m2WKtvYU` |
| cable-repair | `GRsUTaFoynuym8Y2nxZg` |
| cold-lead | `D9oS1uhZPnLGmoEJbVR9` |
| commercial-door | `zlEv6pFnW049IqpJhR2h` |
| contract-signed | `OjwFj1tgjb9byjxCOXaM` |
| emergency-repair | `g5v1Y4PkKuBK3Pjq5ECN` |
| emergency-search | `15H5ARMDKKCapwyqtIfC` |
| estimate-sent | `NJ2hHEY9Lf1yPZ9m9yTG` |
| facebook-ad | `AlTAJRALoqqHwcZs6Hfs` |
| follow-up | `SHRNwMh5I7pjASBc0nXO` |
| google-lsa | `ZXkuxifoViSpBXGkoGmZ` |
| high priority | `gis4cPHqmJBiGDkKd4os` |
| home-builder | `WMoUWE947NQbrKja4P11` |
| job-complete | `p4UTtwiZ6UYeyb4OJOlU` |
| neighbour-campaign | `zUniTM4LvRBFgxXCCZvl` |
| new-door-install | `nLSOGC0kkLFKv7TzjSL5` |
| new-lead | `Y9mHw5bbcVihK3o6bTkD` |
| no-show | `leC6wjX4l4ZWpSJzzmQO` |
| opener-replacement | `lCbFl06EPmMfYaNilywz` |
| property-manager | `pMcslxgc91GxzlzAKuoT` |
| referral | `VBWFhAVM1QZWXLLIovT9` |
| repeat-customer | `ZXqYQ134VmcoaLFoRDcn` |
| review-received | `j0sLG8gywR7LIu6UmtfM` |
| review-requested | `y9iggTSZTcGgcMaXJBbq` |
| scheduled-repair | `Y5rFEN12E8ENU641D7jn` |
| smart-opener-upsell | `tT81hTdUa7UqB0dZxJu3` |
| spring-replacement | `q9nO6TzlRUdyZBX6W1dY` |
| warm lead | `mBCdQ4o1dCrMMSS4zEja` |

---

## CUSTOM FIELDS (17 total)

| Field Name | Field ID | Key |
|-----------|---------|-----|
| Estimate Amount | `0wBlusC8G5VFJau93zxb` | contact.estimate_amount |
| Opener Brand | `37mfVGA8z9VVvUzvkEry` | contact.opener_brand |
| Property Type | `5jmdlMYNH2aiVtjspQjY` | contact.property_type |
| Invoice Amount | `6Pb0fOvEom9DhfzljffU` | contact.invoice_amount |
| Door Material | `9DFJiupNxkcpVNTj7DWf` | contact.door_material |
| Door Type | `DojduIVByPd7SC2WHAWb` | contact.door_type |
| Opener Age | `EpJUj3H9fhPhm8sYeUFw` | contact.opener_age |
| Smart Opener Compatible | `KRkf1QkDPmbAadhABLG7` | contact.smart_opener_compatible |
| Review Received | `TlsAOU2FkcAfSkxYXSa7` | contact.review_received |
| Lead Source | `V8SP8EiNPwEuFb1KHV76` | contact.lead_source |
| Review Requested | `Vgb3ZxQSGhx6ZSrA5eVq` | contact.review_requested |
| Spring Type | `cVWtM8I5uY8rPOL3JBXx` | contact.spring_type |
| Smart Opener Upsell Offered | `m2sxMVgnYdZfIKwDdaeY` | contact.smart_opener_upsell_offered |
| Annual Tune-Up Date | `mg7pzqNkULS1vTeUF7zx` | contact.annual_tuneup_date |
| Service Category | `woE6ovBMRduzrVvNzpN0` | contact.service_category |
| Technician Assigned | `xRvxLyMSq8H63XJUIeem` | contact.technician_assigned |
| Job Type | `zuYIRM2gLVUcXnM57Zld` | contact.job_type |

---

## WORKFLOW SPECS (10 Workflows)

> **Note:** Workflows must be built manually in the GHL UI or via snapshot import. The GHL public API does not expose a workflow/automation creation endpoint. The specs below are the exact build guide for each workflow.

---

### ✅ WORKFLOW 1: Missed Call Text Back — NATIVE GHL SETTING (Not a Workflow)

**Do NOT build this as a workflow.** Use GHL's built-in MCTB feature instead.

**How to enable:**
1. Go to **Settings → Phone Numbers**
2. Click on your phone number
3. Click the **"Voicemail & Missed Call TextBack"** tab
4. Check **"Enable Missed call textback"** ✅
5. Click **"Customize"** and paste the message below

**Customized message for this trade:**
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — garage door emergency or need to book a service? Reply EMERGENCY or BOOK and we'll get right back to you 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2 — New Emergency Lead: Speed to Dispatch
**Trigger:** Contact tag (filter: tag added = emergency-repair) OR Opportunity created (filter: Emergency Repair pipeline, Stage: New Emergency Call)
**Timing:** Immediate

**Action 1 — Send SMS to contact:**
```
Hi {{contact.firstName}}, we got your emergency request. A technician will be calling you within the next 10 minutes. Please keep your phone nearby.
```

**Action 2 — Create internal task (assigned to owner):**
```
🚨 EMERGENCY DISPATCH — {{contact.firstName}} {{contact.lastName}}
Phone: {{contact.phone}}
Address: {{contact.address1}}
Time submitted: {{now}}
ACTION REQUIRED: Call client immediately and dispatch tech.
```

**Action 3 — Internal notification email to team:**
- Subject: "🚨 Emergency Garage Door Lead — Immediate Action Required"
- Body: Contact name, phone, address, time submitted

**Action 4 — Move opportunity to Stage 1 (Dispatched) once task completed**

---

### Workflow 3 — Emergency Dispatch Confirmation + ETA
**Trigger:** Pipeline stage changed (filter: new stage = Dispatched, Emergency Repair pipeline)
**Timing:** Immediate

**Action — Send SMS to contact:**
```
Your technician is on the way! {{custom.technicianName}} will arrive in approximately {{custom.eta}}. You'll get a text when they're 15 minutes out.
```

**15-min ETA reminder (manual trigger by tech or owner):**
```
{{contact.firstName}}, your tech is 15 minutes away! Please make sure someone is home to let them in.
```

**Note:** Technician name and ETA fields are filled manually by dispatcher before triggering this workflow branch.

---

### Workflow 4 — Scheduled Appointment Confirmation + Reminders
**Trigger:** Customer booked appointment (calendar: Scheduled Repair Appointment or Free Estimate - New Door)
**Timing:** Immediate + 24 hrs before + 2 hrs before

**Immediate SMS:**
```
Hi {{contact.firstName}}, you're confirmed! Your garage door appointment is scheduled for {{appointment.startTime}} on {{appointment.startDate}}. 

Reply CANCEL to cancel or RESCHEDULE to change your time.

— [Company Name] Garage Doors
```

**Immediate Email:**
- Subject: "Your Appointment is Confirmed — [Company Name] Garage Doors"
- Body: Full appointment details, tech will call 30 min before arrival, what to expect

**24-Hour Reminder SMS:**
```
Reminder: Your garage door appointment is tomorrow at {{appointment.startTime}}. Address: {{contact.address1}}. 

Questions? Reply or call us at [phone]. See you tomorrow!
```

**2-Hour Reminder SMS:**
```
Just a heads up — your technician will arrive in about 2 hours ({{appointment.startTime}}). Please make sure someone is home. See you soon!
```

---

### Workflow 5 — No-Show Recovery
**Trigger:** Appointment status (filter: no-show)
**Timing:** 30 minutes after scheduled appointment end time

**Action 1 — Tag contact:** `no-show`

**Action 2 — Send SMS:**
```
Hey {{contact.firstName}}, did we get the time wrong? We can still send someone today. Reply RESCHEDULE or call us at [phone] and we'll get you sorted.
```

**Action 3 (if no reply after 4 hours) — Send follow-up SMS:**
```
{{contact.firstName}}, we want to make sure your garage door gets fixed. We have openings this week — reply YES and we'll find you a spot.
```

**Action 4 — Create task for owner:** "No-show — follow up with {{contact.firstName}} via phone"

---

### Workflow 6 — Post-Emergency Review Request
**Trigger:** Pipeline stage changed (filter: new stage = Review Requested, Emergency Repair pipeline)
**Timing:** 90 minutes after trigger

**Action 1 — Send SMS:**
```
Hope your garage door is working perfectly! If we saved the day, a quick Google review means the world to us: [Google Review Link]

Takes 60 seconds and helps families in [City] find reliable help when they need it most. Thank you! 🙏
```

**Action 2 — Update custom field:** `contact.review_requested` = Yes

**Action 3 (if no review after 3 days) — Send email:**
- Subject: "One small favour from [Company Name]..."
- Body: Thank them for trusting you in an emergency, request Google review, include direct link

---

### Workflow 7 — Post-Scheduled Job Review Request
**Trigger:** Pipeline stage changed (filter: new stage = Review Requested, Scheduled Repair pipeline)
**Timing:** Next morning at 9:00 AM (min 12 hrs after trigger)

**Action 1 — Send SMS:**
```
Hi {{contact.firstName}}! Hope the garage door is running smoothly. 

We'd love a quick Google review if you were happy with the work — it really helps us out: [Google Review Link]

Thanks for choosing us! 🙏
```

**Action 2 — Send email (same day, 10:00 AM):**
- Subject: "How did we do? — [Company Name] Garage Doors"
- Body: Thank them, describe what was serviced, include review link + before/after photo if available

**Action 3 — Update custom field:** `contact.review_requested` = Yes

---

### Workflow 8 — New Door Installation Estimate Follow-Up (5-Step, 21-Day Sequence)
**Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent, New Door Installation pipeline)
**Timing:** Sequence begins day after proposal sent

**Step 1 — Day 1 (SMS):**
```
Hi {{contact.firstName}}, just wanted to make sure you got our quote for your new garage door. Any questions I can answer? I'm happy to walk you through the options. — [Name]
```

**Step 2 — Day 3 (Email):**
- Subject: "Your Garage Door Proposal — A Few Things Worth Knowing"
- Body: Value points (warranty, install time, before/after examples), invite them to call or book a 15-min call

**Step 3 — Day 7 (SMS):**
```
{{contact.firstName}}, we have a few install slots opening up next week. Want to lock one in before they fill? Reply YES and I'll reach out directly.
```

**Step 4 — Day 14 (Email):**
- Subject: "Still thinking it over? Here's what our customers say..."
- Body: 2-3 testimonials, photos, reiterate quote validity period, include booking link

**Step 5 — Day 21 (SMS — final touch):**
```
Hey {{contact.firstName}}, last check-in from us on your garage door quote. The offer stands — whenever you're ready, we're here. No pressure. 🙂
```

**End of sequence — tag contact `cold-lead` if no reply. Remove from active follow-up.**

---

### Workflow 9 — Smart Opener Upsell
**Trigger:** Contact tag (filter: tag added = aging-opener-10yr or aging-opener-15yr) after a completed repair
OR Pipeline stage changed (filter: new stage = Smart Opener Upsell, Emergency Repair pipeline)
OR Pipeline stage changed (filter: new stage = Upsell Follow-Up, Scheduled Repair pipeline)

**Timing:** 48 hours after job complete

**Branch A — Opener age 10–15 years (aging-opener-10yr tag):**

SMS Day 2:
```
Hi {{contact.firstName}}, quick follow-up from your recent service. Our tech noted your garage door opener is around {{contact.opener_age}} years old. 

These units are approaching the end of their lifespan. A smart opener upgrade runs $[price] installed — and you'll love the app control + auto-close features. Want a quick quote?
```

**Branch B — Opener age 15+ years (aging-opener-15yr tag):**

SMS Day 2:
```
Hi {{contact.firstName}}, your garage door opener is {{contact.opener_age}} years old — that's past the typical lifespan. When older units fail, it's usually without warning (and always at the worst time 😅). 

We can upgrade you to a smart opener for $[price] installed. Reply YES and I'll get you a confirmed price today.
```

**Day 5 — Email (both branches):**
- Subject: "Before Your Opener Fails — Upgrade to Smart for $[price]"
- Body: Features comparison (old vs smart), app demo screenshot, booking link for install estimate

**Update field on trigger:** `contact.smart_opener_upsell_offered` = Yes

---

### Workflow 10 — Annual Tune-Up Reminder (Spring + Fall Campaigns)
**Trigger:** Scheduler (Spring: March 1–15 each year; Fall: October 1–15 each year) — sent twice per year

**Target Segment:** Contacts tagged `job-complete` (past customers) who do NOT have `annual-tune-up` tag from current year

**Spring SMS Blast:**
```
Hi {{contact.firstName}}! Spring is here — time to make sure your garage door is ready for the season. 

We're booking spring tune-ups now: $[price] covers full inspection, lubrication, balance check & spring test. 

Book here: [Annual Tune-Up calendar link]
— [Company Name] Garage Doors
```

**Fall SMS Blast:**
```
{{contact.firstName}}, fall is here and winter is coming! A pre-winter garage door tune-up can prevent costly emergency repairs in -20°C weather. 

We're running fall specials now — only $[price] for a full service. Book your spot: [Annual Tune-Up calendar link]
```

**Follow-up Email (3 days after SMS, unopened contacts only):**
- Subject: "[Spring/Fall] Garage Door Tune-Up — Book Before Slots Fill"
- Body: What's included in tune-up, before/winter safety stats, booking CTA

**After booking:**
- Tag contact: `annual-tune-up`
- Update field: `contact.annual_tuneup_date` = appointment date
- Appointment confirmation + reminders via Workflow 4

---

## BUILD STATUS SUMMARY

| Resource | Count | Status |
|---------|-------|--------|
| Pipelines | 4 | ✅ All present with correct stages |
| Pipeline Stages | 40 total | ✅ All verified |
| Calendars | 4 | ✅ Present — durations corrected |
| Tags | 30 | ✅ All present |
| Custom Fields | 17 | ✅ All present |
| Workflows | 10 | 📋 Spec documented (manual build required — GHL API does not support workflow creation) |

---

## NEXT STEPS

1. **Build Workflows 1–10 in GHL UI** using the exact specs and copy above
2. **Update placeholder values** in SMS/email copy:
   - `[Company Name]` → actual business name
   - `[phone]` → GHL sub-account phone number
   - `[price]` → actual service pricing
   - `[Google Review Link]` → business Google review URL
   - `[City]` → service area city
3. **Test Workflow 1** (Missed Call Text Back) with a test call to the GHL number
4. **Test Workflow 2** (Emergency Speed to Dispatch) with a test tagged contact
5. **Export snapshot** from GHL (Settings → Snapshots) to save the full build as a portable template
