# 🏊 Pool & Spa GHL Snapshot — Agency Build Research Document
**For:** 1app Technologies Inc.
**Prepared by:** Maximus (AI Business Partner)
**Date:** July 2026
**Version:** 1.0 — Comprehensive Pre-Build Research

---

## TABLE OF CONTENTS

1. [Industry Overview & Business Model](#1-industry-overview--business-model)
2. [Business Pain Points](#2-business-pain-points)
3. [Market Landscape — Existing GHL Snapshots](#3-market-landscape--existing-ghl-snapshots)
4. [Pipeline Architecture](#4-pipeline-architecture)
5. [Workflow Design Blueprint](#5-workflow-design-blueprint)
6. [Lead Sources & Acquisition Channels](#6-lead-sources--acquisition-channels)
7. [SMS & Email Templates](#7-sms--email-templates)
8. [Booking Flow Design](#8-booking-flow-design)
9. [Revenue Program Architecture](#9-revenue-program-architecture)
10. [Seasonal Campaign Blueprints](#10-seasonal-campaign-blueprints)
11. [Equipment Replacement & Upsell Campaigns](#11-equipment-replacement--upsell-campaigns)
12. [Reporting & Dashboard Recommendations](#12-reporting--dashboard-recommendations)
13. [What Makes This Snapshot Stand Out](#13-what-makes-this-snapshot-stand-out)
14. [Snapshot Build Checklist](#14-snapshot-build-checklist)

---

## 1. INDUSTRY OVERVIEW & BUSINESS MODEL

### Who This Snapshot Serves

The pool and spa industry is one of the most **loyalty-rich, high-LTV, service-recurring** niches in the trades. This snapshot targets:

- **Residential pool service companies** (weekly/bi-weekly maintenance routes)
- **Pool opening & closing specialists** (seasonal, often regional)
- **Pool installation & renovation contractors** (new builds, liner replacements, deck/coping upgrades)
- **Hot tub & spa dealers** (showroom + in-home service, chemicals, accessories)
- **Equipment repair specialists** (pumps, heaters, filters, automation systems)
- **Combination shops** (retail store + service routes + install = ideal customer)

### How Pool Companies Actually Make Money

| Revenue Stream | Avg. Ticket | Frequency | LTV Potential |
|---|---|---|---|
| Weekly chemical service | $75–$175/visit | 26–30 visits/season | $2,000–$5,000/year |
| Pool opening | $250–$550 | Once/year | Recurring annual |
| Pool closing / winterization | $200–$450 | Once/year | Recurring annual |
| Equipment repair (pump, filter) | $300–$1,200 | 1–2×/year | Reactive |
| New pool installation | $35,000–$120,000+ | One-time | Massive referral value |
| Liner replacement | $3,500–$8,000 | Every 8–12 years | Re-engagement plays |
| Hot tub sale | $5,000–$18,000 | One-time | Chemical/service LTV |
| Chemical retail / monthly delivery | $60–$150/mo | Monthly | High margin |
| Heater replacement | $1,500–$4,500 | Every 8–12 years | Triggered by age |
| Salt system / automation upgrade | $1,200–$5,000 | One-time | Tech upgrade sell |
| Pool deck jets / water feature | $800–$3,000 | Upgrade add-on | Renovation upsell |

### Seasonality Map (Northern Markets — Ontario, Northern US)

```
JAN  | FEB  | MAR  | APR  | MAY  | JUN  | JUL  | AUG  | SEP  | OCT  | NOV  | DEC
 ──  |  ──  | 🔥PRE | 🔥OPEN| 🔥OPEN| 🌊SVC | 🌊SVC | 🌊SVC | 🔥CLOSE| 🔥CLOSE| ──  |  ──
DEAD | DEAD | SELL | RUSH | RUSH | PEAK | PEAK | PEAK | RUSH  | RUSH  | DEAD | DEAD
```

**Key insight:** Pool companies have a **4–6 month dead window** in northern climates. The snapshot must address off-season revenue and lead nurture aggressively.

---

## 2. BUSINESS PAIN POINTS

### Pain Point #1 — No Lead Capture or Follow-Up System
Most pool companies get leads via word of mouth, Google calls, and lawn signs — and then **lose 60–70% of them** because:
- No one follows up after the first call goes to voicemail
- No text-back system when they're out on a route
- Estimates sit unsent for days
- No pipeline visibility — owner guesses what's in the queue

**GHL Fix:** Missed call text-back, instant lead response workflow, estimate follow-up automation.

### Pain Point #2 — The Spring Opening Crush
Every pool company in a northern climate faces the same terrifying problem: **300 customers all want their pool opened in a 3-week window in May.** Without a system:
- Calls flood the phone
- Scheduling is a whiteboard disaster
- Techs get dispatched to the wrong jobs
- Customers who called first get missed
- Revenue is capped by chaos, not capacity

**GHL Fix:** Pre-season campaign that captures bookings in February/March before the crush hits. Staggered booking calendar with capacity limits per time slot.

### Pain Point #3 — Recurring Maintenance Churn
Weekly maintenance customers are the gold standard — but they leave because:
- No relationship between visits (nobody texts them unless something breaks)
- Competitor door-hangers in the neighbourhood
- Price sensitivity when renewal comes up
- No visible proof of value (what did the tech actually do this week?)

**GHL Fix:** Post-visit SMS with service summary ("Your pool is crystal clear. pH: 7.4, chlorine: 2.1 ppm. See you next week!"), loyalty touchpoints, annual renewal campaigns.

### Pain Point #4 — Emergency Repair Calls with No System
A pump fails on a July Friday afternoon. The pool company:
- Gets flooded with panicked calls
- Has no way to triage urgent vs. non-urgent
- Dispatches blind — tech shows up without parts because no intake form captured equipment details
- Misses the opportunity to upsell during the repair visit

**GHL Fix:** Emergency repair intake form (captures pump model, heater brand, age, symptoms), dispatch workflow, post-repair follow-up with equipment replacement quote.

### Pain Point #5 — Zero Off-Season Revenue
From November to March, pool companies in cold climates have almost zero inbound business. Most owners:
- Don't market in the off-season at all
- Miss the window to lock in spring bookings
- Have no email list to talk to their existing customers
- Lose technicians who find other work during the dead months

**GHL Fix:** Off-season drip sequences that sell winter pool prep products, spa/hot tub service (year-round!), refer-a-friend programs, early spring booking deposits.

### Pain Point #6 — No Review Generation System
Pool companies live and die by Google reviews — but 90% never ask for one. The ones that do ask do it verbally at the end of a job, which is forgotten immediately.

**GHL Fix:** Automated post-service review request SMS triggered 24–48 hours after job completion. 2-step: first ask for 1–5 rating, then route 4–5 stars to Google, route 3 and below to owner inbox for service recovery.

### Pain Point #7 — Chemical Upsell Opportunity Wasted
Every maintenance visit is an opportunity to sell chemicals at retail margins (chlorine tablets, shock, algaecide, pH increaser/decreaser, stabilizer/cyanuric acid, alkalinity increaser, calcium hardness increaser). Most techs just add what's needed and move on — no upsell, no invoice line item education.

**GHL Fix:** Post-service SMS that mentions specific chemical treatments and links to a simple online chemical order form or "schedule a chemical top-up" CTA.

### Pain Point #8 — Equipment Ages Out Silently
Every pool has a pump, filter, heater, salt system, and automation panel. All of them age out on known timelines:
- Sand in filter: replace every 5–7 years
- Pump: 8–12 years
- Heater: 8–15 years
- Liner: 8–15 years
- Salt cell: 3–5 years
- Automation system: 10–15 years

Pool companies know this and never leverage it. No proactive outreach, no replacement campaigns.

**GHL Fix:** Equipment age tracking in custom fields + automated campaigns that trigger when equipment approaches replacement age.

### Pain Point #9 — Hot Tub / Spa Service Is Underserved
Hot tubs run 12 months a year. They require:
- Weekly or bi-weekly water chemistry (chlorine/bromine, pH, alkalinity, calcium hardness)
- Filter cleaning every 1–4 weeks
- Quarterly full drain and refill
- Annual inspection and seal/gasket check
- Cover replacement every 5–7 years

Most pool companies ignore spa service as a year-round revenue stream and miss the entire segment.

**GHL Fix:** Dedicated hot tub maintenance program pipeline with year-round weekly touchpoints.

### Pain Point #10 — No Referral System
Pool and spa customers are social creatures who absolutely talk about their pool at parties. But no one ever asks them for a referral in a systematic way.

**GHL Fix:** Post-season referral campaign with clear incentive ("Refer a friend who books spring opening — you both get $50 off").

---

## 3. MARKET LANDSCAPE — EXISTING GHL SNAPSHOTS

### What Exists

Based on agency and marketplace research, existing pool/spa GHL snapshots fall into three categories:

#### Category A: Generic Home Services Snapshots
- **What they include:** Basic missed call text-back, generic estimate follow-up, 2–3 nurture emails, a simple pipeline
- **Pool relevance:** Low. No seasonal awareness. No opening/closing campaigns. No chemical upsells. No equipment tracking.
- **Examples:** Lawn care snapshots repurposed for pool, HVAC snapshots stretched to cover outdoor work
- **What's missing:** Everything that makes pool industry unique

#### Category B: Pool-Specific Lite Snapshots
- **What they include:** Pool opening booking calendar, basic spring SMS campaign, a maintenance pipeline with 3–4 stages
- **Pool relevance:** Medium. Better than generic, but shallow workflows, no winterization campaign, no equipment lifecycle, no hot tub separation
- **Gaps:** No chemical upsell automation. No equipment age triggers. No referral system. No off-season lead nurture. One-size pipeline for wildly different business types.

#### Category C: Premium Custom Builds (Rare)
- **What they include:** Full multi-pipeline architecture, seasonal campaigns, review automation, chemical tracking custom fields
- **Pool relevance:** High — but these are typically $2,000–$5,000+ custom agency projects, not packaged snapshots
- **Market gap:** No ready-to-deploy, comprehensive, pool-industry-specific snapshot at SaaS price points

### The Market Gap

**The opportunity:** No snapshot on the market combines ALL of the following in one deployable package:
1. Multi-pipeline architecture (install vs. maintenance vs. repair vs. hot tub vs. closing)
2. Seasonal campaign intelligence (spring opening crush + fall winterization)
3. Equipment lifecycle automation (age-triggered replacement campaigns)
4. Chemical service upsell flows
5. Year-round hot tub/spa program management
6. Review generation with service recovery routing
7. Off-season lead nurture and booking deposit capture
8. Referral program automation
9. Google LSA and Facebook lead form integrations

**1app's opportunity:** Build this. Own the pool & spa vertical.

---

## 4. PIPELINE ARCHITECTURE

### Recommended: 6-Pipeline Structure

The pool & spa industry requires multiple distinct pipelines because the customer journey, ticket size, and service delivery are completely different across business types. Cramming everything into one pipeline creates chaos.

---

### PIPELINE 1: New Pool Installation Leads

**Purpose:** Track new build and major renovation leads from first inquiry to signed contract and permit submission.

**Stages:**

| Stage | Description | Trigger Actions |
|---|---|---|
| 📥 New Inquiry | Lead came in (web form, Google, referral) | Immediate SMS response + assign owner |
| 📞 Consultation Booked | Design consultation appointment set | Confirmation email/SMS + reminder sequence |
| 🏠 Site Visit Done | Tech visited property, measurements taken | Post-visit email with "what to expect" |
| 📐 Design & Proposal | Custom proposal being built | Timer: 48hr → nudge if no proposal sent |
| 💰 Proposal Sent | Proposal delivered (email + SMS link) | 24hr → 3-day → 7-day follow-up sequence |
| 🤝 Negotiating | Prospect has questions, pricing discussion | Manual owner follow-up task |
| ✅ Contract Signed | IBA signed, deposit taken | Trigger: onboarding sequence + permit checklist |
| 🚧 Build in Progress | Construction underway | Progress update milestones |
| 🎉 Pool Complete | Final inspection passed, handoff to service | Trigger: maintenance program offer + review request |
| 😔 Lost — Price | Lost on price | 6-month re-engagement sequence |
| 😔 Lost — Other | Lost — competitor, timing, financing | 90-day check-in automation |

**Key Custom Fields:**
- Pool type (in-ground concrete / fibreglass / vinyl liner)
- Estimated budget range
- Property size / lot dimensions
- Features requested (heater, salt system, automation, deck jets, waterfall, hot tub)
- Referral source
- Permit submission date
- Build start date / estimated completion

---

### PIPELINE 2: Spring Pool Opening

**Purpose:** Manage the single most important annual revenue event — the spring opening crush. This pipeline runs Feb 1 – June 30.

**Stages:**

| Stage | Description | Trigger Actions |
|---|---|---|
| 📥 Opening Request | Customer submitted interest (form, SMS keyword, web) | Instant confirmation + calendar booking link |
| 📅 Opening Booked | Appointment on calendar | Confirmation + prep instructions SMS |
| 📋 Pre-Open Prep Sent | Customer instructed on what to do before tech arrives | 48hr pre-appointment reminder |
| 🔧 Opening In Progress | Tech on site | No automation — tech working |
| ✅ Opening Complete | Service done | Post-service SMS: water reading + review request |
| 🧪 Follow-Up Chemistry | 7-day follow-up to check water balance | "How's the pool looking?" SMS + chemical upsell |
| 🔄 Maintenance Offered | Upsell to weekly maintenance program | Maintenance program pitch + booking link |
| 🔁 Annual Renewal Confirmed | Customer confirmed for next year's opening | Tag: "2027 Opening Confirmed" |

**Key Custom Fields:**
- Pool size (gallons / sq ft)
- Pool type (in-ground / above-ground / fibreglass / vinyl)
- Equipment on site (pump brand/model, filter type, heater type, salt system Y/N, automation Y/N)
- Cover type (mesh / solid / automatic)
- Opening date booked
- Tech assigned
- Water test results (pH, chlorine, alkalinity, stabilizer, calcium hardness)
- Opening chemicals used
- Notes (visible damage, rust, cracks, liner condition)

---

### PIPELINE 3: Fall Pool Closing & Winterization

**Purpose:** Manage fall closing season — runs Aug 15 – Nov 15.

**Stages:**

| Stage | Description | Trigger Actions |
|---|---|---|
| 📥 Closing Request | Lead or existing customer requests closing | Instant confirmation + booking link |
| 📅 Closing Booked | Appointment confirmed | Confirmation + prep guide SMS ("Lower water level before we arrive") |
| 🔧 Closing In Progress | Tech on site | No automation |
| ✅ Closing Complete | Pool winterized | Post-service SMS: summary + what was done |
| 🌨️ Winterization Add-On Offered | Salt system winterized, heater bypassed, antifreeze in lines | Upsell SMS/email with price |
| 📆 Next Spring Pre-Book | Offer early-bird spring opening booking | "Lock in your spot before the rush" — with deposit option |
| 💰 Spring Deposit Taken | Deposit collected for spring slot | Confirmation + next-spring reminder set |

**Key Custom Fields:**
- Closing date
- Water level drained to (inches below skimmer)
- Antifreeze used (Y/N + amount)
- Lines blown out (Y/N)
- Cover type installed
- Heater bypassed (Y/N)
- Salt cell removed and stored (Y/N)
- Automation winterized (Y/N)
- Equipment winterized notes
- Spring opening pre-booked (Y/N)

---

### PIPELINE 4: Weekly Maintenance Program

**Purpose:** The highest-LTV pipeline. Track recurring maintenance customers from sign-up through retention and renewal. This is the heartbeat of the business.

**Stages:**

| Stage | Description | Trigger Actions |
|---|---|---|
| 📥 Maintenance Inquiry | Prospect interested in weekly/bi-weekly program | Instant response + program details SMS |
| 📋 Program Quote Sent | Pricing sent based on pool size and frequency | 24hr + 3-day follow-up |
| ✅ Program Signed | Contract signed, route added | Onboarding sequence: welcome + tech intro + what to expect |
| 🌊 Active — Weekly | On weekly route | Post-visit SMS each week with water readings |
| 🌊 Active — Bi-Weekly | On bi-weekly route | Post-visit SMS every other week |
| ⚠️ Chemical Issue Flagged | Algae, cloudy water, pH crash — needs extra visit | Alert to owner + emergency visit booking |
| 🔄 Annual Renewal | Season-end renewal prompt | Renewal offer + loyalty discount |
| 😔 Churned — Price | Cancelled due to price | 30-day win-back sequence |
| 😔 Churned — DIY | Cancelled to DIY | 60-day re-engagement: "DIY pool care is harder than it looks" |
| 😴 Dormant | No contact, didn't renew | Off-season check-in sequence |

**Key Custom Fields:**
- Program type (weekly / bi-weekly / monthly)
- Pool size (gallons)
- Route day (Monday / Tuesday / etc.)
- Assigned technician
- Contract start date / contract end date
- Monthly rate
- Chemical preferences (chlorine / salt / mineral / UV)
- Last water test results (pH, FC, TC, CYA, alkalinity, calcium hardness)
- Special instructions (access code, dog, gate combo, skimmer basket notes)
- Equipment on site (full inventory)
- Consecutive seasons as customer

---

### PIPELINE 5: Equipment Repair & Emergency Service

**Purpose:** Manage reactive service calls — pump failures, heater issues, green pools, filter problems, automation malfunctions.

**Stages:**

| Stage | Description | Trigger Actions |
|---|---|---|
| 🚨 Emergency Request | Urgent call/text — "pump not working," "pool green" | Instant SMS: "We received your request. ETA: [time]" |
| 📋 Diagnosis Booked | Non-emergency — scheduled service call | Confirmation + reminder + equipment intake form |
| 🔍 Diagnosis In Progress | Tech on site assessing | No automation |
| 💰 Repair Quote Sent | Parts and labour quote sent | 4hr + 24hr follow-up |
| 🛠️ Repair Approved | Customer approved repair | Parts order triggered + dispatch notification |
| 🔧 Repair Completed | Work done | Post-service SMS + invoice link + review request |
| 🔄 Replacement Recommended | Equipment beyond repair — replacement quote issued | Replacement quote sequence (see Pipeline 6 below) |
| ✅ Closed — Fixed | Successful repair | 30-day check-in: "How's the equipment holding up?" |
| ❌ Closed — Lost | Went elsewhere for repair | Re-engagement at next season |

**Key Custom Fields:**
- Equipment type (pump / filter / heater / salt system / automation / lights / liner / skimmer)
- Brand / model number
- Approximate age of equipment
- Symptoms described
- Diagnosis notes
- Parts required (part numbers, supplier)
- Repair total
- Warranty offered (Y/N, duration)
- Replacement recommended (Y/N)
- Next equipment inspection date

---

### PIPELINE 6: Hot Tub & Spa Sales & Service

**Purpose:** Manage the hot tub segment separately — it is a year-round revenue stream and a completely different customer journey from pools.

**Stages:**

| Stage | Description | Trigger Actions |
|---|---|---|
| 💬 Hot Tub Inquiry (Purchase) | Prospect interested in buying a hot tub | Instant response + showroom visit booking link |
| 🏪 Showroom Visit Scheduled | In-store appointment | Reminder + "what to expect at the showroom" email |
| 💰 Quote Sent | Specific model priced and quoted | 24hr + 3-day + 7-day follow-up |
| 🤝 Sale Closed | Purchase confirmed, delivery scheduled | Onboarding sequence + delivery confirmation |
| 🚚 Delivery & Installation | Tub delivered and set up | Post-install check-in 48hrs later |
| 🧪 First Chemical Service | New tub owners need startup chemistry help | Chemical education sequence |
| 🌀 Maintenance Program | Monthly or bi-monthly spa service program | Program pitch + booking |
| 🔧 Service Request | Existing spa customer — repair/issue | Repair intake form + quick response |
| 🎄 Year-Round Active | Happy, ongoing spa service customer | Seasonal touchpoints + chemical delivery offers |
| 🔄 Cover/Filter Replacement | Triggered when cover is 5+ years old | Replacement quote |

**Key Custom Fields:**
- Tub type (portable / in-ground / swim spa)
- Brand / model
- Capacity (jets, seats)
- Sanitizer type (chlorine / bromine / salt / mineral)
- Cover type and age
- Filter model and last cleaned date
- Last drain and refill date
- Service frequency
- Water chemistry log (pH, alkalinity, sanitizer level, calcium hardness)
- Delivery address + electrical requirements met (Y/N)

---

## 5. WORKFLOW DESIGN BLUEPRINT

### WORKFLOW 1: Missed Call Text-Back (Universal)

**Trigger:** Missed incoming call to GHL phone number
**Delay:** 30 seconds
**Action:** SMS → "Hey [First Name]! Sorry we missed your call — we're probably out on a route right now. Reply to this text or click here to book: [BOOKING LINK]. We'll get back to you within the hour. — [Business Name]"
**Follow-up:** If no reply in 2 hours → second SMS → "Still here if you need us! What can we help you with?"
**Escalation:** If no reply in 24 hours → Email with booking link + company intro

---

### WORKFLOW 2: New Web Lead — Instant Response

**Trigger:** Form submission from website, Facebook lead ad, or landing page
**Step 1 (0 min):** SMS → "Hey [First Name], thanks for reaching out to [Business Name]! We got your request and someone will be in touch within the hour. In the meantime, you can book directly here: [BOOKING LINK]"
**Step 2 (0 min):** Email → Full intro email with services overview, service area map, and booking link
**Step 3 (0 min):** Internal notification → Owner/admin SMS: "New lead: [Full Name] — [Service Type] — [Phone]"
**Step 4 (30 min):** If no booking made → Follow-up SMS → "Did you get a chance to look at our availability? We have spots open this week!"
**Step 5 (Day 1):** If still no booking → Email with FAQ: "What to expect when you book with us"
**Step 6 (Day 3):** If still no booking → SMS → "We have [X] openings this week — first come, first served in spring! Want us to hold a spot?"
**Step 7 (Day 7):** If no booking → Final email + SMS → move to "Cold Lead Nurture" tag

---

### WORKFLOW 3: Spring Opening Campaign (Pre-Season)

**Launch:** February 1st annually
**Target:** All existing customers tagged "Past Opening Customer" + all contacts in database

**Week 1 (Feb 1) — Email:** Subject: "Spring pool opening — book your spot before they're gone (seriously)"
- Headline: Your Pool Deserves a Head Start This Season
- Body: Last year, we booked solid in 3 weeks. This year we're opening booking NOW so our best customers get first pick.
- CTA: [BOOK MY SPRING OPENING] button

**Week 2 (Feb 7) — SMS:** "Hey [First Name]! Spring opening booking is live. We fill up FAST — grab your spot now: [LINK] 🌊"

**Week 3 (Feb 15) — Email:** Subject: "⚡ Only [X] spots left for May openings"
- Urgency: Real capacity limit (use slot count from calendar)
- Introduce: Early bird pricing — "Book before March 1 and save $25"

**Week 4 (Mar 1) — SMS:** "Last call for early-bird spring opening pricing — locks in at $[X]. Book by Friday: [LINK]"

**Week 5 (Mar 15) — Email:** "Spring opening checklist — what to do before we arrive"
- Value-add educational content
- Secondary CTA: "Still haven't booked? A few spots left"

**Week 6 (Apr 1) — SMS:** "Spring is coming! Confirm your opening appointment: [LINK] 🌊 — [Business Name]"

**Week 7 (May 1) — Email:** "Opening season is HERE — if you haven't booked, we're in emergency-fill mode. A few last-minute spots available."

---

### WORKFLOW 4: Fall Closing Campaign

**Launch:** August 15th annually
**Target:** All active maintenance customers + past opening/closing customers

**Week 1 (Aug 15) — Email:** Subject: "Fall closing — book early, avoid the wait"
- Explain the same crush happens in fall
- CTA: Book your pool closing now

**Week 2 (Sep 1) — SMS:** "Hey [First Name]! Time to start thinking about closing. We book out fast in October — grab your spot: [LINK] 🍂"

**Week 3 (Sep 15) — Email:** "Closing checklist + what we do to protect your pool all winter"
- Detail: Water level, antifreeze in lines, skimmer plugs, equipment bypass, cover install
- Value: "A proper closing protects your liner, equipment, and plumbing from freeze damage"
- CTA: Book closing + offer winterization add-on

**Week 4 (Oct 1) — SMS:** "Oct is here — we're filling up for closings. Don't get left scrambling! [LINK]"

**Week 5 (Oct 15) — Email:** "Last spots for October closings — act now before you're stuck in November"
- Winter storage discount: "Store your pump cover + accessories with us for the winter"
- Spring pre-booking CTA: "Book both closing + next spring opening — save $40"

---

### WORKFLOW 5: Post-Service Review Request

**Trigger:** Job status changed to "Complete" in GHL
**Delay:** 24 hours
**Step 1:** SMS → "Hi [First Name]! [Tech Name] wanted to make sure everything looked great after today's visit. On a scale of 1–5, how did we do? Reply with a number!"

**Branch — Rating 4 or 5:**
- SMS → "So glad to hear it! 🙌 If you have a moment, a Google review means the world to our small business: [GOOGLE REVIEW LINK]. Takes 60 seconds!"

**Branch — Rating 1, 2, or 3:**
- SMS → "Oh no — we're sorry to hear that! Can you tell us what happened? [Owner Name] wants to make it right."
- Internal alert → Owner: "Service recovery needed: [Customer Name] rated [X]/5 — respond ASAP"
- Task created → Owner follow-up within 24hrs

---

### WORKFLOW 6: Weekly Maintenance Post-Visit Summary

**Trigger:** Tag applied "Weekly Visit Complete — [Date]" or form submitted by tech
**Action (immediate):** SMS → "Hi [First Name]! [Tech Name] just finished your pool service for [Date]. Here's your water report:
- 🔵 pH: [VALUE] (target: 7.2–7.6)
- 🟡 Chlorine: [VALUE] ppm (target: 1–3 ppm)
- 🟢 Alkalinity: [VALUE] ppm (target: 80–120 ppm)
- ⚪ Stabilizer (CYA): [VALUE] ppm (target: 30–50 ppm)

Everything looks great! See you next week. 🌊"

**Day 5 after visit:** SMS → "Your next maintenance visit is in [X] days! Anything you want us to check or bring? Reply and let us know."

---

### WORKFLOW 7: Equipment Repair Follow-Up + Replacement Trigger

**Trigger:** Repair job marked Complete
**24 hours:** SMS → "Hey [First Name]! Just checking in — is the [equipment type] running smoothly? Let us know if anything seems off."

**30 days:** SMS → "Quick check-in on your [pump/heater/filter]. How's it performing? Our techs recommend a seasonal check every 30 days for [X]-year-old equipment. Need anything?"

**If Equipment Age Custom Field > Replacement Threshold:**
- Add tag: "Equipment Replacement Candidate — [Type]"
- Trigger: Equipment Replacement Campaign (see Section 11)

---

### WORKFLOW 8: Referral Program

**Trigger:** Tag applied "Active Maintenance Customer — Season 2+" or "Happy Review Left"
**Step 1:** SMS → "Hey [First Name] — quick question. Do you know anyone who needs their pool opened this spring or needs a maintenance crew? If you refer someone who books with us, you BOTH get $50 off. Just have them mention your name! 🌊"
**Step 2:** Email → Full referral program details with simple tracking (unique code or just "mention [name]")
**Step 3 (30 days later):** If no referral → SMS → "Still running our referral program — $50 off for you and a friend! Know anyone with a pool? 🤝"

---

### WORKFLOW 9: Chemical Upsell

**Trigger:** Post-visit note includes "Low stabilizer" / "pH crash" / "High calcium" / "Added shock" / form field flagged
**Step 1 (24hrs):** SMS → "Hi [First Name]! After your service visit, we noticed your pool could use some extra love. We added [X treatment] today, but we'd recommend picking up [product] to keep things balanced. We carry it — want us to bring some next visit?"
**Step 2:** Email → "Pool chemistry 101: what your [pH/chlorine/stabilizer/alkalinity] levels mean and how to keep them perfect"
**Optional:** Link to simple online chemical order form

---

### WORKFLOW 10: Off-Season Nurture (Winter — Nov through Mar)

**Target:** All non-hot-tub customers who are "inactive" (pool closed)
**Goal:** Stay top of mind, generate spring deposits, and offer hot tub or year-round services

**Month 1 (Nov):** Email → "Your pool is closed — now what? Winter checklist and what to watch for"
**Month 2 (Dec):** Email → "The gift of a clean pool: hot tub gift cards for the holidays" + hot tub service offer
**Month 3 (Jan):** SMS → "New Year, New Pool Season — want to lock in your spring opening spot early? We're booking NOW for 2027."
**Month 2 (Feb):** → Transition into Spring Opening Campaign (Workflow 3)

---

## 6. LEAD SOURCES & ACQUISITION CHANNELS

### Priority 1: Google Local Services Ads (LSA)

- **Why:** Pool companies with LSA get Google Guaranteed badge. Homeowners searching "pool opening near me" or "pool repair [city]" click LSA first.
- **Integration:** GHL → LSA connector via Zapier or native integration
- **Key trigger words:** "pool opening," "pool closing," "pool repair," "pool service near me," "hot tub service," "green pool"
- **Lead type:** High intent, ready to buy, often emergency
- **GHL action:** Instant SMS response within 60 seconds (Google measures this for LSA scoring)
- **Best practice:** Add "LSA" tag to all incoming leads to track ROI separately

### Priority 2: Google Organic + Maps

- **Why:** Ongoing organic presence for "pool company [city]" searches
- **Integration:** Website contact form → GHL via native embed or Zapier
- **GHL action:** Standard new lead workflow
- **Reputation play:** Review automation feeds directly into Google Maps ranking

### Priority 3: Facebook & Instagram (Aspirational Content)

- **Why:** Pool photos drive aspirational desire. Before/after transformation content. "This is what a professionally maintained pool looks like vs. a DIY pool."
- **Content types:**
  - Time-lapse green → crystal clear pool transformations
  - Water chemistry explainers ("why is my pool cloudy?")
  - Pool opening day content (early May = viral for local audiences)
  - "We have 3 spots left this week" urgency posts
- **Integration:** Facebook Lead Ads → GHL natively (lead form CTA)
- **Lead types:** Aspirational buyers for new installs, maintenance inquiries

### Priority 4: Referrals

- **Why:** Highest-converting, lowest-cost leads in the pool industry
- **GHL action:** Referral workflow (Workflow 8) + manual referral tracking tag
- **Conversion rate:** 40–70% vs. 5–15% for cold traffic

### Priority 5: New Home Builders

- **Partnership play:** Partner with residential builders. When a new home is built with a pool, the builder refers the homeowner for service.
- **GHL action:** Builder-specific intake form, "new home pool setup" workflow, first-season chemistry package upsell
- **Contact method:** Manual outreach → CRM contact record for each builder relationship

### Priority 6: Real Estate Agents

- **Partnership play:** Homebuyers who purchase a house with an existing pool need service immediately. Agents who refer clients to a trusted pool company get a value-add for their clients.
- **GHL action:** "Real Estate Referral" tag + priority booking workflow
- **Nurture:** Monthly email to agent list with pool tips they can share with clients

### Priority 7: Door Hangers & Yard Signs

- **Old school but still works.** After completing an opening in a neighbourhood, leave door hangers at the next 10 houses.
- **GHL action:** QR code on door hangers → direct to booking page with tracking parameter
- **Tag:** "Door Hanger — [Neighbourhood]" for ROI tracking

---

## 7. SMS & EMAIL TEMPLATES

### SMS TEMPLATES

#### Spring Opening — Initial Outreach (Feb)
> "Hey [First Name]! 🌊 Spring is coming faster than you think — and so is our booking calendar. Lock in your pool opening now before we fill up: [LINK] — [Business Name]"

#### Spring Opening — Urgency (April)
> "⚠️ [First Name] — we're filling FAST for May openings. Only [X] spots left. Grab yours before it's gone: [LINK]"

#### Fall Closing — Outreach (September)
> "Hey [First Name]! 🍂 Summer's winding down — time to think about closing your pool. Book before October and beat the rush: [LINK] — [Business Name]"

#### Missed Call Text-Back
> "Hey [First Name]! Missed your call — we're probably elbow-deep in a pool right now 😄 Text us here or book online: [LINK]. Back to you shortly! — [Business Name]"

#### Post-Service Summary (Weekly Maintenance)
> "Hi [First Name]! Pool service done ✅. pH: [X] | Chlorine: [X] ppm | Alkalinity: [X] ppm — all looking great! See you [next visit day]. — [Tech Name], [Business Name]"

#### Green Pool Emergency Response
> "Hey [First Name]! We got your message about your pool. Green pools need fast action — the longer you wait, the more chemicals it takes. We can get a tech out [TODAY/TOMORROW]. Confirm here: [LINK] — [Business Name]"

#### Equipment Repair — Diagnosis Confirmation
> "Hi [First Name]! Your [pump/heater/filter] repair is confirmed for [DATE] at [TIME]. Our tech will come prepared — can you confirm the brand and model? Reply or fill out this quick form: [LINK]"

#### Post-Repair Check-In (24hrs)
> "Hey [First Name]! Just checking in — is the [equipment] running the way it should? If anything seems off, reply here and we'll get back out. — [Business Name]"

#### Review Request
> "Hi [First Name]! We hope your pool is looking crystal clear after today's service 💙 Quick favor — could you leave us a Google review? It takes 60 seconds and means the world: [LINK]"

#### Chemical Upsell
> "Hi [First Name]! We noticed your pool's [stabilizer/pH/alkalinity] was a bit low today. We can bring [product] on your next visit or drop it off this week. Interested? — [Business Name]"

#### Referral Ask
> "Hey [First Name]! Know anyone with a pool who needs opening, closing, or weekly service? Refer a friend and you BOTH get $50 off. Just have them mention your name when they book! 🤝"

#### Hot Tub Service — Monthly Chemical Check
> "Hi [First Name]! Time for your monthly spa service check. Your filter needs a rinse and it's been [X] days since your last drain/refill. Want to book? [LINK] — [Business Name]"

#### Winter Re-Engagement (January)
> "Hey [First Name]! 🌨️ Spring opening season starts in 6 weeks. We're booking NOW — want to lock in your spot before we sell out? [LINK]"

---

### EMAIL TEMPLATES

#### Email 1: Spring Opening Launch (Subject: "Your pool opening — don't get stuck in the rush")

**Subject line variations to A/B test:**
- "Spring pool opening — book before we fill up (we always do)"
- "Your pool opening spot is waiting — but not for long"
- "[First Name], spring is 8 weeks away. Are you on our calendar?"

**Body:**

Hi [First Name],

Every spring, the same thing happens: we go from completely available to completely booked in about three weeks.

This year, we're giving our existing customers first access to our calendar before we open it to new clients.

Here's what you get when you book your spring opening with [Business Name]:

✅ Full opening service — remove cover, reinstall equipment, check all fittings and returns
✅ Water test — pH, chlorine, alkalinity, stabilizer (CYA), calcium hardness
✅ Chemical treatment — start the season with balanced water
✅ Equipment inspection — pump, filter, heater, salt system, automation
✅ Report card — you'll know exactly where your pool stands

**[BOOK MY SPRING OPENING →]**

Already know you want us back? We've pre-loaded your pool details from last year. Just pick a date.

Talk soon,
[Owner Name]
[Business Name]
[Phone] | [Website]

---

#### Email 2: Fall Closing — Winterization Deep Dive

**Subject:** "How we protect your pool all winter (and why it matters)"

Hi [First Name],

A pool that's properly closed survives winter without a scratch. A pool that's rushed through closing can cost you thousands in spring repairs.

Here's what our complete closing service includes:

🔵 **Water chemistry balanced** — we adjust pH, alkalinity, and add winter algaecide before closing so you don't open to a swamp
🔵 **Water level lowered** — below the skimmer to prevent freeze damage to tile and coping
🔵 **Lines blown out and antifreeze added** — every return line, skimmer, and drain line is cleared of water
🔵 **Equipment bypassed and winterized** — pump, filter, heater, and salt cell safely stored or bypassed
🔵 **Cover installed** — mesh or solid cover properly secured
🔵 **Skimmer plugs + Gizzmos installed** — protect the skimmer body from ice expansion

**Optional winterization add-ons:**
- Salt cell removal and indoor storage
- Pool cover pump installation
- Equipment storage on-site or at our facility

**[BOOK MY POOL CLOSING →]**

Pro tip: Book before October 15 and you'll also get **$25 off your 2027 spring opening**. We're already booking spring slots — your name goes on the list today.

[Owner Name]
[Business Name]

---

#### Email 3: Green Pool Emergency Education + Lead Capture

**Subject:** "Your pool is green — here's exactly what to do right now"

Hi [First Name],

Green pool water is almost always algae — and algae spreads fast in warm water.

Here's the short version of what causes it:
- **Low chlorine** (FC below 1 ppm) allows algae to establish
- **High stabilizer (CYA)** above 80 ppm makes chlorine ineffective even if you add it
- **Low circulation** — skimmer basket full, pump running less than 8 hours/day
- **Missed treatment** — a few days without chemical service in peak summer = green pool

**What NOT to do:** Dump a bucket of chlorine in and wait. This usually doesn't work and delays proper treatment.

**What we do:** Shock treatment, algaecide, pH adjustment, extended pump run time, brush and vacuum, re-test in 24–48 hours.

If you're dealing with a green pool right now, we can typically turn it around in 2–5 days depending on severity.

**[BOOK GREEN POOL TREATMENT →]**

Questions? Text or call us directly: [PHONE]

[Business Name]

---

#### Email 4: Equipment Education — Pump Replacement

**Subject:** "How old is your pool pump? (and why it matters this season)"

Hi [First Name],

Pool pumps are the heart of your system — and like most hearts, they have a lifespan.

Here's the honest truth about pump lifespans:
- **Single-speed pumps** — 8–12 years before they start to go
- **Variable-speed pumps** — 10–15 years, and they save 60–80% on electricity vs. single-speed
- **Signs of a dying pump:** loud bearing noise, tripping breaker, low flow, visible rust or corrosion

If your pump is over 8 years old, it's not a matter of if it will fail — it's when. And it always fails in July on a Friday afternoon when your kids have friends over.

**The smart move:** Replace proactively during the shoulder season (spring or fall) when:
- We have time to do the job right
- Parts are in stock
- You don't lose a week of swimming

**Bonus:** New variable-speed pumps often pay for themselves in 2–3 seasons through electricity savings.

Want us to assess your pump's age and condition? We'll give you an honest evaluation at your next service visit.

**[BOOK EQUIPMENT ASSESSMENT →]**

[Business Name]

---

## 8. BOOKING FLOW DESIGN

### Booking Page Structure — 3 Distinct Entry Points

#### Entry Point 1: Spring Pool Opening Booking
**URL:** /book-pool-opening
**Calendar type:** Service appointment with defined slots
**Fields collected:**
- First Name, Last Name
- Email, Phone
- Service address
- Pool type (in-ground / above-ground / fibreglass / vinyl)
- Approximate pool size (dropdown: under 10,000 gal / 10–20,000 gal / 20,000+ gal)
- Last year's opening — did we do it? (Y/N)
- Preferred week (early May / mid-May / late May / June)
- Any known issues or special notes

**Confirmation:** Immediate SMS + email with prep checklist ("What to do before we arrive: 1. Remove winter cover anchors... 2. Clear the deck area... 3. Have the water source accessible...")

**Reminder sequence:** 72hr → 24hr → 2hr before appointment

---

#### Entry Point 2: Maintenance Program Sign-Up
**URL:** /weekly-pool-service
**Not a calendar booking — a form that goes into pipeline as "Maintenance Inquiry"**
**Fields collected:**
- First Name, Last Name
- Email, Phone
- Service address
- Pool type and approximate size
- Desired frequency (weekly / bi-weekly)
- Current water condition (great / okay / needs work)
- What's currently on site (pump brand, filter type, heater Y/N, salt system Y/N)
- Any special access notes (gate code, dog, etc.)

**Next step:** Owner reviews inquiry, calls within 2 hours to discuss pricing and start date. GHL task created automatically.

---

#### Entry Point 3: Equipment Repair / Emergency Call
**URL:** /pool-repair or /emergency-pool-service
**Urgency-first design — short form, fast response promise**
**Fields collected:**
- First Name, Last Name
- Phone (required — we call, don't just text for emergencies)
- Service address
- What's the issue? (dropdown: green pool / pump not running / heater not heating / cloudy water / low pressure / broken skimmer / crack / liner damage / automation issue / other)
- How urgent is this? (dropdown: Pool is completely unusable / It's bad but we can wait a day or two / Not urgent, just want it looked at)
- Equipment brand and model (if known)
- Anything else we should know?

**Confirmation:** Immediate SMS → "Got it, [First Name]! For [issue type], we prioritize fast response. A tech will call you within [30 min / 2 hours] depending on urgency."

---

#### Entry Point 4: Pool Closing Booking
**URL:** /book-pool-closing
**Mirrors spring opening but fall-specific**
**Additional fields:**
- Cover type (mesh / solid / automatic cover / no cover)
- Lines blown previously? (Y/N)
- Winterization add-on interest (Y/N)
- Interest in spring pre-booking with deposit? (Y/N)

---

#### Entry Point 5: Hot Tub / Spa Service
**URL:** /hot-tub-service
**Fields:**
- Hot tub brand / model
- Hot tub age
- Sanitizer type (chlorine / bromine / salt / mineral / unsure)
- Last water test date
- Issue type (chemical service / not heating / jet issue / leak / general maintenance / chemical delivery)
- Preferred service frequency

---

### Calendar Configuration Best Practices

- **Slot duration:** 2–4 hours for openings/closings (travel + service time)
- **Buffer time:** 30 min between slots on same technician
- **Max daily capacity:** Set per technician (e.g., 4 openings/day max for a 2-person crew)
- **Blackout dates:** Mother's Day weekend is peak opening — consider premium pricing or holding slots
- **Team calendar:** Multiple technicians with individual capacity management
- **Appointment types:** Clearly label (Pool Opening, Pool Closing, Repair Call, Maintenance Assessment) — don't mix on one calendar

---

## 9. REVENUE PROGRAM ARCHITECTURE

### Program 1: Monthly Maintenance Club (Highest Priority)

**The core of the business. Once a customer is on a maintenance contract, they stay for 5–10+ years on average.**

**Tier structure:**

| Tier | Name | Frequency | What's Included | Price Range |
|---|---|---|---|---|
| Basic | Essential Care | Bi-weekly | Water test, chlorine/shock treatment, skim surface, empty baskets | $80–$120/visit |
| Standard | Crystal Clear | Weekly | All basic + brush walls and floor, vacuum, check equipment | $100–$165/visit |
| Premium | Total Care | Weekly | All standard + full chemical log, tech report, priority emergency | $140–$200/visit |

**GHL Implementation:**
- Separate contact tag for each tier
- Weekly post-visit SMS with water readings
- Monthly invoice automation via Stripe integration
- Annual renewal 60 days before season end

---

### Program 2: Opening + Closing Bundle

**"Set it and forget it" annual program — one price, two services, priority booking.**

- Customer pays one annual fee (e.g., $599 combined) in February
- Gets priority slot for both opening and closing
- Gets winter chemical care package mailed in November
- **LTV play:** Bundle buyers almost always become maintenance customers year 2

**GHL Implementation:**
- "Bundle Customer" tag → separate pipeline tracking
- Automatic spring and fall booking triggers in February and August
- Pre-season communications branded "Your Season is Protected"

---

### Program 3: VIP Pool Care Annual Membership

**The premium tier — year-round relationship, maximum LTV**

**What's included:**
- Weekly maintenance (full season)
- Spring opening + fall closing
- 2 free emergency service calls
- Annual equipment inspection
- Chemical delivery (basic chemicals included in price)
- Priority scheduling always
- Winter spa/hot tub service if applicable

**Price:** $2,500–$4,500/season depending on pool size and services

**GHL Implementation:**
- "VIP Member" tag → premium workflow branch in all automations
- VIP gets first slot in all booking windows
- Birthday/anniversary touches ("Happy pool season!")
- Owner-level communication (not just tech)

---

### Program 4: Hot Tub Chemical Delivery

**Year-round revenue. Low labor. High margin.**

Monthly or bi-monthly delivery of:
- Chlorine/bromine tablets
- pH increaser/decreaser
- Alkalinity increaser
- Calcium hardness increaser
- Filter cleaner
- Shock (weekly or as needed)

**GHL Implementation:**
- "Chemical Delivery" subscription tag
- Monthly SMS reminder: "Your chemical order is being prepared for delivery this week. Need anything extra?"
- Quarterly: drain and refill reminder

---

## 10. SEASONAL CAMPAIGN BLUEPRINTS

### CAMPAIGN 1: Spring Opening Blitz (Jan 15 – May 31)

**Goal:** Fill the opening calendar before the crush hits. Generate deposits. Create urgency.

**Phase 1 — Early Bird (Jan 15 – Feb 28):**
- Email #1: "Spring opens in 10 weeks — lock in your spot"
- SMS #1: Early bird booking announcement
- Offer: $25 off for booking before March 1

**Phase 2 — Urgency (Mar 1 – Apr 15):**
- Email #2: "X spots left for May"
- SMS #2: Countdown urgency
- Facebook/Instagram ad: Before/after pool photo + "Book your opening"
- Email #3: "Spring prep checklist" (value-add, soft CTA)

**Phase 3 — Rush Management (Apr 15 – May 31):**
- Email #4: "Opening season is here — confirm your appointment"
- Reminder sequences: 72hr, 24hr, 2hr before each appointment
- Post-opening review request

**KPIs to track in GHL:**
- # of opening leads generated
- # of bookings converted
- # of review requests sent
- # of reviews received
- Conversion rate of opening customers to maintenance program

---

### CAMPAIGN 2: Fall Closing & Winterization (Aug 15 – Nov 15)

**Goal:** Fill the closing calendar. Upsell winterization. Pre-book spring.

**Phase 1 — Early Booking (Aug 15 – Sep 15):**
- Email: "Time to think about closing" + early bird incentive
- SMS: Light touch, "summer's ending — let's get you on the calendar"

**Phase 2 — Active Sell (Sep 15 – Oct 15):**
- Email: Winterization education deep dive
- SMS: Urgency push
- Offer: "Book closing + next spring opening today — save $40"

**Phase 3 — Final Call (Oct 15 – Nov 15):**
- Email: "Last call for fall closings"
- SMS: "We have [X] spots left this week — after this it's first come first served"
- Post-closing review request

---

### CAMPAIGN 3: Algae Attack Season (June – August)

**Goal:** Be top of mind when the inevitable summer green pool crisis hits. Capture emergency repair leads before they call a competitor.

**Month: June:**
- Email: "Algae prevention — what to do before your pool turns green"
- Educational content: ideal chlorine levels, cyanuric acid (CYA) and chlorine lock, backwash frequency for sand filters, importance of running pump minimum 8 hours/day

**Month: July (peak green pool season):**
- Facebook/Instagram post: Time-lapse green → crystal clear transformation
- Email: "Is your pool looking a little... green? We can fix that."
- SMS to past repair customers: "Summer check-in — any issues with the pool? We're in your area this week."

**Month: August:**
- Email: "Late-summer water chemistry — what to watch for before closing season"
- CTA: Schedule end-of-season water test + assessment

---

### CAMPAIGN 4: Holiday Hot Tub Push (Nov – Dec)

**Goal:** Hot tub customers are year-round — but Christmas is the perfect time to sell new tubs and services.

- Email: "The perfect holiday gift — a new hot tub for your backyard"
- Promotion: Holiday financing special, gift cards available
- SMS to spa customers: "It's hot tub season! Your spa is the best place to be in December 🛁"
- Spa chemical delivery promo: "Monthly chemical delivery — set it up now and never run out"

---

## 11. EQUIPMENT REPLACEMENT & UPSELL CAMPAIGNS

### Equipment Age Tracking System

Every contact record should have custom fields for each major piece of equipment:

| Custom Field | Type | Example Values |
|---|---|---|
| Pump Brand | Text | Pentair, Hayward, Zodiac |
| Pump Model | Text | IntelliFlo VS, Super Pump |
| Pump Install Year | Number | 2016 |
| Filter Type | Dropdown | Sand / Cartridge / DE |
| Filter Install Year | Number | 2018 |
| Heater Brand | Text | Hayward, Pentair, Raypak |
| Heater Install Year | Number | 2014 |
| Salt System Brand | Text | Hayward AquaRite, Pentair |
| Salt Cell Install Year | Number | 2020 |
| Liner Install Year | Number | 2012 |
| Automation System | Text | Pentair IntelliCenter, Jandy |
| Automation Install Year | Number | 2019 |
| Last Major Service | Date | 2024-08-15 |

### Triggered Replacement Campaigns

**Pump Replacement Campaign** — triggers when (Current Year - Pump Install Year) ≥ 8

Email #1: "Your pump is [X] years old — what you should know"
- Explain single-speed vs. variable-speed savings
- Variable-speed pays back in 2–3 seasons in energy savings
- "Proactive replacement is always cheaper than emergency replacement"

SMS #1: "Quick question about your pump — our records show it's [X] years old. Want a quote on a variable-speed upgrade before the season starts?"

Email #2 (30 days later): "Final check-in: pool pump assessment offer"
CTA: Schedule free pump assessment

---

**Heater Replacement Campaign** — triggers at 10 years

Email: "Pool heater lifespan — are you on borrowed time?"
- Heaters over 10 years often fail silently until one cold week in June they just don't fire
- Heat pump vs. gas heater breakdown
- "We'll remove your old heater, install new, and test before we leave"

---

**Liner Replacement Campaign** — triggers at 10 years

Email: "Pool liner age checklist — 5 signs it's time to replace"
1. Fading colour and chalky texture
2. Wrinkles that won't smooth out
3. Small tears or patches (even repaired ones)
4. Slippery surface — algae adhering to worn vinyl
5. Loss of water faster than evaporation

"A new liner is 8–12 years of leak-free, beautiful swimming. Want a quote?"

---

**Salt Cell Replacement Campaign** — triggers at 4 years

SMS: "Quick heads up — salt cells typically need replacement every 3–5 years. Your cell is [X] years old. Want us to test cell output at your next service?"

---

**Filter Sand Replacement Campaign** — triggers at 6 years

SMS: "Pool filter running at full power? Sand in DE filters should be replaced every 5–7 years. Let us check yours at your next visit."

---

## 12. REPORTING & DASHBOARD RECOMMENDATIONS

### Key Metrics — GHL Dashboard Setup

#### Owner Dashboard (Real-Time KPIs)

| Metric | Source | Why It Matters |
|---|---|---|
| New leads this week | Pipeline stage 1 entries | Volume pulse |
| Leads responded to within 5 min | Response time tracking | Speed wins in pool |
| Openings booked (season total) | Pipeline 2 count | Revenue forecast |
| Closings booked | Pipeline 3 count | Fall revenue forecast |
| Active maintenance customers | Tag count | Recurring revenue base |
| Reviews generated (MTD) | Google integration | Reputation growth |
| Upsell revenue from chemical add-ons | Custom field tracking | Margin opportunity |
| Equipment replacement quotes sent | Pipeline 6 activity | Future revenue |
| Referrals received (MTD) | Tag "Referral Source" | Best lead quality |

#### Seasonal Performance Report (Monthly)

- Opening appointments booked vs. capacity (% full)
- Closing appointments booked vs. capacity
- Lead source breakdown (LSA / referral / Facebook / website / door hanger)
- Average days from lead to booking
- No-show rate (appointment confirmed but missed)
- Post-service review request to review conversion rate
- Maintenance program conversion rate from one-time services

---

## 13. WHAT MAKES THIS SNAPSHOT STAND OUT

### Competitive Differentiation

**1. Seasonal Intelligence Built In**
Every workflow and campaign is tied to the pool calendar. The snapshot literally knows that February = spring opening campaign launch, August = fall closing campaign launch, and July = algae emergency season. No generic home services template does this.

**2. Water Chemistry as a Relationship Tool**
The post-visit water chemistry SMS (pH, chlorine, alkalinity, CYA) transforms a transactional service into a weekly relationship touchpoint. Customers start to understand their own pool chemistry. They trust the tech. They stay for years.

**3. Equipment Lifecycle Automation**
No other snapshot proactively tracks pump age, liner age, heater age, and salt cell age and triggers replacement campaigns on a schedule. This is massive — every proactive replacement generates $1,500–$8,000+ in revenue the owner didn't have to ask for.

**4. Multi-Pipeline Architecture**
Pool companies are actually 3–5 businesses in one (install, maintenance, opening/closing, repair, hot tub). A single generic pipeline creates chaos. This snapshot's 6-pipeline architecture keeps every business type organized, tracked, and automated separately.

**5. The Spring Opening Crush Is Solved**
The single biggest operational headache in the pool industry — handled with a February-launch booking campaign, early bird incentives, urgency escalation, and a staggered calendar that prevents overbooking.

**6. Hot Tub/Spa Year-Round Revenue**
Most pool snapshots ignore spas entirely. This snapshot treats hot tub customers as a separate year-round revenue stream with their own pipeline, workflow, chemical delivery program, and seasonal campaigns.

**7. Service Recovery Built Into Review Flow**
The branching review request (4–5 stars → Google; 1–3 stars → owner alert) prevents negative reviews and creates service recovery opportunities. Pool companies that implement this see review volume jump 5–10× within 60 days.

**8. Off-Season Lead Capture**
Winter leads are the most undervalued asset in the pool industry. The off-season nurture sequence + spring pre-booking deposit system converts dormant contacts into committed spring customers before any competitor even starts marketing.

**9. Lead Source Intelligence**
Every lead source is tagged and tracked separately (LSA, referral, Facebook, door hanger, website). After 90 days of using the snapshot, the owner knows exactly which channel generates the most bookings per dollar spent.

**10. Referral System That Actually Works**
Not just a "ask for referrals" reminder — a complete automated referral program with defined incentive, multi-touch follow-up, and tracking. Pool customers are social. Their friends have pools. This is the cheapest revenue growth available.

---

## 14. SNAPSHOT BUILD CHECKLIST

### Contacts & CRM Setup
- [ ] Import existing customer list with pool details
- [ ] Create all custom fields (pool type, size, equipment inventory, water chemistry log, equipment age fields)
- [ ] Set up customer tags (Active Maintenance, VIP Member, Opening Booked, Closing Booked, Hot Tub Customer, Past Customer, LSA Lead, Referral, Equipment Replacement Candidate)
- [ ] Configure contact segmentation for seasonal campaigns

### Pipelines
- [ ] Pipeline 1: New Pool Installation (11 stages)
- [ ] Pipeline 2: Spring Pool Opening (8 stages)
- [ ] Pipeline 3: Fall Pool Closing (7 stages)
- [ ] Pipeline 4: Weekly Maintenance Program (10 stages)
- [ ] Pipeline 5: Equipment Repair & Emergency (9 stages)
- [ ] Pipeline 6: Hot Tub & Spa (10 stages)

### Workflows
- [ ] Workflow 1: Missed Call Text-Back
- [ ] Workflow 2: New Web Lead — Instant Response
- [ ] Workflow 3: Spring Opening Campaign (7-touch)
- [ ] Workflow 4: Fall Closing Campaign (5-touch)
- [ ] Workflow 5: Post-Service Review Request (branching)
- [ ] Workflow 6: Weekly Maintenance Post-Visit Summary
- [ ] Workflow 7: Equipment Repair Follow-Up + Replacement Trigger
- [ ] Workflow 8: Referral Program
- [ ] Workflow 9: Chemical Upsell
- [ ] Workflow 10: Off-Season Nurture Sequence
- [ ] Workflow 11: Equipment Replacement Campaigns (pump, heater, liner, salt cell, filter sand) — 5 separate workflows

### Booking Calendars
- [ ] Calendar 1: Spring Pool Opening (Feb–June, capacity-limited slots)
- [ ] Calendar 2: Fall Pool Closing (Aug–Nov, capacity-limited slots)
- [ ] Calendar 3: Equipment Repair / Emergency Call (year-round, urgent triage)
- [ ] Calendar 4: Maintenance Program Assessment (year-round, new customer consult)
- [ ] Calendar 5: Hot Tub Service (year-round)
- [ ] Configure per-calendar reminders (72hr, 24hr, 2hr)
- [ ] Set technician capacity limits per day
- [ ] Add appointment prep instructions to confirmation messages

### Forms
- [ ] Spring opening intake form
- [ ] Fall closing intake form
- [ ] Maintenance program sign-up form
- [ ] Emergency repair intake form (with equipment details)
- [ ] Hot tub service form
- [ ] Post-service tech report form (water chemistry log)
- [ ] Referral submission form
- [ ] Chemical order form

### Email Templates
- [ ] Spring opening launch email (+ 3 follow-up variants)
- [ ] Fall closing education email (+ 2 follow-up variants)
- [ ] Green pool emergency email
- [ ] Equipment education series (pump, heater, liner, salt cell)
- [ ] Off-season nurture emails (4-email sequence)
- [ ] Holiday hot tub campaign emails
- [ ] Welcome email (new maintenance customer)
- [ ] Annual renewal email
- [ ] Referral program email

### SMS Templates
- [ ] Spring opening (initial + urgency variants)
- [ ] Fall closing outreach
- [ ] Missed call text-back
- [ ] Post-service summary (with water chemistry)
- [ ] Review request (initial ask)
- [ ] Emergency service response
- [ ] Equipment repair confirmation + follow-up
- [ ] Chemical upsell
- [ ] Referral ask
- [ ] Hot tub monthly check
- [ ] Winter re-engagement

### Landing Pages / Funnels
- [ ] Spring opening booking page
- [ ] Fall closing booking page
- [ ] Maintenance program landing page
- [ ] Emergency pool repair page
- [ ] Hot tub service page
- [ ] "Why your pool is green" lead capture page (with free guide offer)
- [ ] Home page funnel (service selector → route to appropriate calendar)

### Integrations
- [ ] Google LSA lead integration (Zapier or native)
- [ ] Facebook Lead Ads integration
- [ ] Google Business Profile (for review request link)
- [ ] Stripe (for deposit collection on spring pre-bookings)
- [ ] QuickBooks / Xero (invoice sync if needed)
- [ ] Optional: Skimmer / Service Autopilot route data import

### Dashboard & Reporting
- [ ] Owner KPI dashboard (live metrics)
- [ ] Seasonal performance snapshot (monthly)
- [ ] Lead source ROI report
- [ ] Conversion funnel tracking (lead → booked → completed → reviewed)
- [ ] Maintenance customer count and churn tracking
- [ ] Equipment replacement pipeline value

### Onboarding Assets (for 1app to include with snapshot)
- [ ] Quick-start guide (PDF): "Your Pool & Spa CRM — Day 1 Checklist"
- [ ] Video walkthrough: How to import existing customers
- [ ] Video walkthrough: How to launch the spring opening campaign
- [ ] Technician field guide: How to submit post-service reports via GHL mobile
- [ ] Water chemistry quick reference card (for post-service SMS values)
- [ ] Seasonal campaign calendar (month-by-month action guide)

---

## APPENDIX A: POOL INDUSTRY TERMINOLOGY REFERENCE

For use in all templates, landing pages, and workflow copy:

**Water Chemistry Terms:**
- **Free Chlorine (FC):** Active sanitizer in the water; target 1–3 ppm (non-salt), 1–5 ppm (salt)
- **Combined Chlorine (CC):** Chloramines — spent chlorine that smells bad and irritates eyes; target < 0.2 ppm
- **Total Chlorine (TC):** FC + CC
- **pH:** Water acidity/alkalinity; target 7.2–7.6 (corrosive below 7.0, scaling above 7.8)
- **Total Alkalinity (TA):** pH buffer; target 80–120 ppm
- **Cyanuric Acid (CYA) / Stabilizer:** UV protection for chlorine; target 30–50 ppm (non-salt), 70–80 ppm (salt); above 100 ppm = chlorine lock
- **Calcium Hardness (CH):** Prevents corrosion and scaling; target 200–400 ppm
- **Shock:** High-dose chlorine treatment to break chloramines and kill algae; weekly in summer
- **Algaecide:** Preventive or treatment chemical for algae; clarifier keeps water clear
- **Backwash:** Reversing water flow through sand/DE filter to flush trapped debris
- **Salt (PPM for saltwater pools):** Target 2,700–3,400 ppm for most salt chlorine generators
- **Bromine:** Alternative sanitizer for spas; target 3–5 ppm

**Equipment Terms:**
- **Skimmer:** Wall-mounted intake that removes surface debris; has a basket inside
- **Main drain:** Bottom intake for circulation; important for safety (VGB compliant drain covers)
- **Returns:** Jets that push filtered water back into pool; aim at 45° down for circulation
- **Pump:** Circulates water through filter; single-speed vs. variable-speed (VSP)
- **Filter:** Sand / DE (Diatomaceous Earth) / Cartridge — removes particles from water
- **Heater:** Gas or heat pump; heats water to desired temperature (typically 82–86°F)
- **Salt chlorine generator (SWG/SCG):** Converts salt to chlorine via electrolysis; salt cell is the electrode
- **Automation system:** Controls pump, lights, heater, valves remotely (Pentair IntelliCenter, Jandy AquaLink, Hayward OmniLogic)
- **Deck jets:** Water features mounted in decking that arc water into pool
- **Fountain/waterfall:** Decorative water features; attached to return lines or separate pump
- **Solar cover / blanket:** Retains heat and reduces evaporation; on/off in summer
- **Winter cover:** Solid or mesh cover that goes on when pool is closed for season
- **Gizzmo / skimmer plug:** Device that goes in skimmer to protect from ice expansion
- **Pressure gauge:** On filter — high pressure = dirty filter; low pressure = pump problem
- **Backwash port / sight glass:** Where waste water exits during backwash

**Service Terms:**
- **Opening:** Spring startup — remove cover, reinstall equipment, start system, treat water
- **Closing / Winterization:** Fall shutdown — lower water, blow out lines, add antifreeze, cover pool
- **Green pool treatment:** Shock, algaecide, extended pump run, brush, vacuum to waste
- **Pool school:** Teaching homeowners how to maintain their own pool
- **Chemical service:** Regular tech visit to test and balance water chemistry
- **Equipment inspection:** Seasonal check of all mechanical components
- **Liner measurement:** Precise measuring of pool dimensions for liner replacement

---

## APPENDIX B: PRICING BENCHMARKS (CANADA — ONTARIO MARKET)

*For 1app use in onboarding and pitch materials:*

| Service | Low End | High End | Notes |
|---|---|---|---|
| Spring opening | $250 | $550 | Varies by pool size and cover type |
| Fall closing | $200 | $450 | With antifreeze lines |
| Weekly maintenance | $75/visit | $200/visit | Varies by pool size and market |
| Bi-weekly maintenance | $100 | $250 | Less common, lower value to customer |
| Green pool treatment | $200 | $600 | Depends on severity and time |
| Pump replacement (VSP) | $800 | $2,000 | Labour + Pentair/Hayward VSP |
| Filter sand replacement | $200 | $500 | Labour + sand |
| Heater replacement | $1,500 | $4,500 | Gas vs. heat pump |
| Salt system replacement | $900 | $2,500 | Cell + control board or full unit |
| Liner replacement | $3,500 | $8,000 | Depends on pool size |
| New pool installation | $35,000 | $120,000+ | Concrete vs. fibreglass vs. vinyl |
| Hot tub purchase | $5,000 | $18,000 | Entry vs. premium brand |
| Hot tub monthly service | $80 | $200 | Chemistry + filter |
| Chemical delivery (monthly) | $60 | $150 | Depends on sanitizer type |

---

*End of Research Document*

**Document prepared by:** Maximus — 1app AI Business Partner
**Ready for build:** This research document is the complete pre-build specification for the 1app Pool & Spa GHL Snapshot. It can be handed directly to a GHL build team, used as a sales pitch document to pool company owners, or used as the foundation for a vertical-specific snapshot product offering.

**Estimated build time:** 40–80 hours for full implementation
**Recommended snapshot price point:** $497–$997 (one-time, white-labeled)
**Monthly SaaS attach:** $197–$397/month (1app platform fee + GHL sub-account)
