# 🏗️ Concrete & Driveway GHL Snapshot — Build Log

**Sub-account:** Concrete and driveway  
**Location ID:** `MomQVDxtFt9XoCktDIbQ`  
**MCP Server:** `gohighlevel-concrete-template`  
**Build Date:** 2026-07-21  
**Built by:** Maximus AI Subagent  
**Status:** Phases 1–4 DEPLOYED ✅ | Phase 5 (Workflows) DOCUMENTED BELOW

---

## PHASE 1: CUSTOM FIELDS ✅ COMPLETE

All 20 custom fields created at the contact level.

| # | Field Name | Data Type | Field Key | GHL ID |
|---|-----------|-----------|-----------|--------|
| 1 | Lead Source | SINGLE_OPTIONS | contact.lead_source | `8te5od2OGRd94NmhaGmE` |
| 2 | Job Type | SINGLE_OPTIONS | contact.job_type | `dGHjc0tOOUxmgn7YNnmf` |
| 3 | Service Category | SINGLE_OPTIONS | contact.service_category | `DtKnTbaqs724wC9Li3XT` |
| 4 | Property Type | SINGLE_OPTIONS | contact.property_type | `NpqBpmY0AO6tuGdoL27a` |
| 5 | Surface Material | SINGLE_OPTIONS | contact.surface_material | `KFtoGGlOTOM2x5JA5ufk` |
| 6 | Estimated Square Footage | NUMERICAL | contact.estimated_square_footage | `bYzYFOAxsDw8OcH04qcQ` |
| 7 | Sealer Applied | RADIO (Yes/No) | contact.sealer_applied | `fSqWt55i6TeXqmB9Dxcd` |
| 8 | Sealing Due Date | DATE | contact.sealing_due_date | `BbSiMIHvVxZZVBdYZ2qa` |
| 9 | Permit Required | RADIO (Yes/No) | contact.permit_required | `2jeEz7dBxw7fFlQpgGYo` |
| 10 | Permit Number | TEXT | contact.permit_number | `Dw7VKoJ6ZUZ5C7A21kSe` |
| 11 | Estimate Amount | MONETORY | contact.estimate_amount | `EL3l0qxnatZXJsbVlGX5` |
| 12 | Contract Amount | MONETORY | contact.contract_amount | `poFG9iQeoVJVzsRwJ3W0` |
| 13 | Deposit Paid | RADIO (Yes/No) | contact.deposit_paid | `afVGJbm81WtTq6lqFLGd` |
| 14 | Crew Assigned | TEXT | contact.crew_assigned | `KRtk53R6NQ5FDgSU6RJN` |
| 15 | Pour/Install Date | DATE | contact.pourinstall_date | `IpMwgQxTJ9MYbbL7b0mP` |
| 16 | Weather Hold | RADIO (Yes/No) | contact.weather_hold | `C78UsmVOXA7jkjIIkj5q` |
| 17 | Review Requested | RADIO (Yes/No) | contact.review_requested | `qTquKh5doK2rrUcubGRF` |
| 18 | Review Received | RADIO (Yes/No) | contact.review_received | `uG3YxGvEBQGLznN5X48c` |
| 19 | Neighbour Campaign Sent | RADIO (Yes/No) | contact.neighbour_campaign_sent | `nLkPInRe8EwFnOX8wMgc` |
| 20 | Annual Sealing Reminder | RADIO (Yes/No) | contact.annual_sealing_reminder | `tBsImsmIdx2UEonKQrUA` |

### Dropdown Option Values

**Lead Source:** Google LSA | Google Organic | Referral | Door Knock | Real Estate Agent | Property Manager | Kijiji/Craigslist | Facebook Ad | Repeat Customer

**Job Type:** Driveway Replacement | New Driveway | Interlock/Patio | Stamped Concrete | Exposed Aggregate | Flatwork/Slab | Crack Repair | Resurfacing | Asphalt | Commercial Parking Lot | Walkway/Steps | Foundation Work

**Service Category:** Residential | Commercial | Repair/Maintenance | New Construction

**Property Type:** Residential | Commercial | Multi-Unit | Industrial

**Surface Material:** Concrete | Asphalt | Interlock/Pavers | Stamped Concrete | Exposed Aggregate | Unknown

**All RADIO fields:** Yes | No

---

