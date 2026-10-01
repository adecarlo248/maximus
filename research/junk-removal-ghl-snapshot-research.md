# GHL Snapshot Research: Junk Removal & Moving Companies
## Agency Build Document — 1app Technologies Inc.
**Version:** 1.0 | **Date:** July 2026 | **Prepared for:** 1app Agency Team

---

## EXECUTIVE SUMMARY

Junk removal and moving services are two of the highest-volume, lowest-margin residential service verticals in North America — and they are dramatically underserved by the current GHL snapshot ecosystem. The few snapshots that exist are either generic "home services" templates relabeled for junk removal or bare-bones setups with a pipeline and three workflows. None of them address the industry's core operational reality:

**This is a speed-to-quote, volume-over-ticket business.**

The company that responds first with a clear, confident price — wins. The company that automates post-job review requests — compounds. The company that builds a referral pipeline with real estate agents and property managers — scales.

A purpose-built 1app snapshot for junk removal and moving can be the most comprehensive, highest-converting snapshot in this niche — because the bar is low and the need is real.

---

## SECTION 1: INDUSTRY OVERVIEW

### Who Are These Businesses?

**Junk Removal Operators:**
- Solo operators (one truck, one driver) to small fleets (3–10 trucks)
- Revenue: $150K–$2M+ per year depending on scale
- Average job ticket: $250–$600 (residential), $800–$3,000+ (commercial/estate cleanouts)
- Job types: Full truckload, half load, quarter load, single-item haul away, estate cleanouts, hoarder cleanouts, demolition debris, appliance removal, e-waste, furniture removal, yard waste, mattress disposal, donation drop-off, commercial cleanouts

**Moving Companies:**
- Local movers (in-town residential), small commercial office moves, labor-only movers (customer rents truck), packing + moving bundles
- Average job ticket: $400–$1,800 (local residential), $2,000–$8,000+ (long distance/commercial)
- High cancellation and ghost rates — customers shop multiple quotes

**Key Differentiator Between the Two:**
Junk removal = volume, speed, one-day close. Moving = scheduled in advance, higher stakes, requires trust and reviews.

---

## SECTION 2: BUSINESS PAIN POINTS

### 2.1 Instant Quote Expectations
The junk removal industry has been transformed by 1-800-GOT-JUNK and LoadUp. Customers now expect:
- Online pricing (even if approximate) before they call
- Same-day or next-day availability
- Text/SMS-based booking confirmations
- No-show penalties are almost unenforceable — so they ghost freely

**Pain:** Most small operators have no online quote system. Customers call, wait for a callback, get a price, then call the competitor and book with whoever calls back first. Operators lose jobs in the 15-minute window between call and callback.

### 2.2 Low Average Ticket, High Volume Dependency
Unlike roofing or HVAC, junk removal doesn't have $10K jobs. Margins depend on running 3–6 jobs per truck per day. This means:
- Follow-up sequences need to fire fast
- No room for slow response times
- Seasonal spikes (spring cleanouts, post-holiday, estate settlements) require surge capacity outreach

### 2.3 Zero Follow-Up Infrastructure
The #1 gap in junk removal: **leads die in a text thread or voicemail**. No CRM. No pipeline. No automated follow-up. Operators are running on sticky notes and memory.

Data point: Industry surveys consistently show the average junk removal company follows up on fewer than 30% of quote requests. The ones who follow up within 5 minutes close at 70%+ conversion.

### 2.4 Scheduling Coordination Chaos
Multiple drivers, multiple jobs, changing availability. Without automated confirmation + reminder sequences:
- No-show rates run 15–25% on booked jobs
- Crews show up to locked houses or wrong addresses
- Double-booking happens regularly on busy days

### 2.5 Review Management is Revenue Management
Junk removal is a commodity service. Google reviews and Google Business Profile (formerly GMB) ratings are the primary decision factor for residential customers.

- Top-rated operators (4.8+ stars, 200+ reviews) command 15–30% price premiums
- Most operators never ask for a review — they wait and hope
- Review velocity matters for Local Pack ranking (Google Maps 3-pack)

**Pain:** Small operators have 20–50 reviews after 3–5 years. A systematic post-job review ask via SMS would get them to 200 reviews in 12 months.

### 2.6 Commercial and Recurring Revenue is Untapped
Property managers, real estate agents, and renovation contractors generate recurring junk removal needs:
- Property managers: tenant turnover cleanouts, bulk trash removal, eviction cleanouts
- Real estate agents: estate cleanouts, pre-listing decluttering, furniture removal
- Renovation contractors: demolition debris haul away, construction waste removal

Most operators have never sent a single outreach email to a property manager or real estate office. This is pure upside.

### 2.7 Moving-Specific Pain Points
- Quote competition is brutal — customers get 3–5 quotes before booking
- Last-minute cancellations destroy truck utilization
- Add-on upsells (packing materials, extra labor, specialty items) are never systematically offered
- Moving date reminders are manually sent or not sent at all
- Customer complaints about damages spike when communication pre-move is poor

---

## SECTION 3: GHL SNAPSHOT LANDSCAPE ANALYSIS

### 3.1 What Currently Exists

**Generic Home Services Snapshots:**
Most SaaS agencies sell a "Home Services" or "Trades" snapshot that covers HVAC, plumbing, landscaping, etc. These include:
- Basic 5-stage pipeline (New Lead → Quote Sent → Booked → Complete → Review Requested)
- 2–3 SMS automation workflows
- A contact form
- Google review request at job end

**"Junk Removal" Labeled Snapshots (Marketplace):**
A small number exist on platforms like Gohighlevel.com community marketplace, SnapShotSales, and agency template stores. Common features:
- Renamed pipeline stages (still generic)
- Basic SMS follow-up (1 message, day 1)
- A simple booking form
- Google review link appended to a thank-you message

### 3.2 What's Missing (The Gap = Our Opportunity)

