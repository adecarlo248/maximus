# Cleaning Service — GHL AI Workflow Builder Prompts

Use this file inside VS Code. Copy/paste one prompt at a time into GoHighLevel’s AI Workflow Builder.

Built for residential cleaning, commercial cleaning, deep cleans, move-in/move-out cleans, Airbnb/short-term rental turnovers, post-construction cleaning, and recurring cleaning customers.

**Important:** Workflow 1 is NOT an automation workflow. Use native GHL Missed Call Text Back instead.

---

## WORKFLOW 1 — Missed Call Text Back Native Setting

Do not paste this into AI Workflow Builder.

Set this up manually in GHL:

**Settings → Phone Numbers → Select Number → Voicemail & Missed Call TextBack → Enable Missed Call TextBack**

Message:

```text
Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — looking for a cleaning quote or trying to book a clean? Reply CLEAN and we’ll help you get scheduled 👋
```

---

## WORKFLOW 2 — New Cleaning Lead Speed to Response

```text
Create a GoHighLevel workflow called “Cleaning Service - New Lead Speed to Response”.

Goal:
Respond instantly to new cleaning leads, qualify the type of cleaning needed, and move the contact toward a quote or booking.

Trigger:
Contact Created OR Form Submitted OR Facebook Lead Form Submitted OR Web Chat Submitted.

Entry filters:
Only run if the contact does NOT already have tag customer-active and does NOT have an open opportunity.

Workflow steps:

1. Add tag: new-lead

2. Create or update opportunity in pipeline: Cleaning - New Leads
Stage: New Inquiry

3. Send SMS immediately.
SMS:
Hi {{contact.firstName}}, thanks for reaching out to {{location.name}}! What type of cleaning are you looking for — regular home cleaning, deep clean, move-in/move-out, Airbnb turnover, commercial, or post-construction?

4. Send Email immediately.
Subject: We got your cleaning request
Email body:
Hi {{contact.firstName}},

Thanks for reaching out to {{location.name}}.

To point you in the right direction, we’ll need a few quick details:
- What type of cleaning do you need?
- What town/area are you in?
- Is this one-time or recurring?
- When do you need it done?
- How many bedrooms/bathrooms or approximate square footage?

You can reply here or book/request a quote using this link:
[CLEANING QUOTE OR BOOKING LINK]

{{location.name}}

5. Wait 10 minutes.

6. If customer has replied, stop automated follow-up and notify owner/team.

7. If no reply, send SMS.
SMS:
Quick check, {{contact.firstName}} — if you send your cleaning type, town, and ideal date, we can help you get a quote or booking started.

8. Wait 24 hours.

9. If no reply, send SMS.
SMS:
Still need help with cleaning? Reply anytime and we’ll help you get scheduled. — {{location.name}}

10. Wait 48 hours.

11. If no reply, add tag cold-lead and move opportunity to stage: Cold Lead.
```

---

## WORKFLOW 3 — Cleaning Quote Form Follow-Up

```text
Create a GoHighLevel workflow called “Cleaning Service - Quote Form Follow-Up”.

Goal:
After someone submits a quote form, confirm receipt, collect any missing details, and move them toward booking or a manual quote.

Trigger:
Form Submitted.
Form name contains Cleaning Quote OR Request a Quote OR Book a Cleaning.

Workflow steps:

1. Add tag: quote-requested

2. Create or update opportunity in pipeline: Cleaning - New Leads
Stage: Quote Requested

3. Send SMS immediately.
SMS:
Hi {{contact.firstName}}, we got your cleaning request. If you have photos, access notes, or anything specific you want cleaned, you can send it here. — {{location.name}}

4. Send Email immediately.
Subject: Your cleaning request has been received
Email body:
Hi {{contact.firstName}},

Thanks for requesting a cleaning quote from {{location.name}}.

We’ll review the details and help you with the best next step.

If you haven’t already, please send:
- Cleaning type
- Property size
- Preferred date/time
- Address or town
- Any pets or special instructions
- Photos if helpful

{{location.name}}

5. Send internal notification to owner/team.
Notification:
New cleaning quote request from {{contact.name}}. Review details and follow up.

6. Wait 2 hours.

7. If appointment has not been booked and no manual quote sent, create task:
Review and respond to cleaning quote request for {{contact.name}}
Due: same day.

8. Wait 24 hours.

9. If no appointment booked, send SMS.
SMS:
Hi {{contact.firstName}}, just checking — do you want to book a cleaning time or have us send a quote first?

10. If customer replies, stop automation and notify owner/team.

11. If no reply after 72 hours, move opportunity to stage: Follow-Up Active.
```