## PHASE 2: PIPELINES ✅ COMPLETE

All 4 pipelines created with all stages.

---

### Pipeline 1: Concrete - Residential Driveway (16 stages)
**Pipeline ID:** `USUs7dSun4ORgpRsCdG4`

| Position | Stage Name | Stage ID |
|----------|-----------|---------|
| 0 | New Lead | `d900fba1-da60-4fcc-9e3e-593594fafa1b` |
| 1 | Estimate Scheduled | `87f58daa-ecb8-46a9-b3e6-96c63c845b14` |
| 2 | Estimate Complete | `bcd0d234-a61c-449c-aa09-ecafce66db07` |
| 3 | Proposal Sent | `1a979fef-f3ec-4b5d-b03f-952f6be69049` |
| 4 | Follow-Up Active | `3a536cff-c5e7-428a-ac9c-862807c85ed9` |
| 5 | Contract Signed / Deposit | `7bf32ef1-9ec2-47d9-a3eb-140b65e4a17c` |
| 6 | Weather Window Confirmed | `e9ac16dc-4a18-4eac-af5c-36e80de2fe76` |
| 7 | Prep/Demo | `d4f564ae-a4f8-47fc-aa9a-c57a976bc754` |
| 8 | Pour/Install Day | `d07ba996-fb44-429e-a208-6b918b707889` |
| 9 | Cure Period | `89b6cbd4-b381-45b3-a2fc-a4a8ca60bdb1` |
| 10 | Sealing Complete | `90425924-af50-4403-a7fc-34f528a0e7e2` |
| 11 | Job Complete | `6d04e6f5-d79e-4705-bd5c-9cc801f0e80d` |
| 12 | Invoice Sent | `5603cdb8-64d5-402e-a748-d5d8b667e258` |
| 13 | Paid | `61844083-be30-443f-981d-dac1a355e6c7` |
| 14 | Review Requested | `0a0d9547-1f89-4465-bbbf-d9e45a922a1b` |
| 15 | Neighbour Campaign | `60254ec8-c7ad-4df9-a631-5061820d5c09` |

---

### Pipeline 2: Concrete - Interlock / Stamped / Premium (15 stages)
**Pipeline ID:** `CKQlsT5dc9ejvGTw10BU`

| Position | Stage Name | Stage ID |
|----------|-----------|---------|
| 0 | New Inquiry | `771a26a0-fffc-452e-a40a-5905ab8c93d3` |
| 1 | Site Visit Scheduled | `c268dcde-5100-43d2-90be-e22e93ffdb2d` |
| 2 | Design Consultation | `ea4ddb04-a958-4e2d-9da7-87dfba03dfb7` |
| 3 | Proposal Sent | `56a76053-46d0-420b-8410-d3370c744cca` |
| 4 | Follow-Up Active | `48299957-7314-4738-9f6e-d39d09aa699c` |
| 5 | Contract Signed / Deposit | `8968abf0-8b6c-4f27-b4f7-4c817bfa2e6c` |
| 6 | Materials Ordered | `0db8a8ba-725f-422f-81a3-a7caf5bfafb6` |
| 7 | Prep/Excavation | `e71d7bfc-3e96-42aa-9093-26e0a37b8d75` |
| 8 | Base Work | `ff5ee07f-d006-4325-a0c2-ff901b6a11f4` |
| 9 | Install In Progress | `0585d2db-94a2-4bb3-a4a6-dac3e0eb2e31` |
| 10 | Polymeric Sand/Sealing | `10914a6e-4298-440b-93e4-835bff0aeb7d` |
| 11 | Job Complete | `e5dcae59-9f87-4685-844d-213d713018bc` |
| 12 | Invoice Sent | `6cd76e74-8cbb-4496-859f-773f509ba57c` |
| 13 | Paid | `351a5fa0-9de4-4f7b-8ba9-3d91b2d329ca` |
| 14 | Review + Referral | `8afd2e70-3e45-4190-8c16-29181f9ed906` |

---

### Pipeline 3: Concrete - Repair & Resurfacing (10 stages)
**Pipeline ID:** `aHv2T2fFUVArVoJ41Xik`

