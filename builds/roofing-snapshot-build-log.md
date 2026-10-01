# Roofing Snapshot Build Log

**Location ID:** GWT5q81NPjNigP64flsE  
**MCP Server:** gohighlevel-roofing-template  
**Build Date:** 2026-07-21  
**Status:** Phases 1-4 COMPLETE | Phase 5 (Workflows) — Manual setup required (GHL API limitation)

---

## PHASE 1: CUSTOM FIELDS ✅ COMPLETE

All 17 custom fields created for contacts.

| # | Field Name | Data Type | Field Key | GHL ID |
|---|-----------|-----------|-----------|--------|
| 1 | Lead Source | SINGLE_OPTIONS | contact.lead_source | x7640e3smp9oIRxoWHZj |
| 2 | Job Type | SINGLE_OPTIONS | contact.job_type | dpGldOgqXcdGgaZVVTGs |
| 3 | Insurance Company | TEXT | contact.insurance_company | SyATp5bFkCVjwgVqgABx |
| 4 | Claim Number | TEXT | contact.claim_number | 5O4EcdOvZJMdMAx8orEE |
| 5 | Adjuster Name | TEXT | contact.adjuster_name | uyYAfyZ2yrXr1he77muP |
| 6 | Adjuster Phone | PHONE | contact.adjuster_phone | qrNKkCg6KXuqPIZzVmsk |
| 7 | Deductible Amount | MONETORY | contact.deductible_amount | y6ub1pFc0i3wOHLRurY5 |
| 8 | Storm Date | DATE | contact.storm_date | uMachlviszKanSafV9YO |
| 9 | Roof Age | SINGLE_OPTIONS | contact.roof_age | lpOrDUT9xxzcUYvV3bmd |
| 10 | Square Footage | NUMERICAL | contact.square_footage | hnqPPkYvStTOyGwHTCfm |
| 11 | Estimate Amount | MONETORY | contact.estimate_amount | ee77qSznBO7zq6wGeF1i |
| 12 | Contract Amount | MONETORY | contact.contract_amount | MApwHpvw9ssbOTekaK4S |
| 13 | Final Invoice Amount | MONETORY | contact.final_invoice_amount | lq91wLjW9py8It7IA00P |
| 14 | Crew Assigned | TEXT | contact.crew_assigned | AoGxAcMX4h8xoR21gc3t |
| 15 | Review Requested | CHECKBOX | contact.review_requested | Kd6x6VJ62RSHDnM02Jm2 |
| 16 | Review Received | CHECKBOX | contact.review_received | xJ6oDoivtpJPvI1A6PJ0 |
| 17 | Supplement Filed | CHECKBOX | contact.supplement_filed | uc3sfKp0SMI0IQuDgSVS |

### Custom Field Dropdown Options

**Lead Source:** Facebook Ad, Google LSA, Google PPC, Door Knock, Referral, Storm Alert, Insurance Adjuster, Repeat Customer, Organic  
**Job Type:** Retail/Cash, Insurance Claim, TPO, Metal, Shingle, Flat  
**Roof Age:** Under 5 years, 5-10 years, 10-15 years, 15+ years, Dont Know  
**Review Requested / Review Received / Supplement Filed:** Checkbox with "Yes"  

---

## PHASE 2: PIPELINES ✅ COMPLETE

Both pipelines created via direct GHL REST API.

### Pipeline 1: Roofing - Retail/Cash Jobs
**Pipeline ID:** lIpPsDi2vY8DmvEoEEvl

| Position | Stage Name | Stage ID |
|----------|-----------|---------|
| 0 | New Lead | c64605ce-5aa3-4b18-876d-f4c729d1fb97 |
| 1 | Contacted | 7469b266-a49d-416d-a355-25a4644e4454 |
| 2 | Estimate Scheduled | 87e46486-69c5-4763-950f-1d5391dbfdeb |
| 3 | Estimate Completed | 42d305b0-b601-4e0a-9612-3948ec8edd40 |
| 4 | Proposal Sent | d9748c1d-618d-4928-9786-c698ed1cae1c |
| 5 | Follow-Up Active | 51376cee-c4d8-4295-b8f2-305b5568cab8 |
| 6 | Won - Contract Signed | fd98129c-b105-4c0f-a47a-effc961c320a |
| 7 | Job Scheduled | b3cbb731-7130-422d-bd65-326dd0213ee1 |
| 8 | Job In Progress | b2807c58-c55f-4033-8025-b857df33dec0 |
| 9 | Job Complete | ec2c1d4c-5dc6-4581-be97-2d322e4e97fc |
| 10 | Lost / No Decision | db79259d-3e29-4d96-bbaf-9f0413e287a0 |

