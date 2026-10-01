# HVAC GHL Snapshot — Full Build Log
### Sub-account: HVAC Template | Location ID: 9PZ17iQFwEDlNdsYpSjr
### Built by: Maximus AI (Subagent) | Date: 2026-07-21
### Status: ✅ Complete — All API-buildable components deployed

---

## Build Summary

| Phase | Component | Status | Count |
|---|---|---|---|
| Phase 1 | Custom Fields | ✅ Complete | 20 fields |
| Phase 2 | Pipelines | ✅ Complete | 5 pipelines |
| Phase 3 | Calendars | ✅ Complete | 4 calendars |
| Phase 4 | Tags | ✅ Complete | 29 tags |
| Phase 5 | Workflow Specs | ✅ Documented | 18 workflows |

---

## PHASE 1: CUSTOM FIELDS (Contact-Level)

All fields created under model: `contact` | Location: `9PZ17iQFwEDlNdsYpSjr`

| # | Field Name | Type | Field ID | Options |
|---|---|---|---|---|
| 1 | Lead Source | SINGLE_OPTIONS | `epod38zpee2jAMwOowpW` | Google LSA, Google Organic, Angi/HomeAdvisor, Home Warranty, Referral, Repeat Customer, Property Manager, Facebook Ad, New Construction Builder |
| 2 | Job Type | SINGLE_OPTIONS | `KwmIOe4MFXiYSnX4B0lY` | Emergency Service, Tune-Up/Maintenance, Equipment Replacement, New Installation, Ductwork, Indoor Air Quality, New Construction |
| 3 | Service Category | SINGLE_OPTIONS | `lBGAJPQJmYIWTllvFAT8` | Emergency, Scheduled Service, Maintenance Agreement, Equipment Replacement, Commercial, New Construction |
| 4 | Equipment Type | SINGLE_OPTIONS | `LXTlZoK6t3wG2ck2ebEq` | Central AC, Heat Pump, Furnace, Boiler, Mini-Split, Rooftop Unit, Air Handler |
| 5 | Equipment Brand | TEXT | `SLf9czCBjE36r6ModWdL` | — |
| 6 | Equipment Age | SINGLE_OPTIONS | `JoIin0RqKmSCWW1V4qwn` | Under 5 years, 5-10 years, 10-15 years, 15+ years, Unknown |
| 7 | Tonnage | SINGLE_OPTIONS | `k8NmGkz8NmZDS1IgdXJF` | 1.5 ton, 2 ton, 2.5 ton, 3 ton, 3.5 ton, 4 ton, 5 ton, Unknown |
| 8 | SEER Rating | TEXT | `V0ZRh5mNS6nWmhLcQXwt` | — |
| 9 | Refrigerant Type | SINGLE_OPTIONS | `7PpmPKW3rafx6CKz3DYr` | R-22, R-410A, R-32, R-454B, Unknown |
| 10 | Filter Size | TEXT | `1E9Bh5DwxTiK6H4Z5bdW` | — |
| 11 | Maintenance Agreement Tier | SINGLE_OPTIONS | `FppHPBb6oQfjlFr43zn9` | None, Silver, Gold, Platinum |
| 12 | MA Expiry Date | DATE | `pSRGvnsZIXJumUAmMEPw` | — |
| 13 | Install Date | DATE | `zW8lwnm8kJg18bbwWmfH` | — |
| 14 | Estimate Amount | MONETORY | `2tBDE7MxeGOqVAOIqiRm` | — |
| 15 | Invoice Amount | MONETORY | `DOpri1UmFcRY9sD41p8Z` | — |
| 16 | Technician Assigned | TEXT | `OHIqrAaWv51giG3cF0Wo` | — |
| 17 | Property Type | SINGLE_OPTIONS | `cmUGbSKy9wzeRNmhwI15` | Residential, Light Commercial, Commercial, Multi-Unit, New Construction |
| 18 | Review Requested | CHECKBOX | `Wot5FgXFoo6nwmLDsoK2` | Yes |
| 19 | Review Received | CHECKBOX | `oP2IQCM9a0Rpn9KjJLBn` | Yes |
| 20 | Equipment Replacement Candidate | CHECKBOX | `4EgaGbeXD2SUPdWpxRyu` | Yes |

**Field Keys (for workflow use):**
- `contact.lead_source`
- `contact.job_type`
- `contact.service_category`
- `contact.equipment_type`
- `contact.equipment_brand`
- `contact.equipment_age`
- `contact.tonnage`
- `contact.seer_rating`
- `contact.refrigerant_type`
- `contact.filter_size`
- `contact.maintenance_agreement_tier`
- `contact.ma_expiry_date`
- `contact.install_date`
- `contact.estimate_amount`
- `contact.invoice_amount`
- `contact.technician_assigned`
- `contact.property_type`
- `contact.review_requested`
- `contact.review_received`
- `contact.equipment_replacement_candidate`

---

## PHASE 2: PIPELINES

### Pipeline 1: HVAC - Service Call
**Pipeline ID:** `2HTjYT1DayqZELLUDDt7`
**Purpose:** Manage inbound repair and diagnostic calls from new and existing customers

