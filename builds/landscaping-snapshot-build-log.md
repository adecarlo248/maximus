# 🌿 Landscaping GHL Snapshot — Build Log
**Sub-account:** landscaping (Peterborough, ON)
**Location ID:** YJTZd59YCy0mHJih0K6j
**Build Date:** 2026-07-21
**Built by:** Maximus AI Subagent
**Status:** COMPLETE — Phases 1–4 deployed via API; Phase 5 (Workflows) documented below

---

## PHASE 1: CUSTOM FIELDS ✅

All 17 custom fields created at the contact level.

| # | Field Name | Type | GHL Field ID |
|---|-----------|------|-------------|
| 1 | Lead Source | SINGLE_OPTIONS (dropdown) | `1GtmxLcjnSyuOiv64dit` |
| 2 | Job Type | SINGLE_OPTIONS (dropdown) | `YYOl44lKQKtaiCyJewp7` |
| 3 | Service Category | SINGLE_OPTIONS (dropdown) | `wRFVGJFzwJ1DqeaQ2f88` |
| 4 | Property Type | SINGLE_OPTIONS (dropdown) | `xTRPs34uA9RPL0ZjM6Mc` |
| 5 | Lot Size | SINGLE_OPTIONS (dropdown) | `oHHXPMooXLDWyAz4ggnF` |
| 6 | Maintenance Program Tier | SINGLE_OPTIONS (dropdown) | `NNEkSGJXu403ht8UJMug` |
| 7 | Program Start Date | DATE | `GEdacqBCLvKWeJ4qGlD9` |
| 8 | Program Renewal Date | DATE | `TQJ5MbsblawdBnTRNy5H` |
| 9 | Snow Removal Contract | RADIO (Yes/No) | `xoVKLwZAsTUgKlA1Zc7q` |
| 10 | Snow Contract Renewal Date | DATE | `9104jq5VowAmtv5uNFJl` |
| 11 | Irrigation System Present | RADIO (Yes/No) | `mH7zHGvDuFH8kIbAelsR` |
| 12 | Estimate Amount | MONETORY | `1zOzoCy34nIwIFRdIfVf` |
| 13 | Contract Amount | MONETORY | `TvjcpHPSHVrNrNoF6JUG` |
| 14 | Crew Assigned | TEXT | `t2WvcE866lLrStb4VZDz` |
| 15 | Review Requested | RADIO (Yes/No) | `xk9YiiTnlaL20g3XwpfV` |
| 16 | Review Received | RADIO (Yes/No) | `qlQ02aYlBEnnq3JfyPgC` |
| 17 | Neighbour Campaign Sent | RADIO (Yes/No) | `IKLI5j3If8wROBHVJBBB` |

**Notes:**
- GHL does not support a native CHECKBOX datatype via API for contact fields. Fields 9, 11, 15, 16, 17 use RADIO with Yes/No options as the closest equivalent.
- Field key pattern: `contact.<snake_case_name>` (e.g., `contact.lead_source`)

### Custom Field Option Values

**Lead Source options:** Google LSA | Google Organic | Referral | Door Knock | Kijiji/Craigslist | Real Estate Agent | Property Manager | HOA | Facebook Ad | Repeat Customer

**Job Type options:** Lawn Maintenance | Spring Cleanup | Fall Cleanup | Sod Installation | Hardscaping/Interlock | Retaining Wall | Irrigation | Aeration/Overseeding | Mulching | Fertilization | Snow Removal | Tree/Shrub Trimming | Landscape Design

**Service Category options:** One-Time Job | Recurring Maintenance | Hardscape Project | Snow Removal Contract | Commercial

**Property Type options:** Residential | Commercial | HOA/Condo | Multi-Unit | Municipal

**Lot Size options:** Under 5,000 sqft | 5,000-10,000 sqft | 10,000-20,000 sqft | 20,000+ sqft | Acreage

**Maintenance Program Tier options:** None | Basic | Standard | Premium

---

## PHASE 2: PIPELINES ✅

All 5 pipelines created.

### Pipeline 1: Landscaping - Residential Estimate
**Pipeline ID:** `ZfYs9Xe0rvneMbhh9l0I`

| Stage | Description |
|-------|-------------|
| New Lead | Lead came in — not yet contacted |
| Estimate Scheduled | Site visit appointment booked |
| Estimate Complete | Site visit done, preparing quote |
| Proposal Sent | Quote delivered to client |
| Follow-Up Active | In automated follow-up sequence |
| Contract Signed | Client accepted and signed |
| Job Scheduled | Job on the calendar |
| Job In Progress | Active job site |
| Job Complete | Work finished |
| Review Requested | Google review request sent |
| Maintenance Upsell | Being pitched recurring program |
| Lost | Did not book |

---

### Pipeline 2: Landscaping - Maintenance Program
**Pipeline ID:** `OAT9ARKa97VlkTIihkpH`

