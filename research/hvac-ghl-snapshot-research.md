# HVAC GHL Snapshot — Research & Build Blueprint
### For: 1app | Prepared by: Maximus AI
### Document Type: Agency Build Reference
### Status: Draft v1.0 | July 2026

---

## Executive Summary

The HVAC industry is one of the highest-converting verticals for GHL SaaS agencies. HVAC companies are underserved by generic CRM tools — they deal with seasonal demand spikes, after-hours emergencies, maintenance agreement churn, and complex multi-path pipelines (service call → maintenance agreement → equipment replacement). Most existing GHL HVAC snapshots on the market deliver generic automation without understanding the HVAC business model's real revenue architecture.

**The 1app HVAC snapshot opportunity:** Build the most complete, HVAC-native GHL snapshot that maps directly to how HVAC companies actually make money — emergency service conversion, maintenance agreement enrollment, and equipment replacement timing. The company that owns the maintenance agreement owns the replacement sale.

**Target clients:** Residential HVAC contractors, 1–30 trucks, $500K–$15M annual revenue, owner-operated, already running but struggling with follow-up, no-shows, and seasonal cash flow.

---

## Section 1: HVAC Business Pain Points

Understanding what keeps an HVAC owner up at night is the foundation of every workflow we build.

### 1.1 Seasonal Demand Spikes
HVAC revenue is brutally seasonal. Air conditioning calls spike in June–August when temperatures climb. Furnace and heat pump calls spike in October–December when overnight temperatures drop. The off-season creates cash flow problems — technicians are idle, trucks sit, and the owner is still paying fixed costs.

**Pain:** "I can't handle the volume in June and I'm starving in October."

**GHL opportunity:** Pre-season campaign automation — spring AC startup campaigns (April) and fall furnace tune-up campaigns (September) should be triggered automatically from a calendar-based workflow. These campaigns fill the shoulder-season schedule before demand spikes and create consistent revenue through maintenance agreements.

### 1.2 Emergency After-Hours Service Calls
HVAC emergencies don't respect business hours. A compressor failure at 11pm on a July Friday, a no-heat call at 6am on a January Monday — these are the highest-urgency, highest-margin calls in the business. Most small HVAC companies miss these calls entirely because they don't have an answering service or AI agent.

**Pain:** "We're losing thousands in emergency call revenue every weekend."

**GHL opportunity:** Missed Call Text Back with AI voice agent for after-hours triage. When a call comes in after hours, the AI agent captures: urgency level, equipment type (air handler, condenser, furnace, heat pump), address, and availability — then creates a contact and opportunity in GHL and notifies the on-call tech via SMS.

### 1.3 Maintenance Agreement Churn
Maintenance agreements (also called service agreements, comfort clubs, or PM plans) are the most valuable recurring revenue product in HVAC. A properly priced maintenance agreement ($150–$350/year for residential) includes two tune-ups annually — one cooling tune-up in spring, one heating tune-up in fall. Customers on maintenance agreements:
- Spend 2–3x more lifetime with the company
- Convert to equipment replacement at 3x the rate of non-agreement customers
- Are far more likely to refer

**Pain:** "We sell 200 maintenance agreements but only 60% renew. We're losing $18K/year in lapsed agreements."

**GHL opportunity:** Maintenance agreement renewal workflow — automated 60-day, 30-day, 14-day, and 7-day renewal reminders via SMS and email. Tie renewal to the technician's last visit date. Include a one-click renewal link. Automate "lapsed agreement re-enrollment" campaigns targeting customers who didn't renew.

### 1.4 Equipment Replacement Timing
Residential HVAC equipment (central air conditioners, furnaces, heat pumps, air handlers) has an average lifespan of:
- Central A/C / condenser: 12–17 years
- Gas furnace: 15–20 years
- Heat pump: 10–15 years
- Air handler / fan coil: 15–20 years

Equipment approaching end-of-life is the highest-revenue opportunity in HVAC — a full system replacement (condenser + air handler or gas pack) averages $8,000–$20,000+ depending on tonnage and SEER rating. The company that has the maintenance agreement almost always gets the replacement call. The company that doesn't maintain the equipment usually loses the replacement.

**Pain:** "We installed 400 systems 10–14 years ago and we're not proactively reaching out about replacement. They're calling our competition."

**GHL opportunity:** Equipment age tracking via custom fields (install date, unit age, tonnage, SEER rating, refrigerant type — R-22 units are prime replacement targets). Automated replacement nurture sequence triggered when equipment hits age 10, 12, and 15 years. "Is your system this old?" campaigns with financing offer CTAs.

### 1.5 Technician Scheduling and Dispatch Inefficiency
HVAC business owners spend hours daily playing dispatch coordinator — calling techs, re-routing trucks, managing no-shows, handling emergency call-ins that blow up the day's schedule.

**Pain:** "My dispatcher spends 3 hours a day on the phone just moving jobs around."

**GHL opportunity:** Automated booking confirmation + 24-hour reminder + 2-hour reminder sequences via SMS reduce no-shows by 30–40%. Self-reschedule links in reminder messages reduce inbound reschedule calls. Tech assignment notifications via SMS.

### 1.6 Slow Invoicing and Payment Collection
HVAC companies frequently finish a service call and forget to collect — or send paper invoices that take weeks to pay. Cash flow suffers. The owner doesn't know what's outstanding.

**Pain:** "We have $60K in outstanding invoices from the last 90 days."

**GHL opportunity:** Post-service payment link automation — 1 hour after job marked complete, send SMS with payment link. 24-hour follow-up if unpaid. 72-hour final reminder before escalating to manual follow-up.

### 1.7 No-Show Rate
Residential HVAC no-show rates run 15–25% without confirmation and reminder automation. A missed tune-up appointment wastes a tech's drive time plus the open slot.

**Pain:** "We have 5–8 no-shows per week and it's costing us 15% of our capacity."

**GHL opportunity:** 3-step appointment confirmation sequence — day before (voice/SMS), 2 hours before (SMS with address), 30 minutes before (tech is on the way text). One-click confirm or reschedule link reduces no-shows by 35–40%.

### 1.8 Google Review Generation
HVAC buying decisions are heavily influenced by Google reviews. A company with 150+ 4.9-star reviews dominates LSA (Local Services Ads) rankings vs. a competitor with 40 reviews at 4.2 stars.

**Pain:** "Our competitor has 800 reviews and we have 90. We know we're losing jobs over it."

**GHL opportunity:** Automated post-service review request — 2 hours after job completed, send SMS with direct Google review link. If no action in 48 hours, follow-up email. Positive review response templates for the owner.

---

## Section 2: GHL HVAC Snapshots Currently on Market

### 2.1 What Exists
Based on research, the current GHL HVAC snapshot market includes:

**Basic/Generic Snapshots:**
- Generic "home services" snapshots that include HVAC as one of 5+ trades — no real HVAC specificity
- Simple missed call text back + booking calendar setups rebranded as "HVAC snapshots"
- Templates that replicate a basic sales pipeline without understanding HVAC's service vs. maintenance vs. replacement revenue structure

**More Advanced Snapshots (referenced in YouTube content, 2025–2026):**
- "HVAC AI Snapshot" variations — include AI agent + funnel + basic workflows
- Snapshots with funnel pages, booking calendar, missed call text back, and a 3–5 step email nurture
- Some include seasonal campaign email templates

### 2.2 What's Missing in Existing Snapshots

