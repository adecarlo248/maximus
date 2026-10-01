# Flooring GHL Snapshot — Build Log
**Location ID:** uMNi57hdsyDbrI5XhcYp  
**Build Date:** 2026-07-21  
**Built By:** Maximus (Subagent)  
**Status:** Phase 1–4 Complete | Phase 5 (Workflows) Documented  
**Pipelines:** Created via REST API (2026-07-21) — API limitation workaround successful  

---

## PHASE 1: CUSTOM FIELDS — ✅ COMPLETE (20/20)

All fields created on `contact` model unless noted.

| # | Field Name | Type | Field Key | GHL ID |
|---|---|---|---|---|
| 1 | Lead Source | SINGLE_OPTIONS | contact.lead_source | tgsn4UeBA6M8FpZO16tD |
| 2 | Job Type | SINGLE_OPTIONS | contact.job_type | 6wLs44Qi8HL1e5X4MJ4m |
| 3 | Service Category | SINGLE_OPTIONS | contact.service_category | v07gpTdudFOuPCLP2Er6 |
| 4 | Property Type | SINGLE_OPTIONS | contact.property_type | nqzv6pUuvXvi2obhWhxC |
| 5 | Flooring Material | SINGLE_OPTIONS | contact.flooring_material | UGSRes4ynSLIhEyRFPGR |
| 6 | Estimated Square Footage | NUMERICAL | contact.estimated_square_footage | XDnzH2HkIUFH6GZ2ISlr |
| 7 | Sample Approved | RADIO (Yes/No) | contact.sample_approved | uIaOq31kuz3KDL1z6n0u |
| 8 | Sample Approval Date | DATE | contact.sample_approval_date | 2OiRhd2DxVYUyysdI4Pb |
| 9 | Subfloor Condition | SINGLE_OPTIONS | contact.subfloor_condition | XXGkjU5aMQ46XQ08uo22 |
| 10 | Insurance Claim | RADIO (Yes/No) | contact.insurance_claim | 3IIaZD20UHwUFOlQNVtb |
| 11 | Insurance Company | TEXT | contact.insurance_company | ZjvSjsfGhfnf5KlyR3Mq |
| 12 | Claim Number | TEXT | contact.claim_number | JzYFvrwoLQdgh7CXtMBb |
| 13 | Estimate Amount | MONETORY | contact.estimate_amount | 9VVUsk2dMcubxJGAntvK |
| 14 | Contract Amount | MONETORY | contact.contract_amount | Ahg8qBBQu4jYAiBzVckW |
| 15 | Deposit Paid | RADIO (Yes/No) | contact.deposit_paid | kjMhP7SxD5umsg3mn7GQ |
| 16 | Material Lead Time | SINGLE_OPTIONS | contact.material_lead_time | B5CEB8r3YYuoMA3GEqFh |
| 17 | Install Date | DATE | contact.install_date | t3W9mJ3aXKH6ZvQyhQuG |
| 18 | Review Requested | RADIO (Yes/No) | contact.review_requested | aufxCgrvaq9RfoHOaXsp |
| 19 | Review Received | RADIO (Yes/No) | contact.review_received | VN45zYrhdaaMeoZKSBl8 |
| 20 | Neighbour Campaign Sent | RADIO (Yes/No) | contact.neighbour_campaign_sent | mR5t14KCqWUCkMpGL6V3 |

### Field Option Values

**Lead Source options:** Google LSA, Google Organic, Referral, Real Estate Agent, Property Manager, Insurance Adjuster, Houzz, Kijiji/Craigslist, Facebook Ad, Repeat Customer

**Job Type options:** Hardwood Install, LVP/Laminate Install, Tile Install, Carpet Install, Hardwood Refinishing, Subfloor Repair, Area Rug, Water Damage Replacement, Commercial Flooring, Stair Nosing/Transitions

**Service Category options:** Residential Install, Refinishing/Restoration, Commercial, Insurance/Water Damage

**Property Type options:** Residential, Commercial, Multi-Unit/Rental, Strata/Condo, New Construction

**Flooring Material options:** Hardwood, LVP/Luxury Vinyl, Laminate, Tile/Stone, Carpet, Cork, Bamboo, Polished Concrete, Unknown

**Subfloor Condition options:** Good, Needs Minor Repair, Needs Major Repair, Unknown

**Material Lead Time options:** In Stock, 1-2 weeks, 2-4 weeks, 4+ weeks, Unknown

---

## PHASE 2: PIPELINES — ✅ COMPLETE (4/4)

**Created via GHL REST API on 2026-07-21**