| Position | Stage Name | Stage ID |
|----------|-----------|---------|
| 0 | New Lead | `a56ac42d-ea17-4ab8-a4db-d99dd6465a73` |
| 1 | Estimate Booked | `4fb34948-a816-4738-966d-fe73f7704bce` |
| 2 | Estimate Complete | `622f41c2-e6f5-4882-b3f0-7bee4679cc13` |
| 3 | Proposal Sent | `e6618f94-afb7-44cf-b1b6-befd21453d22` |
| 4 | Follow-Up Active | `b06f9c07-9a20-4ef1-ab33-bb7101408f4e` |
| 5 | Repair Scheduled | `44c3fe2b-0e34-453f-8155-e2579a0552ff` |
| 6 | Repair Complete | `3c2a28ca-fb66-4c82-8f92-10f15b444595` |
| 7 | Invoice Sent | `87e03043-4334-4da3-ab4f-133590eca22e` |
| 8 | Paid | `59cc9cd9-62b2-4886-a902-36bb5712d5eb` |
| 9 | Review + Sealing Upsell | `467933cb-cd15-4d08-b8d4-a9010fb37c92` |

---

### Pipeline 4: Concrete - Commercial / Parking Lot (12 stages)
**Pipeline ID:** `K5uwnUH6i3VsnQSgHJVd`

| Position | Stage Name | Stage ID |
|----------|-----------|---------|
| 0 | New Prospect | `b92e8902-9c7e-4a78-8244-086137629a84` |
| 1 | Site Assessment | `4409ef4c-3d96-4282-81f5-2addfac5a6c4` |
| 2 | Proposal Submitted | `4401c67f-ecaa-48f1-ae59-346594060120` |
| 3 | Contract Awarded | `1eb95101-a218-4e0a-9d98-99a655c602dd` |
| 4 | Permit Applied | `e46a1713-aed2-4edc-be3c-fedc153064c6` |
| 5 | Mobilization | `3157eec9-57b6-4f54-b829-dba50d34a9fe` |
| 6 | Work In Progress | `1bf7e17c-9ec3-4f8c-9adf-01130a4ad377` |
| 7 | Inspection | `7f9ce4d5-2bdd-4cb5-9933-b62778715527` |
| 8 | Job Complete | `9d2e1caf-5455-4ede-9ea9-645f19322cd6` |
| 9 | Invoice Sent | `0b86e98f-dda6-4afc-a87b-25edfcaf9067` |
| 10 | Paid | `cf23e0ff-e11d-4c13-8851-c488ba09f01e` |
| 11 | Maintenance Contract | `76d0ede4-b069-4d45-ae40-4014fc625685` |

---

## PHASE 3: CALENDARS ✅ COMPLETE

| Calendar Name | Duration | Calendar ID |
|--------------|----------|------------|
| Free Estimate - Concrete/Driveway | 45 min | `2taxbz29qHarUxX5c94m` |
| Design Consultation - Premium Concrete | 60 min | `ZTNbh7lX8lAE7rsa0Ihf` |
| Commercial Site Assessment | 60 min | `dSk7FSfqan4WdzoNaAWm` |

**Note:** All calendars created with `autoConfirm: true`, `isActive: true`. Availability hours (Mon–Sat 8am–5pm) must be configured in the GHL UI after assigning a team member to each calendar.

---

## PHASE 4: TAGS ✅ COMPLETE

All 33 tags created.