This is where 1app's snapshot wins:

1. **No maintenance agreement pipeline** — existing snapshots treat all HVAC leads the same. There's no distinction between a service call lead (one-time transaction), maintenance agreement prospect (recurring revenue), and equipment replacement lead ($8K–$20K sale). These need entirely separate pipelines and workflows.

2. **No equipment age lifecycle automation** — no snapshot tracks install date, equipment age, tonnage, or SEER rating to trigger proactive replacement campaigns. This is the single biggest revenue opportunity in HVAC.

3. **No technician dispatch integration** — after-hours AI triage with tech notification is rarely built properly.

4. **No seasonal campaign calendar** — most snapshots have generic email templates. None build a full 12-month seasonal campaign calendar with pre-scheduled spring and fall activation dates.

5. **No commercial/property manager pipeline** — HVAC companies serving apartment complexes, commercial buildings, and HOAs need a completely different workflow with property manager contacts, multiple unit tracking, and quarterly PM scheduling.

6. **No financing workflow** — equipment replacements over $8K frequently require financing. No existing snapshot includes a financing pre-qualification step in the replacement pipeline.

7. **No refrigerant phase-out workflow** — R-22 refrigerant was phased out January 2020. Units still running R-22 are prime replacement targets. No snapshot tracks refrigerant type and triggers replacement campaigns for R-22 units.

8. **No review segmentation** — most snapshots blast review requests to all customers. The 1app snapshot should only trigger review requests for service calls marked "resolved" or rated positive by the tech. Unhappy customers should be routed to a recovery workflow, not asked for a public review.

---

## Section 3: HVAC Pipeline Architecture

### 3.1 Pipeline 1 — Service Call Pipeline
**Purpose:** Manage inbound repair and diagnostic calls from new and existing customers
**Average ticket:** $150–$800 (diagnostic + repair)
**Volume:** Highest volume pipeline, especially in peak season

| Stage | Description |
|---|---|
| New Inquiry | Web form, phone, missed call — contact created |
| Scheduled | Service call appointment booked |
| Confirmed | Customer confirmed appointment (1-click or reply) |
| En Route | Technician notified, "on the way" SMS sent |
| On Site | Job in progress |
| Invoice Sent | Service completed, payment link sent |
| Paid | Payment received |
| Closed — Won | Job complete, review request triggered |
| Closed — No Show | Reschedule sequence triggered |
| Closed — Lost | Re-engagement follow-up at 30 days |

**Upsell trigger in this pipeline:** After every service call, if equipment is 8+ years old → enter equipment replacement nurture. After every service call → offer maintenance agreement enrollment.

---

### 3.2 Pipeline 2 — Maintenance Agreement Pipeline
**Purpose:** Track, sell, and renew residential maintenance agreements (comfort clubs, PM plans)
**Average value:** $150–$350/year | LTV: $800–$3,000 per household
**This is the highest-LTV pipeline in residential HVAC**

| Stage | Description |
|---|---|
| Prospect | Customer identified as non-agreement (post-service call) |
| Agreement Offer Sent | Maintenance agreement pitch sent via SMS/email |
| Agreement Quoted | Quote sent with plan options (Basic/Standard/Premium) |
| Agreement Signed | Agreement enrolled, first tune-up scheduled |
| Active — Cooling Season | Spring tune-up due |
| Active — Heating Season | Fall tune-up due |
| Renewal Due (60 Days) | Renewal reminder sequence starts |
| Renewal Due (30 Days) | Second reminder |
| Renewal Due (7 Days) | Final reminder with renewal link |
| Renewed | Agreement renewed for next year |
| Lapsed | Agreement expired, re-enrollment campaign triggered |
| Cancelled | Exit survey triggered |

**Note:** Maintenance agreement customers should be tagged `MA-Active` in GHL. This tag triggers their inclusion in seasonal tune-up campaign automations.

---

### 3.3 Pipeline 3 — Equipment Replacement Pipeline
**Purpose:** Track and close equipment replacement opportunities (condenser, heat pump, furnace, air handler, full system)
**Average ticket:** $6,000–$20,000+ depending on tonnage and system type
**Close cycle:** 7–45 days (longer for financing, commercial)

| Stage | Description |
|---|---|
| Replacement Lead — Inbound | Customer called with equipment failure or request for quote |
| Replacement Lead — Proactive | Triggered by equipment age workflow |
| Comfort Consultation Booked | In-home assessment scheduled |
| Comfort Consultation Completed | System load calculation done, proposal pending |
| Proposal Sent | Full replacement quote delivered (including equipment specs: tonnage, SEER rating, brand) |
| Proposal Reviewed | Customer acknowledged receipt |
| Financing Pre-Qual Sent | Financing application link sent if ticket > $6K |
| Financing Approved | Deal can close, installation scheduled |
| Deposit Received | Job confirmed, equipment ordered |
| Installation Scheduled | Install date set, crew assigned |
| Installation Completed | System commissioned, test run complete |
| Follow-Up — 30 Day | Post-install comfort check call |
| Closed — Won | Review request + maintenance agreement offer sent |
| Closed — Lost | Lost reason tagged, follow-up in 90 days |

**Custom fields for this pipeline:**
- Old equipment tonnage (1.5, 2, 2.5, 3, 3.5, 4, 5 ton)
- Old equipment SEER rating
- Old equipment refrigerant type (R-22, R-410A, R-32, R-454B)
- Old equipment install year
- New equipment brand
- New equipment SEER2 rating
- New equipment tonnage
- Permit required (Y/N)
- Financing (Y/N), lender, term

---

### 3.4 Pipeline 4 — New Construction / Builder Pipeline
**Purpose:** Track relationships and bids with homebuilders and general contractors
**Average ticket:** $8,000–$25,000 per new construction installation
**Sales cycle:** 30–180 days

| Stage | Description |
|---|---|
| Builder Contact | GC or developer contact created |
| Bid Requested | Project specs received, load calc initiated |
| Bid Submitted | Proposal sent with equipment spec sheet |
| Bid Under Review | Builder reviewing competitive quotes |
| Awarded | Job awarded, contract signed |
| Rough-In Scheduled | Ductwork and rough-in phase |
| Trim-Out Scheduled | Equipment installation phase |
| Final Inspection | City inspection and commissioning |
| Warranty Registered | Equipment warranty filed, owner enrolled in CRM |
| Closed — Won | Homeowner added to service pipeline |

---

### 3.5 Pipeline 5 — Commercial / Property Manager Pipeline
**Purpose:** Track B2B relationships with property managers, building owners, HOAs, and commercial tenants
**Average ticket:** $500–$50,000+ depending on commercial rooftop unit (RTU) size and scope
**Billing:** Quarterly PM contracts, net-30 invoicing

| Stage | Description |
|---|---|
| Property Manager Contact | PM contact created with property count |
| PM Audit Scheduled | Walk-through of all units on property |
| PM Proposal Sent | Quarterly/annual PM contract proposal |
| Contract Signed | PM contract enrolled |
| Q1 PM Service | Winter/spring PM completed |
| Q2 PM Service | Summer PM completed |
| Q3 PM Service | Fall PM completed |
| Q4 PM Service | Winter PM completed |
| Annual Renewal | Contract renewal proposal sent |
| Equipment Replacement Flag | Unit flagged for replacement recommendation |

---

## Section 4: HVAC-Specific Workflow Map