| Feature | Generic Snapshot | Purpose-Built 1app Snapshot |
|---------|-----------------|----------------------------|
| Instant online quote calculator | ❌ | ✅ |
| Load-size-based pricing tiers | ❌ | ✅ |
| Commercial cleanout pipeline (separate) | ❌ | ✅ |
| Estate cleanout pipeline (sensitive tone) | ❌ | ✅ |
| Property manager outreach sequence | ❌ | ✅ |
| Real estate agent referral workflow | ❌ | ✅ |
| Same-day urgency SMS series | ❌ | ✅ |
| Post-job photo trigger (before/after) | ❌ | ✅ |
| Donation drop-off coordination | ❌ | ✅ |
| Hoarder cleanout sensitivity workflow | ❌ | ✅ |
| Moving-specific pipeline | ❌ | ✅ |
| Pre-move prep checklist automation | ❌ | ✅ |
| Referral partner management | ❌ | ✅ |
| Seasonal surge campaigns | ❌ | ✅ |
| Recurring commercial account tracking | ❌ | ✅ |

**Verdict:** No snapshot on the market does more than 20–30% of what this vertical actually needs. The 1app snapshot can own this category outright.

---

## SECTION 4: PIPELINE ARCHITECTURE

### 4.1 Residential Pipeline (Primary)

**Pipeline Name:** Junk Removal — Residential

| Stage | Description | Trigger |
|-------|-------------|---------|
| **New Inquiry** | Web form, phone call log, Facebook/Kijiji lead | Lead captured |
| **Quote Requested** | Customer wants pricing — load size, item type noted | Manual or form tag |
| **Quote Sent** | Price given via phone, text, or online estimate | Stage move |
| **Quote Follow-Up** | No response after 24–48 hrs | Automated sequence fires |
| **Booked — Pending** | Date/time confirmed, crew assigned | Booking confirmed |
| **Job Day** | Day-of reminders, crew dispatch confirmation | Date trigger |
| **Job Complete** | Work done, haul away confirmed | Manual or GPS trigger |
| **Review Requested** | Post-job SMS with Google review link | Auto-fires 2 hrs post-job |
| **Review Received** | Positive review confirmed | Tag added manually |
| **Referral Asked** | Follow-up 7 days post-job asking for referral | Automated |
| **Won** | Paid, satisfied, review left | Closed won |
| **Lost — Price** | Went with competitor (price) | Closed lost — tag for re-engage |
| **Lost — No Response** | Ghosted after quote | Closed lost — 30-day reactivation |

### 4.2 Commercial Cleanout Pipeline (Secondary)

**Pipeline Name:** Commercial Cleanouts — B2B

| Stage | Description |
|-------|-------------|
| **Prospect — Cold** | Property managers, RE agents added from outreach |
| **Contacted** | Initial outreach made |
| **Appointment Set** | Site walk-through scheduled |
| **Site Assessment Done** | Scope of work established |
| **Proposal Sent** | Formal quote/scope doc sent |
| **Negotiating** | Back and forth on price/scope |
| **Contract Signed** | Committed — scheduling underway |
| **In Progress** | Multi-day job actively running |
| **Complete — Invoice Sent** | Job done, invoice outstanding |
| **Paid** | Full payment received |
| **Recurring Account** | Ongoing relationship established |

### 4.3 Estate Cleanout Pipeline (Sensitive Niche)

**Pipeline Name:** Estate Cleanouts — Estates & Hoarding

| Stage | Description |
|-------|-------------|
| **Referred / Inquiry** | Often comes via RE agent, lawyer, or family member |
| **Consultation Scheduled** | In-person or phone assessment booked |
| **Needs Assessment** | Understanding volume, timeline, emotional factors |
| **Proposal Sent** | Detailed written quote with timeline |
| **Approved** | Family/estate trustee sign-off |
| **Scheduled** | Date confirmed — multi-day likely |
| **In Progress** | Active cleanout underway |
| **Donation / Charity Coordination** | Items flagged for donation, arrange pickup |
| **Hazmat / Special Items** | E-waste, paint, chemicals — separate disposal |
| **Complete** | Full cleanout done, space cleared |
| **Review + Referral** | Sensitive ask — timing matters |

### 4.4 Moving Company Pipeline

**Pipeline Name:** Moving Services

| Stage | Description |
|-------|-------------|
| **Quote Request** | Online form, phone, or referral |
| **Inventory Survey** | Virtual or in-home assessment |
| **Quote Sent** | Written moving estimate provided |
| **Quote Follow-Up** | 48-hr follow-up if no response |
| **Booked — Deposit Paid** | Confirmed with deposit |
| **Pre-Move Check-In** | 1-week out reminder + prep checklist |
| **Move Day** | Day-of confirmation, crew dispatch |
| **Move Complete** | Delivery confirmed |
| **Invoice / Balance Due** | Final payment collected |
| **Review Request** | Post-move SMS/email |
| **Referral Ask** | 1-week post-move |
| **Closed Won** | Paid + reviewed |

---

## SECTION 5: WORKFLOW AUTOMATION LIBRARY

### 5.1 Instant Quote Request Flow (Residential)

**Trigger:** Web form submission tagged "Quote Request"

```
Step 1 — IMMEDIATE (0 min)
SMS to lead: 
"Hi [First Name]! Got your request for a haul away — we can usually get you a same-day or next-day pickup. What's the best time to reach you for a quick 2-minute call to confirm pricing? — [Company Name]"

Step 2 — (15 min, if no response)
SMS:
"Hey [First Name] — just following up on your junk removal request. We have trucks available [today/tomorrow]. Want a quick estimate? Reply YES and I'll call you right away."

Step 3 — (1 hour, if no response)
SMS:
"[First Name], last one from us today — our schedule is filling up fast. If you'd like to lock in a time, reply BOOK and someone will call you back in 5 minutes. Otherwise, reach us anytime at [Phone]."

Step 4 — (24 hrs, if no booking)
SMS:
"Hey [First Name] — still have a junk removal coming up? We're booking pickups for this week. Reply and we'll get you a price right away."

Step 5 — (3 days)
Email:
Subject: Still need that haul away done?
Body: Friendly 3-line follow-up with a direct booking link

Step 6 — (7 days)
SMS reactivation:
"[First Name] — checking in one last time. Still have stuff to haul away? We can usually do same-day. Reply QUOTE to get a price."
```

### 5.2 Booking Confirmation Sequence

**Trigger:** Pipeline stage moved to "Booked — Pending"

