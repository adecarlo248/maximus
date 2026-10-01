# 1APP Master SOP Manual

**Company:** 1APP Technologies Inc.  
**Version:** 1.2 Review Draft  
**Effective date:** Pending owner approval  
**Process owner:** Tony DeCarlo  
**Commercial owner:** Justin Roffey

---

## 1. Purpose

This manual turns 1APP into a repeatable business that can grow from the first clients to 100–200+ active clients without relying on tribal knowledge.

Every process must produce five things:

1. A clear owner.
2. A defined trigger.
3. A repeatable checklist.
4. A measurable completion standard.
5. A record inside 1APP.

## 2. Operating Principles

1. **One system of record:** If it is not recorded in 1APP, it did not happen.
2. **No promises from memory:** Scope, price, timing, and exceptions must be written in the opportunity record.
3. **Accepted scope before build:** Trial fulfillment begins only after the custom quote and trial scope are accepted in writing. Paid service begins only after conversion authorization and the required payment clears.
4. **Handoff before setup:** Technical work does not begin until the sales handoff is complete.
5. **Template first:** Use an approved 1APP industry template before building anything custom.
6. **Test before launch:** No workflow, phone route, calendar, AI agent, or payment flow goes live without documented QA.
7. **Least privilege:** Each user receives only the access required for their role.
8. **Client language is 1APP language:** Refer only to 1APP and its features in all documentation and communication.
9. **No unsupported claims:** Never guarantee leads, revenue, rankings, response rates, or results.
10. **Protect recurring revenue:** Onboarding, adoption, support, reporting, and renewal are revenue functions.

## 3. Roles and Decision Rights

### Justin Roffey — Sales and Business Development

Justin owns:

- Prospecting strategy and daily sales activity.
- Lead qualification and discovery.
- Audit/demo booking and follow-up.
- Custom automation quotes and commercial conversations.
- Opportunity accuracy and next actions.
- Sales-to-fulfillment handoff completeness.
- Commercial relationship management.

Justin may not unilaterally:

- Discount approved pricing.
- Promise custom features or integrations.
- Change contract terms.
- Commit to a launch date before fulfillment review.
- Promise results or guarantees not in the approved offer.

### Tony DeCarlo — Technology, Implementation, and Fulfillment

Tony owns:

- Technical discovery and feasibility.
- 1APP account provisioning.
- Industry template selection and configuration.
- Phone, calendar, CRM, workflow, AI, and integration setup.
- Data import quality.
- Testing, launch approval, and rollback plans.
- Technical support and incident response.
- Fulfillment documentation and process improvement.

Tony may not unilaterally:

- Change pricing or payment terms.
- Expand client scope without a written change request.
- Provide free custom work because a request feels small.
- Launch an untested configuration.

### Joint Approval Required

Tony and Justin must both approve:

- Custom pricing or discounts.
- Refunds, credits, or waived setup fees.
- Non-standard contract terms.
- Custom development or integrations.
- Public case studies and testimonials.
- Client suspension or termination.
- Changes to pricing rules, the automation catalogue, commission plans, or trial promises.

### Future Team Roles

- **Sales Associate:** Prospecting, qualification, follow-up, approved demos, and clean CRM records.
- **Onboarding Coordinator:** Form completion, missing information, access collection, scheduling, and status updates.
- **Implementation Specialist:** Approved template setup, configuration, testing, and documentation.
- **Support Specialist:** Ticket triage, standard fixes, client communication, and escalation.
- **Customer Success Manager:** Adoption, reviews, renewals, referrals, and expansion.

## 4. Current Offer Control

1APP does not sell locked-in tiers. It sells a custom set of automations selected after a free quote/demo.

**Public offer:**

- Custom automation starting as low as **$99/month**.
- **14-day free trial**.
- **No credit card required** to begin the trial.
- The free trial covers **one approved starter automation** designed to prove one measurable result.
- Final pricing is quote-based and depends on the automations, setup, usage, and support required.

Rules:

- Diagnose the business problem before quoting.
- Build each quote from named automation line items, not a generic tier.
- State the total monthly price clearly; **$99/month is the starting point, not a universal price or guarantee**.
- Quote any one-time setup fee separately based on the actual implementation required.
- A starter trial must use an approved template, target launch within **1–3 business days after Ready-to-Build**, require no more than **four hours of Tony's hands-on setup time**, and include one revision round.
- Eligible starters include missed-call text-back, booking confirmations/reminders, basic form or chat follow-up, review requests, one simple lead-follow-up sequence, or one basic pipeline.
- AI voice, custom integrations/APIs, accounting/estimate/payment connections, data cleanup/imports, custom websites or landing pages, multiple locations/calendars/departments, complex routing, and full community-platform implementations require a paid setup project and separate delivery schedule.
- Initial capacity is capped at **four live trials** and **two new trial launches per week** unless Tony approves a written exception.
- The quote must define trial scope, trial start trigger, trial end date, post-trial price, included usage, client responsibilities, and exclusions.
- No recurring charge may begin during the free trial unless the client separately and expressly authorizes it in writing.
- No credit card may be required as a condition of starting the advertised trial.
- Quote all prices in the approved currency and identify applicable taxes.
- The client-approved quote or signed order form controls final scope and price.
- Associates may present the starting price and approved automation catalogue but may not invent prices.
- Any discount must include an approver, reason, expiry date, and value received in return.

### Quote Line-Item Standard

Each selected automation must identify:

1. Automation name.
2. Business problem and desired outcome.
3. Trigger and actions.
4. Included channels and integrations.
5. Setup requirements and dependencies.
6. Included usage or volume assumption.
7. Monthly price allocation or bundled quote treatment.
8. One-time setup charge, if any.
9. Trial inclusion and success measure.
10. Explicit exclusions.
11. Trial path: **Starter Trial Eligible** or **Paid Implementation Required**.
12. Launch-slot availability and the one-revision limit when a starter trial is offered.

## 5. Systems of Record

1APP must contain:

- Contact record.
- Business record.
- Opportunity and pipeline stage.
- Lead source and campaign.
- Owner and assigned associate.
- Quote ID/version, selected automations, setup fee, recurring amount, trial dates, and billing cadence.
- Discovery notes and problem statement.
- Decision-maker and target launch date.
- Next action and due date.
- Handoff form.
- Onboarding status.
- Support history.
- Renewal, cancellation, and commission records.

## Standard Opportunity Stages

1. **New Lead**
2. **Contacted**
3. **Free Quote/Demo Booked**
4. **Automation Audit Completed**
5. **Custom Quote Sent**
6. **Quote Accepted — Trial Setup**
7. **Trial Live**
8. **Trial Review / Conversion**
9. **Won — Paid Active**
10. **Lost / Trial Ended**

Contact rules:

- Search before creating.
- Use update-or-create behaviour to prevent duplicate records.
- Use email and phone as primary matching fields.
- Never overwrite verified client data with lower-quality imported data.
- Record consent, communication preferences, and opt-outs.

---

# SOP-01 — Lead Capture and Assignment

**Owner:** Sales  
**Trigger:** A lead enters through a form, call, referral, campaign, social message, event, or manual prospecting.  
**Internal target:** Inbound leads acknowledged within 5 minutes during business hours; all other leads within one business day.

## Procedure

1. Search 1APP for an existing contact and business.
2. Update the existing record or create one clean record.
3. Record lead source, campaign, referrer, niche, location, and date received.
4. Assign one owner. Never allow shared ownership without a named primary owner.
5. Apply the correct tags.
6. Create an opportunity in **New Lead**.
7. Create the first follow-up task with a due date.
8. Send the approved acknowledgement when consent and channel rules permit.
9. If an associate sourced the lead, record the associate before the first sales meeting.

## Completion Standard

- One deduplicated contact.
- One opportunity.
- Source, owner, and next action recorded.
- First response sent or attempted.

## Escalate When

- Two associates claim the same lead.
- The lead requests a custom feature before discovery.
- The lead is outside the approved geography or niche.

---

# SOP-02 — Lead Qualification

**Owner:** Justin or assigned sales associate  
**Trigger:** Two-way contact with a prospect.  
**Goal:** Decide whether to book an audit/demo, nurture, or disqualify.

## Qualification Questions

1. How do new leads currently contact the business?
2. What happens when a call is missed?
3. How quickly does the business respond to new leads?
4. How are appointments, estimates, reminders, and follow-ups handled?
5. Where are leads or admin tasks falling through the cracks?
6. What is that costing in lost jobs, time, or customer experience?
7. Who decides on a system like this?
8. What needs to change, and by when?
9. Is the business willing to review a custom quote, with service starting as low as $99 per month after the trial?