### Pipeline 2: Roofing - Insurance Claims
**Pipeline ID:** ooqLyoEz39D2aJx8zXKz

| Position | Stage Name | Stage ID |
|----------|-----------|---------|
| 0 | Damage Reported | 81d5a371-3a7c-4926-afcf-2881b4ec2cbd |
| 1 | Inspection Scheduled | ba160271-c03a-470f-b669-cb5b90c0fb9a |
| 2 | Inspection Complete | b5af1afb-3ad1-4b5f-9e21-b948ebce6a0f |
| 3 | Claim Filed | e3bdf75e-4be7-46cd-b26c-3a6a4945f9fa |
| 4 | Adjuster Meeting Set | 8acd1553-04e6-4729-928a-64f24e2d695e |
| 5 | Adjuster Meeting Complete | cf1b03a7-54e2-4fc9-9ec0-0f383b074591 |
| 6 | Approval Received | 97592399-e570-48d1-af4c-aa2df1216b15 |
| 7 | Contract Signed | 40725479-fc10-407d-8cd5-aaf72ab2535b |
| 8 | Material Ordered | 708984ad-ae1f-45fb-8975-cf0f97e928e8 |
| 9 | Job Scheduled | 586e7e49-adca-4d8f-9068-ab7afcae5905 |
| 10 | Job Complete | 9d662d58-e71b-4c37-a013-990c2dc963d2 |
| 11 | ACV Check Received | 78112678-7a64-43be-b7c7-11649892ec51 |
| 12 | Supplement Filed | 3d4d5a34-e110-407e-839b-f3ab31725293 |
| 13 | Final Payment Received | f88d10ec-fd1f-4722-ba0f-279758056c78 |
| 14 | Review + Referral | 907aeeaf-d7fd-4090-8f40-06bd6e797c58 |

---

## PHASE 3: CALENDARS ✅ COMPLETE

| Calendar Name | Duration | Slot Interval | Calendar ID |
|--------------|----------|--------------|------------|
| Free Estimate - Roofing | 45 min | 45 min | 3D3F4TzhzqlX9jcxXaFd |
| Insurance Inspection - Roofing | 60 min | 60 min | lQyevRfLW2JB0cJKypXW |
| Pre-Job Scheduling | 30 min | 30 min | oE5MkrJwOAuazxHGv9CR |

**Note:** All calendars are active, auto-confirm enabled, Mon-Fri 8am-5pm availability needs to be manually configured in GHL UI (availability/schedule APIs require team member assignment first).

---

## PHASE 4: TAGS ✅ COMPLETE

All 18 tags created.

| Tag Name | Tag ID |
|---------|--------|
| new-lead | KyjdtcpzKHMoreOfopT5 |
| insurance-lead | LohEXhLKmGiS183FxIgT |
| retail-lead | sA8qxDKsWg4JEtcvHqLJ |
| storm-damage | qhmKvkAn3Hhub2uef5rR |
| estimate-sent | rqoSwfmXQXFkQo41Dmyb |
| contract-signed | grSktDtZ79BasbubrRyA |
| job-complete | ZY4qHfexPGspuzMSTN5O |
| review-requested | dA5JTLH440bJ4tDLEnTg |
| review-received | rWqaaufnPmOTbsVG7RqX |
| referral | a6HY5FWWmyvmZFsmKuzl |
| cold-lead | m8KOsjTeZoR4iaUWiU8H |
| facebook-ad | d2qKGx1smgatSzO3Pjsc |
| google-lsa | BZzI6YgymQ7lkDF4SMN5 |
| door-knock | TzQFQ70IqCXEx72Eiksp |
| neighbor-campaign | fWi20v0ZtrPMWI9qRMOM |
| storm-alert | KYHiXSRkF5Ab0suOp9HR |
| supplement-filed | wbdF8TmfHCEzJ2xeHabX |
| no-show | 476x1Ynb7GimVTCDVuzG |