### PIPELINE 1: Flooring - Residential Install
**Pipeline ID:** `tr4vS2r660MtuokwiaAV`  
**Use:** Hardwood, LVP, Laminate, Carpet, Tile residential installs

| Position | Stage Name | Stage ID |
|---|---|---|
| 0 | New Lead | 7f9fe6b8-460b-4229-a710-b9f627fd3837 |
| 1 | Measure Appointment Scheduled | c07f8b99-2386-4b41-b55f-63d5208ae827 |
| 2 | Measure Complete | 947d3d7e-cdfc-4e7b-82d2-d7cceb1d85e4 |
| 3 | Sample Selection | 62e8d247-ddec-4503-afc4-eb15425e69eb |
| 4 | Sample Approved | 9b90a208-4987-4478-a482-18f62cac6f73 |
| 5 | Proposal Sent | 81424f47-bb84-4bb3-84fd-af870030908f |
| 6 | Follow-Up Active | 4e63bb7e-7514-4250-9d51-d439299dcd7e |
| 7 | Contract Signed / Deposit | 3d5ea1f5-2452-4885-b0f7-803d35cb234c |
| 8 | Material Ordered | ba534e2d-f987-43c8-b072-c47216d81607 |
| 9 | Install Scheduled | 4eb2e7c1-a53f-49c1-bf0a-c18a7108ac92 |
| 10 | Subfloor Prep | aa5ed58d-6740-4b08-90e8-6e5799b72192 |
| 11 | Install In Progress | b0d474b3-1870-48f1-b9bd-7cf8f5ecd765 |
| 12 | Transitions/Finishing | 00a75751-131e-4739-ba15-2badcde6e8e0 |
| 13 | Job Complete | 39f174f7-5f72-4e02-86a5-2d01f7ea8d02 |
| 14 | Invoice Sent | ffd523aa-2c71-4e01-b483-4d7454a96607 |
| 15 | Paid | 556499d0-3ede-44f5-a1bf-950da428fc20 |
| 16 | Review Requested | 867d90a7-8aca-4b6b-a153-fc76b01e90cd |
| 17 | Neighbour Campaign | 7124e028-1dd0-4e7d-a027-3ff4dc646cd2 |

---

### PIPELINE 2: Flooring - Refinishing & Restoration
**Pipeline ID:** `wpVsWUitSyeHlCfKM1Sl`  
**Use:** Sand & finish, screen & recoat, buff & coat for existing hardwood

| Position | Stage Name | Stage ID |
|---|---|---|
| 0 | New Lead | 052722a3-7479-4199-a7f2-372448402395 |
| 1 | Estimate Scheduled | 4a89e310-42bc-48d9-9643-57bbe13c7c00 |
| 2 | Estimate Complete | bb00c505-d697-4dac-a27e-923669af92d8 |
| 3 | Proposal Sent | 8931efff-5f52-4dcc-8e5e-c9b5a2a36f04 |
| 4 | Follow-Up Active | 1d320320-1efb-4c37-969d-1b55541e2eb0 |
| 5 | Contract Signed | a9dbf34b-7c87-46bb-b8cd-1454cb4f6e6c |
| 6 | Job Scheduled | 03c0f506-3977-4c91-ba6b-8a2e5a6db597 |
| 7 | Sanding | 15c6f2b1-2ee6-45d5-8493-c92c4a26d4a3 |
| 8 | Staining/Coating | c904916a-dd97-45b5-a4db-ea63415b0151 |
| 9 | Final Coat | a9da930a-ba06-4f8e-b052-faca753b2185 |
| 10 | Job Complete | e4721664-e2dd-4f65-9530-a7c6ba8144db |
| 11 | Invoice Sent | fd12e6c2-2714-4849-af14-f9e14300be66 |
| 12 | Paid | 806ed622-9b4f-4d5c-8603-d51721935fc8 |
| 13 | Review + Referral | caa59439-20da-4c2f-ae9a-4af2344d2a64 |

---

### PIPELINE 3: Flooring - Commercial / Property Manager
**Pipeline ID:** `HYBimQbL6j3GB1liEK5h`  
**Use:** Commercial offices, retail, multi-unit, property management