| Stage | Stage ID | Notes |
|---|---|---|
| New Call | `aeee3262-e7ee-4232-8f80-7bf2fc2ca1e7` | Trigger: web form, phone, missed call |
| Dispatched | `78e8b97f-8bfd-4cc8-a198-ebe6e321a102` | Tech assigned and notified |
| Technician On-Site | `fd70a720-7790-4245-9f2f-09843fe226da` | Job in progress |
| Diagnosis Complete | `8a3d6ebc-2574-4dcb-a92a-1d3a205cf2ec` | Tech has assessed equipment |
| Repair Approved | `c4b8c10e-eb45-444c-833c-cd924196e4ce` | Customer approved repair scope |
| Work Complete | `b51f1a51-cbac-4488-a560-a5c7f6e00a82` | Service done, triggers payment flow |
| Invoice Sent | `882e426a-10f2-4e65-befa-7f94ec0d8ae4` | Payment link sent |
| Paid | `fe679db5-9e1d-436c-a579-c19798f1c1fa` | Payment received |
| Review Requested | `97a75e97-81cb-4767-a99a-07541267f122` | Google review request sent |
| MA Upsell | `26969bff-e948-4181-99ee-7c3d07d12f2a` | MA offer sent to non-agreement customer |
| Closed | `a0294b18-5c76-496b-91db-a21a06bf5c65` | Job complete |

**Upsell triggers:** After every service call → MA upsell if equipment ≥ 8 years → Equipment replacement nurture

---

### Pipeline 2: HVAC - Maintenance Agreement
**Pipeline ID:** `BbYgGp9lNUUbDqxx5uwb`
**Purpose:** Track, sell, and renew residential maintenance agreements

| Stage | Stage ID | Notes |
|---|---|---|
| MA Prospect | `9b5eab5f-e5d9-4e11-9bfb-76d1f6fa56ae` | Customer identified as non-agreement |
| Proposal Sent | `f8fc5907-abf5-4d99-af57-11e6051adc18` | MA pitch delivered |
| Follow-Up Active | `f335b9ab-3c00-4a81-9b34-ac7163b0fd08` | Prospect considering |
| MA Active - Spring Due | `81e70baa-b272-4f5d-aa3b-02bd550fc7ac` | Spring tune-up scheduled |
| Spring Service Complete | `54c863ac-05d4-4352-9836-c61833b73b37` | Spring tune-up completed |
| MA Active - Fall Due | `27dbb9ae-7216-44b5-91e0-ba88f072413f` | Fall tune-up scheduled |
| Fall Service Complete | `1628f7e2-1727-4b42-8fa7-f86f71da1496` | Fall tune-up completed |
| Renewal Sent | `a7c2b4ca-342c-4ec5-8c38-7a61fb8a2d37` | Renewal reminder initiated |
| Renewed | `f4e71bb6-8864-4681-9c71-30f09497020a` | Agreement renewed |
| Cancelled | `be5065dd-617a-4d86-bb65-ad922e0549bc` | Exit survey triggered |

---

### Pipeline 3: HVAC - Equipment Replacement
**Pipeline ID:** `k1UkgwzC6zDkKzsrm2bW`
**Purpose:** Track and close equipment replacement opportunities

| Stage | Stage ID | Notes |
|---|---|---|
| New Inquiry | `00531c12-ba12-4d48-a45a-54dfc680fc68` | Inbound replacement request or age trigger |
| In-Home Assessment Scheduled | `e1281efd-5c4a-4fb9-9ecd-f43e765eee05` | Comfort consultation booked |
| Assessment Complete | `98fbeaa7-e1eb-42b0-b392-6b8e58be33c3` | Load calc done, proposal pending |
| Proposal Sent | `024f696e-74eb-41c9-bce2-47071ecdbe28` | Full replacement quote delivered |
| Follow-Up Active | `351ddbde-2c9b-42f0-91b6-670c08ae040d` | Customer considering, follow-up active |
| Financing Offered | `db6ddfb0-90a6-42b9-b9e4-ea526c84c387` | Financing application sent (ticket >$6K) |
| Contract Signed | `2335d249-7326-428f-bb81-450c280a9a19` | Deal confirmed, equipment ordered |
| Equipment Ordered | `7318e24d-dda3-4c57-872d-769851cbf604` | Equipment on order |
| Install Scheduled | `67d73e64-e246-4648-b675-88c4e8a9ffa1` | Install date set, crew assigned |
| Install Complete | `8ac2bb51-7fa0-4a1c-8ba3-17db79733947` | System commissioned |
| Final Invoice | `3980f61b-7ebe-4303-8dcf-934dd7175a27` | Final billing sent |
| Paid | `faaca145-ebd0-4383-854a-7102755a22be` | Payment received |
| Review + Referral | `95441f30-97e3-41a9-a175-4202cf78e797` | Review request + MA offer sent |

---

### Pipeline 4: HVAC - New Construction
**Pipeline ID:** `d7ZLYDtFX8lqseIvnzkH`
**Purpose:** Track relationships and bids with homebuilders and general contractors

| Stage | Stage ID | Notes |
|---|---|---|
| Builder Contact | `c5bae606-2db1-44cb-bbe6-5e04eb2546c7` | GC or developer contact created |
| Quote Requested | `e220507c-648f-4b0a-aa62-553169067724` | Project specs received |
| Quote Sent | `d6f924de-138e-4bf0-bcbb-e5b19c864e58` | Proposal with equipment spec sheet |
| Awarded | `d3cf8b06-ad2d-44e7-954e-efedba226063` | Job awarded, contract signed |
| Rough-In Scheduled | `c982236c-92b7-4ba1-bf84-6517bb79dee2` | Ductwork and rough-in phase |
| Rough-In Complete | `7f9c940a-7e24-4932-8113-9c43b0eaf394` | Rough-in done |
| Trim-Out Scheduled | `0f96579c-7160-4ac3-b1c5-6405d4d174f6` | Equipment installation phase |
| Trim-Out Complete | `97cc2c88-e43a-4f70-ada0-e88e8af58d58` | Equipment installed |
| Startup/Commission | `80c38f54-de34-4591-8323-c778e69a9611` | System commissioned, tested |
| Warranty Registered | `54d901c5-133c-4074-95c6-265be4432474` | Equipment warranty filed |
| Closed | `a8d4df7d-987b-4123-a3b7-b9835cb3dda7` | Homeowner added to service pipeline |

