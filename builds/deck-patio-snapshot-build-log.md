# Deck & Patio GHL Snapshot — Build Log
**1APP Technologies Inc. | Confidential**
**Build Date:** July 21, 2026
**Sub-Account Location ID:** AVeFEPk8yZ1yiaWgfOOP
**API Token:** pit-34762dfe-6b1f-4363-b679-09f75923296b

---

## BUILD STATUS: ✅ COMPLETE

| Phase | Component | Status | Count |
|-------|-----------|--------|-------|
| Phase 1 | Custom Fields | ✅ Complete | 20 fields |
| Phase 2 | Pipelines | ✅ Complete | 4 pipelines |
| Phase 3 | Calendars | ✅ Complete | 3 calendars |
| Phase 4 | Tags | ✅ Complete | 34 tags |
| Phase 5 | Workflows (documented) | ✅ Complete | 12 workflows |

---

## PHASE 1: CUSTOM FIELDS

All 20 custom fields created successfully.

| # | Field Name | Type | GHL Field ID |
|---|-----------|------|-------------|
| 1 | Lead Source | SINGLE_OPTIONS (dropdown) | RzEm9TBrwGFiaXijkrrn |
| 2 | Job Type | SINGLE_OPTIONS (dropdown) | LQdeweuMmv8MZx2jTTyH |
| 3 | Service Category | SINGLE_OPTIONS (dropdown) | XAvSqlFOLjFE6cNlKZkE |
| 4 | Decking Material | SINGLE_OPTIONS (dropdown) | 9lvUXWMb6RFxM08M5Z91 |
| 5 | Railing Material | SINGLE_OPTIONS (dropdown) | G1OPvXoxqpmJOQxkPJSP |
| 6 | Permit Required | RADIO (Yes/No) | iCH6wsXL9uYpWZYUBU8M |
| 7 | Permit Number | TEXT | VAHn4VEzxS4AddJe5uLb |
| 8 | Design Approval Required | RADIO (Yes/No) | GzbyntbY49KP5bpDXGAi |
| 9 | Design Approved | RADIO (Yes/No) | hM1iekzOHMmsqO13NlBg |
| 10 | Estimated Square Footage | NUMERICAL | wjLhH7AAwPXjmV9KLBDb |
| 11 | Estimate Amount | MONETORY (currency) | x0lGv7NFYc9aPOL2T0Wz |
| 12 | Contract Amount | MONETORY (currency) | F9Mg7ZAw2pyohAdZLVGT |
| 13 | Deposit Paid | RADIO (Yes/No) | xdZXfRA4urJY93HWJ9E5 |
| 14 | Crew Assigned | TEXT | 9IscOor0kRR98Udj8ZnY |
| 15 | Material Lead Time | SINGLE_OPTIONS (dropdown) | xvNEOAbOG9vzHo786zpY |
| 16 | Build Start Date | DATE | y1xzF0Yq1T4A7Y3z0H1V |
| 17 | Build End Date | DATE | bNL2vb7Avckyy1mKPdWC |
| 18 | Review Requested | RADIO (Yes/No) | MUYFFnjeqVdAsUONcXMX |
| 19 | Review Received | RADIO (Yes/No) | sMUUziHEGEHVv7ULZWYb |
| 20 | Neighbour Campaign Sent | RADIO (Yes/No) | knim8KGFxj8MPQiyz0ss |

### Field Options

**Lead Source options:** Google LSA, Referral, Real Estate Agent, Houzz, Pinterest/Instagram, Door Knock, Facebook Ad, Repeat Customer, Property Manager, Builder/Developer

**Job Type options:** New Deck Build, Deck Repair, Deck Refinishing/Staining, Pergola/Gazebo, Patio Installation, Outdoor Kitchen, Fence Addition, Composite Upgrade, Railing Replacement, Commercial

**Service Category options:** New Build, Repair/Restoration, Pergola/Structure, Outdoor Living, Commercial

