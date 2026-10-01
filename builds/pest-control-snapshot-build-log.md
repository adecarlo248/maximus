# 🐛 Pest Control GHL Snapshot — Build Log
**Sub-account Location ID:** `t8mcJBn6Z1ELEOvGm4Oe`
**Build Date:** 2026-07-21
**Status:** PHASES 1–4 COMPLETE | PHASE 5 DOCUMENTED (manual build required)

---

## PHASE 1: CUSTOM FIELDS ✅ COMPLETE (20/20)

All custom fields created on contact model.

| # | Field Name | Type | GHL Field Key | GHL ID |
|---|-----------|------|---------------|--------|
| 1 | Lead Source | SINGLE_OPTIONS | `contact.lead_source` | `oKg2DO6Xrxrxvs1cb60B` |
| 2 | Job Type | SINGLE_OPTIONS | `contact.job_type` | `TJbXY4NthqLadJnUeEtU` |
| 3 | Service Category | SINGLE_OPTIONS | `contact.service_category` | `izW6usAYnd8xXYChD7Bp` |
| 4 | Pest Type | TEXT | `contact.pest_type` | `txnhHo9qNrwRf8PUBRyz` |
| 5 | Property Type | SINGLE_OPTIONS | `contact.property_type` | `7uzJaOdoO027QPxpylN0` |
| 6 | Infestation Severity | SINGLE_OPTIONS | `contact.infestation_severity` | `f1Gsi92479TDKManQSav` |
| 7 | Recurring Plan Tier | SINGLE_OPTIONS | `contact.recurring_plan_tier` | `Kz6AC8qVKFJvKVAbwMmu` |
| 8 | Plan Start Date | DATE | `contact.plan_start_date` | `lBwxEwhJ2Eag3zB1ioc9` |
| 9 | Plan Renewal Date | DATE | `contact.plan_renewal_date` | `BCmO869XNsz0j7Idps83` |
| 10 | Termite Contract | RADIO (Yes/No) | `contact.termite_contract` | `vnUZQoxxzU1sg5ZbYPWl` |
| 11 | Chemical Sensitivity | RADIO (Yes/No) | `contact.chemical_sensitivity` | `82KA2IGzvsMWPZXZ5l1j` |
| 12 | Pets on Property | RADIO (Yes/No) | `contact.pets_on_property` | `zxFgFbw5LleLrS98pkDx` |
| 13 | Estimate Amount | MONETORY | `contact.estimate_amount` | `QaftO4XvqBW2GOvm7xEa` |
| 14 | Invoice Amount | MONETORY | `contact.invoice_amount` | `WzOzrMWobgGFOnUHR2sn` |
| 15 | Technician Assigned | TEXT | `contact.technician_assigned` | `hFRhUaAkVgrFW4cw90TW` |
| 16 | Treatment Date | DATE | `contact.treatment_date` | `bsC8aVWwYsThjMaWHF3N` |
| 17 | Follow-Up Treatment Required | RADIO (Yes/No) | `contact.followup_treatment_required` | `24yoiHisv16pYSCVwAL5` |
| 18 | Follow-Up Date | DATE | `contact.followup_date` | `6zBALecQkiJPyfJxlY6Y` |
| 19 | Review Requested | RADIO (Yes/No) | `contact.review_requested` | `0dRRucu9TWg8OZYoA61H` |
| 20 | Review Received | RADIO (Yes/No) | `contact.review_received` | `JXf8kRqSjcvVPJZ0PeVp` |

### Picklist Values

**Lead Source:** Google LSA, Google Emergency Search, Referral, Repeat Customer, Property Manager, Real Estate (Pre-Sale), Angi/HomeAdvisor, Facebook Ad, Nextdoor

**Job Type:** General Pest Control, Ant Treatment, Wasp/Hornets, Bed Bug Heat Treatment, Termite Inspection, Termite Treatment, Rodent Control, Mosquito Treatment, Cockroach, Spider, Wildlife Exclusion, Commercial IPM

