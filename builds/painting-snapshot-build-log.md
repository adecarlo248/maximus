# 🎨 Painting GHL Snapshot — Build Log
**Location ID:** uUOspt0oHkxmm53fklpX  
**Built by:** Maximus AI Subagent  
**Build Date:** 2026-07-21  
**Status:** Phases 1–4 COMPLETE | Phase 5 DOCUMENTED

---

## PHASE 1: CUSTOM FIELDS ✅

All 20 custom fields created at the contact level.

| # | Field Name | Field Key | Data Type | ID |
|---|------------|-----------|-----------|-----|
| 1 | Lead Source | contact.lead_source_painting | SINGLE_OPTIONS | ewUxIPoVcV3BZmgIvEsR |
| 2 | Job Type | contact.job_type_painting | SINGLE_OPTIONS | OqM3Q4FfbB3L1WMX0iNF |
| 3 | Service Category | contact.service_category_painting | SINGLE_OPTIONS | 3yD18RpsTUh3SkodwGod |
| 4 | Property Type | contact.property_type_painting | SINGLE_OPTIONS | kLbS8j0649ZbEi9vGIY3 |
| 5 | Colour Approved | contact.colour_approved_painting | RADIO (Yes/No) | YHn09VT1B13m78W48i8l |
| 6 | Colour Approval Date | contact.colour_approval_date_painting | DATE | o7BeQypYnJJo5tKmLEss |
| 7 | Paint Brand Preference | contact.paint_brand_preference_painting | TEXT | E4hKeb5EGwcFurntk2h8 |
| 8 | Prep Work Required | contact.prep_work_required_painting | SINGLE_OPTIONS | qD2l9dyqqqC4JfHRhVua |
| 9 | Estimated Square Footage | contact.est_square_footage_painting | NUMERICAL | khYdfyKvbQiAOtBENfUG |
| 10 | Estimate Amount | contact.estimate_amount_painting | MONETORY | QYeYujfhJv10HS3gsnbW |
| 11 | Contract Amount | contact.contract_amount_painting | MONETORY | Thhx8pSfFRkUeF8EeCz1 |
| 12 | Deposit Paid | contact.deposit_paid_painting | RADIO (Yes/No) | vusaloxYP1jmKMbicZDX |
| 13 | Crew Assigned | contact.crew_assigned_painting | TEXT | FO4IpmbxuU0NU6Xefnqb |
| 14 | Job Start Date | contact.job_start_date_painting | DATE | Zr0PppCvgbkkRH9Uj0Ey |
| 15 | Job End Date | contact.job_end_date_painting | DATE | DemHDwbvxHCMm54blplj |
| 16 | Weather Hold | contact.weather_hold_painting | RADIO (Yes/No) | qWtEQYzrUXAdex56XXL2 |
| 17 | Review Requested | contact.review_requested_painting | RADIO (Yes/No) | psWfBN5fw5gclw22HgA9 |
| 18 | Review Received | contact.review_received_painting | RADIO (Yes/No) | IFcHUU3Jny1R2GZe83e3 |
| 19 | Neighbour Campaign Sent | contact.neighbour_campaign_sent_painting | RADIO (Yes/No) | B89G51zAurzqNdU9ZcWJ |
| 20 | Upsell Offered | contact.upsell_offered_painting | SINGLE_OPTIONS | vrNWUlOq3IZ4nBPNDn3A |

### Field Options Reference

**Lead Source options:** Google LSA, Google Organic, Referral, Real Estate Agent, Property Manager, Kijiji/Craigslist, Facebook Ad, Repeat Customer, Strata/Condo Board, Door Knock

**Job Type options:** Interior Residential, Exterior Residential, Interior Commercial, Exterior Commercial, Strata/Condo, Cabinet Painting, Deck/Fence Staining, New Construction

**Service Category options:** Residential Interior, Residential Exterior, Commercial, Strata/Condo, New Construction

**Property Type options:** Residential, Commercial, Strata/Condo, Multi-Unit, New Construction

**Prep Work Required options:** Minimal, Moderate, Extensive, Unknown

**Upsell Offered options:** None, Exterior Upsell, Interior Upsell, Deck/Fence, Cabinet

---

## PHASE 2: PIPELINES ✅

All 4 pipelines created.

### Pipeline 1: Painting - Residential Interior
**ID:** 2f3kvY8oh2IQZG6HHUCi

| Stage | Position |
|-------|----------|
| New Lead | 0 |
| Estimate Scheduled | 1 |
| Estimate Complete | 2 |
| Colour Consultation | 3 |
| Proposal Sent | 4 |
| Follow-Up Active | 5 |
| Colour Approved | 6 |
| Contract Signed / Deposit | 7 |
| Job Scheduled | 8 |
| Job In Progress | 9 |
| Touch-Ups | 10 |
| Job Complete | 11 |
| Invoice Sent | 12 |
| Paid | 13 |
| Review Requested | 14 |
| Exterior Upsell | 15 |

