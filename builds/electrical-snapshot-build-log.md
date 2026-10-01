# Electrical GHL Snapshot — Complete Build Log
**Sub-Account:** Electrical Template  
**Location ID:** qnKlsusoBKTHqLYIpdDK  
**Build Date:** July 21, 2026  
**Built By:** Maximus (Subagent)  
**Status:** ✅ Phases 1–4 Complete | Phase 5 Documented

---

## Summary of Completed Build

| Phase | Items | Status |
|-------|-------|--------|
| Phase 1: Custom Fields | 20 fields | ✅ Complete |
| Phase 2: Pipelines | 5 pipelines | ✅ Complete |
| Phase 3: Calendars | 4 calendars | ✅ Complete |
| Phase 4: Tags | 29 tags | ✅ Complete |
| Phase 5: Workflows | 18 workflows documented | ✅ Documented (API cannot create) |

---

## PHASE 1: CUSTOM FIELDS

All fields created at contact level in GHL. Field key format: `contact.field_key`

| # | Field Name | Data Type | Field Key | GHL ID | Options |
|---|-----------|-----------|-----------|--------|---------|
| 1 | Lead Source | SINGLE_OPTIONS | contact.lead_source | KJZWlUIJAlcr8q0QModa | Google LSA, Google Organic, Referral, Repeat Customer, EV Charger Program, Real Estate Agent, Property Manager, Angi/HomeAdvisor, Facebook Ad, New Construction Builder |
| 2 | Job Type | SINGLE_OPTIONS | contact.job_type | 7A3SAj6a5FEnenEvsakm | Emergency Service, Panel Upgrade, EV Charger Install, Pot Lights / Fixtures, Rewire, Generator Install, Surge Protection, Bathroom/Kitchen Reno, New Construction, Commercial TI |
| 3 | Service Category | SINGLE_OPTIONS | contact.service_category | M3iRSwT7wgYme2QAeAKN | Emergency, Scheduled Service, Project/Renovation, EV Charger, Commercial, New Construction |
| 4 | Panel Size - Current | SINGLE_OPTIONS | contact.panel_size__current | JZRmM1MpXSip0qndLute | 60 amp, 100 amp, 125 amp, 200 amp, 400 amp, Unknown |
| 5 | Panel Size - Requested | SINGLE_OPTIONS | contact.panel_size__requested | B0igPzgToxRQbwLIfrai | 100 amp, 200 amp, 400 amp, Unknown |
| 6 | Panel Age | SINGLE_OPTIONS | contact.panel_age | dvS87MGrwXu5RCQzvtQC | Under 10 years, 10-20 years, 20-30 years, 30+ years, Unknown |
| 7 | Home Age | SINGLE_OPTIONS | contact.home_age | 6POgMYUWs6oJmXCsSXFO | Under 10 years, 10-20 years, 20-30 years, 30-40 years, 40+ years, Unknown |
| 8 | EV Charger Level | SINGLE_OPTIONS | contact.ev_charger_level | b26beNwChRTIhe4ivXv6 | Level 1, Level 2 (240V), DCFC Level 3, Unknown |
| 9 | EV Vehicle Make | TEXT | contact.ev_vehicle_make | rUQY0jEcoh7juhIyVvCP | Free text |
| 10 | Permit Required | SINGLE_OPTIONS | contact.permit_required | KvNXXPDa0MLK4fTjd4db | Yes, No |
| 11 | Permit Number | TEXT | contact.permit_number | ZqaxPai8zmvZ9JikZRgN | Free text |
| 12 | Permit Status | SINGLE_OPTIONS | contact.permit_status | BYXe16fLi1nrT5fqW88a | Not Required, Applied, Approved, Inspection Booked, Passed, Failed |
| 13 | Inspection Date | DATE | contact.inspection_date | ddl9vwrVIZocsrB4yxXw | Date picker |
| 14 | Estimate Amount | MONETORY | contact.estimate_amount | ptkobpdMnHhTpinva6LX | Currency |
| 15 | Contract Amount | MONETORY | contact.contract_amount | By0BAlKJyjP04mZrTqp5 | Currency |
| 16 | Technician Assigned | TEXT | contact.technician_assigned | M2gNp0NDDTFi1DiFaVnO | Free text |
| 17 | Property Type | SINGLE_OPTIONS | contact.property_type | fftg64553b3oqxSC3by6 | Residential, Light Commercial, Commercial, Multi-Unit, New Construction |
| 18 | Review Requested | SINGLE_OPTIONS | contact.review_requested | E4BVFTCcjAPJp5f2QcO4 | Yes, No |
| 19 | Review Received | SINGLE_OPTIONS | contact.review_received | PFsy1yB2SLZMoPd3kuBc | Yes, No |
| 20 | Panel Upgrade Candidate | SINGLE_OPTIONS | contact.panel_upgrade_candidate | aHcfMMqyJVm0ktXF5VxC | Yes, No |

---

## PHASE 2: PIPELINES

### Pipeline 1: Electrical - Emergency Service
**ID:** ZgeJXiaiwUQ4fsQz9cxg

| Stage | Position | Stage ID |
|-------|----------|----------|
| New Emergency Call | 1 | d317f3ed-4623-4a64-88a4-02b718e3e902 |
| Dispatched | 2 | 161681f3-1f45-4615-ba83-d110a626de7b |
| Technician On-Site | 3 | 3d46df8e-1825-4873-bab9-c4ae91ff8c9e |
| Diagnosis Complete | 4 | 94cc5e97-0cf9-4c92-b79b-65ad49afbd7f |
| Repair Approved | 5 | 0dde1b10-ca43-4ac5-bef3-ddb935e19d26 |
| Work Complete | 6 | 068e2530-b278-4b31-b509-5d86cc71a4d5 |
| Permit Filed (if required) | 7 | f3b5aad3-da25-4d48-ae6e-6e2163cb68fb |
| Inspection Passed | 8 | 2208b816-3302-4799-b0c3-502b8a12ec64 |
| Invoice Sent | 9 | 699c7973-6fe0-4738-8a18-0b0c2f243529 |
| Paid | 10 | 334d9a3e-89fe-48b3-82a7-f3d84ea2dc25 |
| Review Requested | 11 | b48f3257-a697-41d2-b79f-a85c8a1ce97b |
| Upsell Follow-Up | 12 | 6dacbb53-9a51-47e5-82b6-a238d25160b5 |

