# Flooring Workflow AI Builder Prompts

Use these in GHL Automation → Workflows → Create Workflow → AI Builder.

Workflow 1 is NOT a workflow. Enable native Missed Call Text Back under Settings → Phone Numbers → Voicemail & Missed Call TextBack.

---

## WORKFLOW 2 — New Lead Speed to Response

```text
Build a workflow called "FLOORING — Speed to Response" for a flooring company. Trigger: Contact Created, no filters. Step 1: Immediately add tag "new-lead" and move the opportunity to the "New Lead" stage in the "Flooring - Residential Install" pipeline. Step 2: Immediately send SMS — "Hey {{contact.firstName}}! Thanks for reaching out about your flooring project. I’ll personally give you a call in the next few minutes to learn more about what you’re looking for. — {{location.name}}". Step 3: Immediately create internal task — "NEW FLOORING LEAD: {{contact.firstName}} {{contact.lastName}} | {{contact.phone}} — Call now!" Step 4: Wait 15 minutes with no appointment booked, send email with subject "Your free flooring measure is waiting" explaining that the company offers free in-home flooring measures and linking to the in-home measure calendar. Step 5: Wait 1 hour with no appointment booked, send SMS — "Still here when you’re ready, {{contact.firstName}}. Click here to book your free in-home flooring measure: [BOOKING LINK]". Step 6: Wait until next day afternoon with no reply or booking, send SMS — "Quick note — we offer free in-home measures with zero obligation. What flooring are you thinking about: hardwood, vinyl, laminate, tile, carpet, or refinishing?" Exit the workflow if the contact replies or books an appointment.
```

## WORKFLOW 3 — Measure Appointment Confirmation

```text
Build a workflow called "FLOORING — Measure Appointment Confirmation" for a flooring company. Trigger: Appointment booked OR pipeline stage changes to "Measure Appointment Scheduled" in any flooring pipeline. Step 1: Immediately send SMS — "Locked in! Your free flooring measure is set for {{appointment.startTime}}. We’ll call 15 minutes before arrival. Questions? Text anytime. — {{location.name}}". Step 2: Immediately send email with subject "Your flooring measure appointment is confirmed" confirming the appointment details and explaining what to prepare: clear access to rooms, note any squeaks/moisture/subfloor issues, have flooring inspiration photos ready, and make sure pets are secured. Step 3: Send reminder email the day before at 9:00 AM with subject "See you tomorrow for your flooring measure" and include prep tips. Step 4: Send SMS the day before at 5:00 PM — "Reminder: your flooring measure is tomorrow at {{appointment.startTime}}. We’ll call 15 minutes before arrival. Looking forward to it!" Step 5: Send SMS 2 hours before appointment — "Today’s the day! We’ll be there around {{appointment.startTime}} for your flooring measure. Text us here if anything changes."
```

## WORKFLOW 4 — No-Show Recovery

```text
Build a workflow called "FLOORING — No-Show Recovery" for a flooring company. Trigger: Appointment status changes to No Show. Step 1: Immediately add tag "no-show". Step 2: Same day, send SMS — "Hey {{contact.firstName}}, looks like we missed each other today! No worries — let’s find another time for your free flooring measure: [BOOKING LINK]". Step 3: Next day, send email with subject "Want to reschedule your flooring measure?" and include the booking link. Step 4: Wait 3 days, send SMS — "Still want to get that free flooring measure done? We have availability this week: [BOOKING LINK]". Step 5: Wait 7 days, send SMS — "Last check-in — if you’re still thinking about flooring, we’d love to help. No pressure. [BOOKING LINK]". If the contact books a new appointment, remove them from the workflow.
```

## WORKFLOW 5 — Sample Approval Follow-Up

```text
Build a workflow called "FLOORING — Sample Approval Follow-Up" for a flooring company. Trigger: Pipeline stage changes to "Sample Selection". Step 1: Immediately add tag "sample-pending". Step 2: Send SMS — "Your flooring sample has been dropped off! Try it in different rooms and different lighting. What’s your gut reaction?" Step 3: Wait 1 day, send SMS — "How’s the flooring looking in your space, {{contact.firstName}}? Try it next to your cabinets, trim, and furniture — that’s where it really tells the story." Step 4: Wait 2 days, send email with subject "How to evaluate your flooring sample" covering lighting at different times of day, comparing against trim/cabinets, checking grain direction, and taking side-by-side photos. Step 5: Wait 3 days, send SMS — "Loving it, hating it, or somewhere in between? No pressure — if it’s not right, we can show you more options at your price point." Step 6: Wait 5 days, send SMS — "Last check-in on the sample — ready to move forward, want a different option, or want to visit the showroom? Just reply and we’ll handle it." If the contact replies positively, move them to "Sample Approved", add tag "sample-approved", and remove tag "sample-pending". If no response after 7 days, add tag "cold-lead" and create internal task — "Follow up manually on flooring sample for {{contact.firstName}} {{contact.lastName}}".
```