| Position | Stage Name | Stage ID |
|---|---|---|
| 0 | New Prospect | bc26a7ab-7a35-4890-9e0a-18269580f936 |
| 1 | Site Measure | 8c218142-bb06-4f25-90cd-4e1a3d089128 |
| 2 | Proposal Submitted | 9d181dc5-c135-4ea8-9504-68722b2d289a |
| 3 | Contract Awarded | 372a10a2-4502-48a4-b59e-f8c599ae3cb3 |
| 4 | Material Ordered | 95440e7e-3f36-440a-9a2d-c48e712741da |
| 5 | Install Scheduled | 20a126a5-3352-476a-a771-6898d7293baf |
| 6 | Install In Progress | dca8785e-e859-4a3d-ac02-7a74a2219504 |
| 7 | Job Complete | c7331792-d8ab-4c28-a61d-5027baa6cce9 |
| 8 | Invoice Sent | 740d1dcd-6f9e-42c7-bd09-869452940446 |
| 9 | Paid | fb95251d-8433-432b-8443-a0f1097a6405 |
| 10 | Warranty Period | 680b2adf-2c15-469d-883a-90acf19c1fb2 |
| 11 | Renewal | 60f348d2-b1a7-450e-83d7-ecb09a011f4b |

---

### PIPELINE 4: Flooring - Insurance / Water Damage
**Pipeline ID:** `b6dWv1UtuFNyrLT9vWo1`  
**Use:** Insurance-funded floor replacement, water damage claims

| Position | Stage Name | Stage ID |
|---|---|---|
| 0 | Claim Received | cf89ddf3-106e-4a8d-b27a-95fa4ad5b7fa |
| 1 | Emergency Assessment | 6a101bbd-be01-45d3-99ef-5f54b36cfd00 |
| 2 | Scope Approved | 2dde624b-7e66-45af-bc20-70968d81cc28 |
| 3 | Material Selected | f4b315f1-74cb-46d5-bbe7-eeac5e9ab4ea |
| 4 | Install Scheduled | c564a926-11b9-4a63-875b-2dea035aaa95 |
| 5 | Install Complete | 693b9cd1-25a4-4a4a-82e8-3a37d7577082 |
| 6 | Invoice to Insurance | e70eb3d2-7b30-45bb-b787-6ed2cb674768 |
| 7 | Supplement Filed | 5e0835f4-9286-4b59-95b2-ba02363cf5a6 |
| 8 | Final Payment | 7955b8ae-1da3-4386-bdf6-0903466e4242 |
| 9 | Review + Referral | ef81401d-03ca-4977-ba7d-1a2858767fe9 |

---

## PHASE 3: CALENDARS — ✅ COMPLETE (3/3)

| Calendar Name | Duration | Hours | Calendar ID |
|---|---|---|---|
| In-Home Measure - Flooring | 60 min | Mon-Fri 9am-5pm | 0I5k0S72fNmX4v9b1kZ8 |
| Commercial Site Measure | 90 min | Mon-Fri 8am-4pm | Px8egOu2W5kZHfbh37Zl |
| Refinishing Estimate | 45 min | Mon-Fri 8am-5pm | z1qmzzo8pgi156LeqVva |

**Settings applied to all calendars:**
- Buffer after appointment: 30 min (travel time)
- Minimum booking notice: 24 hours
- Booking window: 60 days out
- Rescheduling: Enabled
- Cancellation: Enabled
- Auto-confirm: Yes

---

## PHASE 4: TAGS — ✅ COMPLETE (31/31)

All tags created successfully:

| Tag | Tag | Tag |
|---|---|---|
| new-lead | sample-pending | real-estate-agent |
| hardwood-install | sample-approved | property-manager |
| lvp-laminate | material-on-order | insurance-adjuster |
| tile-install | estimate-sent | cold-lead |
| carpet-install | deposit-paid | no-show |
| refinishing | contract-signed | google-lsa |
| subfloor-repair | job-complete | houzz-lead |
| water-damage | review-requested | facebook-ad |
| commercial-flooring | review-received | repeat-customer |
| insurance-claim | referral | supplement-filed |
| neighbour-campaign | | |

---

## PHASE 5: WORKFLOWS — 📋 DOCUMENTED (API LIMITATION)

**GHL API limitation:** Workflow creation is not available via the GHL public API. All workflows must be built manually in the GHL UI under **Automation → Workflows**. Full specs below for manual build.

---

### ✅ MISSED CALL TEXT BACK — NATIVE GHL SETTING (Not a Workflow)

**Do NOT build this as a workflow.** Use GHL's built-in MCTB feature instead.

**How to enable:**
1. Go to **Settings → Phone Numbers**
2. Click on your phone number
3. Click the **"Voicemail & Missed Call TextBack"** tab
4. Check **"Enable Missed call textback"** ✅
5. Click **"Customize"** and paste the message below

**Customized message for this trade:**
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — looking for a free flooring estimate or measure? Reply YES and we'll reach out right away 👋"

This fires automatically on every missed call. No workflow required.

---