| Stage | Description |
|-------|-------------|
| Upsell Offered | Post-one-time-job pitch initiated |
| Proposal Sent | Full-season pricing delivered |
| Program Active | Enrolled and on recurring schedule |
| Spring Service Due | Spring startup service pending |
| Summer Check-In | Mid-season satisfaction check |
| Fall Service Due | Fall cleanup/winterization pending |
| Renewal Sent | Next season renewal offer sent |
| Renewed | Re-signed for coming season |
| Cancelled | Churned — exit survey triggered |

---

### Pipeline 3: Landscaping - Hardscape Project
**Pipeline ID:** `3S37TBBoh8rtG5Tif2CR`

| Stage | Description |
|-------|-------------|
| New Inquiry | Large project request received |
| Site Visit Scheduled | Walkthrough booked |
| Design/Quote In Progress | Estimating and design underway |
| Proposal Sent | Multi-page quote delivered |
| Follow-Up Active | Following up on sent proposal |
| Deposit Paid | Project confirmed with deposit |
| Materials Ordered | Materials procurement initiated |
| Job Scheduled | On the build calendar |
| Job In Progress | Active job site |
| Punch List | Completion inspection/fixes |
| Job Complete | Work finished |
| Final Invoice | Final billing sent |
| Paid | Full payment received |
| Review + Referral | Google review + neighbour campaign triggered |

---

### Pipeline 4: Landscaping - Snow Removal
**Pipeline ID:** `VH4Rvyxiz9P9ud4dzKB5`

| Stage | Description |
|-------|-------------|
| New Lead | Winter service request received |
| Quote Sent | Seasonal or per-push pricing delivered |
| Contract Signed | Agreement back, route confirmed |
| Active - Season | Full season snow client |
| Renewal Sent (Aug) | Next-season renewal sent in August |
| Renewed | Re-contracted for coming season |
| Cancelled | Did not renew |

---

### Pipeline 5: Landscaping - Commercial / HOA
**Pipeline ID:** `IriZABT2NhsLRIHaEW6j`

| Stage | Description |
|-------|-------------|
| New Prospect | Initial contact from PM or HOA |
| Site Walk Scheduled | Multi-property walkthrough booked |
| Proposal Sent | Formal multi-property proposal delivered |
| Contract Signed | Annual maintenance agreement signed |
| Active Account | Recurring commercial client |
| Seasonal Review | Quarterly/seasonal check-in |
| At Risk | Account showing churn signals |
| Renewed | Re-contracted for another season |
| Lost | Account terminated |

---

## PHASE 3: CALENDARS ✅

All 4 calendars created.

| # | Calendar Name | Duration | GHL Calendar ID |
|---|--------------|----------|----------------|
| 1 | Free Estimate - Landscaping | 45 min | `ys3xUSWsdDxSwsGTdejc` |
| 2 | Hardscape Design Consultation | 60 min | `LtMQOBRVQk0VZAdbBQfi` |
| 3 | Commercial Site Walk | 60 min | `xd3fMLzY8xGKAebdLh4P` |
| 4 | Snow Removal Quote | 30 min | `dIfoDzAud1OwHLY4dzrH` |

**Note:** Calendar availability hours should be manually configured in GHL UI:
- Free Estimate: Mon–Fri 8am–5pm
- Hardscape Design Consultation: Mon–Fri 8am–4pm
- Commercial Site Walk: Mon–Fri 8am–4pm
- Snow Removal Quote: Mon–Fri 8am–5pm

---

## PHASE 4: TAGS ✅

All 30 tags created.

| Tag Name | GHL Tag ID |
|----------|-----------|
| new-lead | `EEytbq1JqDmVFkYLindo` |
| one-time-job | `6wsBUgDcqOIsv7NCO9JT` |
| maintenance-program | `A5kaq8rk9zEb1NIk2OOj` |
| hardscape-project | `VfzGmEXLBgs67KottrBO` |
| snow-removal | `f6SXYn3ByQusf1qn8QGG` |
| spring-cleanup | `pwUy4vnHoUn2tRpiTUC2` |
| fall-cleanup | `Bk3MhsOJ69D4F6ZChCHt` |
| aeration-overseeding | `4y503A5WZxCfeUnxNzjw` |
| sod-installation | `5MPGxiUeUfvFuhjD4xQq` |
| irrigation | `YMgMMJgapi0GvY04CgWa` |
| estimate-sent | `UX9QWjALnLjISnIMDorL` |
| contract-signed | `zsHOZmuPQrsSyumiavcN` |
| job-complete | `uuG0QQOZ4qSX9rqO7isX` |
| review-requested | `6ePkvS8VwUOCiHdo1gXZ` |
| review-received | `3NR85NzAxwc7goiSVTyV` |
| referral | `WaTtFVpPuX0t1d96mU6v` |
| neighbour-campaign | `MF9TEYDqRenfFRU4jtPc` |
| cold-lead | `n0bOYIQtDUQfL9OuQNpj` |
| no-show | `jfKhAunde62Zci0wepi1` |
| google-lsa | `kxfh5LzwCfnRbdda08vu` |
| door-knock | `ugAncCJ8HYWE6cejYRnE` |
| real-estate-agent | `hH6t1qDm5eiC47xFkzzs` |
| hoa | `udbDmEp881DyRloDEnGa` |
| property-manager | `gUlF6cKEo58z1opPsmnu` |
| commercial-account | `TyIkLvIPWS8USgNZ6brS` |
| facebook-ad | `fCiRfsBS0YJv2zGLaaOp` |
| repeat-customer | `CNrl2yhj4mxRuJd5AjIq` |
| snow-contract-renewal-due | `VdpxlgL1TuzgxgEA1XRK` |
| program-renewal-due | `VcwDcDBzUO0O2c2ryLFq` |
| upsell-candidate | `t6VGx7krBnWQVZERwdBK` |

