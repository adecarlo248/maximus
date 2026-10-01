# Peterborough Waterproofing — Google Ads Recovery Plan

**Prepared:** 2026-09-11  
**Prepared by:** 1APP  
**Status:** Audit complete; implementation pending campaign approval and Ad Manager connection

## Executive Finding

The ads are generating traffic, but the current system is not producing or measuring enough qualified opportunities from that traffic. Increasing the budget now would amplify waste.

During the last complete 30-day period reviewed (2026-08-12 through 2026-09-10):

- 42,018 impressions
- 1,144 clicks
- $722.72 CAD in ad spend
- 1 tracked conversion
- 0.09% tracked click-to-conversion rate
- $722.72 blended tracked cost per conversion

The main problem signals are:

1. **Low-quality traffic:** One paused campaign generated 925 clicks for $210.78 and zero conversions. The unusually low $0.23 CPC suggests broad or low-intent traffic that needs a network, placement, location, and search-term audit.
2. **Poor keyword-to-service alignment:** The active campaign spent $168.53 of its keyword-level spend on `free home inspection`, producing 24 clicks and zero conversions. Home-inspection intent is not the same as waterproofing, foundation repair, or mould-remediation intent.
3. **Broken or incomplete conversion measurement:** The 1APP Google Ads connection returns no conversion actions. The website source contains GA4 but no visible Google Ads conversion tag. The embedded estimate form is not preserving usable Google Ads attribution in 1APP.
4. **No Google attribution in client records:** Among 313 non-QuickBooks contacts added since 2026-04-18, zero were identified as Google or paid-search contacts. Recent estimate requests appear as Referral or Other.
5. **Pipeline pollution:** All 260 opportunities reviewed are open in New Lead, have no recorded last action, and have no useful source. Most appear tied to social activity rather than qualified sales leads. This makes ad ROI impossible to judge from the pipeline.
6. **Incomplete response system:** Website Form SMS Text Back is published, but Missed Call Text Back and Peterborough Waterproofing Sales Automation are still drafts. Google Ads traffic therefore does not have a fully proven lead-to-estimate follow-up path.

Most recent weekly trend:

- 2026-09-04 through 2026-09-10: 11 clicks, $73.90 spend, zero conversions.
- 2026-08-28 through 2026-09-03: 523 clicks, $157.68 spend, zero conversions.
- 2026-08-21 through 2026-08-27: 277 clicks, $215.05 spend, zero conversions.

The two high-volume campaigns are now paused. The remaining enabled campaign still produced no tracked conversion in the most recent week.

## What We Can Say to the Client

> You are right that the ads are not producing the same business response. The data shows Google is still sending traffic, but too much of that traffic is either low intent or is not being tracked through to an estimate and completed job. In the last 30-day period, the account received more than 1,100 clicks but recorded only one conversion. One active keyword attracting spend is “free home inspection,” which does not closely match the waterproofing work you want.
>
> Our recommendation is not to increase the budget. First, we will repair the tracking, separate campaigns by service, remove irrelevant searches, send each ad to a matching page, and connect every lead to immediate 1APP follow-up. Once 1APP can show which searches become qualified leads, estimates, and jobs, we can optimize the budget around revenue instead of clicks.

## Recovery Strategy

### Phase 1 — Stop Waste and Establish a Baseline

1. Keep the two currently paused campaigns paused.
2. Do not increase the active campaign budget.
3. Review Google Ads Change History for the date performance declined.
4. Export Search Terms for the last 90 days.
5. Review location, device, hour-of-day, network, and demographic performance.
6. Confirm whether Search Partners or Display traffic is enabled.
7. Confirm every conversion action, its source, status, counting method, and Primary/Secondary setting.
8. Confirm that calls, forms, estimate bookings, qualified leads, and won jobs are not being double-counted.

### Phase 2 — Repair Measurement

1. Connect the Google Ads account to 1APP Ad Manager. The reporting connection exists, but Ad Manager is not connected.
2. Add an account-level tracking template that preserves campaign, ad group, keyword, match type, creative, and GCLID data.
3. Add Google Ads conversion tracking to every ad landing page.
4. Replace or repair the embedded form so click identifiers and UTM fields are captured inside 1APP.
5. Test the complete path with a real ad click:
   - Landing page loads.
   - Call or form submission is recorded.
   - Contact is created or updated once.
   - Opportunity is created once.
   - Source, campaign, ad group, keyword, landing page, and GCLID are stored.
   - Immediate response workflow runs.
   - Google receives the intended conversion.

### Phase 3 — Rebuild Around High-Intent Searches

Use Search only for the controlled restart. Keep Display and Search Partners off until Search performance is proven.

#### Campaign 1 — Basement Waterproofing

- basement waterproofing Peterborough
- wet basement repair
- basement leak repair
- water coming into basement
- interior basement waterproofing
- exterior basement waterproofing

#### Campaign 2 — Foundation and Crack Repair

- foundation crack repair Peterborough
- leaking foundation repair
- foundation water leak
- concrete crack injection

#### Campaign 3 — Mould Removal and Testing

- mould removal Peterborough
- mould remediation Peterborough
- basement mould removal
- mould testing Peterborough

#### Optional Campaign 4 — Sump Pumps and Drainage

- sump pump installation Peterborough
- sump pump replacement
- French drain installation
- weeping tile repair

Start with Phrase and Exact match. Expand only after search-term and conversion data proves the traffic quality.

