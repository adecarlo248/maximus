# Plumbing GHL Snapshot — Build Log
## 1APP Technologies | Sub-Account: Plumbing Template
**Location ID:** `GvcWcM4jUhWzUt3ByNTA`
**Built:** 2026-07-21
**Status:** ✅ Phases 1–4 Complete | ✅ Phase 5 (Workflow Specs) Documented

---

## PHASE 1: CUSTOM FIELDS

All 18 custom fields created at the contact level.

| # | Field Name | Type | ID |
|---|------------|------|-----|
| 1 | Lead Source | SINGLE_OPTIONS | `yBPBhe5tEafuYnTYWt77` |
| 2 | Job Type | SINGLE_OPTIONS | `pZ08jqHF8MqzpuAMWaS3` |
| 3 | Service Category | SINGLE_OPTIONS | `XYo8zRBfXvMbCk4ql7fs` |
| 4 | Property Type | SINGLE_OPTIONS | `ImT4GCUjF0BXgz23KGNM` |
| 5 | Home Ownership | SINGLE_OPTIONS | `LWOJm03NHMEHoU37c2br` |
| 6 | Issue Type | TEXT | `QI5nyUqu7TEP99go7i7Z` |
| 7 | Water Heater Age | SINGLE_OPTIONS | `jm0eiax7bYTu6BsLe8oK` |
| 8 | Water Heater Type | SINGLE_OPTIONS | `ldFnfUaVFHCBxCiiSj5d` |
| 9 | Maintenance Plan Member | CHECKBOX | `eFqe0P8QqZA60RO0X680` |
| 10 | Maintenance Plan Expiry | DATE | `WNBThUbXHbK6VVvHUn26` |
| 11 | Estimate Amount | MONETORY | `gxmSTg1GyW8jq2010dyn` |
| 12 | Invoice Amount | MONETORY | `7suQvy9ZpDgzh6g7w5ZZ` |
| 13 | Technician Assigned | TEXT | `FJVUmzp2hybTmwQaI3NP` |
| 14 | Dispatch Time | DATE | `dqcq6eeZxncYnEEAxJFD` |
| 15 | Review Requested | CHECKBOX | `mKcbikrnAu8fjNGUMjQ4` |
| 16 | Review Received | CHECKBOX | `1dBQbzzVcHUoSt6PAKr5` |
| 17 | Home Warranty Company | TEXT | `Tuuivsbk4l1G3QTQvGU8` |
| 18 | Work Order Number | TEXT | `FbluRUmsWNJaKKNLiO1X` |

### Dropdown Options Reference

**Lead Source options:** Google LSA, Google Organic, Angi/HomeAdvisor, Referral, Repeat Customer, Home Warranty, Property Manager, Yelp, Facebook Ad

**Job Type options:** Emergency Service, Scheduled Service, Water Heater Replacement, Drain Cleaning, Re-Pipe, Backflow Test, Hydro-Jetting, Sewer Scope, Bathroom Remodel, New Construction

**Service Category options:** Emergency, Scheduled, Maintenance Plan, Commercial, Project

**Property Type options:** Residential, Commercial, Multi-Unit/Rental, Strata/Condo

**Home Ownership options:** Owner, Tenant, Property Manager, Unknown

**Water Heater Age options:** Under 5 years, 5-8 years, 8-12 years, 12+ years, Unknown

**Water Heater Type options:** Gas, Electric, Tankless, Heat Pump, Unknown

---

## PHASE 2: PIPELINES

All 5 pipelines created with full stage sets.

---

### Pipeline 1: Plumbing - Emergency Service
**Pipeline ID:** `zu94oBC7zeeSxsJ2SJsp`

| Position | Stage Name | Stage ID |
|----------|-----------|----------|
| 0 | New Emergency Call | `86cffce0-7774-4584-8afa-94830d64f499` |
| 1 | Dispatched | `550d035c-a8bd-45f5-a80b-d22a91602187` |
| 2 | Technician On-Site | `7b99682c-b2c5-48f0-9b70-9cd768469a66` |
| 3 | Diagnosis Complete | `dbb7a09f-30da-4e82-a326-17dc660bb0f0` |
| 4 | Quote Approved | `33431546-5045-488f-82a0-6035d3d3aace` |
| 5 | Work In Progress | `68dcfa8c-020c-49b1-8281-4d836be46f88` |
| 6 | Job Complete | `4a282361-589b-4c95-94c2-bb66f080b9a0` |
| 7 | Invoice Sent | `dad43ced-0613-44b7-8fd4-dc2891c33fe1` |
| 8 | Paid | `f3c04101-bd65-44cd-95f3-a7fddcaa6afe` |
| 9 | Review Requested | `9f843616-b862-46e3-94b4-ac71f4d1d914` |
| 10 | Upsell - Maintenance Plan | `195ffa75-9aa1-472b-a6ec-86eb118afe70` |

---

### Pipeline 2: Plumbing - Scheduled Service
**Pipeline ID:** `EY6Pp4sw3leeV8wMsnpc`