---

## WORKFLOW 4 — Cleaning Appointment Confirmation + Prep Instructions

```text
Create a GoHighLevel workflow called “Cleaning Service - Appointment Confirmation and Prep”.

Goal:
Confirm cleaning appointments, reduce no-shows, and make sure the cleaner has access and proper prep details.

Trigger:
Customer books an appointment on any cleaning calendar:
- Residential Cleaning
- Deep Cleaning
- Move In / Move Out Cleaning
- Commercial Cleaning
- Airbnb Turnover
- Post-Construction Cleaning

Workflow steps:

1. Add tag: cleaning-booked

2. Move opportunity to pipeline: Cleaning - Bookings
Stage: Booked

3. Send SMS immediately.
SMS:
Hi {{contact.firstName}}! Your cleaning with {{location.name}} is confirmed for {{appointment.startTime}}. Please reply with any access notes, pets, parking info, or special requests.

4. Send Email immediately.
Subject: Cleaning appointment confirmed — quick prep notes
Email body:
Hi {{contact.firstName}},

Your cleaning appointment is confirmed for:
{{appointment.startTime}}

Before we arrive, please:
1. Share access instructions if you won’t be home
2. Let us know about pets
3. Clear clutter from surfaces/floors where possible
4. Tell us about priority areas
5. Let us know about parking or building entry instructions

Questions? Reply anytime.

{{location.name}}

5. Wait until 24 hours before appointment.
Send SMS:
Reminder: your cleaning is tomorrow at {{appointment.startTime}}. Please reply with any access notes, pets, parking info, or special requests. — {{location.name}}

6. Wait until 2 hours before appointment.
Send SMS:
We’ll see you soon, {{contact.firstName}}! Your cleaning is today at {{appointment.startTime}}. — {{location.name}}

7. Stop workflow after appointment reminder.
```

---

## WORKFLOW 5 — Move-In / Move-Out Cleaning Urgency Follow-Up

```text
Create a GoHighLevel workflow called “Cleaning Service - Move In Move Out Urgency Follow-Up”.

Goal:
Prioritize move-in and move-out cleaning leads because they usually have deadlines and higher urgency.

Trigger:
Tag added: service-move-in-out
OR custom field Cleaning Type equals Move In / Move Out Cleaning.

Workflow steps:

1. Create or update opportunity in pipeline: Cleaning - New Leads
Stage: Move In / Move Out Lead

2. Send SMS immediately.
SMS:
Hi {{contact.firstName}}, move-in/move-out cleans usually have tight timelines. What date do you need the cleaning completed by?

3. Send Email immediately.
Subject: Move-in / move-out cleaning request
Email body:
Hi {{contact.firstName}},

Thanks for reaching out about move-in/move-out cleaning.

To help quickly, please send:
- Deadline date
- Property address or town
- Number of bedrooms/bathrooms
- Whether the home is empty or furnished
- Any appliances, cupboards, baseboards, or inside windows needed
- Access instructions

You can also book/request a quote here:
[MOVE-IN/MOVE-OUT BOOKING LINK]

{{location.name}}

4. Send internal notification to owner/team:
Urgent move-in/move-out cleaning lead: {{contact.name}}. Follow up today.

5. Wait 15 minutes.

6. If no reply, send SMS.
SMS:
Quick check — when is your deadline for the move-in/move-out clean? We’ll do our best to help if we have availability.

7. Wait 24 hours.

8. If no reply, send final SMS.
SMS:
Still need the move-in/move-out clean booked? Reply with your deadline and property size and we’ll help you with the next step.

9. If no reply after 48 hours, add tag cold-lead.
```

---

## WORKFLOW 6 — Recurring Cleaning Offer After First Clean

```text
Create a GoHighLevel workflow called “Cleaning Service - Recurring Cleaning Upsell”.

Goal:
After a completed one-time clean, offer recurring weekly, bi-weekly, or monthly cleaning service.

Trigger:
Opportunity pipeline stage changed.
Pipeline: Cleaning - Bookings
Stage: Completed

Entry filter:
Contact does NOT have tag recurring-client.

Workflow steps:

1. Wait 24 hours.

2. Send SMS.
SMS:
Hi {{contact.firstName}}, hope you’re enjoying the fresh clean! Would you like pricing for recurring weekly, bi-weekly, or monthly cleaning so it stays that way?

3. Wait for reply.

4. If customer replies YES:
- Add tag: recurring-interest
- Move or create opportunity in pipeline: Cleaning - Recurring Clients
Stage: Recurring Quote Requested
- Create task: Send recurring cleaning quote to {{contact.name}}
- Notify owner/team.

5. If customer does not reply after 3 days, send Email.
Subject: Want to keep your home clean without rebooking every time?
Email body:
Hi {{contact.firstName}},

A lot of our clients prefer recurring cleaning because it keeps the home consistently fresh without having to remember to book.

Common options:
- Weekly
- Bi-weekly
- Monthly

If you want pricing, just reply to this email or text us back.

{{location.name}}

6. Wait 7 days.

7. If no reply, add tag recurring-upsell-sent and end workflow.
```

