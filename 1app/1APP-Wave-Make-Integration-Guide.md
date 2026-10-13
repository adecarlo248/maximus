# 1APP + Wave + Make.com Integration Guide

Updated: 2026-10-13

## Recommended Positioning

**1APP runs the customer journey. Wave keeps the books. Make.com connects the gaps.**

- **1APP:** lead capture, SMS/email/phone communication, pipeline, appointments, follow-up, reviews, tasks, and customer-facing automation.
- **Wave:** customers, invoices, accounting, income/expenses, transactions, reporting, payments, and payroll when separately enabled in Wave.
- **Make.com:** custom logic, field mapping, deduplication, exception handling, status handoffs, and workflows that the native connector does not provide.

## Native Wave Integration Inside 1APP

Verified in the current HighLevel invoices-integration build:

- Connect a Wave business using OAuth.
- Select the Wave income account used for synced transactions.
- Sync 1APP invoices to Wave.
- Import Wave contacts into 1APP.

Do not promise the following until tested in the specific client account:

- Two-way invoice edits or voids.
- Payment-status reconciliation.
- Estimates, payroll, expenses, bank transactions, products, or taxes syncing through the native connector.
- Full two-way customer synchronization.

## Official Make.com Wave Capabilities

Make's official Wave app supports OAuth 2.0 and includes:

### Customers

- List customers.
- Get a customer by ID.
- Get a customer by email.
- Create, update, and delete customers.

### Invoices

- Create an invoice.
- Approve an invoice.
- Send an invoice by email, optionally with a PDF.
- List invoices.
- Watch invoices since the previous scenario run.

### Products and Services

- Create products/services.
- List products/services.
- Update products/services.

### Accounting Actions

- Create transactions.
- Create accounts.
- Create sales taxes.
- Create income or expense records.
- Run authorized Wave GraphQL queries for supported data not covered by a standard module.

## Official Make.com GoHighLevel Capabilities

Make's official GoHighLevel app can:

- Watch supported HighLevel events through webhooks.
- Search, get, create, update, and delete contacts.
- List, get, create, update, and delete opportunities.
- List, get, create, update, and delete tasks.
- Add or remove contacts from campaigns.
- Add notes to contacts.
- Make supported API calls for capabilities not exposed as standard modules.

## Best Integration Architecture

### Baseline: Native Connector

Use the native 1APP Wave integration when the client only needs:

1. Wave contacts imported into 1APP.
2. 1APP invoices synced to Wave.
3. Transactions assigned to the correct Wave income account.

This is the lowest-maintenance setup.

### Advanced: Make.com Automation Layer

Use Make when the client needs custom behavior:

1. **1APP contact to Wave customer:** When a qualified contact becomes a customer, search Wave by email; create the customer only if no match exists, otherwise update it.
2. **Won opportunity to Wave invoice:** When an opportunity reaches the approved billing stage, retrieve the 1APP contact, upsert the Wave customer, create the invoice, approve it, and send it.
3. **Wave invoice back to 1APP:** Watch Wave invoices, match the 1APP contact/opportunity, add a note, create a follow-up task, or move the opportunity when the tested invoice status changes.
4. **Collections workflow:** If Wave exposes an invoice as overdue/unpaid in the connected account, add the contact to an approved 1APP reminder workflow. Remove or stop reminders when paid status is confirmed. This must be tested before sale.
5. **Product/service sync:** Map an approved 1APP service catalogue to Wave products/services with stable IDs to prevent duplicates.
6. **Exception handling:** Route missing customer matches, invalid taxes, duplicate invoices, or failed API calls to a manager task instead of silently failing.
7. **Reconciliation report:** Send a weekly summary of invoices created, sent, paid/unpaid if available, failures, and records requiring review.

## Safeguards

- Use email plus a stable external/contact ID for deduplication; never rely on name alone.
- Add an idempotency/Data Store check before creating invoices or financial records.
- Test with one contact and one small test invoice before enabling the scenario.
- Confirm CAD currency, HST mapping, due dates, line items, Wave business, and income account.
- Define the source of truth: 1APP for CRM/communications; Wave for accounting and reconciliation.
- Do not automatically market to contacts imported from Wave. Accounting records do not prove CASL consent.
- Do not automate deletions or financial adjustments without an approval step.
- Have the client's bookkeeper/accountant approve account and tax mappings.

## Setup Sequence

1. In the client's 1APP sub-account, open the Wave tile in the Integrations area.
2. Connect the correct Wave business through OAuth.
3. Select the intended Wave income account and save.
4. Import contacts and inspect duplicates/field mapping.
5. Create one test contact and one test invoice; verify both systems.
6. Decide whether the native connector is enough.
7. If advanced automation is needed, connect both Wave and GoHighLevel to Make using OAuth.
8. Build one scenario at a time with dedupe, logging, error handling, and a manual exception path.
9. Prove invoice creation, updates, status handling, taxes, and duplicate prevention before production.

## What 1APP Can Sell

**Wave Accounting Handoff Setup**

- Native Wave connection.
- Income-account and tax mapping.
- Contact import cleanup.
- Invoice-sync testing.
- Source-of-truth documentation.

**Wave Automation Plus**

- Custom Make scenarios.
- Customer upsert and deduplication.
- Opportunity-to-invoice automation.
- Status-driven 1APP tasks and follow-up.
- Exception queue and weekly reconciliation report.
- Monitoring and support.

Do not sell payroll automation or full bookkeeping as part of the native connector. Those require separate Wave services, accounting decisions, and a separately tested scope.

## Current Make.com Access Status

The Make.com MCP server is connected and online, but currently exposes **zero callable tools/scenarios**. Make can still be used through its normal web interface, but Maximus cannot inspect or run the account's scenarios through MCP until scenarios/tools are enabled in Make's MCP configuration.

## Sources

- Make Wave documentation: https://apps.make.com/wave
- Make GoHighLevel documentation: https://apps.make.com/highlevel
- Wave accounting: https://www.waveapps.com/accounting
- Wave invoicing: https://www.waveapps.com/invoicing
- Wave payments: https://www.waveapps.com/payments
- Wave payroll: https://www.waveapps.com/payroll