---

### Pipeline 5: HVAC - Commercial / Property Manager
**Pipeline ID:** `vHcu75GOhIOOdx88TgPY`
**Purpose:** Track B2B relationships with property managers, building owners, HOAs

| Stage | Stage ID | Notes |
|---|---|---|
| New Prospect | `fdef2aeb-61f0-4892-871f-5c55ca2f6488` | PM contact created |
| Intro Meeting | `675d814d-c837-4683-8444-04814091275e` | Initial discovery meeting |
| Proposal Sent | `8909408d-e608-4450-9969-32d6fd8001e8` | PM contract proposal |
| Contract Signed | `9a3ae45c-66d0-46fc-8fd8-4e26cd19abb6` | PM contract enrolled |
| Active Account | `3bf55404-7809-480a-813e-2cb629dea894` | Active PM client |
| Seasonal Service Due | `4b260c10-5354-4506-b0b6-e5ff65e029ab` | Seasonal PM reminder |
| At Risk | `7109372e-2c1e-41bd-adb6-9e640f8134e5` | Engagement dropped, re-activate |
| Renewed | `bd9f38ce-9539-41fb-8eed-640d51163ab9` | Contract renewed |
| Lost | `fea81d58-60ba-4666-8c77-7c74c394e54e` | Lost reason tagged |

---

## PHASE 3: CALENDARS

| Calendar | Calendar ID | Duration | Notes |
|---|---|---|---|
| Emergency HVAC Service | `d7IaiZS0PP5Fzc241hWJ` | 60 min | 7 days, 7am-9pm availability |
| Tune-Up / Maintenance Appointment | `8zitNxfkrFmHUblJFCJ7` | 90 min | Mon-Sat, 8am-5pm |
| Equipment Replacement Consultation | `uEMMjtbcuB3hb6HzjBgh` | 60 min | Mon-Fri, 8am-5pm |
| Commercial Site Assessment | `b6z79MbLUpKmZfFLOJ5E` | 90 min | Mon-Fri, 8am-4pm |

**Note:** Calendar availability windows should be configured manually in GHL UI to set specific open hours, buffer times, and technician assignment. The API creates the calendar shell; hours/availability are set in Settings > Calendars.

---

## PHASE 4: TAGS

All 29 HVAC tags created:

| Tag | Tag ID |
|---|---|
| new-lead | `BRZwvtKU4s7ktwXvR6t3` |
| emergency-call | `bAlL0db19NRn7Jirqmf5` |
| tune-up | `Bo3bkM6FvTLgEbrTnJ0S` |
| maintenance-agreement | `mk8PNp18RsUQPn0gISHR` |
| ma-renewal-due | `w0wB4Ij3tFy5XfqVWSJa` |
| equipment-replacement-candidate | `gWA0lIcLbZL2Wrs2OX5D` |
| r22-system | `n7hbYJdnXhQToa8MFLYR` |
| aging-equipment-10yr | `qH0pcuQe4VeRUmiixt2h` |
| aging-equipment-15yr | `Oj6do72qMDb1C6w1JFKC` |
| spring-campaign | `oKFoyx0FOZ4VEp3PFOj5` |
| fall-campaign | `SfPsnK1SCG0EJoUJuoOr` |
| filter-reminder | `Ou2FTw7oy59NfR0I0NLX` |
| home-warranty | `6CiMdRmLCEIqJ3tqN1AV` |
| property-manager | `0QRXSA4GmaiDOH4WYyPI` |
| commercial-account | `4kwKhcHt1LDSOtptw31M` |
| new-construction | `jnvyAogKe5xDnQIIKeAc` |
| estimate-sent | `EPXsFrnpjYTA6g6W4l9T` |
| contract-signed | `Tp034ur5uAjQVL6sSMSQ` |
| install-complete | `0AIKCYzJEkjh0eCOEhJx` |
| review-requested | `4M41rToptAZ2P2bc509n` |
| review-received | `VyAjYyh8nrF43Ugt1Qp9` |
| referral | `aCwuyGEs6d79x5T1L2ut` |
| cold-lead | `pctICkAc7A2IYeZ4aZGY` |
| no-show | `rLEe1sYTbJqST98Wx4MH` |
| facebook-ad | `eGp8oE3gyxnQcA5aTfTa` |
| google-lsa | `JS2xIepl7jxnTgGZxaMb` |
| angi-lead | `ifB4UPlYr84exRj0kMwn` |
| repeat-customer | `h7CM8GPCEvkOwcRI85PM` |
| financing-offered | `ya6KPyqSJe8QvqcCeZO6` |

**Existing system tags (pre-build):** follow-up, high priority, warm lead

---

## PHASE 5: WORKFLOW SPECIFICATIONS

> **Note:** GHL Workflows cannot be created via API. All 18 workflows below are fully documented with triggers, timing, branching logic, and exact message copy. Build each workflow manually in GHL > Automations > Workflows using these specs.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — HVAC emergency or need to book a tune-up? Reply YES and we'll reach out right away 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Emergency Lead — Speed to Dispatch

