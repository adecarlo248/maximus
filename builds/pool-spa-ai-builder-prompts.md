# Pool & Spa — GHL AI Workflow Builder Prompts

Use this file inside VS Code. Copy/paste one prompt at a time into GoHighLevel’s AI Workflow Builder.

**Important:** Workflow 1 is NOT an automation workflow. Use native GHL Missed Call Text Back instead.

---

## WORKFLOW 1 — Missed Call Text Back Native Setting

Do not paste this into AI Workflow Builder.

Set this up manually in GHL:

**Settings → Phone Numbers → Select Number → Voicemail & Missed Call TextBack → Enable Missed Call TextBack**

Message:

```text
Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — pool opening, closing, or service needed? Reply YES and we'll get you scheduled right away 👋
```

---

## WORKFLOW 2 — Spring Opening Campaign

```text
Create a GoHighLevel workflow called “Pool & Spa - Spring Opening Campaign”.

Goal:
Run an annual February/March spring pool opening campaign for past customers, repeat customers, old pool leads, and anyone tagged pool-opening, repeat-customer, or new-lead. The workflow should drive customers to book a Pool Opening Appointment before the spring rush.

Trigger:
Scheduler trigger every year on February 1 at 9:00 AM local time.

Entry filters:
Contacts with ANY of these tags:
- pool-opening
- repeat-customer
- new-lead

Workflow steps:

1. Send Email immediately.
Subject: Spring pool opening — book before we fill up
Email body:
Hi {{contact.firstName}},

Every spring, the same thing happens: everyone wants their pool opened at the same time.

We are giving past customers and existing contacts first access before the schedule fills up.

Our spring opening service can include:
- Equipment reinstall and startup
- Water chemistry test
- Chemical startup treatment
- Pump, filter, heater, and salt system inspection
- Pool condition check

Book your spring opening here:
[POOL OPENING CALENDAR LINK]

Spots fill fast, so book early and we will take care of the rest.

{{location.name}}

2. Send SMS 6 days later.
SMS:
Hey {{contact.firstName}}! 🌊 Spring opening spots are starting to fill. Book your pool opening here: [POOL OPENING CALENDAR LINK] — {{location.name}}

3. Add tag: spring-campaign

4. Wait 8 days.

5. Add If/Else condition:
If customer has booked an appointment on the Pool Opening Appointment calendar, end workflow.
If not booked, continue.

6. Send Email.
Subject: Only a few May opening spots left
Email body:
Hi {{contact.firstName}},

Quick reminder — May opening spots always go fast.

If you want your pool opened without chasing availability last minute, grab a time now:
[POOL OPENING CALENDAR LINK]

{{location.name}}

7. Wait 14 days.

8. Add If/Else condition:
If booked, end workflow.
If not booked, continue.

9. Send SMS.
SMS:
Last call to get ahead of the spring rush, {{contact.firstName}}. Want your pool opening booked? Grab a time here: [POOL OPENING CALENDAR LINK]

10. Wait 30 days.

11. Add If/Else condition:
If booked, end workflow.
If not booked, continue.

12. Send SMS.
SMS:
Spring is here {{contact.firstName}}! If you still need your pool opened, you can book here: [POOL OPENING CALENDAR LINK] 🌊

13. Wait 30 days.

14. Add If/Else condition:
If booked, end workflow.
If not booked, add tag cold-lead and remove tag spring-campaign.

Stop conditions:
End workflow if contact books Pool Opening Appointment or replies asking to stop.
```

---

## WORKFLOW 3 — Opening Appointment Confirmation

```text
Create a GoHighLevel workflow called “Pool & Spa - Opening Appointment Confirmation”.

Goal:
Confirm pool opening appointments, prepare the customer before arrival, reduce no-shows, and make the service feel professional.

Trigger:
Customer books an appointment on calendar: Pool Opening Appointment.

Workflow steps:

1. Send SMS immediately.
SMS:
Hi {{contact.firstName}}! Your pool opening is confirmed for {{appointment.startTime}}. We’ll have your pool up and running soon 🌊 Reply here with any questions. — {{location.name}}

2. Send Email immediately.
Subject: Pool opening confirmed — here’s what to do before we arrive
Email body:
Hi {{contact.firstName}},

Your pool opening appointment is confirmed for:
{{appointment.startTime}}

Before we arrive, please:
1. Clear the deck area around the pool and equipment pad
2. Make sure the gate or pool area is accessible
3. Make sure the water source/garden hose is accessible
4. Locate safety cover tools if you have them
5. Let us know about any equipment issues you noticed last season

Questions? Reply to this email or text us anytime.

We’ll see you soon,
{{location.name}}

3. Add tag: pool-opening

4. Wait until 24 hours before appointment.
Send SMS:
Reminder: your pool opening is tomorrow at {{appointment.startTime}}. Any last questions? Reply here. — {{location.name}}

5. Wait until 2 hours before appointment.
Send SMS:
We’re on our way soon, {{contact.firstName}}! Your pool opening is today at {{appointment.startTime}} 🌊 — {{location.name}}

Stop conditions:
End after final reminder. If appointment is cancelled, stop workflow.
```