**Service Category:** Emergency/One-Time, Recurring Plan, Termite/Specialty, Commercial, Real Estate Inspection

**Property Type:** Residential, Commercial, Multi-Unit/Rental, Restaurant/Food Service, Industrial

**Infestation Severity:** Light, Moderate, Severe, Unknown

**Recurring Plan Tier:** None, Monthly, Bi-Monthly, Quarterly, Annual

---

## PHASE 2: PIPELINES ✅ COMPLETE (5/5)

### Pipeline 1: Pest Control - Residential General
**ID:** `b67z64fqDTMr2WGYkDga`
**Stages (13):** New Lead → Contacted → Inspection Scheduled → Inspection Complete → Treatment Proposal → Follow-Up Active → Treatment Scheduled → Treatment Complete → Follow-Up Treatment → Invoice Sent → Paid → Review Requested → Plan Upsell

### Pipeline 2: Pest Control - Recurring Plan
**ID:** `5SA9VNVzzK6uXI9jCHVE`
**Stages (12):** Plan Prospect → Proposal Sent → Plan Active - Q1 → Q1 Treatment Complete → Plan Active - Q2 → Q2 Treatment Complete → Plan Active - Q3 → Q3 Treatment Complete → Plan Active - Q4 → Renewal Sent → Renewed → Cancelled

### Pipeline 3: Pest Control - Termite / Specialty
**ID:** `oT1UbvSmzvgppTu0nyQi`
**Stages (10):** New Lead → Termite Inspection Scheduled → Inspection Complete → Report Sent → Treatment Proposed → Contract Signed → Treatment Scheduled → Treatment Complete → Annual Inspection Due → Renewed

### Pipeline 4: Pest Control - Commercial
**ID:** `Vli2DDmq5b3cROdsH9tA`
**Stages (10):** New Prospect → Discovery Call → Proposal Sent → Contract Signed → Service Start → Monthly Service Active → Compliance Report Sent → At Risk → Renewed → Lost

### Pipeline 5: Pest Control - Real Estate
**ID:** `lRQO50LcweancoM15XFG`
**Stages (8):** Agent Referral Received → Inspection Scheduled → Inspection Complete → Report Delivered → Treatment Recommended → Treatment Booked → Complete → Clearance Issued

---

## PHASE 3: CALENDARS ✅ COMPLETE (4/4)

| # | Calendar Name | Duration | Days | Hours | GHL ID |
|---|--------------|----------|------|-------|--------|
| 1 | Emergency Pest Inspection | 60 min | Mon–Sat | 8am–6pm | `HaIUqk7d9EW0SBD9lsi0` |
| 2 | Scheduled Pest Treatment | 90 min | Mon–Sat | 8am–5pm | `wELRHxowcjlButSWybTA` |
| 3 | Termite Inspection | 60 min | Mon–Fri | 8am–5pm | `nKD0VyOuFvnuKwIy90yO` |
| 4 | Commercial IPM Assessment | 90 min | Mon–Fri | 8am–4pm | `y9utlf7m6Eadtpiftd7E` |

> **Note:** Calendar open hours require manual configuration in the GHL UI (Calendars → Settings → Availability). The GHL API does not support setting `openHours` object via the REST API for this account tier. Set Mon–Sat 8am–6pm for Emergency, Mon–Sat 8am–5pm for Treatment, Mon–Fri 8am–5pm for Termite, Mon–Fri 8am–4pm for Commercial.

---

## PHASE 4: TAGS ✅ COMPLETE (36/36)

All tags created successfully:

**Pest/Service Tags:** new-lead, emergency-pest, ants, wasps-hornets, bed-bugs, termites, rodents, mosquitoes, cockroach, spiders, wildlife, commercial-ipm

**Plan/Status Tags:** recurring-plan, plan-renewal-due, termite-contract, real-estate-inspection, one-time-treatment, chemical-sensitive, pets-on-property