### WF-001: New Lead — Speed to Response
**Trigger:** Contact created (from web form, Facebook Lead Ad, or Google LSA)
**Tags to apply:** new-lead  
**Pipeline:** Move to Pipeline 1 Stage 1 (New Lead)

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Immediate | SMS | "Hey {{contact.first_name}}! This is [Rep Name] from [Company]. You just reached out about flooring — I'd love to get you taken care of. Are you available for a quick call? 🏠" |
| 2 | 5 min | Internal Task | "Call new lead: {{contact.first_name}} {{contact.last_name}} — {{contact.phone}}" |
| 3 | 15 min | Email | Subject: "Your free flooring measure is waiting" — introduce company, link to booking calendar (In-Home Measure - Flooring) |
| 4 | 1 hr | SMS | "Still here when you're ready, {{contact.first_name}}. Click here to grab a time for your free in-home measure: [CALENDAR LINK]" |
| 5 | Day 1 PM | SMS | "Quick note — we offer free in-home measures with zero obligation. What flooring are you thinking about?" |

**Exit trigger:** Contact replies OR books appointment → remove from workflow

---

### WF-002: Measure Appointment Confirmation
**Trigger:** Pipeline stage changed (filter: new stage = Measure Appointment Scheduled)  
**Tags to apply:** (none additional — stage tracks this)

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Immediate | SMS | "Locked in! Your free flooring measure is set for {{appointment.start_time}}. We'll call 15 min before arrival. Questions? Text anytime." |
| 2 | Immediate | Email | Subject: "Your measure appointment is confirmed" — Confirmation details, estimator name, what to prepare (clear room access, note any subfloor history) |
| 3 | Day before (9am) | Email | "See you tomorrow!" — prep tips: clear furniture access, note any previous moisture issues or squeaky areas |
| 4 | Day before (5pm) | SMS | "Reminder: your flooring measure is tomorrow at [time]. [Estimator] will call 15 min before arrival. Looking forward to it." |
| 5 | Day of (2 hrs before) | SMS | "Today's the day! [Estimator] is heading your way around [time]. They'll text when 15 min out." |

---

### WF-003: No-Show Recovery
**Trigger:** Appointment status (filter: no-show)
**Tags to apply:** no-show

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Same day | SMS | "Hey {{contact.first_name}}, looks like we missed each other today! No worries — let's find another time. [CALENDAR LINK]" |
| 2 | Next day | Email | "We missed you — would you like to reschedule?" — include booking link |
| 3 | Day 3 | SMS | "Still want to get that free flooring measure done? We have availability this week. [CALENDAR LINK]" |
| 4 | Day 7 | SMS | "Last check-in — if you're still thinking about flooring, we'd love to help. No pressure. [CALENDAR LINK]" |

---

### WF-004: Sample Approval Follow-Up
**Trigger:** Pipeline stage changed (filter: new stage = Sample Selection)
**Tags to apply:** sample-pending

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Day of delivery | SMS | "Your [product name] sample has been dropped off! Try it in different rooms and different lighting. What's your gut reaction? 🪵" |
| 2 | Day 1 | SMS | "How's the flooring looking in your space, {{contact.first_name}}? Remember to try it next to your cabinets or trim — that's where it really tells the story." |
| 3 | Day 2 | Email | Subject: "How to evaluate your flooring sample" — tips: lighting at different times of day, compare to trim/cabinets, check grain direction, photo side-by-side |
| 4 | Day 3 | SMS | "Loving it, hating it, or somewhere in between? No pressure — if it's not right, we have 40+ options at your price point. Happy to swap." |
| 5 | Day 5 | SMS | "Last check-in on the sample — ready to move forward, want a different option, or want to come into our showroom? Just reply and we'll handle it. 😊" |

**Branch responses:**
- "Love it / Yes" → Move to "Sample Approved" → Apply tag: sample-approved → Remove tag: sample-pending
- "Not sure / want options" → Internal task: "Send alternative samples to {{contact.first_name}}" → Restart workflow
- No response by Day 7 → Apply tag: cold-lead → Internal alert to rep

---