| Tag Name | Tag ID |
|---------|--------|
| new-lead | `dNZOUjjyjh2Wb76o7yQm` |
| driveway-replacement | `2TLQK40aX1Eld6CNyR02` |
| new-driveway | `f1eVibKl0TaYNQdEhIEm` |
| interlock | `DzTo6hqsPwCQlYfTl9nV` |
| stamped-concrete | `g8MJSCbNuQApX4yhUSgU` |
| exposed-aggregate | `KIanPK8sSGLeR1PS9UGK` |
| flatwork | `7kNTyXXJNVQsaE5mOZag` |
| crack-repair | `zsphCj9A30brrTWmiKmF` |
| resurfacing | `ZtTjxZlIbBl9QKavZo3y` |
| asphalt | `Ex9gpPRuzNuwLmxvXrY9` |
| commercial-parking | `L7g599bkL7UaZU6zlM1x` |
| walkway-steps | `ytShS63LPwQZ276xiqEC` |
| weather-hold | `xoOha1ke7phKqiNfwufo` |
| permit-required | `RPDNQiQxATc4fSa0msSP` |
| estimate-sent | `y7PB3qJmV6vc11sVqkTc` |
| deposit-paid | `1wuPM0wfAIk7KksIern0` |
| contract-signed | `cdbTyRnaRNeQEvcvoSME` |
| cure-period | `iXwbnF2OCQ9nIeBnFQhA` |
| job-complete | `mI6R6GiyrS8H4i72Yq0j` |
| sealing-done | `Ujcg8rhs93QSzSFDYEV8` |
| annual-sealing-due | `NgDODiUoCOCxrhYKiktP` |
| review-requested | `FDu0XgcDQ5vfENLoTJWr` |
| review-received | `ODW1eFxj7L124XVbrmpc` |
| referral | `WekRA4jvszOOdWZcJd0m` |
| neighbour-campaign | `rYahEZLgRq3BsV5eEHmy` |
| cold-lead | `UeqIeK7qblTKNjOAV79M` |
| no-show | `TUWLhlN5Go4HNNObXojP` |
| google-lsa | `XjhcixFt89ERZv04MoFe` |
| real-estate-agent | `s6nHKqP0rNUEd3pPI4Ro` |
| property-manager | `C3irKuuUsKufunPEVw9H` |
| repeat-customer | `sQ8MJdzv2qh2EnydYatG` |
| facebook-ad | `K4PkJ2jPuxwIy3YhRUt8` |
| sealing-upsell-candidate | `cCR5KDeODCh5DHEpBkTi` |

---

## PHASE 5: WORKFLOWS ⚠️ MANUAL SETUP REQUIRED

**GHL's public API does not support workflow creation.** The `/workflows/` endpoint only supports GET (list). All 12 workflows must be created in GHL → Automation → Workflows → + Create Workflow.

Complete specs with exact SMS/email copy are documented below.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — looking for a free estimate on a driveway or concrete project? Reply YES and we'll reach out right away 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Lead — Speed to Response
- **Trigger:** Contact created
- **Action 1 (0 min):** Send SMS →
  ```
  Hi {{contact.firstName}}! This is {{location.name}} — we got your inquiry 
  about a free estimate 👋 We're usually slammed this time of year but want 
  to make sure you're taken care of. What's the job — driveway, patio, or 
  something else? We can get someone out this week.
  ```
- **Action 2 (2 min):** Internal notification to owner → "🚨 New driveway lead: {{contact.firstName}} — {{contact.phone}}"
- **Action 3 (1 hour, if no reply):** Send Email →
  - **Subject:** Your free estimate request — {{location.name}}
  - **Body:**
  ```
  Hi {{contact.firstName}},
  
  Thanks for reaching out to {{location.name}}!
  
  Here's what happens next:
  ✅ We schedule a quick 15-min on-site visit (free, no obligation)
  ✅ We measure the area and assess the work needed
  ✅ You get a detailed quote within 24 hours
  
  We're typically booking 2–3 weeks out — the sooner we get out to you, the better.
  
  [BOOKING LINK]
  
  Or just reply to this email with a few dates and times.
  
  {{user.firstName}}
  {{location.name}}
  ```
- **Action 4 (24 hours, if no reply):** Send SMS →
  ```
  Hey {{contact.firstName}} — just following up on your request for a free estimate. 
  Our schedule fills up fast in {{date.monthName}} — want to grab a time before 
  we book up? Takes about 15 minutes on-site and there's no obligation.
  ```
- **Action 5 (48 hours, if no reply):** Send SMS →
  ```
  {{contact.firstName}}, last try from us — didn't want to lose touch. 
  If now's not the right time that's totally fine, just let us know and 
  we'll follow up in the spring. Otherwise reply with a good time to call.
  ```
- **Action 6 (72 hours, still no reply):** Add tag `cold-lead`

---

### Workflow 3: Estimate Appointment Confirmation
- **Trigger:** Customer booked appointment (calendar: Free Estimate - Concrete/Driveway)
- **Action 1 (immediately):** Send SMS →
  ```
  ✅ Confirmed! We'll be at {{appointment.address}} on {{appointment.date}} 
  at {{appointment.time}} for your free on-site estimate. 
  Questions? Just text back. See you then! — {{location.name}}
  ```