---

## PHASE 5: WORKFLOWS ⚠️ MANUAL SETUP REQUIRED

**GHL's public API does not support workflow creation.** The `/workflows/` endpoint only supports GET (list). Workflow creation requires using GHL's visual builder in the UI.

Below are the complete specs for all 18 workflows. Tony or a VA should create these in GHL → Automation → Workflows → + Create Workflow.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — need a free roof inspection or estimate? Reply YES and we'll reach out right away 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Lead - Speed to Lead
- **Trigger:** Contact created
- **Action 1:** Send SMS immediately → "Hey {{contact.firstName}}, this is [Rep Name] at [Company]. Just saw your request — are you dealing with storm damage or looking for a free estimate?"
- **Action 2:** Create task → "Follow up with {{contact.firstName}} in 30 minutes if no reply"

---

### Workflow 3: Estimate Appointment Confirmation
- **Trigger:** Customer booked appointment (calendar: Free Estimate - Roofing or Insurance Inspection - Roofing)
- **Action 1:** Send SMS immediately → "Hey {{contact.firstName}}, you're confirmed! Your free roofing estimate is set for {{appointment.startTime}}. We'll see you then! Reply STOP to cancel."
- **Action 2:** Wait until 24 hours before appointment
- **Action 3:** Send SMS → "Reminder: Your roofing estimate is tomorrow at {{appointment.startTime}}. Reply RESCHEDULE if you need to change it."
- **Action 4:** Wait until 2 hours before appointment
- **Action 5:** Send SMS → "Heads up — your roofing estimate is in 2 hours at {{appointment.startTime}}. See you soon!"

---

### Workflow 4: No-Show Recovery
- **Trigger:** Appointment status (filter: no-show)
- **Action 1:** Wait 30 minutes
- **Action 2:** Send SMS → "Hey — did we get the time wrong? We're available now if you want us to swing by. Just reply and we'll make it happen."
- **Action 3:** Add tag: no-show
- **Action 4:** Create task → "Call {{contact.firstName}} — no-show recovery"

---

### Workflow 5: Estimate Follow-Up Sequence
- **Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent, Pipeline: Roofing - Retail/Cash Jobs)
- **Action 1:** Add tag: estimate-sent
- **Action 2:** Send SMS immediately → "Hey {{contact.firstName}}, just wanted to make sure you got our estimate. Let me know if you have any questions!"
- **Wait:** 2 days
- **Action 3:** Send SMS → "Hi {{contact.firstName}}, following up on that estimate. Most of our customers get on the schedule within a few days — want to lock in a date?"
- **Wait:** 3 days
- **Action 4:** Send SMS → "{{contact.firstName}}, I don't want to be a pest but roofing costs go up every year — locking in now protects you. Still interested?"
- **Wait:** 7 days
- **Action 5:** Send SMS → "Hey, last check-in on your estimate. If the price is the issue, ask me about our financing options. No credit check required."
- **Wait:** 9 days
- **Action 6:** Send SMS → "{{contact.firstName}}, I'll take you off my follow-up list after today — but if you need anything, I'm here. Just reply anytime."
- **Action 7:** Move to stage: "Follow-Up Active" if no response, else move to "Won - Contract Signed"

---