---

## WORKFLOW 7 — Review Request After Completed Clean

```text
Create a GoHighLevel workflow called “Cleaning Service - Review Request and Service Recovery”.

Goal:
Ask happy customers for reviews and route unhappy customers privately to the owner before they post publicly.

Trigger:
Opportunity stage changed to Completed in any cleaning pipeline.

Workflow steps:

1. Wait 24 hours.

2. Send SMS.
SMS:
Hi {{contact.firstName}}, thanks again for choosing {{location.name}}. On a scale of 1–5, how happy were you with your clean?

3. Wait for reply.

4. If reply is 4 or 5:
Send SMS:
That means a lot — thank you! Would you be willing to leave us a quick review? It helps local families and businesses find us: [GOOGLE REVIEW LINK]
Add tag: review-requested
Set custom field Review Requested = Yes

5. If reply is 1, 2, or 3:
Send SMS:
We’re sorry to hear that. What could we have done better? We’d rather fix it directly.
Send internal notification:
Service recovery needed: {{contact.name}} rated their clean {{contact.message}}/5. Contact them today.
Create task:
Call {{contact.name}} — cleaning service recovery.

6. If no reply after 3 days:
Send SMS:
Quick follow-up — if you were happy with your clean, a quick review would mean a lot: [GOOGLE REVIEW LINK]

7. End workflow.
```

---

## WORKFLOW 8 — Referral Ask After Positive Review

```text
Create a GoHighLevel workflow called “Cleaning Service - Referral Ask After Positive Review”.

Goal:
Ask happy customers for referrals after a positive review or successful completed clean.

Trigger:
Tag added: review-received
OR custom field Review Received = Yes.

Workflow steps:

1. Wait 5 days.

2. Send SMS.
SMS:
Hi {{contact.firstName}}, one more quick favour — if you know anyone who needs home, office, move-out, Airbnb, or deep cleaning, feel free to send them our way. Referrals mean a lot for a local business like ours 🙏 — {{location.name}}

3. Wait 14 days.

4. Send Email.
Subject: Know someone who needs a reliable cleaner?
Email body:
Hi {{contact.firstName}},

Thanks again for trusting {{location.name}}.

If you know someone who needs cleaning help — residential, commercial, move-in/move-out, Airbnb turnover, or deep cleaning — we’d be grateful if you sent them our way.

They can request a quote here:
[CLEANING QUOTE LINK]

{{location.name}}

5. Add tag: referral-requested

6. End workflow.
```

---

## WORKFLOW 9 — Recurring Cleaning Reminder / Rebooking

```text
Create a GoHighLevel workflow called “Cleaning Service - Recurring Cleaning Reminder and Rebooking”.

Goal:
Remind recurring clients about upcoming weekly, bi-weekly, or monthly cleans and reduce schedule confusion.

Trigger:
Appointment booked on recurring cleaning calendar.

Workflow steps:

1. Add tag: recurring-client

2. Send SMS immediately.
SMS:
Hi {{contact.firstName}}, your recurring cleaning with {{location.name}} is confirmed for {{appointment.startTime}}.

3. Wait until 24 hours before appointment.
Send SMS:
Reminder: your cleaning is tomorrow at {{appointment.startTime}}. Please reply with any access notes, pet updates, or priority areas. — {{location.name}}

4. Wait until 2 hours before appointment.
Send SMS:
We’ll see you soon! Your recurring clean is today at {{appointment.startTime}}. — {{location.name}}

5. Wait until 24 hours after appointment.
Send SMS:
Thanks {{contact.firstName}} — your clean is complete. If you have any feedback or priority notes for next time, reply here.

6. End workflow.
```

---

## WORKFLOW 10 — Airbnb / Short-Term Rental Turnover Workflow