## Qualified Lead Standard

A qualified lead has:

- A real operating business.
- A measurable lead, follow-up, booking, review, payment, or admin problem.
- A decision-maker involved or accessible.
- Willingness to review and approve a custom quote and evaluate the solution through the 14-day trial.
- A reason to act within 90 days.
- A use case 1APP can deliver reliably.

## Disqualify or Nurture When

- The prospect wants guaranteed leads or revenue.
- The business has no active customers or ability to pay.
- The request is primarily custom software development.
- The prospect refuses to identify a business problem.
- The required outcome is outside 1APP's approved capabilities.

## Completion Standard

- Opportunity moves to **Contacted**.
- Qualification fields are complete.
- Audit/demo is booked, a nurture date is set, or a loss reason is recorded.

---

# SOP-03 — Audit and Demo

**Owner:** Justin; Tony joins for technical risk or custom scope  
**Trigger:** Qualified meeting booked.  
**Standard length:** 15–30 minutes.

## Before the Meeting

1. Review the website, reviews, lead sources, services, and locations.
2. Confirm the decision-maker is invited.
3. Prepare one likely leak and one relevant 1APP workflow.
4. Open the opportunity record before the meeting.

## Meeting Flow

1. **Set the contract:** Confirm time, agenda, and that either side can say no.
2. **Current state:** Map lead intake, missed calls, booking, estimates, follow-up, reviews, and payments.
3. **Implication:** Quantify lost opportunities and wasted owner/admin time.
4. **Future state:** Confirm what success must look like.
5. **Demonstrate:** Show only the 1APP features tied to those problems.
6. **Recommend:** Select the smallest useful automation set and explain why each item is included.
7. **Advance:** Agree on a dated next step.

## Demo Rules

- Never feature-dump.
- Never show another client's data.
- Never guarantee performance.
- Never promise an integration or timeline without Tony's approval.
- Record exact client language for the custom quote.

## Completion Standard

- Opportunity moves to **Free Quote/Demo Booked**, then **Automation Audit Completed** after attendance.
- Pain, impact, decision process, recommended automations, objections, and next action are recorded.

---

# SOP-04 — Custom Quote, Scope, and Close

**Owner:** Justin  
**Trigger:** Demo completed with confirmed fit.  
**Internal target:** Standard custom quote sent within one business day.

## Procedure

1. Restate the client's current problem in their own language.
2. Define the desired business outcome.
3. Recommend the smallest automation set that solves the priority problem.
4. List every automation as a named line item with outcome, scope, and exclusion.
5. Show the total monthly price, any setup fee, taxes, and the price that begins after the trial.
6. State the 14-day starter-trial scope, eligibility, start trigger, end date, success measure, one-revision limit, and no-credit-card requirement.
7. State client responsibilities and required access.
8. Use only approved terms, timelines, and claims.
9. Define the next step: quote approval and trial onboarding.
10. Record objections and a dated follow-up.

## Standard Closing Rule

Do not ask, “What do you think?” Ask:

> Based on the problems we mapped, I recommend testing [one approved starter automation] during the 14-day free trial. The trial begins after it is live and tested, requires no credit card, and measures [success measure]. The full paid solution is [price] per month after written continuation approval, with [setup fee or “no setup fee”] clearly listed. Advanced or custom work is quoted separately. Is there anything specific preventing us from approving the starter-trial scope and beginning onboarding?

## Exceptions

- No discount without joint approval.
- No free custom work.
- No launch date is final until Tony completes the handoff review.
- Any custom request requires a change request or separate statement of work.

## Completion Standard

- Opportunity moves to **Custom Quote Sent**.
- A trial moves forward only after the quote and trial scope are accepted in writing.
- A paid win is recorded only after the client converts and the first required payment clears.
- Lost opportunities require a structured loss reason and future follow-up date when appropriate.

---

# SOP-05 — Quote Acceptance, Trial Activation, and Paid Conversion

**Owner:** Justin for commercial confirmation; Tony for fulfillment release  
**Trigger:** Prospect accepts the custom quote and 14-day trial scope.