### Pipeline 2: Painting - Residential Exterior
**ID:** iEF89vZiut4ioLF686ug

| Stage | Position |
|-------|----------|
| New Lead | 0 |
| Estimate Scheduled | 1 |
| Estimate Complete | 2 |
| Proposal Sent | 3 |
| Follow-Up Active | 4 |
| Contract Signed / Deposit | 5 |
| Weather Window Confirmed | 6 |
| Prep/Pressure Wash | 7 |
| Job In Progress | 8 |
| Job Complete | 9 |
| Invoice Sent | 10 |
| Paid | 11 |
| Review Requested | 12 |
| Neighbour Campaign | 13 |
| Interior Upsell | 14 |

### Pipeline 3: Painting - Commercial / Strata
**ID:** uow0sBv1EclXmFGYrHb2

| Stage | Position |
|-------|----------|
| New Prospect | 0 |
| Site Walk | 1 |
| Proposal Sent | 2 |
| Follow-Up Active | 3 |
| Contract Signed | 4 |
| Scheduling Confirmed | 5 |
| Job In Progress | 6 |
| Punch List | 7 |
| Job Complete | 8 |
| Invoice Sent | 9 |
| Paid | 10 |
| Review + Renewal | 11 |

### Pipeline 4: Painting - Lead Triage
**ID:** i3cu4RZno3ha4N3fcu4A

| Stage | Position |
|-------|----------|
| New Lead | 0 |
| Qualified | 1 |
| Not a Fit - Nurture | 2 |
| Lost | 3 |

---

## PHASE 3: CALENDARS ✅

All 3 calendars created.

| # | Calendar Name | Duration | Hours | ID |
|---|---------------|----------|-------|-----|
| 1 | Free Estimate - Painting | 45 min | Mon-Fri 8am-5pm | WzYZ3MJI1OE1sYwyBls1 |
| 2 | Colour Consultation | 30 min | Mon-Fri 9am-4pm | YD8UczfxiGOf2bARikdJ |
| 3 | Commercial Site Walk | 60 min | Mon-Fri 8am-4pm | KqeMu6Mmd7XNoZ4hdqsx |

**Calendar Settings:**
- Free Estimate: Auto-confirm ON, reschedule/cancel allowed
- Colour Consultation: Auto-confirm ON, reschedule/cancel allowed  
- Commercial Site Walk: Auto-confirm OFF (requires manual confirmation), 15-min buffer

---

## PHASE 4: TAGS ✅

All 30 tags created.

| Tag Name | ID |
|----------|----|
| new-lead | 3ircScDb6IN6zudSnXg7 |
| interior-job | k6Iq3feOzXFSjvjGL7p3 |
| exterior-job | yyaEBApTFsIUrZo0MvJq |
| commercial-job | 3UQTtkRwCsRgoz3WNur7 |
| strata-job | SM58mL69BPHNWC3EMDd3 |
| cabinet-painting | I7rPx5blwJzjp35drj7f |
| deck-staining | sy9FMQBLsjsJSvu3SYG8 |
| new-construction | dVWty9bdZRWB9pJotny8 |
| colour-pending | yJBAUfXv5TNUx6N3eBjJ |
| colour-approved | qVvNkJOV92KoHd9AE3zk |
| weather-hold | nfnzAAEyOZqT9LaRz40J |
| estimate-sent | 49sUFP4WMyahGWlASNd6 |
| deposit-paid | nLGBADizFsu3IOfxkH3S |
| contract-signed | tMQOs71c359IUQrtAC7M |
| job-in-progress | 1dibNClSgAcoVoIVhmzl |
| job-complete | ezO3HsQFgUW7V76pwuqs |
| review-requested | hVpUvKJpeXLhtLStVjki |
| review-received | ILO7o31WITA7O6QXpfoc |
| referral | LZiibqvIML9mFuCz4zFt |
| neighbour-campaign | I7vhKYjTqKJj1UfGK1f3 |
| exterior-upsell-candidate | aQTzP97u9TxhuAKuBs8C |
| interior-upsell-candidate | svHZwJHdYieGrzJIxqXI |
| real-estate-agent | GHqorD6x688WLLMABoDq |
| property-manager | XHDbpjDXkWz4y8y3TXzx |
| strata-board | xO0x0xPdUQs7VL01ycLq |
| repeat-customer | qKdzao3Jvgzpbpo5huSC |
| cold-lead | SuQCeQMgizzxA7J4OuPM |
| no-show | w9aJRlPigCMcIsaBydAw |
| google-lsa | zPDSCBsiU7gX4P3aPZdL |
| facebook-ad | BHTXFxtCZzkaeEangIJr |