---

## WORKFLOW 4 — Post-Opening Review + Maintenance Plan Upsell

```text
Create a GoHighLevel workflow called “Pool & Spa - Post Opening Review and Maintenance Upsell”.

Goal:
After a pool opening is completed and paid, request a review, route unhappy customers to the owner, and offer weekly maintenance.

Trigger:
Opportunity pipeline stage changed.
Pipeline: Pool - Spring Opening
Stage: Paid

Workflow steps:

1. Wait 24 hours.

2. Send SMS.
SMS:
Hi {{contact.firstName}}! Hope you’re enjoying your pool. On a scale of 1–5, how did our opening service go? Reply with a number 🌊

3. Wait for customer reply.

4. Add If/Else condition based on reply.
If reply is 4 or 5:
- Send SMS:
So glad to hear it! 🙌 A quick Google review means the world to us and helps local families find us: [GOOGLE REVIEW LINK]
- Add tag: review-requested
- Set custom field Review Requested = Yes

If reply is 1, 2, or 3:
- Send SMS:
We’re sorry to hear that. Can you tell us what happened? Our owner wants to make it right.
- Send internal notification to owner:
Service recovery needed: {{contact.name}} rated their pool opening {{contact.message}}/5. Respond within 24 hours.
- Create task:
Call {{contact.name}} — low rating service recovery

If no reply after 2 days:
Continue to maintenance upsell.

5. Wait 5 days.

6. Send SMS maintenance offer.
SMS:
Hey {{contact.firstName}}! Now that your pool is open, have you thought about weekly maintenance? We handle the chemistry and cleaning so you just swim. Want a quick quote? Reply YES. — {{location.name}}

7. Wait for reply.

8. If contact replies YES:
- Move or create opportunity in Pool - Weekly Maintenance pipeline, stage Prospect
- Add tag: weekly-maintenance
- Create task: Call {{contact.name}} — maintenance program interest
- Send internal notification to owner/team.

9. If no reply after 7 days:
- Add tag: cold-lead
- End workflow.
```

---

## WORKFLOW 5 — Equipment Age Trigger 10 Year

```text
Create a GoHighLevel workflow called “Pool & Spa - 10 Year Equipment Replacement Candidate”.

Goal:
Proactively educate customers whose pool equipment is 10–15 years old and encourage them to book an equipment assessment before emergency failure.

Trigger options:
1. Contact custom field Equipment Age is updated to 10-15 years
OR
2. Tag added: aging-equipment-10yr

Workflow steps:

1. Add tags:
- aging-equipment-10yr
- equipment-replacement-candidate

2. Set custom field:
Equipment Replacement Candidate = Yes

3. Send Email immediately.
Subject: Your pool equipment is 10+ years old — what you need to know
Email body:
Hi {{contact.firstName}},

Pool equipment has a lifespan. Once equipment hits the 10-year range, parts can start failing at the worst possible time — usually right in the middle of swim season.

Common timelines:
- Pump: 8–12 years
- Filter media: 5–7 years
- Heater: 8–15 years
- Salt cell: 3–5 years
- Automation system: 10–15 years

The smart move is a proactive equipment assessment before something fails.

Book an equipment service call here:
[EQUIPMENT SERVICE CALL CALENDAR LINK]

{{location.name}}

4. Wait 14 days.

5. Send SMS.
SMS:
Hi {{contact.firstName}}! Quick follow-up — your pool equipment is in the 10-year range. Want us to check it out at your next service? We’ll give you an honest assessment. — {{location.name}}

6. Wait 30 days.

7. Send Email.
Subject: Variable-speed pump upgrade — why many pool owners switch
Email body:
Hi {{contact.firstName}},

If your pump is older or still single-speed, a variable-speed pump may reduce energy use and make the pool run quieter and more efficiently.

If you want us to check whether your setup is worth upgrading, book an equipment assessment here:
[EQUIPMENT SERVICE CALL CALENDAR LINK]

{{location.name}}

8. End workflow.
```

