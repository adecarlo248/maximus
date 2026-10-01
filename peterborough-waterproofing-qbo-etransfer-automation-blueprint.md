# Peterborough Waterproofing — QBO e-Transfer Automation Blueprint

## Goal
Automatically turn incoming Interac/e-transfer confirmation emails into QuickBooks Online payments, then update GoHighLevel, while avoiding Stripe/card processing fees as the default payment path.

## System Roles
- **QuickBooks Online:** accounting source of truth; invoices and payment records live here.
- **Bank feed in QBO:** confirms money actually landed in the bank; downloaded bank transaction should match to the created payment/deposit, not be added again.
- **Email inbox:** receives bank/interac deposit confirmation emails.
- **Parseur:** extracts structured data from each email: sender, amount, memo, date, email source, transaction/reference ID if available.
- **Make.com:** matching and automation brain.
- **GoHighLevel:** mobile dashboard/notifications/workflows for owner and customer follow-up.

## Important Accounting Design Decision
Because the bank account is already linked to QBO, the automation should generally:

1. Create a **Receive Payment** in QBO against the correct open invoice.
2. Set **Deposit To Account** to the same linked bank account, or to an e-transfer clearing account depending on the bookkeeper's preference.
3. Let the downloaded bank feed transaction **MATCH** the payment/deposit.
4. Do **not** let the bank feed create a second income transaction.

### Recommended default
Use the linked bank account as the Deposit To account for one-to-one e-transfer deposits.

Why:
- E-transfers usually land as individual bank deposits.
- The QBO bank feed should then show a match instead of needing manual income entry.
- Cleaner than dumping everything into Uncategorized Income.

### If the bookkeeper prefers Undeposited Funds / Clearing
Use an **E-Transfer Clearing** account only if they want payments received first, then bank deposits matched/cleared later. This is more accounting-heavy and may require an extra deposit/matching step.

## What QuickBooks Must Have Ready
- Client's bank account connected to QBO.
- Customer records cleaned up enough to match names/emails.
- Invoices created in QBO with open balances.
- Payment method created: `E-Transfer`.
- Decide Deposit To account:
  - Preferred: linked bank account for individual e-transfer deposits.
  - Alternative: Undeposited Funds or E-Transfer Clearing.

## What Parseur Extracts
Create fields:
- `sender_name`
- `amount`
- `payment_date`
- `memo`
- `invoice_number` if present in memo/message
- `reference_id` / confirmation number if present
- `recipient_email`
- `source_email_subject`
- `source_email_id` if available

## Customer-Facing Invoice Instruction
Add this to every QBO/GHL invoice/payment email:

> Paying by e-Transfer? Send to [payment email] and include invoice #[InvoiceNumber] in the message field so your payment can be applied correctly.

This is the difference between 70–80% automation and 95%+ automation.

## Make.com Scenario — Main Flow

### Trigger
**Parseur — Watch Documents**
- Watches parsed e-transfer emails.
- Runs every 5–15 minutes.
- Limit: 10+ documents per run.

### Step 1 — Normalize Parsed Data
Use Make tools / set variables:
- Convert amount from `$1,234.56` to numeric `1234.56`.
- Trim sender name.
- Uppercase/normalize invoice number.
- Store Parseur document ID / email ID for duplicate protection.

### Step 2 — Duplicate Protection
Before touching QBO, check a log table/sheet/datastore for `reference_id` or email ID.

If already processed:
- Stop scenario.

If new:
- Continue.

Recommended log location:
- Make Data Store, Airtable, or Google Sheet.

Minimum log columns:
- timestamp
- source email ID / Parseur document ID
- reference ID
- sender
- amount
- invoice number
- QBO payment ID
- match status
- exception status

### Step 3 — Match Logic

#### Path A — Invoice number found
QBO query/search:
- Find open invoice where `DocNumber = invoice_number` and `Balance > 0`.

If found:
- Confirm amount equals invoice balance OR amount is less than balance for partial payment.
- Create payment linked to invoice.

