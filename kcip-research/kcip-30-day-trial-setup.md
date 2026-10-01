# KCIP 30-Day Trial Setup — Internal Notes for Tony

## Main recommendation
Do **not** port KCIP’s main business number for the trial.

Use a dedicated local 1APP/KCIP trial number instead. Forward calls to his current business number and use that trial number for AI Voice, missed-call text back, SMS replies, quote forms, and estimate booking.

## Why
Porting the main number too early creates friction and risk. A trial should prove value with low operational risk.

## Trial setup

1. Provision local 705 trial number
   - Label: KCIP Quote / Estimate Line
   - Forward inbound calls to existing KCIP business phone
   - Use AI Voice for overflow or after-hours if configured

2. Create KCIP inbox
   - Shared inbox for SMS/email replies
   - Customer replies land in KCIP’s inbox
   - Attach conversations to contact records

3. Build estimate calendar
   - Calendar name: Backyard Estimate
   - Controlled estimate blocks
   - 24-hour and 2-hour reminders
   - Optional phone consultation calendar if needed

4. Build quote intake form / landing page
   - First name
   - Last name
   - Phone
   - Email
   - Town / service area
   - Service category
   - Desired timeline
   - Project notes
   - Photo upload if possible

5. Connect trial channels
   - Add trial quote link/number to Facebook bio/posts
   - Add temporary CTA button or link on Shopify website if possible
   - Use QR code on leave-behind/business card if needed
   - Optional: update voicemail greeting to mention quote link or trial number

6. Build trial pipeline
   - New Lead
   - Auto-Reply Sent
   - Qualified
   - Estimate Booked
   - Quote Sent
   - Follow-Up Active
   - Won
   - Lost / Later

7. Build core workflows
   - Missed-call text back on trial number
   - Website/form confirmation
   - Estimate booking confirmation/reminders
   - Quote follow-up sequence
   - Review request after completed trial job if applicable

## What he should get access to during trial

Customer-facing:
- Quote/estimate number
- Quote request form or temporary landing page
- Booking calendar
- SMS confirmation/reminders
- AI Voice overflow/after-hours handling

Owner/team-facing:
- KCIP shared inbox
- CRM contacts
- Opportunity pipeline
- Calendar view
- Conversation history
- Weekly performance snapshot

## What should NOT be included free

- Full website rebuild
- QuickBooks live automation
- Full customer database migration
- Advanced Revenue Engine buildout
- Social content management
- Complex custom workflows beyond the agreed trial scope
- Porting main business number

## Trial success metrics

Track:
- Calls to trial number
- Missed calls recovered
- SMS replies
- Form submissions
- Estimate bookings
- No-shows avoided by reminders
- Quotes followed up
- Jobs won / potential revenue
- Admin time saved

## Customer-friendly positioning

“Instead of changing your main business number right away, we’ll give KCIP a dedicated trial quote line and front-office system for 30 days. If it captures leads, saves time, and makes follow-up easier, then we can decide whether to connect more of the business permanently.”

## Important limitation

If KCIP keeps using only the old business number and does not forward calls or promote the trial number/link, 1APP cannot magically detect every missed call from the old number. The trial works best when new inquiries are routed through the trial quote number, quote form, calendar, or web chat.
