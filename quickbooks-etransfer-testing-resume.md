# QuickBooks e-Transfer Automation — Testing Resume

## Project
Peterborough Waterproofing e-transfer email → Parseur → Make.com → QuickBooks Online Receive Payment → Google Sheet audit log → GHL notification/update.

## Current Phase
Testing phase. Do **not** fully auto-create payments for all real deposits yet. Start with controlled test invoices and only enable auto-create for safe invoice-number matches.

## Core Rule
QBO is the accounting source of truth. The automation should create a QBO **Receive Payment** against an open invoice. When the bank feed imports the real deposit, QBO should **MATCH** it — not add duplicate income.

## Resume Here — Immediate Next Steps

### 1. Confirm Parseur output is clean
Required fields:
- sender_name
- amount
- payment_date
- memo
- invoice_number
- reference_id or email/document ID
- source_email_subject

Pass condition:
- Amount is numeric, e.g. `10.00`, not `$10.00`
- Date is usable by Make/QBO
- Invoice number is extracted from memo/message when present
- Reference/email ID exists for duplicate protection

### 2. Build/confirm Make scenario modules
Recommended v1 modules:
1. Parseur — Watch Documents
2. Tools — Set Variables / normalize values
3. Data Store or Google Sheets — Search duplicate by `reference_id` or Parseur document ID
4. Router
   - Duplicate → stop
   - Missing required fields → exception path
   - Invoice number present → QBO invoice lookup
   - No invoice number → conservative matching / exception
5. QuickBooks — Search/List Invoices
6. Filter — invoice open + amount safe
7. QuickBooks — Create Payment / Receive Payment
8. Google Sheets/Data Store — Log success
9. GHL — Send internal notification/update contact

### 3. First test case to run
Use QBO test invoice:
- Customer: `Test Etransfer Customer`
- Invoice: `TEST-1001`
- Amount: `$10.00`

Send/forward test e-transfer email with memo:
`Invoice TEST-1001`

Expected result:
- Parseur extracts `TEST-1001`, `10.00`, sender, date, reference ID
- Make finds open QBO invoice `TEST-1001`
- Make creates Receive Payment for `$10.00`
- Invoice becomes paid
- Audit log records one row
- Duplicate run stops and does not create a second payment

## Make Filters

### Required fields filter
Continue only if:
- amount exists
- payment_date exists
- sender_name exists
- reference_id OR parseur_document_id exists

### Duplicate filter
If log lookup finds same reference/document ID:
- Stop scenario
- Do not touch QBO

### Safe auto-payment filter
Auto-create QBO payment only if:
- invoice_number exists
- QBO invoice found
- invoice balance > 0
- amount <= invoice balance
- no duplicate found

If any of those fail:
- Route to exception notification
- Do not create QBO payment

## QBO Payment Mapping

Create payment fields:
- CustomerRef = invoice customer
- TotalAmt = parsed amount
- TxnDate = parsed payment date
- PaymentMethodRef = E-Transfer
- DepositToAccountRef = linked bank account OR bookkeeper-approved clearing account
- PrivateNote = `Auto-created from e-transfer email. Sender: {{sender_name}}. Memo: {{memo}}. Ref: {{reference_id}}.`
- LinkedTxn:
  - TxnId = QBO invoice ID
  - TxnType = Invoice
  - Amount = parsed amount

## Exception Message Template

⚠️ Unmatched e-Transfer
Amount: ${{amount}}
From: {{sender_name}}
Memo: {{memo}}
Date: {{payment_date}}
Reason: {{exception_reason}}

Action needed: Review in QBO / GHL before marking invoice paid.

## Testing Checklist

### Test 1 — Perfect match
Memo includes invoice number, amount equals balance.
Expected: auto-payment created, invoice paid.

### Test 2 — Partial payment
Memo includes invoice number, amount less than balance.
Expected: payment created, invoice still partially unpaid.

### Test 3 — Duplicate
Run/send same email twice.
Expected: second attempt stops before QBO.

### Test 4 — No invoice number
Sender/amount may match, but v1 should be conservative.
Expected: exception unless Tony explicitly enables safe no-invoice matching.

### Test 5 — Unknown sender
Expected: exception, no QBO payment.

### Test 6 — Amount mismatch
Expected: exception unless partial payments are intentionally allowed.

### Test 7 — Bank feed match
When bank feed deposit arrives, QBO should offer Match, not Add.
Expected: no duplicate income.

## Go-Live Safety
For first 2–3 real e-transfers:
- Run monitoring/logging only if possible
- Compare automation match to manual/bookkeeper choice
- Then enable auto-create only for invoice-number matches

## Client Explanation
“Your bank is already connected to QuickBooks, so the deposit shows up there. This automation reads the e-transfer email, figures out which invoice it belongs to, marks that invoice paid in QuickBooks, and then the bank feed deposit can match it. If the system isn’t sure, it flags it instead of guessing.”