## Trial Activation Procedure

1. Confirm written acceptance of the quote, trial scope, post-trial monthly price, and any separately quoted setup work.
2. Verify selected automations, quote version, taxes, trial dates, success measures, and sales attribution.
3. Confirm the trial path is marked **Starter Trial Eligible** or **Paid Implementation Required**.
4. For a starter trial, verify one approved template, one measurable result, a 1–3-business-day target after Ready-to-Build, no more than four hours of Tony's hands-on setup time, one revision round, and an available launch slot.
5. For advanced/custom work, approve the paid setup project and separate delivery schedule before work begins.
6. Confirm that no credit card is required to start the advertised starter trial.
7. Move the opportunity to **Quote Accepted — Trial Setup**.
8. Create the onboarding opportunity in **Trial / Form Sent**.
9. Send the client welcome message and onboarding form.
10. Create the sales-to-fulfillment handoff task.
11. Do not start fulfillment until the handoff passes review.
12. Start the 14-day trial clock only when Tony confirms the approved starter automation is live, tested, and usable—not when the quote is accepted, access is provided, or the job enters the queue.

## Paid Conversion Procedure

1. Review agreed success measures with the client before the trial ends.
2. Obtain written confirmation that the client wants to continue.
3. Collect recurring billing authorization through the approved secure process.
4. Confirm the quoted monthly amount, taxes, billing date, and any setup balance.
5. Verify the first required payment clears.
6. Move the sales opportunity to **Won — Paid Active**.
7. Update the client record from Trial to Active.

## Completion Standard

- Accepted quote and trial scope attached.
- Trial start and end dates recorded.
- Handoff form issued and accepted.
- Paid conversion is recorded only after authorization and cleared payment.

---

# SOP-06 — Sales-to-Fulfillment Handoff

**Owner:** Justin completes; Tony accepts or rejects  
**Trigger:** Custom quote and trial scope accepted in writing.  
**Internal target:** Sales submits within two business hours; fulfillment reviews within one business day.

## Required Handoff Fields

- Client and business contact information.
- Decision-maker and day-to-day contact.
- Quote ID/version, selected automations, setup fee, post-trial recurring fee, billing cadence, and taxes.
- Trial scope, success measures, start trigger, and end date.
- Exact problem being solved.
- Agreed deliverables and exclusions.
- Services, locations, hours, and emergency rules.
- Required phone, calendar, CRM, AI, reputation, payment, and website components.
- Existing data and systems to be imported or connected.
- Promises made during sales.
- Target launch date and reason.
- Associate attribution and commission status.
- Open questions and known risks.

## Acceptance Test

Tony marks the handoff:

- **Accepted:** Complete and deliverable.
- **Returned:** Missing required information.
- **Scope Review:** Custom work, unclear promise, or technical risk.

No setup begins while the handoff is Returned or in Scope Review.

---

# SOP-07 — Client Onboarding Intake

**Owner:** Onboarding coordinator; Tony accountable  
**Trigger:** Welcome message and onboarding form sent.  
**Internal target:** Follow up after two business days if incomplete.

## Procedure

1. Send the secure onboarding form.
2. Collect business identity, contacts, hours, services, service areas, booking rules, escalation rules, branding, review link, and approved messaging.
3. Collect only information required for setup.
4. Use secure access-sharing methods. Never request passwords by email, text, chat, or notes.
5. Review the form for contradictions or missing safety rules.
6. Conduct a short clarification call only when needed.
7. Move onboarding to **Info Review** or **Needs Client Info**.

## Completion Standard

- All required fields complete.
- Client approvals recorded.
- Brand assets received.
- Access dependencies available.
- Risks and missing items resolved.

---

# SOP-08 — 1APP Account Provisioning

**Owner:** Tony or implementation specialist  
**Trigger:** Handoff accepted and onboarding intake complete.

## Procedure

1. Create the client account using the approved naming convention.
2. Apply the closest approved industry template.
3. Set business name, legal name, address, timezone, currency, locale, and contact details.
4. Create users using named accounts only.
5. Assign least-privilege permissions.
6. Enable only the automations and supporting features included in the accepted quote.
7. Record the template version and setup date.
8. Create one designated test contact clearly labelled **1APP TEST — DO NOT MARKET**.
9. Move onboarding to **1APP Setup**.