---

## WORKFLOW 6 — Equipment Age Trigger 15 Year Urgent Campaign

```text
Create a GoHighLevel workflow called “Pool & Spa - 15 Year Equipment Urgent Replacement Campaign”.

Goal:
Create urgency for customers with 15+ year-old pool equipment, educate them on failure signs, and drive priority equipment assessments.

Trigger options:
1. Contact custom field Equipment Age is updated to 15+ years
OR
2. Tag added: aging-equipment-15yr

Workflow steps:

1. Add tags:
- aging-equipment-15yr
- equipment-replacement-candidate

2. Set custom field:
Equipment Replacement Candidate = Yes

3. Send SMS immediately.
SMS:
Hi {{contact.firstName}}, quick heads up — equipment at 15+ years is past its expected lifespan. A proactive replacement is usually cheaper than an emergency one. Want to schedule a quick assessment? — {{location.name}}

4. Send Email immediately.
Subject: 15-year equipment alert — what to watch for this season
Email body:
Hi {{contact.firstName}},

When pool equipment reaches 15+ years, failures become more likely — especially during peak season.

Watch for:
- Loud pump bearing noise
- Breaker trips
- Low pressure
- Visible rust or corrosion
- Heater pilot or ignition problems
- Poor circulation
- Salt readings that seem off

We recommend a quick assessment before the season gets busy.

Book here:
[EQUIPMENT SERVICE CALL CALENDAR LINK]

{{location.name}}

5. Wait 7 days.

6. Send SMS.
SMS:
{{contact.firstName}}, have you noticed any changes in pump, heater, or filter performance? Equipment at 15+ years can fail without warning. Reply YES if you want us to assess it. — {{location.name}}

7. Wait 14 days.

8. Send Email.
Subject: Final reminder — avoid an emergency pool equipment failure
Email body:
Hi {{contact.firstName}},

This is a final reminder to get ahead of aging pool equipment before it becomes an emergency repair.

If you want us to take a look, book here:
[EQUIPMENT SERVICE CALL CALENDAR LINK]

{{location.name}}

9. End workflow.
```

---

## WORKFLOW 7 — Fall Closing Campaign

```text
Create a GoHighLevel workflow called “Pool & Spa - Fall Closing Campaign”.

Goal:
Run an annual August/September fall pool closing campaign to book closing appointments early before the fall rush.

Trigger:
Scheduler trigger every year on August 15 at 9:00 AM local time.

Entry filters:
Contacts with ANY of these tags:
- pool-opening
- pool-closing
- repeat-customer

Workflow steps:

1. Send Email immediately.
Subject: Fall pool closing — book early, avoid the wait
Email body:
Hi {{contact.firstName}},

The same rush that happens in spring for pool openings happens again in fall for closings.

Book your closing early so you can:
- Pick a preferred date
- Avoid the October scramble
- Protect your pool properly for winter
- Lock in your spring opening date while we’re there

Book your pool closing here:
[POOL CLOSING CALENDAR LINK]

{{location.name}}

2. Add tag: fall-campaign

3. Wait 14 days.

4. Add If/Else condition:
If booked on Pool Closing Appointment calendar, end workflow.
If not booked, continue.

5. Send SMS.
SMS:
Hey {{contact.firstName}}! 🍂 Time to think about closing. October fills fast — grab your pool closing spot here: [POOL CLOSING CALENDAR LINK] — {{location.name}}

6. Wait 14 days.

7. If booked, end workflow. If not booked, send Email.
Subject: What proper winterization should include
Email body:
Hi {{contact.firstName}},

A proper pool closing helps prevent freeze damage, plumbing issues, and spring headaches.

Our closing process can include:
- Lowering water to the correct level
- Blowing out lines
- Adding antifreeze where needed
- Winterizing equipment
- Installing plugs and cover
- Balancing winter chemicals

Book your closing here:
[POOL CLOSING CALENDAR LINK]

{{location.name}}

8. Wait 14 days.

9. If booked, end workflow. If not booked, send SMS.
SMS:
October is here — we’re filling up for closings. Don’t get left scrambling in November: [POOL CLOSING CALENDAR LINK]

10. Wait 14 days.

11. If booked, end workflow. If not booked, send final SMS.
SMS:
Last call for pool closing spots, {{contact.firstName}}. If you still need your pool winterized, book here: [POOL CLOSING CALENDAR LINK]

12. End workflow.
```

---

## WORKFLOW 8 — Closing Appointment Confirmation + Spring Pre-Book

