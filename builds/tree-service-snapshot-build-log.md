# Tree Service GHL Snapshot - Build Log

**Sub-Account Location ID:** GmFMWWCcsXE0oksic6VV
**Build Date:** 2026-07-21
**Built by:** Maximus Subagent
**Reference:** `/home/maximus/.openclaw/workspace/research/tree-service-ghl-snapshot-research.md`

---

## BUILD STATUS SUMMARY

| Phase | Component | Status | Count |
|-------|-----------|--------|-------|
| Phase 1 | Custom Fields | ✅ Complete | 19 fields |
| Phase 2 | Pipelines | ✅ Complete | 5 pipelines |
| Phase 3 | Calendars | ✅ Complete | 3 calendars |
| Phase 4 | Tags | ✅ Complete | 30 tags |
| Phase 5 | Workflow Specs | ✅ Documented | 10 workflows |

---

## PHASE 1: CUSTOM FIELDS

All fields created at contact model level in sub-account `GmFMWWCpsXE0oksic6VV`.

| # | Field Name | Data Type | GHL Field ID |
|---|-----------|-----------|--------------|
| 1 | Lead Source | SINGLE_OPTIONS | `lp1RAextIu2HN2VVmtZf` |
| 2 | Job Type | SINGLE_OPTIONS | `0TjgK2khlUj3hAHwAYxR` |
| 3 | Service Category | SINGLE_OPTIONS | `xvGTTl6wD8JVdcHqYxqa` |
| 4 | Property Type | SINGLE_OPTIONS | `ws8R8EkfrcR1ry34UcTW` |
| 5 | Tree Species | TEXT | `YghsTI3YdlqsMiJHUTq0` |
| 6 | DBH - Diameter at Breast Height | SINGLE_OPTIONS | `3Gg07ud667sNySStR3Og` |
| 7 | Hazard Level | SINGLE_OPTIONS | `uL7SwRGPj24Ok1ksqA0s` |
| 8 | Permit Required | RADIO | `kGqMXQqnjQ7IchgZbpgl` |
| 9 | Permit Number | TEXT | `CblEepGrsbTo23HKnNm1` |
| 10 | Insurance Claim | RADIO | `YBNwohW3v28q4jPVvqlf` |
| 11 | Insurance Company | TEXT | `HW0VFuFAEpzmTuYFUyeR` |
| 12 | Estimate Amount | MONETORY | `iPGLO2nCmHOWGJABrh6q` |
| 13 | Contract Amount | MONETORY | `MvJb3yWSmQmc6ZJvkLr4` |
| 14 | Crew Assigned | TEXT | `BpbPFtxXgdib0qQhEbt9` |
| 15 | Equipment Required | SINGLE_OPTIONS | `6W33q8aznndgAaECVl5j` |
| 16 | Review Requested | RADIO | `eqDeZzRjf9RSaH8hZmAB` |
| 17 | Review Received | RADIO | `X7fnSC1Uaap3mNJfAyTi` |
| 18 | Neighbour Campaign Sent | RADIO | `pOBU0w4UUGIBE1ozHsfb` |
| 19 | Annual Trimming Reminder | RADIO | `xeATVKJLn46iNwZhrp50` |

### Field Option Values

**Lead Source options:** Google LSA, Google Emergency Search, Referral, Storm Event, Property Manager, Municipality, Insurance Adjuster, HOA, Facebook Ad, Repeat Customer

**Job Type options:** Emergency Storm Removal, Tree Removal, Tree Trimming/Pruning, Stump Grinding, Crown Reduction, Lot Clearing, Deadwood Removal, Cabling/Bracing, Arborist Assessment, Commercial

**Service Category options:** Emergency, Scheduled, Commercial/Municipal, Recurring Maintenance

**Property Type options:** Residential, Commercial, Municipal, HOA, Multi-Unit

**DBH options:** Under 12 inches, 12-24 inches, 24-36 inches, 36+ inches, Unknown

**Hazard Level options:** Low, Moderate, High, Emergency, Unknown

**Equipment Required options:** Chainsaw Only, Bucket Truck, Crane, Chipper, Stump Grinder, Full Equipment

**All RADIO fields:** Yes / No

---

## PHASE 2: PIPELINES

All pipelines created via GHL Opportunities API.