## Naming Standard

- Account: `[Legal Business Name]`
- Calendar: `[Business Name] — [Appointment Type]`
- Workflow: `[CLIENT] — [FUNCTION] — v#`
- Campaign: `[CLIENT] — [AUDIENCE] — [PURPOSE] — YYYY-MM`
- Test contact: `1APP TEST — [Business Name]`

## Completion Standard

- Account settings verified.
- Correct quoted automation scope enabled.
- Users and permissions documented.
- Template version recorded.

---

# SOP-09 — Configuration by Quoted Automation

**Owner:** Implementation specialist; Tony accountable  
**Trigger:** Account provisioned.

Configure only the named automations and supporting components included in the accepted quote. Available automation categories include:

- Missed-call text-back.
- AI voice agent.
- Appointment booking, confirmations, and reminders.
- CRM and lead pipeline.
- Two-way text, email, and approved messaging channels.
- Google review automation.
- Lead nurture and follow-up sequences.
- Invoice, payment reminder, and text-to-pay workflows.
- Email marketing and re-engagement.
- Website and landing-page lead capture.
- Social media planning.
- Reporting and analytics.

For every quoted automation, document:

1. Trigger.
2. Actions and timing.
3. Entry and stop conditions.
4. Required data and access.
5. Human owner and escalation path.
6. Success measure for the 14-day trial.
7. Usage assumption.
8. Test cases and rollback method.

## Configuration Rules

- Every workflow needs a trigger, goal, stop condition, owner, and rollback method.
- AI agents need approved purpose, tone, knowledge, booking rules, escalation rules, prohibited claims, and human handoff.
- Calendars need timezone, availability, duration, buffers, assignment, confirmations, rescheduling, and cancellation rules.
- Payment features require written client authorization and a test transaction when practical.
- No dormant or unused features are activated “just in case.”

---

# SOP-10 — Data Import and Migration

**Owner:** Tony or implementation specialist  
**Trigger:** Client supplies data for import.

## Procedure

1. Obtain written authorization and confirm data ownership.
2. Create an encrypted working copy in the approved client folder.
3. Map source fields to 1APP fields.
4. Normalize phone numbers, emails, names, tags, and consent status.
5. Remove obvious duplicates without destroying the source file.
6. Import a small test batch.
7. Verify matching, ownership, tags, and workflow exclusions.
8. Import the approved full batch.
9. Reconcile source count, imported count, rejected count, and duplicate count.
10. Store an import report and securely dispose of temporary copies when no longer required.

## Hard Rules

- Imported contacts do not enter marketing workflows by default.
- Consent and opt-out status must be preserved.
- Never import sensitive payment credentials or passwords.
- Never delete the client's source data.

---

# SOP-11 — Quality Assurance and Launch Approval

**Owner:** Tester completes; Tony approves  
**Trigger:** Configuration marked ready for testing.

## Required Tests

1. User login and permissions.
2. Inbound call routing.
3. Missed-call text-back.
4. Two-way text and email.
5. Web form and chat lead creation.
6. Contact deduplication.
7. Pipeline creation and stage movement.
8. Calendar availability and timezone.
9. Booking, confirmation, reminder, reschedule, and cancellation.
10. AI greeting, knowledge, qualification, booking, human transfer, prohibited claims, and failure behaviour.
11. Review request timing and stop conditions.
12. Payment or invoice workflow when included.
13. Opt-out keywords and suppression.
14. Internal alerts and task creation.
15. Mobile app login and core client actions.

## Defect Levels

- **Blocker:** Wrong recipient, privacy/security issue, payment error, broken opt-out, incorrect AI safety response, or core workflow failure. Launch stops.
- **Major:** A purchased feature does not work reliably. Fix before launch.
- **Minor:** Cosmetic or low-impact issue. May launch only with Tony's approval and a dated fix task.

## Completion Standard

- Every required test has evidence and a pass/fail result.
- Blockers and major defects are zero.
- Rollback plan is documented.
- Tony signs launch approval.

---

# SOP-12 — Client Training and Go-Live

**Owner:** Tony or assigned trainer  
**Trigger:** QA approved.

## Procedure