---

### Pipeline 2: Electrical - Panel Upgrade
**ID:** D0Zj6VW9gZ4A3B8qIJ1r

| Stage | Position |
|-------|----------|
| New Inquiry | 1 |
| Quote Appointment Scheduled | 2 |
| Quote Sent | 3 |
| Follow-Up Active | 4 |
| Contract Signed | 5 |
| Permit Applied | 6 |
| Permit Approved | 7 |
| Job Scheduled | 8 |
| Rough-In Complete | 9 |
| Inspection Booked | 10 |
| Inspection Passed | 11 |
| Final Complete | 12 |
| Invoice Sent | 13 |
| Paid | 14 |
| Review + Referral | 15 |

---

### Pipeline 3: Electrical - EV Charger Install
**ID:** fMATveEHrftggvYUOHNZ

| Stage | Position |
|-------|----------|
| New Lead | 1 |
| Consultation Booked | 2 |
| Site Assessment Complete | 3 |
| Quote Sent | 4 |
| Follow-Up Active | 5 |
| Rebate Application Submitted | 6 |
| Contract Signed | 7 |
| Install Scheduled | 8 |
| Install Complete | 9 |
| Inspection Passed | 10 |
| Invoice Sent | 11 |
| Paid | 12 |
| Review + Referral | 13 |

---

### Pipeline 4: Electrical - Renovation / Project
**ID:** 4DFZCRxLv3sOt7b8nHDe

| Stage | Position |
|-------|----------|
| New Inquiry | 1 |
| Site Visit Scheduled | 2 |
| Scope Confirmed | 3 |
| Quote Sent | 4 |
| Follow-Up Active | 5 |
| Contract Signed | 6 |
| Permit Applied | 7 |
| Rough-In Scheduled | 8 |
| Rough-In Complete | 9 |
| Trim-Out Scheduled | 10 |
| Trim-Out Complete | 11 |
| Inspection Passed | 12 |
| Final Invoice | 13 |
| Paid | 14 |
| Review + Referral | 15 |

---

### Pipeline 5: Electrical - Commercial / Property Manager
**ID:** 3QKkIrkwwBWVIrnYw4ji

| Stage | Position |
|-------|----------|
| New Prospect | 1 |
| Discovery Call | 2 |
| Proposal Sent | 3 |
| Contract Signed | 4 |
| Active Account | 5 |
| Project In Progress | 6 |
| At Risk | 7 |
| Renewed | 8 |
| Lost | 9 |

---

## PHASE 3: CALENDARS

| # | Name | ID | Duration | Hours | Days |
|---|------|----|----------|-------|------|
| 1 | Emergency Electrical Service | WO05w9RdmhMBqJiuwJrn | 60 min | 7am–9pm | 7 days/week |
| 2 | Electrical Quote Appointment | FCtUkDXDVfBicvRsdP4w | 60 min | 8am–5pm | Mon–Fri |
| 3 | EV Charger Consultation | FR8eakxNsC5Rr4OD3UQ3 | 45 min | 8am–5pm | Mon–Fri |
| 4 | Commercial Site Assessment | mw31444IMqgXbRULuvYl | 90 min | 8am–4pm | Mon–Fri |

**Note on Emergency Calendar:** The Emergency Electrical Service calendar is configured as a fallback/reference only. In production, emergency leads should bypass calendar booking and trigger the immediate SMS dispatch workflow instead. The calendar provides a backup booking option and is useful for recording emergency appointments after the fact.

---

## PHASE 4: TAGS

All 29 tags created successfully.

| Tag | ID |
|-----|-----|
| new-lead | LaccHvyH94brQFxvvy67 |
| emergency-call | NS8kkvoJf7owZGb5wkjw |
| panel-upgrade-candidate | BVmQrAg40MjRPTdJNwym |
| ev-charger-lead | fSouSHncJm4x0hhlSBhY |
| ev-rebate-eligible | WGO05CSJgdVDb7akyM53 |
| aging-panel-20yr | UEmlek6IyoAfNefwlRAB |
| aging-panel-30yr | 3vfIqSC6IOAAR2vpa74x |
| permit-required | Ddhu0mCvS3KWqO1B3EWk |
| permit-pending | 3nBYtjhRnpiwDiqz1ikq |
| inspection-booked | 9XzjkdMCqU7CJ3owDqTi |
| renovation-lead | rU1X3JKJDbG2MnYdIxR8 |
| new-construction | lotSanFlTmNh6urFLcew |
| commercial-account | fkTLv5XF8XMqRUX1P5Hj |
| property-manager | mEUVV3bTSyLlopnHYlw6 |
| real-estate-agent | QinfmxlAwc2iW1h7m54o |
| estimate-sent | GFNV1QFEKWIZRQ3JflZS |
| contract-signed | sY9Mfotv0hmiVW4Yhyme |
| job-complete | Xc2WqhqoOIbQH8u2hHlf |
| review-requested | I9N4UedZ6M9paYXbTa5t |
| review-received | bHnTzQdVH2JPUIGuC04a |
| referral | sqCU5RD4OzjVlhnh0agT |
| cold-lead | fWdGBLrXMC3JMGGNH6tY |
| no-show | 0PtZRzhHeEBREVHjHIqG |
| google-lsa | ZQifiqgldmExuxrzeR5u |
| angi-lead | PUN0nXIt9PHnUJVFS36M |
| facebook-ad | 7Ydk88ZJWSdfOxmToRUI |
| repeat-customer | 2f2Jw9aopuRTWFSqj3yF |
| generator-lead | Kim2bG2PAa9YHHx7uzVj |
| surge-protection-upsell | VFCciwNxGH04IuieMWQf |

