# 🏊 Pool & Spa GHL Snapshot — Build Log
**Location ID:** lqHFFe4zxaoMPysaTPAQ
**Built by:** Maximus Subagent
**Date:** 2026-07-21
**Status:** COMPLETE ✅

---

## Summary

Full GHL pool and spa snapshot built via REST API (MCP search returned empty results — fell back to direct REST API as instructed). All phases complete.

---

## PHASE 1: CUSTOM FIELDS ✅ (20/20)

All 20 custom fields created under `contact` model.

| # | Field Name | Type | Options / Notes | GHL ID |
|---|---|---|---|---|
| 1 | Lead Source | SINGLE_OPTIONS (dropdown) | Google LSA, Google Organic, Referral, New Home Builder, Real Estate Agent, Facebook/Instagram, Repeat Customer, Property Manager | Rr7UrNslMEpXTaIYkdni |
| 2 | Job Type | SINGLE_OPTIONS (dropdown) | Pool Opening, Pool Closing/Winterization, Weekly Maintenance, Equipment Repair, Equipment Replacement, New Pool Install, Hot Tub Service, Hot Tub Install, Water Chemistry, Liner Replacement | vdmfTDwaNpCkZEu26JKO |
| 3 | Service Category | SINGLE_OPTIONS (dropdown) | Seasonal Opening/Closing, Weekly Maintenance, Equipment Service, New Install, Hot Tub/Spa, Commercial | T4j8Dv2NENnBLJURihwP |
| 4 | Pool Type | SINGLE_OPTIONS (dropdown) | Inground Concrete, Inground Vinyl Liner, Inground Fiberglass, Above Ground, Hot Tub/Spa, Unknown | KSPe6aZUE6TCnftQtml0 |
| 5 | Pool Size | SINGLE_OPTIONS (dropdown) | Under 10,000 gal, 10,000-20,000 gal, 20,000-30,000 gal, 30,000+ gal, Unknown | S5YMjcAEcNdYOHm5MJri |
| 6 | Equipment Age | SINGLE_OPTIONS (dropdown) | Under 5 years, 5-10 years, 10-15 years, 15+ years, Unknown | G8QnWrv1VvEwwzFNcZ92 |
| 7 | Salt System | RADIO | Yes / No | br8fm0n34HbSxCJuEo2X |
| 8 | Heater Type | SINGLE_OPTIONS (dropdown) | Gas, Heat Pump, Electric, Solar, None, Unknown | yE6KdPISTklnituotwUo |
| 9 | Maintenance Plan Active | RADIO | Yes / No | bUBP9QwEqIPXAnXJSqLY |
| 10 | Plan Tier | SINGLE_OPTIONS (dropdown) | None, Basic, Standard, Premium | nl7WP98rLSz1EZsHqDgg |
| 11 | Plan Start Date | DATE | — | 9aJAecWkOTtrm2IVIPx1 |
| 12 | Plan Renewal Date | DATE | — | F5PwT5ggsUYbIJ4Io0NY |
| 13 | Opening Date | DATE | — | N982cOcHGhRnGdR5uITK |
| 14 | Closing Date | DATE | — | jwkgdZMqVX4EgnanWj42 |
| 15 | Estimate Amount | MONETORY | Currency field | TnuXvqX9w8o8K9n0DitE |
| 16 | Invoice Amount | MONETORY | Currency field | MPqsFDG3BX3rkOJAZGbC |
| 17 | Technician Assigned | TEXT | Free text | kzmJLkbw8Vo4CHX2aPm9 |
| 18 | Review Requested | RADIO | Yes / No | ZzJ0SqDntRSmPctbOUMp |
| 19 | Review Received | RADIO | Yes / No | lukWbbrxhKnpMV73ay2u |
| 20 | Equipment Replacement Candidate | RADIO | Yes / No | 2zgfRmcCRMoMJPbIXuhv |