**Decking Material options:** Pressure Treated, Cedar, Composite (Trex/Fiberon), PVC, Hardwood, Aluminum, Unknown

**Railing Material options:** Wood, Composite, Aluminum, Glass, Cable, Wrought Iron, Unknown

**Material Lead Time options:** In Stock, 1-2 weeks, 2-4 weeks, 4+ weeks, Unknown

---

## PHASE 2: PIPELINES

All 4 pipelines created successfully.

### Pipeline 1: Deck - New Build
**Pipeline ID:** LnGu7X1caJSbn5q2zxhp
**Stages (19):**
1. New Lead (position 0)
2. Design Consultation Scheduled (position 1)
3. Consultation Complete (position 2)
4. Design Approved (position 3)
5. Proposal Sent (position 4)
6. Follow-Up Active (position 5)
7. Contract Signed / Deposit (position 6)
8. Permit Applied (position 7)
9. Permit Approved (position 8)
10. Materials Ordered (position 9)
11. Build Start (position 10)
12. Framing (position 11)
13. Decking (position 12)
14. Railing/Finishing (position 13)
15. Job Complete (position 14)
16. Invoice Sent (position 15)
17. Paid (position 16)
18. Review Requested (position 17)
19. Neighbour Campaign (position 18)

---

### Pipeline 2: Deck - Repair & Refinishing
**Pipeline ID:** vSqkvHaSZgfElXkc4u40
**Stages (11):**
1. New Lead (position 0)
2. Estimate Scheduled (position 1)
3. Estimate Complete (position 2)
4. Proposal Sent (position 3)
5. Follow-Up Active (position 4)
6. Work Scheduled (position 5)
7. Work In Progress (position 6)
8. Job Complete (position 7)
9. Invoice Sent (position 8)
10. Paid (position 9)
11. Review + Composite Upsell (position 10)

---

### Pipeline 3: Deck - Pergola / Outdoor Structure
**Pipeline ID:** Yht47jCj0HxpL7g5G77S
**Stages (12):**
1. New Inquiry (position 0)
2. Design Consultation (position 1)
3. Proposal Sent (position 2)
4. Follow-Up Active (position 3)
5. Contract Signed / Deposit (position 4)
6. Permit Applied (position 5)
7. Materials Ordered (position 6)
8. Build Start (position 7)
9. Build Complete (position 8)
10. Invoice Sent (position 9)
11. Paid (position 10)
12. Review + Referral (position 11)

---

### Pipeline 4: Deck - Commercial / HOA
**Pipeline ID:** o8F6xgLdbjKfGV8m1y6e
**Stages (11):**
1. New Prospect (position 0)
2. Site Assessment (position 1)
3. Proposal Submitted (position 2)
4. Contract Awarded (position 3)
5. Permit Applied (position 4)
6. Build Scheduled (position 5)
7. Build In Progress (position 6)
8. Inspection (position 7)
9. Job Complete (position 8)
10. Invoice Sent (position 9)
11. Paid (position 10)

---

## PHASE 3: CALENDARS

All 3 calendars created successfully.

| # | Calendar Name | Duration | Buffer | Calendar ID |
|---|--------------|----------|--------|------------|
| 1 | Free Design Consultation - Deck/Patio | 60 min | 30 min | mfkx3l0ga1aLqTyRc6kh |
| 2 | Deck Repair Estimate | 45 min | 15 min | oQi6wrtR57RESJvQKQe4 |
| 3 | Commercial Site Assessment | 90 min | 30 min | OBoI0JjOZOIIVEh3xDhu |

**Booking Links (after slug setup):**
- Design Consultation: `https://api.leadconnectorhq.com/widget/bookings/mfkx3l0ga1aLqTyRc6kh`
- Repair Estimate: `https://api.leadconnectorhq.com/widget/bookings/oQi6wrtR57RESJvQKQe4`
- Commercial Assessment: `https://api.leadconnectorhq.com/widget/bookings/OBoI0JjOZOIIVEh3xDhu`