| Position | Stage Name | Stage ID |
|----------|-----------|----------|
| 0 | New Lead | `cb96b260-0014-4297-b9ff-479b4871c139` |
| 1 | Appointment Booked | `dabcc1c4-d9ab-4bcb-a2dd-7fffcc61861e` |
| 2 | Confirmed | `0ba05b4d-e1fb-448a-a4a3-d56039d7147e` |
| 3 | Technician Dispatched | `fc2234e2-20b2-49a9-ba22-66ac4cb7aebe` |
| 4 | Job Complete | `b2b92325-8580-4cf5-be52-76e81c02a58d` |
| 5 | Invoice Sent | `492d13ba-f46b-4832-95a7-3b6d662f21de` |
| 6 | Paid | `7f4f6296-0c18-48ad-bcda-aa54c9800e9d` |
| 7 | Review Requested | `dbada364-f169-41ec-8d16-d346826a87a0` |
| 8 | Upsell - Maintenance Plan | `f104fd25-7159-4516-8d23-427059423ddd` |

---

### Pipeline 3: Plumbing - Projects (Water Heater / Re-Pipe / Remodel)
**Pipeline ID:** `y76BhqASVMP1MtO3JveW`

| Position | Stage Name | Stage ID |
|----------|-----------|----------|
| 0 | New Inquiry | `6370ef44-6165-49b0-a587-d0afd713b76d` |
| 1 | Site Visit Scheduled | `c75e8c6f-10a4-4a56-8dfd-aa48a079d27e` |
| 2 | Quote Sent | `695c4802-3ca5-4ca9-b85c-c846983e5431` |
| 3 | Follow-Up Active | `3c82824c-46d0-4dc0-8cfd-168868856a27` |
| 4 | Quote Approved / Deposit Paid | `2f39238e-accf-432e-8a7c-5ab80057c972` |
| 5 | Materials Ordered | `5247f990-3a70-4a81-8570-a1a35e0c34de` |
| 6 | Job Scheduled | `8d20a37a-9c7f-4c55-8b44-a0e1aa2f7fb0` |
| 7 | Job In Progress | `de3fc14e-d3a2-48e3-895d-3fea8fe24678` |
| 8 | Job Complete | `f37fa998-1944-4dce-8a65-e4ccafb8a151` |
| 9 | Final Invoice Sent | `2c5e02aa-4724-419d-8737-95a95edf0b16` |
| 10 | Paid in Full | `980332be-fc15-450b-97c1-48fcf724c242` |
| 11 | Review + Referral | `ce7c867c-9afa-4770-8370-733dc4ac0bfe` |

---

### Pipeline 4: Plumbing - Maintenance Plans
**Pipeline ID:** `relM2GU962IgFIF8TB0T`

| Position | Stage Name | Stage ID |
|----------|-----------|----------|
| 0 | Upsell Offered | `f65ad5a5-149c-4b76-9d3e-0284610082a0` |
| 1 | Proposal Sent | `1c4f3529-b4c0-49df-9af2-0e613862bfe8` |
| 2 | Plan Active | `836ddf62-1d3e-4ca2-b557-7b226863ac18` |
| 3 | Annual Service Due | `ef220dd9-9adc-428e-b902-e8afe74729b7` |
| 4 | Renewal Sent | `9974605d-acca-449d-9e39-7440919ef0e4` |
| 5 | Renewed | `b942871b-4b5e-4069-af6b-ffd385db5441` |
| 6 | Cancelled | `0452ea97-4309-4db2-a687-aff2676ed70f` |

---

### Pipeline 5: Plumbing - Commercial / Property Manager
**Pipeline ID:** `WTS2TAZlKeuyEiXjPDZZ`

| Position | Stage Name | Stage ID |
|----------|-----------|----------|
| 0 | New Prospect | `94e23dbb-2de2-4428-bdbf-826e11088827` |
| 1 | Meeting Scheduled | `36630350-816a-45bc-860d-5e3cc19d17f4` |
| 2 | Proposal Sent | `58e67528-13be-4600-a149-12b540d424e3` |
| 3 | Contract Signed | `b694dfb0-043f-468e-8ec5-8538a3218547` |
| 4 | Active Account | `b9ff37dd-0ebc-4cca-8c35-548733ef21f8` |
| 5 | At Risk | `9589fc0b-f610-4780-9422-ffc6f8fb5bc5` |
| 6 | Lost | `bff15558-e84f-4bef-9b45-5e228c723449` |

---

## PHASE 3: CALENDARS

All 4 calendars created.

| # | Calendar Name | Slot Duration | Calendar ID |
|---|--------------|---------------|-------------|
| 1 | Emergency Service - Plumbing | 60 min | `52ayaoQcYuZrjO4Iawx4` |
| 2 | Scheduled Service - Plumbing | 90 min | `nQsA0bh5v4xsr3FXYiLx` |
| 3 | Free Estimate - Plumbing Project | 60 min | `zkOBOjjbwMMHPkQMdtDe` |
| 4 | Maintenance Plan Inspection - Plumbing | 60 min | `rt48Zh22iR8l9VrwYprA` |

