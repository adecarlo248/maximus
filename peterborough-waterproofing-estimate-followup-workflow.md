# 1APP Estimate and Quote Follow-Up System

Version 2.0 — September 14, 2026

## Operating decision

- **QuickBooks Online:** estimate/quote and accounting source of truth.
- **Make:** detects the event, prevents duplicates, maps data, and passes it to 1APP.
- **1APP:** owns SMS, email, pipeline, reply handling, timing, tasks, and stop logic.

Build the pattern once, then deploy separate copies for Peterborough Waterproofing and 1APP. Separate Make scenarios and 1APP workflows prevent cross-company routing mistakes.

## Conversion action by business

### Peterborough Waterproofing

- Immediate CTA: review the estimate and pay the job-specific deposit when ready.
- 48-hour CTA: reply with questions or pay the deposit to book the job.
- Stop when the client replies, pays, books, accepts, declines, or is marked won/lost.

### 1APP

- Immediate CTA: review/approve the custom quote and schedule the 30-day free-trial kickoff.
- 48-hour CTA: reply with questions or approve the quote to start the trial.
- Do **not** request a deposit or credit card before the trial; that contradicts the current 1APP offer.
- Stop when the prospect replies, approves, starts the trial, declines, or is marked won/lost.

## Shared 1APP fields

1. `External Estimate ID`
2. `Estimate Number`
3. `Estimate Amount`
4. `Estimate URL`
5. `Conversion URL`
6. `Estimate Sent At`
7. `Estimate Source`
8. `Follow-Up Status`
9. `Deposit Paid At`
10. `Quote Approved At`

`Conversion URL` is the unique deposit-payment URL for Peterborough Waterproofing and the quote-approval/trial-start URL for 1APP.

## Pipelines

### Peterborough Waterproofing — Jobs

1. New Lead
2. Inspection Booked
3. Inspection Completed
4. Estimate Sent
5. Deposit Paid / Job Booked
6. Won
7. Lost / Declined

### 1APP — Sales

1. Qualified Lead
2. Demo Completed
3. Quote Sent
4. Quote Approved
5. Trial Setup
6. Trial Live
7. Paid Active
8. Lost / Declined

## Make scenario A — estimate or quote sent

Create one copy per QuickBooks company.

1. Watch QuickBooks estimates every five minutes.
2. Continue only when the estimate email status is `sent` and a phone or email exists.
3. Check a Make Data Store key: `{business}:{estimate_id}:sent`. Stop if it already exists.
4. Normalize the email and phone.
5. Map name, estimate ID/number, amount, sent date, estimate URL, and conversion URL.
6. Upsert the contact in the correct 1APP account, matching email first and normalized phone second.
7. Create or update one opportunity keyed to the QuickBooks estimate ID.
8. Set the value and move it to `Estimate Sent` or `Quote Sent`.
9. Write the shared custom fields.
10. Start the correct 1APP workflow.
11. Write the Data Store key only after 1APP succeeds.
12. Retry transient errors and alert Tony after the final failed attempt.

## Make scenario B — payment, acceptance, or trial status

### Peterborough Waterproofing

When the job-specific deposit is paid:

- Set `Deposit Paid At` and follow-up status `deposit_paid`.
- Move the opportunity to `Deposit Paid / Job Booked`.
- Remove the contact from estimate follow-up.
- Notify the owner to schedule or confirm the job.

### 1APP

When the quote is approved or trial is activated:

- Set `Quote Approved At` and status `quote_approved` or `trial_started`.
- Move the opportunity to `Quote Approved`, `Trial Setup`, or `Trial Live`.
- Remove the contact from quote follow-up.
- Create the onboarding task.

## 1APP workflow sequence

1. Trigger when the opportunity enters `Estimate Sent` or `Quote Sent`.
2. Confirm a valid channel and non-empty `Conversion URL`.
3. Send immediate SMS where mobile consent is valid.
4. Send immediate email where an email is valid.
5. Create an owner task: `Estimate/quote sent — monitor replies`.
6. Wait 48 hours.
7. Evaluate every stop condition.
8. If still open, send the 48-hour SMS and email.
9. Create a manual follow-up task for the next business day.
10. Mark status `48h_sent` and end.

Allow re-entry because one customer can receive multiple estimates, but use the external estimate ID and Make Data Store to prevent duplicate sends from repeated QuickBooks updates.

## Stop conditions

Remove the contact before any delayed message when:

- The customer replies by SMS or email.
- Deposit is paid, quote is approved, or trial starts.
- Job, appointment, or kickoff is booked.
- Opportunity becomes won, lost, declined, or cancelled.
- Owner applies `manual_takeover`.
- Contact opts out or lacks channel consent.