If not found:
- Go exception path.

#### Path B — No invoice number
Search QBO customers by sender name.

Then search open invoices for likely match:
- Same customer + open balance equal to amount = strong match.
- Same customer + one open invoice + amount less than balance = possible partial payment.
- Multiple open invoices / amount mismatch = exception.

#### Path C — No customer match
Exception path.

### Step 4 — Create QBO Payment
Create a Payment / Receive Payment with:
- CustomerRef = invoice customer
- TotalAmt = parsed amount
- Payment date = parsed payment date
- PaymentMethodRef = E-Transfer
- DepositToAccountRef = chosen bank/clearing account
- PrivateNote = `Auto-created from e-transfer email. Sender: [sender]. Memo: [memo]. Ref: [reference_id].`
- Line.LinkedTxn:
  - TxnId = QBO invoice ID
  - TxnType = Invoice
  - Amount = parsed amount

Expected result:
- Invoice balance reduces or becomes paid.
- Bank feed deposit can match against this QBO payment/deposit.

### Step 5 — Log Success
Update log:
- status = auto_matched
- QBO payment ID
- QBO invoice number
- customer
- amount

### Step 6 — Update GHL
Find/update contact.

Update fields:
- Last Payment Date
- Last Payment Amount
- Payment Method = E-Transfer
- Last Paid Invoice #

Trigger workflow:
- Payment received confirmation
- Pipeline stage update
- Review request delay if final payment
- Internal owner notification

## Exception Flow
When no safe match exists, do not create a payment automatically.

Exception triggers when:
- No invoice number and multiple possible invoices.
- Amount doesn't match any open invoice.
- Sender cannot be matched to a QBO customer.
- QBO connection/auth error.
- Parseur field missing amount/date/sender.
- Duplicate reference suspicious.

### Exception Notification in GHL
Send to a dedicated GHL contact/thread:
`🚨 Payment Exceptions`

Message format:

```
⚠️ Unmatched e-Transfer
Amount: $450.00
From: John Smith
Memo: [blank]
Date: June 2, 2026 2:34 PM
Reason: No invoice number + multiple possible matches

Action needed: Review in QBO / GHL
```

For mobile-first owner:
- GHL app internal notification.
- Optional SMS backup if unresolved after 30 minutes.
- Tony also gets backend alert so he can monitor.

## Test Blueprint Before Client Go-Live

### Phase 1 — Sandbox/Controlled Test
Do this before touching real incoming payments.

1. Create/choose a test customer in QBO:
   - Name: `Test Etransfer Customer`
   - Email: your/test email.

2. Create test invoices:
   - Invoice `TEST-1001` for `$10.00`
   - Invoice `TEST-1002` for `$15.00`
   - Invoice `TEST-1003` for `$20.00`

3. Create a sample e-transfer email template by forwarding/copying an old real notification with sensitive info redacted, or use a fake test email with the same structure.

4. Send test email to Parseur.

5. Train Parseur fields:
   - Sender
   - Amount
   - Date
   - Memo
   - Invoice number
   - Reference ID

6. Confirm Parseur output is clean JSON/table data.

7. Run Make scenario manually once.

8. Verify in QBO:
   - Correct invoice marked paid or partially paid.
   - Payment method says E-Transfer.
   - Payment date correct.
   - Deposit To account correct.
   - Memo/note contains source email/reference.

9. Verify in GHL:
   - Contact updated.
   - Internal notification sent.
   - Receipt/review workflow starts only when expected.

10. Verify log table:
   - Processed payment recorded once.
   - QBO payment ID stored.

### Phase 2 — Matching Tests
Run these test cases:

#### Test 1 — Perfect match
Email memo includes `TEST-1001`, amount `$10.00`.
Expected:
- Auto-match.
- QBO invoice paid.
- GHL payment workflow fires.

#### Test 2 — Invoice number with partial payment
Memo includes `TEST-1003`, amount `$5.00`.
Expected:
- Payment applies to invoice.
- Invoice remains partially unpaid.
- GHL marks partial/deposit received, not final paid.