```text
Create a GoHighLevel workflow called “Cleaning Service - Airbnb Turnover Workflow”.

Goal:
Manage Airbnb and short-term rental turnover leads with fast scheduling, guest-readiness reminders, and recurring turnover upsell.

Trigger:
Tag added: service-airbnb-turnover
OR custom field Cleaning Type equals Airbnb / Short-Term Rental Turnover.

Workflow steps:

1. Create or update opportunity in pipeline: Cleaning - Airbnb Turnovers
Stage: New Turnover Request

2. Send SMS immediately.
SMS:
Hi {{contact.firstName}}, thanks for reaching out about Airbnb/short-term rental turnover cleaning. What is the checkout date/time and next guest check-in date/time?

3. Send Email immediately.
Subject: Airbnb turnover request — quick details needed
Email body:
Hi {{contact.firstName}},

To confirm a turnover clean, please send:
- Property address/town
- Checkout time
- Next guest check-in time
- Number of beds/baths
- Laundry or linen requirements
- Restock requirements
- Access instructions
- Photos/checklist if available

{{location.name}}

4. Send internal notification:
New Airbnb turnover request from {{contact.name}}. Check deadline and availability.

5. Wait 15 minutes.

6. If no reply, send SMS:
Quick check — for turnovers, timing matters. What time does the current guest check out and the next guest check in?

7. If customer books or confirms:
- Move opportunity to stage: Turnover Scheduled
- Add tag: airbnb-turnover-booked
- Send confirmation SMS:
You’re booked for your turnover clean on {{appointment.startTime}}. Please make sure access, linens, and restock notes are ready. — {{location.name}}

8. After completed, wait 24 hours.
Send SMS:
Want to set up recurring turnover cleaning for this rental so you don’t have to rebook every time? Reply YES and we’ll help set it up.

9. If YES:
- Add tag: recurring-turnover-interest
- Create task: Set up recurring Airbnb turnover schedule for {{contact.name}}

10. End workflow.
```

---

## WORKFLOW 11 — Commercial Cleaning Lead Nurture

```text
Create a GoHighLevel workflow called “Cleaning Service - Commercial Cleaning Lead Nurture”.

Goal:
Qualify office, retail, salon/spa, daycare, venue, and commercial cleaning leads and move them toward a walkthrough or quote.

Trigger:
Tag added: service-commercial-cleaning
OR custom field Cleaning Type equals Commercial Cleaning.

Workflow steps:

1. Create or update opportunity in pipeline: Cleaning - Commercial Leads
Stage: New Commercial Inquiry

2. Send SMS immediately.
SMS:
Hi {{contact.firstName}}, thanks for reaching out about commercial cleaning. What type of space do you need cleaned — office, retail, salon/spa, daycare, venue, or something else?

3. Send Email immediately.
Subject: Commercial cleaning request received
Email body:
Hi {{contact.firstName}},

Thanks for reaching out to {{location.name}}.

To prepare a commercial cleaning quote, we’ll need:
- Type of business
- Approximate square footage
- Cleaning frequency needed
- Preferred days/times
- Number of washrooms/kitchens
- Any special requirements
- Address or town

The best next step is usually a quick walkthrough or phone consultation.

Book here:
[COMMERCIAL WALKTHROUGH OR CALL LINK]

{{location.name}}

4. Wait 1 day.

5. If no appointment booked, send SMS:
Hi {{contact.firstName}}, do you want to book a quick walkthrough or phone call for your commercial cleaning quote? Here’s the link: [COMMERCIAL WALKTHROUGH OR CALL LINK]

6. Wait 3 days.

7. If no appointment booked, create task:
Follow up with commercial cleaning lead {{contact.name}}

8. Wait 7 days.

9. If no response, add tag: commercial-cold-lead and move opportunity to stage: Follow-Up Later.
```

---

## WORKFLOW 12 — Dormant Cleaning Lead Reactivation

```text
Create a GoHighLevel workflow called “Cleaning Service - Dormant Lead Reactivation”.

Goal:
Re-engage cleaning leads who requested a quote or asked about service but never booked.

Trigger:
Tag added: cold-lead
OR opportunity moved to stage: Cold Lead.

Workflow steps:

1. Wait 14 days after cold-lead tag is added.

2. Send SMS.
SMS:
Hi {{contact.firstName}}, just checking — are you still looking for cleaning help, or should we close this out for now?

3. Wait 3 days.

4. If customer replies interested:
- Remove tag cold-lead
- Move opportunity to Follow-Up Active
- Send booking/quote link
- Notify owner/team.

5. If no reply, send Email.
Subject: Still need help with cleaning?
Email body:
Hi {{contact.firstName}},

Just checking in — if you still need cleaning help, we can help with:
- Regular home cleaning
- Deep cleaning
- Move-in/move-out cleaning
- Airbnb turnovers
- Commercial cleaning
- Post-construction cleaning

Request a quote or book here:
[CLEANING QUOTE OR BOOKING LINK]

{{location.name}}

6. Wait 30 days.

7. If no reply, send final SMS.
SMS:
Last check, {{contact.firstName}} — still need cleaning help? Reply CLEAN and we’ll help with the next step.

8. If still no reply after 7 days, leave tag cold-lead and end workflow.
```