### Workflow 6: Insurance Claim Nurture
- **Trigger:** Contact tag (filter: tag added = insurance-lead)
- **Action 1:** Send SMS immediately → "Hey {{contact.firstName}}, thanks for reaching out. Insurance claims can feel overwhelming — we handle everything for you. When's good to talk?"
- **Wait:** 1 day
- **Action 2:** Send email → Subject: "How the insurance claim process works" | Body: Educational email about claim process, timeline, what to expect
- **Wait:** 2 days
- **Action 3:** Send SMS → "Did you know most insurance companies cover a full roof replacement after storm damage? We've helped dozens of homeowners get paid in full. Want us to assess yours?"
- **Wait:** 3 days
- **Action 4:** Send email → Subject: "What to say to your adjuster" | Body: Tips for adjuster meeting
- **Wait:** 2 days
- **Action 5:** Send SMS → "{{contact.firstName}}, have you filed your claim yet? We can help you through every step — including the adjuster meeting."
- **Wait:** 3 days
- **Action 6:** Send email → Subject: "Real results from homeowners like you" | Body: Social proof + case studies
- **Wait:** 3 days
- **Action 7:** Send SMS → "Last message from us on this — if you need help with your insurance claim now or in the future, we're here. Just reply anytime."

---

### Workflow 7: Post-Job Quality Check
- **Trigger:** Pipeline stage changed (filter: new stage = Job Complete)
- **Action 1:** Add tag: job-complete
- **Wait:** 2 hours
- **Action 2:** Send SMS → "Hey {{contact.firstName}}, the crew just wrapped up! How does everything look? Reply GREAT if you love it, or ISSUE if there's something we should check."

---

### Workflow 8: Review Request - Happy Customer
- **Trigger:** Inbound SMS reply contains "GREAT" (from Workflow 7)
- **Action 1:** Wait 30 minutes
- **Action 2:** Send SMS → "Awesome! So glad you're happy with the work. Would you mind leaving us a quick Google review? It helps a ton: [INSERT GOOGLE REVIEW LINK]. Takes 2 minutes!"
- **Action 3:** Add tag: review-requested
- **Action 4:** Update custom field: Review Requested = checked

---

### Workflow 9: Review Recovery - Unhappy Customer
- **Trigger:** Inbound SMS reply contains "ISSUE" (from Workflow 7)
- **Action 1:** Add tag: no-show (reuse or create "quality-issue" tag)
- **Action 2:** Send internal notification to manager/owner → "⚠️ Quality issue reported by {{contact.firstName}} {{contact.lastName}} — {{contact.phone}}. DO NOT send review request. Call immediately."
- **Action 3:** Create task → "URGENT: Call {{contact.firstName}} re: quality issue. Do not send review request."
- **⚠️ DO NOT send review request to this contact**

---

### Workflow 10: Referral Request
- **Trigger:** Contact tag (filter: tag added = review-received)  
  OR  
  Pipeline stage changed (filter: new stage = Job Complete) AND 7 days have passed
- **Action 1:** Send SMS → "Hey {{contact.firstName}}, so happy we could help! Do you know anyone else who needs their roof looked at? We pay a referral fee — just send them our way and let us know."
- **Action 2:** Add tag: referral (after positive response)

---

### Workflow 11: Storm Alert Campaign
- **Trigger:** Contact tag (filter: tag added = storm-alert OR storm-damage) — activate manually after storm events
- **Action 1:** Send SMS blast → "⚠️ Storm Alert: If you haven't had your roof inspected after the recent storm, now's the time. We're offering free inspections this week — reply INSPECT to book yours."
- **Action 2:** Create task → "Call storm-alert contacts in affected area"

---

### Workflow 12: 30-Day Cold Lead Re-Engagement
- **Trigger:** Stale opportunities (no activity for 30 days)
- **Condition:** Contact is NOT tagged job-complete
- **Action 1:** Add tag: cold-lead
- **Action 2:** Send SMS → "Hey {{contact.firstName}}, it's been a while! We're still here if you need a roof inspection or estimate. Prices and materials go up every season — want to lock something in?"
- **Action 3:** If no reply in 7 days → create task to manually follow up

---

### Workflow 13: Seasonal Campaign - Spring
- **Trigger:** Scheduler (run each spring — April/May)
- **Action 1:** Send SMS → "Spring is here, {{contact.firstName}}! Time to check if winter did any damage to your roof. We're booking free spring inspections now — want one?"
- **Action 2:** Send email → Subject: "Is your roof ready for spring storms?" | Body: Spring roof care tips + call to action to book

---