---

## PHASE 5: WORKFLOWS — Build Specs (Manual Build Required)

> **Note:** GHL public API does not support workflow creation. All 18 workflow specs below are complete and ready to build manually in GHL → Automation → Workflows.

---

### ✅ WORKFLOW 1: Missed Call Text Back — NATIVE GHL SETTING (Not a Workflow)

**Do NOT build this as a workflow.** Use GHL's built-in MCTB feature instead.

**How to enable:**
1. Go to **Settings → Phone Numbers**
2. Click on your phone number
3. Click the **"Voicemail & Missed Call TextBack"** tab
4. Check **"Enable Missed call textback"** ✅
5. Click **"Customize"** and paste the message below

**Customized message for this trade:**
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — looking for a free landscaping estimate or spring cleanup? Reply YES and we'll get right back to you 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Lead - Speed to Quote
**Trigger:** Contact created OR Contact tag (filter: tag added = new-lead)
**Filter:** Exclude if opportunity already exists in any pipeline

**Actions:**

1. **Send SMS** (immediate)
   > "Hi {{contact.firstName}}! Thanks for reaching out. We'll get back to you within the hour to schedule your free landscaping estimate. – [Owner Name]"

2. **Create Opportunity** → Pipeline: Landscaping - Residential Estimate → Stage: New Lead

3. **Create Task** → "Call {{contact.name}} — new landscaping lead" → Due: 1 hour → Assign to owner

4. **Wait:** 30 minutes (if no reply/call booked)

5. **Send SMS** (if no appointment booked)
   > "{{contact.firstName}}, we want to make sure we connect! What's the best time for us to call about your landscaping project?"

6. **Wait:** 2 hours

7. **Send Email** (if no appointment booked)
   - **Subject:** "Your Free Landscaping Estimate from [Company Name]"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Thanks for reaching out to [Company Name]! We'd love to get out to your property and take a look.
   >
   > Our free estimates are quick, no-pressure, and we'll walk you through exactly what we'd do and what it costs.
   >
   > 📅 Click here to book your free estimate: [Calendar Link — Free Estimate - Landscaping]
   >
   > Or just reply to this email and we'll get back to you right away.
   >
   > Looking forward to connecting!
   > [Owner Name] | [Company Name]

8. **Wait:** 1 day

9. **Send SMS** (if no appointment)
   > "Hey {{contact.firstName}}! Still hoping to connect — our [Month] schedule is filling up fast. Want to lock in your free estimate? 🌿"

10. **Wait:** 2 days

11. **Send SMS** (final attempt)
    > "{{contact.firstName}} — last reach-out! If landscaping is still on your radar this season, we'd love to get out and look at your property. No pressure! [Calendar Link]"

12. **Wait:** 1 day

13. **If No Appointment Booked:** Add tag `cold-lead` → Move opportunity to Lost → End workflow

---

### Workflow 3: Estimate Appointment Confirmation
**Trigger:** Customer booked appointment (calendar: Free Estimate - Landscaping)

**Actions:**

1. **Send SMS** (immediate)
   > "Hi {{contact.firstName}}! Your free landscaping estimate with [Company Name] is confirmed for {{appointment.start_time}}. We'll see you then! 🌿"