## WORKFLOW 6 — Estimate Follow-Up Sequence

```text
Build a workflow called "FLOORING — Estimate Follow-Up Sequence" for a flooring company. Trigger: Pipeline stage changes to "Proposal Sent" on any flooring pipeline. Step 1: Immediately add tag "estimate-sent". Step 2: Wait 1 hour, send SMS — "Your flooring estimate just hit your inbox! Let me know if you have questions or want to go over anything, {{contact.firstName}}." Step 3: Wait 2 days, send email with subject "How to read your flooring estimate" explaining what is included: materials, labour, removal, underlayment, transitions, prep, and cleanup. Step 4: Wait 3 days, send SMS — "Quick check-in — have you had a chance to look over your flooring estimate? Happy to answer any questions." Step 5: Wait 5 days, send email with subject "Flooring options at your price point" comparing hardwood, LVP, laminate, tile, and carpet options. Step 6: Wait 7 days, send SMS — "Still thinking it over? A few flooring materials have lead times, so if you’re leaning toward moving ahead, we can help hold your spot." Step 7: Wait 9 days, send email with subject "Common questions before booking your flooring project" covering install time, furniture, pets, baseboards, and cleanup. Step 8: Wait 10 days, send SMS — "Last touch for now — if timing doesn’t work, no problem. Reply READY and we’ll get your flooring project on the schedule." Step 9: Wait 21 days, send SMS — "Hey {{contact.firstName}}, it’s {{location.name}}. Still thinking about the flooring project? Happy to revisit or adjust the quote if needed." Exit the workflow if the contact replies, moves stages, signs contract, or pays deposit.
```

## WORKFLOW 7 — Material Lead Time Update

```text
Build a workflow called "FLOORING — Material Lead Time Update" for a flooring company. Trigger: Pipeline stage changes to "Material Ordered" OR tag "material-on-order" is added. Step 1: Immediately send SMS — "Great news — your flooring order is placed! Expected arrival: [LEAD TIME]. We’ll text you the moment it’s in. Any questions in the meantime?" Step 2: Wait 3 days, send email with subject "While your flooring is on its way" with prep tips: clearing space, furniture planning, baseboards, pets, access, and what to expect before install. Step 3: When material arrives using a manual trigger or tag update, send SMS — "Great news — your flooring is in! Ready to schedule your install? Here are the next available dates: [BOOKING LINK]" Step 4: Send email with subject "Your flooring order has arrived" including install prep checklist and next steps.
```

## WORKFLOW 8 — Install Day Notification

```text
Build a workflow called "FLOORING — Install Day Notification" for a flooring company. Trigger: Pipeline stage changes to "Install Scheduled". Step 1: 7 days before install, send email with subject "Your flooring install is coming up" explaining how to prepare: furniture removal, clear pathways, pets, parking, access, dust/noise expectations, and baseboard notes. Step 2: 3 days before install, send SMS — "3 days until install day! Quick reminder: clear access to the work areas, plan for pets, and let us know if anything changed. Questions before the crew arrives?" Step 3: Day before at 9:00 AM, send email with subject "Flooring install day guide" covering arrival window, crew size, daily progress timeline, cleanup, and what to expect. Step 4: Day before at 5:00 PM, send SMS — "Tomorrow’s the big day! The crew will arrive between [WINDOW]. We’ll call 30 minutes before. See you then!" Step 5: Morning of install at 7:00 AM, send SMS — "Good morning! The {{location.name}} crew is on the way. Arrival estimate: [TIME]. Excited for you to see the transformation!"
```

## WORKFLOW 9 — Post-Install Review and Neighbour Campaign