**Pre-existing tags retained:** follow-up, high priority, warm lead

---

## PHASE 5: WORKFLOWS — Full Specifications

> **Note:** GHL Workflows cannot be created via API. All 18 workflows are fully specified below for manual build in the GHL Workflow Builder. Each spec includes: trigger, steps, timing, branching logic, and exact message copy.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — electrical emergency or need a quote? Reply YES and we'll reach out right away 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Emergency Lead — Speed to Dispatch

**Trigger:** Form submission with Job Type = "Emergency Service" OR Tag "emergency-call" added OR SMS/chat contains keywords: "no power", "burning smell", "sparking", "tripped breaker", "electrical fire", "emergency"

**Goal:** Dispatch technician within 15 minutes

**Step 1 — Immediate (0 min):**
- Action: Send SMS to contact
- Message: `⚡ [Company Name]: Got your emergency electrical request. Our licensed electrician is being dispatched. You'll receive a call with ETA in the next 5 minutes. For immediate assistance: [Phone]`
- Action: Send internal notification (SMS + email to owner/dispatcher)
- Internal message: `🚨 EMERGENCY LEAD: {{contact.first_name}} {{contact.last_name}} | {{contact.phone}} | {{contact.address}} | Submitted: {{now}}`
- Action: Create Task: "CALL NOW — Emergency dispatch for {{contact.first_name}}" (Due: immediately)
- Action: Add to Pipeline "Electrical - Emergency Service" → Stage "New Emergency Call"
- Action: Add Tag: `emergency-call`

**Step 2 — Wait 5 minutes (if no outbound call logged):**
- Condition: No call logged by team
- Action: Send second internal alert: "⚠️ Emergency not called yet — {{contact.first_name}} waiting. Call NOW: {{contact.phone}}"

**Step 3 — Wait 30 minutes (if contact still in "New Emergency Call" stage):**
- Action: Send SMS to contact
- Message: `Hi {{contact.first_name}} — checking in on your electrical emergency. Are you still in need of service? Reply YES and we'll get someone out immediately.`

**End condition:** Pipeline stage moves past "New Emergency Call" → stop

---

### Workflow 3: Emergency Dispatch Confirmation + ETA

**Trigger:** Opportunity moved to "Dispatched" stage in Electrical - Emergency Service pipeline

**Step 1 — Immediate:**
- Action: Send SMS to contact
- Message: `Your electrician is on the way to {{contact.address}}. ETA: approximately {{custom.eta}} minutes. They'll call when 10 minutes out. Any questions? Reply to this text. — [Company Name]`

**Step 2 — On-Site Confirmation:**
- (Manual trigger when tech arrives — move stage to "Technician On-Site")
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — your electrician has arrived at {{contact.address}} and is beginning the assessment. — [Company Name]`

---

### Workflow 4: Quote Appointment Confirmation (Immediate + 24hr + 2hr)

**Trigger:** Customer booked appointment (calendar: Electrical Quote Appointment or EV Charger Consultation or Commercial Site Assessment)

**Step 1 — Immediate:**
- Action: Send SMS
- Message: `✅ Booked! Your free electrical assessment is confirmed for {{appointment.start_date_time}}. Our electrician will arrive at {{contact.address}}. If anything changes, reply here or call [Phone]. See you then! — [Company Name]`

- Action: Send Email
- Subject: `Your Electrical Assessment is Confirmed — {{appointment.start_date_time}}`
- Body: `Hi {{contact.first_name}},\n\nYour free electrical assessment is confirmed!\n\n📅 Date: {{appointment.start_date}}\n⏰ Time: {{appointment.start_time}}\n📍 Address: {{contact.address}}\n👷 Technician: Will be confirmed the morning of your appointment\n\nWhat to expect:\n- The assessment takes 30–60 minutes\n- Please ensure access to your electrical panel\n- If you have questions before the appointment, reply to this email\n\nWe look forward to seeing you!\n\n[Company Name]\n[Phone] | [Email]`

**Step 2 — Wait until 24 hours before appointment:**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — reminder that your electrical assessment with [Company] is tomorrow at {{appointment.start_time}} at {{contact.address}}. Still good? Reply YES to confirm or call [Phone] to reschedule.`

**Step 3 — Wait until 2 hours before appointment:**
- Action: Send SMS
- Message: `Your electrician is heading your way in about 2 hours for your {{appointment.start_time}} appointment. They'll call when 10 minutes out. Any questions? Reply here.`

**End condition:** Appointment completed or cancelled

---

### Workflow 5: No-Show Recovery

**Trigger:** Appointment status changes to "No Show" OR appointment marked as missed

**Step 1 — Immediate:**
- Action: Add Tag: `no-show`
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — we were at {{contact.address}} at {{appointment.start_time}} for your electrical assessment but may have missed you. Want to reschedule? Book a new time here: [booking link] or reply with a time that works.`

**Step 2 — Wait 2 hours:**
- Condition: No reply and no new booking
- Action: Create Task: "Call {{contact.first_name}} — no-show recovery. Last appointment: {{appointment.start_date_time}}"

**Step 3 — Wait 3 days (if still no booking):**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — [Company Name] here. We missed you for your electrical assessment. We'd still love to help — want to book for this week? [booking link]`

**Step 4 — Wait 7 days (if still no booking):**
- Action: Send Email
- Subject: `Still interested in your electrical assessment?`
- Body: `Hi {{contact.first_name}},\n\nWe noticed you weren't able to make your assessment appointment. No worries — we know life gets busy.\n\nWhenever you're ready, your free electrical assessment is still available. Just book here: [booking link]\n\n[Company Name] | [Phone]`

