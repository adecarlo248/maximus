# KCIP / Pool + Landscaping Workflow Pack

Prepared for Tony DeCarlo / 1APP  
Trade: Custom inground pools, pool service, landscaping, concrete, turf, stone, cabanas, sport courts

## Recommended Build

**Base plan:** 1APP Growth  
**Monthly:** $499/mo  
**Setup:** starts at $999  

**Increase setup when adding:**
- Website rebuild / revamp
- QuickBooks automation
- Advanced Revenue Engine tools
- Large contact import / cleanup
- More than 3–5 custom workflows
- Multiple pipelines or separate service divisions

---

# 1. Core Business Goal

KCIP does not need “more software.” KCIP needs a front-office machine that:

1. Captures every lead from phone, website, Facebook, Google, and referrals.
2. Responds instantly when Scott or the crew are busy.
3. Qualifies the job before wasting time.
4. Books estimate appointments into controlled calendar blocks.
5. Tracks every opportunity from first contact to booked job.
6. Follows up after quotes automatically.
7. Reactivates past customers for seasonal pool services.
8. Builds reviews and referrals after completed jobs.

---

# 2. Suggested Pipelines

## Pipeline A — New Project / Estimate Pipeline

Use for new builds, revamps, liners, concrete, turf, stone, cabanas, sport courts, and larger backyard jobs.

Stages:
1. New Lead
2. Auto-Reply Sent
3. Needs Qualification
4. Qualified Lead
5. Estimate Booked
6. Estimate Completed
7. Quote Sent
8. Follow-Up Active
9. Deposit / Job Won
10. Lost / Not Now
11. Future Season Nurture

## Pipeline B — Pool Service Pipeline

Use for openings, closings, inspections, leak detection, repairs, and urgent service.

Stages:
1. New Service Request
2. Urgency Checked
3. Service Booked
4. Service Reminder Sent
5. Service Completed
6. Invoice / Payment Follow-Up
7. Review Request Sent
8. Seasonal Reminder List

## Pipeline C — Past Customer / Reactivation Pipeline

Use for seasonal and repeat revenue.

Stages:
1. Past Customer
2. Spring Opening Campaign
3. Summer Service Campaign
4. Fall Closing Campaign
5. Upgrade Opportunity
6. Referral Requested
7. Rebooked
8. Dormant

---

# 3. Recommended Calendars

## Calendar 1 — Backyard Estimate

Purpose: Larger project estimates.

Use for:
- New inground pool
- Pool revamp
- Liner replacement
- Concrete / patio
- Turf / putting green
- Armour stone / masonry
- Cabana / lighting
- Sport court

Suggested settings:
- Controlled weekly estimate blocks
- No same-day booking unless approved
- Buffer time between appointments
- Required intake form before booking
- SMS + email confirmation
- 24-hour reminder
- 2-hour reminder

## Calendar 2 — Pool Service Visit

Purpose: Openings, closings, leak detection, service calls.

Suggested settings:
- Shorter appointment blocks
- Service-area routing if possible
- Urgent service option
- Weather/reschedule messaging

## Calendar 3 — Phone Consultation / Discovery Call

Purpose: Quick calls before booking an in-person estimate.

Use when:
- Customer is unsure what they need
- Large project needs pre-qualification
- Customer asks pricing before details are known

---

# 4. Custom Fields

## Contact Fields

- Lead Source
- Service Category
- Project Type
- Town / Service Area
- Address
- Preferred Contact Method
- Best Time To Reach
- Urgency Level
- Desired Timeline
- Budget Range
- Existing Pool? yes/no
- Pool Type
- Project Photos Submitted? yes/no
- Quote Sent Date
- Follow-Up Status
- Won/Lost Reason
- Seasonal Service Customer? yes/no
- Last Opening Date
- Last Closing Date
- Review Requested? yes/no
- Referral Asked? yes/no

## Opportunity Fields

- Estimated Job Value
- Estimate Appointment Date
- Quote Amount
- Deposit Status
- Expected Start Date
- Crew / Installer Assigned
- Materials Needed
- Permit Required? yes/no
- Follow-Up Attempt Count

---

# 5. Tags

## Lead Source Tags

- source_website
- source_facebook
- source_google
- source_referral
- source_phone_call
- source_missed_call
- source_web_chat
- source_existing_customer

## Service Tags

- service_new_pool
- service_pool_revamp
- service_liner_replacement
- service_leak_detection
- service_pool_opening
- service_pool_closing
- service_concrete
- service_turf
- service_putting_green
- service_armour_stone
- service_masonry
- service_cabana
- service_lighting
- service_sport_court