2. **Send Email** (immediate)
   - **Subject:** "Your Estimate Appointment is Confirmed — [Date]"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Your free landscaping estimate is confirmed!
   >
   > 📅 **Date & Time:** {{appointment.start_time}}
   > 📍 **Address:** {{contact.address1}}
   >
   > **What to expect:**
   > - Our estimator will walk your property with you (or on their own if you can't be there)
   > - We'll review what services you're looking for
   > - You'll receive a detailed quote within 24 hours
   >
   > **A few things that help:**
   > - Make sure the property is accessible (unlatch any gates)
   > - Have a rough idea of what services you're looking for
   >
   > Questions? Reply to this email or call us at [Phone].
   >
   > See you soon!
   > [Owner Name] | [Company Name]

3. **Wait:** Until 24 hours before appointment

4. **Send SMS** (24hr reminder)
   > "Hi {{contact.firstName}}, just a reminder — your free landscaping estimate is tomorrow at {{appointment.start_time}}. See you then! 🌿"

5. **Wait:** Until 2 hours before appointment

6. **Send SMS** (2hr reminder)
   > "{{contact.firstName}}, we're heading your way in about 2 hours for your landscaping estimate! See you at {{appointment.start_time}}."

7. **Move Opportunity** → Stage: Estimate Scheduled

---

### Workflow 4: No-Show Recovery
**Trigger:** Appointment status (filter: no-show, calendar: Free Estimate - Landscaping)

**Actions:**

1. **Add Tag:** `no-show`

2. **Send SMS** (immediate)
   > "Hi {{contact.firstName}}, we just missed you at your scheduled estimate! No worries — these things happen. Want to reschedule? [Calendar Link]"

3. **Create Task** → "No-show — call {{contact.name}} to reschedule" → Due: Same day

4. **Wait:** 1 day (if not rescheduled)

5. **Send SMS**
   > "{{contact.firstName}}, still interested in a free landscaping estimate? We have openings this week — click here to grab a time that works: [Calendar Link]"

6. **Wait:** 3 days

7. **Send Email** (if no reschedule)
   - **Subject:** "We missed you — want to reschedule your estimate?"
   - **Body:** Brief, friendly reschedule offer

8. **If No Reschedule in 7 days:** Add tag `cold-lead` → End workflow

---

### Workflow 5: Estimate Follow-Up Sequence (5-Step, 21 Days)
**Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent, Pipeline: Landscaping - Residential Estimate)

**Actions:**

1. **Add Tag:** `estimate-sent`

2. **Send SMS** (immediate)
   > "Hi {{contact.firstName}}! Your landscaping estimate has been sent — check your email! Any questions, just reply here. Happy to walk you through anything. 🌿"

3. **Wait:** 2 days

4. **Send SMS** (Follow-up 1)
   > "{{contact.firstName}}, just checking in on your estimate! Did you have a chance to look it over? Happy to answer any questions or adjust the scope."

5. **Wait:** 3 days

6. **Send Email** (Follow-up 2)
   - **Subject:** "Still interested in your landscaping project, {{contact.firstName}}?"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Just following up on the estimate we sent over. We know decisions like this take time — no rush at all.
   >
   > If you have any questions, want to adjust the scope, or just want to chat about options — I'm always happy to connect.
   >
   > 📞 [Phone] | 📧 Reply to this email
   >
   > We'd love to work with you this season!
   > [Owner Name]

7. **Wait:** 5 days

8. **Send SMS** (Follow-up 3)
   > "{{contact.firstName}} — quick check-in! Our schedule is booking up for the season. If you'd like to get on the calendar, now's a great time. Want to move forward?"

9. **Wait:** 5 days

10. **Send SMS** (Follow-up 4 — final)
    > "Last follow-up from us, {{contact.firstName}} — if the timing isn't right this season, totally understood. We'll be here when you're ready! 🌿"

11. **Wait:** 6 days

12. **Add Tag:** `cold-lead` → Move Opportunity to "Lost" → End workflow

---

### Workflow 6: Maintenance Program Upsell (Post One-Time Job)
**Trigger:** Pipeline stage changed (filter: new stage = Maintenance Upsell, Pipeline: Landscaping - Residential Estimate) OR Contact tag (filter: tag added = job-complete) + Service Category = One-Time Job

**Actions:**

1. **Add Tag:** `upsell-candidate`

2. **Wait:** 1 day

3. **Send SMS**
   > "Hi {{contact.firstName}}! Hope you love the work we did 🌿 Did you know we offer full-season lawn maintenance programs — mowing, fertilization, spring & fall cleanup all bundled? Want to hear about it?"

4. **Wait:** 2 days

5. **Send Email**
   - **Subject:** "Turn your one-time service into a full-season program — here's what's included"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Thanks again for choosing [Company Name]!
   >
   > Since we're already familiar with your property, we wanted to let you know about our lawn maintenance programs:
   >
   > 🌱 **Basic** — Weekly/biweekly mowing, edging & blowing
   > 🌿 **Standard** — Above + 4-application fertilization program
   > 🏆 **Premium** — Above + spring cleanup, fall cleanup, aeration & overseeding
   >
   > Full-season clients get priority scheduling, a dedicated crew, and the peace of mind that your lawn is always taken care of.
   >
   > Interested? Reply to this email or call [Phone] — we'd love to set you up.
   >
   > [Owner Name]

6. **Wait:** 5 days

7. **Send SMS** (final upsell)
   > "{{contact.firstName}}, last nudge on the maintenance program! Spots for the season are limited. Interested in locking one in? [Calendar Link to book a quick call]"

8. **Create Opportunity** → Pipeline: Landscaping - Maintenance Program → Stage: Upsell Offered

---

### Workflow 7: Maintenance Program Renewal
**Trigger:** Custom date reminder (select Program Renewal Date field, set 60 days before)

**Actions:**

1. **Add Tag:** `program-renewal-due`

