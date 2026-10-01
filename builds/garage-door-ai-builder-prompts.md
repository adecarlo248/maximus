# Garage Door Workflow AI Builder Prompts

Use these in GHL Automation → Workflows → Create Workflow → AI Builder.

Workflow 1 is NOT a workflow. Enable native Missed Call Text Back under Settings → Phone Numbers → Voicemail & Missed Call TextBack.

---

## WORKFLOW 1 — Missed Call Text Back — Native Setting

```text
Do not build this as a workflow. Enable GHL native Missed Call Text Back under Settings → Phone Numbers → Voicemail & Missed Call TextBack. Use this message: "Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — garage door emergency or need to book a service? Reply EMERGENCY or BOOK and we'll get right back to you 👋"
```

---

## WORKFLOW 2 — New Emergency Lead Speed to Dispatch

```text
Build a workflow called "GARAGE DOOR — Emergency Speed to Dispatch" for a garage door company. Trigger: Tag "emergency-repair" is added OR opportunity is created in the "Garage Door - Emergency Repair" pipeline at stage "New Emergency Call". Step 1: Immediately send SMS — "Hi {{contact.firstName}}, we got your emergency request. A technician will be calling you within the next 10 minutes. Please keep your phone nearby." Step 2: Immediately create internal task assigned to the owner — "🚨 EMERGENCY DISPATCH — {{contact.firstName}} {{contact.lastName}} | Phone: {{contact.phone}} | Address: {{contact.address1}} | Time submitted: {{now}} | ACTION REQUIRED: Call client immediately and dispatch tech." Step 3: Immediately send internal notification email to team with subject "🚨 Emergency Garage Door Lead — Immediate Action Required" and include contact name, phone, address, and time submitted. Step 4: Move opportunity to "Dispatched" stage once dispatch task is completed. Keep this workflow emergency-first and do not delay the internal alert.
```

## WORKFLOW 3 — Emergency Dispatch Confirmation and ETA

```text
Build a workflow called "GARAGE DOOR — Emergency Dispatch Confirmation and ETA" for a garage door company. Trigger: Pipeline stage changes to "Dispatched" in the "Garage Door - Emergency Repair" pipeline. Step 1: Immediately send SMS — "Your technician is on the way! {{custom.technicianName}} will arrive in approximately {{custom.eta}}. You'll get a text when they're 15 minutes out." Step 2: Create internal task — "Confirm technician name and ETA were filled for {{contact.firstName}} {{contact.lastName}}." Step 3: Add a manual-trigger branch or wait step for the dispatcher/tech to send the 15-minute ETA reminder. SMS for 15-minute reminder: "{{contact.firstName}}, your tech is 15 minutes away! Please make sure someone is home to let them in." Note: Technician name and ETA fields must be filled manually by dispatcher before triggering this branch.
```

## WORKFLOW 4 — Scheduled Appointment Confirmation and Reminders

```text
Build a workflow called "GARAGE DOOR — Scheduled Appointment Confirmation and Reminders" for a garage door company. Trigger: Customer booked appointment on either "Scheduled Repair Appointment" calendar or "Free Estimate - New Door" calendar. Step 1: Immediately send SMS — "Hi {{contact.firstName}}, you're confirmed! Your garage door appointment is scheduled for {{appointment.startTime}} on {{appointment.startDate}}. Reply CANCEL to cancel or RESCHEDULE to change your time. — {{location.name}}" Step 2: Immediately send email with subject "Your Appointment is Confirmed — {{location.name}}" including full appointment details, explaining the technician will call 30 minutes before arrival, what to expect, and how to reschedule. Step 3: 24 hours before appointment, send SMS — "Reminder: Your garage door appointment is tomorrow at {{appointment.startTime}}. Address: {{contact.address1}}. Questions? Reply or call us. See you tomorrow!" Step 4: 2 hours before appointment, send SMS — "Just a heads up — your technician will arrive in about 2 hours ({{appointment.startTime}}). Please make sure someone is home. See you soon!" Stop if appointment is cancelled or rescheduled.
```