## Status Tags

- lead_new
- lead_qualified
- estimate_booked
- quote_sent
- followup_active
- deposit_received
- job_won
- job_lost
- seasonal_customer
- review_requested
- referral_requested

---

# 6. Workflow 1 — Missed Call Text Back

## Trigger

Customer calls KCIP and call is missed.

## Goal

Catch the lead before they call a competitor.

## Actions

1. Send SMS immediately:

> Hey, thanks for calling KCIP — sorry we missed you. Are you looking for pool service, liner/revamp, new pool install, concrete/turf, or a full backyard project?

2. Add tag: `source_missed_call`
3. Create / update contact
4. Create opportunity in correct pipeline
5. Notify Scott / team
6. If customer replies, pause automated follow-up and mark as engaged
7. If no reply after 10 minutes, send second SMS:

> Just checking — if you send over what you need and your town, we can point you in the right direction and let you know the next step.

8. If no reply after 24 hours, send final soft follow-up:

> Still need help with your pool or backyard project? Reply here anytime and we’ll get you looked after.

---

# 7. Workflow 2 — Website Quote Intake

## Trigger

Customer submits quote form or web chat.

## Required form questions

- First name
- Last name
- Phone
- Email
- Town / service area
- Service needed
- Desired timeline
- Project details
- Upload photos if available
- Preferred contact method

## Actions

1. Send confirmation SMS:

> Thanks {{contact.first_name}}, we got your request. KCIP will review the details and help you with the right next step. If you have photos, you can send them here.

2. Add service tag based on selected service
3. Create opportunity
4. Assign pipeline:
   - Big project → New Project / Estimate Pipeline
   - Service request → Pool Service Pipeline
5. Notify team with submitted details
6. If high-value category, send booking link:

> Based on what you selected, the best next step is a quick estimate appointment. You can grab a time here: {{calendar.link}}

7. If urgent service, notify team immediately.

---

# 8. Workflow 3 — AI Voice Receptionist

## Trigger

After-hours, overflow, or unanswered incoming call.

## AI Voice Purpose

The AI should not try to sell the job. It should capture clean information and route the lead.

## AI Voice Script Outline

Opening:

> Thanks for calling Kawartha Custom Inground Pools and Landscaping. I can help get the right details over to the team. Are you calling about pool service, a new pool or backyard project, or something else?

Qualification questions:

1. What service are you looking for?
2. What town or area are you located in?
3. Is this urgent or are you planning ahead?
4. Do you already have a pool or is this a new project?
5. What timeline are you hoping for?
6. What is the best phone number and email for the team to follow up?
7. Would you like to book an estimate or have someone call you first?

Routing:

- Urgent leak / service issue → immediate team notification
- Large project → estimate calendar / callback
- Seasonal opening/closing → service pipeline
- Unknown request → callback task

---

# 9. Workflow 4 — Estimate Booking Confirmation

## Trigger

Customer books an estimate appointment.

## Actions

1. Move opportunity to `Estimate Booked`
2. Add tag `estimate_booked`
3. Send SMS confirmation:

> You’re booked with KCIP for {{appointment.start_time}}. If you have photos of the pool/backyard area, send them here before the appointment — it helps us prepare.

4. Send email confirmation
5. Internal notification to team
6. 24-hour reminder:

> Reminder: KCIP is scheduled for your estimate tomorrow at {{appointment.start_time}}. Reply here if anything changes.

7. 2-hour reminder:

> KCIP estimate reminder: we’ll see you around {{appointment.start_time}} today.

---

# 10. Workflow 5 — Quote Sent Follow-Up

## Trigger

Quote is marked as sent.

## Goal

Prevent good quotes from dying because nobody followed up.

## Actions

### Day 1

> Hey {{contact.first_name}}, just checking that you received the quote from KCIP. Any questions about the scope, timing, or next steps?

### Day 3

> Quick follow-up — do you want us to keep this project active for scheduling, or are you still reviewing options?

### Day 7

> We know backyard projects are a big decision. If helpful, we can walk through the quote with you and tighten the scope around your priorities.

### Day 14

> Should we keep this open, adjust the quote, or revisit later in the season? Just reply with what works best.

## Stop Conditions

Stop sequence if:
- Customer replies
- Customer books call
- Deposit received
- Opportunity marked lost

---

# 11. Workflow 6 — Seasonal Pool Opening Campaign

## Trigger

March / April, or manual campaign launch.

## Audience

Past customers, pool service customers, opening/closing customers.

## SMS 1