**Trigger:** Contact tag (filter: tag added = emergency-call) OR Opportunity created (filter: Service Call pipeline, Stage: New Call, Job Type = Emergency Service)
**Goal:** Dispatch tech within 30 minutes, set expectations

**Step 1 (Immediate):** SMS to customer:
> "🚨 Emergency call received! [Company Name] is on it. Our dispatcher is assigning your call right now. You'll receive a tech ETA text within 15 minutes. — [Company Name]"

**Step 2 (Immediate — internal):** Email/SMS to dispatcher:
> "NEW EMERGENCY — [Contact Name] | [Phone] | [Address] | Issue: [Job Type note] | Time received: [timestamp]. Assign tech NOW."

**Step 3 (15 min — if stage still "New Call"):** Internal alert:
> "⚠️ UNASSIGNED EMERGENCY — [Contact Name] has been waiting 15 minutes. Assign immediately."

**Step 4:** When stage moved to "Dispatched" → trigger Workflow 3 (Dispatch Confirmation)

---

### Workflow 3: Emergency Dispatch Confirmation + ETA Text

**Trigger:** Pipeline stage changed (filter: new stage = Dispatched, HVAC - Service Call pipeline) + Contact tag (filter: tag added = emergency-call)
**Goal:** Confirm tech is coming, set ETA, reduce customer anxiety

**Step 1 (Immediate):** SMS to customer:
> "✅ Help is on the way! [Tech Name] is heading to [Address] now. ETA: approximately [X] minutes. If you need to reach them directly: [Tech Phone]. — [Company Name]"

**Summer variant (June–August, No AC):**
> "🌡️ We know how rough no A/C is in this heat! [Tech Name] is en route — ETA [X] min. Close your blinds, use fans, stay hydrated. Almost there! — [Company Name]"

**Winter variant (Nov–March, No Heat):**
> "❄️ No heat in this weather is a real emergency — we get it. [Tech Name] is on the way, ETA [X] minutes. Stay warm and we'll have you sorted soon! — [Company Name]"

**Step 2 (30 min before arrival):** SMS:
> "[Tech Name] is about 30 minutes out. Please make sure the equipment is accessible. — [Company Name]"

---

### Workflow 4: Tune-Up Appointment Confirmation (Immediate + 24hr + 2hr)

**Trigger:** Customer booked appointment (calendar: Tune-Up / Maintenance Appointment)
**Goal:** Confirm, reduce no-shows, set expectations

**Step 1 (Immediate — booking confirmation):** SMS:
> "✅ Confirmed! [Company Name] is scheduled for your HVAC tune-up on **[Date]** between **[Start Time]–[End Time]**. Tech: [Tech Name]. Questions? Reply here or call [Phone]. — [Company Name]"

**Step 1B (Immediate):** Email:
> **Subject:** "Your HVAC Tune-Up is Confirmed — [Date]"
> Body: Appointment details, what to expect (inspection checklist), tech bio/photo if available, "have your equipment accessible" reminder, company contact info.

**Step 2 (Day before at 4:00 PM):** SMS:
> "Reminder: [Company Name] arrives tomorrow between **[Time Window]** for your HVAC tune-up. Reply **CONFIRM** to lock it in, or **RESCHEDULE** if needed. — [Company Name]"

**Branch — Reply CONFIRM:**
- Move opportunity to "Confirmed" stage (if applicable)
- Internal note: confirmed
- No further action until day-of

**Branch — Reply RESCHEDULE:**
- SMS: "No problem! Click here to find a new time: [Self-Schedule Link]. We'll update your appointment right away. — [Company Name]"
- Apply tag: `no-show` (pending reschedule)
- Notify office

**Branch — No reply by 8:00 PM:**
- Auto-attempt call (voicemail if no answer)
- If voicemail: "Hi [Name], just confirming your HVAC tune-up tomorrow with [Company Name]. Call us at [Phone] if you need to reschedule. Thanks!"

**Step 3 (Day of appointment, 2 hours before):** SMS:
> "[Tech Name] is heading your way in about 2 hours for your HVAC tune-up! Please make sure the equipment area is clear and accessible. See you soon! — [Company Name]"

---

### Workflow 5: No-Show Recovery

**Trigger:** Appointment status (filter: no-show)
**Goal:** Recover the appointment, understand what happened

**Step 1 (30 min after no-show confirmed):** SMS:
> "Hi [First Name], it looks like we may have missed each other today for your HVAC appointment. Are you still looking to get this taken care of? Reply YES and we'll get you rescheduled right away. — [Company Name]"

**Step 2 (24 hours later — if no reply):** SMS:
> "No worries, [First Name] — life gets busy! We still have some availability this week. Book a new time here: [Booking Link]. — [Company Name]"

**Step 3 (3 days later — if still no action):** Email:
> **Subject:** "[First Name], we held a spot for you"
> Body: Soft re-engagement. "Your HVAC system still needs that tune-up — let's get it on the calendar before the busy season hits. Here's your booking link: [Link]"

**Step 4 (7 days — if no action):** Apply tag `cold-lead`. Enter cold lead re-engagement sequence (Workflow 18).

---

### Workflow 6: Post-Service Follow-Up + Review Request (Happy Path)

**Trigger:** Pipeline stage changed (filter: new stage = Work Complete, HVAC - Service Call pipeline)
**Goal:** Payment collection, review generation, MA upsell

**Step 1 (1 hour after stage change):** SMS — Payment:
> "Hi [First Name]! Your [Job Type] is complete — great work by [Tech Name] today! Invoice total: **$[Invoice Amount]**. Pay securely here: [Payment Link]. Thank you for choosing [Company Name]!"