## WORKFLOW 5 — No-Show Recovery

```text
Build a workflow called "GARAGE DOOR — No-Show Recovery" for a garage door company. Trigger: Appointment status changes to No Show. Step 1: Wait 30 minutes after scheduled appointment end time. Step 2: Add tag "no-show". Step 3: Send SMS — "Hey {{contact.firstName}}, did we get the time wrong? We can still send someone today. Reply RESCHEDULE or call us and we'll get you sorted." Step 4: Wait 4 hours with no reply, send SMS — "{{contact.firstName}}, we want to make sure your garage door gets fixed. We have openings this week — reply YES and we'll find you a spot." Step 5: Create internal task for owner — "No-show — follow up with {{contact.firstName}} via phone." Stop workflow if contact replies or books a new appointment.
```

## WORKFLOW 6 — Post-Emergency Review Request

```text
Build a workflow called "GARAGE DOOR — Post-Emergency Review Request" for a garage door company. Trigger: Pipeline stage changes to "Review Requested" in the "Garage Door - Emergency Repair" pipeline. Step 1: Wait 90 minutes after trigger. Step 2: Send SMS — "Hope your garage door is working perfectly! If we saved the day, a quick Google review means the world to us: [GOOGLE REVIEW LINK] Takes 60 seconds and helps families in [CITY] find reliable help when they need it most. Thank you! 🙏" Step 3: Update custom field "Review Requested" to Yes. Step 4: Wait 3 days. If review has not been received, send email with subject "One small favour from {{location.name}}..." thanking them for trusting the company in an emergency, asking for a Google review, and including the direct review link. Stop review reminders if review-received tag or Review Received field is set.
```

## WORKFLOW 7 — Post-Scheduled Job Review Request

```text
Build a workflow called "GARAGE DOOR — Post-Scheduled Job Review Request" for a garage door company. Trigger: Pipeline stage changes to "Review Requested" in the "Garage Door - Scheduled Repair" pipeline. Step 1: Wait until next morning at 9:00 AM, with a minimum 12-hour delay after trigger. Step 2: Send SMS — "Hi {{contact.firstName}}! Hope the garage door is running smoothly. We'd love a quick Google review if you were happy with the work — it really helps us out: [GOOGLE REVIEW LINK] Thanks for choosing us! 🙏" Step 3: Same day at 10:00 AM, send email with subject "How did we do? — {{location.name}}" thanking them, describing the service completed, and including the review link plus before/after photo placeholder if available. Step 4: Update custom field "Review Requested" to Yes. Stop if review-received tag or Review Received field is set.
```

## WORKFLOW 8 — New Door Installation Estimate Follow-Up

```text
Build a workflow called "GARAGE DOOR — New Door Installation Estimate Follow-Up" for a garage door company. Trigger: Pipeline stage changes to "Proposal Sent" in the "Garage Door - New Door Installation" pipeline. Step 1: Wait 1 day, send SMS — "Hi {{contact.firstName}}, just wanted to make sure you got our quote for your new garage door. Any questions I can answer? I'm happy to walk you through the options. — [NAME]" Step 2: Wait 3 days, send email with subject "Your Garage Door Proposal — A Few Things Worth Knowing" covering warranty, install time, before/after examples, product options, and inviting them to call or book a 15-minute call. Step 3: Wait 7 days, send SMS — "{{contact.firstName}}, we have a few install slots opening up next week. Want to lock one in before they fill? Reply YES and I'll reach out directly." Step 4: Wait 14 days, send email with subject "Still thinking it over? Here's what our customers say..." including 2–3 testimonials, photos, quote validity period, and booking link. Step 5: Wait 21 days, send SMS — "Hey {{contact.firstName}}, last check-in from us on your garage door quote. The offer stands — whenever you're ready, we're here. No pressure. 🙂" Step 6: If no reply after sequence, add tag "cold-lead" and remove from active follow-up. Exit workflow if contact replies, books, signs contract, or moves out of Proposal Sent/Follow-Up Active.
```