1. Schedule a 30–45 minute launch session.
2. Confirm administrator and day-to-day users.
3. Teach only the actions required in week one:
   - Log in.
   - View and respond to conversations.
   - Manage opportunities.
   - View and manage appointments.
   - Pause or escalate automation.
   - Get support.
4. Review what 1APP automates and what remains the client's responsibility.
5. Run one live acceptance test with the client.
6. Obtain written go-live approval.
7. Enable live workflows in a controlled sequence.
8. Monitor for at least one business day.
9. Send launch confirmation, training link, support process, and next check-in date.
10. Move onboarding to **Launched**.

## Completion Standard

- Client can complete the five week-one actions.
- Acceptance test passed.
- Approval recorded.
- Monitoring owner assigned.

---

# SOP-13 — Post-Launch Success

**Owner:** Customer success; Tony handles technical escalation  
**Trigger:** Client goes live.

## Cadence

- **Day 1:** Verify messages, calls, bookings, and alerts.
- **Day 7:** Adoption and issue check.
- **Day 14:** Review early results and adjust configuration.
- **Day 30:** First value review.
- **Monthly:** Automated performance summary and health review.
- **Quarterly:** Business review for clients with multiple automations, material recurring revenue, or elevated risk.

## 14-Day Starter-Trial Cadence

- **Day 1:** Confirm the automation is live and start the official trial clock.
- **Day 3:** Confirm the client has seen the first value event or resolve activation blockers.
- **Day 7:** Adoption and issue review.
- **Day 10:** Schedule the conversion review, summarize value evidence, and restate the approved post-trial quote.
- **Day 12:** Confirm continue, modify through a paid change request, or end decision.
- **Day 14:** Convert to paid active after written authorization and cleared required payment, or complete trial offboarding.

## First Value Metrics

Use metrics relevant to the signed outcome:

- Missed calls answered by text.
- Lead response time.
- Leads captured.
- Appointments booked.
- No-shows reduced.
- Follow-up attempts completed.
- Reviews requested and received.
- Estimates or invoices followed up.
- Owner/admin hours saved.

Do not claim causation unless the data supports it.

## Health Status

- **Green:** Active use, stable workflows, desired result visible, bills current.
- **Yellow:** Low adoption, unresolved issue, missed check-in, or weak results.
- **Red:** Core failure, cancellation risk, payment failure, security concern, or client escalation.

---

# SOP-14 — Support Ticket Management

**Owner:** Support specialist; Tony is technical escalation  
**Trigger:** Client requests help or monitoring detects an issue.

## Ticket Priorities

| Priority | Definition | Internal acknowledgement target |
|---|---|---:|
| P1 | Security/privacy risk, service unavailable, messages sent incorrectly, or payment-impacting failure | 1 hour during business hours |
| P2 | Purchased core feature materially impaired with no reasonable workaround | 4 business hours |
| P3 | Normal defect or configuration question | 1 business day |
| P4 | Training request, enhancement, or low-impact change | 2 business days |

These are internal operating targets, not contractual promises unless included in the signed agreement.

## Procedure

1. Create a ticket for every request.
2. Record client, issue, impact, start time, screenshots, and reproduction steps.
3. Assign priority based on impact, not emotion.
4. Acknowledge and provide the next update time.
5. Reproduce safely using test data.
6. Apply the smallest controlled fix.
7. Test the fix and affected workflows.
8. Explain the resolution in plain language.
9. Record root cause and prevention action.
10. Close only after client confirmation or documented validation.

## Escalation

- P1 goes directly to Tony.
- Billing, refund, or contract disputes go to Tony and Justin.
- Feature requests are not treated as defects.
- Repeated issues require a problem record and permanent corrective action.

---

# SOP-15 — Change Requests and Scope Control

**Owner:** Tony assesses; Justin prices and closes  
**Trigger:** Client asks for work outside the signed scope.

## Procedure

1. Record the request without promising delivery.
2. Clarify desired outcome, urgency, users, systems, and success criteria.
3. Classify:
   - Included configuration.
   - Paid add-on.
   - Custom project.
   - Product request.
   - Unsupported request.
4. Tony estimates technical risk, effort, testing, and support impact.
5. Justin prepares price and terms.
6. Obtain written approval and payment when required.
7. Schedule work and define acceptance criteria.
8. Build, test, document, release, and update the client record.

## Hard Rule

“It will only take five minutes” is not approval to perform free out-of-scope work.