### 4.1 Emergency Service Call Workflow (After-Hours AI Triage)
**Trigger:** Missed call after hours (6pm–7am weekdays, weekends)
**Goal:** Capture the lead, triage urgency, notify on-call tech

```
Step 1 (Immediate): Missed call detected → Auto-send SMS:
"Hi, this is [Company Name]! We missed your call but we're here to help. 
Is this an HVAC emergency? Reply YES for emergency or NO for next-day service."

Step 2A (YES — Emergency): Reply received →
"We've got you. Our on-call tech will call you within 30 minutes. 
What's the issue? (e.g., no A/C, no heat, water leak, strange noise)"

Step 2B (NO — Non-Emergency): Reply received →
"No problem! Let's get you scheduled. What type of service do you need? 
(1) AC Repair (2) Heating Repair (3) Maintenance Tune-Up (4) Free Estimate"

Step 3: Contact created in Service Call Pipeline → Stage: New Inquiry
Step 4 (Emergency): SMS to on-call tech with contact name, address, equipment issue
Step 5 (Emergency): Opportunity created, priority tag applied
Step 6 (Next morning): If non-emergency and no booking → Schedule follow-up call at 8am
```

---

### 4.2 Appointment Confirmation Workflow
**Trigger:** Appointment booked (service call or tune-up)
**Goal:** Confirm appointment, reduce no-shows, set expectations

```
Step 1 (Immediate after booking): Confirmation SMS:
"✅ Confirmed! [Company Name] is scheduled for your [Service Type] on 
[Date] between [Time Window]. Tech: [Name]. Questions? Reply or call [Phone]."

Step 2 (Day before, 4pm): Reminder SMS:
"Reminder: [Company Name] arrives tomorrow between [Time Window] for your 
[Service Type]. Reply CONFIRM to lock it in or RESCHEDULE if needed."

Step 3A: Reply CONFIRM → Move pipeline to "Confirmed", notify tech
Step 3B: Reply RESCHEDULE → Send self-schedule link, move to "Rescheduling"
Step 3C: No reply by 8pm → Automated call attempt (IVR or AI)

Step 4 (Day of, 2 hours before): SMS:
"[Tech Name] is heading your way in about 2 hours. Make sure someone 
15+ and your equipment is accessible. See you soon! — [Company Name]"

Step 5 (30 min before): Optional tech-triggered SMS:
"[Tech Name] is 30 minutes out. Be there shortly! — [Company Name]"
```

---

### 4.3 Post-Service Follow-Up Workflow
**Trigger:** Job marked "Completed" in pipeline
**Goal:** Payment, review, upsell maintenance agreement, upsell replacement if applicable

```
Step 1 (1 hour after completion): Payment SMS (if invoice not paid):
"Hi [First Name]! Your [Service Type] is complete. Invoice total: $[Amount]. 
Pay securely here: [Link]. Thank you for choosing [Company Name]!"

Step 2 (2 hours after completion): Review request SMS:
"[First Name], how did we do today? Your feedback means everything to us. 
Leave us a quick Google review: [Link] — It takes 60 seconds and helps us a ton!"

Step 3 (24 hours after completion, if equipment age > 8 years): Replacement awareness SMS:
"Hi [First Name]! Quick note — your [Equipment Type] is [X] years old. 
Units like yours typically last 12–17 years. When you're ready to talk replacement options 
(we offer great financing), we're here. No pressure — just want to keep you informed. — [Company]"

Step 4 (3 days after completion, if no maintenance agreement): MA upsell SMS:
"Did you know [Company Name] customers with a Comfort Club Maintenance Agreement 
get priority service, annual tune-ups, and 15% off repairs? Starting at just $[Price]/year. 
Interested? Reply PLAN and we'll send details."

Step 5 (7 days after completion, if no MA): Email:
"[Maintenance Agreement Benefits] — Full email with pricing tiers and sign-up link"

Step 6 (30 days): Check-in SMS:
"Hi [First Name]! Just checking in — is everything running smoothly since your 
[Service Type]? Any questions or concerns, we're just a text away. — [Company Name]"
```

---

### 4.4 Maintenance Agreement Renewal Workflow
**Trigger:** MA renewal date approaching (calculated from enrollment date)
**Goal:** Maximize renewal rate, reduce churn

```
Step 1 (60 days before expiry): Email — "Your Comfort Plan is Expiring Soon"
Subject: "Your [Company Name] Comfort Club renews in 60 days"
Body: Summary of benefits used (tune-ups, discounts), renewal price, one-click renewal link

Step 2 (30 days before expiry): SMS:
"[First Name], your Comfort Club membership expires [Date]. Renew now to keep 
priority service + your annual tune-ups: [Renewal Link]. Any questions? Reply here."

Step 3 (14 days before expiry): Email — "Don't miss your renewal window"
Body: Urgency framing — "Without your plan, service calls are full price. Renew now."

Step 4 (7 days before expiry): SMS (final):
"Last call [First Name]! Your Comfort Club expires in 7 days. Renew in 30 seconds: 
[Link]. After expiry, new member pricing applies. — [Company Name]"

Step 5 (Day of expiry — not renewed): Tag: MA-Lapsed
→ Enter Lapsed MA Re-enrollment Campaign (30/60/90 day follow-up)

Step 6 (Renewed): 
→ Tag: MA-Active
→ SMS: "You're all set! Comfort Club renewed through [New Date]. 
We'll be in touch to schedule your next seasonal tune-up. — [Company Name]"
→ Schedule next tune-up based on season
```

---

### 4.5 Equipment Replacement Nurture Workflow (Age-Triggered)
**Trigger:** Custom field "Install Year" → equipment age calculation
**Logic:** Tag customer when equipment reaches 10 years old, 12 years old, 15 years old

```
AGE 10 YEARS — Entry into Replacement Awareness Sequence:

Email 1 (Day 1): "How Long Do HVAC Systems Last?"
Subject: "Your [Equipment Type] is 10 years old — here's what to know"
Body: Educational content on equipment lifespan, efficiency decline, SEER2 ratings, 
R-22 phase-out if applicable. Soft CTA: "Book a free equipment health check."

SMS (Day 3): "Hi [First Name]! Your [Equipment Type] is 10 years old this year. 
Modern systems are 30–50% more efficient. Would a free efficiency consultation be helpful? 
Reply YES and we'll set something up. — [Company Name]"

Email 2 (Day 14): "The Real Cost of Running an Old HVAC System"
Body: Cost comparison — old system at low SEER vs. new system at high SEER2. 
ROI calculation. Financing options. CTA: "See our current replacement specials."

AGE 12 YEARS — Upgrade to Replacement Consideration Sequence:

Email 1: "Is Your System Getting Ready to Retire?"
Body: Signs it's time to replace (frequent repairs, refrigerant top-offs, uneven cooling, 
high utility bills). "If you've spent $500+ on repairs in the last 2 years, replacement 
may be the smarter financial move."

SMS: "Time for a free comfort consultation? Your [Equipment Type] is 12 years old 
and may be costing you more than you think. Free assessment — no obligation. 
Book here: [Link] — [Company Name]"

AGE 15 YEARS — Urgency Replacement Sequence:

Email: "Your System is Living on Borrowed Time"
Body: High urgency. Statistics on failure rates for 15+ year equipment. 
Equipment failure in summer heat/winter cold messaging. Emergency replacement 
wait times. Financing available. "Replace on YOUR timeline, not when it breaks."

SMS: "Heads up [First Name] — 15-year-old [Equipment Type] systems have a 
high failure rate heading into [Season]. Don't get caught without A/C in July. 
Let's talk options: [Booking Link]. — [Company Name]"

R-22 REFRIGERANT TRIGGER (regardless of age):
Contact tagged R22-Unit → Enter R-22 Phase-Out Campaign immediately

Email: "R-22 Refrigerant is No Longer Being Manufactured — What This Means for You"
Body: R-22 background, cost increase ($100–$200+/lb vs. $10–$15/lb for R-410A/R-32). 
"Your system may be costing you $800–$2,000 per refrigerant recharge. 
A new system is often cheaper long-term. Let's run the numbers together."
```