### Workflow 14: Seasonal Campaign - Fall
- **Trigger:** Scheduler (run each fall — September/October)
- **Action 1:** Send SMS → "Before winter hits, {{contact.firstName}}, now's the time to check your roof. A small repair now saves a big headache in January. Want a free fall inspection?"
- **Action 2:** Send email → Subject: "Get your roof ready before winter" | Body: Fall prep checklist + booking CTA

---

### Workflow 15: Facebook Lead - Initial Contact
- **Trigger:** Contact tag (filter: tag added = facebook-ad)
- **Action 1:** Send SMS immediately → "Hey {{contact.firstName}}! Saw your form from Facebook — great timing. Are you dealing with storm damage or just want to see what a new roof would cost? Just reply and I'll help."
- **Wait:** 1 hour (if no reply)
- **Action 2:** Send SMS → "No worries if you're busy — whenever you're ready, just reply to this message and we'll get you a free estimate. Takes about 45 minutes."
- **Wait:** 1 day (if no reply)
- **Action 3:** Send SMS → "One more check-in, {{contact.firstName}}. A lot of our Facebook leads are surprised by what insurance covers. Want me to take a quick look at your roof — free, no obligation?"

---

### Workflow 16: Neighbor Campaign
- **Trigger:** Contact tag (filter: tag added = job-complete)
- **Action 1:** Create task → "NEIGHBOR CANVAS — {{contact.firstName}}'s street. Visit neighbors within 5 houses to introduce [Company Name]. Use: 'We just finished a roof at your neighbor's house — want a free inspection while we're in the area?'"
- **Action 2:** Add tag: neighbor-campaign

---

### Workflow 17: Financing Awareness
- **Trigger:** Stale opportunities (filter: stage = Proposal Sent for 5+ days, stage NOT changed to won/lost)
- **Action 1:** Send SMS → "Hey {{contact.firstName}}, one thing a lot of homeowners don't know — we offer flexible financing with no credit check required. Monthly payments as low as $X. Want the details?"
- **Action 2:** If no response in 3 days → create task "Financing follow-up call — {{contact.firstName}}"

---

### Workflow 18: Pre-Job Homeowner Education
- **Trigger:** Pipeline stage changed (filter: new stage = Job Scheduled)
- **Action 1:** Send email → Subject: "Your install is coming up — here's what to expect" | Body:
  - What day/time the crew arrives
  - How long the job takes
  - What to do with pets/vehicles
  - How to prep your home (clear driveway, etc.)
  - "We'll clean up everything — leave no trace"
  - Who to call with questions
- **Wait:** 1 day before job
- **Action 2:** Send SMS → "Just a reminder — your roofing crew arrives tomorrow! Any questions before we get started?"

---

## SUMMARY

| Phase | Status | Count |
|-------|--------|-------|
| Custom Fields | ✅ Complete | 17 |
| Pipelines | ✅ Complete | 2 (26 total stages) |
| Calendars | ✅ Complete | 3 |
| Tags | ✅ Complete | 18 |
| Workflows | ⚠️ Manual required | 18 specs documented above |

**Total items created via API:** 40  
**Items requiring manual GHL setup:** 18 workflows + calendar availability hours

### Quick-Start Checklist for Tony (Post-Build)

1. **Calendars** → Go to Calendars → Edit each → Set team member and availability (Mon-Fri 8am-5pm)
2. **Workflows** → Go to Automation → Workflows → Create each one using specs above
3. **Custom Fields** → Verify they appear in Contacts → Custom Fields section
4. **Pipelines** → Go to Opportunities → confirm both pipelines appear in dropdown
5. **Tags** → Go to Contacts → Tags — verify all 18 show up
6. **Review links** → Add your Google review link to Workflow 8 before activating

### Notes
- All monetary fields use GHL's "MONETORY" dataType (their spelling)
- Checkbox fields have "Yes" as the single option — in GHL these function as yes/no toggles
- Calendar booking pages are auto-generated at `/widget/bookings/{calendarId}`
- Free Estimate calendar: `/widget/bookings/3D3F4TzhzqlX9jcxXaFd`
- Insurance Inspection calendar: `/widget/bookings/lQyevRfLW2JB0cJKypXW`
- Pre-Job Scheduling calendar: `/widget/bookings/oE5MkrJwOAuazxHGv9CR`