---

## PHASE 5: WORKFLOWS — FULL SPECS 📋

> ⚠️ GHL API cannot create workflows programmatically. These are complete build specs to be entered manually in the GHL Workflow Builder or imported via snapshot. Each workflow is production-ready copy with exact timing.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — looking for a free painting estimate? Reply YES and we'll reach out right away 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 1: New Lead — Speed to Response

**Trigger:** Contact created (from web form, LSA, Facebook Lead Ad, Kijiji submission)
**Enroll condition:** Tag added: `new-lead`  
**Goal:** Contact within 5 minutes of lead arrival

**Steps:**

**Step 1 — Immediate SMS (0 min delay)**
```
Hi {{contact.first_name}}! This is {{location.name}} — we got your painting inquiry and will reach out within the hour. Talk soon! 🎨
```

**Step 2 — Internal Notification (0 min delay)**
- Type: Internal notification / email alert to owner
- Subject: `New Painting Lead: {{contact.full_name}} — {{contact.phone}}`
- Body: `New lead just came in. Name: {{contact.full_name}} | Phone: {{contact.phone}} | Email: {{contact.email}} | Source: {{contact.lead_source_painting}} | Call NOW — first response wins.`

**Step 3 — Wait (30 min)**

**Step 4 — Condition: Has contact replied?**
- If NO reply: Send SMS:
```
Hey {{contact.first_name}}, tried to reach you! Want to book a quick 15-min call to talk about your painting project? Here's our calendar: {{location.booking_url}}
```

**Step 5 — Wait (24 hours)**

**Step 6 — Condition: Has opportunity been created (contact moved forward)?**
- If NO: Send SMS:
```
Hi {{contact.first_name}}, circling back on your painting inquiry — still looking for a quote? We can even do a drive-by estimate so you don't have to be home. Just reply and we'll get it set up!
```

**Step 7 — Wait (3 days)**

**Step 8 — Condition: Still no movement?**
- If NO: Send SMS:
```
Hey {{contact.first_name}}, one last check-in from {{location.name}}. If you're still in the research phase, no worries — reply when you're ready and we'll get you sorted. 🙂
```

**Step 9 — Wait (7 days)**

**Step 10 — If still no response:**
- Add tag: `cold-lead`
- Remove tag: `new-lead`
- Remove from workflow

---

### Workflow 2: Estimate Appointment Confirmation

**Trigger:** Customer booked appointment (calendar: Free Estimate - Painting, ID: WzYZ3MJI1OE1sYwyBls1)  
**Goal:** Reduce no-shows, build confidence before the visit

**Step 1 — Immediate Email (booking confirmed)**
```
Subject: Your Free Painting Estimate is Confirmed ✅

Hi {{contact.first_name}},

Your painting estimate appointment is confirmed!

📅 Date: {{appointment.start_date}}
🕐 Time: {{appointment.start_time}}
📍 Location: {{contact.address}}

Our estimator will walk through your project, discuss options, and answer any questions. You'll receive your written quote within 24 hours of the visit.

To prepare:
• Note any specific areas of concern
• Have your colour ideas ready (Pinterest board, paint chips, etc.)
• We'll cover: surfaces, prep requirements, coat plan, and timeline

Questions? Reply to this email or call {{location.phone}}.

See you soon!
{{location.name}}
```

**Step 2 — SMS (immediate, booking confirmed)**
```
Hi {{contact.first_name}}, your painting estimate is confirmed for {{appointment.start_date}} at {{appointment.start_time}}. Our estimator will be there! Reply CANCEL if plans change. — {{location.name}}
```

**Step 3 — Wait until 24 hours before appointment**

**Step 4 — SMS (24hr reminder)**
```
Hey {{contact.first_name}}, reminder — your painting estimate is TOMORROW at {{appointment.start_time}}. Reply YES to confirm or CANCEL if you need to reschedule. See you then! 🎨
```

**Step 5 — Wait (4 hours)**

**Step 6 — Condition: Did contact reply YES?**
- If NO reply: Internal alert to owner: `{{contact.full_name}} hasn't confirmed tomorrow's estimate at {{appointment.start_time}}. Call to confirm: {{contact.phone}}`

**Step 7 — Wait until 2 hours before appointment**

**Step 8 — SMS (2hr reminder)**
```
Hi {{contact.first_name}}, see you in about 2 hours for your painting estimate! Our estimator will arrive around {{appointment.start_time}}. 📞 {{location.phone}} if anything comes up.
```

---

### Workflow 3: No-Show Recovery

**Trigger:** Appointment status (filter: no-show)  
**Goal:** Re-engage and rebook within 48 hours

**Step 1 — SMS (1 hour after no-show)**
```
Hey {{contact.first_name}}, looks like we missed each other at {{appointment.start_time}} today. No worries — want to rebook? Here's our calendar: {{location.booking_url}}
```