2. **Send Email** (60 days out)
   - **Subject:** "Your lawn care program renews soon — lock in your [Year] pricing now"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Your [Company Name] maintenance program is coming up for renewal — and we wanted to reach out early so you can lock in the same great pricing before any seasonal adjustments.
   >
   > **Your current program:** {{contact.maintenance_program_tier}}
   > **Renewal date:** {{contact.program_renewal_date}}
   >
   > To confirm your renewal, simply reply "RENEW" to this email or click below.
   >
   > If you'd like to upgrade your program this season (add snow removal, fall cleanup, fertilization), now is the perfect time!
   >
   > [Owner Name]

3. **Wait:** Until 30 days before renewal date

4. **Send SMS** (30 days out)
   > "Hi {{contact.firstName}}! Your lawn maintenance program renews in 30 days. Want to confirm for next season? Reply YES and we'll lock you in! 🌿"

5. **Wait:** Until 14 days before renewal date

6. **Send SMS** (14 days — urgent)
   > "{{contact.firstName}}, renewal is in 2 weeks! If you'd like to continue with [Company Name] this season, now's the time to confirm. Reply YES or call [Phone]."

7. **Move Opportunity** (if not renewed) → Pipeline: Landscaping - Maintenance Program → Stage: Renewal Sent

---

### Workflow 8: Snow Removal Contract Campaign (Annual — August)
**Trigger:** Scheduler (August 15 annually)
**Audience:** All contacts tagged `maintenance-program` OR prior `snow-removal` tag

**Actions:**

1. **Add Tag:** `snow-contract-renewal-due`

2. **Send Email** (August 15)
   - **Subject:** "Lock in your snow removal contract before spots fill up — [City]"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > We know it's still summer, but trust us — the best time to secure your snow removal is before the first frost!
   >
   > [Company Name] is now booking seasonal snow removal contracts for winter [Year]. Early birds get:
   > ✅ Priority route placement
   > ✅ Locked-in seasonal pricing
   > ✅ Guaranteed service for every snowfall
   >
   > Once our routes are full, we move to per-push only (no guaranteed availability).
   >
   > **Seasonal contract includes:**
   > - Residential driveway + walkway clearing
   > - Ice melt application
   > - Priority response within 4 hours of snowfall
   >
   > Ready to lock in? Reply to this email or book a quick quote: [Calendar Link — Snow Removal Quote]
   >
   > [Owner Name]

3. **Send SMS** (August 15)
   > "{{contact.firstName}}, it's not too early to think about snow! ❄️ We're booking seasonal snow removal contracts now. Early birds lock in best pricing and route priority. Interested?"

4. **Wait:** 12 days

5. **Send Email** (August 27)
   - **Subject:** "Last chance for early bird snow removal pricing"
   - **Body:** Brief urgency email, fewer words, strong CTA

6. **Send SMS** (September 5)
   > "{{contact.firstName}}, our snow removal routes are filling in fast. Seasonal contracts will close soon — want to lock in before we go per-push only? [Calendar Link]"

7. **Wait:** 20 days

8. **Send SMS** (September 25 — final)
   > "{{contact.firstName}}, final call for snow removal contracts! Once we're full, no more seasonal pricing. Last chance to lock in guaranteed winter coverage."

---

### Workflow 9: Snow Contract Renewal (September Annual)
**Trigger:** Scheduler (September 1 annually)
**Audience:** Contacts tagged `snow-removal` with Snow Contract Renewal Date set in next 60 days

**Actions:**

1. **Send Email**
   - **Subject:** "Your snow removal contract renewal — [Year–Year] season"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Your snow removal contract with [Company Name] is up for renewal for the coming winter season!
   >
   > We'd love to keep you on our route. To confirm your renewal, simply reply to this email or sign your renewal contract: [Contract Link]
   >
   > **Renewal deadline:** October 15 (routes close after this date)
   >
   > Questions? Call [Phone] or reply here.
   >
   > [Owner Name]

2. **Wait:** 14 days

3. **Send SMS**
   > "{{contact.firstName}}, snow season is coming! Ready to renew your snow removal contract? Reply YES and we'll send over your renewal agreement."

---

### Workflow 10: Spring Startup Campaign (Annual — March 1)
**Trigger:** Scheduler (March 1 annually)
**Audience:** All contacts with tag `maintenance-program` OR `job-complete` OR previous season activity

**Actions:**

1. **Send Email** (March 1)
   - **Subject:** "Spring is almost here — book your spring cleanup before we fill up"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Spring is around the corner and [Company Name] is already booking up for the season!
   >
   > 🌱 **Spring Cleanup** — Remove winter debris, edge beds, refresh mulch, first mow
   > 🌿 **Lawn Maintenance Program** — Lock in your full-season mowing + fertilization
   > 🏗️ **New Projects** — Patios, retaining walls, sod installs — book now for May/June start
   >
   > Our spring schedule fills up fast — don't get left out!
   >
   > [Book Now — Calendar Link]
   >
   > [Owner Name]

2. **Send SMS** (March 1)
   > "Hey {{contact.firstName}}! Spring is almost here and our [Month] schedule is filling up 🌱 Want to lock in your spring cleanup or first mow? Book now: [Calendar Link]"

3. **Wait:** 8 days