**Step 2 (2 hours after stage change):** SMS — Review:
> "[First Name], how did [Tech Name] do today? Your review means everything to us and helps other families find trusted HVAC help. Takes 60 seconds: [Google Review Link] — [Company Name]"
- Apply tag: `review-requested`
- Update custom field: Review Requested = Yes

**Step 3 (24 hours — if equipment age ≥ 10 years based on Equipment Age field):** SMS:
> "Hi [First Name]! Quick note — your [Equipment Type] is [Equipment Age] years old. Units this age are approaching end-of-life. When you're ready to explore replacement options (we offer flexible financing), we're here. No pressure! — [Company Name]"
- Apply tag: `equipment-replacement-candidate`
- Update custom field: Equipment Replacement Candidate = Yes

**Step 4 (3 days — if no Maintenance Agreement tag):** SMS:
> "Did you know [Company Name] customers with a Comfort Club get priority service, 2 tune-ups/year, and 15% off all repairs? Starting at $149/year. Reply **PLAN** for details. — [Company Name]"

**Step 5 (7 days — if still no MA, no reply to Step 4):** Email:
> **Subject:** "The HVAC maintenance plan that pays for itself"
> Body: Full MA benefits breakdown with three tier pricing (Bronze $149/yr, Silver $199/yr, Gold $299/yr), sign-up link, one-click enrollment CTA.

**Step 6 (30 days):** Check-in SMS:
> "Hi [First Name]! Checking in — is everything running smoothly since your [Job Type]? Any questions or concerns, we're just a text away. — [Company Name]"

---

### Workflow 7: Unhappy Customer Recovery (Internal Alert, No Review)

**Trigger:** Contact tag (filter: tag added = callback-required)
**Goal:** Prevent negative public review, escalate to owner, resolve before customer vents online

**Step 1 (Immediate — internal):** Email to owner/manager:
> **Subject:** "⚠️ Customer Issue — Action Required: [Contact Name]"
> Body: Contact name, phone, address, job type, issue flag. "This customer had an unresolved concern. Call them before they post a review. Do NOT let this go to the automated review request workflow."

**Step 2 (Immediate — to customer):** SMS:
> "Hi [First Name], we want to make sure you're 100% satisfied. Did everything go as expected today? Reply YES or let us know what we can improve — we take every experience seriously. — [Company Name]"

**Step 3 (If customer replies with concern):** Internal alert to owner with message content.

**Step 4:** Do NOT trigger Workflow 6 (review request) for this contact on this job.

---

### Workflow 8: Maintenance Agreement Upsell (Post Service Call)

**Trigger:** Pipeline stage changed (filter: new stage = MA Upsell, HVAC - Service Call pipeline)
**Condition:** Contact does NOT have tag `maintenance-agreement`
**Goal:** Convert service call customers to recurring MA revenue

**Step 1 (Immediate):** SMS:
> "[First Name], glad we got your [Job Type] sorted! One thing — our Comfort Club members get 2 free tune-ups/year, priority scheduling, and 15% off every repair. Starting at just $149/year. Interested? Reply **PLAN** and I'll send the details. — [Company Name]"

**Step 2 (3 days — if no reply):** Email:
> **Subject:** "The plan that practically pays for itself — [Company Name] Comfort Club"
> Body: MA tiers with pricing, benefits breakdown, "customers on our plan save an average of $280/year," one-click enrollment link.

**Step 3 (7 days — if no reply):** SMS:
> "Still thinking about the Comfort Club? Here's a quick link: [MA Enrollment Link]. Locks in your 15% discount for life of membership. — [Company Name]"

**Step 4 (14 days — if no action):** Move opportunity to Closed. Apply tag `cold-lead`.

---

### Workflow 9: MA Renewal Sequence (60/30/14/7 Days Before Expiry)

**Trigger:** Custom date reminder (select MA Expiry Date field, set 60 days before)
**Goal:** Maximize renewal rate, make it frictionless

**Step 1 (60 days before expiry):** Email:
> **Subject:** "Your [Company Name] Comfort Club renews in 60 days"
> Body: "Hi [First Name]! Your Comfort Club membership is coming up for renewal on [MA Expiry Date]. This year, you received [X] tune-ups and saved approximately $[amount] with your member discount. Renew in one click: [Renewal Link]. Same great price: $[amount]/year."

**Step 2 (30 days before expiry):** SMS:
> "[First Name], your Comfort Club expires [MA Expiry Date]. Renew now to keep priority scheduling + your annual tune-ups: [Renewal Link]. Questions? Reply here. — [Company Name]"
- Apply tag: `ma-renewal-due`

**Step 3 (14 days before expiry):** Email:
> **Subject:** "Don't miss your renewal window — [Company Name]"
> Body: "Without your Comfort Club, service calls go back to full price and you lose priority scheduling. Renew now before your membership lapses: [Renewal Link]."

**Step 4 (7 days before expiry):** SMS — FINAL:
> "Last chance [First Name]! Comfort Club expires in 7 days. Renew in 30 seconds: [Renewal Link]. After expiry, new member pricing applies. — [Company Name]"

**Step 5 (Day of expiry — if NOT renewed):**
- Remove tag `maintenance-agreement`
- Apply tag `ma-renewal-due` → escalate to cold
- Move to "Cancelled" stage in MA pipeline
- Begin Lapsed MA re-enrollment: 30/60/90-day follow-up sequence

**Step 6 (If renewed at any point):**
- Remove tag `ma-renewal-due`
- Confirm tag `maintenance-agreement` active
- SMS: "You're all set! Comfort Club renewed through [New Expiry Date]. We'll be in touch to schedule your next seasonal tune-up. — [Company Name]"
- Update MA Expiry Date field to +1 year