### Pipeline 1: Tree Service - Emergency
**ID:** `08ylSiaCAUzR8PTxX6rF`

Stages (in order):
1. New Emergency Call
2. Dispatched
3. On-Site Assessment
4. Hazard Secured
5. Work Approved
6. Work In Progress
7. Cleanup Complete
8. Invoice Sent
9. Paid
10. Review Requested
11. Insurance Follow-Up

---

### Pipeline 2: Tree Service - Residential
**ID:** `fzJnDLTHkctZt9F9bxuL`

Stages (in order):
1. New Lead
2. Estimate Scheduled
3. Estimate Complete
4. Proposal Sent
5. Follow-Up Active
6. Contract Signed
7. Job Scheduled
8. Job In Progress
9. Cleanup Complete
10. Invoice Sent
11. Paid
12. Review + Referral

---

### Pipeline 3: Tree Service - Stump Grinding
**ID:** `kUcOsASsURQpYasW40Hx`

Stages (in order):
1. New Lead
2. Quote Sent
3. Follow-Up
4. Job Scheduled
5. Job Complete
6. Invoice Sent
7. Paid
8. Review Requested

---

### Pipeline 4: Tree Service - Commercial / Municipal
**ID:** `vpz1seQBmlDjHZfJg0a1`

Stages (in order):
1. New Prospect
2. Site Walk
3. Proposal Submitted
4. Contract Signed
5. Job Scheduled
6. Job In Progress
7. Job Complete
8. Invoice Sent
9. Paid
10. Annual Contract Renewal

---

### Pipeline 5: Tree Service - Annual Recurring
**ID:** `wZjVZnCP8dcuuyD0iWmi`

Stages (in order):
1. Annual Reminder Sent
2. Response Received
3. Job Scheduled
4. Job Complete
5. Invoice Sent
6. Paid
7. Next Year Reminder Set

---

## PHASE 3: CALENDARS

All calendars created via GHL Calendars API.

### Calendar 1: Free Tree Assessment
**ID:** `7hS6GlnNrrUQEXlW94lG`
- **Duration:** 45 minutes
- **Buffer:** 30 minutes after (travel time)
- **Availability:** Monday-Friday, 8:00 AM - 5:00 PM
- **Description:** Free on-site tree assessment and estimate. Our ISA-trained arborists will walk the property with you and provide a written estimate.

---

### Calendar 2: Emergency Tree Service
**ID:** `teclEVhpzMvznoZgHYcs`
- **Duration:** 60 minutes
- **Buffer:** 15 minutes
- **Availability:** 7 days a week, 7:00 AM - 7:00 PM
- **Description:** Emergency tree removal and hazard response. Available 7 days a week for storm damage, trees on structures, and urgent hazard situations.

---

### Calendar 3: Commercial Site Walk
**ID:** `jLk5pxxlq0KNrG3s6VJv`
- **Duration:** 60 minutes
- **Buffer:** 30 minutes
- **Availability:** Monday-Friday, 8:00 AM - 4:00 PM
- **Description:** Site walk for HOA, property managers, municipalities, and commercial property tree care contracts. Includes canopy assessment and proposal discussion.

---

## PHASE 4: TAGS

All 30 tags created via GHL Tags API.