### Calendar Configuration Notes
- **Calendar 1 (Emergency):** 7 days/week, 7am–8pm. Set `slotInterval: 60`. Requires manual hours configuration in GHL UI (API doesn't accept openHours format for this account).
- **Calendar 2 (Scheduled):** Mon–Sat, 8am–5pm. 90-min slots. Configure hours in GHL UI.
- **Calendar 3 (Free Estimate):** Mon–Fri, 8am–5pm. 60-min slots. Site assessment calendar for project work.
- **Calendar 4 (Maintenance Inspection):** Mon–Fri, 8am–4pm. 60-min slots. Members only.

> **Action Required:** Log into GHL UI and set open hours for each calendar. The API successfully creates calendars but the openHours format is not accepted by this account's API version.

---

## PHASE 4: TAGS

All 27 tags created successfully.

| Tag Name | Tag ID |
|----------|--------|
| new-emergency | `cnGQPGTRg4ZpCMUa56pY` |
| scheduled-service | `dFpBo1E1zB8ONdE3XrXQ` |
| water-heater-replacement | `6RlNFWL8GCXiDnOkGDoS` |
| drain-cleaning | `Grnd6LWwaDbez5VaeU0i` |
| hydro-jetting | `5esKOxt9lgYDCpp6R2V3` |
| sewer-scope | `SMXkwS7EYIM0qVLrKDJP` |
| re-pipe | `qAByVhT0s0uvLL4E1BmM` |
| backflow-test | `iSrCXGLlUDjAP4Q4GF86` |
| maintenance-plan-member | `vrDDmAXunkcpehobaBwF` |
| maintenance-plan-prospect | `92m1xbWvOGCNY3A5hi4I` |
| water-heater-aging | `tDU4wzVG2lis1CTfkkUG` |
| home-warranty | `v7TiXgAB0FACk1RlkGHV` |
| property-manager | `IzQYgdSvggDNSnTABbBq` |
| commercial-account | `VNdx7HiAPxdGFlAS5P0W` |
| estimate-sent | `dry60Tnttchtq5Fabkn8` |
| job-complete | `knYunLbWcHk3BnWYGVKD` |
| invoice-sent | `OTTY7UjwZm5AGnzrHTee` |
| paid | `3570mgNHz1VytXW0pTlf` |
| review-requested | `MECWLSY7FjpMhW1vXw1z` |
| review-received | `Hlt8gSLWPqE88xyaLTpt` |
| referral | `1bSBATbyZQYjFx4Ryhyy` |
| cold-lead | `IQlCSCUqH8XifWAUOgQL` |
| no-show | `zawAxNu2hmKxRMwP4eJx` |
| google-lsa | `XalgYFuAQ11Rogs38oNo` |
| angi-lead | `V5LCbrsLbY0afsm91hk2` |
| facebook-ad | `2mHfyzG6dvTYssdBrqPQ` |
| repeat-customer | `fKZvffDGXd4jou8Y2OQq` |

---

## PHASE 5: WORKFLOW SPECIFICATIONS

> **⚠️ NOTE:** GHL workflows cannot be created via API. All 17 workflow specs below are fully documented for manual build in the GHL Automation builder. Each spec includes trigger, timing, conditions, and exact SMS/email copy.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — plumbing emergency or need to schedule? Reply EMERGENCY or SCHEDULE and we'll get right back to you 👋"

This fires automatically on every missed call. No workflow required.

---

### WORKFLOW 2: New Emergency Lead — Speed to Dispatch

**Trigger:** Contact tag (filter: tag added = new-emergency) OR Contact created (from Emergency Service form submission)
**Timing:** Immediate
**Pipeline:** Emergency Service → Stage: New Emergency Call

**Step 1 — Immediate SMS to Contact:**
> ✅ {{contact.firstName}}, your emergency service request is confirmed! We're dispatching a technician now. You'll get a text when they're on their way. Questions? Call {{location.phone}}

**Step 2 — Immediate Internal Task:**
> Task Title: 🚨 EMERGENCY DISPATCH — {{contact.name}}
> Task Body: Emergency service request from {{contact.firstName}} {{contact.lastName}}
> Phone: {{contact.phone}}
> Address: {{contact.address1}}
> Issue: {{contact.lead_source}} — {{contact.issue_type}}
> **Action required: Assign technician and dispatch immediately**
> Due: NOW

**Step 3 — Move Pipeline Stage:** New Emergency Call → Dispatched (after task assigned)

---

### WORKFLOW 3: Emergency Dispatch Confirmation (Technician En Route)

**Trigger:** Pipeline stage changed (filter: new stage = Dispatched, Emergency Service Pipeline)
**Timing:** Immediate

**Step 1 — SMS to Contact:**
> 🔧 Your plumber is on the way, {{contact.firstName}}! {{contact.technician_assigned}} will arrive in approximately [ETA]. You'll get a text when they're 15 minutes away. Call them directly at {{location.phone}} if needed.

**Step 2 — Update custom field:** Dispatch Time = current time

**Step 3 — Internal note:** Log dispatch confirmation sent

---

### WORKFLOW 4: Scheduled Appointment Confirmation Sequence

**Trigger:** Customer booked appointment (calendar: Scheduled Service - Plumbing or Free Estimate - Plumbing Project)
**Pipeline:** Scheduled Service → Stage: Appointment Booked

**Step 1 — Immediate Confirmation SMS:**
> Hi {{contact.firstName}}! Your appointment with [Company Name] is confirmed for {{appointment.startTime}}. Your technician will text you when they're on their way. Questions? Call {{location.phone}} 🔧

**Step 2 — Immediate Confirmation Email:**
> Subject: Your Plumbing Appointment is Confirmed ✅
>
> Hi {{contact.firstName}},
>
> Your appointment is confirmed for **{{appointment.startTime}}** at {{contact.address1}}.
>
> **What to expect:**
> - Our technician will arrive during your scheduled window
> - You'll receive a text when they're 30 minutes away
> - Please ensure someone 18+ is home to authorize any work
>
> Need to reschedule? Reply to this email or call {{location.phone}}.
>
> See you soon,
> [Company Name] Plumbing

**Step 3 — Wait until 24 hours before appointment**

**Step 4 — 24-Hour Reminder SMS:**
> Reminder: [Company Name] is coming tomorrow, {{appointment.startTime}}. Reply C to confirm or RESCHEDULE if you need to change.

**Step 5 — If no "C" reply after 2 hours:**
> Hey {{contact.firstName}}, just want to make sure you got our reminder! We're still planning to see you tomorrow at {{appointment.startTime}}. Reply C to confirm.

**Step 6 — Wait until 2 hours before appointment**

**Step 7 — Day-Of Reminder SMS:**
> 👋 Just a reminder — your [Company Name] technician will arrive within your {{appointment.startTime}} window today. Get ready to say goodbye to that plumbing issue! Call us if anything changes: {{location.phone}}

**Step 8 — Move Pipeline Stage:** Appointment Booked → Confirmed

---

### WORKFLOW 5: No-Show Recovery

**Trigger:** Appointment status (filter: no-show) OR Contact tag (filter: tag added = no-show)
**Tags to Add:** `no-show`

**Step 1 — Immediate SMS:**
> {{contact.firstName}}, we had a technician scheduled at your home today at {{appointment.startTime}}. We weren't able to reach you — are you still looking for plumbing help? We can rebook you today: {{calendar.link}}

**Step 2 — Wait 2 hours**

**Step 3 — Call attempt** (internal task: call {{contact.name}})

**Step 4 — Wait 24 hours**

**Step 5 — Email:**
> Subject: Still need a hand with your plumbing?
>
> Hi {{contact.firstName}},
>
> We missed you at your appointment yesterday. Life happens — we get it! We still have openings this week if you need us.
>
> Book a new time here: {{calendar.link}}
>
> Or just reply to this email and we'll get you sorted.
>
> [Company Name] Plumbing

**Step 6 — Wait 7 days**

**Step 7 — Add tag:** `cold-lead`
**Remove tag:** `scheduled-service`
**Move to:** 30-Day Re-engagement sequence (Workflow 17)

---

### WORKFLOW 6: Post-Emergency Review Request

**Trigger:** Pipeline stage changed (filter: new stage = Job Complete, Emergency Service Pipeline)
**Timing:** Wait 90 minutes after trigger

**Condition Check:** Was review already requested? (Check custom field Review Requested = Yes → skip)

**Step 1 — SMS (90 min after job complete):**
> Hi {{contact.firstName}} – our tech just wrapped up your emergency service. Hope everything is flowing again! If [Company Name] saved the day, a quick Google review means everything to us: [Google Review Link] 🙏

**Step 2 — Update custom field:** Review Requested = Yes
**Add tag:** `review-requested`
**Move Pipeline Stage:** Job Complete → Review Requested

**Step 3 — Wait 48 hours (if no review detected)**

**Step 4 — Email:**
> Subject: Quick favor — did we save the day?
>
> Hi {{contact.firstName}},
>
> We hope your plumbing emergency is fully resolved! If our team came through for you, a Google review would mean the world to our small business — and it helps other homeowners in [City] find trustworthy plumbing help when they need it most.
>
> Leave a review here: [Google Review Link]
>
> It takes about 2 minutes and we genuinely appreciate every single one.
>
> Thank you,
> [Company Name] Plumbing

**Step 5 — Wait 5 days**

**Step 6 — Final SMS:**
> {{contact.firstName}}, just one last check-in on that review — no pressure at all! If you have 2 minutes: [Google Review Link]. Thanks again for trusting us! 🔧

---

### WORKFLOW 7: Post-Scheduled Review Request

**Trigger:** Pipeline stage changed (filter: new stage = Job Complete, Scheduled Service Pipeline)
**Timing:** Wait 3 hours after trigger

**Condition Check:** Review Requested field = Yes → skip

**Step 1 — SMS (3 hours after job complete):**
> Hi {{contact.firstName}}! Hope [Tech Name] sorted everything out today. If you're happy with the service, a quick Google review would help us out a ton: [Google Review Link] ⭐

**Step 2 — Update custom field:** Review Requested = Yes
**Add tag:** `review-requested`

**Step 3 — Wait 48 hours**

**Step 4 — Email follow-up** (same as Workflow 6, Step 4)

**Step 5 — Wait 5 days**

**Step 6 — Final SMS** (same as Workflow 6, Step 6)

---

### WORKFLOW 8: Unhappy Customer Recovery

**Trigger:** Contact submits negative feedback OR internal tag "unhappy-customer" added (manual)
**Timing:** Immediate

**Step 1 — Internal Alert (DO NOT contact customer via automation):**
> 🚨 UNHAPPY CUSTOMER ALERT
> Contact: {{contact.name}}
> Phone: {{contact.phone}}
> Email: {{contact.email}}
> Job: {{contact.job_type}}
> Issue: {{contact.issue_type}}
>
> **Action Required:** Owner must call personally within 2 hours. Do NOT send review request. Do NOT send any automated messages until resolved.

**Step 2 — Add internal note to contact record**

**Step 3 — Remove contact from all review request sequences**

**Step 4 — Create task:** "Call {{contact.name}} — Unhappy Customer — PRIORITY" Due: 2 hours from now

---

### WORKFLOW 9: Maintenance Plan Upsell Sequence

**Trigger:** Pipeline stage changed (filter: new stage = Upsell - Maintenance Plan, Emergency or Scheduled Pipeline)
**Timing:** Wait 24 hours after trigger
**Tags:** `maintenance-plan-prospect`
**Pipeline:** Move contact to Maintenance Plans Pipeline → Stage: Upsell Offered

**Step 1 — SMS (24 hours after job):**
> {{contact.firstName}} — thanks for choosing [Company Name]! Quick question: have you heard about our HomeShield Plumbing Plan? For just $[X]/year you get annual water heater flush, drain check, priority emergency dispatch + 10% off all services. Want to hear more? Reply YES

**If YES reply → trigger booking link for maintenance inspection calendar**

**Step 2 — Wait 5 days (if no response)**

**Step 3 — Email:**
> Subject: Stop Paying Emergency Rates — Here's a Smarter Option
>
> Hi {{contact.firstName}},
>
> Most homeowners only think about plumbing when something breaks — and that's usually when it costs the most.
>
> Our HomeShield Plumbing Plan changes that. For $[X]/year, you get:
>
> ✅ Annual water heater flush and inspection
> ✅ Full drain flow check
> ✅ Toilet and fixture performance check
> ✅ Outdoor hose bib inspection
> ✅ **Priority dispatch on emergency calls** (you go to the front of the line)
> ✅ 10% discount on all service calls
> ✅ No diagnostic fees on covered visits
>
> Most of our plan members save more than the plan cost in their first year.
>
> [Learn More & Enroll] → [Link]
>
> Questions? Just reply to this email.
>
> [Company Name] Plumbing

**Step 4 — Wait 7 days**

**Step 5 — Final SMS:**
> Last chance, {{contact.firstName}} — our maintenance plan spots are filling up for the season. Lock in your rate here: [Link]. After that we can't guarantee the current price.

**Step 6 — If no response:** Add tag `cold-lead`. Remove from upsell sequence. Schedule re-offer in 6 months.

---

### WORKFLOW 10: Maintenance Plan Renewal

**Trigger:** Custom date reminder (select Maintenance Plan Expiry field, set 60 days before)
**Timing:** Scheduled / date-based trigger

**Move Pipeline Stage:** Plan Active → Annual Service Due

**Step 1 — Day 60 before renewal — Email:**
> Subject: Your [Company Name] Plumbing Plan Renews in 60 Days
>
> Hi {{contact.firstName}},
>
> Just a heads-up — your HomeShield Plumbing Plan renews on {{contact.maintenance_plan_expiry}}.
>
> Before it renews, we want to make sure you've used your annual benefits:
> ✅ Annual water heater flush — booked?
> ✅ Drain flow check — completed?
>
> If not, book your annual inspection now so you get full value: [Book Annual Inspection] → {{calendar.maintenance_link}}
>
> Your renewal will process automatically. Nothing to do unless you want to make changes.
>
> [Company Name] Plumbing

**Step 2 — Wait until 14 days before renewal**

**Step 3 — SMS (14 days before):**
> {{contact.firstName}}, your [Company Name] plumbing plan renews in 2 weeks on {{contact.maintenance_plan_expiry}}. Any questions about your plan? Reply here or call {{location.phone}}.

**Move Pipeline Stage:** Annual Service Due → Renewal Sent

**Step 4 — Wait until 7 days before renewal**

**Step 5 — Email (7 days before):**
> Subject: Your Plan Renews in 1 Week — Here's What You're Getting
>
> Hi {{contact.firstName}},
>
> Your HomeShield Plumbing Plan renews in 7 days. Here's what's included in your next year:
> [List all plan benefits]
>
> All good? No action needed — your plan renews automatically.
>
> Want to make changes or cancel? Reply to this email or call {{location.phone}} at least 5 days before renewal.

**Step 6 — Day of renewal:** Send renewal confirmation email
**Move Pipeline Stage:** Renewal Sent → Renewed

---

### WORKFLOW 11: Water Heater Aging Campaign

**Trigger:** Contact changed (filter: Water Heater Age field updated to 8-12 years OR 12+ years)
**Tags:** `water-heater-aging`

**Step 1 — Email:**
> Subject: Your {{contact.water_heater_age}} Water Heater Is Living on Borrowed Time
>
> Hi {{contact.firstName}},
>
> Most water heaters fail between 8–12 years — often without warning, and usually at the worst possible time (cold morning, full house, holiday weekend).
>
> Since yours is {{contact.water_heater_age}} old, now is the ideal time to get ahead of it.
>
> **Planned replacement vs. emergency replacement:**
> - Planned: $[X]–$[Y], your timeline, your choice of unit
> - Emergency: $[X]–$[Y] more, plus damage risk, no unit selection
>
> **Options we install:**
> - Traditional tank (gas or electric)
> - Tankless (on-demand, energy efficient)
> - Heat pump water heaters (most efficient)
>
> Get a free water heater estimate — we'll assess your current unit and give you an honest recommendation: [Get Free Estimate] → {{calendar.estimate_link}}
>
> [Company Name] Plumbing

**Step 2 — Wait 7 days (if no booking)**

**Step 3 — SMS:**
> {{contact.firstName}}, did you see our note about your {{contact.water_heater_age}}-old water heater? Most units fail between 8–12 years. A quick free estimate takes 10 minutes — book here: [Link]

**Step 4 — Wait 14 days**

**Step 5 — Email (seasonal angle):**
> Subject: Winter is coming — is your water heater ready?
>
> Hi {{contact.firstName}},
>
> Cold weather is the #1 cause of unexpected water heater failures. A unit that's been limping along through summer may not make it through winter.
>
> We're offering free water heater assessments this month. Takes 10 minutes — and we'll tell you honestly whether yours needs replacement or just maintenance.
>
> [Book Free Assessment] → {{calendar.estimate_link}}

---

### WORKFLOW 12: Winterization Campaign (Seasonal — Manual Launch)

**Trigger:** Scheduler (launch early-mid November, targets contacts tagged repeat-customer or past customers)
**Audience:** Contacts tagged `repeat-customer` OR past customers in service area
**Launch timing:** Early-mid November

**Step 1 — SMS Blast:**
> ❄️ Winter prep time! [Company Name] is offering pipe winterization services before the cold hits. Don't wait until you have a burst pipe — schedule your winterization for just $[X]: [Link]

**Step 2 — Wait 3 days**

**Step 3 — Email:**
> Subject: Are Your Pipes Ready for [City] Winter? (They Might Not Be)
>
> Hi {{contact.firstName}},
>
> [City] winters are no joke — and frozen pipes are one of the most expensive plumbing emergencies there is. A single burst pipe can cause thousands in water damage.
>
> What we winterize:
> ✅ Outdoor hose bibs (shutoff and drain)
> ✅ Exposed pipe insulation check
> ✅ Water heater efficiency check for winter demand
> ✅ Sump pump pre-winter test
> ✅ Irrigation system blowout (if applicable)
>
> Winterization is $[X] and takes about 60–90 minutes. Book before [Date] for guaranteed pre-freeze scheduling: [Book Now] → [Link]
>
> [Company Name] Plumbing

**Step 4 — Wait 5 days**

**Step 5 — Final Urgency SMS:**
> Only [X] slots left for November winterization — once those go, we're booking into December: [Link]

---

### WORKFLOW 13: Spring Plumbing Checkup Campaign (Seasonal — Manual Launch)

**Trigger:** Scheduler (launch late March / early April)

**Step 1 — SMS:**
> 🌱 Spring is here and your plumbing survived winter — but let's check under the hood. [Company Name] is running spring checkup specials this month. Book here: [Link]

**Step 2 — Wait 4 days**

**Step 3 — Email:**
> Subject: 5 Things Every Homeowner Should Check After Winter
>
> Hi {{contact.firstName}},
>
> Winter is hard on your home's plumbing. Here are 5 things to check now that temperatures are rising:
>
> 1. **Outdoor hose bibs** — reconnect and check for drips (a frozen pipe may have cracked over winter)
> 2. **Sump pump** — spring rain is coming; is yours working?
> 3. **Backflow preventer** — annual testing is required if you have irrigation
> 4. **Water heater** — flush sediment buildup from the winter
> 5. **Under-sink pipes** — check for any slow drips that have been hiding
>
> Want us to run through the whole list? Our Spring Checkup takes 45 minutes and covers everything: [Book a Spring Checkup] → [Link]
>
> [Company Name] Plumbing

**Step 4 — Wait 5 days**

**Step 5 — Final SMS:**
> {{contact.firstName}}, spring checkup special ends [Date]. Grab a slot while we have them: [Link]

---

### WORKFLOW 14: Drain Cleaning Special Campaign (Seasonal — Manual Launch)

**Trigger:** Scheduler (launch May, September, or as needed)
**Audience:** All past customers, especially those tagged `drain-cleaning` or no service in 60+ days
**Launch timing:** May, September, or as needed

**Step 1 — SMS:**
> Is your kitchen drain running slower than usual? 🚿 [Company Name] is running a drain cleaning special this month for $[X]. Book by [Date]: [Link]

**Step 2 — Wait 4 days**

**Step 3 — Email:**
> Subject: Top 5 Signs Your Drains Need Professional Cleaning
>
> Hi {{contact.firstName}},
>
> If you're seeing any of these, it's time for a professional drain cleaning:
>
> 1. 🐌 Water draining slower than usual (kitchen or bathroom)
> 2. 🤢 Gurgling sounds when drains are running
> 3. 💧 Multiple drains backing up at once
> 4. 🪰 Fruit flies or drain flies appearing
> 5. 👃 Bad odors coming from drains
>
> DIY drain cleaners often make this worse — they can damage pipes and mask the real problem.
>
> Our hydro-jetting and drain cleaning services clear the blockage completely, not just punch a hole through it.
>
> **$[X] drain cleaning special — book by [Date]:** [Book Now] → [Link]
>
> [Company Name] Plumbing

**Step 5 — Wait 5 days**

**Final SMS:**
> Last day for our $[X] drain cleaning special — grab your slot before we're full: [Link]

---

### WORKFLOW 15: Home Warranty Lead Workflow

**Trigger:** Contact tag (filter: tag added = home-warranty) OR Contact changed (filter: Lead Source = Home Warranty)
**Pipeline:** Emergency or Scheduled (based on urgency), with internal note

**Step 1 — Immediate Internal Note:**
> HOME WARRANTY LEAD — Different process applies
> Company: {{contact.home_warranty_company}}
> Work Order: {{contact.work_order_number}}
> Rate is pre-set. No price negotiation with homeowner.
> Get work order # before dispatching.
> Document everything — photos, description, parts used.
> Do NOT send maintenance plan upsell.

**Step 2 — SMS to Contact:**
> Hi {{contact.firstName}}, we received your service request from {{contact.home_warranty_company}}. We'll be in touch shortly to confirm your appointment. Please have your work order number {{contact.work_order_number}} available. Questions? Call {{location.phone}}.

**Step 3 — Confirmation and scheduling** (same as standard scheduled workflow)

**Step 4 — Post-job documentation task:**
> Task: Submit service report to {{contact.home_warranty_company}} for Work Order {{contact.work_order_number}}
> Include: photos, description, parts used, labor time
> Due: Same day as job completion

**Step 5 — Review request:** Send standard review request (same timing as scheduled service)

> **Note:** Skip all maintenance plan upsell sequences for home warranty contacts.

---

### WORKFLOW 16: Property Manager Onboarding

**Trigger:** Contact tag (filter: tag added = property-manager) AND Pipeline stage changed (filter: new stage = Contract Signed, Commercial Pipeline)
**Tags to Add:** `commercial-account`

**Step 1 — Immediate Welcome Email:**
> Subject: Welcome to [Company Name] — Your Dedicated Plumbing Partner
>
> Hi {{contact.firstName}},
>
> Welcome to [Company Name]! We're excited to be your plumbing partner for {{contact.company_name}}.
>
> **How to submit service requests:**
> - Emergency (same-day): Call {{location.phone}} directly — 24/7 emergency line
> - Scheduled service: Book online at [Booking Link] or call during business hours
> - Email for non-urgent: [service@companyemail.com]
>
> **Your account details:**
> - Account manager: [Manager Name]
> - Direct line: [Direct Number]
> - Priority dispatch: Yes — you go to the front of the line
> - Billing: [Net-30 / Credit card on file / etc.]
>
> **What to have ready when you call:**
> - Property address
> - Unit number (if applicable)
> - Tenant name and contact info
> - Brief description of issue
>
> We'll send you a monthly service summary every [day of month] so you always know what's happening across your properties.
>
> Looking forward to a great partnership.
>
> [Your Name]
> [Company Name] Plumbing

**Step 2 — Day 3: Internal task:**
> Task: Introduction call — {{contact.name}} at {{contact.company_name}}
> "Check in, confirm account details, ask about any immediate needs"
> Due: 3 days from contract signed

**Step 3 — Day 7: SMS:**
> Hi {{contact.firstName}}, hope everything's been smooth at {{contact.company_name}} this week! Any maintenance needs or questions for us? Reply here or call {{location.phone}}.

**Step 4 — Day 30: Monthly Summary Email:**
> Subject: [Month] Service Summary — {{contact.company_name}}
>
> Hi {{contact.firstName}},
>
> Here's a quick summary of work completed at your properties this month:
> [Manual entry required — link to service reports or list in email]
>
> Upcoming scheduled maintenance: [List any upcoming booked work]
>
> Any questions or upcoming needs? Reply here or call {{location.phone}}.

**Step 5 — Day 85: Quarterly review task:**
> Task: Quarterly review call — {{contact.name}} at {{contact.company_name}}
> "Review past 90 days, discuss upcoming needs, ask about other properties they manage"
> Due: 85 days from onboarding

**Move Pipeline Stage:** Contract Signed → Active Account

---

### WORKFLOW 17: 30-Day Cold Lead Re-Engagement

**Trigger:** Contact tag (filter: tag added = cold-lead) AND Stale opportunities (no activity in 30 days)
**Also triggers for:** Contact tag (filter: tag added = no-show) + 30 day wait

**Step 1 — SMS:**
> Hey {{contact.firstName}}! Still dealing with that plumbing issue? We're still here whenever you're ready. Reply here or book at your convenience: [Link]

**Step 2 — Wait 7 days**

**Step 3 — Email:**
> Subject: Still thinking about that plumbing work?
>
> Hi {{contact.firstName}},
>
> It's been a little while since we connected — just wanted to check in. Whether it's that [issue type] we talked about or something new that's come up, we're here to help.
>
> We have openings this week. Book here: [Booking Link]
>
> Or if you have questions before booking, reply to this email and we'll answer them.
>
> [Company Name] Plumbing

**Step 4 — Wait 14 days**

**Step 5 — Final SMS:**
> {{contact.firstName}}, last check-in from [Company Name]. If the timing isn't right right now, no worries — we'll still be here when you're ready. [Link] 🔧

**Step 6 — If no response:** Move to long-term nurture list. Add tag `long-term-nurture`. Remove from active sequences.

---

## SUMMARY: WHAT WAS BUILT

### ✅ Completed via API

| Category | Count | Status |
|----------|-------|--------|
| Custom Fields | 18 | ✅ All created |
| Pipelines | 5 | ✅ All created |
| Pipeline Stages | 44 total | ✅ All created |
| Calendars | 4 | ✅ All created |
| Tags | 27 | ✅ All created |

### 📋 Needs Manual Build in GHL UI

| Item | Notes |
|------|-------|
| Calendar hours configuration | Set open hours for all 4 calendars in GHL UI |
| 17 Workflow automations | Specs fully documented above — build in Automation builder |
| Email templates | Copy provided in workflow specs above — create in Email Templates library |
| Forms | 4–6 intake forms (Emergency, Scheduled, Project, Commercial, Maintenance Plan) |
| Snapshot export | Once built, export as snapshot from Settings → Snapshots |

### 🔑 Key IDs Quick Reference

```
LOCATION ID: GvcWcM4jUhWzUt3ByNTA
API TOKEN:   pit-a72eaf37-b714-4951-86eb-bd22783f9c58

PIPELINES:
Emergency Service:         zu94oBC7zeeSxsJ2SJsp
Scheduled Service:         EY6Pp4sw3leeV8wMsnpc
Projects:                  y76BhqASVMP1MtO3JveW
Maintenance Plans:         relM2GU962IgFIF8TB0T
Commercial/PM:             WTS2TAZlKeuyEiXjPDZZ

CALENDARS:
Emergency Service:         52ayaoQcYuZrjO4Iawx4
Scheduled Service:         nQsA0bh5v4xsr3FXYiLx
Free Estimate:             zkOBOjjbwMMHPkQMdtDe
Maintenance Inspection:    rt48Zh22iR8l9VrwYprA

CUSTOM FIELDS:
Lead Source:               yBPBhe5tEafuYnTYWt77
Job Type:                  pZ08jqHF8MqzpuAMWaS3
Service Category:          XYo8zRBfXvMbCk4ql7fs
Property Type:             ImT4GCUjF0BXgz23KGNM
Home Ownership:            LWOJm03NHMEHoU37c2br
Issue Type:                QI5nyUqu7TEP99go7i7Z
Water Heater Age:          jm0eiax7bYTu6BsLe8oK
Water Heater Type:         ldFnfUaVFHCBxCiiSj5d
Maintenance Plan Member:   eFqe0P8QqZA60RO0X680
Maintenance Plan Expiry:   WNBThUbXHbK6VVvHUn26
Estimate Amount:           gxmSTg1GyW8jq2010dyn
Invoice Amount:            7suQvy9ZpDgzh6g7w5ZZ
Technician Assigned:       FJVUmzp2hybTmwQaI3NP
Dispatch Time:             dqcq6eeZxncYnEEAxJFD
Review Requested:          mKcbikrnAu8fjNGUMjQ4
Review Received:           1dBQbzzVcHUoSt6PAKr5
Home Warranty Company:     Tuuivsbk4l1G3QTQvGU8
Work Order Number:         FbluRUmsWNJaKKNLiO1X
```

---

*Built by Maximus | 1APP Technologies | 2026-07-21*