**Step 5 — Wait 30 days (final touch):**
- Action: Add Tag: `cold-lead`
- Action: Send SMS (if no engagement)
- Message: `Hi {{contact.first_name}} — it's been a while since we connected about your electrical assessment. If you're still interested, we're here. Book anytime: [link]`

---

### Workflow 6: Post-Service Review Request (Happy Path)

**Trigger:** Opportunity moved to "Paid" stage in any pipeline

**Step 1 — Wait 24 hours:**
- Action: Add Tag: `review-requested`
- Action: Update Custom Field: Review Requested = "Yes"
- Action: Send SMS
- Message: `Hi {{contact.first_name}}! [Tech Name] from [Company] here — hope everything is working perfectly! If you had a great experience with us, a 5-star Google review would mean the world to our small team. Takes 30 seconds: [Google Review Link] 🙏⭐`

**Step 2 — Wait 72 hours (if no review detected):**
- Action: Send Email
- Subject: `Quick favour — 30-second review request`
- Body: `Hi {{contact.first_name}},\n\nWe loved working on your home's electrical system and hope you're happy with the results!\n\nIf you had a great experience, would you mind taking 30 seconds to leave us a Google review? It helps other families in [City] find a trustworthy electrician.\n\n👉 [Google Review Link]\n\nThank you so much!\n\n[Company Name] | [Phone]`

**Step 3 — Wait 7 days:**
- Condition: Still no review
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — one last ask! A Google review from you would really help our business. Direct link: [Google Review Link] 🙏`

**Step 4 — After Review Request Sequence:**
- Action: Update Custom Field: Review Received = "Yes" (manual update when review confirmed)
- Add Tag: `review-received`

---

### Workflow 7: Unhappy Customer Recovery (Internal Alert Only)

**Trigger:** Contact replies with negative sentiment OR staff marks contact as "At Risk" OR pipeline moves to "At Risk" stage

**Goal:** Prevent public negative review through fast internal response

**Step 1 — Immediate:**
- Action: Send internal notification (SMS + email to owner)
- Message: `⚠️ UNHAPPY CUSTOMER ALERT: {{contact.first_name}} {{contact.last_name}} | {{contact.phone}} | Issue flagged. Call immediately to resolve before review is posted.`
- Action: Create Task: "URGENT — Call unhappy customer {{contact.first_name}}. Resolve issue today."
- Action: Add Tag: `at-risk` (internal)

**Step 2 — DO NOT send any automated messages to contact:**
- All communication must be personal and manual for unhappy customers
- Remove contact from all automated review request sequences

---

### Workflow 8: Panel Upgrade Nurture (6-Touch Educational Sequence)

**Trigger:** Tag `panel-upgrade-candidate` added OR Custom Field "Panel Size - Current" = "100 amp" AND "Home Age" = "30-40 years" or "40+ years" OR Inquiry form received with panel upgrade reason

**Goal:** Convert cold panel upgrade inquiry into booked assessment over 30 days

**Step 1 — Immediate (Day 0):**
- Action: Send SMS
- Message: `Thanks for reaching out about your electrical panel! Panel upgrades are one of our specialties. We'll be in touch within 2 hours to book your free load assessment. — [Company Name]`

- Action: Send Email (Day 0)
- Subject: `Is Your Electrical Panel Holding Your Home Back?`
- Body: `Hi {{contact.first_name}},\n\nThanks for reaching out about your electrical panel. Here's the honest rundown:\n\n🏠 IF YOUR HOME WAS BUILT BEFORE 2000...\nMost homes of that era were wired for 100A service — enough for the appliances of that time. Today's homes need more: EV chargers, heat pumps, induction stoves, multiple home offices, and more. A 100A panel running at full load is a fire risk and a limit on what you can add.\n\n⚡ SIGNS YOU NEED A PANEL UPGRADE:\n- Breakers trip when you run multiple appliances\n- Lights flicker when AC kicks on\n- You want to add an EV charger or hot tub but were told the panel can't support it\n- Your panel has fuses instead of breakers (immediate concern)\n- You can smell something warm or burning near your panel\n\n💲 WHAT A 200A UPGRADE COSTS:\nTypically $3,500–$6,500 depending on your panel location, service entrance, and whether the utility needs to disconnect/reconnect. We'll give you an exact quote after the site assessment.\n\n📋 THE PROCESS:\n1. Free load assessment (30–45 min at your home)\n2. Detailed quote within 24 hours\n3. Permit pulled (usually 3–7 business days)\n4. Install day (6–10 hours)\n5. ESA inspection (1–3 business day scheduling)\n6. Certificate of Completion in your hands\n\nReady to book your free assessment?\n\n[Booking Link]\n\n[Company Name] | [Phone]`

**Step 2 — Wait 1 day (if no booking):**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — did you get a chance to look at the panel upgrade info we sent? Happy to answer questions or book a free assessment at a time that works for you. What's a good day this week?`

**Step 3 — Wait 3 days (if no booking):**
- Action: Send Email
- Subject: `Is your home ready for an EV charger or heat pump?`
- Body: `Hi {{contact.first_name}},\n\nHere's something most homeowners don't realize:\n\nMost 100A panels can't support a 240V EV charger circuit AND a heat pump AND a hot tub without a panel upgrade.\n\nAs EV adoption accelerates and heat pumps replace old gas furnaces, the homes that keep a 100A panel will hit a wall — you simply can't add the circuits needed for modern home energy.\n\nA 200A panel upgrade future-proofs your home for:\n✅ EV charger (dedicated 240V, 50A circuit)\n✅ Heat pump or mini-split\n✅ Hot tub or swim spa\n✅ Induction range\n✅ Battery backup system\n\nFree assessment, no obligation. Book here: [Booking Link]\n\n[Company Name] | [Phone]`

**Step 4 — Wait 7 days (if no booking):**
- Action: Send SMS
- Message: `Just checking in — panel upgrades typically book out 2–3 weeks once we pull the permit. If you want this done before [season], it's worth booking your assessment this week. No pressure, just want to make sure you're not stuck waiting.`