**Step 2 — Add tag:** `no-show`

**Step 3 — Wait (24 hours)**

**Step 4 — SMS**
```
Hi {{contact.first_name}}, {{location.name}} here — still interested in a painting quote? We have openings this week. Book here: {{location.booking_url}}
```

**Step 5 — Wait (5 days)**

**Step 6 — Condition: Has contact rebooked?**
- If NO: Add tag `cold-lead`, send final email:
```
Subject: Still thinking about your painting project?

Hi {{contact.first_name}},

We know life gets busy. Whenever you're ready to get your painting project moving, we're here.

Book your free estimate at a time that works for you: {{location.booking_url}}

Or reply to this email and we'll find a time that works.

— {{location.name}}
```

---

### Workflow 4: Post-Estimate Follow-Up (5-Step Over 21 Days)

**Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent)
**Goal:** Convert estimate to signed contract  
**Add tag:** `estimate-sent`

**Step 1 — SMS (Day 0, immediately)**
```
Hi {{contact.first_name}}, your painting estimate just hit your inbox! Let me know if you have any questions about scope, timing, or what's included. Happy to walk you through it. — {{location.name}}
```

**Step 2 — Wait (2 days)**

**Step 3 — SMS (Day 2)**
```
Hey {{contact.first_name}}, following up on your painting estimate — any questions about what we've included? We're happy to adjust scope or discuss payment options.
```

**Step 4 — Wait (2 days)**

**Step 5 — SMS (Day 4, urgency)**
```
Hi {{contact.first_name}}, just checking in on your quote. We're booking {{opportunity.estimated_start_month}} now and spots are filling up. Want to lock in a date?
```

**Step 6 — Wait (3 days)**

**Step 7 — Call attempt + voicemail (Day 7)**
- Internal task: "Call {{contact.full_name}} re: estimate follow-up. Phone: {{contact.phone}}"
- Voicemail drop (if available):
```
"Hi {{contact.first_name}}, this is [name] from {{location.name}}. Just following up on the painting estimate we sent over. Give me a call at {{location.phone}} or reply to this message if that's easier. Thanks!"
```

**Step 8 — Wait (7 days)**

**Step 9 — Email (Day 14)**
```
Subject: Still thinking it over? Here's what to know.

Hi {{contact.first_name}},

We know choosing a painter is a decision — you're trusting someone with your home.

Here's why our clients choose us:
✅ [Insert 3 key differentiators — e.g., 5-year labour warranty, insured crew, same-day quote turnaround]
✅ [Add a client testimonial or 5-star review snippet]
✅ Flexible payment: deposit + balance on completion

We'd love to earn your business. If you have any lingering questions, reply here.

Book your start date: {{location.booking_url}}

— {{location.name}}
```

**Step 10 — Wait (7 days)**

**Step 11 — Final SMS (Day 21)**
```
Hi {{contact.first_name}}, last follow-up from us — if you're still in research mode, no worries. Just reply READY when you want to move forward and we'll get you sorted. 🎨
```

**Step 12 — Add tag:** `cold-lead`  
**Step 13 — Remove from workflow**

---

### Workflow 5: Colour Approval Request

**Trigger:** Pipeline stage changed (filter: new stage = Colour Approved or Contract Signed / Deposit)  
**Goal:** Get colour selections confirmed before material ordering deadline  
**Add tag:** `colour-pending`

**Step 1 — SMS (Day 0)**
```
Hi {{contact.first_name}}! Great news — your painting project is confirmed 🎉 

Next step: colour selection. We need your choices confirmed by {{colour_deadline}} so we can order materials in time.

We're using {{contact.paint_brand_preference_painting}}. Their online visualizer can help: 
• Benjamin Moore: benjaminmoore.com/colour-visualizer
• Sherwin-Williams: sherwin-williams.com/visualizer

Just text back your colour codes/names when ready!
```

**Step 2 — Email (Day 0)**
```
Subject: Action Required — Colour Selection Needed by {{colour_deadline}}

Hi {{contact.first_name}},

Your painting project is confirmed — exciting! 🎨

We need your colour selections finalized by {{colour_deadline}} (5 business days before your start date) so we can order materials on time.

SURFACES NEEDING COLOUR SELECTION:
□ Siding/Walls: _____________
□ Trim: _____________
□ Fascia/Soffit: _____________
□ Front Door: _____________
□ Other: _____________

HOW TO SHARE YOUR CHOICES:
• Take a photo of your paint chip and text/email it
• Email us the paint name and code (e.g., BM White Dove OC-17)
• Visit your local Benjamin Moore or Sherwin-Williams and let them mix a sample

FAQ:
Q: Can you match my neighbour's colour?
A: Yes — just get the paint code from their can label.

Q: What if I change my mind after ordering?
A: Changes after ordering may incur a restocking fee. Let us know ASAP if anything changes.

Q: Can I supply my own paint?
A: We prefer to supply paint for quality control, but let's discuss.

Reply to this email or text {{location.phone}} when you're ready!

— {{location.name}}
```