### WF-005: Estimate Follow-Up Sequence (5-Step, 21 Days)
**Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent)
**Tags to apply:** estimate-sent

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | 1 hr after | SMS | "Your flooring estimate just hit your inbox! Let me know if you have questions or want to go over anything, {{contact.first_name}}." |
| 2 | Day 2 | Email | Subject: "How to read your flooring estimate" — breakdown of what's included: materials, labour, removal, underlayment, transitions |
| 3 | Day 3 | SMS | "Quick check-in — have you had a chance to look over your estimate? Happy to answer any questions." |
| 4 | Day 5 | Email | Subject: "Flooring options at your price point" — hardwood vs. LVP vs. laminate comparison at their quoted tier |
| 5 | Day 7 | SMS | "Still thinking it over? A few things worth knowing: [product] typically ships in 3–4 weeks. Happy to hold your spot if you're leaning toward proceeding." |
| 6 | Day 9 | Email | Subject: "Common questions before booking your flooring project" — FAQ: How long does install take? Do I need to move furniture? What about pets? |
| 7 | Day 10 | SMS | "Last touch for now — if the timing doesn't work right now, no problem. I'll check back in a few weeks. Or reply READY and we'll get you on the schedule. 👍" |
| 8 | Day 14 | Email | Subject: "Still interested in the flooring? Pricing valid through [date]" |
| 9 | Day 21 | SMS | "Hey {{contact.first_name}}, it's [Rep] from [Company]. It's been a few weeks — still thinking about the flooring project? Happy to revisit." |

**Exit trigger:** Any positive response, stage change, or deposit taken → exit sequence

---

### WF-006: Material Lead Time Update
**Trigger:** Pipeline stage changed (filter: new stage = Material Ordered) OR Contact tag (filter: tag added = material-on-order)

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Immediate | SMS | "Great news — your flooring order is placed! Expected arrival: [lead time]. We'll text you the moment it's in. Any questions in the meantime?" |
| 2 | Day 3 | Email | "While your flooring is on its way..." — prep guide: clearing the space, what to do with baseboards, pet/furniture planning |
| 3 | On material arrival (manual trigger) | SMS | "Great news — your flooring is in! Ready to schedule your install? Here are the next available dates: [dates or booking link]" |
| 4 | On material arrival | Email | "Your flooring has arrived!" — install prep checklist, what to expect on install day |

---

### WF-007: Install Day Notification
**Trigger:** Pipeline stage changed (filter: new stage = Install Scheduled)

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | 7 days before | Email | "Your install is coming up! Here's how to prepare:" — furniture removal, clear pathways, pets, baseboard removal note, parking for crew |
| 2 | 3 days before | SMS | "3 days until install day! Quick reminder: [prep items]. Any questions before the crew arrives?" |
| 3 | Day before (9am) | Email | Full install day guide: arrival window, crew size, noise/dust expectations, daily progress timeline |
| 4 | Day before (5pm) | SMS | "Tomorrow's the big day! The crew will arrive between [window]. We'll call 30 min before. See you then!" |
| 5 | Morning of (7am) | SMS | "Good morning! The [Company] crew is on their way. Arrival estimate: [time]. Excited for you to see the transformation! 🏠" |

---

### WF-008: Post-Install Review Request + Neighbour Campaign
**Trigger:** Pipeline stage changed (filter: new stage = Job Complete)
**Tags to apply:** job-complete, review-requested

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | 1 hr after | SMS | "The floors look amazing! 😍 If you're happy with how it turned out, a quick Google review means the world to a local business: [GOOGLE REVIEW LINK]" |
| 2 | Day 1 | Email | Subject: "Your flooring journey is complete!" — summary of work, care & maintenance guide for [product type], warranty info, review request |
| 3 | Day 3 | SMS | "Still thinking about leaving a review? It only takes 2 minutes: [GOOGLE REVIEW LINK]" |
| 4 | Day 2 | Internal Task | "Drop 10 door hangers on [street] near [address] — job just completed. Neighbour campaign." |
| 5 | Day 2 | SMS | "Quick favour — did any of your neighbours mention they liked the floors? If they're interested, we'd take great care of them. Feel free to share my number!" |
| 6 | Day 7 | Email | "3-month care tips for your new [LVP/hardwood/tile] floors" — establishes ongoing relationship, soft referral ask |
| 7 | Day 7 | SMS | "Hey {{contact.first_name}}! If any neighbours mention they like your new floors — send them our way! We have a referral program: [REFERRAL LINK]" |

**On review received:** Apply tag: review-received → Remove tag: review-requested → Stop review request loop

---

### WF-009: Unhappy Customer Recovery
**Trigger:** Contact tag (filter: tag added = unhappy-customer)  
**This workflow sends INTERNAL ALERTS ONLY — no customer-facing messages**

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Immediate | Email to Owner | ALERT: "Customer complaint flagged for {{contact.first_name}} {{contact.last_name}} — {{contact.phone}}. Immediate follow-up required." |
| 2 | Immediate | Internal Task | "PRIORITY: Call {{contact.first_name}} within 30 minutes re: complaint. See contact notes." |
| 3 | 1 hr | Internal Task | "Has complaint been addressed? Update contact notes and remove unhappy-customer tag when resolved." |