**Manual configuration needed in GHL UI:**
- Set availability hours: Mon-Fri 9am-5pm (Design Consultation), Mon-Fri 8am-5pm (Repair Estimate), Mon-Fri 8am-4pm (Commercial)
- Assign team member/user to each calendar
- Configure form fields (name, email, phone, project type, address, sq footage)
- Set confirmation and reminder email/SMS sequences

---

## PHASE 4: TAGS

All 34 tags created successfully.

| Tag | ID |
|-----|-----|
| new-lead | 7EYBglFkiIPMSOmJ8rLT |
| new-deck-build | aRbNEsX5Nmyilf6AStyk |
| deck-repair | WPZNcvxYGqjfr0RQ1K8o |
| deck-refinishing | WOG2frwBEI6z67ol7JX8 |
| pergola-gazebo | 9bNXCMbIvkb0Xy7CFOqw |
| patio-install | TXct3m1kJIPqETW2Dois |
| outdoor-kitchen | blU67olJdNvHnmlsGPt3 |
| composite-deck | Dx16M8JR4o80S0ulIfL1 |
| composite-upsell-candidate | TiuIFHcsjtWKD3elPLAk |
| cedar-deck | cG2RQN3JkIVXh3XH7fvo |
| pressure-treated | SQMdXD3MqsvQqhUdrnwY |
| railing-replacement | MXLvyMqY04Nt1Hi3Htv5 |
| permit-required | nkA38r3M62Y8XWwtBYQS |
| permit-pending | bZEpYvBr5gATv95brJZK |
| design-pending | HNaPbcfD9csTtOIr3Cxi |
| design-approved | nKTPJrsauNSxLSza1YIx |
| material-on-order | x2U1svzQWEPUD5jpyXAy |
| estimate-sent | JqHAacODXOr46sxI6blf |
| deposit-paid | 0jTl1JOAFZxFSYTR766S |
| contract-signed | Dwn1U8YpuVOmuXG6KrIR |
| build-active | hdtv7fPTCD4GOAZsnVWD |
| job-complete | b21HnK4rksPu0hxd64IO |
| review-requested | Lo5oqH3pwrQRMFJfa5Uj |
| review-received | IENu04oqDKIAVDSZaDXY |
| referral | yvbFJjjhOLOd5T8OVDoY |
| neighbour-campaign | HKcyMiTAWEKnx4hgCen2 |
| cold-lead | imvsGbQVDs3qKlZcT0KW |
| no-show | 53J4TgCix2KN7JswYecq |
| google-lsa | CvxrTIOZk0rhUanYCroL |
| houzz-lead | o7L2OkCAh4od6TsnwC2K |
| real-estate-agent | fcGcr9Oy9zemsqORzrcU |
| repeat-customer | fa4VxGWED1TNBRPXqY2S |
| facebook-ad | AOWlylsPaSFu0kGQjYkc |
| annual-refinishing-due | r6VW66HSI34GqRi6Fd3B |

---

## PHASE 5: WORKFLOWS (Full Specifications)

> **Note:** GHL API does not support workflow creation via REST API. All 12 workflows must be built manually in the GHL UI using the specifications below. This document serves as the complete build spec for the workflow builder.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — looking for a deck or patio quote? Reply YES and we'll get right back to you 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Lead - Speed to Response

**Name:** `DECK — Speed to Lead`
**Trigger:** Contact created (from any source)
**Delay:** 0 minutes

**Step 1 — SMS (0 min):**
```
Hi {{contact.firstName}}! Thanks for reaching out to {{location.name}} about your deck project! I'm reviewing your request now and will call you within the next few minutes.
```

**Step 2 — Internal Task (0 min):**
- Task: "CALL NOW — New deck/patio lead: {{contact.firstName}} {{contact.lastName}} | {{contact.phone}}"
- Due: Immediately
- Assign to: Account owner