---

### 4.6 Spring AC Startup Campaign (Seasonal — April)
**Trigger:** Date-based automation — fires April 1 each year
**Target:** All contacts tagged `MA-Active` (scheduled tune-up) + non-MA customers (upsell opportunity)

**For MA-Active Customers:**
```
SMS (April 1): "Spring is here! Time to schedule your annual A/C tune-up 
included in your Comfort Club. Book your spot now before we fill up: [Link] — [Company Name]"

Email (April 1): "Schedule Your Spring A/C Tune-Up — It's Included in Your Plan"
Body: What the cooling tune-up covers (coil cleaning, refrigerant check, 
capacitor test, thermostat calibration, filter check, blower inspection)

SMS (April 14, if not booked): "Still need to book your spring A/C tune-up? 
Slots are filling fast. Lock yours in: [Link] — [Company Name]"
```

**For Non-MA Customers:**
```
SMS (April 1): "Beat the summer rush! [Company Name] spring A/C tune-ups 
are booking fast. $[Price] covers full system inspection + cleaning. 
Book now: [Link]"

Email: "Don't Wait Until Your A/C Breaks Down on the Hottest Day of the Year"
Body: Tune-up benefits, spring pricing, maintenance agreement upsell 
("Get this tune-up FREE when you join our Comfort Club")
```

---

### 4.7 Fall Furnace/Heat Pump Tune-Up Campaign (Seasonal — September)
**Trigger:** Date-based automation — fires September 5 each year
**Target:** Same logic as Spring campaign, flipped for heating season

**For MA-Active Customers:**
```
SMS (September 5): "Fall is coming — time to schedule your annual heating tune-up! 
Your Comfort Club includes this service. Book before slots fill: [Link] — [Company Name]"

Email: "Don't Get Caught Without Heat This Winter"
Body: What the heating tune-up covers (heat exchanger inspection, 
flue gas analysis, gas pressure check, burner cleaning for furnace; 
refrigerant check, defrost cycle test, reversing valve for heat pump)
```

**For Non-MA Customers:**
```
SMS (September 5): "Fall furnace tune-ups: $[Price]. Keep your family warm all winter. 
Book now before October rush: [Link] — [Company Name]"

Email: "Is Your Furnace Ready for Winter? Book Your Tune-Up Now."
```

---

### 4.8 Review Generation Workflow (Post-Service)
**Trigger:** Pipeline stage moved to "Closed — Won" after service, tune-up, or installation

```
Step 1 (2 hours after job close): SMS — Primary ask:
"Hi [First Name]! We hope [Tech Name] took great care of you today. 
Could you take 60 seconds to share your experience on Google? 
It means the world to our team: [Google Review Link]. Thank you! — [Company Name]"

Step 2 (48 hours later, if no review detected): Email — Secondary ask:
Subject: "[First Name], your review helps families like yours find us"
Body: Personal note from owner. Social proof (current review count). 
Direct link to Google review page.

Step 3 (7 days later, if no review): Final SMS:
"[First Name], still thinking about that Google review? 😊 
Even 2–3 sentences helps our small business a ton. Here's the link: [Link]
No worries if not — we're just glad we could help! — [Company Name]"

NEGATIVE EXPERIENCE BRANCH:
If tech flags job as "Issue / Callback Required" → DO NOT trigger review request
→ Trigger Recovery Workflow:
SMS: "Hi [First Name], we want to make sure you're 100% satisfied. 
Did everything meet your expectations today? Reply YES or let us know 
what we can improve. — [Company Name]"
```

---

### 4.9 Commercial / Property Manager Workflow
**Trigger:** Contact tagged as Property-Manager or Commercial-Account

```
Initial Outreach (Cold Property Manager):
Email 1: "Property Manager intro — quarterly PM contracts for [City] properties"
Subject: "Cut HVAC headaches in half — here's how we work with property managers"
Body: Property manager pain points (after-hours tenant calls, emergency replacement costs, 
unit-by-unit tracking). Offer: Free property HVAC audit — walk every unit, 
document equipment age, tonnage, refrigerant type, condition. 
CTA: "Schedule your free property audit."

Follow-up SMS (Day 3 if no reply):
"Hi [PM Name], sent you an email about our property HVAC program. 
Do you handle HVAC for your properties? Would love 10 minutes to talk. — [Company Name]"

Phone call attempt (Day 7)

Monthly PM Clients — Ongoing Sequence:
Monthly email: Equipment status report summary
Quarterly: PM scheduling reminder with property-specific calendar
Annual: Contract renewal proposal with updated pricing
Emergency: PM flagged for after-hours → Priority dispatch, separate notification chain
```

---

### 4.10 Filter Replacement Reminder Workflow
**Trigger:** Date-based, based on filter replacement frequency (tagged on contact: 1-month, 3-month, 6-month)
**Goal:** Keep company top-of-mind, drive online sales or upsell maintenance visit

```
1-Month Filter Customers:
SMS (every 28 days): "Time to swap your filter! [First Name], your 1" filter should 
be changed monthly. Grab one at any hardware store or reply DELIVERY if you want us 
to drop off a 6-pack. — [Company Name]"

3-Month Filter Customers:
SMS (every 85 days): "Filter reminder! It's been about 3 months since your last 
filter change. Don't let a dirty filter hurt your system's efficiency. 
Reply HELP if you'd like a tech to swing by. — [Company Name]"

6-Month Filter Customers:
Email (every 175 days): Seasonal filter reminder with system care tips.
SMS follow-up if no engagement.
```

---

## Section 5: Lead Sources and Attribution

### 5.1 Lead Source Tracking (GHL Custom Field)
Every contact should have a Lead Source custom field populated. This drives attribution reporting and campaign optimization.

**Lead Sources to track:**
- Google LSA (Local Services Ads)
- Google PPC (Pay-Per-Click)
- Google Organic / SEO
- Google Business Profile (GBP call)
- Angi / HomeAdvisor
- Thumbtack
- Home Warranty (American Home Shield, First American, Old Republic, etc.)
- Referral — Customer (which customer?)
- Referral — Contractor (plumber, electrician, roofer)
- Referral — Property Manager
- Facebook Ad
- Instagram Ad
- Direct Mail / Postcard
- Yard Sign
- Truck Wrap
- Repeat Customer (no new marketing needed)
- Walk-In / In-Person

### 5.2 Home Warranty Leads
Home warranty calls (American Home Shield, First American, Choice Home Warranty, etc.) represent a significant volume source for many HVAC companies. These calls are dispatched from the warranty company, not self-generated.

**Specific challenge:** Home warranty work is typically low-margin (the warranty company pays a capped service fee, often $75–$150 per call), but home warranty customers often need non-covered repairs or replacement work that falls outside the warranty scope. This is where GHL automation creates real revenue.