---

### WF-010: Insurance Claim Fast-Track
**Trigger:** Contact changed (filter: Insurance Claim field updated to Yes) OR Contact tag (filter: tag added = insurance-claim)
**Pipeline:** Move to Pipeline 4 (Insurance / Water Damage)

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Immediate | SMS | "Hi {{contact.first_name}}, this is [Rep] from [Company]. I understand you're dealing with water damage — we work with insurance claims regularly and can have someone out to assess within 24 hours. Are you available tomorrow morning or afternoon?" |
| 2 | Immediate | Email | Subject: "Emergency Flooring Replacement — What to Expect" — calm guide to insurance claim process, what adjuster does, our role, timeline expectations |
| 3 | Immediate | Internal Task | "PRIORITY: Emergency assessment for {{contact.first_name}} at {{contact.address}}. Call within 30 minutes." |
| 4 | Day 3 | SMS | "Quick update on your claim at [address]: We submitted the estimate to [insurance company] on [date]. We'll notify you the moment we hear back. Any questions?" |
| 5 | Day 6 | SMS | "Checking in — no news yet from [insurer]. We're following up on our end. Typical approval time is 5–10 business days from submission." |
| 6 | On approval (manual) | SMS | "Great news — your insurance approved the scope! We're ready to get started. When works for a quick call to review next steps?" |

---

### WF-011: Real Estate Agent Referral Nurture
**Trigger:** Contact tag (filter: tag added = real-estate-agent)  

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Immediate | SMS | "[First Name], thanks for connecting! We specialize in pre-listing flooring refreshes — fast turnaround, clean work, and agent-priority scheduling. Do you have a listing coming up where the floors need attention?" |
| 2 | Day 3 | Email | Subject: "Why flooring is the highest-ROI pre-listing upgrade" — stat-backed: 150-200% ROI, avg $2K-$8K job value |
| 3 | Week 2 | SMS | "Working on any listings where the floors need attention? LVP installs in 1–2 days for smaller spaces — perfect for tight listing timelines." |
| 4 | Week 3 | Email | Subject: "Before & after: pre-listing flooring transformations" — photo gallery |
| 5 | Week 4 | SMS | "We prioritize agent referrals for fast turnaround. Most pre-listing jobs completed in 5–10 business days." |
| 6 | Month 2 | Email | Subject: "Our agent referral program" — referral incentive details |

**On first referral job won:** Apply tag: repeat-customer → Send thank-you SMS to agent → Monthly newsletter signup

---

### WF-012: Property Manager Account Outreach
**Trigger:** Contact tag (filter: tag added = property-manager)

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Immediate | SMS | "Hi [First Name], this is [Rep] from [Company]. We specialize in flooring for rental properties and multi-unit buildings — quick turnaround, minimal disruption to tenants. Do you have any units coming up for flooring?" |
| 2 | Day 2 | Email | Subject: "Commercial flooring built for property managers" — durability, fast booking, invoice-ready documentation |
| 3 | After first job | SMS | "Thanks for the job at [Property]. Our crew is in and out efficiently — great for occupied buildings. Happy to quote your next unit or building anytime." |
| 4 | Monthly | Email | "Available install windows for the month" + "Unit turnover flooring specials" |

---

### WF-013: Seasonal Campaign — Spring Renovation Push
**Trigger:** Scheduler (April 1 each year)
**Target segment:** Contacts tagged warm-lead, cold-lead, or in nurture with no active pipeline

| Step | Day | Channel | Message/Action |
|---|---|---|---|
| 1 | April 1 | Email | "Spring is here — and so is the perfect time to refresh your floors. Here's what's trending in 2026." + gallery |
| 2 | April 3 | SMS | "Spring is the busiest time for flooring — schedule filling fast. Want to get your free measure on the calendar? [CALENDAR LINK]" |
| 3 | April 7 | Email | "Limited spring availability — here's how to lock in your install before summer" |
| 4 | April 10 | SMS | "Final heads up — we have limited measure slots left this month. Happy to hold one for you. [CALENDAR LINK]" |

---

### WF-014: Seasonal Campaign — Fall Refresh
**Trigger:** Scheduler (September 1 each year)
**Target segment:** Same as Spring — warm/cold/nurture leads with no active pipeline

| Step | Day | Channel | Message/Action |
|---|---|---|---|
| 1 | Sept 1 | Email | "Fall flooring refresh — get your project done before the holidays" |
| 2 | Sept 3 | SMS | "Perfect time to get new floors in before family comes over for the holidays. We're booking October and November now. [CALENDAR LINK]" |
| 3 | Sept 7 | Email | "Flooring for colder months: why LVP and engineered hardwood are perfect for Canadian winters" |
| 4 | Sept 10 | SMS | "November installs almost full. If you've been thinking about it — now's the time. [CALENDAR LINK]" |