**Step 3 — SMS (5 min, if no reply):**
```
Hey {{contact.firstName}} — I just tried calling. I'd love to chat about your outdoor living project. What time works best for a quick call today? Or book directly here: [CALENDAR LINK]
```

**Step 4 — Email (1 hour, if no response):**
- Subject: `Your Deck Project — Let's Talk, {{contact.firstName}}`
- Body: Portfolio intro + booking link + "We build decks people can't stop talking about"

**Step 5 — SMS (24 hours):**
```
{{contact.firstName}} — still thinking about your deck? We're booking spring/summer projects now — spots fill up fast. Here's our latest work: [PORTFOLIO LINK]
```

**Step 6 — SMS (72 hours):**
```
{{contact.firstName}} — last reach out before I close your file. If you're still considering a deck or patio this season, here's our availability: [CALENDAR LINK]. No pressure either way — just don't want you to miss the season.
```

**If no response after Step 6:** Add tag `cold-lead`, remove tag `new-lead`

---

### Workflow 3: Design Consultation Confirmation

**Name:** `DECK — Design Consultation Confirmation`
**Trigger:** Customer booked appointment (calendar: Free Design Consultation - Deck/Patio)
**Pipeline:** Move to "Design Consultation Scheduled"

**Step 1 — Email (immediate):**
- Subject: `Your Free Deck Design Consultation is Confirmed — {{appointment.startTime}}`
- Body:
```
Hi {{contact.firstName}},

You're confirmed! Here are your appointment details:

📅 Date: {{appointment.startDate}}
⏰ Time: {{appointment.startTime}}
📍 Location: Your property at {{contact.address1}}

To make the most of our consultation, feel free to:
• Gather any inspiration photos (Houzz, Pinterest, Instagram)
• Think about how you plan to use the space (dining, lounging, grilling, entertaining)
• Note any concerns about sun exposure, privacy, or neighbour sightlines

We're looking forward to helping you build your dream outdoor living space!

— {{location.name}}
{{location.phone}} | {{location.email}}
```

**Step 2 — SMS (-24 hours before appointment):**
```
Reminder: Your free deck design consultation is tomorrow at {{appointment.startTime}}. {{user.firstName}} will be at your property. Have any inspiration photos ready (Houzz, Pinterest, Instagram) — it helps us nail your vision. See you then!
```

**Step 3 — SMS (-2 hours before appointment):**
```
On my way shortly for your deck consultation at {{appointment.startTime}}. Looking forward to seeing your space!
```

**Step 4 — SMS (+2 hours after appointment end):**
```
Great meeting you today, {{contact.firstName}}! I'm putting together your design concept — you'll have it within a few business days. Any questions in the meantime, just text me here.
```

**Tags:** Add `design-pending`
**Pipeline:** Move to "Consultation Complete"

---

### Workflow 4: No-Show Recovery

**Name:** `DECK — No-Show Recovery`
**Trigger:** Appointment status (filter: no-show)
**Delay:** 0 minutes

**Step 1 — SMS (30 min after missed appointment):**
```
Hey {{contact.firstName}} — we missed you at your deck consultation today! No worries at all. Want to reschedule? Here's our booking link: [CALENDAR LINK]
```

**Step 2 — SMS (24 hours later):**
```
{{contact.firstName}} — still want to get your deck project rolling? We can find another time that works for you: [CALENDAR LINK]. Spring/summer slots are filling up fast!
```

**Step 3 — Internal Task:**
- "No-show follow-up call: {{contact.firstName}} {{contact.lastName}}"
- Due: 1 business day

**Tags:** Add `no-show`

---

### Workflow 5: Design Approval Follow-Up

**Name:** `DECK — Design Approval Follow-Up`
**Trigger:** Pipeline stage changed (filter: new stage = Design Approved) OR Contact changed (filter: Design Approval Required = Yes)
**Goal:** Get design approval confirmed