| Tag | ID |
|-----|-----|
| new-lead | `CUzYeFFMCod0w3KQzidA` |
| emergency-removal | `1K6WL3w1XhPUAAMbjV1n` |
| tree-removal | `g4WvZcDpZtgcVBCjhqop` |
| tree-trimming | `trlTHPzaDYb8m9uvYqdh` |
| stump-grinding | `LaphYrVrcSTbS2rBsJm9` |
| crown-reduction | `PfPwUuVaL4rNXUShEYX8` |
| lot-clearing | `NTrFsDpCr8nyoFQNGX63` |
| arborist-assessment | `9MbQpnmJF42NLeNXU1bH` |
| commercial-job | `r10LHvDPEdb6nbuKWyd3` |
| municipal-job | `KBQQxGKh02g08RDv5dh3` |
| storm-event | `UjN6x7OsLcXRQXDr3iQT` |
| insurance-claim | `mo19x5Cz7sBAJtZRdfZ6` |
| hazard-tree | `Uy22EfeyJ4CItBS8suPN` |
| permit-required | `U7TpJRdUzcZyVROa8REu` |
| estimate-sent | `YuJqzXTtH4q9CVJ59ECt` |
| contract-signed | `QkhllDpMCIJNJX8OZQv2` |
| job-complete | `qpC8wzulPhZsCHAuvoYh` |
| review-requested | `qpIBny8d4F8gz8tuBomw` |
| review-received | `O3gUpLnFYAWajXHI6Rjq` |
| referral | `RUaLx25zNm1SorRoCAbT` |
| neighbour-campaign | `F5SyEexj6eMJgpUtcKPQ` |
| annual-trimming-due | `YjzoI2ELuhkNMtQPW8PF` |
| cold-lead | `cFXfTaMKe5fz0ltYFREJ` |
| no-show | `pyOVONgiyL12GalkHZen` |
| google-lsa | `sylDpQPo9FL6FnPbNUzm` |
| storm-lead | `lPiq01S6cCivGMDTQ8KY` |
| property-manager | `uG7U7hQIYnMMsQFziZFK` |
| hoa | `miadFyVKbcoVeaWPTSzm` |
| repeat-customer | `K5z5D7Z9VZXLipfN6wHW` |
| facebook-ad | `PPdgZeehp7o93hpnUuyF` |

---

## PHASE 5: WORKFLOW SPECIFICATIONS

> **Note:** Workflows must be built manually in the GHL Workflow Builder UI, or via the GHL Workflow API if access is available. The specs below are complete build-ready blueprints - exact SMS/email copy, trigger logic, timing, and branching included.

---

### ✅ WORKFLOW 1: Missed Call Text Back - NATIVE GHL SETTING (Not a Workflow)

**Do NOT build this as a workflow.** Use GHL's built-in MCTB feature instead.

**How to enable:**
1. Go to **Settings → Phone Numbers**
2. Click on your phone number
3. Click the **"Voicemail & Missed Call TextBack"** tab
4. Check **"Enable Missed call textback"** ✅
5. Click **"Customize"** and paste the message below

**Customized message for this trade:**
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call - tree emergency or need a free assessment? Reply YES and we'll call you right back 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Emergency Lead - Speed to Dispatch

**Trigger:** Contact tag (filter: tag added = emergency-removal)
**Pipeline:** Tree Service - Emergency (Stage: New Emergency Call)

**Step 1 - Immediately Send SMS:**
> "⚡ Emergency Tree Crew - we received your request! To get a crew to you ASAP, reply with:
> 1. Your address
> 2. Is the tree on your house, power line, or blocking the road? (Yes/No)
> 3. Any photos you can send?
> We'll respond within 15 minutes."

**Step 2 - Immediately Create Internal Task:**
> Title: "EMERGENCY LEAD - Call Now: {{contact.firstName}} {{contact.lastName}}"
> Due: Immediately
> Assign to: Account owner

**Step 3 - Immediately Send Internal Email/Notification to owner:**
> Subject: "🚨 EMERGENCY TREE LEAD - {{contact.firstName}} {{contact.phone}}"
> Body: "Emergency tree lead just came in. Contact immediately. Lead source: {{contact.lead_source}}. Phone: {{contact.phone}}."

**Step 4 - Wait 15 minutes (if no reply from contact)**

**Step 5 - If no reply, Send SMS:**
> "Still with you! Our crew is ready to roll. Is this an active emergency? Reply YES and we'll call you right now."

**Step 6 - Wait 5 minutes**

**Step 7 - If contact replies YES, Send SMS:**
> "✅ Connecting you with our crew lead now. You'll receive a call in the next 5 minutes."

**Step 8 - Move opportunity to Stage: Dispatched**

**Step 9 - After dispatch confirmed (manual stage move to "On-Site Assessment"), Send SMS:**
> "Our crew is on the way! We'll document everything for your insurance claim if needed. Any questions? Reply here."

**Step 10 - Wait 24 hours after job completion (manual stage move to "Cleanup Complete")**

**Step 11 - Send SMS:**
> "The crew was glad to help after the storm! If you need anything documented for your insurance claim, just let us know. We work with adjusters regularly. 🌲"

---

### Workflow 3: Estimate Appointment Confirmation

**Trigger:** Customer booked appointment (calendar: Free Tree Assessment)
**Tags applied:** `estimate-sent`