## WORKFLOW 9 — Smart Opener Upsell

```text
Build a workflow called "GARAGE DOOR — Smart Opener Upsell" for a garage door company. Trigger: Tag "aging-opener-10yr" is added OR tag "aging-opener-15yr" is added after completed repair OR pipeline stage changes to "Smart Opener Upsell" in Emergency Repair pipeline OR pipeline stage changes to "Upsell Follow-Up" in Scheduled Repair pipeline. Step 1: Wait 48 hours after job complete. Step 2: If contact has tag "aging-opener-10yr", send SMS — "Hi {{contact.firstName}}, quick follow-up from your recent service. Our tech noted your garage door opener is around {{contact.opener_age}} years old. These units are approaching the end of their lifespan. A smart opener upgrade runs $[PRICE] installed — and you'll love the app control + auto-close features. Want a quick quote?" Step 3: If contact has tag "aging-opener-15yr", send SMS — "Hi {{contact.firstName}}, your garage door opener is {{contact.opener_age}} years old — that's past the typical lifespan. When older units fail, it's usually without warning and always at the worst time 😅. We can upgrade you to a smart opener for $[PRICE] installed. Reply YES and I'll get you a confirmed price today." Step 4: Wait until Day 5, send email to both branches with subject "Before Your Opener Fails — Upgrade to Smart for $[PRICE]" comparing old opener vs smart opener features, app control, auto-close, security alerts, and booking link for install estimate. Step 5: Update field "Smart Opener Upsell Offered" to Yes. Stop if contact replies, books, or declines.
```

## WORKFLOW 10 — Annual Tune-Up Reminder

```text
Build a workflow called "GARAGE DOOR — Annual Tune-Up Reminder" for a garage door company. Trigger: Date/time based twice per year: Spring campaign March 1–15 and Fall campaign October 1–15. Target segment: contacts tagged "job-complete" who do not have current-year "annual-tune-up" tag. Spring branch Step 1: Send SMS — "Hi {{contact.firstName}}! Spring is here — time to make sure your garage door is ready for the season. We're booking spring tune-ups now: $[PRICE] covers full inspection, lubrication, balance check & spring test. Book here: [ANNUAL TUNE-UP BOOKING LINK] — {{location.name}}" Fall branch Step 1: Send SMS — "{{contact.firstName}}, fall is here and winter is coming! A pre-winter garage door tune-up can prevent costly emergency repairs in -20°C weather. We're running fall specials now — only $[PRICE] for a full service. Book your spot: [ANNUAL TUNE-UP BOOKING LINK]" Step 2: Wait 3 days after SMS, send follow-up email to contacts who have not booked with subject "[Spring/Fall] Garage Door Tune-Up — Book Before Slots Fill" explaining what is included in the tune-up, seasonal safety benefits, and CTA to book. Step 3: After booking, add tag "annual-tune-up" and update field "Annual Tune-Up Date" to appointment date. Appointment confirmation and reminders should be handled by the scheduled appointment confirmation workflow.
```

---

## Recommended Build Order

1. Workflow 2 — Emergency Speed to Dispatch
2. Workflow 4 — Scheduled Appointment Confirmation and Reminders
3. Workflow 8 — New Door Installation Estimate Follow-Up
4. Workflow 6 — Post-Emergency Review Request
5. Workflow 7 — Post-Scheduled Job Review Request
6. Workflow 5 — No-Show Recovery
7. Workflow 9 — Smart Opener Upsell
8. Workflow 10 — Annual Tune-Up Reminder
9. Workflow 3 — Emergency Dispatch Confirmation and ETA