- **Action 2 (immediately):** Send Email →
  - **Subject:** ✅ Your estimate appointment is confirmed — {{appointment.date}}
  - **Body:**
  ```
  Hi {{contact.firstName}},
  
  Your free on-site estimate is confirmed!
  📅 Date: {{appointment.date}}
  ⏰ Time: {{appointment.time}}
  📍 Address: {{appointment.address}}
  
  What to expect:
  • Our estimator will walk the area and take measurements
  • We'll ask a few questions about what you're looking for
  • No sales pressure — just straight answers and a fair quote
  
  If anything changes, reply to this email or call {{location.phone}}.
  
  {{user.firstName}}
  {{location.name}}
  ```
- **Action 3 (24 hrs before):** Send SMS →
  ```
  Quick reminder, {{contact.firstName}} — we're coming by tomorrow, 
  {{appointment.date}} at {{appointment.time}} for your free estimate. 
  Any questions before we arrive? — {{location.name}}
  ```
- **Action 4 (2 hrs before):** Send SMS →
  ```
  Hey {{contact.firstName}}, we're on our way — see you in a couple hours 
  at {{appointment.time}}. If something comes up, just text or call 📞
  ```

---

### Workflow 4: No-Show Recovery
- **Trigger:** Appointment status (filter: no-show)
- **Action 1 (30 min after):** Send SMS →
  ```
  Hey {{contact.firstName}} — we came by earlier but looks like we missed 
  each other. No problem at all — want to set up another time? 
  Just reply and we'll work around your schedule.
  ```
- **Action 2 (24 hrs later, if no reply):** Send SMS →
  ```
  {{contact.firstName}} — still interested in getting a free estimate? 
  We have a few spots opening up this week. Just reply and we'll get you booked.
  ```
- **Action 3:** Add tag `no-show`

---

### Workflow 5: Estimate Follow-Up Sequence (5-step, 21 days)
- **Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent, any pipeline)
- **Action 1 (Day 0 — immediate):** Send SMS →
  ```
  Hi {{contact.firstName}} — just sent over your estimate to {{contact.email}}. 
  Total: {{opportunity.monetaryValue}} — any questions? 
  We can usually start within 2–3 weeks of deposit.
  ```
- **Action 2 (Day 2, if no reply):** Send SMS →
  ```
  Hey {{contact.firstName}} — did you get a chance to look over the estimate? 
  Happy to answer any questions or walk you through what's included.
  ```
- **Action 3 (Day 5, if no reply):** Send Email →
  - **Subject:** Still thinking it over? Here's what our recent clients said
  - **Body:**
  ```
  Hi {{contact.firstName}},
  
  Just following up on the estimate. A big project is a big decision — 
  we want you to feel confident before moving forward.
  
  ⭐⭐⭐⭐⭐ "The crew was professional, showed up on time, and the finished 
  concrete looks amazing. Neighbours have already been asking for their number." 
  — Mike T.
  
  ⭐⭐⭐⭐⭐ "Got 4 quotes — they weren't the cheapest, but they were the most 
  thorough and actually explained what was included. Worth every penny." 
  — Sarah K.
  
  Still have questions? Reply here.
  
  {{user.firstName}}, {{location.name}}
  ```
- **Action 4 (Day 7, if no reply):** Send SMS (Financing Awareness) →
  ```
  {{contact.firstName}} — quick note: some clients use financing to spread 
  the cost of their driveway project. If that'd help, we can point you 
  in the right direction. No pressure — just wanted you to know the option exists.
  ```
- **Action 5 (Day 10, if no reply):** Send SMS →
  ```
  Hey {{contact.firstName}} — just a heads up, we're booking 
  {{date.monthNamePlus2}} dates now and they're going fast. 
  If you want to lock in a spot, now's the time. Let me know!
  ```
- **Action 6 (Day 14, if no reply):** Send SMS →
  ```
  {{contact.firstName}} — last check-in before we close your file out. 
  If you've gone in another direction, totally understand. 
  If you're still thinking about it, just reply and we'll pick up where we left off.
  ```
- **Action 7 (Day 21, if no reply):** Add tag `cold-lead`, move to stage "Follow-Up Active" (or close lost)

---

### Workflow 6: Weather Hold Notification
- **Trigger:** Contact changed (filter: Weather Hold field updated to Yes)
- **Action 1:** Send SMS to contact →
  ```
  Hi {{contact.firstName}} — we wanted to give you a heads up that we're 
  watching the weather closely for your upcoming job. If conditions don't 
  cooperate, we may need to adjust your start date by 1–2 days. 
  We'll keep you updated! — {{location.name}}
  ```