4. **Send Email** (March 9 — if no booking)
   - **Subject:** "A few spots left for early spring — [City]"
   - **Body:** Shorter urgency email with limited availability angle + CTA

5. **Send SMS** (March 12)
   > "{{contact.firstName}} — just checking in! Did you want to get on the spring schedule? We have a few spots left in your area."

6. **Wait:** 10 days

7. **Send SMS** (March 22 — final spring push)
   > "Last spring outreach from us! If you're ready to book spring cleanup or a maintenance program, click here: [Calendar Link] 🌿"

---

### Workflow 11: Fall Cleanup Campaign (Annual — September 1)
**Trigger:** Scheduler (September 1 annually)
**Audience:** All active clients + contacts tagged `job-complete` or `maintenance-program`

**Actions:**

1. **Send Email** (September 1)
   - **Subject:** "Leaf season is coming — book your fall cleanup before we fill up"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Fall is officially here and [Company Name] is now booking fall cleanup appointments!
   >
   > 🍂 **Fall Cleanup includes:**
   > - Leaf removal and disposal
   > - Final mow cut (lower for winter)
   > - Lawn winterization prep
   > - Garden bed cleanup
   > - Shrub & hedge trimming
   > - Aeration + overseeding (great for spring lawn!)
   >
   > **Plus — while we're thinking ahead:**
   > Are you set for snow removal this winter? We're now booking seasonal snow contracts! Lock in early for best pricing. ❄️
   >
   > Book your fall appointment: [Calendar Link]
   >
   > [Owner Name]

2. **Send SMS** (September 1)
   > "{{contact.firstName}}, fall is almost here! 🍂 We're now booking fall cleanups and leaf removal. Want to grab a spot before we fill up?"

3. **Wait:** 12 days

4. **Send SMS** (September 13)
   > "{{contact.firstName}}, fall cleanup spots are going fast! We have openings [this week/next week] in your area. Want to lock one in?"

5. **Wait:** 9 days

6. **Send SMS** (September 22 — last call)
   > "Last call for fall cleanup, {{contact.firstName}}! October is booking up. If you want your lawn put to bed right before winter, now's the time 🍂 [Calendar Link]"

---

### Workflow 12: Aeration & Overseeding Campaign (Late Summer)
**Trigger:** Scheduler (August 20 recommended)
**Audience:** Contacts tagged `maintenance-program` or `lawn-maintenance`

**Actions:**

1. **Send SMS**
   > "{{contact.firstName}}, late summer is the perfect time for lawn aeration and overseeding! It's the single best thing you can do to thicken your lawn before winter. Want us to add it to your next visit? 🌱"

2. **Wait:** 3 days

3. **Send Email**
   - **Subject:** "The best thing you can do for your lawn before winter — aeration & overseeding"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > If there's one service we'd recommend every homeowner does this time of year, it's **aeration and overseeding**.
   >
   > **Why now?**
   > Late summer/early fall is prime time — the soil is warm, moisture is increasing, and new grass has all fall to establish roots before winter.
   >
   > **What you get:**
   > ✅ Reduced compaction (better water + nutrient absorption)
   > ✅ Thicker, denser lawn next spring
   > ✅ Crowds out weeds naturally
   > ✅ Fills in thin or bare patches
   >
   > We can add this to your next scheduled visit or book a standalone appointment.
   >
   > Interested? Reply here or call [Phone].
   >
   > [Owner Name]

4. **Wait:** 5 days

5. **Send SMS** (follow-up)
   > "{{contact.firstName}}, quick follow-up on aeration & overseeding! Want to add it to your fall service? We have openings this week. [Calendar Link]"

---

### Workflow 13: Post-Job Review Request (Happy Path)
**Trigger:** Pipeline stage changed (filter: new stage = Review Requested) OR Contact tag (filter: tag added = review-requested)
**Filter:** Only if Review Requested field ≠ "Yes" (prevent duplicates)

**Actions:**

1. **Update Custom Field:** Review Requested = "Yes"

2. **Send SMS** (immediate)
   > "Hi {{contact.firstName}}! We just wrapped up at your property — hope everything looks great! Could you take 30 seconds to leave us a Google review? It means the world to small local businesses like ours 🌿 [Google Review Link]"

3. **Wait:** 1 day

4. **Send Email**
   - **Subject:** "How did we do, {{contact.firstName}}?"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Thanks so much for choosing [Company Name]! We hope you're happy with the work.
   >
   > If you have a quick minute, a Google review would mean the world to our small team — it's the #1 way local families find us, and it takes less than 60 seconds:
   >
   > ⭐ [Leave a Google Review — Direct Link]
   >
   > Thank you from the whole crew!
   > [Owner Name]

5. **Wait:** 3 days

6. **Send SMS** (if no review yet)
   > "{{contact.firstName}}, if you had a moment, a quick Google review would really help us out! Takes less than a minute: [Review Link] 🌿"

---

### Workflow 14: Unhappy Customer Recovery (Internal Alert Only)
**Trigger:** Customer replied (with keyword filter: unhappy, not happy, disappointed, problem)