```
Immediate — Confirmation SMS:
"✅ You're booked! [Company Name] will arrive [Date] between [Time Window]. Your crew will text you 30 minutes before arrival. Questions? Reply or call [Phone]. See you then!"

Immediate — Confirmation Email:
Includes: Job address, estimated time window, what to expect, payment methods accepted, what happens to items (recycling, donation, disposal), contact number for day-of issues

Day Before (5 PM) — Reminder SMS:
"Reminder: [Company Name] arrives tomorrow between [Time Window]. We'll text you 30 min ahead. If anything changes, reply here or call [Phone]. See you tomorrow! 🚛"

Day Of (7 AM) — Morning Reminder SMS:
"Good morning [First Name]! Your haul away is today. We'll text you when we're on our way. Got a big truckload ready? We'll take it all. 💪"

Day Of (En Route) — Dispatch SMS [Manual Trigger]:
"[First Name] — your crew is on the way! ETA approx [X] minutes. They'll arrive in [Color] truck. See you soon! — [Company Name]"
```

### 5.3 Post-Job Review Request Sequence

**Trigger:** Pipeline stage moved to "Job Complete"

```
2 Hours Post-Job — SMS:
"[First Name] — thanks for choosing [Company Name] today! Hope the space is looking great. If you have 60 seconds, a Google review helps us a ton: [Review Link] We'd really appreciate it! 🙏"

24 Hours — SMS (if no review):
"Hey [First Name]! We hope you're loving the extra space. Would you mind leaving us a quick Google review? It really helps our small business: [Review Link] — Thanks!"

3 Days — Email (if no review):
Subject: Quick favor from [Company Name]
Body: Friendly note about what the review means to the team, direct link to Google review, photo of crew (optional)
```

### 5.4 Same-Day Urgency Campaign

**Trigger:** Tag "Same-Day Available" applied (manual or automation-triggered daily at 8 AM if slots open)

```
SMS Blast to "Interested — Not Booked" contacts:
"🚛 [Company Name] here — we have a truck available TODAY in [Area]. First-come, first-served. Need junk, furniture, or appliances hauled away? Reply BOOK and we'll get you scheduled in the next 30 minutes."
```

### 5.5 Commercial Prospect Outreach Sequence

**Trigger:** Contact tagged "Property Manager" or "Real Estate Agent" added to pipeline

```
Day 1 — Email:
Subject: Junk removal for your properties in [City]
Body: 
Hi [First Name],

I run [Company Name] — we specialize in full-property cleanouts, tenant turnover trash removal, and estate cleanouts for property managers in [Area].

A few things we do for property managers specifically:
• Same-week scheduling on most cleanouts
• Full truckloads or light cleanouts — we handle both
• Before/after photos sent directly to you
• Clean, professional crews (no subcontractors)
• Donation and recycling coordination when appropriate

Are you currently using a junk removal company for your properties? Happy to introduce ourselves and earn your business.

[Signature + Phone]

Day 4 — SMS:
"Hi [First Name] — sent you an email earlier this week about property cleanouts and haul away. [Company Name] works with a number of property managers in [City]. Quick 10-minute chat to see if we'd be a fit? — [Name, Company]"

Day 10 — Email:
Subject: One thing most property managers hate about junk removal companies
Body: Pain-point focused email about unreliable crews, no-shows, debris left behind. Positions [Company Name] as the reliable alternative.

Day 21 — Final Touch SMS:
"[First Name] — last follow-up from [Company Name]. We handle property cleanouts, tenant turnovers, and haul away in [Area]. If you ever need a reliable crew on short notice, save our number: [Phone]. We pick up."
```

### 5.6 Estate Cleanout Intake Workflow (Sensitive Tone)

**Trigger:** Tag "Estate Cleanout" or "Hoarder Cleanout" applied

```
Immediate — SMS (soft, empathetic):
"Hi [First Name] — thank you for reaching out to [Company Name]. We understand estate cleanouts can be a difficult time. We're here to help make it as easy as possible. When would be a good time for a brief call so we can learn more about your situation?"

No Response — 24 hrs — SMS:
"[First Name] — just checking in. Whenever you're ready, we're here. Estate cleanouts are a specialty of ours — we handle everything with care and discretion. No rush. [Phone]"

Post-Inquiry — Email:
Subject: What to expect from your estate cleanout
Content covers: Process (assessment → scheduled dates → donation coordination → disposal → cleanup), pricing structure, how we handle sentimental items, timeline, references available
```

### 5.7 Real Estate Agent Referral Workflow

**Trigger:** Contact tagged "RE Agent" enters pipeline

```
Day 1 — Email:
Subject: Junk removal referrals for your listings
Body:
Hi [First Name],

We work with several real estate agents in [City] who refer us to clients who need furniture, appliances, or full cleanouts done before listing a property.

What we offer your clients:
• Pre-listing cleanouts — clear clutter to maximize showing appeal
• Estate cleanouts — full home, basement, garage, attic
• Same-week availability in most cases
• Donation coordination for items clients want donated
• Professional crews — no mess left behind

We'd love to be your go-to referral for junk removal. We treat your clients like they're our best clients — because they are.

Interested in a quick call? [Booking Link] — takes 10 minutes.

Day 7 — SMS:
"Hi [First Name] — sent you an email last week about junk removal referrals for your listings. [Company Name] helps agents get homes ready to show. Worth a quick call? — [Name]"

Day 30 — Email (value-add):
Subject: Free guide: Pre-listing checklist for sellers
Content: Useful resource for their clients — establishes [Company Name] as a trusted resource, soft CTA at bottom
```

### 5.8 Referral Request (Post-Job, 7-Day Follow-Up)

**Trigger:** 7 days after "Job Complete" stage

```
SMS:
"Hi [First Name]! Hope the space is still looking great after your cleanout. 😊 If you know anyone who needs junk hauled away — a neighbor, family member, coworker — we'd love the referral. We offer [10%/$25] off for anyone you send our way. Just have them mention your name. Thanks!"
```

### 5.9 30-Day Lead Reactivation Campaign

**Trigger:** Contacts in "Lost — No Response" for 25+ days