---

### Workflow 10: Equipment Age Trigger — 10 Year

**Trigger:** Contact changed (filter: Equipment Age field updated to 10-15 years)
**Goal:** Begin replacement awareness education — soft sell

**Step 1 (Day 1):** Email:
> **Subject:** "Your [Equipment Type] is 10+ years old — here's what to know"
> Body: "Hi [First Name]! We noticed your [Equipment Type] is approaching the 10-year mark — great time to assess its health. The good news: it likely has several years left. The thing to watch: efficiency decline and upcoming repair costs. Modern systems are 30–50% more efficient, often paying for themselves in 5–8 years. No pressure — just want to keep you informed. Want a free efficiency assessment? Reply or book here: [Consultation Link]."

**Step 2 (Day 3):** SMS:
> "Hi [First Name]! Your [Equipment Type] is hitting the 10-year mark. Modern systems are 30–50% more efficient. Want a free consultation to see what a new system would save you? Reply YES. — [Company Name]"
- Apply tag: `aging-equipment-10yr`
- Update custom field: Equipment Replacement Candidate = Yes

**Step 3 (Day 14):** Email:
> **Subject:** "The real cost of running a 10-year-old HVAC system"
> Body: Cost comparison — old SEER 13 vs new SEER2 18. ROI calculation example. Financing options. CTA: "See our current replacement specials: [Link]."

**Step 4 (Day 30):** If no engagement → Move to cold. Revisit at age 12 years.

---

### Workflow 11: Equipment Age Trigger — 15 Year

**Trigger:** Contact changed (filter: Equipment Age field updated to 15+ years)
**Goal:** Urgency-based replacement campaign — protect customer before failure

**Step 1 (Day 1):** Email:
> **Subject:** "Your system is living on borrowed time — here's what to know"
> Body: "Hi [First Name]! Your [Equipment Type] is 15+ years old, which puts it past the average industry lifespan. At this age, failure rates increase significantly — especially heading into peak season. The risk: your system breaks down on the hottest day of July or the coldest night in January — when replacement wait times are 2–4 weeks. Replace on YOUR timeline, not when it breaks. We offer zero-pressure consultations and flexible financing. Book your free assessment: [Link]."

**Step 2 (Day 3):** SMS:
> "Heads up [First Name] — 15+ year old [Equipment Type] systems have a high failure rate heading into [Season]. Don't get caught without [AC/heat]. Let's talk options: [Booking Link]. — [Company Name]"
- Apply tag: `aging-equipment-15yr`
- Apply tag: `equipment-replacement-candidate`
- Update custom field: Equipment Replacement Candidate = Yes

**Step 3 (Day 7):** Email:
> **Subject:** "What happens when a 15-year-old HVAC system fails?"
> Body: Story-based messaging. Emergency replacement during peak season. Long wait times. Temporary hotel costs. "Planned replacement is always cheaper than emergency replacement." Financing options. Book now CTA.

**Step 4 (Day 21):** Final SMS:
> "[First Name], still running that 15-year-old [Equipment Type]? Summer is [X weeks] away. One free call is all it takes to know your options. Reply CALL and we'll reach out today. — [Company Name]"

---

### Workflow 12: R-22 Phase-Out Campaign

**Trigger:** Contact changed (filter: Refrigerant Type field updated to R-22) OR Contact tag (filter: tag added = r22-system)
**Goal:** Educate customer on cost risk, position replacement as financial protection

**Step 1 (Day 1):** Email:
> **Subject:** "Important: Your A/C uses R-22 refrigerant — here's what changed"
> Body: "Hi [First Name], we want to make sure you're aware of something important about your current air conditioning system. Your unit uses R-22 refrigerant (also called Freon), which was completely phased out of production in January 2020. This means R-22 is increasingly scarce — prices have risen to $100–$200+ per pound. A single refrigerant recharge can cost $800–$2,000 (vs. $200–$400 for modern refrigerant). Parts are becoming harder to source. In many cases, a new efficient system is the smarter financial choice. We offer free in-home consultations and flexible financing. Want to talk options? Reply or book here: [Consultation Link]."
- Apply tag: `r22-system`

**Step 2 (Day 5):** SMS:
> "[First Name], quick heads up — R-22 refrigerant for your A/C now costs $100-200/lb. One recharge = $800-$2,000+. A new system can often pay for itself vs. ongoing R-22 costs. Free consultation? [Booking Link] — [Company Name]"

**Step 3 (Day 14):** Email:
> **Subject:** "The math on your R-22 system"
> Body: Side-by-side cost comparison — staying with R-22 (repair costs, refrigerant costs over 3 years) vs. new system (energy savings, financing payment). ROI analysis. "In most cases, our customers save money switching." Urgency: "R-22 will only get more expensive."

**Step 4 (Day 30):** SMS — Final nudge:
> "[First Name], still on R-22? Prices went up again this year. When you're ready to run the numbers on a new system, we're here — no pressure. [Booking Link] — [Company Name]"

---

### Workflow 13: Spring AC Startup Campaign (Manual Trigger — April)

**Trigger:** Scheduler (fires April 1 annually, or manual launch)
**Target:** ALL contacts — MA-Active customers get different messaging than non-MA

**FOR CONTACTS WITH TAG `maintenance-agreement`:**

**Step 1 (April 1):** SMS:
> "Spring is here! ☀️ Time to schedule your annual A/C tune-up — it's included in your Comfort Club. Book before we fill up: [Tune-Up Booking Link] — [Company Name]"
- Apply tag: `spring-campaign`