**Step 3 — Wait (3 days)**

**Step 4 — SMS (Day 3)**
```
Hey {{contact.first_name}}, reminder — we need your colour selections by {{colour_deadline}} to keep your start date on track. 

Have you had a chance to visit {{contact.paint_brand_preference_painting}}?

Siding: ___
Trim: ___
Front Door: ___

Just text back the names or codes!
```

**Step 5 — Wait (2 days)**

**Step 6 — Call task (Day 5)**
- Internal task: "Call {{contact.full_name}} — colour selection deadline approaching. Offer colour consultation call if stuck."

**Step 7 — Wait (2 days — at deadline)**

**Step 8 — SMS (Day 7 — deadline)**
```
Hi {{contact.first_name}}, we need your colour choices TODAY to keep your {{job_start_date}} start date on schedule. If you need more time, we may need to push your start date by one week. Reply now or call {{location.phone}}! 
```

**Step 9 — Internal alert (Day 7, if no colours received)**
- Alert: `COLOUR APPROVAL OVERDUE — {{contact.full_name}} | Job Start: {{contact.job_start_date_painting}} | Call: {{contact.phone}}`

**Step 10 — If colour approved:**
- Update custom field: Colour Approved = Yes
- Update custom field: Colour Approval Date = today
- Add tag: `colour-approved`
- Remove tag: `colour-pending`
- End workflow

---

### Workflow 6: Weather Hold Notification

**Trigger:** Contact tag (filter: tag added = weather-hold)  
**Goal:** Proactively communicate delay, maintain trust

**Step 1 — SMS (immediate)**
```
Hi {{contact.first_name}}, heads up ☁️ — we're monitoring the weather forecast for your exterior job starting {{contact.job_start_date_painting}}. 

We may need to push your start by 1–2 days due to rain in the forecast. We'll confirm by {{weather_update_time}}.

Paint quality depends on dry conditions — we'd rather wait and do it right. Sorry for any inconvenience!
— {{location.name}}
```

**Step 2 — Email (immediate)**
```
Subject: Weather Update — Your Painting Job

Hi {{contact.first_name}},

We're keeping a close eye on the weather forecast for your upcoming exterior painting job.

Current forecast shows [rain/cold temperatures] during your scheduled start date. To ensure proper adhesion and a lasting finish, we need:
• No rain 24 hours before and after application
• Temperatures above 10°C during application and drying

We will contact you by {{weather_update_time}} with a confirmed new start date.

We appreciate your patience — doing it right means your paint job lasts 7–10 years instead of 3–4.

Questions? Call or text {{location.phone}}.

— {{location.name}}
```

**Step 3 — Internal task:** Update job schedule and crew assignment for rescheduled date

**Step 4 — Wait (per resolution)**  
When rescheduled:
- SMS: `Good news, {{contact.first_name}}! The weather is cooperating and your exterior painting is rescheduled to {{new_start_date}}. We're back on! 🎨`
- Update custom field: Job Start Date = new date
- Remove tag: `weather-hold`
- Add tag: `job-in-progress` when job starts

---

### Workflow 7: Job Start Notification (Day Before + Day Of)

**Trigger:** Custom date reminder (select Job Start Date field, set 1 day before)  
**Goal:** Set expectations, reduce surprises, professional first impression

**Step 1 — SMS (3 days before)**
```
Hi {{contact.first_name}}, your {{contact.job_type_painting}} painting starts {{contact.job_start_date_painting}}. 

Crew lead: {{contact.crew_assigned_painting}}
Arrival: 8:00 AM

Please ensure:
• Pets are secured
• Access to all work areas is clear
• Cars moved from driveway (exterior jobs)
• Windows and doors accessible

Questions? Call {{location.phone}}. See you soon! 🎨
```

**Step 2 — SMS (24 hours before)**
```
Reminder, {{contact.first_name}} — your painting crew arrives TOMORROW morning at 8:00 AM. 

Reply YES to confirm or call {{location.phone}} if anything has changed.
```

**Step 3 — Condition: No reply in 4 hours**
- Internal alert: `{{contact.full_name}} hasn't confirmed job start tomorrow. Call: {{contact.phone}}`

**Step 4 — SMS (morning of job)**
```
Good morning {{contact.first_name}}! The {{location.name}} crew is on their way. {{contact.crew_assigned_painting}} will arrive around 8:00 AM. Have a great day! 🎨
```

**Step 5 — Add tag:** `job-in-progress`

---

### Workflow 8: Post-Job Review Request — Interior