**Step 1 - Immediately Send SMS:**
> "✅ Confirmed! We're booked for your free tree assessment on {{appointment.startTime | date: '%A, %B %d'}} at {{appointment.startTime | time: '%I:%M %p'}}. We'll come to {{contact.address}}. If anything changes, call or reply here."

**Step 2 - Immediately Send Email:**
> **Subject:** Your Tree Assessment is Confirmed - [Company Name]
>
> Hi {{contact.firstName}},
>
> We're confirmed for your free tree assessment:
>
> 📅 **Date:** {{appointment.startTime | date: '%A, %B %d, %Y'}}
> ⏰ **Time:** {{appointment.startTime | time: '%I:%M %p'}}
> 📍 **Address:** {{contact.address}}
>
> What to expect:
> - Our ISA-trained crew lead will walk the property with you
> - We'll assess the tree(s), root zone, access conditions, and discuss your options
> - We'll provide a written estimate before we leave
>
> **Please have access to the property and any back gates unlocked.**
>
> If anything changes, reply here or call us.
>
> See you then!

**Step 3 - Wait until 24 hours before appointment**

**Step 4 - Send SMS (24hr reminder):**
> "Heads up - your free tree assessment is TOMORROW at {{appointment.startTime | time: '%I:%M %p'}} at {{contact.address}}. We're looking forward to seeing your trees! - [Company Name]"

**Step 5 - Wait until 1 hour before appointment**

**Step 6 - Send SMS (1hr reminder):**
> "Our crew is heading your way! Assessment at {{contact.address}} at {{appointment.startTime | time: '%I:%M %p'}}. Be there shortly."

---

### Workflow 4: No-Show Recovery

**Trigger:** Appointment status (filter: no-show) OR Contact tag (filter: tag added = no-show)
**Tags applied:** `no-show`

**Step 1 - Wait 30 minutes after missed appointment**

**Step 2 - Send SMS:**
> "Hey {{contact.firstName}}, we came out for your tree assessment today but didn't catch you. No worries - want to reschedule? Reply and we'll get you back on the calendar. {{calendar.freeTreeAssessment.link}}"

**Step 3 - Wait 24 hours (if no response)**

**Step 4 - Send SMS:**
> "Still happy to come by for that free tree assessment, {{contact.firstName}}. Just let us know when works best. Reply or book here: {{calendar.freeTreeAssessment.link}}"

**Step 5 - Wait 7 days (if still no response)**

**Step 6 - Send SMS:**
> "Last check-in, {{contact.firstName}} - we'd still love to assess those trees for you. Free, no pressure. Book any time: {{calendar.freeTreeAssessment.link}}"

**Step 7 - If no response after Day 7 → Add tag `cold-lead` → Remove from active sequences**

---

### Workflow 5: Estimate Follow-Up Sequence (5-step, 21 days)

**Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent, Residential pipeline)
**Tags applied:** `estimate-sent`

**Step 1 - Day 0 (immediately) - Send Email:**
> **Subject:** Your Tree Service Estimate - [Company Name]
>
> Hi {{contact.firstName}},
>
> Thank you for having us out! Your estimate for {{contact.job_type}} at {{contact.address}} is ready.
>
> A few things worth knowing:
> - We're fully insured - your property is protected
> - All wood and brush is chipped and removed from site (or left as mulch - your call)
> - ISA-compliant pruning and removal practices on every job
>
> **Estimate Total: {{contact.estimate_amount}}**
>
> Questions? Reply here or call us directly.
>
> Ready to move forward? Just reply YES and we'll get you on the schedule.
>
> - [Company Name]

**Step 2 - Day 0 (immediately) - Send SMS:**
> "Hey {{contact.firstName}}! Your tree estimate is in your inbox from [Company Name]. Any questions, just reply! We can usually fit you in within the week."

**Step 3 - Wait 2 days**

**Step 4 - Day 2 - Send SMS:**
> "Hey {{contact.firstName}}, just checking in on your estimate for {{contact.job_type}}. Any questions about the scope or pricing? Happy to walk through it. - [Company Name]"

**Step 5 - Wait 2 days**

**Step 6 - Day 4 - Send SMS:**
> "Still available for your {{contact.job_type}} job! We have openings this week/next week. Want to lock in a date? Reply YES and we'll get you on the schedule."