**Step 1B (April 1):** Email:
> **Subject:** "Your spring A/C tune-up is included — time to book!"
> Body: What the spring cooling tune-up covers (coil cleaning, refrigerant check, capacitor test, thermostat calibration, filter inspection, blower check). "Your Comfort Club includes this service at no charge. Spots fill fast in spring — book yours now."

**Step 2 (April 15 — if no booking):** SMS:
> "[First Name], your spring A/C tune-up is still waiting! Slots are filling fast — lock yours in before the heat arrives: [Booking Link] — [Company Name]"

**FOR CONTACTS WITHOUT `maintenance-agreement` TAG:**

**Step 1 (April 1):** SMS:
> "Beat the summer rush! [Company Name] spring A/C tune-ups are booking fast. $149 for a full system inspection + cleaning. Book now: [Booking Link] — [Company Name]"

**Step 1B (April 1):** Email:
> **Subject:** "Don't wait until your A/C breaks on the hottest day of the year"
> Body: Tune-up benefits, spring pricing, MA upsell — "Get this tune-up FREE when you join our Comfort Club. Starting at $149/year."

**Step 2 (April 15 — if no booking):** SMS — MA focus:
> "[First Name], still need your spring tune-up? Join our Comfort Club and get it included FREE — plus priority service all year. [MA Link] — [Company Name]"

---

### Workflow 14: Fall Furnace Tune-Up Campaign (Manual Trigger — September)

**Trigger:** Scheduler (fires September 5 annually, or manual launch)
**Target:** ALL contacts — same MA/non-MA split as Workflow 13

**FOR CONTACTS WITH TAG `maintenance-agreement`:**

**Step 1 (Sept 5):** SMS:
> "Fall is coming — time for your annual heating tune-up! ❄️ Your Comfort Club includes this. Book before slots fill: [Booking Link] — [Company Name]"

**Step 1B (Sept 5):** Email:
> **Subject:** "Don't get caught without heat this winter — book your tune-up now"
> Body: What the fall heating tune-up covers (heat exchanger inspection, flue gas check, gas pressure, burner cleaning for furnaces; refrigerant check, defrost cycle, reversing valve for heat pumps). "Book now before October rush."

**Step 2 (Sept 20 — if no booking):** SMS:
> "[First Name], fall furnace tune-up still available — but spots are going fast. Lock yours in: [Booking Link] — [Company Name]"

**FOR CONTACTS WITHOUT `maintenance-agreement` TAG:**

**Step 1 (Sept 5):** SMS:
> "Fall furnace tune-up: $149. Keep your family warm all winter. Book before October rush: [Booking Link] — [Company Name]"

**Step 1B (Sept 5):** Email:
> **Subject:** "Is your furnace ready for winter? Book your tune-up now."
> Body: What happens when a furnace breaks down in January. Tune-up benefits. Pricing. MA upsell — "Get this tune-up FREE with Comfort Club — 2 tune-ups + 15% off repairs from $199/year."

---

### Workflow 15: Filter Replacement Reminder (Every 90 Days)

**Trigger:** Scheduler (fires every 85-90 days from last filter reminder date)
**Target:** All contacts with tag `filter-reminder`
**Goal:** Top-of-mind, system care, potential upsell visit

**Step 1 (Every 90 days):** SMS:
> "Quick heads up [First Name] — time to change your air filter! 🔧 A clean filter = better air quality, lower energy bills, and longer equipment life. Grab a [Filter Size] at any hardware store. Need a hand? Reply HELP. — [Company Name]"

**Variation for 1-month filters (contacts tagged `filter-1month`):**
- Send every 28 days
- SMS: "Monthly filter reminder! Time to swap out your 1" filter. Stay on top of it and your system will thank you. — [Company Name]"

**Variation for 6-month filters:**
- Send every 175 days
- Email with full seasonal system tips

---

### Workflow 16: Financing Awareness (Estimate Sent 5+ Days, No Decision)

**Trigger:** Stale opportunities (filter: stage = Proposal Sent, Equipment Replacement pipeline, no movement for 5+ days)
**Goal:** Remove financing as a barrier to closing

**Step 1 (Day 5 after proposal):** SMS:
> "[First Name], just checking in on the replacement proposal we sent. Is cost or financing holding things up? We work with lenders who offer 0% for 12 months on systems like yours. Happy to walk through your options — no commitment needed. Reply or call [Phone]. — [Company Name]"
- Apply tag: `financing-offered`
- Update custom field: Equipment Amount (if not already set)

**Step 2 (Day 8):** Email:
> **Subject:** "Flexible payment options for your new HVAC system"
> Body: Financing details — "As low as $X/month for 12 months with approved credit." Monthly payment calculator example. "Don't let cost delay your family's comfort — let's find a payment that works for you." Financing application link.

**Step 3 (Day 12):** SMS — Final:
> "[First Name], your replacement proposal is still open. Financing options are available if budget is a concern. Would a quick 10-minute call help? Reply CALL. — [Company Name]"

**Step 4 (Day 21 — no movement):** Move to "Closed - Lost" tentatively. Apply tag `cold-lead`. Schedule 90-day follow-up.

---

### Workflow 17: Commercial PM Outreach Sequence

**Trigger:** Contact tag (filter: tag added = property-manager or commercial-account)
**Goal:** Book property audit, convert to PM contract