**Home Warranty Workflow:**
```
Tag: Home-Warranty-Lead
Source: [Warranty Company Name]

After service call:
SMS: "Hi [First Name]! We hope we took good care of your [issue] today. 
Did you know [Company Name] also handles AC and heating services outside your 
home warranty? We'd love to be your go-to HVAC team for everything. 
Let's stay in touch! — [Company Name]"

30 days later: Maintenance agreement offer
60 days later: If equipment is old — replacement awareness email
```

### 5.3 Angi / HomeAdvisor Leads
Angi and HomeAdvisor leads tend to be price-shoppers. Speed-to-lead is critical — response within 5 minutes increases close rate by 400%.

**Angi Lead Workflow:**
```
Trigger: Lead form submitted (via Zapier/webhook integration)
Step 1 (Immediate): SMS — "Hi [First Name], this is [Company Name]! 
We just got your request for [Service Type]. We have availability this week — 
what time works best? [Booking Link] or reply to this message. — [Rep Name]"

Step 2 (5 min later, if no reply): Phone call attempt
Step 3 (1 hour, if no reply): SMS follow-up
Step 4 (3 hours, if no reply): Email with company info, reviews, booking link
Step 5 (24 hours, if no reply): Final SMS — "Still interested in [Service]? 
We can get you on the schedule this week. — [Company Name]"
Step 6 (72 hours, if no reply): Move to Cold Lead nurture sequence
```

### 5.4 Google LSA Leads
Google Local Services Ad leads are the highest intent leads in HVAC marketing. These homeowners are actively searching for HVAC help right now.

**LSA Lead Handling Protocol:**
- Response target: < 2 minutes during business hours, < 30 minutes after hours
- Auto-reply SMS within 60 seconds: "Hi! [Company Name] here — we just got your request! Someone from our team will call you in the next few minutes. — [Company Name]"
- Phone call attempt triggered immediately
- If no answer: Leave voicemail + send SMS with booking link
- LSA leads should be priority-tagged in GHL: `LSA-Lead`

---

## Section 6: SMS and Email Templates

### 6.1 Emergency Tone Templates

**Emergency Inquiry Response:**
```
"🚨 [Company Name] Emergency Line — We're here! Our on-call technician is being 
notified right now. What's the situation? (No A/C / No Heat / Water Leak / Other) 
— Reply or call [Phone] for fastest response."
```

**Emergency Dispatch Confirmation:**
```
"Hi [First Name]! [Tech Name] is on the way to [Address]. ETA: approximately 
[X] minutes. If anything changes, reply here or call [Phone]. — [Company Name]"
```

**After-Hours No Heat (High Urgency Variant):**
```
"❄️ No heat in [Month]? We understand — that's a real emergency. 
We dispatch after-hours for heating calls. [Tech Name] will call you within 
20 minutes to confirm arrival time. Stay warm! — [Company Name]"
```

**After-Hours No A/C (Summer):**
```
"🌡️ We know how brutal a broken A/C feels in [Month]. Our on-call tech 
will reach out within 30 minutes. In the meantime, close blinds, use fans, 
and stay hydrated. Help is coming! — [Company Name]"
```

---

### 6.2 Seasonal Campaign Tone Templates

**Spring A/C Tune-Up Launch:**
```
Subject (Email): "Your A/C is about to work harder than it has in months — is it ready?"

SMS: "Summer's coming — is your A/C ready? Schedule your spring tune-up 
before the heat hits: [Booking Link]. Book now → Skip the wait in June. 
— [Company Name]"
```

**Fall Furnace Tune-Up Launch:**
```
Subject (Email): "Don't wait until you wake up freezing — book your furnace tune-up now"

SMS: "Cold nights are coming. Book your fall furnace tune-up before the 
October rush. Comfort Club members: your tune-up is already included! 
[Booking Link] — [Company Name]"
```

**Filter Reminder:**
```
SMS: "Quick heads up [First Name] — time to change your air filter! 
A clean filter = better air quality + lower energy bills + longer equipment life. 
Any questions, we're here. — [Company Name]"
```

---

### 6.3 Maintenance Agreement Upsell Templates

**Post-Service MA Pitch (SMS):**
```
"[First Name], glad we got your [issue] sorted! Did you know our Comfort Club 
members get 2 tune-ups/year, priority scheduling, and 15% off repairs? 
Starting at $[Price]/year. Interested? Reply PLAN and we'll send details. — [Company Name]"
```

**MA Welcome Message:**
```
"Welcome to the Comfort Club, [First Name]! 🎉 Your membership is active 
and your first tune-up is being scheduled. Here's your member portal: [Link]. 
Questions? We're always a text away. — [Company Name]"
```

**MA Renewal — Warm Tone:**
```
Subject: "Quick note about your [Company Name] Comfort Club membership"

Hi [First Name],

Just a heads-up — your Comfort Club membership is coming up for renewal on [Date].

This year you received: [X] tune-up(s), [Y] priority service call(s), 
and saved approximately $[Amount] with your 15% member discount.

Renew for another year in one click: [Renewal Link]

Same great price: $[Amount]/year.

Talk soon,
[Owner Name]
[Company Name]
```

---

### 6.4 Equipment Replacement Templates

**Soft Replacement Awareness (Age 10):**
```
Subject: "[First Name], your [Equipment] is 10 years old — here's what to know"

Hi [First Name],

We noticed your [Equipment Type] was installed in [Year], which puts it at 
about 10 years old. The good news: it likely has several good years left!

That said, systems this age often start showing signs of efficiency decline:
• Higher monthly utility bills
• Longer run cycles to reach set temperature
• Occasional refrigerant top-offs

A modern [Equipment Type] can be 30–50% more efficient, which often pays for 
itself in energy savings within 5–8 years.

No pressure — just want to keep you informed. If you ever want a free 
efficiency assessment, we're happy to run the numbers.

Stay comfortable,
[Owner Name] | [Company Name]
```

**Urgent Replacement (R-22 Units):**
```
Subject: "Important: Your A/C uses R-22 refrigerant — here's what changed"

Hi [First Name],

We want to make sure you're aware of something important regarding your current 
air conditioning system.

Your unit uses R-22 refrigerant (also called Freon), which has been completely 
phased out of production since January 2020. This means:

• R-22 is increasingly scarce — prices have risen to $100–$200+ per pound
• A single refrigerant charge can cost $800–$2,000 (vs. $200–$400 for modern refrigerant)
• Parts are becoming harder to source

If your system ever needs a refrigerant recharge, you're facing significant cost.

In many cases, replacement with a new, efficient system is the smarter financial choice.

We offer free in-home consultations and flexible financing options.

Would you like us to put together a no-obligation comparison? 
Just reply to this email or call us at [Phone].

[Owner Name] | [Company Name]
```

---

## Section 7: Booking Flow Architecture

### 7.1 Emergency Booking Flow
**Channel:** Phone / SMS / Web chat
**Required fields:** Name, address, phone, issue description
**Goal:** Book or dispatch within 15 minutes

```
Trigger: Incoming contact (call, SMS, web form)
→ Triage: Emergency or non-emergency?
→ Emergency: Immediate technician notification + ETA confirmation
→ Non-emergency after hours: Book next available + reminder sequence
→ Non-emergency business hours: Live booking → calendar confirmation
```