**Step 1 — SMS (0 min):**
```
{{contact.firstName}} — your deck design is ready for your review! Once you approve, we can lock in your build date and get materials ordered. Have a look and let me know what you think: [DESIGN LINK]
```

**Step 2 — SMS (24 hours, if not approved):**
```
{{contact.firstName}} — just following up on your deck design. Any changes you'd like before we finalize? Happy to jump on a call to walk through it together.
```

**Step 3 — Email (48 hours, if not approved):**
- Subject: `Your Deck Design is Waiting for Your Approval`
- Body: Design summary + approval link + "We want to get your build scheduled as soon as possible!"

**Step 4 — SMS (72 hours, if not approved):**
```
{{contact.firstName}} — last nudge on your deck design approval. Want me to call you to walk through any questions? Just reply YES and I'll give you a ring.
```

**If approved:** Set custom field "Design Approved" = Yes, Add tag `design-approved`, Remove tag `design-pending`
**Pipeline:** Move to "Proposal Sent"

---

### Workflow 6: Estimate Follow-Up Sequence (5-step, 21 days)

**Name:** `DECK — Estimate Follow-Up Sequence`
**Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent) OR Contact tag (filter: tag added = estimate-sent)
**Duration:** 21 days

**Step 1 — Email (Day 0, immediate):**
- Subject: `Your Deck Estimate from {{location.name}}`
- Body: Full estimate summary with:
  - Project scope breakdown (decking, framing, footings, railing, stairs, fascia, lighting rough-in)
  - Material spec sheet
  - Project timeline overview
  - FAQ: "What happens next if I want to move forward?"
  - Booking link for follow-up questions

**Step 2 — SMS (Day 1):**
```
Hey {{contact.firstName}} — just making sure the estimate came through okay. Any questions on the materials or scope? Happy to walk you through it anytime — just text back.
```

**Step 3 — Email (Day 3):**
- Subject: `Composite vs. Pressure Treated — What's Right for You?`
- Body: Educational comparison:
  - Composite lifespan (25-50 years) vs pressure treated (12-18 years)
  - Maintenance cost comparison over 15 years
  - Home value impact
  - Warranty overview (Trex 25-year, Fiberon 50-year, AZEK 30-year)
  - "Questions? Reply to this email or text us."

**Step 4 — SMS (Day 5):**
```
{{contact.firstName}} — still holding your preferred start date for now. Spring/summer slots fill up quick around here. Let me know when you're ready to move forward!
```

**Step 5 — SMS (Day 10) — Social Proof:**
```
Just finished this deck nearby — thought you'd love it: [PORTFOLIO PHOTO LINK]. Your project scope is very similar. Still available to build yours!
```

**Step 6 — Email (Day 14):**
- Subject: `Are you still interested in your deck project, {{contact.firstName}}?`
- Body:
```
Hi {{contact.firstName}},

I want to make sure I hold time in our schedule for your project. Can you let me know if you're still moving forward, need more time, or went a different direction?

No hard feelings either way — just helps me plan my season properly.

— {{user.firstName}}
{{location.name}}
```

**Step 7 — SMS (Day 21) — Final:**
```
{{contact.firstName}} — I'll close your file after today since we haven't heard back. If the timing wasn't right, no worries — give me a call when you're ready. I'd love to build something great for you.
```

**If no response after Day 21:** Add tag `cold-lead`, move opportunity to "Closed Lost"

---

### Workflow 7: Permit Tracking Update

**Name:** `DECK — Permit Status Updates`
**Trigger:** Pipeline stage changed (filter: new stage = Permit Applied)
**Tags:** Add `permit-pending`

**Step 1 — SMS (Day 0 — immediately after permit submitted):**
```
Great news — we've submitted your building permit to the municipality. Expected review time is approximately 3-6 weeks. I'll keep you updated at every step. No news is good news!
```