**Step 1 (Day 1):** Email:
> **Subject:** "Cut HVAC headaches in half — how we work with property managers"
> Body: Property manager pain points (after-hours tenant calls, emergency replacement costs, unit-by-unit chaos). Offer: Free property HVAC audit — walk every unit, document equipment age, tonnage, refrigerant type, condition. "No obligation, no pressure — just real intel on your equipment portfolio." CTA: "Schedule your free property audit: [Commercial Assessment Booking Link]"

**Step 2 (Day 3 — if no reply):** SMS:
> "Hi [PM Name], sent you an email about our property HVAC program. Do you handle HVAC for your properties? Would love 10 minutes to talk. — [Company Name]"

**Step 3 (Day 7 — if no reply):** Phone call attempt. If voicemail:
> "Hi [Name], this is [Rep] from [Company Name]. We work with property managers in [City] on commercial HVAC maintenance and emergency response. I'd love 10 minutes to show you how we can reduce after-hours calls and emergency repair costs. Call me back at [Phone]. Thanks!"

**Step 4 (Day 14 — if no reply):** Email:
> **Subject:** "What other property managers in [City] are doing differently"
> Body: Social proof — "We manage HVAC for X properties in [City]. Here's what changed for our clients..." Testimonial or case study. Seasonal PM contract value proposition. Book audit CTA.

**Step 5 (Day 30 — if still no engagement):** Final SMS:
> "[PM Name], last reach-out — we specialize in commercial HVAC PM in [City]. If the timing is ever right for a chat, we're here: [Phone]. — [Company Name]"
- Apply tag `cold-lead`

**Ongoing (For Active Commercial PM Clients):**
- Monthly email: Equipment status summary
- Quarterly: PM scheduling reminder
- Annual: Contract renewal proposal with updated pricing

---

### Workflow 18: 30-Day Cold Lead Re-Engagement

**Trigger:** Contact tag (filter: tag added = cold-lead)
**Goal:** One final attempt to re-engage before archiving

**Condition:** Wait 30 days from tag applied

**Step 1 (Day 30):** SMS:
> "Hi [First Name]! It's been a while — [Company Name] checking in. Still need HVAC service or a system assessment? We're booking quickly for [current season]. [Booking Link] — [Company Name]"

**Step 2 (Day 37 — if no reply):** Email:
> **Subject:** "[First Name], one last note from [Company Name]"
> Body: Soft close. "We don't want to bother you — just want to make sure you're taken care of. If you ever need HVAC service, a tune-up, or a replacement quote, we're here. Here's our booking link when you're ready: [Link]. We'll stop reaching out unless you reach back — no worries either way."

**Step 3:** If no engagement after email → archive contact, remove from active sequences. Keep in GHL with `cold-lead` tag for future re-activation campaigns.

---

## BUILD NOTES & MANUAL CONFIGURATION REQUIRED

### Calendar Availability Windows (Configure in GHL UI)
After build, set these in GHL → Settings → Calendars:

| Calendar | Days | Hours |
|---|---|---|
| Emergency HVAC Service | Mon-Sun | 7:00 AM – 9:00 PM |
| Tune-Up / Maintenance Appointment | Mon-Sat | 8:00 AM – 5:00 PM |
| Equipment Replacement Consultation | Mon-Fri | 8:00 AM – 5:00 PM |
| Commercial Site Assessment | Mon-Fri | 8:00 AM – 4:00 PM |

### Technician Assignment
- Add technicians as GHL users
- Link technicians to calendars for round-robin or assigned dispatch
- Create internal SMS notification number for on-call tech alerts

### Smart Lists to Build (GHL > Contacts > Smart Lists)
Create these smart lists for campaign targeting:
1. **MA-Active** — Tag = `maintenance-agreement`
2. **MA-Renewal-Due-30** — MA Expiry Date within 30 days
3. **R-22 Units** — Tag = `r22-system`
4. **Aging Equipment 10+** — Tag = `aging-equipment-10yr` OR `aging-equipment-15yr`
5. **Equipment Replacement Hot** — Tag = `equipment-replacement-candidate` + no `contract-signed`
6. **Cold Leads** — Tag = `cold-lead`
7. **Non-MA Customers** — No tag `maintenance-agreement`
8. **Commercial Accounts** — Tag = `commercial-account` OR `property-manager`

### Dashboard Widgets to Configure
Build these in GHL → Reporting → Dashboards:
1. Active MA Count (contacts with `maintenance-agreement` tag)
2. MA Renewals Due - 30 Days
3. MA Renewals Due - 60 Days
4. Lapsed MAs - Last 90 Days
5. Opportunities by Pipeline (all 5 pipelines)
6. Revenue by Stage (Equipment Replacement pipeline)
7. Lead Source Attribution (from custom field)
8. Review Count + Rating

---

## IMPORTANT: DEFAULT "MARKETING PIPELINE" NOTE

The sub-account was provisioned with a default "Marketing Pipeline" (ID: `vMF48z5DCEgXkWQ0lGoA`). This can be archived or kept as a general intake pipeline. All HVAC-specific work should flow into the 5 dedicated HVAC pipelines above.

---

## COMPLIANCE NOTES

- All SMS messages require written consent collection at opt-in (web form or booking)
- CASL (Canada) and TCPA (US) require explicit opt-in before SMS — confirm client is collecting properly
- No financial product language in scheduling tool names or calendar descriptions
- Review request workflows must segment by job outcome (positive only)
- All phone numbers for SMS should be verified in GHL > Settings > Phone Numbers

---

*Build log generated by Maximus AI — 1app HVAC Snapshot*
*Location: 9PZ17iQFwEDlNdsYpSjr | Build date: 2026-07-21*