---

# SOP-16 — Billing, Failed Payments, and Collections

**Owner:** Finance/commercial owner  
**Trigger:** Invoice issued, recurring charge due, or payment fails.

## Procedure

1. Reconcile active clients, accepted quotes, selected automations, recurring charges, taxes, discounts, and commissions monthly.
2. Do not charge recurring fees during the advertised 14-day free trial without separate, express written authorization.
3. Do not require a credit card to start the advertised trial.
4. Issue invoices and receipts through approved 1APP billing processes.
5. On failed payment, notify the client promptly and provide a secure update-payment path.
6. Retry and follow up according to the signed agreement and approved billing schedule.
7. Escalate unresolved payment to Justin.
8. Restrict or suspend service only when authorized by the signed terms and after written notice.
9. Restore service only after payment status is verified.
10. Record all credits, refunds, write-offs, and reasons.

## Commission Control

- Pay commission only on collected, cleared revenue.
- Use the signed associate agreement in force on the deal date.
- Reverse commission on refunds or chargebacks when the agreement permits.
- Reconcile lead attribution before payout.
- Preserve a payout ledger and approval record.

---

# SOP-17 — Cancellation and Offboarding

**Owner:** Justin owns commercial conversation; Tony owns technical offboarding  
**Trigger:** Client requests cancellation or 1APP terminates under signed terms.

## Save Attempt

1. Acknowledge without arguing.
2. Identify the root cause: results, adoption, service, price, business closure, or competitor.
3. Review usage, outcomes, unresolved issues, and contract terms.
4. Offer a fix only when it addresses the real problem.
5. Do not offer discounts automatically.

## Offboarding Procedure

1. Confirm effective date, final charges, and data-export terms in writing.
2. Disable new marketing and automation at the agreed time.
3. Export client-owned data covered by the agreement.
4. Revoke users, connected services, credentials, and phone/payment access as applicable.
5. Archive the configuration and support history according to retention rules.
6. Record cancellation reason and competitive destination.
7. Calculate final commission adjustments.
8. Confirm completion to the client.

## Completion Standard

- No active automation remains after the authorized cutoff.
- Access is revoked.
- Data handling is documented.
- Billing and commission records are reconciled.

---

# SOP-18 — Security, Privacy, and Access

**Owner:** Tony  
**Trigger:** New user, client setup, integration, incident, role change, or offboarding.

## Rules

1. Require multi-factor authentication wherever supported.
2. Use named accounts; never share administrator logins.
3. Store credentials only in an approved protected credential system.
4. Never place passwords, API keys, recovery codes, or payment credentials in chat, email, forms, tickets, or SOPs.
5. Apply least-privilege access.
6. Review administrator access monthly.
7. Remove access immediately when a person leaves or changes role.
8. Use test data for QA whenever possible.
9. Collect and retain only necessary client information.
10. Record suspected security or privacy incidents immediately.

## Incident First Response

1. Stop further exposure without destroying evidence.
2. Notify Tony immediately.
3. Record what happened, when, systems affected, and people affected.
4. Revoke or rotate affected access through approved secure processes.
5. Preserve logs.
6. Assess notification and legal obligations with qualified counsel when required.
7. Document corrective action before closure.

---

# SOP-19 — Workflow Change Management

**Owner:** Tony  
**Trigger:** Any change to a live workflow, AI agent, calendar, phone route, payment flow, or integration.

## Procedure

1. Create a change record with reason, owner, risk, affected clients, and desired result.
2. Capture the current version and rollback method.
3. Build or edit outside the live path when possible.
4. Test normal, error, duplicate, opt-out, and edge-case behaviour.
5. Obtain approval based on risk.
6. Release during a monitored window.
7. Verify live behaviour.
8. Roll back immediately if a blocker appears.
9. Update the version number, documentation, and client record.

## Approval Levels

- Low-risk copy or timing change: Implementation owner plus peer check.
- Workflow logic or routing change: Tony approval.
- Billing, AI safety, privacy, or multi-client template change: Tony approval plus documented business review.

---

# SOP-20 — Associate Onboarding and Governance

**Owner:** Justin; Tony certifies technical competence where required  
**Trigger:** New referral associate, sales associate, or certified partner.

## Procedure