```text
Create a GoHighLevel workflow called “Pool & Spa - Closing Confirmation and Spring Pre-Book”.

Goal:
Confirm pool closing appointments, prepare customers before arrival, and use the completed closing to pre-book next spring’s opening.

Trigger:
Customer books an appointment on calendar: Pool Closing Appointment.

Workflow steps:

1. Send SMS immediately.
SMS:
Hi {{contact.firstName}}! Your pool closing is confirmed for {{appointment.startTime}}. We’ll make sure your pool is protected for winter 🍂 — {{location.name}}

2. Send Email immediately.
Subject: Pool closing confirmed — prep guide inside
Email body:
Hi {{contact.firstName}},

Your pool closing appointment is confirmed for:
{{appointment.startTime}}

Before we arrive:
1. Keep your pump running until we arrive if possible
2. Have the pool cover ready and accessible
3. Note any issues you want us to inspect
4. Make sure gates and equipment areas are accessible
5. Locate cover straps, anchors, and accessories if needed

We can also help lock in your spring opening date while we’re there so you get priority next season.

{{location.name}}

3. Add tag: pool-closing

4. Wait until 24 hours before appointment.
Send SMS:
Reminder: your pool closing is tomorrow at {{appointment.startTime}}. Please make sure the pool area and equipment are accessible. — {{location.name}}

5. Wait until 2 hours before appointment.
Send SMS:
We’ll see you soon, {{contact.firstName}}. Your pool closing is scheduled for today at {{appointment.startTime}} 🍂 — {{location.name}}

6. Wait until opportunity is moved to Pool - Fall Closing pipeline stage: Closing Complete.

7. Send SMS spring pre-book offer.
SMS:
Great news — your pool is closed for winter! Want to lock in your spring opening date now before the May rush? Reply YES and we’ll save you a spot. — {{location.name}}

8. Wait for reply.

9. If reply is YES:
- Create task: Book spring opening for {{contact.name}} — requested after closing
- Move opportunity to Pool - Fall Closing pipeline stage: Spring Opening Pre-Book
- Send internal notification to owner/team.

10. If no reply after 7 days:
- Wait 30 days
- Send Email off-season nurture.
Subject: Your pool is closed — here’s how to make spring easier
Email body:
Hi {{contact.firstName}},

Your pool is closed for the season. The easiest way to avoid spring scheduling stress is to pre-book your opening early.

Reply to this email or book here:
[POOL OPENING CALENDAR LINK]

{{location.name}}

11. End workflow.
```

---

## WORKFLOW 9 — Weekly Maintenance Plan Renewal

```text
Create a GoHighLevel workflow called “Pool & Spa - Weekly Maintenance Plan Renewal”.

Goal:
Renew weekly or bi-weekly pool maintenance customers before their plan expires and reduce churn.

Trigger:
Custom date reminder based on custom field Plan Renewal Date.
Start workflow 60 days before Plan Renewal Date.

Workflow steps:

1. Send Email 60 days before renewal.
Subject: Your maintenance plan renews soon — want to keep your spot?
Email body:
Hi {{contact.firstName}},

Your pool maintenance plan is coming up for renewal.

We’d love to keep you on the route for another season.

Plan options:
- Basic: bi-weekly service
- Standard: weekly service
- Premium: weekly service + priority support

Reply to this email or click here to renew:
[RENEWAL LINK OR CALENDAR LINK]

{{location.name}}

2. Add tag: plan-renewal-due

3. Wait 30 days.

4. Add If/Else condition:
If Maintenance Plan Active = Yes and Plan Renewal Date has been updated, remove tag plan-renewal-due, add tag maintenance-plan-active, and end workflow.
If not renewed, continue.

5. Send SMS 30 days before renewal.
SMS:
Hi {{contact.firstName}}! Your maintenance plan renews soon. Want to lock in your route for next season? Reply YES and we’ll confirm your spot. — {{location.name}}

6. Wait 16 days.

7. Add If/Else condition:
If renewed, remove tag plan-renewal-due, add tag maintenance-plan-active, and end workflow.
If not renewed, continue.

8. Send SMS 14 days before renewal.
SMS:
{{contact.firstName}}, quick heads up — your maintenance plan expires in about 2 weeks. Routes fill fast in spring. Want to stay on? Reply YES. — {{location.name}}

9. Wait 14 days.

10. Add If/Else condition:
If renewed, remove tag plan-renewal-due, add tag maintenance-plan-active, and end workflow.
If not renewed:
- Create task: Call {{contact.name}} — maintenance renewal not confirmed
- Move opportunity to Pool - Weekly Maintenance pipeline stage At Risk
- Send internal notification to owner/team.

11. End workflow.
```