**Step 7 - Wait 3 days**

**Step 8 - Day 7 - Send Email:**
> **Subject:** Last check-in - [Company Name]
>
> Hi {{contact.firstName}},
>
> Just a final check-in on your estimate. We're filling our schedule quickly - if you'd like to move forward, now is a great time to book before the calendar fills.
>
> If the timing doesn't work right now, no worries - we'll follow up when schedules open up.
>
> [Link to book or approve estimate]
>
> Thanks, [Company Name]

**Step 9 - Day 7 - Send SMS:**
> "Quick heads-up {{contact.firstName}} - our pricing on your estimate is good for another 3 days. Spring bookings fill fast. Want us to lock you in? Reply YES."

**Step 10 - Wait 14 days (Days 7-21, no response)**

**Step 11 - Day 21 - Send SMS (final):**
> "Last check-in, {{contact.firstName}}. Still interested in getting those trees taken care of? Whenever you're ready, we're here. - [Company Name]"

**Step 12 - If no response after Day 21 → Add tag `cold-lead` → Move stage to "Follow-Up Active" → Remove from active sequence**

---

### Workflow 6: Post-Job Review + Neighbour Campaign

**Trigger:** Pipeline stage changed (filter: new stage = Cleanup Complete or Paid, Residential or Stump pipeline)
**Tags applied:** `job-complete`, `review-requested`

**Step 1 - Wait 24 hours**

**Step 2 - Send SMS (review request):**
> "Hey {{contact.firstName}}! The crew just finished up - hope everything looks great! Would you mind leaving us a quick Google review? It helps families in your area find a trusted tree service. [Google Review Link] - Thanks! 🙏"

**Step 3 - Wait 72 hours (if no review)**

**Step 4 - Send SMS:**
> "Hi again! Just wanted to make sure everything was 100% with your {{contact.job_type}}. If you have a moment, a quick review means the world to our crew: [Google Review Link] 🙏"

**Step 5 - Wait 2 days**

**Step 6 - Send Email:**
> **Subject:** How did we do? - [Company Name]
>
> Hi {{contact.firstName}},
>
> Hope the {{contact.job_type}} went smoothly and the yard is looking great!
>
> If you were happy with our work, a Google review helps us stay busy and keeps our crew working. It takes 30 seconds: [Google Review Link]
>
> Also - if you have any other trees that need attention, we offer a free annual canopy assessment for returning clients. Just reply to book.
>
> Thanks for choosing us!

**Step 7 - Send internal task (Neighbour Campaign):**
> "NEIGHBOUR CAMPAIGN: Send SMS to nearby contacts for job at {{contact.address}}. Use the neighbour campaign template."

**Step 8 - Update custom field `Neighbour Campaign Sent` = Yes**

**Neighbour Campaign SMS (send manually or via smart list to nearby contacts):**
> "Hi! We're working on a tree job right next door at {{contact.address}}. If you've been thinking about getting your trees assessed, we can swing by for a FREE look while we're in the neighbourhood. Reply YES and we'll knock on your door! - [Company Name]"

---

### Workflow 7: Unhappy Customer Recovery

**Trigger:** Customer replied (with keyword filter: TERRIBLE, UNHAPPY, AWFUL, REFUND, COMPLAINT) OR Contact tag (filter: tag added = unhappy-customer)

**Step 1 - Immediately Send Internal Alert Email to owner:**
> **Subject:** ⚠️ UNHAPPY CUSTOMER - {{contact.firstName}} {{contact.lastName}}
>
> An unhappy customer response was detected.
>
> Contact: {{contact.firstName}} {{contact.lastName}}
> Phone: {{contact.phone}}
> Email: {{contact.email}}
> Job Type: {{contact.job_type}}
>
> IMMEDIATE ATTENTION REQUIRED. Call this customer before responding via any automated channel.

**Step 2 - Immediately Create Task:**
> "PRIORITY: Call unhappy customer {{contact.firstName}} within 1 hour - {{contact.phone}}"

**Step 3 - Remove contact from ALL active automated sequences**

**Step 4 - DO NOT send any further automated messages until task is marked complete**

> ⚠️ NOTE: No automated outbound SMS or email to unhappy customer. Human response only.

---

### Workflow 8: Storm Alert Campaign (Manual Trigger)