**Transaction Tags:** estimate-sent, treatment-complete, follow-up-required, invoice-sent, paid, review-requested, review-received

**Lead Source Tags:** referral, cold-lead, no-show, google-lsa, property-manager, facebook-ad, repeat-customer

**Seasonal Tags:** seasonal-spring, seasonal-summer, seasonal-fall

---

## PHASE 5: WORKFLOWS — FULL SPECS 📋

> **API Note:** GHL Workflow API is write-only via UI. All 10 workflows are fully specced below with exact SMS/email copy for manual build in GHL → Automation → Workflows.

---

### ✅ WF-01: Missed Call Text Back — NATIVE GHL SETTING (Not a Workflow)

**Do NOT build this as a workflow.** Use GHL's built-in MCTB feature instead.

**How to enable:**
1. Go to **Settings → Phone Numbers**
2. Click on your phone number
3. Click the **"Voicemail & Missed Call TextBack"** tab
4. Check **"Enable Missed call textback"** ✅
5. Click **"Customize"** and paste the message below

**Customized message for this trade:**
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — pest emergency or need to schedule a treatment? Reply EMERGENCY or BOOK and we'll get right back to you 👋"

This fires automatically on every missed call. No workflow required.

---

### WF-02: New Lead - Speed to Contact

**Trigger:** Contact created (from form submission, LSA integration, or web chat)
**Tags to apply on trigger:** `new-lead`

**Step 1 — Immediate (0 min): SMS**
```
Hi {{contact.firstName}}! Got your message about a pest issue. What are you dealing with and what's your address? We'll get you taken care of. — {{location.name}}
```

**Step 2 — Immediate (0 min): Internal Task**
- Task: "SPEED TO CONTACT — New lead in! Call/text within 5 min"
- Due: Now + 5 minutes
- Assign to: Owner/assigned rep

**Step 3 — Wait 5 min (if no lead reply): SMS**
```
We have openings today and tomorrow. Want us to pop by for a quick inspection? Takes about 20 minutes. — {{location.name}}
```

**Step 4 — Wait 1 hour (if still no booking): Email**
- Subject: `Got your pest inquiry — let's get you booked`
- Body: Include booking link + what to expect + company info

**Step 5 — Wait 3 hours (if no booking): SMS**
```
Last message from us today — if you're still dealing with pests, we're here. Book at [calendar link] or reply here. — {{location.name}}
```

**Step 6 — Wait 24 hours (if no response): Apply tag** `cold-lead`, create 7-day follow-up task

---

### WF-03: Treatment Appointment Confirmation

**Trigger:** Customer booked appointment (any pest control calendar)
**Tags to apply:** `appointment-booked` (create this tag manually)

**Step 1 — Immediate: SMS**
```
Confirmed! Your pest appointment is set for {{appointment.start_time}}. Our tech will call/text 30 min before arrival. Reply STOP to cancel or RESCHEDULE to change. — {{location.name}}
```

**Step 1b — Immediate: Email**
- Subject: `Your pest service is confirmed — here's how to prepare`
- Body:
  - Appointment details (date, time, service type)
  - Prep instructions:
    - Remove pet food/water dishes from areas to be treated
    - Clear under sinks and along baseboards
    - Keep pets and children away from treated areas for 2–4 hours after service
    - Ensure technician has access to all areas (garage, crawlspace if applicable)
  - Technician will call/text 30 min before arrival
  - Contact number for questions

**Step 2 — 48 hours before appointment: SMS**
```
Reminder: Your pest service is in 2 days — {{appointment.start_time}}. Need to make changes? Reply RESCHEDULE or call {{location.phone}}.
```

**Step 3 — 24 hours before: SMS**
```
Your technician is coming tomorrow! Quick prep: remove pet dishes from treated areas, clear under sinks, keep kids/pets out for 2–4 hours post-treatment. See you {{appointment.start_time}}! — {{location.name}}
```

**Step 4 — 2 hours before: SMS**
```
Your tech is on their way today! Estimated arrival: {{appointment.start_time}}. Any access notes we should know? Reply here. — {{location.name}}
```