**No booking form for emergencies.** Emergencies bypass the calendar and go directly to dispatch notification. The contact record and opportunity are created automatically.

### 7.2 Scheduled Tune-Up Booking Flow
**Channel:** Inbound call, email campaign, SMS campaign, web calendar
**Required fields:** Name, address, phone, email, service type, equipment type

```
Step 1: Customer selects "Tune-Up" from web calendar or clicks SMS booking link
Step 2: Select equipment type (A/C, Furnace, Heat Pump, Full System)
Step 3: Select available time window (morning / afternoon)
Step 4: Confirmation page with tech name and what to expect
Step 5: Immediate confirmation SMS + email
Step 6: Reminder sequence activates (day before, 2 hours before)
```

**Calendar note:** Block seasonal windows by technician capacity. Don't allow unlimited bookings on one day. GHL calendar should cap tune-up bookings at technician max (typically 6–8 tune-ups per tech per day).

### 7.3 Equipment Replacement Consultation Booking Flow
**Channel:** AI agent, email campaign, SMS campaign, web form
**Required fields:** Name, address, phone, email, current equipment type, current equipment age, primary concern (efficiency, breakdown, cost)

```
Step 1: Landing page — "Book Your Free Comfort Consultation"
Headline: "Is Your System Ready to Retire? Find Out in 60 Minutes — Free."
Form collects: Name, address, phone, email, equipment type, age, concern

Step 2: Immediate confirmation SMS + email
"We'll have one of our comfort advisors at [Address] on [Date] at [Time]. 
They'll assess your current system, run a load calculation for your home's 
exact needs, and present your options — zero pressure, zero obligation."

Step 3: Pre-appointment email (day before):
"What to expect at your comfort consultation: [What we'll look at, what questions to prepare]"

Step 4: Post-consultation proposal follow-up sequence
(24 hours if no decision, 48 hours, 7 days)
```

---

## Section 8: Maintenance Agreement Upsell System (Highest LTV Play)

### 8.1 Business Case

Maintenance agreements are the backbone of a sustainable HVAC business. The math:
- Average MA price: $200/year (residential)
- Average MA customer LTV: $1,500–$4,000 over lifetime
- Average non-MA customer LTV: $400–$800
- MA customer equipment replacement conversion rate: 3–4x higher
- MA customers refer at 2x the rate of non-MA customers

A residential HVAC company with 500 active maintenance agreements generates $100,000/year in guaranteed recurring revenue before a single service call is booked.

**The 1app snapshot must make selling and managing maintenance agreements the easiest thing an HVAC company does.**

### 8.2 MA Tiered Pricing Structure
Build the snapshot with three maintenance agreement tiers:

**Bronze / Basic Plan (~$149–$179/year)**
- 1 annual tune-up (customer chooses cooling OR heating)
- 10% discount on repairs
- Priority scheduling (next available, not emergency)

**Silver / Standard Plan (~$199–$249/year)**
- 2 annual tune-ups (spring cooling + fall heating)
- 15% discount on repairs
- Priority scheduling
- Free diagnostic on covered equipment failures

**Gold / Premium Plan (~$299–$349/year)**
- 2 annual tune-ups
- 20% discount on repairs
- Same-day priority service
- Free diagnostic
- Annual thermostat calibration
- Free filter on each visit

### 8.3 MA Enrollment Triggers
Build automation to offer MA enrollment at every logical touchpoint:
- After every service call (tag: MA-Offer-Sent if not already active)
- After every emergency call (higher urgency = higher conversion)
- After first tune-up if not yet enrolled
- After equipment age hits 5 years (start protecting the investment)
- After moving into a new home (new homeowner sequence)

### 8.4 MA Dashboard View
GHL dashboard should surface:
- Total active maintenance agreements
- MA renewals due in next 30 days
- MA renewals due in next 60 days
- Lapsed MAs in last 90 days
- Revenue from MA renewals this month
- MA conversion rate (service calls → MA enrollment)

---

## Section 9: Seasonal Campaign Calendar

### 12-Month HVAC Campaign Schedule

| Month | Campaign Name | Target | Offer |
|---|---|---|---|
| January | "Beat the Freeze" | Non-MA heating customers | Emergency heat service discount, MA enrollment |
| February | "Pre-Season A/C Savings" | All customers | Early bird spring tune-up booking discount |
| March | "Spring Startup Special" | Non-MA customers | $X off AC tune-up or free with MA enrollment |
| April | **Spring A/C Tune-Up Launch** | MA-Active (scheduled) + all customers | MA: Schedule free tune-up. Others: $X tune-up or MA enrollment |
| May | "Summer Ready Checklist" | All customers | Filter reminder, indoor air quality upsell (IAQ, UV purifiers) |
| June | "Beat the Heat" | Non-MA, old equipment | Emergency-season urgency, replacement consultations |
| July | "Peak Season" | Hot leads, replacements | Replacement consultations, financing promos, emergency dispatch |
| August | "End of Summer Savings" | Replacement pipeline | End-of-season equipment incentives, financing closeout |
| September | **Fall Furnace Tune-Up Launch** | MA-Active (scheduled) + all customers | MA: Schedule free tune-up. Others: $X tune-up or MA enrollment |
| October | "Winter Ready" | Non-MA heating customers | Furnace inspection, heat pump check, duct sealing |
| November | "Pre-Holiday Comfort Check" | All customers | Filter reminder, thermostat upgrade, MA renewal push |
| December | "Year-End Replacement Tax Incentive" | Replacement pipeline | Federal/provincial HVAC efficiency tax credits, year-end install before deadline |

### Indoor Air Quality (IAQ) Upsell Campaign
**Best months:** March–May (spring allergen season), October–November (windows close, recirculated air)
**Products:** UV germicidal lights, electronic air purifiers, whole-home humidifiers, HEPA media filters, ERV/HRV ventilators

```
SMS: "With everything circulating in [Month], air quality matters. 
Did you know we install whole-home air purifiers that eliminate 99.9% of airborne 
contaminants? Ask your tech about it at your next tune-up, or reply for more info. 
— [Company Name]"
```

---

## Section 10: Review Generation Sequence (Full)

### 10.1 Review Strategy
**Goal:** 100+ Google reviews with 4.8+ average rating within 12 months

**Key principles:**
1. Only ask happy customers (do not auto-blast all jobs)
2. Send review request within 2 hours of job close while sentiment is highest
3. Make it 1-click — no login, no friction
4. Never ask for a 5-star review directly (Google ToS violation) — ask for "honest review"
5. Segment by job type — tune-ups and new installs get higher review conversion than repair calls

### 10.2 Review Funnel
```
Job Closed — Won
↓
Internal sentiment check (tech rating or flag)
↓ (positive)              ↓ (negative / callback)
Review Request Sequence    Recovery Workflow
↓
SMS → 2hr post-close
↓ (no action)
Email → 48hr post-close
↓ (no action)
Final SMS → 7 days
```

### 10.3 Review Response Templates

**5-Star Review Response:**
"Thank you so much [Name]! We're thrilled [Tech Name] took great care of you. 
We appreciate your trust and look forward to keeping your system running efficiently 
for years to come. — [Company Name]"

**4-Star Review Response:**
"Thanks for the review, [Name]! We'd love to know what we could have done to make 
it a 5-star experience — feel free to reach out anytime. We appreciate your business! 
— [Company Name]"