#### Test 3 — No invoice number, exact amount/customer match
Sender matches QBO customer, amount equals one open invoice.
Expected:
- Auto-match if only one safe candidate.

#### Test 4 — No invoice number, multiple possible invoices
Sender matches customer, multiple open invoices.
Expected:
- Exception notification.
- No QBO payment created automatically.

#### Test 5 — Amount mismatch
Invoice is `$500`, email says `$450` and not set as partial.
Expected:
- Exception or partial-payment rule, depending on agreed settings.

#### Test 6 — Unknown sender
Sender not in QBO.
Expected:
- Exception notification.
- No QBO payment created.

#### Test 7 — Duplicate email
Send same email twice.
Expected:
- Second run stops due to duplicate reference/email ID.
- No duplicate QBO payment.

#### Test 8 — Missing/unclear amount
Parseur fails amount field.
Expected:
- Exception.
- No QBO payment.

#### Test 9 — Bank feed match
After payment is created, when bank feed downloads the deposit, verify QBO offers a MATCH rather than Add.
Expected:
- No duplicate income.

### Phase 3 — Real Soft Launch
1. Turn on monitoring only for 2–3 real e-transfer emails.
2. Do not auto-create payments yet — log and notify only.
3. Compare automation's suggested match against what the client/bookkeeper would do manually.
4. If suggestions are correct, enable auto-create for invoice-number matches only.
5. After 1 week, enable safe no-invoice-number matching.
6. Keep exceptions manual forever unless confidence is high.

## Go-Live Rules
Start conservative:

Auto-create payment only when:
- Invoice number found and QBO invoice open.
- Amount equals balance or is clearly partial.
- Not duplicate.
- Required fields are present.

Send exception when:
- Anything is uncertain.

After 2–4 weeks:
- Add smarter rules for recurring customers.
- Add trusted aliases for sender names.
- Improve Parseur templates for bank email variations.

## Owner Explanation
"Your bank is already connected to QuickBooks, so the money is already showing up there. The problem is QuickBooks doesn't know which customer/invoice each e-transfer belongs to. This automation reads the e-transfer email, grabs the sender, amount, memo, and invoice number, then marks the right invoice paid in QuickBooks. When the bank feed brings in the deposit, QuickBooks can match it instead of you manually entering it. If the system isn't 100% sure, it flags it in your GHL app so you can confirm it in seconds."

## Tony's Backend Management Checklist
Daily first 2 weeks:
- Check Make scenario history.
- Check Parseur failed/low-confidence parses.
- Check QBO for duplicate deposits/payments.
- Check GHL exception thread.

Weekly ongoing:
- Auto-match rate.
- Number of exceptions.
- Failed runs/auth issues.
- Total payments processed.
- Time saved estimate.

## Pricing/Scope Note
This is separate scope from regular GHL AI voice/conversation/calendar automation because it touches accounting, bank transactions, and ongoing monitoring.

Suggested add-on:
- Setup: $1,500–$2,000
- Monthly management: $300–$350/month

Include:
- Parseur/Make setup and monitoring.
- Exception handling.
- Weekly reconciliation report.
- Template refinement.
- Support when QBO/Google/Outlook auth breaks.

## Red Flags / Things to Confirm Before Selling
- Does the bank e-transfer email include sender name, amount, memo, and reference ID consistently?
- Does the client invoice from QBO, GHL, or both?
- Does the client/customer already include invoice numbers in e-transfer messages?
- Does the bookkeeper want payments deposited directly to bank or Undeposited Funds/clearing?
- Are QBO customer names clean enough for matching?
- Does GHL have working mobile notifications for the owner?
- Who has authority to approve unmatched payments?

## Best First Build
Build v1 like this:

Parseur → Make → QBO Receive Payment → Google Sheet audit log → GHL notification/workflow.

Do not build one-tap resolve buttons first. Get the core payment matching stable, then add fancy mobile exception buttons later.