**Trigger:** Scheduler (manual activation by owner after major storm event, or date-based)
**Audience:** Smart List "Storm Response Target" (all residential contacts in service area)
**Activation timing:** Within 2–4 hours of storm event

**Step 1 - Send SMS Blast (to full residential list):**
> "⛈ Attention [City] residents - [Company Name] is deployed for storm response. If you have downed limbs, split canopies, or trees on structures, we're responding NOW. Call [phone] or reply here for priority scheduling. Emergency crews available 24/7."

**Step 2 - Send Email Blast (same list, same send time):**
> **Subject:** Storm Response - Emergency Tree Crews Available Now in [City]
>
> Hi {{contact.firstName}},
>
> The storm that hit [City] last night has left a lot of damage across the area. Our emergency crews are actively responding to:
> - Tree-on-structure emergencies
> - Downed limbs blocking driveways and roads
> - Hanging widow-makers threatening safety
> - Root failures with exposed root flares
>
> **If you're affected, call us now:** [phone]
>
> We document all damage for insurance claims and work directly with adjusters. Photos, scope-of-work letters, and liability coverage all included.
>
> **This is our busiest time - book now to secure a crew.**
>
> [Emergency Booking Link]
>
> Stay safe, [Company Name]

**Step 3 - Wait 24 hours**

**Step 4 - Send SMS to non-responders:**
> "Still helping [City] recover from the storm. A few crew slots still open this week. Reply CREW if you need help - we'll get back to you within the hour."

**Step 5 - Wait 48 hours**

**Step 6 - Send Email to non-responders (Day 3):**
> **Subject:** Still cleaning up storm damage in [City]
>
> Hi {{contact.firstName}},
>
> If you had trees down or limbs in your yard, we can usually fit remaining jobs within a few days. Book here: [Emergency Booking Link]

**Step 7 - After Day 7, non-responders → Add tag `cold-lead` → move to 30-day follow-up**

> **Owner Setup Instructions:**
> - Pre-build the smart list "Storm Response Target" filtering by residential client tag + city/postal code
> - Owner activates by opening the workflow, editing the city/date tokens, and clicking "Run Now"
> - Best send time: 2:00 PM same day as storm event for maximum open rates

---

### Workflow 9: Annual Trimming Reminder (Spring and Fall)

**Trigger (Spring):** Contact tag (filter: tag added = annual-trimming-due) — Scheduler set for March or April
**Trigger (Fall):** Contact tag (filter: tag added = annual-trimming-due) — Scheduler set for October or November
**OR:** Custom date reminder (select Last Job Date field, set 11 months after)

**SPRING VERSION:**

**Step 1 - Send SMS:**
> "Hey {{contact.firstName}}! Spring is here and [Company Name] is booking canopy assessments for the season. Trees look different after dormancy - some need crown reduction, deadwood clearing, or structural pruning. Want us to swing by for a free assessment? Reply YES 🌿"

**Step 2 - Wait 14 days (if no response)**

**Step 3 - Send SMS:**
> "Hi {{contact.firstName}}! Just a heads-up - we're almost fully booked for spring. If you want to get on the schedule for tree trimming or a canopy check, now's the time. {{calendar.freeTreeAssessment.link}} or reply here."

**Step 4 - Send Email:**
> **Subject:** Time for your annual tree check-in? 🌲
>
> Hi {{contact.firstName}},
>
> It's been about a year since we worked on your property. Spring is the ideal time to assess your trees before summer storm season hits.
>
> Here's what we check during a canopy assessment:
> - Crown density and light penetration - is the canopy too heavy?
> - Deadwood - dead limbs are a safety hazard
> - Root flare exposure - buried root flares lead to girdling roots
> - Structural defects - included bark, co-dominant stems, cracks
> - Disease/pest - emerald ash borer, oak wilt, cankers, fungal indicators
>
> **Free assessments for returning clients.** Book here: {{calendar.freeTreeAssessment.link}}

**Step 5 - Wait 7 days (if still no response)**

**Step 6 - Send SMS (final):**
> "Last heads-up for the season, {{contact.firstName}}. Still happy to do a free assessment whenever you're ready. Just reply YES anytime. - [Company Name]"

**Step 7 - No response → Remove tag `annual-trimming-due` → Add tag `cold-lead` for season → Re-add `annual-trimming-due` in 6 months (for fall campaign)**