```
SMS:
"Hey [First Name] — [Company Name] here. You reached out about a junk removal a while back. Still have stuff you need hauled? We're doing runs in [Area] this week. Reply and we'll get you a quick price. 🚛"

Email (same day as SMS):
Subject: Still need that haul away?
Body: 3-line friendly note, direct booking link

Day 2 — SMS:
"[First Name] — still here if you need us! Same-day pickups available. Just reply QUOTE."
```

### 5.10 Moving Company Pre-Move Prep Workflow

**Trigger:** Pipeline stage "Booked — Deposit Paid"

```
Booking Confirmation — Immediate:
"✅ Your move is booked with [Company Name]! Move date: [Date]. Crew arrival: [Time]. Confirmation # [XXXX]. Reply anytime with questions."

1 Week Out — SMS:
"One week until your big move, [First Name]! Here are a few tips to make move day go smoothly: 📦 Label boxes by room. 🗃️ Pack valuables separately. 🚗 Clear parking for our truck. Any questions? Reply or call [Phone]."

1 Week Out — Email:
Subject: Your move is one week away — here's your checklist
Content: Full pre-move checklist PDF or inline list — professional, helpful, reduces day-of confusion

3 Days Out — SMS:
"3 days until your move! Quick reminder: [Time Window] arrival on [Date]. Please make sure we have parking access. Got fragile items? Let us know so we can pack them with extra care."

Day Before — SMS:
"Tomorrow's the big day! [Company Name] crew arrives [Time Window]. We'll text you when we're 30 min out. Sleep well tonight — we've got this. 🚛"

Post-Move (Day Of) — Payment Confirmation + Review:
"Thanks for choosing [Company Name], [First Name]! Hope the new place feels like home already. Mind leaving us a review? It means a lot to the crew: [Review Link]"
```

---

## SECTION 6: LEAD SOURCE STRATEGY

### 6.1 Google Local Services Ads (LSA)
**The #1 paid channel for junk removal.**
- Pay-per-lead, Google-verified businesses appear above regular ads
- Average CPL: $25–$80 per junk removal lead (Canada/US)
- Requires Google Guaranteed badge — background checks, license/insurance verification
- GHL integration: LSA leads auto-populate via webhook or Zapier → snapshot pipeline

**Snapshot Setup:**
- Dedicated LSA landing page (simple, fast, review-focused)
- LSA lead → auto-added to "New Inquiry" pipeline stage
- Instant SMS follow-up fires within 60 seconds of lead capture

### 6.2 Kijiji (Canada) / Craigslist (US)
**Still a major source for price-conscious residential junk removal leads.**
- Free and low-cost listings drive significant volume in secondary markets
- Buyers here are comparison shopping — speed of response is everything
- Kijiji leads often don't have email — SMS-first workflow is critical

**Snapshot Setup:**
- Phone number as primary capture point (GHL tracking number routes to pipeline)
- Missed call triggers immediate SMS: "We missed you! Here's a quick quote — [link or reply]"

### 6.3 Facebook Marketplace
- Furniture removal, appliance haul away — customers post "need this removed"
- Contractors also post "debris removal needed" jobs
- Operators can monitor and respond — not easily automated, but GHL can track leads entered manually

### 6.4 Facebook/Instagram Ads (Retargeting)
- Before/after cleanout photos perform extremely well
- Video of a full truckload haul away gets shares and saves
- Target homeowners 35–65, renters moving out, property owners in specific zip codes

### 6.5 Referral Partners (B2B Pipeline)
Critical relationship categories to build into CRM:

**Property Managers:**
- Multi-family residential properties (apartments, condos)
- Commercial property management companies
- HOA management companies
- Target: 10–20 property managers in local market = consistent monthly volume

**Real Estate Agents:**
- Estate cleanouts are often agent-referred
- Pre-listing cleanouts are a common ask
- Post-sale cleanout (when previous owner leaves behind furniture/junk)
- Target: Top-producing agents in local MLS, senior real estate specialists (estate focus)

**Renovation Contractors:**
- Demo debris — drywall, flooring, framing materials
- Construction cleanup on residential renovations
- Target: Licensed contractors in local area — build reciprocal referral arrangement

**Moving Companies:**
- Customers who need junk removed before, during, or after a move
- Moving companies regularly encounter items customers won't take — refer them to junk removal
- Cross-referral opportunity: moving company refers junk removal; junk removal refers moving

### 6.6 Google Business Profile (Organic / Maps)
- Reviews are the fuel
- Regular photo uploads of before/after cleanouts rank in GBP
- "Near me" searches dominate junk removal — local pack placement is revenue

---

## SECTION 7: SMS & EMAIL TEMPLATE LIBRARY

### 7.1 Instant Quote — Initial Response
```
"Hi [First Name]! Thanks for reaching out to [Company Name]. To give you an accurate price, can you tell us: 
1. What items need to go? 
2. Roughly how much — one or two items, half a truck, or a full load? 

We can usually get out same day or next day. Prices start at [$XXX]. — [Name]"
```

### 7.2 Same-Day Urgency
```
"🚛 Same-day junk removal available in [Area] TODAY. Furniture, appliances, full cleanouts — we haul it all. Limited slots left. Reply BOOK now or call [Phone] to lock in your time."
```

### 7.3 Quote Follow-Up (Day 1)
```
"Hey [First Name] — still interested in getting that junk hauled away? We're booking [tomorrow/this week] and spots fill fast. Reply and I'll get you a price in 2 minutes."
```

### 7.4 Quote Follow-Up (Day 3)
```
"[First Name] — [Company Name] here. Checking back on that haul away. If the timing isn't right, no worries — just reply LATER and we'll check back in a couple weeks. Otherwise, we're ready when you are!"
```

### 7.5 Post-Job Thank You + Review Ask
```
"Thanks so much for choosing [Company Name] today, [First Name]! We hope the space looks exactly how you wanted. 😊

One quick favor — a Google review helps our small crew more than you know:
👉 [Google Review Link]

Thanks again — we hope to help you again sometime! — [Crew Name/Company]"
```

### 7.6 Referral Request
```
"Hey [First Name]! It's been a week since we hauled away your [items/cleanout] — hope you're loving the extra space! 

If anyone you know needs junk hauled away — friends, neighbors, family — we'd love the referral. Have them mention your name and we'll take care of them. 🙏 — [Company Name]"
```