```text
Build a workflow called "FLOORING — Post-Install Review and Neighbour Campaign" for a flooring company. Trigger: Pipeline stage changes to "Job Complete" on any flooring pipeline. Step 1: Immediately add tags "job-complete" and "review-requested". Step 2: Wait 1 hour, send SMS — "The floors look amazing! If you’re happy with how everything turned out, a quick Google review means the world to a local business: [GOOGLE REVIEW LINK]". Step 3: Wait 1 day, send email with subject "Your flooring project is complete" including summary of work, care and maintenance guide, warranty info, and review request. Step 4: Wait 2 days, create internal task — "Drop 10 door hangers near {{contact.address}} — flooring job just completed. Neighbour campaign." Step 5: Wait 2 days, send SMS — "Quick favour — did any neighbours mention they liked the new floors? If they’re interested, we’d take great care of them. Feel free to share our number!" Step 6: Wait 3 days, send SMS — "Still thinking about leaving a review? It only takes 2 minutes: [GOOGLE REVIEW LINK]" Step 7: Wait 7 days, send email with subject "Care tips for your new floors" with product-specific maintenance advice and a soft referral ask. Step 8: Wait 7 days, send SMS — "Hey {{contact.firstName}}! If any neighbours mention they like your new floors, send them our way — we have a referral program: [REFERRAL LINK]". If review-received tag is added, remove review-requested tag and stop review reminders.
```

## WORKFLOW 10 — Unhappy Customer Recovery

```text
Build a workflow called "FLOORING — Unhappy Customer Recovery" for a flooring company. Trigger: Tag "unhappy-customer" is added. This workflow is internal only and must not send customer-facing messages. Step 1: Immediately send internal email to owner with subject "URGENT: Flooring customer complaint" and body "Customer complaint flagged for {{contact.firstName}} {{contact.lastName}} — {{contact.phone}}. Immediate follow-up required. Check contact notes before calling." Step 2: Immediately create internal task — "PRIORITY: Call {{contact.firstName}} within 30 minutes re: complaint. Review notes first." Step 3: Wait 1 hour, create internal task — "Has complaint been addressed? Update contact notes and remove unhappy-customer tag when resolved." Step 4: Pause or suppress marketing automation for this contact until the issue is resolved.
```

## WORKFLOW 11 — Insurance Claim Fast-Track

```text
Build a workflow called "FLOORING — Insurance Claim Fast-Track" for a flooring company. Trigger: Insurance Claim custom field changes to Yes OR tag "insurance-claim" is added. Step 1: Move opportunity to the "Insurance / Water Damage" flooring pipeline. Step 2: Immediately send SMS — "Hi {{contact.firstName}}, this is {{location.name}}. I understand you’re dealing with water damage — we work with flooring insurance claims regularly and can assess within 24 hours. Are you available tomorrow morning or afternoon?" Step 3: Immediately send email with subject "Emergency flooring replacement — what to expect" explaining the insurance claim process, adjuster role, inspection, estimate, approval timeline, material ordering, and install scheduling. Step 4: Immediately create internal task — "PRIORITY: Emergency flooring assessment for {{contact.firstName}} at {{contact.address}}. Call within 30 minutes." Step 5: Wait 3 days, send SMS — "Quick update on your claim: we submitted the flooring estimate to your insurance company. We’ll notify you the moment we hear back. Any questions?" Step 6: Wait 6 days, send SMS — "Checking in — no news yet from the insurer. We’re following up on our end. Typical approval time is 5–10 business days from submission." Step 7: On approval using manual trigger, send SMS — "Great news — your insurance approved the scope! We’re ready to get started. When works for a quick call to review next steps?"
```

## WORKFLOW 12 — Real Estate Agent Referral Nurture

```text
Build a workflow called "FLOORING — Real Estate Agent Referral Nurture" for a flooring company. Trigger: Tag "real-estate-agent" is added. Step 1: Immediately send SMS — "{{contact.firstName}}, thanks for connecting! We specialize in pre-listing flooring refreshes — fast turnaround, clean work, and agent-priority scheduling. Do you have a listing coming up where the floors need attention?" Step 2: Wait 3 days, send email with subject "Why flooring is one of the highest-ROI pre-listing upgrades" explaining fast LVP, hardwood refinishing, carpet replacement, and small upgrades that help homes show better. Step 3: Wait 2 weeks, send SMS — "Working on any listings where the floors need attention? LVP installs can be done fast for smaller spaces — perfect for tight listing timelines." Step 4: Wait 3 weeks, send email with subject "Before and after: pre-listing flooring transformations" and include photo gallery placeholders. Step 5: Wait 4 weeks, send SMS — "We prioritize agent referrals for fast turnaround. Most pre-listing jobs can be measured quickly and scheduled around listing timelines." Step 6: Wait 2 months, send email with subject "Our agent referral program" explaining referral incentive details. If first referral job is won, apply tag "repeat-customer" and create task to thank the agent.
```