---

### WF-015: Refinishing Upsell — Restore Before Replace
**Trigger:** Contact changed (filter: Flooring Material = Hardwood) AND Stale opportunities (no active pipeline)  
**Goal:** Upsell refinishing to existing hardwood clients

| Step | Timing | Channel | Message/Action |
|---|---|---|---|
| 1 | Day 1 | SMS | "Hi {{contact.first_name}}! Quick question — how are your hardwood floors holding up? If they're looking a bit worn, refinishing might be the answer. It costs a fraction of replacement and your floors look brand new. Interested in a free assessment?" |
| 2 | Day 3 | Email | Subject: "Restore your hardwood before replacing it — here's why it makes sense" — cost comparison: refinishing at $3-5/sqft vs replacement at $8-15/sqft |
| 3 | Day 7 | SMS | "If you're curious what your floors could look like with a full sand and refinish, I'd love to show you some before/afters from similar homes. Want me to send some photos?" |

---

## WORKFLOW SPECS: SUPPORTING WORKFLOWS (WF-016 through WF-030)

### WF-016: No-Show Re-booking
**Trigger:** Appointment cancelled or missed (auto or manual)  
**Action:** SMS immediately → "Looks like we missed each other! Want to grab another time? [CALENDAR LINK]" → Email same day with reschedule link → Day 3 SMS final nudge

### WF-017: Estimate Expired Reactivation
**Trigger:** Contact in "Proposal Sent" stage for 60+ days with no activity  
**Action:** Email — "Your flooring quote from [date] is about to expire — want us to refresh it?" → SMS — "Hey {{contact.first_name}} — we quoted your flooring project a couple months ago. Still on the radar? Happy to revisit."

### WF-018: Referral Thank-You + Tracking
**Trigger:** Tag: referral applied to a new contact  
**Action:** Internal task — "Contact referral source for {{contact.first_name}} — thank them and track." → After job won, SMS referral source — "Your referral just booked! Thank you — [referral reward details]."

### WF-019: Commercial Account Check-In (Quarterly)
**Trigger:** Date-based, every 90 days, applied to contacts tagged: property-manager or commercial-flooring  
**Action:** Email — "Quarterly flooring update for your properties" — availability windows, new product arrivals, any promotions for multi-unit accounts

### WF-020: Google Review Follow-Up
**Trigger:** review-requested tag applied, no review-received tag after 7 days  
**Action:** Day 7 SMS — "We noticed you haven't had a chance to leave a review yet — no worries! It only takes 2 minutes if you get a moment: [GOOGLE REVIEW LINK]" → Day 14 final email reminder

### WF-021: Negative Review Intercept
**Trigger:** Tag: "negative-feedback" applied by rep (internal use only)  
**Action:** Internal alert to owner → HOLD all marketing automation for this contact → Internal task: "Call {{contact.first_name}} — resolve complaint before any further automation"

### WF-022: Deposit Payment Reminder
**Trigger:** Opportunity moved to "Contract Signed / Deposit" but Deposit Paid = No after 48 hours  
**Action:** SMS — "Quick reminder — to lock in your install date, we'll need the deposit processed. Here's how to pay: [PAYMENT LINK]" → Day 3 email with payment instructions

### WF-023: Final Payment Reminder
**Trigger:** Opportunity moved to "Invoice Sent" stage  
**Action:** Day 3 SMS — "Your invoice for [project] was sent [date]. Did you receive it okay?" → Day 7 Email — "Following up on invoice [#]" → Day 14 Internal task — "Escalate: {{contact.first_name}} invoice unpaid 14 days"

### WF-024: Care & Maintenance Onboarding
**Trigger:** Opportunity moved to "Job Complete"  
**Action:** Email with product-specific care guide based on Flooring Material field — Day 1: care instructions → Day 30: "30-day check-in: how are your new floors holding up?" → Day 90: "3-month care tips"

### WF-025: Subfloor Repair Update Notification
**Trigger:** Tag "subfloor-issue" applied by installer (internal trigger)  
**Action:** Immediate SMS to customer — "Hi [First Name], our crew found something we need to discuss before proceeding. Available for a quick call in the next 15 minutes?" → Email with subfloor issue summary, photos placeholder, Option A/B approval request → Internal task: "Call customer within 30 min re: subfloor issue"