1. Confirm the correct signed associate agreement.
2. Verify identity, payment details, tax responsibility acknowledgement, and contact information through approved processes.
3. Provide approved brand, offer, pricing, and messaging materials.
4. Train on ICP, qualification, CRM stages, claims, scope, and handoff.
5. Require role-play and a passing score before independent demos.
6. Restrict access according to level.
7. Review the first three opportunities and first three calls.
8. Track lead attribution, pipeline hygiene, complaints, and conversion.
9. Review standing monthly.

## Immediate Violations

- Unauthorized discounts.
- False or guaranteed claims.
- Misrepresentation of ownership or employment.
- Unapproved use of brand assets.
- Hidden lead activity outside 1APP.
- Mishandling client data or credentials.
- Circumventing lead ownership or commission rules.

Serious violations trigger immediate suspension pending review.

---

# SOP-21 — Weekly Operating Rhythm

## Monday — Pipeline and Capacity

Owners: Tony and Justin

- Review every opportunity without a next action.
- Review demos this week and custom quotes outstanding.
- Review accepted trials, paid conversions, and launch capacity.
- Review onboarding blockers and client dependencies.
- Confirm one weekly revenue target and one delivery target.

## Wednesday — Fulfillment and Risk

- Review every client in Needs Client Info, 1APP Setup, Testing, and Launched.
- Review open P1/P2 tickets.
- Review changes scheduled for release.
- Review capacity for the next ten business days.

## Friday — Numbers and Learning

- Leads created and contacted.
- Audits booked, attended, and completed.
- Custom quotes, trials started, paid conversions, losses, setup revenue, and new recurring revenue.
- Time from quote acceptance to accepted handoff.
- Time from accepted handoff to trial go-live.
- QA defects and support volume.
- At-risk clients, churn, referrals, and expansion.
- One process failure and one improvement action.

---

# SOP-22 — Monthly Management Review

**Owners:** Tony and Justin

Review:

1. New recurring revenue, total recurring revenue, setup revenue, churned revenue, and collected cash.
2. Pipeline conversion by stage and source.
3. Acquisition cost and payback by channel.
4. Trial activation rate, trial-to-paid conversion, and trial losses by reason.
5. Average time to launch and hours per implementation.
6. Support tickets per client and top root causes.
7. Client health distribution.
8. Gross margin by automation and quote size.
9. Associate production, quality, and payout accuracy.
10. Template defects and requested improvements.
11. Decisions, owners, and due dates.

## Core Targets to Establish After 90 Days of Data

- Speed to lead.
- Qualified lead rate.
- Demo show rate.
- Demo-to-quote rate.
- Quote acceptance rate.
- Trial activation rate.
- Trial-to-paid conversion rate.
- Average setup revenue.
- New recurring revenue per month.
- Median days to launch.
- QA first-pass rate.
- Support tickets per client.
- 30-day activation rate.
- Gross revenue retention.
- Referral rate.

Do not invent benchmarks before enough 1APP data exists. Establish the baseline, then improve it monthly.

---

## Open Decisions Requiring Tony and Justin

These items were inconsistent or not finalized across existing 1APP documents and should be resolved before this manual becomes contractual:

1. Approved internal price-building method for each automation and bundle combination.
2. Final setup-fee rules and whether setup fees are waived, deferred, or payable for trial clients.
3. What happens by default at trial expiry if the client does not respond.
4. Refund window and cancellation notice after paid conversion.
5. Service suspension timeline after failed payment.
6. Included usage allowances and overage handling.
7. Support business hours and any contractual response targets.
8. Data retention and export period after trial or paid cancellation.
9. The Level 1 referral bonus summary, which conflicts in an older associate document.
10. How associate commission is calculated on custom automation quotes.
11. Final commission approval and payout date each month.

## Version History

| Version | Date | Change | Approved by |
|---|---|---|---|
| 1.0 | 2026-09-09 | Initial consolidated SOP system | Pending Tony/Justin review |
| 1.1 | 2026-09-09 | Replaced fixed tiers with custom per-automation quotes starting at $99/month and added the 14-day no-credit-card trial process | Pending Tony/Justin review |
| 1.2 | 2026-09-22 | Limited the free trial to one approved starter automation; added eligibility, delivery, capacity, revision, paid-project, and trial-start rules | Pending Tony/Justin review |