**Step 2 — SMS (Day 7):**
```
Week 1 update on your permit: Still in review. These things take time — we're monitoring it daily. In the meantime, we're finalizing your materials and pre-staging for your project.
```

**Step 3 — SMS (Day 14, if still pending):**
```
Still waiting on your building permit — the municipality is running a few weeks right now, which is typical for the season. The moment it's approved, we'll contact you within the hour to lock in your start date.
```

**Step 4 — SMS (Day 21, if still pending):**
```
{{contact.firstName}} — permit still in review. We know the wait is frustrating — we're following up with the building department on your behalf. We'll have an update for you soon.
```

**When permit approved (trigger: pipeline moves to "Permit Approved"):**
- SMS (immediate): 
```
GREAT NEWS! 🎉 Your building permit has been approved! We're locking in your start date right now. Expect a call from us within the next 2 hours to confirm your schedule and get your build on the calendar!
```
- Remove tag `permit-pending`, Add tag `contract-signed`
- Internal Task: "Call client NOW — permit approved, lock in start date"

---

### Workflow 8: Build Start Notification

**Name:** `DECK — Build Start Notification`
**Trigger:** Pipeline stage changed (filter: new stage = Build Start) OR Custom date reminder (select Build Start Date field, set 1 day before)

**Step 1 — SMS (Day before build start):**
```
{{contact.firstName}} — we start your deck project tomorrow! 🛠️ A few things to have ready:
• Clear the work area if possible (patio furniture, planters, etc.)
• Ensure access to the backyard gate
• Our crew arrives between 7:30-8:00 AM

Any questions? Text or call us anytime. We're excited to get started!
```

**Step 2 — Email (Day before):**
- Subject: `Build Day Tomorrow — What to Expect`
- Body: Detailed build day prep guide including crew arrival time, site access, noise expectations, parking for material deliveries, and daily check-in process

**Step 3 — Tag:** Add `build-active`

---

### Workflow 9: Post-Build Review Request + Neighbour Campaign

**Name:** `DECK — Post-Build Review & Neighbour Campaign`
**Trigger:** Pipeline stage changed (filter: new stage = Job Complete or Paid)
**Tags:** Add `job-complete`

**Step 1 — SMS (Day 0 — immediately after job complete):**
```
{{contact.firstName}} — your deck/patio is done! 🎉 It was a pleasure working with you. Would you mind leaving us a quick Google review? It takes 60 seconds and helps us a lot: [GOOGLE REVIEW LINK]
```

**Step 2 — Email (Day 1):**
- Subject: `Your Care Guide for Your New Deck`
- Body: Professional post-build care guide:
  - Composite: Annual wash, avoid rubber mats, avoid wire brush
  - Pressure treated: Annual inspection, stain/seal every 2-3 years, check joist hangers
  - Cedar: Seal within 30 days, annual maintenance staining
  - Warranty information (Trex 25-year fade/stain, Fiberon 50-year, etc.)
  - "Save this email — it's your deck's maintenance bible."

**Step 3 — SMS (Day 3):**
```
Hope you're enjoying the new deck! If you have 60 seconds, a Google review means the world to us: [GOOGLE REVIEW LINK] 🙏
```

**Step 4 — SMS (Day 7) — Referral + Neighbour:**
```
{{contact.firstName}} — if your neighbours ask about your deck, send them our way! We're offering a $250 referral credit for every project you refer us to this season. Thanks for being such a great client! 🙏
```

**Step 5 — Internal Task (Day 7):**
- "NEIGHBOUR CAMPAIGN — Drop door hangers within 5-house radius of {{contact.address1}}"
- Door hanger copy: "We just built the deck at [nearby address]. Free design consultation: [QR/booking link]"

**Tags:** Add `review-requested`, Add `neighbour-campaign`
**If review received:** Add tag `review-received`

---

### Workflow 10: Unhappy Customer Recovery

