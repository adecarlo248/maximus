# Make / QuickBooks Estimate-to-Invoice — Corrected Dedupe Build

## Verified Make behavior from research
- Make Data Store `Get a record` / search-style modules may return **no bundles** when no record exists; that is not necessarily an error.
- The module must have **Continue scenario if no results** enabled if downstream filtering needs to evaluate no-match cases.
- Better dedupe module: **Data store → Check the existence of a record** keyed by Estimate ID. It returns an existence boolean and avoids relying on missing bundles.
- Error handlers are not the right primary dedupe path here; they caused confusion and do not provide a clean normal-flow bundle for filtering in Tony's scenario.
- The final Data Store step only prevents duplicates on future runs if the initial check is correctly wired before invoice creation.

## Correct scenario order
1. QuickBooks — Search for Estimates
   - Query: `SELECT * FROM Estimate WHERE MetaData.LastUpdatedTime > '2026-07-01' MAXRESULTS 10`
2. Filter: `Estimate found`
   - Use Search module total bundles > 0 if needed.
3. QuickBooks — Get an Estimate
   - Estimate ID = Search result Estimate ID.
4. Filter: `Accepted date exists`
   - Field: Get Estimate → Accepted date
   - Operator: Exists
   - Do not rely on Transaction status; it was unreliable in Make tests.
5. Data store — Check the existence of a record
   - Key = Get Estimate → Estimate ID
6. Filter: `Not already processed`
   - Field: Data Store Check existence result / exists boolean
   - Operator: Boolean equal to false
7. QuickBooks — Create an Invoice
   - Map from Get Estimate, not Search Estimate.
8. QuickBooks — Send an Invoice
   - Invoice ID = Create Invoice → Invoice ID.
9. Data store — Update a record (or Add/replace if visible)
   - Key = Get Estimate → Estimate ID
   - Insert missing record = Yes
   - Store: estimateId, invoiceId, invoiceDocNumber, processedAt/current date.

## Data store structure
Create data structure fields:
- estimateId — Text
- invoiceId — Text
- invoiceDocNumber — Text
- processedAt — Date
- customerName — Text (optional)

## Key principle
The duplicate prevention happens before Create Invoice, not after. The final data store write is only the receipt that future runs check against.