---

## WORKFLOW 10 — Hot Tub / Spa Lead Nurture

```text
Create a GoHighLevel workflow called “Pool & Spa - Hot Tub and Spa Lead Nurture”.

Goal:
Nurture new hot tub/spa leads, drive showroom visits or consultations, and position hot tub ownership as a lifestyle and year-round service opportunity.

Trigger options:
1. Opportunity created in pipeline: Pool - Hot Tub / Spa, stage: New Inquiry
OR
2. Tag added: hot-tub

Workflow steps:

1. Send SMS immediately.
SMS:
Hi {{contact.firstName}}! Thanks for reaching out about hot tubs/spas. Want to book a showroom visit, service call, or have us call you first? Reply anytime. — {{location.name}}

2. Send Email immediately.
Subject: Hot tub ownership — what it actually looks like day to day
Email body:
Hi {{contact.firstName}},

Owning a hot tub is not just about jets and lights. For most customers, it becomes a daily ritual — 20 minutes to relax, recover, and enjoy the backyard year-round.

Hot tub ownership in real life:
- Average soak: 20–30 minutes
- Typical use: 3–5 times per week
- Maintenance: water chemistry, filter cleaning, and periodic drain/refill
- Year-round enjoyment, especially in colder weather

We can walk you through models, service, chemicals, installation, and ownership costs.

Book a showroom visit or consultation here:
[NEW POOL / HOT TUB CONSULTATION CALENDAR LINK]

{{location.name}}

3. Wait 3 days.

4. Add If/Else condition:
If booked appointment on New Pool/Hot Tub Consultation calendar, move opportunity to Demo/Showroom stage and end workflow.
If not booked, continue.

5. Send SMS.
SMS:
{{contact.firstName}}, still thinking about a hot tub or spa? We can walk you through options without pressure. Want to come by this week? [CONSULTATION CALENDAR LINK]

6. Wait 4 days.

7. If booked, move opportunity to Demo/Showroom stage and end workflow.
If not booked, send Email.
Subject: Is a hot tub really worth it?
Email body:
Hi {{contact.firstName}},

The biggest question we hear is: “Will we actually use it?”

Most hot tub owners tell us they use it far more than expected — for stress relief, family time, sore muscles, and quiet time outside.

If you’re still curious, book a quick consultation here:
[CONSULTATION CALENDAR LINK]

No pressure — just answers.

{{location.name}}

8. Wait 7 days.

9. Add If/Else condition:
If booked, move opportunity to Demo/Showroom stage and end workflow.
If not booked:
- Add tag cold-lead
- Wait 30 days
- Send final SMS.

Final SMS:
Still interested in a hot tub or spa, {{contact.firstName}}? Best time to plan is before the season rush. Reply YES if you want help choosing options. — {{location.name}}

10. End workflow.
```

---

## Optional Extra Workflow — Equipment Service Call Confirmation

Use this if you want a separate confirmation workflow for equipment repair appointments.

```text
Create a GoHighLevel workflow called “Pool & Spa - Equipment Service Call Confirmation”.

Goal:
Confirm equipment service calls, collect useful equipment details before arrival, and prepare the customer.

Trigger:
Customer books appointment on calendar: Equipment Service Call.

Workflow steps:

1. Send SMS immediately.
SMS:
Hi {{contact.firstName}}! Your equipment service call is confirmed for {{appointment.startTime}}. If you know the pump/heater/filter brand or model, reply with it here. — {{location.name}}

2. Send Email immediately.
Subject: Equipment service call confirmed
Email body:
Hi {{contact.firstName}},

Your equipment service call is confirmed for:
{{appointment.startTime}}

Before we arrive, please send anything you know about:
- Pump brand/model
- Filter type
- Heater type
- Salt system or automation panel
- Symptoms you noticed
- Photos of the equipment pad if possible

This helps us arrive better prepared.

{{location.name}}

3. Add tag: equipment-repair

4. Wait until 24 hours before appointment.
Send SMS:
Reminder: your pool equipment service call is tomorrow at {{appointment.startTime}}. Please make sure the equipment pad is accessible. — {{location.name}}

5. Wait until 2 hours before appointment.
Send SMS:
We’ll see you soon, {{contact.firstName}}. Your equipment service call is today at {{appointment.startTime}}. — {{location.name}}

6. End workflow.
```