- **Action 2:** Internal task → "⚠️ Weather hold active — reschedule {{contact.firstName}}'s job when clear"

---

### Workflow 7: Pour Day Notification (Day Before)
- **Trigger:** Custom date reminder (select Pour/Install Date field, set 1 day before)
- **Action 1:** Send SMS →
  ```
  Hey {{contact.firstName}}! 🏗️ Big day tomorrow — your concrete/driveway 
  install is scheduled. The crew will arrive around [TIME]. 
  Please make sure the area is clear and accessible. 
  Any questions? Call {{location.phone}}. See you tomorrow!
  ```
- **Action 2:** Internal task → "Confirm crew assignment and materials for {{contact.firstName}} job tomorrow"

---

### Workflow 8: Post-Job Review Request + Neighbour Campaign Trigger
- **Trigger:** Pipeline stage changed (filter: new stage = Job Complete, any pipeline)
- **Action 1 (24 hrs):** Add tag `job-complete`; Send SMS →
  ```
  {{contact.firstName}} — the crew said the job turned out great! 
  Hope you're loving your new {{contact.jobType}} 🙌
  
  If you're happy with the work, we'd really appreciate a quick Google review — 
  takes 30 seconds and helps our small business a ton:
  {{custom.googleReviewLink}}
  
  Thank you! — {{location.name}}
  ```
- **Action 2 (3 days, if no review):** Send Email →
  - **Subject:** How did we do, {{contact.firstName}}?
  - **Body:**
  ```
  Hi {{contact.firstName}},
  
  Thank you for choosing {{location.name}}!
  
  If you're happy with the job, would you mind leaving us a quick Google review? 
  It takes about 30 seconds and helps families in your neighbourhood find a 
  contractor they can trust.
  
  👉 {{custom.googleReviewLink}}
  
  If for any reason you're not 100% satisfied, please reach out directly — 
  we want to make it right.
  
  {{user.firstName}}
  {{location.name}}
  ```
- **Action 3 (7 days, if no review):** Send SMS →
  ```
  Hey {{contact.firstName}} — just a gentle nudge on that Google review 
  if you haven't had a chance yet. It really makes a difference for us. 
  {{custom.googleReviewLink}} — thanks again!
  ```
- **Action 4:** Add tag `review-requested`
- **Action 5:** Internal task → "Door knock 3–5 houses on {{contact.streetAddress}} — neighbour campaign"
- **Action 6:** Add tag `neighbour-campaign`

---

### Workflow 9: Unhappy Customer Recovery (Internal Alert Only)
- **Trigger:** Customer replied (with keyword filter: not happy, disappointed, refund, complaint) OR New review received (filter: rating ≤ 3)
- **Action 1 (immediate):** Internal notification to owner →
  ```
  ⚠️ UNHAPPY CUSTOMER ALERT
  Contact: {{contact.fullName}} | {{contact.phone}}
  Trigger: Negative sentiment or low review detected
  Action required: Call within 2 hours to resolve
  ```
- **Action 2:** Add internal note to contact: "⚠️ Potential complaint — follow up immediately"
- **Note:** Do NOT send any automated messages to the customer. Owner handles personally.

---

### Workflow 10: Annual Sealing Reminder (12 months post job-complete)
- **Trigger:** Contact tag (filter: tag added = job-complete) → Wait 12 months (365 days)
- **Action 1:** Send SMS →
  ```
  Hi {{contact.firstName}}! It's {{user.firstName}} from {{location.name}} — 
  we installed your [driveway/concrete] about a year ago. 
  
  This is a great time for a fresh coat of sealer before winter — protects 
  your investment and keeps it looking sharp. 
  
  Sealing takes about 2–3 hours and starts at $350. Want us to swing by?
  ```
- **Action 2 (3 days, if no reply):** Send Email →
  - **Subject:** Protect your investment — is your driveway due for sealing?
  - **Body:**
  ```
  Hi {{contact.firstName}},
  
  It's been about a year since we installed your [driveway/concrete/patio]. 
  Sealing your surface is one of the best things you can do to protect your investment.
  
  Why seal?
  ✅ Prevents water penetration and freeze-thaw cracking
  ✅ Blocks oil stains and UV fading
  ✅ Makes your surface easier to clean
  ✅ Extends the life of your driveway by 5–10 years
  
  The right time to seal is before winter. We can usually get out within 1–2 weeks.
  
  [BOOK YOUR SEALING APPOINTMENT]
  
  {{user.firstName}}
  {{location.name}}
  ```