**Step 5 — Wait 14 days (if no booking):**
- Action: Send Email
- Subject: `What our customers say about their panel upgrade`
- Body: `Hi {{contact.first_name}},\n\n"Before the upgrade, our breakers were tripping every time we ran the dishwasher and AC at the same time. Now we have the EV charger we wanted, the AC runs perfectly, and I don't even think about the panel anymore. Best money we spent on the house." — [Customer Name], [City]\n\n[Before/after photo if available]\n\nReady to get yours done? Free assessment, no commitment: [Booking Link]\n\n[Company Name]`

**Step 6 — Wait 30 days (final direct CTA):**
- Action: Send Email
- Subject: `Still thinking about your electrical panel?`
- Body: `Hi {{contact.first_name}},\n\nIf you're still thinking about your panel — let's get the assessment done. It's free, takes 30 minutes, and you'll know exactly where you stand.\n\nNo pressure. No commitment. Just answers.\n\nBook your free panel assessment here: [Booking Link]\n\n[Company Name] | [Phone]`

**End condition:** Contact books assessment → move to pipeline, stop nurture

---

### Workflow 9: EV Charger Campaign (Rebate Education + Booking CTA)

**Trigger:** Tag `ev-charger-lead` added OR Form submission with Job Type = "EV Charger Install"

**Step 1 — Immediate:**
- Action: Add to Pipeline "Electrical - EV Charger Install" → Stage "New Lead"
- Action: Send SMS
- Message: `Hi {{contact.first_name}}! Thanks for reaching out about your EV charger. We install Level 2 chargers for all EV makes and handle the permit + electrical — everything done properly. Did you know you may qualify for a rebate up to $500? I'll call you within 2 hrs to book your free assessment. 🔋`

**Step 2 — Wait 30 minutes:**
- Action: Send Email
- Subject: `Your EV Charger Install: What to Expect + Rebates Available`
- Body: `Hi {{contact.first_name}},\n\nThanks for reaching out about your EV charger installation. Here's what you need to know before we meet:\n\n🔌 WHAT YOU NEED: A dedicated 240V circuit (Level 2 charging)\nThis gives you ~25–30 miles of range per hour of charging — most people charge overnight and wake up to a full battery. We run a dedicated circuit from your panel to your garage or charging location, pull the permit, and have you charging within a week of permit approval.\n\n💡 WILL YOUR PANEL HANDLE IT?\nIf your home has a 100A electrical panel, we'll check during our site assessment. Many 100A panels can support an EV charger circuit. If your panel is already loaded (HVAC, hot tub, etc.), we may recommend a 200A panel upgrade — which we can quote at the same time.\n\n💰 REBATES AVAILABLE:\n- Province/utility rebates available for residential Level 2 EV charger installation\n- Federal rebate programs apply in most Canadian provinces\n- We'll help you navigate the paperwork\n\n📋 THE PROCESS:\n1. Free site assessment (30–45 min)\n2. Quote sent within 24 hours\n3. Permit pulled by us\n4. Installation day (typically 2–4 hours)\n5. Help with rebate paperwork\n\nQuestions? Reply to this email or call [Phone].\n\n[Company Name] | Licensed Electrical Contractor\nESA Licence: [#] | Fully Insured | [Google Review Link]`

**Step 2b — Wait 2 hours (business hours check):**
- Action: Create Task: "Call EV charger lead — {{contact.first_name}} {{contact.last_name}} | {{contact.phone}}. Book site assessment."

**Step 3 — Wait 1 day (if no booking):**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — wanted to check in about your EV charger install. Any questions before we book your site assessment? We can usually get someone out within 3–5 business days. Book here: [EV Charger Booking Link]`

**Step 4 — Wait 3 days (if no booking):**
- Action: Add Tag: `ev-rebate-eligible`
- Action: Send Email
- Subject: `EV Charger Rebate Deadline Reminder`
- Body: `Hi {{contact.first_name}},\n\nJust a quick heads up — rebate programs for EV charger installations are time-limited and tied to program funding. The sooner you install, the more likely you are to qualify.\n\nHere's what you qualify for in Ontario:\n- Greener Homes rebate (federal): $600 for Level 2 EV charger\n- Some utility providers offer additional $200–$300 rebates\n\nWe handle the rebate paperwork for you. Book your free assessment now and we'll confirm your eligibility at the site visit.\n\n[Booking Link]\n\n[Company Name]`

**Step 5 — Wait 7 days (if no booking):**
- Action: Send SMS
- Message: `Hey {{contact.first_name}} — last follow-up on your EV charger install. We're booking about 2 weeks out right now. If you want it done this month, this week is the time to book. Link: [booking link] — or just reply and I'll get you on the schedule.`

**End condition:** Consultation booked → update pipeline stage, stop follow-up sequence

---

### Workflow 10: Permit Follow-Up (Internal Task Reminders)

**Trigger:** Custom Field "Permit Status" changes to "Applied" OR Tag `permit-pending` added

**Goal:** Communicate permit status to customer + keep team on top of permit tracking

**Step 1 — Immediate (Permit Applied):**
- Action: Send SMS to contact
- Message: `Great news — we've submitted the electrical permit for your [job type] at {{contact.address}}. Permits typically take 3–7 business days to process. We'll let you know the moment it's approved so we can get started.`

**Step 2 — Wait 3 days:**
- Action: Create Internal Task: "Check permit status — {{contact.first_name}} {{contact.last_name}} | {{contact.address}}"
- Condition: If Permit Status still = "Applied":
  - Action: Send SMS to contact: `Quick update on your permit — still in queue at the permit office. No news yet, but we're monitoring it. We'll reach out the moment it clears. — [Company Name]`