**Actions:**

1. **Add Tag:** `cold-lead`

2. **Create Task** → "⚠️ URGENT: Unhappy customer — call {{contact.name}} within 24 hours" → Assign to owner → High priority

3. **Send Internal Notification** (to owner)
   > "Unhappy customer alert! {{contact.name}} ({{contact.phone}}) has indicated dissatisfaction. Call them today."

4. **DO NOT send to Google review.** End workflow.

**Note:** This workflow should NOT be connected to the review request flow in a way that auto-routes. It should monitor incoming replies/conversations only.

---

### Workflow 15: Referral Request (7 Days Post Review)
**Trigger:** Contact tag (filter: tag added = review-received)

**Actions:**

1. **Wait:** 7 days

2. **Send SMS**
   > "{{contact.firstName}}, thanks so much for your review — it really helps! 🙌 Do you know anyone else who might benefit from our lawn care or landscaping services? If they book with us, we'll send you a thank-you gift as our way of saying thanks!"

3. **Send Email**
   - **Subject:** "Got a friend or neighbor who needs their lawn looked after?"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > Thank you again for your kind Google review — it means so much to our team!
   >
   > If you know anyone in [City] who could use our help — whether it's lawn maintenance, a spring/fall cleanup, or a hardscape project — we'd love to work with them.
   >
   > **Our referral program:** Send a friend our way, and when they complete their first service, we'll send you a [discount/gift card] as a thank-you.
   >
   > Just reply to this email with their name and contact info, or forward them our booking link: [Calendar Link]
   >
   > Thanks again!
   > [Owner Name]

---

### Workflow 16: Neighbour Campaign (Post Exterior/Hardscape Job)
**Trigger:** Pipeline stage changed (filter: new stage = Review + Referral, Pipeline: Landscaping - Hardscape Project) OR Contact tag (filter: tag added = job-complete AND tag added = hardscape-project)

**Actions:**

1. **Add Tag:** `neighbour-campaign`

2. **Update Custom Field:** Neighbour Campaign Sent = "Yes"

3. **Send SMS to Contact**
   > "{{contact.firstName}}, your new [interlock / retaining wall / sod] looks incredible! 🌿 We'd love to work with your neighbors too — would you be open to us putting a small lawn sign in front for a few days? It's totally optional!"

4. **Create Task** → "Neighbour campaign — send targeted SMS to {{contact.address1}} postal code contacts" → Assign to rep

5. **Internal notification to owner:**
   > "Neighbour campaign trigger: Job complete at {{contact.address1}}. Pull contacts in same postal code and send targeted outreach: 'Hi [FirstName] — we just completed a [project type] on your street. While our crew is in the area, we're offering FREE estimates. Interested? [Calendar Link]'"

**Note:** The actual neighbour SMS blast should be done manually or via a smart list filtered by postal code, due to GHL limitations on geo-targeting automation.

---

### Workflow 17: Commercial / HOA Outreach Sequence
**Trigger:** Contact tag (filter: tag added = commercial-account) OR Contact created (with Property Type = Commercial or HOA/Condo)

**Actions:**

1. **Create Opportunity** → Pipeline: Landscaping - Commercial / HOA → Stage: New Prospect

2. **Create Task** → "Call {{contact.name}} — commercial landscaping inquiry" → Due: Same day

3. **Send Email** (next day if no call booked)
   - **Subject:** "Commercial Landscape Maintenance — [Company Name]"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > I'm [Owner Name] from [Company Name]. We specialize in commercial landscape maintenance for property managers, HOAs, and commercial property owners in [Area].
   >
   > We currently maintain [X] properties in your area, including [examples if applicable].
   >
   > Our commercial program includes:
   > ✅ Dedicated crew assigned to your properties
   > ✅ Seasonal maintenance schedule (spring through fall)
   > ✅ Snow removal contracts available
   > ✅ Fully insured + WSIB coverage
   > ✅ Monthly reporting and account manager contact
   >
   > I'd love to schedule a quick site walk to understand your needs and put together a proposal.
   >
   > Are you available for a 30-minute call this week?
   >
   > [Owner Name] | [Phone] | [Company Name]

4. **Wait:** 5 days

5. **Send SMS** (if no response)
   > "Hi {{contact.firstName}}, following up on my email about commercial landscaping services for [Property/Company Name]. Happy to do a quick site walk — would this week work? [Calendar Link — Commercial Site Walk]"

6. **Wait:** 7 days

7. **Send Email** (final commercial outreach)
   - **Subject:** "One more reach-out — commercial landscape maintenance for [Company]"
   - **Body:** Brief, professional, reference the site walk offer, include contact info

8. **Create Task** → "Final commercial follow-up sent — move to cold if no response in 3 days"

---

### Workflow 18: 30-Day Cold Lead Re-Engagement
**Trigger:** Contact tag (filter: tag added = cold-lead) OR Pipeline stage changed (filter: new stage = Lost) → Wait 30 days
**Also fires:** Scheduler (April 1 annually) for all `cold-lead` tagged contacts

**Actions:**