**Negative Review Response:**
"We're sorry to hear this, [Name]. This isn't the experience we strive to deliver. 
Please call us at [Phone] or email [Email] — we'd like to make this right immediately. 
— [Company Name]"

---

## Section 11: Custom Fields Required in 1app HVAC Snapshot

### 11.1 Equipment Fields (Primary System)
| Field Name | Type | Options |
|---|---|---|
| Equipment Type | Dropdown | Central A/C, Furnace, Heat Pump, Air Handler, Package Unit, Mini-Split, Boiler |
| Equipment Brand | Text | — |
| Equipment Model | Text | — |
| Equipment Serial | Text | — |
| Equipment Install Year | Number | — |
| Equipment Age (calculated) | Number | Auto-calculated |
| Equipment Tonnage | Dropdown | 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 ton |
| SEER Rating (old) | Number | — |
| Refrigerant Type | Dropdown | R-22, R-410A, R-32, R-454B, R-407C, Unknown |
| Last Service Date | Date | — |
| Next Tune-Up Due | Date | — |
| Filter Size | Text | e.g. 16x25x1 |
| Filter Change Frequency | Dropdown | Monthly, Every 3 Months, Every 6 Months |
| Equipment Condition | Dropdown | Excellent, Good, Fair, Poor, End-of-Life |

### 11.2 Maintenance Agreement Fields
| Field Name | Type | Options |
|---|---|---|
| MA Status | Dropdown | Active, Lapsed, Never Enrolled, Cancelled |
| MA Plan Tier | Dropdown | Bronze, Silver, Gold |
| MA Start Date | Date | — |
| MA Expiry Date | Date | — |
| MA Price | Currency | — |
| MA Renewal Date | Date | — |
| Spring Tune-Up Scheduled | Checkbox | — |
| Spring Tune-Up Completed | Checkbox | — |
| Fall Tune-Up Scheduled | Checkbox | — |
| Fall Tune-Up Completed | Checkbox | — |

### 11.3 Lead & Job Fields
| Field Name | Type | Options |
|---|---|---|
| Lead Source | Dropdown | (Full list from Section 5.1) |
| Job Type | Dropdown | Emergency Repair, Routine Repair, Tune-Up, Replacement, New Install, Commercial PM |
| Assigned Technician | Dropdown | (Tech names) |
| Job Total | Currency | — |
| Invoice Sent | Checkbox | — |
| Invoice Paid | Checkbox | — |
| Review Requested | Checkbox | — |
| Review Received | Checkbox | — |
| Review Stars | Dropdown | 1, 2, 3, 4, 5 |
| Customer Since | Date | — |
| Property Type | Dropdown | Residential, Light Commercial, Commercial, Multi-Family, New Construction |
| Home Warranty Company | Dropdown | AHS, First American, Choice, Old Republic, None |

---

## Section 12: What Makes This Snapshot Stand Out

### 12.1 The 1app HVAC Snapshot Differentiators

**1. Revenue-Mapped Pipeline Architecture**
Not just "leads" — three distinct revenue tracks (service, maintenance, replacement) with different automation logic, different follow-up cadences, and different upsell triggers. This mirrors how an actual HVAC company makes money.

**2. Equipment Lifecycle Intelligence**
Install date + age calculation + refrigerant type = proactive replacement campaigns that no other snapshot runs automatically. This is money sitting on the table for every HVAC company with a customer list.

**3. Maintenance Agreement Engine**
The only snapshot with a full MA selling, tracking, renewal, and re-enrollment system. Includes MA tiered pricing structure, renewal reminders, lapsed re-enrollment campaign, and MA upsell triggers baked into post-service workflows.

**4. True Seasonal Campaign Calendar**
Pre-built spring and fall campaign triggers with full email + SMS sequences — not templates, but fully activated automations that fire on schedule every year.

**5. Commercial / Property Manager Track**
Separate pipeline and workflow for the B2B side of the business. Property managers represent a high-value, high-LTV segment that generic snapshots completely ignore.

**6. Emergency Dispatch Triage**
After-hours AI triage workflow with technician notification that actually routes emergency leads to the right outcome — not just a "we'll call you back" message.

**7. Review Segmentation (No Public Blasting of Unhappy Customers)**
Review requests only go to confirmed positive experiences. Negative experiences route to a recovery workflow. This protects the company's Google rating while maximizing positive reviews.

**8. Financing Integration Point**
Replacement pipeline includes financing pre-qualification step — because a $15K equipment replacement often needs a financing conversation, and companies that don't offer it lose jobs to companies that do.

**9. 12-Month Campaign Calendar**
Every month has a campaign. No dead months. Spring, summer, fall, winter — each season has an activation sequence that keeps the HVAC company top-of-mind year-round.

**10. Full Custom Field Library**
Equipment tonnage, SEER rating, refrigerant type, MA tier, filter size — all the fields a professional HVAC operation needs to run business intelligence, segment campaigns, and trigger the right automation at the right time.

---

## Section 13: Technical Build Specifications (GHL)

### 13.1 Snapshot Components Checklist

**Funnels / Landing Pages:**
- [ ] Emergency Service Request page (phone + SMS, minimal friction)
- [ ] Tune-Up Booking page (MA vs. non-MA version)
- [ ] Free Replacement Consultation page (comfort consultation)
- [ ] Maintenance Agreement enrollment page (3 tiers)
- [ ] Commercial / Property Manager contact page

**Calendars:**
- [ ] Service Call calendar (same-day / next-day availability)
- [ ] Tune-Up calendar (scheduled, capacity capped by tech)
- [ ] Replacement Consultation calendar (comfort advisor)
- [ ] Commercial PM calendar (separate flow)
- [ ] After-Hours Emergency calendar (bypass to dispatch)

**Pipelines:**
- [ ] Service Call Pipeline (12 stages)
- [ ] Maintenance Agreement Pipeline (14 stages)
- [ ] Equipment Replacement Pipeline (15 stages)
- [ ] New Construction Pipeline (10 stages)
- [ ] Commercial / Property Manager Pipeline (10 stages)

**Workflows (Automations):**
- [ ] Missed Call Text Back (business hours)
- [ ] After-Hours Emergency Triage
- [ ] Appointment Confirmation + Reminder (3-step)
- [ ] Post-Service Follow-Up (payment, review, MA upsell)
- [ ] Maintenance Agreement Renewal (60/30/14/7 day)
- [ ] Lapsed MA Re-enrollment Campaign
- [ ] Equipment Age Trigger — 10 year
- [ ] Equipment Age Trigger — 12 year
- [ ] Equipment Age Trigger — 15 year
- [ ] R-22 Refrigerant Phase-Out Campaign
- [ ] Spring A/C Campaign (date-triggered, April)
- [ ] Fall Furnace Campaign (date-triggered, September)
- [ ] Filter Reminder (1-month / 3-month / 6-month variants)
- [ ] Review Generation (post-service, segmented)
- [ ] Recovery Workflow (negative experience)
- [ ] Angi/HomeAdvisor Speed-to-Lead
- [ ] Home Warranty Post-Service Conversion
- [ ] Commercial / Property Manager Outreach
- [ ] New Homeowner Sequence
- [ ] Equipment Replacement Nurture
- [ ] Post-Installation Follow-Up + MA enrollment