**Step 5 — If no confirmation reply by 24-hour mark:** Internal task — "Unconfirmed appointment — call to confirm"

---

### WF-04: No-Show Recovery

**Trigger:** Appointment status (filter: no-show)

**Step 1 — Immediate: SMS**
```
Hi {{contact.firstName}}, we missed you for your appointment today. No worries — life happens! Want to reschedule? Reply YES and we'll find another time. — {{location.name}}
```

**Step 2 — Wait 2 hours (if no reply): SMS**
```
Still want to get that pest issue handled? We have openings this week. Just reply here or book at [calendar link].
```

**Step 3 — Wait 24 hours (if no reply): Email**
- Subject: `We missed you — let's reschedule your pest service`
- Body: Friendly re-engagement + booking link + mention of active pest issues getting worse without treatment

**Step 4 — If no response after 48 hours:** Apply tag `cold-lead`, create task "No-show follow-up — call attempt"

---

### WF-05: Post-Treatment Follow-Up (48hr check-in)

**Trigger:** Contact tag (filter: tag added = treatment-complete)

**Step 1 — Wait 1 hour: SMS**
```
Treatment complete! Thanks for trusting {{location.name}} with your home. The treatment is now working — give it 5–7 days for full effect. Any questions? Reply here.
```

**Step 2 — Wait 24 hours: SMS**
```
Hi {{contact.firstName}}! How's everything looking post-treatment? Any pest activity? Also — if you want to make sure they don't come back, ask us about our Quarterly Protection Plan. We'll keep your home pest-free all year. Worth a quick chat?
```

**Step 3 — Wait 72 hours: SMS**
```
{{contact.firstName}}, most pest problems return within 3–6 months without a protection plan. Our Quarterly Service keeps you covered year-round for less than a cup of coffee a day. Want me to lock in a rate for you? Reply YES and I'll send details.
```

**Step 4 — Wait 7 days: Email**
- Subject: `One more thing before {{season}} pest season hits...`
- Body:
  - Seasonal pest context (link to current season)
  - Quarterly protection plan benefits:
    - 4 scheduled treatments per year
    - All covered pest types (ants, roaches, spiders, silverfish, and more)
    - Unlimited callbacks between visits at no extra charge
    - Priority scheduling during outbreak season
  - Starting at $X/quarter (fill in local pricing)
  - Clear CTA: "Book Your Plan" → link

**Step 5 — If no enrollment after 7 days:** Apply tag `cold-lead`, enter 90-day re-engagement (separate workflow or task)

---

### WF-06: Post-Treatment Review Request (Happy Path)

**Trigger:** Contact tag (filter: tag added = treatment-complete) AND `review-requested` NOT applied
**Wait:** 3 days after treatment (or immediately after all-clear for bed bugs)

**Step 1 — Day 3: SMS**
```
Hi {{contact.firstName}}! How are things looking after your treatment? If we knocked it out of the park, would you mind leaving us a quick Google review? It means the world to our team: [Google Review Link]
```

**Apply tag:** `review-requested`, update custom field Review Requested = Yes

**Step 2 — Wait 24 hours (if no click): Email**
- Subject: `Quick question about your service...`
- Body:
  ```
  Hi {{contact.firstName}},
  
  We want to make sure you're 100% satisfied. Did we solve your pest problem?
  
  If yes, could you share a quick review on Google? Takes 90 seconds and helps families in {{location.city}} find us when they need help:
  
  [Leave a Review → Button]
  
  Thank you!
  — {{location.name}}
  ```

**Step 3 — If review link clicked / tag `review-received` applied:** Remove from sequence
**Step 4 — If no action after 5 days:** Remove from sequence (do not push further)

---

### WF-07: Unhappy Customer Recovery

**Trigger:** Customer replied (with keyword filter for negative sentiment) OR Contact tag (filter: tag added = unhappy-customer)