## WORKFLOW 13 — Property Manager Account Outreach

```text
Build a workflow called "FLOORING — Property Manager Account Outreach" for a flooring company. Trigger: Tag "property-manager" is added. Step 1: Immediately send SMS — "Hi {{contact.firstName}}, this is {{location.name}}. We specialize in flooring for rentals and multi-unit buildings — quick turnaround, durable materials, and minimal disruption to tenants. Do you have any units coming up for flooring?" Step 2: Wait 2 days, send email with subject "Commercial flooring built for property managers" covering durable flooring options, fast booking, invoice-ready documentation, tenant turnover timelines, and multi-unit pricing. Step 3: After first job is completed using a manual trigger or job-complete tag, send SMS — "Thanks for the job at [PROPERTY]. Our crew is built for efficient unit turnovers. Happy to quote your next unit or building anytime." Step 4: Monthly, send email with subject "Available install windows for your properties" with upcoming availability and unit-turnover flooring specials.
```

## WORKFLOW 14 — Spring Renovation Campaign

```text
Build a workflow called "FLOORING — Spring Renovation Campaign" for a flooring company. Trigger: Date/time based every year on April 1. Filter audience to contacts tagged warm-lead, cold-lead, or nurture with no active pipeline. Step 1: April 1, send email with subject "Spring is here — perfect time to refresh your floors" with trending flooring ideas and gallery placeholders. Step 2: April 3, send SMS — "Spring is the busiest time for flooring and our measure schedule fills fast. Want to get your free measure on the calendar? [BOOKING LINK]" Step 3: April 7, send email with subject "Limited spring availability — lock in your install before summer" explaining lead times and booking windows. Step 4: April 10, send SMS — "Final heads up — we have limited measure slots left this month. Happy to hold one for you: [BOOKING LINK]" Stop workflow if contact books or replies.
```

## WORKFLOW 15 — Fall Refresh Campaign

```text
Build a workflow called "FLOORING — Fall Refresh Campaign" for a flooring company. Trigger: Date/time based every year on September 1. Filter audience to contacts tagged warm-lead, cold-lead, or nurture with no active pipeline. Step 1: September 1, send email with subject "Fall flooring refresh — get your project done before the holidays". Step 2: September 3, send SMS — "Perfect time to get new floors in before family comes over for the holidays. We’re booking October and November now: [BOOKING LINK]" Step 3: September 7, send email with subject "Flooring for colder months" explaining why LVP, engineered hardwood, carpet, and tile upgrades make sense before winter. Step 4: September 10, send SMS — "November installs are filling up. If you’ve been thinking about flooring, now’s the time: [BOOKING LINK]" Stop workflow if contact books or replies.
```

## WORKFLOW 16 — Refinishing Upsell

```text
Build a workflow called "FLOORING — Refinishing Upsell" for a flooring company. Trigger: Flooring Material custom field equals Hardwood OR tag "hardwood-interest" is added, only for contacts with no active pipeline. Step 1: Send SMS — "Hi {{contact.firstName}}! Quick question — how are your hardwood floors holding up? If they’re looking worn, refinishing might be the answer. It costs a fraction of replacement and makes the floors look brand new. Interested in a free assessment?" Step 2: Wait 3 days, send email with subject "Restore your hardwood before replacing it" explaining refinishing vs replacement, cost savings, sanding, staining, finish options, and when replacement is actually needed. Step 3: Wait 7 days, send SMS — "If you’re curious what your floors could look like with a full sand and refinish, we can show before/afters from similar homes. Want me to send some photos?" Stop if contact replies or books.
```

## WORKFLOW 17 — Estimate Expired Reactivation

```text
Build a workflow called "FLOORING — Estimate Expired Reactivation" for a flooring company. Trigger: Contact has been in "Proposal Sent" stage for 60 days with no activity. Step 1: Send email with subject "Want us to refresh your flooring quote?" explaining that pricing, material availability, and install windows may have changed. Step 2: Send SMS — "Hey {{contact.firstName}} — we quoted your flooring project a couple months ago. Still on the radar? Happy to refresh the numbers or show updated options." Step 3: Wait 7 days with no reply, add tag "cold-lead" and create internal task — "Check if flooring estimate should be archived or reactivated for {{contact.firstName}}".
```