**Trigger:** Pipeline stage changed (filter: new stage = Job Complete, Residential Interior pipeline)  
**Goal:** 5-star Google review within 48 hours of job completion  
**Add tag:** `job-complete`

**Step 1 — SMS (2 hours after trigger)**
```
Hi {{contact.first_name}}! Hope you love the fresh new look 🏡✨ 

If we earned it, a Google review makes a huge difference for our small business — takes just 60 seconds:
[GOOGLE REVIEW LINK]

Thank you so much! 🙏
— {{location.name}}
```

**Step 2 — Add tag:** `review-requested`  
**Step 3 — Update custom field:** Review Requested = Yes

**Step 4 — Wait (48 hours)**

**Step 5 — Condition: Tag "review-received" present?**
- If NO: Send SMS:
```
Hey {{contact.first_name}}, just following up — did we earn a 5-star review? Here's the direct link if you missed it: [GOOGLE REVIEW LINK]. Every review helps our small business grow. Thank you! 🙏
```

**Step 6 — Wait (5 days)**

**Step 7 — Email (Day 7)**
```
Subject: Your Project Photos + One Last Ask

Hi {{contact.first_name}},

It's been a week since we completed your painting project — hope you're still loving it!

[If photos available: Attached are a few photos from your completed project.]

One last ask: if you have 60 seconds, your Google review means the world to us and helps other homeowners find our work:
[GOOGLE REVIEW LINK]

You can also find us on Facebook: [FACEBOOK LINK]

Thank you for choosing {{location.name}}. We'd love to work with you again!

— {{location.name}}
```

---

### Workflow 9: Post-Job Review Request — Exterior + Neighbour Campaign

**Trigger:** Pipeline stage changed (filter: new stage = Job Complete, Residential Exterior pipeline)  
**Goal:** 5-star Google review + activate neighbour outreach simultaneously  
**Add tags:** `job-complete`, `review-requested`

**Step 1 — SMS (2 hours after trigger)**
```
Hi {{contact.first_name}}! Your home looks incredible 🏡✨ 

If we did great work, would you take 60 seconds to leave us a Google review? It helps other homeowners in your neighbourhood find us:
[GOOGLE REVIEW LINK]

Thank you so much! — {{location.name}}
```

**Step 2 — Internal task:** "Yard sign placed at {{contact.address}}? Confirm and activate neighbour campaign."

**Step 3 — Update custom field:** Review Requested = Yes

**Step 4 — SMS to owner/crew (parallel)**
```
INTERNAL: Job complete at {{contact.address}}. Please confirm: 1) Yard sign placed, 2) 10 door hangers dropped on adjacent homes, 3) Before/after photos taken (with client permission).
```

**Step 5 — Add tag:** `neighbour-campaign`  
**Step 6 — Update custom field:** Neighbour Campaign Sent = Yes

**Step 7 — Wait (48 hours)**

**Step 8 — Condition: Review received?**
- If NO: Send SMS:
```
Hey {{contact.first_name}}, just a quick follow-up — here's that Google review link one more time: [GOOGLE REVIEW LINK]. We really appreciate it! 🙏
```

**Step 9 — Wait (12 days)**

**Step 10 — SMS (Day 14 — referral ask)**
```
Hi {{contact.first_name}}, hope the exterior is turning heads! 😄 If any neighbours ask who painted your home, we'd love the referral. We offer [a $100 referral credit] for any friend or neighbour who books with us. Just have them mention your name!
```

---

### Workflow 10: Unhappy Client Recovery (Internal Alert Only)

**Trigger:** Contact tag (filter: tag added = no-show) AND Stale opportunities (not moved forward within 7 days), OR Customer replied (with keyword filter: unhappy, not satisfied, terrible, refund, complaint)  
**Goal:** Flag immediately for owner intervention before it escalates publicly  
**⚠️ No client-facing messages in this workflow**

**Step 1 — Internal email (immediate)**
```
Subject: ⚠️ POTENTIAL UNHAPPY CLIENT — Action Required

Contact: {{contact.full_name}}
Phone: {{contact.phone}}
Email: {{contact.email}}
Job Type: {{contact.job_type_painting}}
Job Start: {{contact.job_start_date_painting}}

Trigger reason: [Negative keyword / No-show / No stage movement]

Recommended action:
1. Call client personally within 2 hours
2. Do NOT send any automated messages — pause their workflows
3. Offer to revisit/remediate before they post a review
4. Document resolution in opportunity notes

This alert was triggered automatically. Check conversation history for context.
```

**Step 2 — Create internal task:** "URGENT: Call {{contact.full_name}} re: potential complaint. Phone: {{contact.phone}}. Due: TODAY."

**Step 3 — Pause all other active workflows for this contact**

---

### Workflow 11: Exterior Upsell (After Interior Job Complete)