**FALL VERSION:**

**Step 1 - Send SMS:**
> "Hey {{contact.firstName}}, before the snow loads hit - now is the time to remove dead limbs and hazard trees. Ice and snow on a compromised canopy causes failures that cost 3x more to clean up in winter. Reply for a free assessment."

**Step 2 - Wait 14 days (if no response)**

**Step 3 - Send Email:**
> **Subject:** Before the snow loads hit - is your canopy ready?
>
> Hi {{contact.firstName}},
>
> Fall is the last window before winter to deal with:
> - Hazard trees that could fail under snow/ice load
> - Dead limbs (they snap without warning in winter)
> - Large conifers with dense crowns that catch snow
>
> We're booking canopy assessments and late-season pruning now. Don't wait until something falls.
>
> [Booking Link]

**Step 4 - Wait 7 days (if no response)**

**Step 5 - Send SMS (final nudge):**
> "Last call before winter, {{contact.firstName}}. Free assessment - no pressure. Just reply YES whenever you're ready. - [Company Name]"

---

### Workflow 10: Insurance Claim Workflow

**Trigger:** Contact changed (filter: Insurance Claim field updated to Yes) OR Contact tag (filter: tag added = insurance-claim)
**Pipeline:** Tree Service - Emergency (Stage: Insurance Follow-Up)

**Step 1 - Immediately Send SMS to contact:**
> "Hi {{contact.firstName}} - we've documented the storm damage at your property. We're compiling:
> ✅ Timestamped photos of the tree failure
> ✅ Written scope of work
> ✅ Our liability certificate for your adjuster
> ✅ Removal and disposal invoice
>
> We'll have everything ready within 24 hours. What's your claim number and adjuster's contact?"

**Step 2 - Immediately Create Internal Checklist Task:**
> Title: "INSURANCE CLAIM - {{contact.firstName}} {{contact.address}}"
>
> Checklist:
> - [ ] Capture 10+ time-stamped photos (tree position, root condition, damage to structure)
> - [ ] Identify tree species and approximate DBH
> - [ ] Document failure mechanism (wind shear / root plate failure / structural defect / included bark split / trunk decay)
> - [ ] Write scope of work letter using insurance-friendly language
> - [ ] Confirm business liability insurance certificate is current
> - [ ] Get claim number and adjuster name from homeowner
> - [ ] Send documentation package to homeowner

**Step 3 - Wait 24 hours**

**Step 4 - Send Email to contact (Insurance Documentation Package):**
> **Subject:** Your Storm Damage Documentation - [Company Name]
>
> Hi {{contact.firstName}},
>
> Attached is your complete storm damage documentation package for your insurance claim at {{contact.address}}:
>
> 1. **Site Assessment Report** - Tree species, DBH, estimated age, failure mechanism
> 2. **Photo Documentation** - Time-stamped photos of tree position, root flare, damage
> 3. **Scope of Work Letter** - Written in language your adjuster expects
> 4. **Certificate of Insurance** - Our $2M liability coverage
> 5. **Invoice** - Itemized by task for claim submission
>
> We work with adjusters from all major carriers. If they have questions, give them our number directly.
>
> [Company Name] | [Phone] | [Email]

**Step 5 - Wait 5 days (if no reply from contact)**

**Step 6 - Send SMS follow-up:**
> "Hey {{contact.firstName}}, just following up on your insurance claim. Did your adjuster receive the documentation package okay? Let us know if they need anything else from us."

**Step 7 - If claim resolved (manual field update or stage move) → Move to "Closed" → Add tag `job-complete`**

---

## FIELD KEY REFERENCE (for workflow variable usage)