**Name:** `DECK — Unhappy Customer Recovery`
**Trigger:** Contact tag (filter: tag added = complaint) OR Customer replied (with keyword filter for negative sentiment)
**⚠️ INTERNAL ONLY — No automated client-facing messages**

**Step 1 — Internal SMS to Owner (immediate):**
```
⚠️ ALERT: Potential unhappy customer — {{contact.firstName}} {{contact.lastName}} | {{contact.phone}}. Review conversation and call ASAP.
```

**Step 2 — Internal Task (immediate):**
- "URGENT: Unhappy customer call — {{contact.firstName}} {{contact.lastName}}"
- Priority: High
- Due: Within 2 hours

**Step 3 — Internal Email to Owner:**
- Subject: `[ACTION REQUIRED] Customer Issue — {{contact.firstName}} {{contact.lastName}}`
- Body: Contact details, pipeline stage, recent conversation summary

**Do NOT send any automated messages to the client. All communication must be personal and handled directly by the business owner.**

---

### Workflow 11: Composite Upsell (Post-Repair/Refinishing)

**Name:** `DECK — Composite Upgrade Pitch`
**Trigger:** Pipeline stage changed (filter: new stage = Review + Composite Upsell, Repair & Refinishing pipeline)
**Condition:** Only if Decking Material = Pressure Treated OR Cedar
**Tags:** Add `composite-upsell-candidate`

**Step 1 — Email (Day 7 post-job-complete):**
- Subject: `Is It Time to Upgrade to Composite? (Honest Answer)`
- Body:
```
{{contact.firstName}} — we just finished your deck repair/refinish, and it looks great. But I want to be straight with you: if your deck is more than 10 years old and pressure treated, you're going to keep spending money on it every couple of years.

Here's the math:
• Pressure treated deck: ~$800-1,200/year in maintenance x 15 years = $12,000-18,000
• Composite deck (Trex, Fiberon): $0 maintenance, 25-50 year warranty, adds 70-80% of cost back in home resale value

We can often apply what you've already paid toward a new composite build.

Want me to put together a free comparison quote? No obligation — just the numbers so you can make an informed decision.

— {{user.firstName}}
{{location.name}}
```

**Step 2 — SMS (Day 14):**
```
{{contact.firstName}} — did you get the composite upgrade info I sent? A lot of our clients who started with repairs ended up going composite and said it was the best decision they made. Happy to answer any questions: {{location.phone}}
```

**If interested:** Create new opportunity in "Deck - New Build" pipeline at "New Lead" stage

---

### Workflow 12: Seasonal Campaigns

#### 12A: Spring Build Push

**Name:** `DECK — Spring Surge Campaign`
**Trigger:** Scheduler (February 1 each year)
**Target contacts:** Tags: `cold-lead` OR `annual-refinishing-due` OR custom field indicates past client
**Tags:** Add `campaign-spring-push`

**Email (February 1):**
- Subject: `Spring Deck Season is Almost Here — Lock In Your Spot Now`
- Body:
```
{{contact.firstName}} — we start booking our spring build calendar in February. Last year we were fully booked by April 15.

If you've been thinking about a new deck, patio, or pergola for this summer, now is the time to secure your spot. Early bookings also lock in current pricing before material costs go up.

🏗️ Free design consultation: [CALENDAR LINK]

— {{user.firstName}}
{{location.name}}
```

**SMS (February 15):**
```
Deck season spots filling fast. We're already booking April/May. Book your free consultation: [CALENDAR LINK]
```

**SMS (March 1):**
```
{{contact.firstName}} — March is here. Time to get your deck done before summer. We can usually get permits filed, materials ordered, and build started within 6-8 weeks of signing. Want a May deck? Book now: [CALENDAR LINK]
```

**Email (March 15):**
- Subject: `Last Call for a May/June Deck Build`
- Body: Urgency + recent project photos + booking link

---

#### 12B: Fall Before-Winter Urgency