**Trigger:** Pipeline stage changed (filter: new stage = Exterior Upsell, Residential Interior pipeline) OR Contact tag (filter: tag added = exterior-upsell-candidate)  
**Goal:** Convert interior client to exterior job (spring/summer timing)

**Step 1 — Wait (7 days after job complete)**

**Step 2 — SMS**
```
Hi {{contact.first_name}}, hope you're loving your freshly painted rooms! 

Quick question — have you thought about the exterior this spring? We noticed the trim/siding on your home could use some attention. We'd be happy to include that in an early-bird spring quote. Interested?
```

**Step 3 — Add tag:** `exterior-upsell-candidate`
**Step 4 — Update custom field:** Upsell Offered = Exterior Upsell

**Step 5 — Wait (7 days)**

**Step 6 — If no reply:**
```
Subject: Spring Exterior Painting — Early-Bird Pricing for Past Clients

Hi {{contact.first_name}},

With spring around the corner, it's the perfect time to book your exterior repaint before our schedule fills up.

As a past client, you get priority booking and our best seasonal pricing.

Signs your exterior might be due:
✅ Peeling or fading paint
✅ Chalking or powdery residue
✅ Cracking caulk around windows
✅ Mildew or moisture staining

We're happy to do a drive-by estimate — no need to be home.

[BOOK YOUR EXTERIOR QUOTE]

— {{location.name}}
```

---

### Workflow 12: Interior Upsell (After Exterior Job Complete)

**Trigger:** Pipeline stage changed (filter: new stage = Interior Upsell, Residential Exterior pipeline) OR Contact tag (filter: tag added = interior-upsell-candidate)  
**Goal:** Convert exterior client to interior job (fall/winter timing)

**Step 1 — Wait (30 days after exterior job complete)**

**Step 2 — SMS**
```
Hi {{contact.first_name}}, with the exterior looking sharp, have you thought about refreshing the inside too? 

Many of our exterior clients add interior rooms in fall and winter when outdoor work slows down. Want a quick quote on any rooms?
```

**Step 3 — Add tag:** `interior-upsell-candidate`
**Step 4 — Update custom field:** Upsell Offered = Interior Upsell

**Step 5 — Wait (14 days)**

**Step 6 — Email (if no reply)**
```
Subject: Fall Interior Painting — Fill Your Home with Fresh Colour Before the Holidays

Hi {{contact.first_name}},

Your exterior looks great. Now imagine the inside matching that energy.

Fall and winter are the perfect time for interior painting:
🎨 No weather constraints
🎨 Fresh smell for holiday guests
🎨 Beat the spring rush pricing
🎨 Cozy new colours for the season

We're booking October–December interiors now. Reply to get a quote or book here: {{location.booking_url}}

— {{location.name}}
```

---

### Workflow 13: Seasonal Campaign — Spring Exterior

**Trigger:** Scheduler (fires annually on March 1)
**Target:** All contacts with tags: `interior-job`, `cold-lead` (past year), OR `exterior-upsell-candidate`  
**Goal:** Pre-book May–July exterior slots

**Step 1 — Email (March 1)**
```
Subject: Your exterior is going to love this spring (limited openings)

Hi {{contact.first_name}},

Spring is here — and so is exterior painting season.

After a long winter, wood siding, trim, and fascia take a beating. If you've noticed any of these, it's time:

✅ Peeling or bubbling paint
✅ Fading colour or chalking surface
✅ Cracking caulk around windows and doors
✅ Mildew or moisture staining
✅ Fascia or soffit looking rough

We're booking May and June now, and spots fill up faster than a fresh coat dries.

[BOOK YOUR FREE EXTERIOR QUOTE]

— {{location.name}}

P.S. We're happy to do a drive-by estimate — no need to be home.
```

**Step 2 — Wait (14 days)**

**Step 3 — SMS (March 15, if no booking)**
```
🌸 Spring is here! Time to get your exterior quote locked in before {{location.name}}'s May/June schedule fills. Book here: {{location.booking_url}}
```

---

### Workflow 14: Seasonal Campaign — Fall Interior

**Trigger:** Scheduler (fires annually on September 1)
**Target:** All contacts with tags: `exterior-job`, `cold-lead` (past year), OR `interior-upsell-candidate`  
**Goal:** Fill November–February interior calendar

**Step 1 — Email (September 1)**
```
Subject: Outdoor season is winding down. Time to refresh inside.

Hi {{contact.first_name}},

As the leaves turn and outdoor projects wrap up, it's the perfect time to turn attention inside.

Interior painting is our fall and winter specialty:

🎨 No UV or weather constraints
🎨 Your home smells fresh before the holidays
🎨 Guests see a refreshed space at family gatherings
🎨 Earlier booking = better pricing

We're taking interior bookings for October, November, and December now. Spaces go fast.

[GET YOUR INTERIOR QUOTE]

— {{location.name}}
```