1. **Wait:** 30 days from trigger

2. **Send SMS**
   > "Hi {{contact.firstName}}, it's been a while since we connected! Spring/summer is a great time to get your property looking its best. Are you still thinking about [landscaping / lawn care / your project]?"

3. **Wait:** 3 days

4. **Send Email**
   - **Subject:** "Still thinking about your lawn or landscaping project, {{contact.firstName}}?"
   - **Body:**
   > Hi {{contact.firstName}},
   >
   > We haven't heard from you in a while — and we wanted to check in!
   >
   > Whether you're looking for a full-season lawn maintenance program, a spring/fall cleanup, or a bigger project like a patio or retaining wall — we'd love to get out and take a look.
   >
   > We have openings in your area right now, and our schedule fills up quickly as the season heats up.
   >
   > Click here to book a free estimate: [Calendar Link]
   >
   > No pressure — just wanted to reach out!
   >
   > [Owner Name]

5. **Wait:** 7 days

6. **Send SMS** (final)
   > "{{contact.firstName}}, last note from us! If the timing isn't right, totally understood — we'll be here when you need us. You can always reach us at [Phone] or [Website]. 🌿"

7. **Remove Tag:** `cold-lead` → Add Tag: `cold-lead-final` → End workflow

---

## SUMMARY: ALL CREATED ASSETS

### Custom Fields (17)
| Field | ID |
|-------|-----|
| Lead Source | `1GtmxLcjnSyuOiv64dit` |
| Job Type | `YYOl44lKQKtaiCyJewp7` |
| Service Category | `wRFVGJFzwJ1DqeaQ2f88` |
| Property Type | `xTRPs34uA9RPL0ZjM6Mc` |
| Lot Size | `oHHXPMooXLDWyAz4ggnF` |
| Maintenance Program Tier | `NNEkSGJXu403ht8UJMug` |
| Program Start Date | `GEdacqBCLvKWeJ4qGlD9` |
| Program Renewal Date | `TQJ5MbsblawdBnTRNy5H` |
| Snow Removal Contract | `xoVKLwZAsTUgKlA1Zc7q` |
| Snow Contract Renewal Date | `9104jq5VowAmtv5uNFJl` |
| Irrigation System Present | `mH7zHGvDuFH8kIbAelsR` |
| Estimate Amount | `1zOzoCy34nIwIFRdIfVf` |
| Contract Amount | `TvjcpHPSHVrNrNoF6JUG` |
| Crew Assigned | `t2WvcE866lLrStb4VZDz` |
| Review Requested | `xk9YiiTnlaL20g3XwpfV` |
| Review Received | `qlQ02aYlBEnnq3JfyPgC` |
| Neighbour Campaign Sent | `IKLI5j3If8wROBHVJBBB` |

### Pipelines (5)
| Pipeline | ID |
|----------|-----|
| Landscaping - Residential Estimate | `ZfYs9Xe0rvneMbhh9l0I` |
| Landscaping - Maintenance Program | `OAT9ARKa97VlkTIihkpH` |
| Landscaping - Hardscape Project | `3S37TBBoh8rtG5Tif2CR` |
| Landscaping - Snow Removal | `VH4Rvyxiz9P9ud4dzKB5` |
| Landscaping - Commercial / HOA | `IriZABT2NhsLRIHaEW6j` |

### Calendars (4)
| Calendar | Duration | ID |
|----------|----------|-----|
| Free Estimate - Landscaping | 45 min | `ys3xUSWsdDxSwsGTdejc` |
| Hardscape Design Consultation | 60 min | `LtMQOBRVQk0VZAdbBQfi` |
| Commercial Site Walk | 60 min | `xd3fMLzY8xGKAebdLh4P` |
| Snow Removal Quote | 30 min | `dIfoDzAud1OwHLY4dzrH` |

### Tags (30)
All 30 tags created — see Phase 4 table above for full ID list.

### Workflows (18) — Build Specs Documented
All 18 workflow specs are fully documented above. Build manually in GHL → Automation → Workflows.

---

## MANUAL COMPLETION TASKS

The following items require manual completion in the GHL UI:

1. **Calendar Availability Hours** — Set Mon–Fri 8am–5pm (Free Estimate, Snow Removal), Mon–Fri 8am–4pm (Hardscape, Commercial Site Walk) in each calendar's availability settings
2. **Workflow Build** — Build all 18 workflows using the specs above (GHL API does not support workflow creation)
3. **Google Review Link** — Add client's actual Google Review URL to review request workflows
4. **Calendar Booking Links** — Add actual booking URLs from each calendar into workflow SMS/email templates
5. **Company Name / Owner Name / Phone** — Replace all placeholders with client's real info during onboarding
6. **Workflow Phone Number** — Assign a GHL phone number for SMS sends
7. **Delete "Marketing Pipeline"** — The default pipeline created with the sub-account can be deleted or kept for internal use

---

*Build log generated by Maximus AI Subagent*
*Location: YJTZd59YCy0mHJih0K6j — landscaping (Peterborough, ON)*