## WORKFLOW 18 — Referral Thank-You and Tracking

```text
Build a workflow called "FLOORING — Referral Thank-You and Tracking" for a flooring company. Trigger: Tag "referral" is added to a new contact. Step 1: Immediately create internal task — "Contact referral source for {{contact.firstName}} {{contact.lastName}} — thank them and track referral source." Step 2: Add tag "referral-lead". Step 3: When job is won using manual trigger or stage change to Contract Signed / Deposit, send SMS to referral source — "Your referral just booked! Thank you — we appreciate you sending them our way. [REFERRAL REWARD DETAILS]" Step 4: Create internal task — "Confirm referral reward for source tied to {{contact.firstName}}".
```

## WORKFLOW 19 — Commercial Account Quarterly Check-In

```text
Build a workflow called "FLOORING — Commercial Account Quarterly Check-In" for a flooring company. Trigger: Date/time based every 90 days. Filter contacts tagged "property-manager" or "commercial-flooring". Step 1: Send email with subject "Quarterly flooring update for your properties" covering available install windows, new durable product options, multi-unit pricing, tenant turnover scheduling, and commercial maintenance support. Step 2: Send SMS — "Hi {{contact.firstName}}, checking in — any units or commercial spaces coming up that need flooring this quarter? Happy to quote fast." Step 3: If contact replies, create internal task — "Commercial flooring follow-up for {{contact.firstName}}".
```

## WORKFLOW 20 — Google Review Follow-Up

```text
Build a workflow called "FLOORING — Google Review Follow-Up" for a flooring company. Trigger: Tag "review-requested" is added and tag "review-received" is not present after 7 days. Step 1: Wait 7 days, send SMS — "We noticed you haven’t had a chance to leave a review yet — no worries! If you get a moment, it only takes 2 minutes and really helps us: [GOOGLE REVIEW LINK]" Step 2: Wait 14 days, send email with subject "Quick favour — could you leave us a review?" and include the Google review link. Step 3: Stop if tag "review-received" is added.
```

## WORKFLOW 21 — Negative Review Intercept

```text
Build a workflow called "FLOORING — Negative Review Intercept" for a flooring company. Trigger: Tag "negative-feedback" is added. This workflow is internal only. Step 1: Immediately send internal email to owner with subject "URGENT: Negative flooring feedback flagged" and include contact name, phone, email, and notes. Step 2: Immediately create internal task — "Call {{contact.firstName}} within 30 minutes to resolve issue before any review request or marketing continues." Step 3: Remove or suppress review-requested workflows for this contact. Step 4: Add tag "automation-hold" so no promotional automation continues until resolved.
```

## WORKFLOW 22 — Deposit Payment Reminder

```text
Build a workflow called "FLOORING — Deposit Payment Reminder" for a flooring company. Trigger: Opportunity moves to "Contract Signed / Deposit" and Deposit Paid custom field is No after 48 hours. Step 1: Send SMS — "Quick reminder — to lock in your flooring install date, we’ll need the deposit processed. Here’s how to pay: [PAYMENT LINK]" Step 2: Wait 3 days, send email with subject "Deposit payment needed to secure your install date" with payment instructions and who to contact with questions. Step 3: Create internal task — "Follow up on unpaid flooring deposit for {{contact.firstName}} {{contact.lastName}}".
```

## WORKFLOW 23 — Final Payment Reminder

```text
Build a workflow called "FLOORING — Final Payment Reminder" for a flooring company. Trigger: Opportunity moves to "Invoice Sent" stage. Step 1: Wait 3 days, send SMS — "Your flooring invoice was sent. Did you receive it okay? Let us know if you need it resent." Step 2: Wait 7 days, send email with subject "Following up on your flooring invoice" with payment instructions and invoice details placeholder. Step 3: Wait 14 days, create internal task — "Escalate: {{contact.firstName}} invoice unpaid 14 days." Step 4: Add tag "payment-follow-up".
```

## WORKFLOW 24 — Care and Maintenance Onboarding