**Step 2 — Wait (14 days)**

**Step 3 — SMS (September 15, if no booking)**
```
🍂 Fall's here! Perfect time to tackle those interior rooms before the holidays. {{location.name}} has openings in Oct/Nov/Dec. Book here: {{location.booking_url}}
```

---

### Workflow 15: Commercial / Strata Outreach Sequence

**Trigger:** Contact tag (filter: tag added = property-manager or strata-board or commercial-job)  
**Goal:** Build relationship, book intro meeting, convert to recurring contract

**Step 1 — Email (Day 0 — introduction)**
```
Subject: Commercial Painting Services — {{location.name}}

Hi {{contact.first_name}},

I'm reaching out because we specialize in commercial repaints, strata projects, and property management painting work across [region].

We understand what property managers and strata councils need:
✅ Reliable crews that show up as scheduled
✅ Insurance certificates and WCB coverage on file
✅ Clean, consistent invoicing
✅ Minimal disruption to tenants and residents
✅ Phased scheduling for large buildings

We've completed work for [insert reference types — e.g., "strata councils, rental property managers, commercial building owners"] in the area.

Can I book a 20-minute intro call to learn more about your properties and how we can support your maintenance schedule?

— [Owner Name], {{location.name}}
{{location.phone}}
```

**Step 2 — Wait (7 days)**

**Step 3 — Follow-up email (Day 7)**
```
Subject: Re: Commercial Painting — {{location.name}}

Hi {{contact.first_name}},

Just following up on my earlier note. We're currently booking commercial projects for [next quarter] and wanted to make sure you had our info.

We're happy to provide:
• Certificate of insurance on request
• References from similar properties
• Same-day quoting for urgent unit turnovers

Even if you have a painter on contract now, we're happy to be a backup resource.

Would a quick call or site visit make sense?

— {{location.name}}
```

**Step 4 — Wait (14 days)**

**Step 5 — SMS (Day 21)**
```
Hi {{contact.first_name}}, {{location.name}} here — following up on commercial painting for your properties. Happy to do a site walk and quote at no charge. Worth 20 minutes? Call or text {{location.phone}}.
```

**Step 6 — Wait (30 days)**

**Step 7 — Monthly nurture email (recurring)**
```
Subject: {{month}} Painting Openings — {{location.name}}

Hi {{contact.first_name}},

{{location.name}} here. We have openings in {{month}} for:

• Unit repaints (move-out / move-in turnovers)
• Common area touch-ups
• Exterior maintenance (weather permitting)
• Strata common areas and parkades

If you have anything coming up, just forward me the address and we'll get you a same-day quote.

— {{location.name}} | {{location.phone}}
```

**Step 8 — Continue monthly nurture indefinitely until opportunity created**

---

## SUMMARY: WHAT WAS BUILT

| Phase | Status | Count |
|-------|--------|-------|
| Custom Fields | ✅ Complete | 20 fields |
| Pipelines | ✅ Complete | 4 pipelines (44 total stages) |
| Calendars | ✅ Complete | 3 calendars |
| Tags | ✅ Complete | 30 tags |
| Workflow Specs | ✅ Documented | 15 workflows |

**Total API objects created:** 57 (20 fields + 4 pipelines + 3 calendars + 30 tags)

**Workflows:** Fully specified with exact SMS/email copy, timing, conditions, and internal logic. Ready for manual build in GHL Workflow Builder or import via snapshot.

---

## NEXT STEPS FOR OPERATOR

1. **Build workflows** in GHL Workflow Builder using the specs in Phase 5 above
2. **Set Google Review link** — replace all `[GOOGLE REVIEW LINK]` placeholders with the actual GHL reputation management review link for this location
3. **Set booking URL** — ensure `{{location.booking_url}}` resolves to the "Free Estimate - Painting" calendar link (ID: WzYZ3MJI1OE1sYwyBls1)
4. **Add location phone** in GHL location settings
5. **Configure forms** — create 3 intake forms (Residential Quote Request, Drive-By Estimate, Commercial/Strata Inquiry) using the custom fields built in Phase 1
6. **Set up smart lists** — build the 9 smart lists documented in the research file (Estimates Sent No Response, Colour Approval Overdue, Jobs In Progress, Review Not Left, Seasonal Re-Engagement Pool, Real Estate Agent Contacts, Property Manager Contacts, Strata Pending Vote, Neighbour Campaign Active)
7. **Connect LSA integration** — set up webhook or Zap to push Google LSA leads into GHL with tag `new-lead` and source `Google LSA`
8. **Test Workflow 1** — submit a test form and verify the 0-minute SMS fires within 60 seconds

---

*Build log generated by Maximus AI Subagent | 2026-07-21 | Location: uUOspt0oHkxmm53fklpX*