Initial negative-keyword themes:

- home inspection / home inspector
- jobs / careers / salary
- course / training / certification
- DIY / how-to / materials only
- free inspection when it indicates a general home inspection rather than a waterproofing estimate
- pool / boat / vehicle / clothing / spray products
- rental / tenant questions when outside the approved customer profile

### Phase 4 — Landing-Page Alignment

Each service group needs a matching landing page rather than sending every click to the general homepage.

Every page should contain:

1. Exact service and geography in the headline.
2. Active-water/emergency call option.
3. Free-estimate CTA above the fold.
4. Click-to-call button on mobile.
5. Proof: 25-year transferable warranty, service area, reviews, and relevant project images.
6. Short form: name, phone, email, postal code, service needed, and urgency.
7. No unrelated service clutter.
8. Confirmation page that fires the correct Google Ads conversion.

### Phase 5 — 1APP Lead-Response Build

#### Required Contact Fields

- Lead Source
- Original Campaign
- Ad Group
- Keyword/Search Term
- Match Type
- GCLID
- Landing Page
- Service Needed
- Postal Code
- Active Water Now? Yes/No
- Urgency
- Estimated Job Value

#### Workflow A — Google Ads Lead: Immediate Response

**Trigger:** Google lead form, tracked website form, or tracked call.  
**Actions:**

1. Add tag `source-google-ads`.
2. Create or update one opportunity in New Lead.
3. Assign the lead to Justin.
4. Send immediate internal notification to Justin and Belinda.
5. Send immediate SMS:

> Hi {{contact.first_name}}, this is Peterborough Waterproofing. We just received your request. Are you dealing with active water coming in right now, or are you looking to arrange a free estimate?

6. Create a call task due within five minutes during business hours.
7. If no reply: follow up at 15 minutes, 2 hours, Day 1, Day 3, and Day 7.
8. Stop the sequence when the lead replies, books, opts out, or is marked not qualified.

#### Workflow B — Qualified Lead and Estimate Booking

**Trigger:** Required qualification fields completed.  
**Actions:**

1. Move opportunity to Contacted or Estimate Booked.
2. Send the matching confirmation and reminders.
3. Record the qualified-lead timestamp.
4. Send an offline conversion to Google for Qualified Lead or Estimate Booked.
5. Alert the owner if no appointment is booked within one business day.

#### Workflow C — Job Won Revenue Feedback

**Trigger:** Opportunity moves to Job Won.  
**Actions:**

1. Require job value.
2. Send the won-job conversion and value to Google.
3. Remove the contact from open sales follow-up.
4. Begin post-job review and referral workflow after completion/payment.

#### Workflow D — Ads Health Alert

**Trigger:** Daily scheduled check.  
**Actions:**

1. Compare spend, tracked leads, qualified leads, estimate bookings, and won jobs.
2. Alert Tony when spend exceeds the agreed guardrail without a qualified lead.
3. Alert when tracking produces zero leads despite recorded clicks.
4. Alert when lead response exceeds five minutes.

The spend guardrail must be based on acceptable cost per qualified lead, which requires average job value, gross margin, and estimate-to-job close rate.

### Phase 6 — Pipeline Repair

1. Stop social comments from creating sales opportunities before qualification.
2. Keep social engagement in a separate nurture process or separate pipeline.
3. Deduplicate contacts and opportunities.
4. Require Source, Service Needed, Next Action, and Owner for every sales opportunity.
5. Close, archive, or requalify the 260 open New Lead opportunities only after Justin or Belinda approves the cleanup list.

## Measurement Scorecard

Track weekly by campaign and service:

- Spend
- Impressions
- Clicks
- CTR
- CPC
- Tracked leads
- Qualified leads
- Estimate bookings
- Estimates completed
- Quotes sent
- Jobs won
- Revenue won
- Cost per lead
- Cost per qualified lead
- Cost per booked estimate
- Cost per won job
- Lead-to-estimate rate
- Estimate-to-job rate
- Return on ad spend
- Median lead-response time

Clicks and impressions are diagnostic. Cost per qualified lead, cost per booked estimate, cost per won job, and revenue are the business metrics.

## Information Required From Peterborough Waterproofing

1. Approximate date the ads stopped performing like before.
2. Average job value by service.
3. Gross-margin range by service.
4. Estimate-to-job close rate.
5. Monthly Google Ads budget and maximum acceptable cost per booked estimate.
6. Priority services for the next 60 days.
7. Confirmation of the highest-priority service towns.
8. Approval to connect Google Ads to 1APP Ad Manager.
9. Approval to install conversion tracking and tracking parameters on the website.
10. Approval for Tony to rebuild campaign structure and publish only after their review.

## Implementation Gate

Do not publish a replacement campaign until:

- Ad Manager connection is complete.
- Conversion tests pass.
- Search Terms audit is reviewed.
- Negative keyword list is approved.
- Service-specific landing pages are live.
- Lead response workflow is published and tested.
- Daily budget and success thresholds are approved.
- Justin or Belinda gives written launch approval.

## Sources

- 1APP live account audit performed 2026-09-11.
- Google Ads reporting: 2026-06-13 through 2026-09-10.
- 1APP contact and opportunity records: 2026-04-18 through 2026-09-11.
- [Google Ads search terms report](https://support.google.com/google-ads/answer/2472708)
- [Google Ads Quality Score](https://support.google.com/google-ads/answer/6167118)