```text
Build a workflow called "FLOORING — Care and Maintenance Onboarding" for a flooring company. Trigger: Opportunity moves to "Job Complete" OR tag "job-complete" is added. Step 1: Day 1, send email with subject "How to care for your new floors" and personalize content based on Flooring Material field: hardwood, LVP, laminate, tile, carpet, or refinishing. Step 2: Wait 30 days, send SMS — "30-day check-in — how are your new floors holding up? Any questions about care or maintenance?" Step 3: Wait 90 days, send email with subject "3-month care tips for your floors" with cleaning tips, warranty reminders, and referral ask.
```

## WORKFLOW 25 — Subfloor Repair Update Notification

```text
Build a workflow called "FLOORING — Subfloor Repair Update Notification" for a flooring company. Trigger: Tag "subfloor-issue" is added by installer or rep. Step 1: Immediately send SMS — "Hi {{contact.firstName}}, our crew found something with the subfloor that we need to discuss before proceeding. Are you available for a quick call in the next 15 minutes?" Step 2: Immediately send email with subject "Subfloor issue found — approval needed" including summary placeholder, photo placeholder, and Option A / Option B approval request. Step 3: Immediately create internal task — "Call {{contact.firstName}} within 30 minutes re: subfloor issue and document approval." Step 4: Add tag "approval-needed".
```

## WORKFLOW 26 — Material Arrival Notification

```text
Build a workflow called "FLOORING — Material Arrival Notification" for a flooring company. Trigger: Tag "material-arrived" is added OR manual trigger by rep. Step 1: Send SMS — "Great news — your flooring is in! Ready to schedule your install? Here are the next available dates: [BOOKING LINK]" Step 2: Send email with subject "Your flooring order has arrived" with install prep checklist, scheduling instructions, and what happens next. Step 3: Create internal task — "Schedule install for {{contact.firstName}} — material arrived." Step 4: Remove tag "material-on-order" if present.
```

## WORKFLOW 27 — Holiday Shutdown Notification

```text
Build a workflow called "FLOORING — Holiday Shutdown Notification" for a flooring company. Trigger: Date/time based every year on December 15. Filter to all active pipeline contacts. Step 1: Send email with subject "Holiday hours and your flooring project" explaining closed dates, reopening date, emergency water damage contact process, and reassurance that active projects are not forgotten. Step 2: Send SMS — "Quick holiday heads up from {{location.name}}: we’re closed [DATES CLOSED] and reopen [DATE]. If your project is active, we’ll keep you updated. Emergency water damage? Call [PHONE]."
```

## WORKFLOW 28 — New Product Announcement

```text
Build a workflow called "FLOORING — New Product Announcement" for a flooring company. Trigger: Manual launch trigger. Filter to contacts tagged warm-lead, estimate-sent, sample-pending, hardwood-interest, LVP-interest, or commercial-flooring. Step 1: Send email with subject "Just in: [NEW PRODUCT NAME]" with product specs, photos, pricing range, best-use cases, and booking link. Step 2: Wait 1 day, send SMS — "We just got [NEW PRODUCT NAME] in — thought you might want to see it based on what you were looking for. Want photos or a sample?" Step 3: If contact replies, create internal task — "Send new product info/sample to {{contact.firstName}}".
```

## WORKFLOW 29 — 12-Month Win-Back Campaign

```text
Build a workflow called "FLOORING — 12-Month Win-Back Campaign" for a flooring company. Trigger: Date-based or smart list filter for contacts quoted 12+ months ago who never converted. Step 1: Send email with subject "Still thinking about flooring?" explaining that products, pricing, and availability may have changed since their quote. Step 2: Send SMS — "Hey {{contact.firstName}}! We quoted your flooring project about a year ago. Prices and products have changed a lot — want a fresh look?" Step 3: Wait 7 days with no reply, send SMS — "No pressure — if the project is off the table, just reply STOP. If it’s still on your list, we can refresh the quote." Step 4: If no response, add tag "cold-lead".
```

## WORKFLOW 30 — Internal Escalation

```text
Build a workflow called "FLOORING — Internal Escalation" for a flooring company. Trigger: Tag "escalate" is added OR complaint flag is applied. This workflow is internal only and must send no customer-facing messages. Step 1: Immediately send internal email to owner and manager with subject "ESCALATION: {{contact.firstName}} requires immediate attention" including contact name, phone, email, opportunity, and notes. Step 2: Immediately create task — "ESCALATION: Call {{contact.firstName}} immediately and update notes." Step 3: Add tag "automation-hold". Step 4: Create follow-up task after 24 hours — "Confirm escalation resolved and remove automation-hold if safe."
```