- **Action 3:** Add tag `annual-sealing-due`

---

### Workflow 11: Seasonal Campaign — Spring (Post-Frost Driveway Damage)
- **Trigger:** Scheduler (April 1 each year, run once annually)
- **Filter:** Contacts with tag `cold-lead` OR contacts in stage "Follow-Up Active" older than 90 days
- **Action 1:** Send SMS →
  ```
  Hey {{contact.firstName}}! 🌱 Spring is here and so is driveway season. 
  You reached out to us earlier — our schedule is filling up fast for May/June. 
  Still interested in getting that project done? 
  Reply and we'll get you back on the books!
  ```
- **Action 2 (7 days, if no reply):** Send Email →
  - **Subject:** Spring is here — time to fix that driveway before summer
  - **Body:**
  ```
  Hi {{contact.firstName}},
  
  Another Ontario winter is behind us — and so are all the freeze-thaw cycles 
  that crack concrete and heave asphalt.
  
  ❄️ → ☀️ Spring is ideal for concrete pours — ground is settled, temps are 
  perfect, and cure conditions are optimal
  
  📅 Summer books fast — our schedule starts filling up in April and by June 
  we're often 4–6 weeks out
  
  💰 Material prices increase through the season — locking in now means 
  locking in today's pricing
  
  [CLICK HERE TO BOOK YOUR FREE ESTIMATE]
  
  {{user.firstName}}
  {{location.name}}
  ```

---

### Workflow 12: Seasonal Campaign — Fall (Seal Before Freeze)
- **Trigger:** Scheduler (September 1 each year, run once annually)
- **Filter:** Contacts with tag `cold-lead` OR `annual-sealing-due` OR past clients (tag `job-complete`)
- **Action 1:** Send SMS →
  ```
  Hi {{contact.firstName}} — fall is the last window to get your driveway 
  project done before freeze-up. If you want to avoid another winter on 
  that cracked [asphalt/concrete], now's the time to act. 
  Reply and we'll see what we can fit in before the ground freezes.
  ```
- **Action 2 (7 days, if no reply):** Send Email →
  - **Subject:** Last chance before freeze-up — driveway season closing soon
  - **Body:**
  ```
  Hi {{contact.firstName}},
  
  We're in the final weeks of driveway season in Ontario.
  
  Once temperatures consistently drop below 5°C, we can't safely pour concrete 
  or lay fresh asphalt. The window is closing.
  
  What we can still fit in before season end:
  ✅ Asphalt driveway replacement or overlay
  ✅ Concrete crack repair and joint sealing
  ✅ Interlock installation (can push later than concrete)
  ✅ Driveway sealing — before winter hits
  
  Reply now and we'll see what we can fit in.
  
  {{user.firstName}}
  {{location.name}}
  ```

---

## SUMMARY

| Phase | Status | Items Deployed |
|-------|--------|----------------|
| Phase 1: Custom Fields | ✅ COMPLETE | 20 fields (5 dropdown, 8 RADIO Yes/No, 3 text, 2 date, 2 currency) |
| Phase 2: Pipelines | ✅ COMPLETE | 4 pipelines, 53 total stages |
| Phase 3: Calendars | ✅ COMPLETE | 3 calendars (45 min, 60 min, 60 min) |
| Phase 4: Tags | ✅ COMPLETE | 33 tags |
| Phase 5: Workflows | ⚠️ DOCUMENTED | 12 workflows — manual build in GHL UI required |

**Total API calls:** ~60 successful operations  
**Next actions:**
1. Configure calendar availability (Mon–Sat 8am–5pm) in GHL UI → assign team member to each calendar
2. Build 12 workflows in GHL → Automation using specs above
3. Add Google Review link as a custom value in GHL → Settings → Custom Values → `{{custom.googleReviewLink}}`
4. Connect Google Business Profile for review monitoring
5. Set up GHL phone number for SMS capability (Twilio)
6. Verify sub-account branding (logo, colours, business name)