### WF-026: Material Arrival Notification
**Trigger:** Tag: material-on-order removed OR manual trigger by rep  
**Action:** SMS — "Great news — your flooring is in! Ready to schedule your install? Here are the next available dates: [CALENDAR LINK]" → Email — "Your order has arrived" with install prep checklist

### WF-027: Holiday Shutdown Notification
**Trigger:** Date-based — December 15 each year  
**Action:** Email to all active pipeline contacts — "[Company] holiday hours: [dates closed]. Emergency water damage available [contact number]. We reopen [date] — your project is not affected."

### WF-028: New Product Announcement
**Trigger:** Manual launch trigger  
**Action:** Email to all contacts with active interest — "Just in: [new product name]" — specs, photos, pricing → SMS — "We just got [product] in — thought you might want to see it given what you were looking for."

### WF-029: Win-Back Campaign (12 months)
**Trigger:** Date-based — contacts quoted 12+ months ago, never converted  
**Action:** Email — "It's been a year — are you still thinking about flooring?" → SMS — "Hey {{contact.first_name}}! We quoted your flooring project about a year ago. Prices and products have changed a lot — want a fresh look?" → If no response: Move to cold-lead segment

### WF-030: Internal Escalation Workflow
**Trigger:** Tag: "escalate" applied OR complaint flag  
**Action:** Internal-only: Email owner + rep manager → Task: "ESCALATION: {{contact.first_name}} requires immediate owner attention." → No customer-facing messages

---

## SUMMARY: WHAT WAS BUILT

| Phase | Items | Status |
|---|---|---|
| Phase 1: Custom Fields | 20 fields | ✅ Complete |
| Phase 2: Pipelines | 4 pipelines, 53 stages | ✅ Complete (via REST API 2026-07-21) |
| Phase 3: Calendars | 3 calendars | ✅ Complete |
| Phase 4: Tags | 31 tags | ✅ Complete |
| Phase 5: Workflows | 15 primary + 15 supporting = 30 workflows | 📋 Fully documented, manual build required (API limitation) |

**Total via API:** 54 items (20 custom fields + 3 calendars + 31 tags)  
**Documented for manual build:** 4 pipelines (44 stages) + 30 workflows

---

## MANUAL BUILD CHECKLIST (for GHL UI)

### Pipelines — ✅ COMPLETE (created via REST API 2026-07-21)
- [x] Flooring - Residential Install — Pipeline ID: tr4vS2r660MtuokwiaAV
- [x] Flooring - Refinishing & Restoration — Pipeline ID: wpVsWUitSyeHlCfKM1Sl
- [x] Flooring - Commercial / Property Manager — Pipeline ID: HYBimQbL6j3GB1liEK5h
- [x] Flooring - Insurance / Water Damage — Pipeline ID: b6dWv1UtuFNyrLT9vWo1

### Workflows (Automation → Workflows → Create Workflow)
- [ ] WF-001: Speed to Response
- [ ] WF-002: Measure Appointment Confirmation
- [ ] WF-003: No-Show Recovery
- [ ] WF-004: Sample Approval Follow-Up
- [ ] WF-005: Estimate Follow-Up Sequence
- [ ] WF-006: Material Lead Time Update
- [ ] WF-007: Install Day Notification
- [ ] WF-008: Post-Install Review + Neighbour Campaign
- [ ] WF-009: Unhappy Customer Recovery
- [ ] WF-010: Insurance Claim Fast-Track
- [ ] WF-011: Real Estate Agent Referral Nurture
- [ ] WF-012: Property Manager Account Outreach
- [ ] WF-013: Spring Renovation Campaign
- [ ] WF-014: Fall Refresh Campaign
- [ ] WF-015: Refinishing Upsell
- [ ] WF-016 through WF-030: Supporting workflows (see specs above)

---

## NOTES FOR ONBOARDING A NEW CLIENT

When installing this snapshot for a new flooring client, customize:

1. **Calendar bookings** — add team member/user to each calendar
2. **SMS sender name** — replace [Rep Name] with actual rep name in all workflows
3. **Company name** — update [Company] in all templates
4. **Google Review link** — add actual Google Business Profile review URL
5. **Payment link** — connect Stripe or preferred payment method
6. **Referral program details** — define incentive amount for WF-018 and WF-008
7. **Booking calendar links** — replace [CALENDAR LINK] with actual calendar embed URLs
8. **Insurance pipeline** — toggle on/off based on client focus
9. **Commercial pipeline** — toggle on/off based on client focus
10. **Product categories** — update Flooring Material and Job Type options if client has different specialties

---

*Build log complete. Location: uMNi57hdsyDbrI5XhcYp | Built: 2026-07-21*