**Name:** `DECK — Fall Urgency Campaign`
**Trigger:** Scheduler (August 15 each year)
**Target contacts:** Open leads, unbooked prospects, `estimate-sent` without `contract-signed`

**Email (August 15):**
- Subject: `Get Your Deck Done Before the Snow Hits`
- Body:
```
{{contact.firstName}} — summer isn't over yet. We have limited spots left in our September/October build calendar.

A fall deck build means you're ready to enjoy it the minute next spring hits — and you lock in this year's pricing.

📅 Current availability: [CALENDAR LINK]
```

**SMS (September 1):**
```
{{contact.firstName}} — last realistic window to start and finish a deck before winter. We have limited spots left in September. Want one? [CALENDAR LINK]
```

**SMS (September 15):**
```
Weather window closing. Our last build slots of the season are almost gone. Contact us today if you want a deck ready for next spring: {{location.phone}}
```

---

## TECHNICAL NOTES & BUILD LESSONS

### GHL API Quirks Encountered

1. **DROPDOWN type is `SINGLE_OPTIONS` in GHL API** — not "DROPDOWN" or "dropdown"
2. **MONETARY type is `MONETORY` in GHL API** — note the deliberate typo in the GHL API spec
3. **RADIO fields require `options` array** — not `picklistOptions`
4. **Pipeline stages require explicit `position` integer** — omitting it causes 422 error
5. **Calendar `calendarType` uses lowercase `"event"`** — not "EVENT"
6. **MCP search_operations returns empty** — fall back to direct REST API for all operations
7. **Pipelines API endpoint:** `POST /opportunities/pipelines` (not `/pipelines/`)
8. **Custom fields endpoint:** `POST /locations/{locationId}/customFields`
9. **Tags endpoint:** `POST /locations/{locationId}/tags`
10. **Calendars endpoint:** `POST /calendars/` (note trailing slash)

### Items Requiring Manual GHL UI Configuration

1. **Calendar availability hours** — set Mon-Fri 9am-5pm in each calendar's availability settings
2. **Calendar user assignment** — assign team member to each calendar
3. **Calendar form fields** — add custom intake form to each booking calendar
4. **All 12 workflows** — must be built in GHL Workflow Builder UI (API doesn't support workflow creation)
5. **Pipeline win/lost probability** — adjust stage win probabilities as needed
6. **Custom field placement** — drag fields into contact detail view layout in GHL settings

### Pre-Existing Data

- 1 existing pipeline ("Marketing Pipeline") was present before build — kept as-is
- No existing custom fields before build
- No existing calendars before build
- No existing tags before build

---

## ONBOARDING CHECKLIST (When Deploying to Client)

### Information to Collect
- [ ] Business name, phone, email
- [ ] Service area (city/cities)
- [ ] GHL phone number for SMS/calls
- [ ] Google Review link
- [ ] Portfolio photos (minimum 10 project photos)
- [ ] Contractor first name for SMS personalization
- [ ] Referral incentive amount (default: $250)
- [ ] Do they handle permits themselves? (yes/no)
- [ ] Services offered (new builds, repair, refinishing, pergola, patio, outdoor kitchen)

### Customization Required
- [ ] Replace all `[CALENDAR LINK]` placeholders with actual booking URLs
- [ ] Replace `[GOOGLE REVIEW LINK]` with client's Google Business review link
- [ ] Replace `[PORTFOLIO LINK]` / `[PORTFOLIO PHOTO LINK]` with actual portfolio
- [ ] Set correct service area in calendar settings
- [ ] Upload portfolio photos to email templates
- [ ] Configure seasonal campaign dates (adjust for local climate)
- [ ] Set lead notification to contractor's phone/email
- [ ] Add team member users to sub-account
- [ ] Assign calendars to users
- [ ] Build all 12 workflows in GHL UI using specs above

---

*Build log generated by 1APP Technologies | Deck & Patio Snapshot v1.0 | July 2026*