**Step 3 — Wait 5 days (if still "Applied"):**
- Action: Create Internal Task: "CALL permit office for {{contact.first_name}} — permit overdue. Follow up urgently."
- Action: Send SMS to contact: `Still waiting on the permit — we're following up with the permit office directly today to get an update. Thanks for your patience. — [Company Name]`

**Step 4 — Permit Approved (Trigger: Custom Field "Permit Status" = "Approved"):**
- Action: Send SMS to contact
- Message: `✅ Permit approved! We can now schedule your electrical work. We'll be in touch within 24 hours to book your installation date. — [Company Name]`
- Action: Update Pipeline stage to "Permit Approved"
- Action: Create Task: "Schedule installation for {{contact.first_name}} — permit approved"

**Step 5 — Inspection Passed:**
- Action: Send SMS to contact
- Message: `Your electrical work passed inspection — you're all clear! ✅ Your work is certified and ready. If you'd like a copy of your Certificate of Completion, just reply and we'll send it.\n\n5-star reviews help families like yours find a trustworthy electrician — would you mind leaving us a quick review? [Google link]`

---

### Workflow 11: Renovation Estimate Follow-Up (5-Step, 21 Days)

**Trigger:** Opportunity moves to "Quote Sent" stage in "Electrical - Renovation / Project" pipeline OR Tag `estimate-sent` added

**Step 1 — Wait 1 day:**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — just wanted to make sure you received your electrical quote for the {{contact.job_type}} at {{contact.address}}. Any questions? Happy to walk through it with you.`

**Step 2 — Wait 3 days:**
- Action: Send Email
- Subject: `A couple questions about your electrical quote`
- Body: `Hi {{contact.first_name}},\n\nFollowing up on the quote we sent for your [job type]. A few things people typically want to know at this stage:\n\n**How long will the job take?**\nFor a project of this scope, we typically estimate [X days]. We'll protect your space during the work and clean up completely each day.\n\n**What about permits?**\n[Permit required/not required for this job type]. [If required: We pull all permits — that's included in your quote.]\n\n**Payment terms?**\nWe take a deposit at contract signing and the balance on job completion.\n\nReady to move forward or have questions? Reply here or call [Phone].\n\n[Company Name]`

**Step 3 — Wait 7 days:**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — checking in on your electrical quote. We're currently booking about [X] weeks out. If you'd like to lock in your start date, now is a good time. Want to proceed or have questions I can answer?`

**Step 4 — Wait 14 days:**
- Action: Send Email
- Subject: `Your electrical quote — still valid, but a quick note`
- Body: `Hi {{contact.first_name}},\n\nJust a heads up — our quotes are valid for 30 days from the date sent. Material prices do fluctuate, so if you're planning to move forward, I'd recommend getting the contract signed this week.\n\nIf timing doesn't work right now, that's okay — just let me know where you're at and we'll figure it out.\n\nReply here or call [Phone] anytime.\n\n[Company Name]`

**Step 5 — Wait 21 days:**
- Action: Send SMS (final touch)
- Message: `Hi {{contact.first_name}} — last follow-up on your electrical quote. If timing isn't right, no worries. Just reply LATER and I'll circle back in 60 days. Otherwise, ready when you are. — [Company Name]`
- Action: If no response: Add Tag `cold-lead`

---

### Workflow 12: Post-Project Review + Referral

**Trigger:** Pipeline stage changed (filter: new stage = Paid, Electrical - Panel Upgrade or EV Charger Install or Renovation / Project pipeline)

**Step 1 — Wait 48 hours:**
- Action: Add Tag: `review-requested`
- Action: Send SMS
- Message: `Hi {{contact.first_name}}! [Tech Name] from [Company] — hope everything is working great! If you had a good experience with us, a quick Google review would mean the world to our team. Takes 30 seconds: [Google Review Link] 🙏⭐`

**Step 2 — Wait 7 days:**
- Action: Send SMS (referral ask)
- Message: `Hey {{contact.first_name}} — one quick question. Do you know any neighbours, friends, or family who might need electrical work? EV charger, panel upgrade, renovation — anything. If someone you send our way books a job, we'll send you a $[X] Visa gift card as a thank-you. No limit! Reply with their name and number and I'll take it from there. ⚡`

**Step 3 — Wait 30 days:**
- Action: Add Tag: `repeat-customer`
- Action: Add to database reactivation list (for future seasonal campaigns)

---

### Workflow 13: Surge Protection Upsell (Post-Job)

**Trigger:** Pipeline stage changed (filter: new stage = Paid, any pipeline) AND Contact tag `surge-protection-upsell` NOT already present

**Step 1 — Wait 14 days:**
- Action: Add Tag: `surge-protection-upsell`
- Action: Send SMS
- Message: `One more thing I wanted to mention — your home doesn't have a whole-home surge protector installed. With storm season coming, a single lightning strike or power surge can fry your TV, appliances, and HVAC equipment in seconds. We install whole-home surge protectors for $349 — takes under an hour. Want to add it to your system? — [Company Name]`

**Step 2 — Wait 3 days (if no response):**
- Action: Send Email
- Subject: `Spring storms are coming — is your home protected?`
- Body: `Hi {{contact.first_name}},\n\nA single lightning strike on your street can send a voltage spike through your home's wiring and fry your TV, refrigerator, HVAC system, and smart home devices in milliseconds. Surge protection strips only protect what's plugged into them.\n\nA whole-home surge protector ($349 installed) protects every circuit in your home — permanently.\n\nWe're offering this as an add-on for past customers. Want it added? Reply YES and we'll get it scheduled.\n\n[Company Name]`

---

### Workflow 14: Generator Lead Nurture

**Trigger:** Tag `generator-lead` added OR Form submission with Job Type = "Generator Install"

**Step 1 — Immediate:**
- Action: Send SMS
- Message: `Thanks for your interest in generator installation! We install both portable transfer switch setups and fully automatic standby generators. I'll call you within 2 hours to learn more about your needs. — [Company Name]`