### 7.7 Hoarder/Hoarding Cleanout — Sensitive Inquiry Response
```
"Hi [First Name] — thank you for reaching out. We've helped many families and individuals through cleanouts that can feel overwhelming. We work at your pace, with full discretion and respect for your space. 

When's a good time for a brief phone call? No pressure — just a conversation to understand what you need. — [Name], [Company Name]"
```

### 7.8 Estate Cleanout — After Initial Call
```
"Hi [First Name] — thank you for speaking with us today. We understand this is a difficult time, and we're here to make the cleanout process as smooth and stress-free as possible.

Attached is a brief overview of how we handle estate cleanouts — including what happens to donations, how we coordinate with family members, and our timeline process.

Please don't hesitate to reach out with any questions. We'll follow up on [Date] as discussed. — [Name], [Company Name]"
```

### 7.9 Commercial Property Manager — First Outreach Email
**Subject:** Reliable junk removal for your properties in [City]

```
Hi [First Name],

My name is [Name] — I run [Company Name], and we specialize in tenant turnover cleanouts, bulk trash removal, and property cleanouts for property managers in [City/Region].

Here's what sets us apart for property managers:
• Fast scheduling — often same week or next week
• Before/after photos sent to you after every job
• We handle everything: furniture, appliances, demolition debris, e-waste
• Professional, insured crews — no day labor

We work with [X] property management companies in [Area] and would love to introduce ourselves.

Would you be open to a 10-minute call this week? [Booking Link]

[Signature]
```

### 7.10 Seasonal Campaign — Spring Cleanout Blast
**SMS (April/May broadcast to past customers and "Interested" pipeline):**
```
"🌱 Spring cleanout time! [Company Name] is booking garage, basement, and yard waste haul aways for [Month]. Slots fill fast this time of year. Get on the schedule now — reply SPRING or call [Phone]. First 10 bookings get [offer]."
```

### 7.11 Moving Inquiry Response
```
"Hi [First Name]! Thanks for reaching out about your move. To get you an accurate quote, can you share:

1. Moving from/to (same city, or longer distance)?
2. Approximate home size (1-bed, 2-bed, house)?
3. Target move date?

We'll get back to you with a quote within 30 minutes. — [Company Name]"
```

### 7.12 Moving — Pre-Move Check-In (1 Week Out)
```
"Hi [First Name]! One week until your move with [Company Name]. Quick tips:
📦 Label boxes with room names
🏋️ Let us know about heavy/specialty items (piano, safe, gym equipment)
🅿️ Reserve parking for our truck if needed
📞 Questions? Reply or call [Phone]

We've got you covered! See you [Date]."
```

---

## SECTION 8: BOOKING FLOW & INSTANT ONLINE QUOTE

### 8.1 Why Online Quoting is the Major Differentiator

The biggest gap in the junk removal industry is the absence of upfront online pricing. Customers want to know the price before they call. 1-800-GOT-JUNK built a $600M+ business partly on the back of giving customers a clear price range online.

For independent operators, an instant online quote — even an approximate one — is a massive competitive advantage.

**GHL Implementation:**

**Option A: GHL Survey/Form as Quote Calculator**
- Multi-step form: Item category → Volume estimate → Location → Contact info
- Based on responses, display price range (built into form logic)
- Form submits → Contacts added to CRM → Instant SMS follow-up fires

**Option B: Embedded third-party calculator (Quotient, PandaDoc, custom)**
- Integrated via GHL embed or iFrame on landing page
- Submission webhook connects to GHL contact + pipeline

**Option C: GHL Chat Widget with Pricing Logic**
- Chat popup on website asks: "What do you need hauled away?"
- Based on chat responses, provides approximate price range
- Captures contact info mid-conversation

**Recommended for 1app Snapshot:** Option A (GHL-native form) as the base offering, with Option B as an upgrade. Native keeps it clean and fully within the CRM.

### 8.2 Booking Form Fields (Residential)
- First Name, Last Name
- Phone Number (SMS consent checkbox — CRITICAL for compliance)
- Email
- Service Address (with postal/zip code)
- Job Type: [ ] Furniture Removal [ ] Appliance Haul Away [ ] Full Truckload [ ] Half Load [ ] Estate/Cleanout [ ] Demolition Debris [ ] Yard Waste [ ] E-Waste [ ] Other
- Volume Estimate: [ ] 1–2 items [ ] ¼ Load [ ] Half Load [ ] Full Load [ ] Not Sure
- Preferred Date: [Date Picker]
- Preferred Time: [ ] Morning [ ] Afternoon [ ] Flexible
- Additional Notes (access issues, heavy items, stairs, etc.)
- How did you hear about us? [Dropdown for attribution]

### 8.3 Commercial Cleanout Request Form
- Business/Property Name
- Contact Name + Title
- Phone + Email
- Property Address
- Job Type: [ ] Office Cleanout [ ] Retail/Commercial Space [ ] Tenant Turnover [ ] Storage Unit [ ] Construction Debris [ ] Multi-Unit Property [ ] Other
- Estimated Volume: [ ] Small (pickup truck) [ ] Medium (half ton) [ ] Large (full truck) [ ] Multiple loads [ ] Not Sure
- Timeline: [ ] ASAP [ ] Within 1 week [ ] Within 1 month [ ] Flexible
- Additional Details
- Would you like regular recurring service? [ ] Yes [ ] No

---

## SECTION 9: COMMERCIAL CLEANOUT WORKFLOW

### 9.1 Property Manager Nurture Track

**Who They Are:** Property managers handle residential apartment buildings, condo complexes, commercial strip malls, industrial units. Their pain is tenant turnover — when a tenant leaves, they need the unit cleared fast so it can be re-rented.

**What They Need:**
- Fast response times (days, not weeks)
- Professional, presentable crews
- Before/after photo documentation (for security deposit disputes)
- Volume pricing for recurring work
- Simple invoicing (NET 30 terms often expected)

**Snapshot Workflow:**
1. Contact added as "Property Manager" via manual entry or intake form
2. Initial outreach email sent (Day 1) — service overview + portfolio
3. SMS Day 4 follow-up
4. Value-add email Day 10 (content-focused — "3 things to include in your tenant lease about bulk item removal")
5. If no response after 21 days — move to "Long Game" list — quarterly check-in SMS