| Custom Field | GHL Field Key | Variable Usage |
|---|---|---|
| Lead Source | `contact.lead_source` | `{{contact.lead_source}}` |
| Job Type | `contact.job_type` | `{{contact.job_type}}` |
| Service Category | `contact.service_category` | `{{contact.service_category}}` |
| Property Type | `contact.property_type` | `{{contact.property_type}}` |
| Tree Species | `contact.tree_species` | `{{contact.tree_species}}` |
| DBH | `contact.dbh_-_diameter_at_breast_height` | `{{contact.dbh_-_diameter_at_breast_height}}` |
| Hazard Level | `contact.hazard_level` | `{{contact.hazard_level}}` |
| Permit Required | `contact.permit_required` | `{{contact.permit_required}}` |
| Permit Number | `contact.permit_number` | `{{contact.permit_number}}` |
| Insurance Claim | `contact.insurance_claim` | `{{contact.insurance_claim}}` |
| Insurance Company | `contact.insurance_company` | `{{contact.insurance_company}}` |
| Estimate Amount | `contact.estimate_amount` | `{{contact.estimate_amount}}` |
| Contract Amount | `contact.contract_amount` | `{{contact.contract_amount}}` |
| Crew Assigned | `contact.crew_assigned` | `{{contact.crew_assigned}}` |
| Equipment Required | `contact.equipment_required` | `{{contact.equipment_required}}` |
| Review Requested | `contact.review_requested` | `{{contact.review_requested}}` |
| Review Received | `contact.review_received` | `{{contact.review_received}}` |
| Neighbour Campaign Sent | `contact.neighbour_campaign_sent` | `{{contact.neighbour_campaign_sent}}` |
| Annual Trimming Reminder | `contact.annual_trimming_reminder` | `{{contact.annual_trimming_reminder}}` |

---

## NEXT STEPS FOR MANUAL BUILD IN GHL UI

The following must be built manually in the GHL Workflow Builder (API workflow creation is not available in standard GHL plan):

1. **Workflow 1:** Missed Call Text Back - set trigger to "Customer Replied" + call status = missed
2. **Workflow 2:** Emergency Dispatch - set trigger to tag `emergency-removal` added
3. **Workflow 3:** Estimate Appointment Confirmation - set trigger to "Appointment Created" on Free Tree Assessment calendar
4. **Workflow 4:** No-Show Recovery - set trigger to "Appointment Status Changed" = No Show
5. **Workflow 5:** Estimate Follow-Up - set trigger to "Opportunity Stage Changed" = Proposal Sent
6. **Workflow 6:** Post-Job Review + Neighbour Campaign - set trigger to "Opportunity Stage Changed" = Cleanup Complete
7. **Workflow 7:** Unhappy Customer Recovery - set trigger to "Customer Replied" with keyword filters
8. **Workflow 8:** Storm Alert Campaign - set as manual-trigger workflow; owner activates from GHL mobile app
9. **Workflow 9:** Annual Trimming Reminder - set trigger to tag `annual-trimming-due` added OR date-based trigger
10. **Workflow 10:** Insurance Claim - set trigger to custom field `Insurance Claim` = Yes

---

## SMART LISTS TO BUILD (Manual - GHL UI)

1. **All Active Residential Leads** - Filter: Pipeline = Tree Service - Residential, Stage ≠ Paid/Closed
2. **All Past Residential Clients** - Filter: Tag = `job-complete`, Pipeline = Residential
3. **Storm Response Target** - Filter: Tag contains `residential` + assigned city/postal codes (edit at campaign time)
4. **Commercial Leads Active** - Filter: Pipeline = Tree Service - Commercial / Municipal, Stage ≠ Paid
5. **Estimate Sent - No Response** - Filter: Tag = `estimate-sent`, Last Activity > 7 days ago
6. **Emergency - Open / Unresolved** - Filter: Pipeline = Tree Service - Emergency, Stage ≠ Paid/Insurance Follow-Up closed

---

## BUILD NOTES & OBSERVATIONS

1. **GHL search_operations MCP tool returned empty results** for this sub-account. All Phase 1-4 builds were executed via direct GHL REST API calls using the Bearer token from the mcporter config.

2. **RADIO field type** works correctly in GHL API for Yes/No fields (confirmed working for all 6 RADIO fields).

3. **MONETORY data type** (note: GHL spells it without the "a") works for currency fields.

4. **Calendar API version:** Must use `Version: 2021-04-15` for calendar endpoints (not 2021-07-28).

5. **Pipeline API:** Stages can be created inline in the pipeline POST body - no separate stage creation call needed.

6. **Workflows:** GHL's public API does not expose workflow creation endpoints in the standard plan. All 10 workflow specs above are documented in full detail for manual build in GHL Workflow Builder UI.

---

*Build log generated: 2026-07-21*
*Sub-account: Tree Service Template | Location ID: GmFMWWCpsXE0oksic6VV*