On reply, notify the owner and create an immediate task. Automated sales messages should stop once a human conversation begins.

## Peterborough Waterproofing copy

### Immediate SMS

Hi {{contact.first_name}}, your estimate from Peterborough Waterproofing has been sent. If you have any questions, just reply here — we look forward to working with you. When you're ready to book, you can pay your deposit here: {{contact.conversion_url}}

### Immediate email

**Subject:** Your Peterborough Waterproofing estimate

Hi {{contact.first_name}},

Your estimate has been sent. If you have any questions, reply to this email and we'll be happy to help.

When you're ready to book the work, you can pay your deposit here:
{{contact.conversion_url}}

We look forward to working with you.

Peterborough Waterproofing

### 48-hour SMS

Hi {{contact.first_name}}, we're following up on your Peterborough Waterproofing estimate. Is there anything we can clarify to help get your job booked? When you're ready, you can pay the deposit here: {{contact.conversion_url}}

### 48-hour email

**Subject:** Any questions about your estimate?

Hi {{contact.first_name}},

We're following up on the estimate we sent. Is there anything we can clarify or do to help get your project booked?

When you're ready, you can pay the deposit here:
{{contact.conversion_url}}

Just reply to this email if you'd like to discuss the work.

Peterborough Waterproofing

## 1APP copy

### Immediate SMS

Hi {{contact.first_name}}, your custom 1APP quote has been sent. If you have any questions, just reply here. When you're ready, approve your quote here and we'll schedule your 30-day free-trial kickoff: {{contact.conversion_url}}

### Immediate email

**Subject:** Your custom 1APP quote

Hi {{contact.first_name}},

Your custom 1APP quote has been sent. If you have questions about the recommended automations, reply to this email and we'll walk through them with you.

When you're ready, approve the quote here and we'll schedule your 30-day free-trial kickoff:
{{contact.conversion_url}}

No credit card is required to begin the trial.

1APP

### 48-hour SMS

Hi {{contact.first_name}}, I'm following up on your 1APP quote. Is there anything we can clarify to help you move forward? You can approve it and start the 30-day free trial here: {{contact.conversion_url}}

### 48-hour email

**Subject:** Any questions about your 1APP quote?

Hi {{contact.first_name}},

I'm following up on the custom quote we sent. Is there anything we can clarify about the recommended automations or rollout?

When you're ready, approve the quote here and we'll schedule your 30-day free-trial kickoff:
{{contact.conversion_url}}

No credit card is required to begin the trial.

1APP

## Deposit-link rule

Use a unique, job-specific payment link whenever possible. A generic link makes reconciliation and stop logic unreliable.

If QuickBooks cannot provide a stable deposit-payment URL when the estimate is sent, do not create an unpaid deposit invoice for every unaccepted estimate solely to obtain a link. Use this staged process:

1. Immediate and 48-hour messages link to estimate acceptance.
2. Acceptance creates the deposit invoice.
3. The client immediately receives the unique invoice/payment link.
4. Payment moves the opportunity to `Deposit Paid / Job Booked`.

## Test checklist

1. Estimate sent triggers exactly once.
2. Repeated QuickBooks updates do not restart the sequence.
3. SMS and email merge fields render correctly.
4. Missing phone skips SMS without failing email.
5. Missing email skips email without failing SMS.
6. Reply stops the 48-hour messages and alerts the owner.
7. Deposit payment stops Peterborough follow-up.
8. Quote approval or trial activation stops 1APP follow-up.
9. Booked, won, lost, cancelled, and opt-out states stop follow-up.
10. A second legitimate estimate for the same customer works independently.
11. Make failure alerts Tony and does not prematurely write the dedupe key.

## Weekly metrics

- Estimates/quotes sent.
- Delivery rate by channel.
- Reply rate.
- Conversion before 48 hours.
- Conversion after the 48-hour touch.
- Time to deposit paid or quote approved.
- Total value converted.
- Workflow failures and duplicate-prevention events.

## Build order

1. Confirm how Peterborough Waterproofing creates the deposit link.
2. Create the shared fields in both 1APP accounts.
3. Build and test the Peterborough workflow.
4. Build its two Make scenarios and prove deduplication.
5. Clone the workflow for 1APP and replace the conversion action/copy.
6. Build the 1APP Make scenario copies with the correct QuickBooks connection.
7. Test all stop conditions.
8. Publish Peterborough first and monitor for seven days.
9. Publish 1APP after the first deployment is stable.