**Step 1 — Immediate: Internal Notification Only (DO NOT send to Google)**
- Internal email/push to owner: "⚠️ Unhappy customer alert — {{contact.name}} — {{contact.phone}}"
- Internal task: "URGENT: Call unhappy customer within 1 hour"

**Step 2 — Wait 30 min (if no internal action): Escalation ping to manager**

**Do NOT:**
- Send review requests to this contact
- Add `review-requested` tag
- Route to any public review platform

**Step 3 — After resolution (manual): Apply `resolved` tag, resume normal nurture sequence**

---

### WF-08: Recurring Plan Upsell (Post One-Time)

**Trigger:** Contact tag (filter: tag added = treatment-complete) AND Contact NOT tagged `recurring-plan`
**Purpose:** Convert one-time customers to recurring plan enrollees

**Step 1 — Wait 24 hours: SMS (Soft)**
```
Your {{contact.pest_type}} treatment should be fully active now. One thing to know: most pest problems return within 90–180 days without a maintenance plan. Our Quarterly Service is designed exactly for this. Want to know more?
```

**Step 2 — Wait 72 hours: SMS (Direct Offer)**
```
{{contact.firstName}} — I wanted to follow up on your recent service. We have a Quarterly Protection Plan that covers unlimited callbacks + quarterly treatments. Want me to add you? Reply YES and I'll get it set up.
```

**Step 3 — Wait 7 days: Email (Benefits)**
- Subject: `Stop dealing with the same problem every 6 months`
- Body:
  ```
  Hi {{contact.firstName}},
  
  You called us because you had a pest problem. We fixed it. But here's the truth: without a maintenance plan, there's a good chance you'll deal with the same thing next season.
  
  Our Quarterly Service covers:
  • 4 scheduled treatments per year
  • All covered pest types (ants, roaches, spiders, silverfish, and more)
  • Unlimited callbacks between visits at no extra charge
  • Priority scheduling during outbreak season
  
  Starting at just $[X]/quarter. That's $[X/month]/month to never deal with this again.
  
  [Book Your Plan →]
  
  — {{location.name}}
  ```

**If enrolled:** Apply tag `recurring-plan`, update custom field Recurring Plan Tier, move to Recurring Plan pipeline
**If declined after Step 3:** Apply tag `cold-lead`, enter 90-day re-engagement

---

### WF-09: Plan Renewal Sequence

**Trigger:** Custom date reminder (select Plan Renewal Date field, set 60 days before)

**Step 1 — 60 days before renewal: Email**
```
Subject: Your pest protection plan renewal is coming up

Hi {{contact.firstName}},

Your annual pest protection plan renewal is coming up in 60 days. We'll automatically schedule your next treatment soon. Same great coverage.

Want to review your plan, add services, or make any changes? Just reply here or call {{location.phone}}.

— {{location.name}}
```

**Step 2 — 30 days before: SMS**
```
Hi {{contact.firstName}}! Your quarterly service is coming up in about a month. Any new pest concerns we should know about before the visit? Reply here anytime. — {{location.name}}
```

**Step 3 — 14 days before: SMS**
```
{{contact.firstName}}, your pest protection renewal is 2 weeks out. We'll be reaching out soon to confirm your next visit time. Talk soon! — {{location.name}}
```

**Step 4 — 7 days before: Booking confirmation for renewal visit** (if not already booked — internal task to book)
- If no booking: Internal task "Book renewal visit — {{contact.name}}"

**Step 5 — After service complete: SMS**
```
Another year of protection locked in! Thanks for sticking with {{location.name}}. Let us know if you ever notice anything between visits — that's what we're here for.
```

**Apply tag:** `plan-renewal-due` removed, re-set renewal date +1 year in custom field

---

### WF-10: Seasonal Outbreak Campaign (Manual Trigger)

**Trigger:** Scheduler (3 weeks before each seasonal peak, or manual launch)
**Segments:** Full database (all contacts) + filter by no `do-not-contact` tag