> Spring is coming fast — KCIP is starting to organize pool openings. Want us to get you on the list before the schedule fills up?

## SMS 2 — 5 days later

> Quick reminder: if you want KCIP to handle your pool opening this season, reply OPEN and we’ll help get you scheduled.

## SMS 3 — 10 days later

> Last check before we move on — do you need your pool opening booked this spring?

## Actions

- If reply OPEN → send booking/service flow
- If no reply → leave in seasonal list
- If booked → move to Pool Service Pipeline

---

# 12. Workflow 7 — Fall Closing Campaign

## Trigger

Late August / September.

## SMS 1

> KCIP is organizing fall pool closings. Want to get your closing scheduled before the busy season hits?

## SMS 2

> Pool closing reminder — reply CLOSE if you want us to help get you on the schedule.

## SMS 3

> Last check for this season — do you still need your pool closing booked?

---

# 13. Workflow 8 — Completed Job Review Request

## Trigger

Job marked completed.

## SMS 1

> Thanks again for choosing KCIP. If you’re happy with the work, would you be willing to leave us a quick review? It helps local homeowners know who they can trust.

Include Google/Facebook review link.

## If positive response

> Really appreciate it. Here’s the link: {{review.link}}

## If negative response

> Thanks for letting us know. We’d rather fix the issue directly — what could we have done better?

## Actions

- Add tag `review_requested`
- Notify team if negative
- After review, send referral ask later

---

# 14. Workflow 9 — Referral Ask

## Trigger

7 days after positive review or completed job.

## SMS

> One more quick favour — if you know anyone planning a pool, liner, backyard, concrete, turf, or stone project, feel free to send them our way. Referrals are huge for a local business like KCIP.

## Actions

- Add tag `referral_requested`
- If referral received, create new lead and tag `source_referral`

---

# 15. Workflow 10 — Dormant Quote Reactivation

## Trigger

Quote sent 30–90+ days ago, not won/lost.

## SMS

> Hey {{contact.first_name}}, are you still thinking about the pool/backyard project we quoted, or should we close this out for now?

## If interested

Move to `Follow-Up Active` and notify team.

## If not now

Move to `Future Season Nurture`.

---

# 16. Website / Funnel Recommendation

If Tony sells a website revamp as an add-on, KCIP should get:

## Homepage Sections

1. Hero: “Custom Inground Pools & Backyard Transformations in Kawartha Lakes, Peterborough & Beyond”
2. Primary CTA: “Book Your Backyard Estimate”
3. Secondary CTA: “Request Pool Service”
4. Proof strip: awards, years in business, service area, guarantee
5. Service cards
6. Before/after gallery
7. Revamp / liner specialty section
8. Seasonal pool services section
9. Testimonials / reviews
10. FAQ
11. Booking CTA

## Dedicated Service Pages

- New Inground Pools
- Pool Revamps
- Liner Replacement
- Leak Detection
- Pool Openings / Closings
- Concrete / Patios
- Turf / Putting Greens
- Armour Stone / Masonry
- Cabanas / Lighting
- Sport Courts

## Website CTA Structure

Primary:
- Book Your Backyard Estimate

Secondary:
- Request Pool Service
- Send Project Photos
- Ask a Question

---

# 17. QuickBooks Automation Add-On

Possible automations:

1. When opportunity marked `Job Won`, create/update customer in QuickBooks.
2. When quote accepted, create estimate or invoice.
3. When invoice sent, trigger payment reminder sequence.
4. When paid, move opportunity to completed/paid.
5. Weekly unpaid invoice report.

Important: scope carefully. QuickBooks automation should increase setup fee because it needs testing, field mapping, and client-specific accounting rules.

---

# 18. Revenue Engine Add-On

Recommend Revenue Engine if KCIP wants:

- Social Planner
- Invoice tools
- Form Builder
- Survey Builder
- Trigger Links
- Advanced workflows
- Funnels
- Websites
- Blogs
- SMS/email templates
- Campaigns
- Reporting dashboards
- Heavier review/referral engine
- Monthly performance reporting

Positioning:

> Growth gets the front office organized. Revenue Engine turns the system into a marketing and operations machine.

---

# 19. Tony’s Meeting Close

Use this:

> I wouldn’t start by rebuilding everything. I’d start by fixing the lead leak: missed calls, quote requests, booking, follow-up, and seasonal reminders. That’s the Growth system. If you want the website rebuilt or QuickBooks connected, we scope that separately because that’s custom infrastructure — not a basic setup.

Then ask:

> If this captured even one extra serious project or saved you 5–10 hours of admin a month, would it be worth testing for 30 days?