**Step 2 — Wait 30 minutes:**
- Action: Send Email
- Subject: `Standby vs Portable Generators — What's Right for You?`
- Body: `Hi {{contact.first_name}},\n\nThanks for reaching out about generator installation. Here's what you need to know:\n\n🔋 STANDBY GENERATOR (Automatic)\n- Installs permanently outside your home (like a central AC unit)\n- Connects to your home's natural gas or propane supply\n- Turns on automatically within 30 seconds of a power failure\n- No extension cords, no manual start, no going outside in a storm\n- Protects: heat, AC, fridge, well pump, medical equipment, lights, everything\n- Cost: $8,000–$20,000 installed (includes transfer switch + permit)\n\n🔌 PORTABLE GENERATOR + TRANSFER SWITCH\n- You own the generator, we install a proper transfer switch\n- Manual start required when power goes out\n- Can power essential circuits (fridge, well pump, a few lights)\n- Cost: Transfer switch installation $1,500–$3,000 + generator cost\n\n📋 THE PROCESS:\n1. Site assessment to determine generator size and fuel source\n2. Quote (includes permit, transfer switch, concrete pad if needed)\n3. Permit pulled (required for standby generators)\n4. Installation day\n5. Utility coordination if required\n\nPower outages in Ontario average 5+ hours per event. Is your home protected?\n\nBook your free consultation: [Booking Link]\n\n[Company Name] | [Phone]`

**Step 3 — Wait 3 days (if no booking):**
- Action: Send SMS
- Message: `Still thinking about a generator? Power outages in [region] average several hours per year. A standby generator means your heat, well pump, fridge, and lights stay on automatically — no extension cords, no starting a generator in the rain. Want a quote? — [Company Name]`

**Step 4 — Wait 7 days (if no booking):**
- Action: Send Email
- Subject: `Generator installs book out fast in fall — lock in your spot`
- Body: `Hi {{contact.first_name}},\n\nJust a heads up — fall is our busiest season for generator installs. Every time there's a storm warning, our phone rings off the hook.\n\nIf you want your generator installed before winter, the time to book the consultation is now. We're booking [X] weeks out.\n\nReady to lock in your spot? [Booking Link]\n\n[Company Name]`

---

### Workflow 15: Commercial PM Outreach Sequence

**Trigger:** Tag `property-manager` added OR Lead Source = "Property Manager" OR Pipeline "Electrical - Commercial / Property Manager" Stage "New Prospect" entered

**Step 1 — Immediate:**
- Action: Send Email
- Subject: `Electrical for your [City] properties — faster response, clean reporting`
- Body: `Hi {{contact.first_name}},\n\nI'm [Your Name], owner of [Company], a licensed electrical contractor in [City]. I work with property managers who need electrical issues handled fast, documented properly, and billed cleanly.\n\nWhat I offer property management clients:\n- Priority emergency dispatch (target response: 60 min or less)\n- Detailed work orders with before/after documentation for your records\n- Direct billing to your management company with itemized invoices\n- All permits pulled — no liability for you\n- Annual electrical inspection packages available\n\nHappy to meet for 15 minutes. Worth a quick call?\n\n[Your Name]\n[Company Name] | [Phone] | ESA Licence: [#] | Fully Insured`

**Step 2 — Wait 3 days:**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — [Your Name] from [Company]. Sent you an email about electrical services for your properties. We're available 24/7 for your tenants' emergencies and provide full documentation for your files. Quick call this week?`
- Action: Create Task: "Call {{contact.first_name}} — PM outreach follow-up. Email sent 3 days ago."

**Step 3 — Wait 7 days:**
- Action: Create Task: "Phone call attempt + voicemail — {{contact.first_name}} PM prospect. Note response in CRM."

**Step 4 — Wait 14 days:**
- Action: Send Email
- Subject: `How we handle electrical for [similar property type] in [City]`
- Body: `Hi {{contact.first_name}},\n\nFollowing up one more time. Here's a quick case study:\n\n[Property type similar to theirs] in [City] — they were using a rotating list of contractors and getting inconsistent response times and incomplete documentation. After switching to us:\n- Emergency response time dropped to under 45 minutes\n- All work orders include before/after photos\n- Zero missed permit pulls\n- Simplified invoicing to their management company\n\nIf you're open to a 15-minute call to see if we'd be a fit for your portfolio, I'd appreciate the time.\n\n[Your Name] | [Company Name] | [Phone]`

**Step 5 — Wait 30 days (quarterly re-touch):**
- Action: Send Email
- Subject: `Q[X] Electrical Checklist for Property Managers`
- Body: `Hi {{contact.first_name}},\n\nHere's your seasonal electrical checklist for your properties:\n\nSPRING:\n☐ Test all GFCI outlets in kitchens, bathrooms, and outdoor areas\n☐ Inspect exterior outlets and fixtures after winter\n☐ Check panel for any tripping breakers from heating season load\n☐ Test smoke and CO detectors (replace batteries)\n\nIf anything on this list needs attention, we're one call away.\n\n[Company Name] | [Phone]`

---

### Workflow 16: 30-Day Cold Lead Re-Engagement

**Trigger:** Tag `cold-lead` added AND contact has NOT had outbound activity in 30 days

**Step 1 — Immediate (after trigger):**
- Action: Wait 30 days from last contact
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — [Company Name] here. We connected a while back about electrical work. Just checking in — still something you're thinking about? Happy to answer questions or book a no-obligation assessment. — [Company]`

**Step 2 — Wait 7 days (if no response):**
- Action: Send Email
- Subject: `Still thinking about your electrical work?`
- Body: `Hi {{contact.first_name}},\n\nWe connected a while back about your electrical needs. We know timing isn't always right immediately — life gets busy.\n\nWhenever you're ready, we're here. No pressure, no follow-up unless you want it.\n\nJust reply to this email or book here: [booking link]\n\n[Company Name]`