#### Spring Campaign (Trigger: Early March)
**SMS:**
```
⚠️ Spring pest season is here for {{location.city}}! Ants and termites are already active in your area. Get ahead of it before your schedule fills. Book now: [calendar link] — {{location.name}}
```

**Email:**
- Subject: `{{location.city}}'s Ant Season Starts Earlier Every Year — Here's How to Beat It`
- Body: Educational content about spring ant/termite surge + quarterly plan offer + booking CTA
- Apply tag: `seasonal-spring`

#### Summer Campaign (Trigger: Late May)
**SMS:**
```
Summer mosquito season is peaking. Our barrier spray gives you 3–4 weeks of yard protection. Perfect before outdoor events. Book before spots fill: [calendar link]
```

**Email:**
- Subject: `Enjoy your backyard this summer (without DEET)`
- Apply tag: `seasonal-summer`

#### Fall Campaign (Trigger: Early September)
**SMS:**
```
🐭 FALL RODENT ALERT: Mice start moving indoors as temps drop. They fit through a hole the size of a dime. Our exclusion service permanently seals entry points. Spots are limited — book now: [calendar link]
```

**Email:**
- Subject: `Seal your home before winter — rodents are already looking`
- Apply tag: `seasonal-fall`

#### Winter Campaign (Trigger: Early November)
**SMS:**
```
Winter pests don't go away — they move inside. Roaches, silverfish, and stored product pests thrive in heated homes. Last service was a while ago? Book a winter check-up. — {{location.name}}
```

**Email:**
- Subject: `Start the new year pest-free`

---

## SUMMARY TABLE

| Phase | Component | Count | Status |
|-------|-----------|-------|--------|
| 1 | Custom Fields | 20 | ✅ COMPLETE |
| 2 | Pipelines | 5 | ✅ COMPLETE |
| 3 | Calendars | 4 | ✅ COMPLETE |
| 4 | Tags | 36 | ✅ COMPLETE |
| 5 | Workflows (documented) | 10 | 📋 MANUAL BUILD |

**Total API objects created:** 65 (20 fields + 5 pipelines + 4 calendars + 36 tags)

---

## POST-BUILD MANUAL ACTIONS REQUIRED

### Calendars (in GHL UI → Calendars → Edit each):
1. **Emergency Pest Inspection** — Set availability: Mon–Sat 8:00am–6:00pm
2. **Scheduled Pest Treatment** — Set availability: Mon–Sat 8:00am–5:00pm
3. **Termite Inspection** — Set availability: Mon–Fri 8:00am–5:00pm
4. **Commercial IPM Assessment** — Set availability: Mon–Fri 8:00am–4:00pm

### Workflows (in GHL UI → Automation → Workflows):
Build all 10 workflows using the specs above. Recommended build order:
1. WF-01: Missed Call Text Back (highest ROI — build first)
2. WF-03: Appointment Confirmation (reduces no-shows immediately)
3. WF-02: New Lead Speed to Contact
4. WF-05: Post-Treatment Follow-Up
5. WF-06: Review Request
6. WF-08: Recurring Plan Upsell
7. WF-09: Plan Renewal Sequence
8. WF-04: No-Show Recovery
9. WF-07: Unhappy Customer Recovery
10. WF-10: Seasonal Campaigns

### Additional Tags to Create Manually:
- `appointment-booked` — for appointment confirmation workflow trigger
- `unhappy-customer` — for unhappy customer recovery workflow
- `resolved` — for resolved unhappy customer cases

### Additional Notes:
- Set Google Review link in all review request templates
- Replace `[calendar link]` placeholders with actual booking widget URLs
- Set local pricing in plan upsell email templates
- Connect LSA integration via Settings → Integrations → Google LSA
- Set Missed Call Text Back trigger in Settings → Phone → Missed Call Text Back (built-in GHL feature)

---

*Build completed by Maximus AI — 1app Technologies Inc.*
*Location ID: t8mcJBn6Z1ELEOvGm4Oe*