**Note:** GHL API uses `SINGLE_OPTIONS` for dropdown fields, `RADIO` for Yes/No binary choices, and `MONETORY` (GHL's spelling) for currency fields. `DROPDOWN` is not a valid GHL API dataType.

---

## PHASE 2: PIPELINES ✅ (6/6)

### Pipeline 1: Pool - Spring Opening
**ID:** aOVLeGUANhiKgH9cVcn5
**Stages (8):**
1. Opening Request
2. Scheduled
3. Confirmed
4. Opening Complete
5. Chemical Balance Check
6. Invoice Sent
7. Paid
8. Maintenance Upsell

**Purpose:** Manage spring pool opening season (Feb–June). Primary annual revenue event. After "Paid," move qualified leads to "Maintenance Upsell" and trigger maintenance program pitch.

---

### Pipeline 2: Pool - Weekly Maintenance
**ID:** vPC6Rv05K5u7k9RCmmzc
**Stages (9):**
1. Prospect
2. Trial Visit Scheduled
3. Trial Complete
4. Plan Proposal Sent
5. Plan Active
6. At Risk
7. Renewal Sent
8. Renewed
9. Cancelled

**Purpose:** Highest-LTV pipeline. Track recurring maintenance customers from inquiry through multi-season retention. "At Risk" stage triggers service recovery workflow.

---

### Pipeline 3: Pool - Equipment Repair/Replacement
**ID:** gb5UFvCBxV6L14GktdGm
**Stages (10):**
1. New Service Call
2. Diagnosis Scheduled
3. Diagnosis Complete
4. Parts Ordered
5. Repair Scheduled
6. Repair Complete
7. Invoice Sent
8. Paid
9. Review Requested
10. Replacement Upsell

**Purpose:** Manage reactive service calls and proactive equipment replacement campaigns. "Replacement Upsell" stage triggers equipment age campaign.

---

### Pipeline 4: Pool - New Install
**ID:** PLvhhGWuPaXbCzm8KUT9
**Stages (15):**
1. New Inquiry
2. Design Consultation
3. Proposal Sent
4. Follow-Up Active
5. Contract Signed / Deposit
6. Permit Applied
7. Excavation
8. Shell/Form
9. Plumbing/Electric
10. Decking
11. Finish/Fill
12. Startup
13. Final Invoice
14. Paid
15. Review + Referral

**Purpose:** Track new pool and major renovation installs from inquiry to completed build. Longest pipeline — full construction lifecycle. Highest ticket ($35K–$120K+).

---

### Pipeline 5: Pool - Fall Closing
**ID:** Hlu86BYGmUOVKs1UluP3
**Stages (8):**
1. Closing Request
2. Scheduled
3. Confirmed
4. Closing Complete
5. Winterization Done
6. Invoice Sent
7. Paid
8. Spring Opening Pre-Book

**Purpose:** Manage fall closing season (Aug–Nov). "Spring Opening Pre-Book" stage is the key upsell — lock in next year's opening booking at the point of closing.

---

### Pipeline 6: Pool - Hot Tub / Spa
**ID:** I8xUA14Bei1N4FrMaPe3
**Stages (11):**
1. New Inquiry
2. Demo/Showroom
3. Proposal Sent
4. Follow-Up
5. Contract Signed
6. Delivery Scheduled
7. Install Complete
8. Water Balance
9. Invoice Sent
10. Paid
11. Service Plan Upsell

**Purpose:** Separate pipeline for hot tub/spa sales and service. Year-round revenue stream — spas run 12 months. "Service Plan Upsell" triggers ongoing chemical delivery and maintenance program.

---

## PHASE 3: CALENDARS ✅ (4/4)

| # | Calendar Name | Duration | Hours | GHL ID |
|---|---|---|---|---|
| 1 | Pool Opening Appointment | 90 min | Mon–Sat 8am–5pm | zXtukzRNE7jzFOVU8tSX |
| 2 | Pool Closing Appointment | 90 min | Mon–Sat 8am–5pm | qs5iHYp14u5wn6J3rZjS |
| 3 | Equipment Service Call | 60 min | Mon–Fri 8am–5pm | WgnpiLaolN1om3gTs4KW |
| 4 | New Pool/Hot Tub Consultation | 60 min | Mon–Fri 9am–4pm | dBoJ6Y9goU4xJBsiQg99 |

**Note:** GHL calendar API does not accept `openHours` array via REST API (returns 422 "must be a valid day of week"). Hours and capacity limits must be configured manually in GHL UI after creation. Calendar shells are live and bookable.

---

## PHASE 4: TAGS ✅ (32/32)

All 32 tags created:

| Tag | ID |
|---|---|
| new-lead | iWOUU4Oj4Y35JLlf5l3J |
| pool-opening | DF7rHjOWzaAahYzcOY2a |
| pool-closing | AjRoMz1bi1m0GKmtGBtl |
| weekly-maintenance | Drq8N60grC9A6R5TmHsR |
| equipment-repair | jJ4YNLST5Yss6JkkLTJd |
| equipment-replacement | 84c94L4m8LY3E92NM1lx |
| new-pool-install | S0rGxevtreIItQNI6jsm |
| hot-tub | BX4WeGwHTVVds4PH4CFb |
| liner-replacement | UrxTYZ3UvkgQl7EDz3ia |
| salt-system | qJJSYIN5LHOmKbdnIcJF |
| aging-equipment-10yr | cJlcvluhg9Y2XTBRAhIq |
| aging-equipment-15yr | xW1pwzwUbVbM9EVcMEmb |
| maintenance-plan-active | GbOvB6B1Z6yZcCgp0xse |
| plan-renewal-due | juVzBDAh9j6HrzKcioTi |
| equipment-replacement-candidate | UhTgJbtYmdXxEVgbMUAw |
| spring-campaign | X5Ynoc28zhOFYRA1sKul |
| fall-campaign | B7mlMHgruRAv6SihU0SZ |
| chemical-service | GZx0TCRa3SMcxkzDtcOx |
| estimate-sent | jJxiW8ql5jdwbRirxmGn |
| contract-signed | iikGeYLBOWk9eSYhsWNP |
| job-complete | fGcSrOdiqV1xDtrAtV9R |
| review-requested | ICcXTb8iuo4vB2bmpBNv |
| review-received | hP6dLjY6Kokc5UryIkzx |
| referral | vYjuFmOz31TYOs9K4LrF |
| cold-lead | QmP88DwjM8Qm5gdtMA1W |
| no-show | K0KOT1OXWB7YUUkq38Yr |
| google-lsa | R4Rb5A5cIMrDuNy1kvRt |
| new-home-builder | kKOp7w22uKBYogNHbAuf |
| real-estate-agent | yEKvVIHtAkNN9WNUvr2W |
| repeat-customer | U7tZlO1MEVeNQLYtnPBV |
| facebook-ad | xysGVPvQO9TyZBzB6dd7 |
| property-manager | 0eKKGUxGXuR3kepCEvaL |

---

## PHASE 5: WORKFLOWS — Full Specifications ✅

**Note:** GHL REST API does not support workflow creation. All 10 workflow specs below are complete build instructions for manual creation in the GHL Automations UI, or for use with GHL's internal snapshot export system.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — pool opening, closing, or service needed? Reply YES and we'll get you scheduled right away 👋"

This fires automatically on every missed call. No workflow required.

---

### WORKFLOW 2: Spring Opening Campaign (February Blast)

**Trigger:** Scheduler (February 1 annually)
**Target Audience:** All contacts tagged `pool-opening` OR `repeat-customer` OR `new-lead` (existing customers + past leads)

**Step 1 — Email (Feb 1):**
- **Subject:** "Spring pool opening — book before we fill up (we always do)"
- **Body:**
  > Hi {{contact.firstName}},
  >
  > Every spring, the same thing happens: we go from available to fully booked in about 3 weeks.
  >
  > This year, we're giving our existing customers first access before we open to new clients.
  >
  > Here's what you get with our spring opening service:
  > ✅ Full equipment reinstall and startup
  > ✅ Water chemistry test (pH, chlorine, alkalinity, stabilizer, calcium)
  > ✅ Chemical startup treatment
  > ✅ Equipment inspection — pump, filter, heater, salt system
  > ✅ Written report card on your pool's condition
  >
  > **[BOOK MY SPRING OPENING →]** [calendar link: Pool Opening Appointment]
  >
  > Spots fill fast — book now and we'll take care of the rest.
  >
  > [Business Name]

**Step 2 — SMS (Feb 7):**
> "Hey {{contact.firstName}}! 🌊 Spots filling fast! Book your pool opening now before we're full: [BOOKING LINK] — [Business Name]"

**Step 3 — Add Tag:** `spring-campaign`

**Step 4 — Wait:** 14 days

**Step 5 — Condition:** Has contact booked?
- If NO → **Email (Feb 15):**
  - **Subject:** "⚡ Only a few May opening spots left"
  - Urgency email with early-bird pricing mention: "Book before March 1 — save $25 on your opening"
  - CTA: [BOOK NOW]

**Step 6 — Wait:** 14 days

**Step 7 — Condition:** Has contact booked?
- If NO → **SMS (Mar 1):**
  > "Last call for early-bird spring opening pricing. Book by Friday to lock in your spot: [LINK]"

**Step 8 — Wait:** 30 days

**Step 9 — Condition:** Has contact booked?
- If NO → **SMS (Apr 1):**
  > "Spring is here {{contact.firstName}}! Confirm your opening: [LINK] 🌊 — [Business Name]"
- If YES → **End workflow**

**Step 10 — Wait:** 30 days

**Step 11 — Condition:** Has contact booked?
- If NO → **Add Tag:** `cold-lead`, **Remove Tag:** `spring-campaign`
- If YES → **End workflow**

---

### WORKFLOW 3: Opening Appointment Confirmation

**Trigger:** Customer booked appointment (calendar: Pool Opening Appointment)

**Step 1 — Immediate SMS:**
> "Hi {{contact.firstName}}! Your pool opening is confirmed for {{appointment.startTime}}. We'll have your pool up and running! 🌊 Reply with any questions. — [Business Name]"

**Step 2 — Immediate Email:**
- **Subject:** "Pool opening confirmed — here's what to do before we arrive"
- **Body:**
  > Hi {{contact.firstName}},
  >
  > Your pool opening appointment is confirmed for:
  > 📅 **{{appointment.startTime}}**
  >
  > **Before we arrive, please:**
  > 1. Remove winter cover anchors/water bags (leave the cover for us to remove)
  > 2. Clear the deck area around the equipment pad
  > 3. Make sure the water source (garden hose) is accessible
  > 4. If you have a safety cover, locate the cover reel/handle
  > 5. Ensure gate or pool area is accessible to our tech
  >
  > **Questions?** Reply to this email or text us at [Business Phone].
  >
  > We'll see you soon!
  > [Business Name]

**Step 3 — Add Tag:** `pool-opening`

**Step 4 — Wait until 24 hours before appointment:**
**SMS:**
> "Reminder: Your pool opening is tomorrow at {{appointment.startTime}}. Tech: {{appointment.assignedUser}}. Any last questions? Reply here! — [Business Name]"

**Step 5 — Wait until 2 hours before appointment:**
**SMS:**
> "We're on our way soon, {{contact.firstName}}! Your pool opening is today at {{appointment.startTime}}. 🌊 — [Business Name]"

---

### WORKFLOW 4: Post-Opening Review + Maintenance Plan Upsell

**Trigger:** Pipeline stage changed (filter: new stage = Paid, Pool - Spring Opening pipeline)

**Step 1 — Wait:** 24 hours
**Step 2 — SMS:**
> "Hi {{contact.firstName}}! Hope you're enjoying your pool! On a scale of 1–5, how did our opening service go? Reply with a number 🌊"

**Step 3 — Condition:** Branch on reply value
- **Rating 4 or 5:**
  - **SMS:**
    > "So glad to hear it! 🙌 A Google review means the world to us — takes 60 seconds: [GOOGLE REVIEW LINK]"
  - **Add Tag:** `review-requested`
  - **Set Custom Field:** Review Requested = Yes
- **Rating 1, 2, or 3:**
  - **SMS:**
    > "We're sorry to hear that! Can you tell us what happened? Our owner wants to make it right."
  - **Internal Notification to Owner:** "⚠️ Service recovery needed: {{contact.name}} rated {{rating}}/5 — respond within 24hrs"
  - **Create Task:** "Call {{contact.name}} — low rating service recovery"

**Step 4 — Wait:** 5 days (all branches)
**Step 5 — SMS (Maintenance Upsell):**
> "Hey {{contact.firstName}}! Now that your pool is open, have you thought about weekly maintenance? We handle all the chemistry so you just swim. Want a quick quote? Reply YES! — [Business Name]"

**Step 6 — Condition:** Contact replies YES?
- YES → **Move to Pool - Weekly Maintenance pipeline (Prospect stage)**, **Create Task:** "Call {{contact.name}} — maintenance program interest"
- NO → **Add Tag:** `cold-lead` for maintenance, **Wait 30 days**, **Send one final maintenance offer email**

---

### WORKFLOW 5: Equipment Age Trigger — 10 Year

**Trigger:** Contact changed (filter: Equipment Age field updated to 10-15 years) OR Contact tag (filter: tag added = aging-equipment-10yr)

**Step 1 — Add Tag:** `aging-equipment-10yr`, `equipment-replacement-candidate`
**Step 2 — Set Custom Field:** Equipment Replacement Candidate = Yes

**Step 3 — Email (Day 1):**
- **Subject:** "Your pool equipment is 10+ years old — what you need to know"
- **Body:**
  > Hi {{contact.firstName}},
  >
  > Pool equipment has a lifespan. At 10+ years, your system is entering the zone where components start to fail — usually at the worst possible moment (July 4th, anyone?).
  >
  > Here's the honest timeline for common equipment:
  > 🔵 **Pump:** 8–12 years — if single-speed, upgrading to variable-speed saves 60–80% on electricity
  > 🔵 **Filter:** Sand needs replacing every 5–7 years (cartridge media every 3–5)
  > 🔵 **Heater:** 8–15 years — gas heaters often go without warning
  > 🔵 **Salt cell:** 3–5 years — if your salt readings are off, the cell may be failing
  > 🔵 **Automation system:** 10–15 years — older units lose compatibility with modern equipment
  >
  > **The smart move:** A proactive equipment assessment now costs nothing. An emergency replacement in July costs double in labour and lost swimming time.
  >
  > **[BOOK A FREE EQUIPMENT ASSESSMENT →]** [Equipment Service Call calendar]
  >
  > [Business Name]

**Step 4 — Wait:** 14 days
**Step 5 — SMS:**
> "Hi {{contact.firstName}}! Quick follow-up — we noticed your equipment is in the 10-year range. Want us to check it out at your next service? We'll give you an honest assessment. — [Business Name]"

**Step 6 — Wait:** 30 days
**Step 7 — Email:**
- **Subject:** "Variable-speed pump upgrade — the numbers that make it obvious"
- Educational content on VSP energy savings + quote CTA

---

### WORKFLOW 6: Equipment Age Trigger — 15 Year (Urgent Replacement Campaign)

**Trigger:** Contact changed (filter: Equipment Age field updated to 15+ years) OR Contact tag (filter: tag added = aging-equipment-15yr)

**Step 1 — Add Tag:** `aging-equipment-15yr`, `equipment-replacement-candidate`
**Step 2 — Set Custom Field:** Equipment Replacement Candidate = Yes

**Step 3 — SMS (Immediate — more urgent tone):**
> "Hi {{contact.firstName}}, quick heads up — equipment at 15+ years is past its expected lifespan. A proactive replacement is always cheaper than an emergency one. Can we schedule a quick assessment? — [Business Name]"

**Step 4 — Email (Day 1):**
- **Subject:** "⚠️ 15-year equipment alert — what to watch for this season"
- Urgent but educational tone
- Specific failure signs: loud bearing noise, tripping breaker, low pressure, visible rust/corrosion, pilot won't stay lit
- **CTA:** [BOOK EQUIPMENT ASSESSMENT — PRIORITY BOOKING]

**Step 5 — Wait:** 7 days
**Step 6 — SMS:**
> "{{contact.firstName}}, have you noticed any changes in your pump/heater performance? Equipment at 15+ years can fail without warning. Let us assess before season — reply YES to book. — [Business Name]"

**Step 7 — Wait:** 14 days
**Step 8 — Email:**
- Final urgent pitch with specific replacement pricing estimates
- Financing option mention if applicable
- **CTA:** Call us directly or book online

---

### WORKFLOW 7: Fall Closing Campaign

**Trigger:** Scheduler (August 15 annually)
**Target:** All contacts tagged `pool-opening` OR `pool-closing` OR `repeat-customer`

**Step 1 — Email (Aug 15):**
- **Subject:** "Fall pool closing — book early, avoid the wait"
- **Body:**
  > Hi {{contact.firstName}},
  >
  > The same crush that happens in spring for openings? It happens again in fall for closings. October books solid in about 3 weeks.
  >
  > Book your closing now and:
  > ✅ Pick your preferred date (vs. taking what's left in October)
  > ✅ Add winterization services at the same visit
  > ✅ Lock in your 2027 spring opening date while we're at your pool
  >
  > **[BOOK MY POOL CLOSING →]** [Pool Closing Appointment calendar]
  >
  > [Business Name]

**Step 2 — Add Tag:** `fall-campaign`

**Step 3 — Wait:** 14 days

**Step 4 — SMS (Sep 1):**
> "Hey {{contact.firstName}}! 🍂 Time to think about closing. We book out fast in October — grab your spot now: [BOOKING LINK] — [Business Name]"

**Step 5 — Wait:** 14 days

**Step 6 — Condition:** Booked?
- NO → **Email (Sep 15):** Deep-dive closing education email (what proper winterization includes, freeze damage risks)
- YES → **End workflow**

**Step 7 — Wait:** 14 days

**Step 8 — Condition:** Booked?
- NO → **SMS (Oct 1):**
  > "Oct is here — we're filling up for closings. Don't get left scrambling in November! [LINK]"
- YES → **End workflow**

**Step 9 — Wait:** 14 days

**Step 10 — Condition:** Booked?
- NO → **SMS (Oct 15):** Final urgency push — "Last spots available"
- YES → **End workflow**

---

### WORKFLOW 8: Closing Appointment Confirmation + Spring Pre-Book

**Trigger:** Customer booked appointment (calendar: Pool Closing Appointment)

**Step 1 — Immediate SMS:**
> "Hi {{contact.firstName}}! Your pool closing is confirmed for {{appointment.startTime}}. We'll make sure your pool is perfectly protected for winter. 🍂 — [Business Name]"

**Step 2 — Immediate Email:**
- **Subject:** "Pool closing confirmed — prep guide inside"
- **Body:**
  > Your closing appointment: **{{appointment.startTime}}**
  >
  > **Before we arrive:**
  > 1. Run your pump until we get there (keep water circulating)
  > 2. Have the cover ready and accessible
  > 3. Note any issues you want us to look at
  > 4. If you have a safety cover, locate the cover straps and anchors
  >
  > **We will handle:**
  > ✅ Lower water below skimmer level
  > ✅ Blow out all lines and add antifreeze
  > ✅ Bypass and winterize equipment
  > ✅ Install skimmer plugs and Gizzmos
  > ✅ Install your cover
  > ✅ Balance winter chemicals
  >
  > **While we're there:** We can lock in your 2027 spring opening date — no additional charge, first priority.
  >
  > [Business Name]

**Step 3 — Add Tag:** `pool-closing`

**Step 4 — Wait:** 24 hours before appointment
**SMS:** Standard reminder with tech name

**Step 5 — Wait:** After appointment (trigger on opportunity moved to "Closing Complete"):

**Step 6 — SMS (Spring Pre-Book):**
> "Great news — your pool is perfectly closed for winter! 🌨️ Want to lock in your spring opening date NOW while we're thinking about it? We fill up fast in May. Reply YES and we'll save you a spot. — [Business Name]"

**Step 7 — Condition:** Replied YES?
- YES → **Create Task:** "Book spring opening for {{contact.name}} — requested via closing follow-up", **Move opportunity to "Spring Opening Pre-Book" stage**
- NO → **Wait 30 days**, **Email:** Off-season nurture email #1

---

### WORKFLOW 9: Weekly Maintenance Plan Renewal

**Trigger:** Custom date reminder (select Plan Renewal Date field, set 60 days before)

**Step 1 — Email (60 days before renewal):**
- **Subject:** "Your maintenance plan renews in 60 days — here's what's new"
- **Body:**
  > Hi {{contact.firstName}},
  >
  > Your pool maintenance plan is up for renewal in 60 days. We'd love to have you back for another season.
  >
  > Last season highlights:
  > - [X] service visits
  > - Zero algae incidents
  > - Crystal clear water all season
  >
  > **Your 2027 plan options:**
  > - **Basic (Bi-weekly):** $[price]/visit
  > - **Standard (Weekly):** $[price]/visit
  > - **Premium (Weekly + Priority):** $[price]/visit
  >
  > **[RENEW MY PLAN →]** [or call us to discuss]
  >
  > [Business Name]

**Step 2 — Add Tag:** `plan-renewal-due`

**Step 3 — Wait:** 30 days

**Step 4 — SMS (30 days before renewal):**
> "Hi {{contact.firstName}}! Your maintenance plan renews in 30 days. Want to lock in your route for next season? Reply YES and we'll confirm your spot. — [Business Name]"

**Step 5 — Wait:** 16 days

**Step 6 — Condition:** Renewed?
- YES → **Remove Tag:** `plan-renewal-due`, **Add Tag:** `maintenance-plan-active`, **Update Plan Renewal Date** for following year
- NO → **SMS (14 days before):**
  > "{{contact.firstName}}, quick heads up — your maintenance plan expires in 2 weeks. Routes fill fast in spring. Want to stay on? Reply YES! — [Business Name]"

**Step 7 — Wait:** 14 days

**Step 8 — Condition:** Renewed?
- YES → Renewal confirmed workflow
- NO → **Create Task:** "Call {{contact.name}} — renewal not confirmed, at risk of churn", **Move to "At Risk" stage in Weekly Maintenance pipeline**

---

### WORKFLOW 10: Hot Tub / Spa Lead Nurture

**Trigger:** Opportunity created (filter: Pool - Hot Tub / Spa pipeline, Stage: New Inquiry) OR Contact tag (filter: tag added = hot-tub)

**Step 1 — Immediate SMS:**
> "Hi {{contact.firstName}}! Thanks for reaching out about hot tubs. There's nothing quite like your own spa in the backyard — especially in a Canadian winter 🛁 Want to book a showroom visit or have us call you? Reply anytime. — [Business Name]"

**Step 2 — Immediate Email:**
- **Subject:** "Hot tub ownership — what it actually looks like day-to-day"
- **Body:** Lifestyle email — not specs, not prices. Paint the picture.
  > Imagine this: It's -15°C outside. The rest of the neighbourhood is frozen. You walk out your back door, step into 104°F water, and spend 20 minutes looking at the stars.
  >
  > That's what hot tub owners actually tell us they love. Not the jets, not the LED lighting — the *ritual*. The 20 minutes of decompression at the end of every day.
  >
  > **Hot tub ownership in real life:**
  > - Average soak time: 20–30 minutes, 3–5x per week
  > - Monthly maintenance: 30–45 minutes (water chemistry + filter rinse)
  > - Energy cost: $30–$80/month depending on model and usage
  > - Lifespan: 15–20 years with proper care
  >
  > We'll walk you through everything — no pressure, no upsell — at a free showroom visit.
  >
  > **[BOOK A SHOWROOM VISIT →]** [New Pool/Hot Tub Consultation calendar]
  >
  > [Business Name]

**Step 3 — Wait:** 3 days

**Step 4 — Condition:** Booked showroom/consultation?
- YES → **Move to "Demo/Showroom" stage**, **End nurture**
- NO → **SMS:**
  > "{{contact.firstName}}, still thinking about a hot tub? We have some new models in the showroom that just arrived. No pressure — just worth a look. Want to come by this week? [LINK]"

**Step 5 — Wait:** 4 days

**Step 6 — Condition:** Booked?
- YES → **Move to "Demo/Showroom" stage**
- NO → **Email:**
  - **Subject:** "The hot tub question we get most: 'Is it really worth it?'"
  - Feature owner testimonials and ROI framing (cost per use vs. going out, family time, stress relief)
  - CTA: "Still curious? Let's talk. No commitment." [Book Call]

**Step 7 — Wait:** 7 days

**Step 8 — Condition:** Booked?
- YES → Move to next stage
- NO → **Add Tag:** `cold-lead`, **Wait 30 days**, **SMS:** Final re-engagement — "Still interested? Summer's coming — best time to get set up is now."

---

## MANUAL CONFIGURATION REQUIRED (Post-Build)

The following items require manual setup in the GHL UI — they cannot be created via REST API:

### Calendars — Business Hours Configuration
Each calendar needs hours set manually:
- **Pool Opening Appointment:** Mon–Sat 8am–5pm
- **Pool Closing Appointment:** Mon–Sat 8am–5pm
- **Equipment Service Call:** Mon–Fri 8am–5pm
- **New Pool/Hot Tub Consultation:** Mon–Fri 9am–4pm

### Calendars — Reminders
Set in each calendar's settings:
- 72 hours before: Email reminder
- 24 hours before: SMS reminder
- 2 hours before: SMS reminder

### Calendars — Technician Assignment
Add team members to each calendar with capacity limits:
- Suggested: max 4 openings/day per 2-person crew
- Buffer time: 30 min between slots on same technician

### Workflows
All 10 workflows documented above must be built manually in GHL Automations (Marketing → Automations → New Workflow).

### Pipeline — Existing "Marketing Pipeline"
A default "Marketing Pipeline" (ID: aFoCn3OO1zFV1G7uLK5C) was pre-existing in the sub-account. This can be kept for general lead capture or repurposed/deleted by the client.

---

## API NOTES FOR FUTURE REFERENCE

- **Custom field dataTypes available:** TEXT, LARGE_TEXT, NUMERICAL, PHONE, MONETORY, CHECKBOX, SINGLE_OPTIONS, MULTIPLE_OPTIONS, FLOAT, TIME, DATE, TEXTBOX_LIST, FILE_UPLOAD, SIGNATURE, RADIO
- **Dropdown fields:** Use `SINGLE_OPTIONS` with `"options": ["val1", "val2"]` (string array)
- **Yes/No fields:** Use `RADIO` with `"options": ["Yes", "No"]`
- **Currency fields:** Use `MONETORY` (GHL's spelling — not MONETARY)
- **Pipelines:** Must include `locationId` in the POST body
- **Calendar open hours:** Cannot be set via API — must configure in UI
- **Workflows:** Cannot be created via API — build manually in UI
- **MCP server gohighlevel-pool-spa-template:** search_operations returned empty for all queries — fell back to direct REST API

---

## BUILD COMPLETE ✅

**Total items built:**
- ✅ 20 Custom Fields
- ✅ 6 Pipelines (58 total stages)
- ✅ 4 Calendars
- ✅ 32 Tags
- ✅ 10 Workflow specs (documented — manual build required)

**Time to complete:** ~15 minutes (API build) + workflow documentation

**Next steps for 1app:**
1. Configure calendar business hours and reminders in GHL UI
2. Build the 10 workflows in GHL Automations using the specs above
3. Add tech team members to calendars
4. Connect Google Business Profile for review request links
5. Set up Stripe for deposit collection (spring pre-booking)
6. Import existing client list with pool details mapped to custom fields
7. Launch spring opening campaign (if Feb–May) or fall closing campaign (if Aug–Oct)