**Tags (Smart Lists):**
- [ ] MA-Active
- [ ] MA-Lapsed
- [ ] MA-Never-Enrolled
- [ ] MA-Bronze / MA-Silver / MA-Gold
- [ ] R22-Unit
- [ ] Equipment-Age-10 / Equipment-Age-12 / Equipment-Age-15
- [ ] Emergency-Lead
- [ ] LSA-Lead
- [ ] Angi-Lead
- [ ] Home-Warranty-Lead
- [ ] Property-Manager
- [ ] Commercial-Account
- [ ] Review-Requested / Review-Received
- [ ] Filter-1Month / Filter-3Month / Filter-6Month
- [ ] New-Homeowner
- [ ] Replacement-Lead-Active

**Custom Fields:**
- [ ] (Full list from Section 11)

**Email Templates:**
- [ ] Emergency Response
- [ ] Appointment Confirmation
- [ ] Day-Before Reminder
- [ ] Post-Service Follow-Up
- [ ] MA Welcome
- [ ] MA Renewal (60/30/14/7 day versions)
- [ ] MA Lapsed Re-enrollment
- [ ] Equipment Age 10 / 12 / 15 awareness
- [ ] R-22 Phase-Out Alert
- [ ] Spring A/C Campaign (2 emails)
- [ ] Fall Furnace Campaign (2 emails)
- [ ] Replacement Consultation Confirmation
- [ ] Pre-Consultation Preparation
- [ ] Post-Consultation Proposal Follow-Up (3 emails)
- [ ] Review Request
- [ ] Recovery / Callback Request
- [ ] Commercial / PM Outreach (3 emails)
- [ ] New Homeowner Welcome
- [ ] Filter Reminder (3 variants)

**SMS Templates:**
- [ ] (All SMS templates from Section 6 — minimum 35 unique SMS templates)

**Reporting / Dashboard:**
- [ ] Active MA count
- [ ] MA renewals due next 30 / 60 days
- [ ] Lapsed MA last 90 days
- [ ] Monthly revenue from MAs
- [ ] Jobs booked by lead source
- [ ] Review count + average rating
- [ ] Pipeline stage distribution for each pipeline
- [ ] Revenue by job type (service vs. MA vs. replacement)

---

## Section 14: Onboarding Checklist for 1app HVAC Clients

When a new HVAC company activates the 1app snapshot, the onboarding flow should include:

**Week 1 — Setup:**
- [ ] Import existing customer list (CSV) with equipment data
- [ ] Configure technician calendar availability and capacity limits
- [ ] Set up phone number (GHL number for Missed Call Text Back)
- [ ] Connect Google Business Profile for review link
- [ ] Configure payment link (Stripe / Square)
- [ ] Set company branding (logo, colors, name, phone, address)
- [ ] Review and approve all SMS templates (legal compliance review)
- [ ] Activate Missed Call Text Back
- [ ] Set after-hours hours and AI triage workflow

**Week 2 — Data Population:**
- [ ] Tag all existing customers with equipment type and age (if available)
- [ ] Identify all customers without maintenance agreement → enter MA-Never-Enrolled pipeline
- [ ] Identify R-22 units → apply R22-Unit tag → review campaign sequence
- [ ] Set up 3 MA tiers with pricing and descriptions
- [ ] Configure seasonal campaign trigger dates (spring/fall)
- [ ] Import lead source attribution for existing customers where possible

**Week 3 — Go Live:**
- [ ] Launch first campaign (whatever season is most relevant)
- [ ] Test full booking flow (emergency, tune-up, replacement consultation)
- [ ] Train owner and office staff on pipeline stage management
- [ ] Verify review request workflow with test contact
- [ ] Set up reporting dashboard views
- [ ] First performance check-in call scheduled (30 days out)

---

## Section 15: Pricing Recommendation for 1app

### Snapshot Packaging for HVAC Vertical:

**Starter — $197/month**
- Core pipelines (Service Call + MA)
- Missed Call Text Back
- Appointment Confirmation + Reminder
- Post-Service Follow-Up + Review Request
- Spring + Fall Seasonal Campaigns
- GHL sub-account (all features)
- Onboarding support

**Growth — $297/month**
- Everything in Starter
- Equipment Replacement Pipeline
- Equipment Age Trigger Campaigns (10/12/15 year)
- R-22 Phase-Out Campaign
- Maintenance Agreement Renewal + Lapsed Re-enrollment
- Commercial / Property Manager Pipeline
- Monthly performance reporting

**Scale — $397/month**
- Everything in Growth
- Custom AI voice agent (after-hours emergency triage)
- Full 12-month campaign calendar activation
- Lead source attribution reporting
- Technician performance dashboard
- Reputation management (review monitoring, response templates)
- Dedicated onboarding + monthly strategy call

---

## Appendix A: HVAC Industry Glossary (For Client Communication)

| Term | Definition |
|---|---|
| Service Call | A technician visit to diagnose and repair an equipment problem |
| Tune-Up / PM | Preventive maintenance visit — cleaning, inspection, testing |
| Maintenance Agreement | Annual contract for 2 tune-ups + priority service + repair discounts |
| Comfort Club | Marketing name for maintenance agreement |
| FNA (Field Service) | Field Not Available — tech can't resolve on first visit |
| Tonnage | Cooling capacity of an HVAC system (1 ton = 12,000 BTU/hr) |
| SEER Rating | Seasonal Energy Efficiency Ratio — higher = more efficient |
| SEER2 | Updated SEER standard (effective Jan 1, 2023) |
| Refrigerant | Fluid used in cooling cycle (R-22, R-410A, R-32, R-454B) |
| R-22 (Freon) | Legacy refrigerant, phased out since 2020, very expensive to source |
| R-410A (Puron) | Current standard residential refrigerant (being phased down) |
| R-32 / R-454B | Next-gen low-GWP refrigerants replacing R-410A |
| Condenser | Outdoor unit of a split A/C or heat pump system |
| Air Handler | Indoor unit (fan coil) of a split system — circulates conditioned air |
| Evaporator Coil | Heat exchanger inside air handler — where cooling actually happens |
| Ductwork | The duct system that distributes conditioned air through the building |
| Heat Exchanger | Component in furnace that separates combustion gases from supply air |
| Load Calculation (Manual J) | Engineering calculation to determine correct tonnage for a home |
| Commissioning | Final system startup, calibration, and performance verification |
| LSA | Google Local Services Ads — pay-per-lead advertising |
| RTU | Rooftop Unit — self-contained commercial HVAC unit |
| Mini-Split / Ductless | Split system without ductwork — individual room/zone control |
| Heat Pump | Dual-function system — cools in summer, heats in winter |
| No-Cool | Emergency call — A/C system not producing cold air |
| No-Heat | Emergency call — heating system not producing heat |
| Refrigerant Leak | Loss of refrigerant charge — major service event |
| Capacitor | Electrical component that starts and runs compressor/motor — common failure |
| Contactor | High-voltage electrical switch that starts the compressor — common failure |
| Thermostat | Control device — controls system setpoint and scheduling |
| HVAC Comfort Advisor | Sales-focused technician or advisor who runs replacement consultations |
| ERV / HRV | Energy/Heat Recovery Ventilator — whole-home fresh air system |
| IAQ | Indoor Air Quality — encompasses filtration, UV, humidification |

---

*Document prepared by Maximus AI for 1app GHL Agency.*
*Version 1.0 | July 2026 | Internal use — do not distribute to clients.*
*For questions or revisions, contact Tony DeCarlo via workspace memory system.*