---

## Optional Workflow 13 — Post-Construction Cleaning Lead Workflow

```text
Create a GoHighLevel workflow called “Cleaning Service - Post Construction Cleaning Lead Workflow”.

Goal:
Qualify post-construction cleaning leads and capture the details needed to quote properly.

Trigger:
Tag added: service-post-construction
OR custom field Cleaning Type equals Post-Construction Cleaning.

Workflow steps:

1. Create or update opportunity in pipeline: Cleaning - New Leads
Stage: Post-Construction Lead

2. Send SMS immediately.
SMS:
Hi {{contact.firstName}}, thanks for reaching out about post-construction cleaning. Is this for a home, commercial space, renovation, or new build?

3. Send Email immediately.
Subject: Post-construction cleaning request received
Email body:
Hi {{contact.firstName}},

Post-construction cleaning usually needs a few details before quoting:
- Property type
- Approximate square footage
- Renovation or new build?
- Deadline date
- Amount of dust/debris
- Windows, cabinets, appliances, or floors included?
- Address/town
- Photos if possible

Reply with the details or book a walkthrough here:
[WALKTHROUGH / QUOTE LINK]

{{location.name}}

4. Send internal notification:
Post-construction cleaning lead from {{contact.name}}. Review details and schedule walkthrough if needed.

5. Wait 1 day.

6. If no reply or booking, send SMS:
Quick check — do you want to book a walkthrough for the post-construction clean? Here’s the link: [WALKTHROUGH / QUOTE LINK]

7. Wait 3 days.

8. If no reply, create task:
Follow up with post-construction cleaning lead {{contact.name}}

9. End workflow.
```

---

## Suggested Tags for Cleaning Snapshot

```text
new-lead
quote-requested
cleaning-booked
customer-active
cold-lead
recurring-client
recurring-interest
recurring-upsell-sent
review-requested
review-received
referral-requested
service-residential-cleaning
service-deep-cleaning
service-move-in-out
service-commercial-cleaning
service-airbnb-turnover
service-post-construction
service-recurring-cleaning
service-one-time-cleaning
airbnb-turnover-booked
recurring-turnover-interest
commercial-cold-lead
no-show
cancelled
facebook-lead
google-lead
referral-lead
website-lead
```

---

## Suggested Pipelines for Cleaning Snapshot

```text
Pipeline 1: Cleaning - New Leads
Stages:
- New Inquiry
- Auto Reply Sent
- Quote Requested
- Needs More Info
- Quote Sent
- Follow-Up Active
- Booked
- Cold Lead
- Lost / Not Now

Pipeline 2: Cleaning - Bookings
Stages:
- Booked
- Confirmed
- Cleaner Assigned
- In Progress
- Completed
- Invoice Sent
- Paid
- Review Requested

Pipeline 3: Cleaning - Recurring Clients
Stages:
- Recurring Quote Requested
- Recurring Proposal Sent
- Active Weekly
- Active Bi-Weekly
- Active Monthly
- At Risk
- Paused
- Cancelled

Pipeline 4: Cleaning - Airbnb Turnovers
Stages:
- New Turnover Request
- Timing Confirmed
- Turnover Scheduled
- Cleaner Assigned
- Completed
- Issue Reported
- Recurring Turnover Offered
- Recurring Turnover Active

Pipeline 5: Cleaning - Commercial Leads
Stages:
- New Commercial Inquiry
- Walkthrough Booked
- Walkthrough Completed
- Proposal Sent
- Follow-Up Active
- Contract Won
- Active Account
- Lost / Not Now
```

---

## Suggested Calendars for Cleaning Snapshot

```text
Calendar 1: Residential Cleaning
Duration: 2-4 hours depending service
Use for: standard home cleans and recurring cleans

Calendar 2: Deep Cleaning / Move-Out Cleaning
Duration: 4-6 hours
Use for: deep cleans, move-in/move-out, one-time heavy cleans

Calendar 3: Commercial Walkthrough / Quote Call
Duration: 30 minutes
Use for: office, retail, salon/spa, daycare, venue, commercial spaces

Calendar 4: Airbnb Turnover Cleaning
Duration: variable
Use for: short-term rental turnover windows

Calendar 5: Post-Construction Walkthrough
Duration: 30 minutes
Use for: renovation/new-build quote review
```