**Step 3 — Wait 30 days more (if still no response):**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — last check-in from [Company]. If electrical work is on your list for this year, we'd love to help. Reply READY anytime. If not, reply STOP and we won't contact you again.`
- Action: If no response in 7 days: Remove from active sequences, archive lead

---

### Workflow 17: Seasonal Campaign — Spring (Outdoor Lighting, AC Circuits, Spring Reno)

**Trigger:** Date-based — Launch first week of April each year  
**Audience:** All past customers tagged `job-complete` + contacts tagged `panel-upgrade-candidate`

**Step 1 (Email — Week 1 of April):**
- Subject: `Spring electrical checklist — is your home ready?`
- Body: `Hi {{contact.first_name}},\n\nSpring is here — and so are a few things worth checking on your home's electrical system.\n\n⚡ SPRING ELECTRICAL CHECKLIST:\n☐ Test all GFCI outlets (kitchens, bathrooms, garage, exterior)\n☐ Check outdoor lighting fixtures and outlets\n☐ Panel health check — any breakers tripping?\n☐ Planning a deck, patio, or outdoor kitchen? New circuits needed\n☐ AC season starting soon — is your panel load ready?\n\n🌩️ SURGE PROTECTION:\nSpring storm season means lightning risk. A whole-home surge protector ($349 installed) protects every device in your home permanently. Most homeowners don't know they need one until it's too late.\n\n🔌 EV CHARGER SEASON:\nSpring is when most EV buyers want their charger installed. We're booking now — federal rebates are available.\n\nReply YES for any of the above and we'll get you booked. Or call [Phone].\n\n[Company Name]`

**Step 2 (SMS — 3 days after email):**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — spring check-in from [Company]. Are your outdoor outlets and lighting ready for the season? GFCI check, new circuits for the deck, or just a panel health check — reply YES and we'll book you in. ⚡`

---

### Workflow 18: Seasonal Campaign — Fall (Generator Prep, Panel Check Before Winter)

**Trigger:** Date-based — Launch first week of September each year  
**Audience:** All past customers + contacts tagged `generator-lead` + `panel-upgrade-candidate`

**Step 1 (Email — Week 1 of September):**
- Subject: `Is your home ready for winter? Electrical checklist inside`
- Body: `Hi {{contact.first_name}},\n\nFall is here — and so is storm season. Here's your annual electrical checklist:\n\n⚡ FALL ELECTRICAL CHECKLIST:\n☐ Generator test — does it start? Is fuel supply ready?\n☐ Panel inspection — ready for heating season load?\n☐ Heating system circuits — heat pump, electric baseboard, in-floor heating\n☐ Smoke + CO detector test (replace batteries before winter)\n☐ Outdoor circuits shut off and GFCI tested\n\n🔋 GENERATOR SEASON:\nIf you don't have a standby generator, this is the time to get one installed before the first major storm. We're booking October and November installs now.\n\n⚡ PANEL CHECK:\nIf your home is 25+ years old and still has a 100A panel, winter heating load is when it's most at risk. A free panel check takes 20 minutes.\n\nReply YES for any of these or call [Phone].\n\n[Company Name]`

**Step 2 (SMS — 3 days after email):**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — fall electrical check-in from [Company]. Generator ready? Panel ready for heating season? Reply YES for a quick check or to book a generator consultation before the snow hits. ⚡`

**Step 3 (Generator Lead Specific SMS — if tagged `generator-lead`):**
- Action: Send SMS
- Message: `Hi {{contact.first_name}} — storm season is here. Standby generator installs are booking out. If you want one before winter, now's the time. We can usually get permits approved in 5–10 business days. Want to lock in your spot? — [Company Name]`

---

## Build Notes & Implementation Guide

### Workflow Builder Priority Order
When building in GHL Workflow Builder, build in this order:
1. **Workflow 1** (Missed Call Text Back) — immediate revenue recovery
2. **Workflow 2** (Emergency Lead — Speed to Dispatch) — highest urgency
3. **Workflow 4** (Quote Appointment Confirmation) — needed for all calendars
4. **Workflow 6** (Post-Service Review Request) — passive revenue (reviews = more leads)
5. **Workflow 8** (Panel Upgrade Nurture) — highest value lead type
6. **Workflow 9** (EV Charger Campaign) — highest growth market
7. Remaining workflows in order listed

### Custom Values to Set Per Client
When deploying this snapshot to a client sub-account, populate these custom values:
- `{{company_name}}` — Electrical contractor business name
- `{{phone}}` — Main business phone
- `{{email}}` — Owner/dispatcher email
- `{{address}}` — Business address
- `{{google_review_link}}` — Direct Google review link
- `{{booking_link}}` — Primary booking calendar link
- `{{ev_booking_link}}` — EV charger consultation calendar link
- `{{esa_license}}` — ESA licence number
- `{{city}}` — Service area city

### Pipeline Usage Guide
- **Emergency Service** → Any same-day, urgent, or hazard-related call
- **Panel Upgrade** → Any 200A service upgrade inquiry or recommendation
- **EV Charger Install** → EV charger install only (flag panel upgrade as separate opportunity if needed)
- **Renovation / Project** → Kitchen, basement, addition, rewire, new construction
- **Commercial / Property Manager** → B2B accounts, property managers, strata, commercial buildings

### Tag Usage Guide
- Apply `panel-upgrade-candidate` at site visit whenever panel is 100A and home is 20+ years old
- Apply `ev-rebate-eligible` for all Ontario residential EV charger leads
- Apply `aging-panel-20yr` or `aging-panel-30yr` based on panel age from site visit
- Apply `google-lsa`, `angi-lead`, or `facebook-ad` to track lead source ROI
- `cold-lead` = no engagement in 30+ days → enters re-engagement workflow

---

*Build log complete. All IDs verified in GHL sub-account qnKlsusoBKTHqLYIpdDK.*  
*For questions: Tony DeCarlo — adecarlo@use1app.com*