**When Relationship Established:**
- Dedicated contact record with property count, average job size, typical volume
- Tagged "Property Manager — Active" for priority response SLA
- Monthly check-in scheduled via GHL task assignment

### 9.2 Renovation Contractor Workflow

**Who They Are:** Residential renovation contractors, kitchen/bath remodelers, addition builders. They generate demolition debris — drywall, subflooring, framing, roofing materials. Most have a regular trash hauler but hate overage fees and dumpster swap-outs.

**Value Prop:**
- On-call haul away — call same day, get a truck
- Pricing per load, not per day (vs. dumpster rental)
- Crews who can help load (labor + haul)
- No dumpster damage liability

**Snapshot Workflow:**
1. Contact added as "Contractor" via intake or manual
2. Outreach email — position against dumpster rental (cost comparison angle)
3. SMS Day 5 — "We handle same-day demo debris haul away. No dumpster swaps, no waiting. Interested?"
4. Follow up with case study or before/after of a renovation job cleanout

---

## SECTION 10: ESTATE CLEANOUT WORKFLOW

### 10.1 Understanding the Estate Cleanout Customer

Estate cleanouts are triggered by:
- Death of a family member (executors, family members handling estate)
- Senior move to assisted living or downsizing
- Hoarding situations (family intervention)
- Pre-sale property clearing (often real estate agent-referred)

**Emotional Profile:**
- Often stressed, overwhelmed, grieving
- Trust is paramount — they're inviting strangers into an emotionally significant space
- Decision-making can be slow — respect the pace
- Often don't know what they have (value items mixed with junk)
- May need donation coordination (items going to charity, family members)
- May need specialty removal (piano, safe, antiques, vehicles)

### 10.2 What They Need from the Operator:
- Clear, written quote with scope of work
- Transparent process: what's recycled, donated, vs. disposed
- Flexible scheduling (they're coordinating with multiple family members)
- References or reviews from similar jobs
- Professional, compassionate communication

### 10.3 Snapshot Workflow (Distinct from Residential)

**Stage 1 — Soft Inquiry:**
- Empathetic intake form with minimal required fields
- Automated response: "Thank you — we understand this can be a difficult time. We'll reach out within [X hours] to learn more about your situation."
- No hard-sell language. No urgency triggers.

**Stage 2 — Consultation:**
- 30-minute consultation call (or in-person visit for larger estates)
- GHL calendar booking link for consultation (different calendar from standard booking)
- Pre-consult SMS: "Looking forward to speaking with you, [First Name]. Take your time — we're here to help, not rush."

**Stage 3 — Proposal:**
- Written scope: square footage, number of rooms, estimated load volume, special items noted
- Timeline: expected days to complete
- Donation coordination: which charity, who arranges pickup
- Post-cleanout: broom-swept, photos provided

**Stage 4 — Approval & Scheduling:**
- Signed proposal or email confirmation accepted
- Multi-day scheduling via GHL calendar blocks
- Family member coordination notes in contact record

**Stage 5 — Active Cleanout:**
- Daily progress updates (optional — ask client preference)
- Photo documentation throughout
- Flagging process for items with potential value (consult with family before discarding)

**Stage 6 — Completion:**
- Final walkthrough with client/family
- Photos sent
- Invoice + donation receipts if applicable
- Sensitive review request: "When you're ready, a review would mean a lot to our team. No rush."

---

## SECTION 11: REFERRAL PARTNERSHIP SYSTEM

### 11.1 Partnership Categories

**Tier 1 — High Value (Build First):**
- Senior living facilities / retirement communities (frequent moves + cleanouts)
- Real estate attorneys handling probate estates
- Licensed real estate agents in local MLS
- Property management companies (multi-unit residential)

**Tier 2 — Medium Value (Build Second):**
- Moving companies (cross-referral)
- Home staging companies
- Senior relocation specialists
- Renovation contractors

**Tier 3 — Long Game:**
- Charity/thrift stores (they refer customers who need items hauled)
- Insurance adjusters (flood/fire damage cleanouts)
- Hoarding intervention counselors / social workers

### 11.2 GHL Tracking for Referral Partners

Each referral partner should be:
- Tagged in CRM as "Partner — [Category]" (e.g., "Partner — Real Estate Agent")
- Have a custom field: "Partner — Referral Count" (manually updated or via automation)
- Tracked via UTM parameter on their referral link if using a custom URL
- Assigned a quarterly check-in task in GHL

**Referral Source Tracking:**
- Custom field on contact record: "How did you hear about us?"
- Options match lead sources: Google, Kijiji, Facebook, Referred By [Partner Name], Other
- Reports built in GHL to show which partner is sending most volume

### 11.3 Partner Recognition Workflow
**Trigger:** Contact's referral source tagged as a specific partner

```
Automated email to partner (same day lead captured):
"Hi [Partner Name] — just wanted to let you know [First Name] reached out today and mentioned you referred them. We'll take great care of them. Thank you for thinking of us! — [Company Name]"

After job complete — Email to partner:
"Quick update — we completed the job for [First Name] today. Everything went smoothly. Thank you again for the referral. We're always here for your clients. 🙏"
```

---

## SECTION 12: REVIEW GENERATION SYSTEM

### 12.1 Why Reviews Win in Junk Removal

Junk removal is a trust purchase — customers are letting strangers haul away their belongings. Reviews are the primary trust signal.

**Data:**
- 86% of customers read reviews before hiring a local service business
- Moving from 4.2 → 4.8 stars can increase booking rate by 30–40%
- 200+ reviews signals established business — dramatically increases Google Local Pack ranking
- Response to reviews (positive and negative) shows professionalism

**Most operators have:**
- 20–75 reviews after 3–5 years in business
- Zero automated review system
- Sporadic review requests (only when owner remembers to ask)

**With automated review workflow:**
- Operators can generate 3–5 reviews per week from existing job volume
- 200+ reviews achievable in 12–18 months

### 12.2 Review Timing Research

**Best times to ask for a review (junk removal):**
- 2–4 hours after job completion (still excited about clear space)
- SMS converts better than email for review requests (70%+ higher open rate)
- Asking in the first 24 hours captures 80% of all reviews you'll get

**Worst times:**
- Immediately at job site (crew shouldn't ask — awkward)
- More than 3 days after job (memory fades, motivation drops)
- Via email-only (too easy to ignore)

### 12.3 GHL Review Workflow Details

**Step 1 — Primary Ask (2 hours post-job, SMS):**
Direct link to Google review. 15 words or less. No preamble.

**Step 2 — Secondary Ask (24 hours, if no review, SMS):**
Slightly longer, mention the crew by name if possible.

**Step 3 — Final Ask (3 days, email):**
Friendly, not pushy. Offer an alternative if they prefer (Facebook, Yelp).

**Step 4 — Stop sequence if review detected:**
GHL webhook from Zapier/ReviewTrackers/BirdEye can trigger "Review Received" tag → stops sequence.

**Manual override:** If customer mentions complaint in any communication, remove from review sequence immediately, flag for owner follow-up.

### 12.4 Negative Review Response Templates

**Template 1 — Operational Issue:**
"Thank you for your feedback, [First Name]. We're sorry this experience didn't meet our standards. We take all feedback seriously — please reach out to us directly at [Phone/Email] so we can make this right. — [Owner Name], [Company Name]"

**Template 2 — Pricing Dispute:**
"We're sorry for any confusion about pricing, [First Name]. We strive to be upfront about our costs. Please contact us directly at [Phone] and we'd like to understand what happened. — [Company Name]"

---

## SECTION 13: SNAPSHOT TECHNICAL BUILD SPECIFICATIONS

### 13.1 GHL Objects to Build

**Contacts:**
- Custom Fields: Job Type, Load Size, Source, Property Type, Partner Name, Review Status, Job Count (lifetime), Total Revenue (lifetime)
- Tags: Residential, Commercial, Estate, Moving, Property Manager, RE Agent, Contractor, Active Customer, VIP, Review Received, Referral Partner, Seasonal Campaign

**Pipelines (4 total):**
1. Junk Removal — Residential (13 stages)
2. Commercial Cleanouts — B2B (12 stages)
3. Estate Cleanouts (11 stages)
4. Moving Services (12 stages)

**Workflows (minimum 12 core workflows):**
1. Instant Quote Request — Residential
2. Booking Confirmation Sequence
3. Day-Before / Day-Of Reminders
4. Post-Job Review Request
5. Quote Follow-Up (3-step)
6. 30-Day Lead Reactivation
7. Commercial Prospect Outreach
8. Estate Cleanout Intake (sensitive)
9. Real Estate Agent Referral Outreach
10. Property Manager Outreach
11. Seasonal Campaign Trigger
12. Referral Partner Notification
13. Moving Booking Confirmation + Pre-Move Prep
14. Post-Move Review Request
15. Same-Day Urgency Blast

**Forms (4 core):**
1. Residential Quote Request Form (multi-step)
2. Commercial Cleanout Inquiry Form
3. Estate Cleanout Consultation Request Form
4. Moving Quote Request Form

**Calendars (3):**
1. Standard Booking — Junk Removal (slots by truck availability)
2. Commercial Site Assessment (45–60 min consultation)
3. Estate Cleanout Consultation (30 min — soft entry)

**Snapshots / Landing Pages:**
1. Residential Landing Page (Google Ads / LSA)
2. Commercial Landing Page (Property Managers / B2B)
3. Estate Cleanout Landing Page (empathetic, trust-focused)
4. Moving Services Landing Page

**Email Templates (pre-built, branded):**
- Welcome / Quote Confirmation
- Booking Confirmation
- Pre-Move Checklist
- Post-Job Thank You + Review
- Commercial Outreach (cold)
- Estate Cleanout Info Package
- Referral Partner Introduction
- Reactivation Campaign

**Automation Triggers Configured:**
- Form submission → pipeline stage + tag + workflow
- Pipeline stage change → workflow triggers
- Tag applied → workflow enrollment
- Calendar appointment booked → confirmation sequence
- Date-based triggers (day before, day of, 2 hrs post-job)

### 13.2 GHL Reporting Dashboard

**Recommended Widgets:**
- New Leads (last 7 / 30 days)
- Leads by Source (Google, Kijiji, Facebook, Referral, Direct)
- Pipeline Conversion Rate (Quote Sent → Booked)
- Jobs Completed (weekly/monthly)
- Reviews Generated (monthly)
- Revenue by Job Type (Residential vs. Commercial vs. Estate)
- Open Follow-Up Sequences Count
- Lost Leads (price vs. no response)

---

## SECTION 14: DIFFERENTIATION — WHAT MAKES THIS SNAPSHOT STAND OUT

### 14.1 Industry-Specific Language Throughout

No generic "customer" references. The snapshot uses the industry's actual vocabulary:
- Haul away, cleanout, full truckload, half load, quarter load
- Demolition debris, estate cleanout, hoarder cleanout, e-waste, donation drop-off
- Load size pricing, same-day availability, property manager outreach
- Before/after photos, crew dispatch, on the way text

### 14.2 Four Distinct Pipelines (Not One Generic Pipeline)

Most competitors give operators a single pipeline and expect them to fit all job types in. This snapshot recognizes that a hoarder cleanout is fundamentally different from a same-day furniture haul away — emotionally, operationally, and commercially.

### 14.3 The Referral Partner Infrastructure

No other junk removal snapshot includes a full B2B referral partner management system. This is the lever that transforms a single-truck operator into a company with 10–20 commercial accounts generating consistent monthly volume.

### 14.4 Estate Cleanout as a Distinct Workflow

Estate cleanouts command significantly higher ticket sizes ($1,500–$8,000+) and require a completely different tone and process than standard residential haul away. Building this as a standalone workflow and pipeline is unique in the market.

### 14.5 Compliance-Ready SMS Sequences

All SMS templates built with TCPA/CRTC compliance in mind:
- Consent captured at point of form submission
- Opt-out language included in first SMS
- Unsubscribe/STOP instructions in all automated messages
- Sequence stops on STOP reply (GHL native)

### 14.6 Moving Company Bolt-On

The snapshot includes a complete moving company module — making it deployable to two adjacent industries, not just one. This doubles the addressable market for 1app with no additional build cost.

---

## SECTION 15: ONBOARDING CHECKLIST FOR 1APP CLIENTS

When onboarding a junk removal or moving client onto this snapshot:

**Week 1 — Foundation:**
- [ ] Connect GHL sub-account and load snapshot
- [ ] Customize all SMS/email templates with company name, phone, logo
- [ ] Connect Google Business Profile for review requests
- [ ] Set up tracking phone number (GHL native)
- [ ] Configure business hours in GHL settings
- [ ] Add team members + assign roles
- [ ] Import existing customer list (past jobs → tag "Past Customer")

**Week 2 — Lead Capture:**
- [ ] Embed quote request form on existing website
- [ ] Set up GHL landing page (residential)
- [ ] Configure LSA webhook (if running Google LSA)
- [ ] Connect Facebook Lead Ads (if running FB ads)
- [ ] Test all form submissions → confirm pipeline stage and workflow enrollment

**Week 3 — Automation Testing:**
- [ ] Test instant quote follow-up sequence (send test lead)
- [ ] Test booking confirmation workflow
- [ ] Test review request trigger
- [ ] Test day-before reminder
- [ ] Confirm all SMS sending numbers are verified and compliant

**Week 4 — Commercial Pipeline Launch:**
- [ ] Build list of 20–30 local property managers + real estate agents
- [ ] Import to CRM with correct tags
- [ ] Launch commercial outreach sequences
- [ ] Schedule owner review of pipeline in 2 weeks

**Ongoing (Monthly):**
- [ ] Review pipeline — move stuck contacts
- [ ] Review review count vs. prior month
- [ ] Run seasonal campaign if applicable
- [ ] Check referral partner activity
- [ ] Optimize underperforming sequences based on reply rates

---

## SECTION 16: PRICING RECOMMENDATIONS FOR 1APP CLIENTS

**Setup Fee:** $497–$997 (snapshot load, customization, testing, training)
**Monthly Retainer:** $197–$397/month (GHL sub-account + ongoing support)

**Value Justification for Client:**
- A single additional residential job booked per week from automated follow-up = $250–$600/week = $12,000–$31,200/year
- One commercial property manager account = $1,500–$5,000/month recurring
- Review velocity improvement → Local Pack ranking → organic leads worth $500–$2,000/month in ad spend savings

**ROI Statement for Sales Conversations:**
"If this system helps you book just 2 more jobs per week that you would have lost without follow-up, it pays for itself in the first month. Everything else — the reviews, the commercial accounts, the referral partners — that's your growth engine."

---

## APPENDIX A: JUNK REMOVAL INDUSTRY GLOSSARY

| Term | Definition |
|------|-----------|
| **Haul away** | Removal and transportation of unwanted items |
| **Cleanout** | Complete removal of all items from a space (basement, garage, house) |
| **Full truckload** | Entire truck capacity loaded with junk (~10–15 cubic yards) |
| **Half load** | 50% of truck capacity |
| **Quarter load** | Minimum load — few items, priced accordingly |
| **Estate cleanout** | Complete clearance of a property following death or major life transition |
| **Hoarder cleanout** | Large-volume, often emotionally complex cleanout of accumulated items |
| **Demolition debris** | Construction waste from renovation/demolition work |
| **Appliance removal** | Specific haul away of fridges, washers, dryers, dishwashers, etc. |
| **E-waste** | Electronic waste — computers, TVs, phones — requires specialized disposal |
| **Donation drop-off** | Items in usable condition taken to Goodwill, Salvation Army, or similar |
| **Property cleanout** | Commercial or residential property cleared for re-rental/re-sale |
| **Eviction cleanout** | Removal of tenant belongings after eviction |
| **Commercial cleanout** | Large-scale removal from offices, retail, warehouses |
| **White glove** | Premium service — extra care, crew in uniform, specialty wrapping |
| **Load and go** | Basic service — customer loads, crew hauls |
| **Full-service** | Crew does all carrying and loading, customer doesn't lift anything |

---

## APPENDIX B: COMPETITIVE SNAPSHOT COMPARISON

| Feature | Competitor A (Generic Home Services) | Competitor B (Basic Junk Removal) | 1app Junk Removal Snapshot |
|---------|--------------------------------------|-----------------------------------|---------------------------|
| Industry-specific language | ❌ | Partial | ✅ Full |
| Pipelines | 1 generic | 1 basic | 4 specialized |
| Workflows | 3–5 | 4–6 | 15+ |
| Commercial pipeline | ❌ | ❌ | ✅ |
| Estate cleanout workflow | ❌ | ❌ | ✅ |
| Moving company module | ❌ | ❌ | ✅ |
| Referral partner system | ❌ | ❌ | ✅ |
| Online instant quote form | Basic | Basic | ✅ Multi-step |
| Review generation | Basic | Basic | ✅ 3-step sequence |
| Seasonal campaigns | ❌ | ❌ | ✅ |
| Reactivation campaigns | ❌ | Basic | ✅ |
| Compliance-ready SMS | Partial | Partial | ✅ |
| Onboarding checklist | ❌ | ❌ | ✅ |
| B2B outreach sequences | ❌ | ❌ | ✅ |

---

## APPENDIX C: QUICK WIN OPPORTUNITIES FOR NEW CLIENTS

These can be implemented in the first week and show results immediately:

1. **Activate the review request workflow** — every completed job triggers a review SMS 2 hours later. Operators will see their first new reviews within 48 hours of activation.

2. **Import past customer list** — every past customer gets a 30-day reactivation SMS: "Need another haul away? We're running routes in [Area] this week." Even a 5% response rate on a list of 200 customers = 10 new inquiries.

3. **Set up missed call text back** — any missed call gets an immediate SMS: "Sorry we missed your call — we're likely on a job. What can we haul away for you? Text us back and we'll get you a price." This alone captures 20–30% of leads that would have called a competitor.

4. **Launch property manager outreach** — import a list of 20 local property managers and activate the outreach sequence. One property manager relationship = consistent monthly volume.

5. **Same-day urgency blast** — when trucks are open, send a same-day availability SMS to all "Interested — Not Booked" contacts. One blast typically books 1–3 jobs from contacts that were previously lost.

---

*Document prepared by 1app Technologies Inc. | Research compiled July 2026*
*For internal use in GHL snapshot development and client onboarding*
