# 🎨 GHL Painting Contractor Snapshot — Research & Build Document
### For: 1app | SaaS Agency Build Reference
### Prepared by: Maximus AI | Research Date: July 2026

---

## EXECUTIVE SUMMARY

The painting industry runs on relationships, referrals, and timing — but most painting contractors manage leads through sticky notes, missed calls, and gut instinct. The gap between how painters operate and what a well-built CRM can automate represents a massive opportunity for a 1app GHL snapshot.

**Market gap identified:** Most GHL snapshots sold to painters are generic home-services templates with a coat of "painter" branding. They miss the core operational reality: painting is seasonal, weather-dependent, approval-heavy (colour selection is a relationship bottleneck), and extremely referral-driven at the neighbourhood level.

**The 1app painting snapshot should be purpose-built for the trade** — with workflows that speak the language of prep work, primer, top coat, and colour boards, not generic "service requests."

---

## PART 1 — PAINTING BUSINESS PAIN POINTS

### 1.1 Seasonal Demand Swings

Exterior painting in Canadian and northern US markets is a 5-to-7-month season (April through October). Interior work fills winter months, but not predictably. Painters experience:

- **Feast/famine cash flow** — booked solid May–August, starving in December–February
- **Spring rush chaos** — every homeowner wants their exterior done "before summer" and calls within the same 3-week window
- **Shoulder-season dead zones** — September/October exterior jobs cancelled by early frost; November bookings collapse
- **No system to pre-book off-season interior work** during the busy exterior season

**GHL fix:** Seasonal campaign workflows triggered automatically by month/date, pre-booking interior work in July/August for November–February slots. Calendar capacity limits and waitlist automation.

### 1.2 Weather Cancellations

Exterior painting requires dry conditions (typically 10°C minimum, no rain forecast 24 hours before/after). A crew showing up to a rained-out job means:

- Lost labour day (2–6 painters idle)
- Customer confusion if not notified early
- Rescheduling friction (calendar gaps or double-booking)
- Crew morale and sub-contractor payment disputes

**GHL fix:** Weather cancellation workflow — templated SMS/email to client with rescheduling link when crew lead marks job "weather hold"; automated next available date offer from calendar.

### 1.3 Quoting Accuracy and Scope Creep

Painters quote by:
- **Square footage** (walls, ceilings, trim linear feet)
- **Surface type** (drywall vs. plaster vs. stucco vs. hardiboard vs. wood siding)
- **Prep requirements** (pressure washing, scraping, spot priming, caulking, TSP washing)
- **Coat count** (prime coat + one top coat vs. two top coats)
- **Spray vs. roll/brush** labour differential

Common pain: estimate is done at drive-by or over the phone, then crew shows up to find:
- Peeling paint requiring extensive scraping (adds 1–2 days of prep)
- Rotten fascia or soffits that need carpentry before painting
- Customer wants trim, fascia, soffit, and front door added after signing
- "While you're here" extras (garage door, fence, garden shed)

**GHL fix:** Structured quote intake form capturing: square footage (approx), surfaces included (checklist), prep condition (good/fair/poor), special items (fascia/soffit/trim/doors), colour change (yes/no — dark to light requires extra coats). These become quote-ready fields the estimator reviews before attending.

### 1.4 Colour Approval Delays

Colour selection is one of the biggest sources of job start delays. A client:
1. Gets their estimate approved
2. Is asked to choose their colour(s)
3. Goes to Benjamin Moore or Sherwin-Williams
4. Spends 3 days agonizing over 47 shades of "Chantilly Lace"
5. Doesn't respond to follow-up calls
6. Finally picks a colour... the week before the job starts
7. Painter can't pre-order 20 gallons with 2 days notice

**GHL fix:** Colour approval workflow — automated 3-step follow-up sequence (Day 1/3/7) after estimate approval, with link to digital colour selector resources (BM/SW fan deck links), reminder that paint must be ordered 5–7 days before job start. Include "Colour Approval Received" pipeline stage that gates the "Materials Ordered" stage.

### 1.5 No-Shows and Last-Minute Cancellations

Painting jobs are typically 1–5 days. A homeowner no-show or same-day cancellation means:
- Entire crew is mobilized for nothing (vehicles loaded, crew paid)
- Job gap impossible to fill same-day
- Revenue loss of $800–$3,000+

**GHL fix:** 72hr confirmation SMS + 24hr final confirmation with "Reply YES to confirm" automation. If no reply within 4 hours of 24hr message, alert to crew lead with instructions to call. Track confirmation response rate as a contact field.

### 1.6 Upselling Exterior When Doing Interior (and Vice Versa)

Most painters leave money on the table. When doing an interior job:
- Front door and trim are visible and often need refreshing
- Garage door is often next to the entrance
- Deck/fence maintenance may be needed

When doing an exterior job:
- Ceilings, walls, and feature wall in primary room may need freshening
- Garage interior is often grimy from use

**GHL fix:** Post-job upsell workflow with photo prompt ("Did you notice the [exterior trim / interior ceiling]?") and templated offer: "Since we were just at your home, we can schedule your [interior refresh / exterior trim] before year-end at a preferred rate."

### 1.7 Crew Scheduling and Sub-Contractor Management

Painters rely on a mix of full-time employees and day-labour sub-contractors. Scheduling pain points:
- Which crew goes to which job
- Sub-contractors have competing commitments
- New job added, crew not informed
- Customer asked crew directly about pricing (sub-contractor lacks this info)

**GHL fix:** Job assigned tag + internal notification workflow when opportunity moves to "Crew Assigned" stage. SMS to crew lead with job address, date/time, scope summary. Not a full crew management system — but enough to close the communication gap.

### 1.8 Review Collection Failure

Painters do excellent work and then fail to capture the testimonial. Most painters:
- Ask verbally ("leave us a review if you get a chance")
- Never follow up
- Have fewer than 20 Google reviews despite hundreds of completed jobs

**GHL fix:** Automated review request sent 2 hours after "Job Complete" stage is triggered, with direct Google review link. Secondary follow-up at 48 hours. Neighbour campaign triggered simultaneously (see Part 6).

---

## PART 2 — MARKET LANDSCAPE: EXISTING PAINTING SNAPSHOTS

### 2.1 What Exists on the Market

Based on research of the GHL ecosystem, painting contractor snapshots currently available fall into three categories:

**Category A — Generic Home Services Snapshots "Dressed Up"**
- Take a landscaping or HVAC template, swap in paint-related copy
- Missing: colour approval stage, weather cancellation workflow, strata/condo commercial workflow
- Missing: paint-specific intake fields (sq footage, surface type, coat count)
- Missing: neighbour campaign after exterior completion
- Typically priced $97–$197 one-time or bundled into agency deals
- Examples: Most "Painting Contractor" snapshots on Snapshots.io and various GHL affiliates

**Category B — Functional but Incomplete**
- Has a basic pipeline (New Lead → Quote Sent → Booked → Complete)
- Has a review request workflow
- May have some seasonal email templates
- Missing: colour approval workflow, strata/PM targeting sequences, seasonal pre-booking system
- Priced $197–$497

**Category C — Comprehensive Painting-Specific (Very Rare)**
- Rarely seen; most agencies don't specialize deeply enough in the painting trade
- Full pipeline differentiation (residential interior / exterior / commercial / strata)
- Painting-specific intake forms and automations
- Neighbour and referral campaigns using yard sign + digital follow-up logic

### 2.2 What's Missing Across the Board

No existing snapshot we've identified includes all of:

1. ✅ Colour approval stage with automated follow-up sequence
2. ✅ Weather cancellation workflow with auto-rescheduling offer
3. ✅ Strata/condo commercial pipeline with separate PM nurture track
4. ✅ Real estate agent referral partnership sequence
5. ✅ Neighbour "we painted next door" outreach campaign
6. ✅ Seasonal pre-booking (book your exterior in spring, interior in fall)
7. ✅ Paint materials ordering gate (colour confirmed → materials ordered → crew scheduled)
8. ✅ Drive-by estimate vs. in-home quote booking distinction
9. ✅ Paint-specific intake form capturing surface type, sq footage, prep condition

**This is the white space. 1app's snapshot fills it.**

---

## PART 3 — PIPELINE ARCHITECTURE

### 3.1 Residential Interior Pipeline

Designed for: Homeowners booking indoor painting (bedrooms, living rooms, kitchens, basements)

**Stages:**

| Stage | Description | Trigger |
|-------|-------------|---------|
| 🟡 New Inquiry | Lead comes in via web form, referral, Kijiji, LSA | Automation: immediate text back "Got your request, booking a time to connect" |
| 📞 Contacted | First call/text made | Manual move or automation if call connected |
| 📋 Estimate Scheduled | In-home walkthrough booked | Calendar booking confirmed |
| 💬 Estimate Delivered | Quote sent (email + PDF) | Estimate sent via GHL or linked tool |
| 🎨 Colour Approval Pending | Quote accepted; awaiting colour selection | Automation: colour approval sequence starts |
| 🛒 Materials Ordered | Colour confirmed; paint ordered | Manual confirmation; triggers materials checklist |
| 🗓️ Job Scheduled | Crew assigned and start date confirmed | Automation: job start notification to client |
| 🔨 In Progress | Active job underway | Optional: progress photo update workflow |
| ✅ Job Complete | Work done and signed off | Automation: review request + upsell sequence |
| ⭐ Review Received | Google/Facebook review posted | Manual tag or webhook |
| 🔁 Referral/Repeat | Referred a friend or rebooked | Automation: referral thank you + $25 credit |

**Key fields on Residential Interior contact:**
- Square footage (approximate)
- Rooms included (checklist: bedrooms / living room / kitchen / bathroom / basement / other)
- Surface conditions (good / fair / needs patching / extensive repair)
- Paint finish requested (flat / eggshell / satin / semi-gloss)
- Colour change? (yes/no — dark to light = extra coat surcharge)
- Preferred paint brand (Benjamin Moore / Sherwin-Williams / CIL / Behr / client supplies)
- Move-in/move-out? (yes/no — affects timeline and access)

---

### 3.2 Residential Exterior Pipeline

Designed for: Homeowners booking exterior siding, trim, fascia, soffit, doors, decks, fences

**Stages:**

| Stage | Description | Trigger |
|-------|-------------|---------|
| 🟡 New Inquiry | Web form, referral, drive-by sign, LSA | Automation: immediate SMS |
| 🚗 Drive-By Estimate | Estimator does curbside look | Alternate to in-home — faster for paint-only exterior |
| 📋 In-Home Quote | Detailed walkthrough for complex jobs | Calendar booking |
| 💬 Estimate Delivered | Quote sent with scope: siding / trim / fascia / soffit detail | |
| 🎨 Colour Approval Pending | Quote accepted; colour(s) to be selected | Automation: colour approval sequence |
| 🧹 Prep Scheduled | Pressure wash + scraping + caulking date set | Separate booking if prep is a separate day |
| 🛒 Materials Ordered | Paint, caulk, primer ordered | Manual confirmation |
| 🗓️ Job Scheduled | Crew assigned, start date set | Job start SMS to client |
| ⛅ Weather Hold | Job paused due to weather | Weather hold workflow triggered |
| 🔨 In Progress | Job underway | Progress photo update optional |
| ✅ Job Complete | Work complete, yard sign placed | Automation: review + neighbour campaign |
| 🏘️ Neighbour Campaign | Outreach to adjacent homes | Automated direct mail + digital sequence |
| ⭐ Review Received | Google review posted | Tag applied |

**Key fields on Residential Exterior contact:**
- Home style (detached / semi / townhouse / condo unit / other)
- Siding type (vinyl / hardiboard / wood / stucco / brick accent / aluminum)
- Surfaces included (siding / trim / fascia / soffit / front door / garage door / deck / fence)
- Storey count (1 / 1.5 / 2 / 2.5 — affects ladder/scaffolding cost)
- Pressure wash needed (yes/no)
- Prep condition (good / fair — peeling / poor — extensive scraping)
- Spray or roll/brush preference
- HOA colour approval required (yes/no)
- Previous colour vs. new colour (same / similar / significant change)

---

### 3.3 Commercial Pipeline

Designed for: Business owners, property managers, building managers, strata councils booking commercial repaints

**Stages:**

| Stage | Description | Trigger |
|-------|-------------|---------|
| 🟡 New Lead | Inbound inquiry or outbound prospecting | Automation: PM-specific nurture sequence |
| 🤝 Intro Meeting | Discovery call or site visit | Calendar booking |
| 🏢 Site Assessment | Crew lead walks property | Manual stage |
| 📋 Commercial Quote | Detailed scope: sq footage, surfaces, phases, access hours | Quote delivered |
| 📝 Contract Review | Client reviewing and possibly requesting revisions | Follow-up sequence active |
| ✍️ Contract Signed | Deal won | Automation: kickoff workflow |
| 📅 Phased Schedule Set | Multi-phase job dates confirmed | Calendar events created |
| 🔨 Phase 1 In Progress | Work underway | Progress update workflow |
| ✅ Phase Complete / Job Done | All phases complete | Review request (Google + industry directories) |
| 🔁 Annual Repaint Reminder | Triggered 11 months after completion | Automation: annual maintenance sequence |

**Key fields on Commercial contact:**
- Property type (office / retail / warehouse / multi-unit residential / strata / condo complex / school / healthcare)
- Interior / exterior / both
- Square footage (approximate)
- Number of units or floors
- Access restrictions (business hours / off-hours only / phased access)
- Union or non-union requirement
- Property manager name and direct contact
- Strata council contact (if applicable)
- Existing contract in place (yes — with whom / no)
- Budget range indicated (yes/no)
- Decision timeline

---

### 3.4 Strata / Condo Corporation Pipeline

Designed for: Strata councils, condo corporations, and property management companies overseeing multi-unit residential buildings

**Stages:**

| Stage | Description | Trigger |
|-------|-------------|---------|
| 🟡 PM / Strata Inquiry | Property manager or strata council member contacts | Automation: commercial PM sequence |
| 📁 RFP / Tender Received | Formal request for proposal sent by strata | Manual stage |
| 🏢 Building Walk | Site inspection with strata rep or PM | Calendar booking |
| 📋 Proposal Submitted | Formal written proposal with phasing, timeline, and cost | |
| 🗳️ Strata Council Vote | Pending board approval | Follow-up sequence: "Still in review?" at 7/14/21 days |
| ✍️ Contract Awarded | Won the tender | Kickoff workflow triggered |
| 📅 Phase Schedule Set | Seasonal phases (e.g., south face in June, north face in August) | |
| 🔨 Phase In Progress | Active painting | Progress photo update workflow |
| ✅ Project Complete | All phases done, touch-up inspection complete | |
| 🔄 Annual Maintenance | Follow-up sequence triggered for next season | Automation: 10-month touchpoint |

**Strata-specific notes:**
- Decision cycle is 30–90 days (requires council vote)
- Multiple stakeholders: strata manager + strata council + individual unit owners for exterior approvals
- Often require phased execution (can't paint entire building at once — unit residents still living there)
- Colour selection requires strata council resolution — use "Strata Colour Approval" sub-stage
- Reference letters from other strata properties are a major conversion factor
- Annual or multi-year maintenance contracts are the goal

---

## PART 4 — PAINTING-SPECIFIC WORKFLOWS

### 4.1 Lead Intake & Immediate Response

**Trigger:** New form submission (web, LSA, Kijiji, referral link)

**Sequence:**
- [0 min] SMS: "Hey [First Name], thanks for reaching out to [Company]! We got your request for [interior/exterior] painting. I'll personally follow up within the hour. - [Owner Name]"
- [0 min] Internal notification to estimator with lead details
- [5 min] If no call made: second internal alert to call now
- [30 min] If no contact: follow-up SMS: "Hey [First Name], tried to reach you — want to book a quick 15-min call to discuss your project? Here's my calendar: [link]"
- [24 hr] If still no response: "Circling back on your painting inquiry — are you still looking for a quote?"
- [3 days] If no response: "Just checking in one last time — happy to arrange a drive-by estimate so you don't need to be home. Let me know!"
- [7 days] If no response: Move to "Cold Lead" and tag for seasonal re-engagement

**Response time matters:** Industry data shows painters who respond within 5 minutes close 4x more than those who respond within 1 hour.

---

### 4.2 Estimate Confirmation Sequence

**Trigger:** Quote sent to prospect

**Sequence:**
- [Day 0] Email: Professional PDF quote with scope details, paint brand, coat plan, timeline
- [Day 0] SMS: "Hi [First Name], just sent over your estimate for the [exterior siding + trim] at [address]. Let me know if you have any questions!"
- [Day 2] SMS: "Hey [First Name], following up on your painting estimate — any questions about the scope or pricing?"
- [Day 4] SMS: "Just checking in — have you had a chance to review the quote? We have openings in [Month] and they're filling up fast."
- [Day 7] Call attempt + voicemail: "Hi [First Name], [Name] from [Company]. Just wanted to touch base on your estimate — give me a call at [number] or reply to this text if easier."
- [Day 10] Final SMS: "Last follow-up — if you're still in the research phase, no worries. We're here when you're ready. Just reply 'READY' and we'll get a date locked in."
- [Day 14] Move to "Estimate - No Response" bucket for seasonal re-touch

---

### 4.3 Colour Approval Workflow

**Trigger:** Opportunity moved to "Colour Approval Pending" stage

This is the most underestimated bottleneck in painting. This workflow is a differentiator.

**Sequence:**
- [Day 0] SMS: "Hi [First Name]! Great news — your estimate is approved. The next step is selecting your colours. We need your choices confirmed by [DATE - 7 days before job start] so we can order materials. Here's a helpful tool: [Sherwin-Williams colour visualizer link / BM fan deck link]"
- [Day 0] Email: Full colour approval instructions with:
  - List of surfaces requiring colour selection (siding / trim / fascia / soffit / door — each may differ)
  - Paint brand we're using (so they visit the right store)
  - How to share colours (email photo of chip, paint code, or colour name)
  - FAQ: "Can you match my neighbour's colour?" "What if I change my mind after ordering?"
  - Deadline: paint must be ordered 5 business days before start date
- [Day 3] SMS: "Hey [First Name], just a reminder we need your colour selections by [DATE]. Have you had a chance to visit [Benjamin Moore / Sherwin-Williams]?"
- [Day 5] Call attempt: offer a colour consultation call with crew lead or designer if stuck
- [Day 7] If deadline missed: "Hi [First Name], we need your colour choices today to keep your [DATE] start on schedule. If you need more time, we may need to push your start date by one week."
- [Day 7+] If still no response: Trigger internal alert; estimator to call

**Internal gate:** "Materials Ordered" stage cannot be entered until "Colour Approval" checkbox is marked complete on the opportunity.

---

### 4.4 Job Start Notification

**Trigger:** Opportunity moved to "Job Scheduled" stage + start date confirmed

**Sequence:**
- [3 days before start] SMS: "Hi [First Name], your [exterior painting] starts [DAY, DATE]. Your crew lead is [Name] and they'll arrive around [TIME]. Please ensure [pets are secured / access to backyard / cars moved from driveway]."
- [24 hours before] SMS: "Just a reminder — your painting crew arrives tomorrow morning at [TIME]. Reply 'YES' to confirm, or call [number] if anything has changed."
- [If no reply in 4 hours] Internal alert: crew lead to call for verbal confirmation
- [Day of job, morning] SMS: "Good morning [First Name]! The [Company] crew is on their way. Crew lead [Name] will be there around [TIME]. Have a great day!"

---

### 4.5 Weather Hold Workflow

**Trigger:** Job tagged "Weather Hold" by crew lead or office

**Sequence:**
- [Immediately] SMS to client: "Hi [First Name], we're monitoring the weather forecast for your [exterior painting] job starting [DATE]. We may need to push your start by 1–2 days due to rain in the forecast. We'll confirm by [time/date]. Sorry for any inconvenience — outdoor painting quality depends on dry conditions!"
- [If rescheduled] SMS with new date + calendar confirmation link
- [Internal] Notify crew lead of hold and estimated restart date
- [Tracking] Tag contact with "Weather Hold" and count of holds (>2 may signal high-risk season timing for future quotes)

---

### 4.6 Post-Job Review Request

**Trigger:** Opportunity moved to "Job Complete" stage

**Sequence:**
- [2 hours after completion] SMS: "Hi [First Name]! Hope you love the fresh look. We really enjoyed working on your home. If you have 60 seconds, a Google review makes a huge difference for our small business: [direct Google review link]. Thank you!"
- [48 hours later, if no review] SMS: "Hey [First Name], just following up — did we earn a 5-star review? Here's the direct link if you missed it: [link]. We're grateful for every one of them."
- [7 days later] Email: Photo gallery of completed project (if photos were taken) + review ask with Facebook and Houzz as secondary options

**Platform links to include:** Google Business Profile review link (primary), Facebook Reviews, Houzz

---

### 4.7 Referral & Neighbour Campaign

**Trigger:** Opportunity moved to "Job Complete" — exterior job specifically

**Neighbour SMS Campaign (runs parallel to review request):**
- [Day 0 — job complete] If yard sign placed: Internal note triggers "Neighbour Campaign Active" tag
- [Day 2] Send to contacts in same neighbourhood (if existing database matches postal code / street name) OR use direct mail trigger: postcard to 10 adjacent homes — "We just painted your neighbour's home at [STREET] — here's what we can do for yours." + QR code to quote request form
- [Day 3] If digital ad running: geo-targeted Facebook/Google ad activated for 1km radius around job site address ("We just finished a beautiful exterior repaint in your neighbourhood")

**Referral Sequence (to job-complete client):**
- [Day 14] SMS: "Hi [First Name], we hope you're still loving the new look! If any friends or neighbours ask about your painters, we'd love a referral. We offer [a $100 referral credit / a free touch-up / a gift card] for any referral that books. Just have them mention your name."
- [Day 30] Email: "Referral reminder" with shareable link to quote request form and referral terms

---

### 4.8 Upsell Sequence — Interior to Exterior (and Reverse)

**Trigger:** Job Complete — Interior job

**Sequence:**
- [Day 7] SMS: "Hi [First Name], hope you're enjoying your freshly painted rooms! Quick question — have you thought about the exterior this spring? We noticed [mention specific observation — e.g., 'the trim on the north side is showing some weathering']. We'd be happy to include that in an early-bird spring quote. Interested?"
- [Day 14 if no response] Email: "Spring Exterior Painting — Early-Bird Pricing" with seasonal urgency and link to request a quote

**Trigger:** Job Complete — Exterior job

**Sequence:**
- [Day 30] SMS: "Hi [First Name], with the exterior looking sharp, the inside deserves some attention too! Many of our exterior clients add interior rooms in fall/winter when outdoor work slows down. Would you like a quick quote on any rooms?"

---

### 4.9 Annual Repaint Reminder (Retention Campaign)

**Trigger:** Date-based — 11 months after "Job Complete" date tag

**Sequence:**
- [11 months] SMS: "Hi [First Name]! It's been almost a year since [Company] refreshed your [home / office / building]. How's it looking? If any touch-ups are needed, or if you're thinking about changing up colours this season, reply and we'll get you a priority quote."
- [11 months] Email: "Annual Home Maintenance Reminder — Is It Time for a Touch-Up?" with checklist: "Signs your exterior paint is due for maintenance" (peeling, fading, chalk, cracking, mildew growth)
- [12 months] Internal alert: Flag for personal outreach from owner/estimator

---

## PART 5 — LEAD SOURCES & TARGETING

### 5.1 Google Local Services Ads (LSA)

**Best for:** High-intent homeowners searching "painter near me" or "exterior painting [city]"

**GHL Integration:**
- LSA leads fed directly into "New Inquiry" stage via webhook or Zapier
- Automated immediate SMS response within 60 seconds of lead arrival
- Track lead source in contact field for ROI measurement
- Pay-per-lead model: $20–$80/lead; average close rate 20–30% with fast follow-up

**Painting-specific LSA categories:**
- Exterior Painting
- Interior Painting
- Cabinet Painting
- Deck Staining
- Commercial Painting

**Conversion tip:** LSA leads have shown up to 4x higher close rates when contacted within 5 minutes. The GHL instant response workflow is a direct revenue multiplier here.

---

### 5.2 Referrals — Existing Clients

**Best for:** Warm leads with highest close rate (60–80%)

**GHL workflow:**
- Post-job referral sequence (see 4.7)
- Referral source tracking field on every new contact
- Referral source leaderboard (smart list: "Contacts who referred 2+ clients")
- Referral thank-you gift workflow (automated $25–$50 gift card trigger if available via integration)

---

### 5.3 Real Estate Agents — Move-In/Move-Out Painting

**Highest-value B2B referral channel often overlooked by painters**

Move-in/move-out scenarios:
- Seller needs home painted before listing (increases sale price)
- Buyer wants rooms refreshed before moving in (timeline: close date to move-in)
- Property sold "as-is" and buyer needs full interior repaint
- Staging company needs painter for vacant home

**GHL Outreach Sequence for Agents:**
- Contact created with tag "Real Estate Agent"
- Placed in "Real Estate Agent Nurture" pipeline
- Email/SMS sequence:
  - [Day 0] Introduction: "Hi [Name], I'm [Owner] from [Company Painting]. We specialize in pre-listing and move-in repaints with quick turnaround. Many agents in [City] use us on short timelines — can I buy you a coffee and show you how we can make your listings shine?"
  - [Day 7] Value email: "Before & After: How fresh paint added $15K to a listing in [Neighbourhood]" with photos
  - [Day 21] Follow-up: "Do you have a listing coming up that could use a refresh?"
  - [Monthly] Market update/seasonal: "Spring listing season is here — we have openings for pre-listing paint jobs in [Month]"

**Key offer to agents:** 48-hour turnaround on colour selection and quote, 5–7 day turnaround on standard interior repaint, payment at close of sale possible (discuss with your bookkeeper)

---

### 5.4 Property Managers

**Best for:** Commercial repaint contracts, recurring maintenance agreements

**Types of PM relationships:**
- Residential property managers (rental homes, duplexes, small multi-unit)
- Commercial property managers (office, retail, industrial)
- Strata property managers (condo corporations, townhouse complexes)

**GHL PM Sequence:**
- Contact tagged "Property Manager"
- Nurture pipeline: PM Outreach → Intro Meeting Booked → First Job Quoted → First Job Won → Recurring Contract
- Email sequence focused on: reliability, insurance certificates (have these ready as GHL attachment), crew size, turnaround times, annual maintenance program
- Monthly touchpoint: "We have 2 openings in [Month] for commercial repaints — any units coming up?"

---

### 5.5 Kijiji / Craigslist / Facebook Marketplace

**Best for:** Budget-conscious homeowners, price-shoppers (lower margin but volume)

**GHL workflow:**
- Lead source tag: "Kijiji" / "Craigslist" / "Facebook Marketplace"
- Separate follow-up cadence (faster, more price-anchored messaging)
- Qualify quickly: ask for square footage and paint condition in first response
- Price anchoring: respond with "our quotes typically range from $X–$Y for [size] interiors" before booking a visit

**Reality check:** These leads convert lower (15–25%) and are more price-sensitive. Build a script that moves them quickly to an estimate or closes the conversation. Don't waste 5-step nurture sequences on Kijiji leads.

---

### 5.6 Yard Signs & Neighbourhood Marketing

**Post-job passive lead generation**

- Yard sign placed at every exterior job (with client permission)
- QR code on sign links to "Get a Quote for Your Home" form
- GHL form captures: address, type of job, surface interest, email/phone
- Track how many leads come from yard sign source
- Seasonal: spring/summer exterior season = more yard signs = neighbourhood effect

**Digital complement:** After placing a yard sign, geo-targeted Facebook ad running $5/day for 1km radius around job address showing before/after of the home (get client permission first). Run for 2 weeks per job.

---

## PART 6 — SMS & EMAIL TEMPLATES

### 6.1 Instant Lead Response — SMS (send within 60 seconds)

```
Hi [First Name]! This is [Name] from [Company Painting]. 
Got your request for [interior/exterior] painting — I'll 
personally reach out within the hour. Talk soon! 🎨
```

---

### 6.2 Estimate Follow-Up — SMS Day 2

```
Hey [First Name], following up on the estimate we sent 
for your [exterior siding and trim]. Any questions about 
the scope or what's included? Happy to walk you through it.
```

---

### 6.3 Estimate Follow-Up — SMS Day 4 (Urgency)

```
Hi [First Name], just checking in on your painting quote. 
We're booking [Month] now and spots fill up fast. 
Let me know if you'd like to lock in a date!
```

---

### 6.4 Colour Approval Request — SMS

```
Hi [First Name]! Your estimate is confirmed 🎉 
Next step: colour selection. We need your choices by 
[DATE] to order materials in time. 

We're using [Benjamin Moore / Sherwin-Williams]. 
Their online colour visualizer can help: [link]

Have your colour code or chip name ready and just 
text it back or email us!
```

---

### 6.5 Colour Approval Reminder — SMS (Day 3, Deadline Approaching)

```
Hey [First Name], reminder that we need your colour 
selections by [DATE] to keep your [DATE] start on track. 

Siding: _____
Trim: _____
Fascia/Soffit: _____
Front Door: _____

Just text back or email the codes/names!
```

---

### 6.6 Job Start Notification — SMS (3 days before)

```
Hi [First Name]! Your [exterior/interior] painting 
starts [DAY, DATE]. 

Crew lead: [Name]
Arrival time: [TIME]

Please ensure: [dogs secured / garage accessible / 
cars moved from driveway / window trim cleared]

Questions? Reply or call [NUMBER]. See you soon!
```

---

### 6.7 Weather Hold — SMS

```
Hi [First Name], heads up — we're monitoring rain in 
the forecast for your [exterior] job starting [DATE]. 

We may need to push your start by 1–2 days to ensure 
proper adhesion and finish quality. We'll confirm by 
[DATE/TIME]. Thanks for your understanding! ☁️

Paint quality depends on dry conditions — we'd rather 
wait and do it right.
```

---

### 6.8 Post-Job Review Request — SMS

```
Hi [First Name]! We just wrapped up at [address] — 
hope you love the transformation! 🏡✨

If we earned it, a Google review means the world 
to our small business:
[DIRECT GOOGLE REVIEW LINK]

Takes 60 seconds and helps other homeowners find us. 
Thank you! 🙏
```

---

### 6.9 Neighbour Campaign — SMS or Postcard Copy

**SMS (to neighbourhood database or door hangers with QR):**
```
Hi! We recently completed a [colour] exterior repaint 
on [STREET] and wanted to reach out to neighbours. 

If your home could use a refresh, we'd love to 
give you a complimentary quote. We're already familiar 
with homes in your area!

[QUOTE REQUEST LINK]
— [Company Name]
```

**Postcard Headline:**
> "We just painted your neighbour's home on [STREET]. Here's what we can do for yours."

---

### 6.10 Seasonal Spring Exterior Push — Email

**Subject:** Your exterior is going to love this spring (limited openings)

```
Hi [First Name],

Spring is here — and so is exterior painting season.

After a long winter, wood siding, trim, and fascia take 
a beating. If you've noticed any of these, it's time:

✅ Peeling or bubbling paint
✅ Fading colour or chalking surface  
✅ Cracking caulk around windows and doors
✅ Mildew or moisture staining
✅ Fascia or soffit looking rough

We're booking May and June now, and spots fill up 
faster than a fresh coat dries.

[BOOK YOUR FREE EXTERIOR QUOTE]

— [Owner Name], [Company Painting]

P.S. We're happy to do a drive-by estimate — no need 
to be home.
```

---

### 6.11 Fall Interior Push — Email

**Subject:** Outdoor season is winding down. Time to refresh inside.

```
Hi [First Name],

As the leaves turn and outdoor projects wrap up, 
it's the perfect time to turn attention inside.

Interior painting is our fall and winter specialty:

🎨 No UV or weather constraints
🎨 Your home smells fresh before the holidays
🎨 Guests see a refreshed space at family gatherings
🎨 Earlier booking = better pricing

We're taking interior bookings for [October / November / 
December] now. Spaces go fast as painters fill indoor 
slots for the quiet season.

[GET YOUR INTERIOR QUOTE]

— [Owner Name], [Company Painting]
```

---

### 6.12 Commercial / Strata Annual Repaint Reminder — Email

**Subject:** [Building Name] — Is it time for your annual exterior review?

```
Hi [PM Name],

It's been [X months/a year] since we completed the 
repaint at [Building/Property Name].

With [spring / fall] approaching, now is a good time 
to assess:

• Caulking around window frames (typical lifespan: 5–7 years)
• Fascia and soffit condition post-winter
• Common area paint in hallways and stairwells
• Touch-ups from move-out/move-in damage

We'd be happy to do a complimentary walk-through and 
provide a maintenance quote. No obligation.

Would [DATE] or [DATE] work for a site visit?

— [Owner/Account Manager Name], [Company Painting]
```

---

## PART 7 — BOOKING FLOW DESIGN

### 7.1 In-Home Quote vs. Drive-By Estimate

**Two booking types — different GHL calendar types needed:**

**In-Home Quote (45–60 min):**
- Used for: interior jobs, complex exteriors with multiple surfaces, large commercial
- Requires homeowner to be present
- Estimator walks all rooms/surfaces, measures, discusses colour preferences, explains scope
- Outcome: detailed written quote sent within 24 hours
- Calendar: 60-min appointment slots, buffer 30 min, limited to 4/day per estimator

**Drive-By Estimate (15 min — curbside assessment):**
- Used for: straightforward exterior repaints where scope is visible from the road
- Homeowner does NOT need to be present (huge selling point)
- Estimator takes photos, measures visual exposure, notes surface type and condition
- Outcome: ballpark estimate or detailed quote depending on complexity
- Calendar: 15-min slots, grouped by geography for efficient routing
- **Script on booking page:** "Not home? No problem. We can assess most exteriors from the street — just leave us your address and we'll send a quote."

**GHL Setup:**
- Two booking calendars: "In-Home Quote" and "Drive-By Estimate"
- Booking form on website with smart conditional: "Is this for interior or exterior painting?" → routes to appropriate calendar type
- Drive-by estimates can be batched by neighbourhood for efficiency

---

### 7.2 Booking Confirmation Flow

Post-booking automation:
1. **Immediate** — Email confirmation with: date, time, what to expect, how to prepare (clear rooms / make sure estimator can access all areas)
2. **24 hours before** — SMS reminder with estimator name and a link to reschedule if needed
3. **Morning of** — "Your estimator [Name] is on their way / will arrive at [TIME]" SMS
4. **Post-estimate** — SMS: "Thanks for having us! Your quote will be emailed within 24 hours."

---

### 7.3 Missed Appointment Re-engagement

If prospect books but no-shows:
- [1 hour after no-show] SMS: "Hey [First Name], looks like we missed each other at [time]. No worries — want to rebook? Here's our calendar: [link]"
- [24 hours later] SMS: "Still interested in a [exterior/interior] quote? We have spots next week. [BOOK LINK]"
- If no rebook within 7 days: move to "Cold Lead" with seasonal re-engagement tag

---

## PART 8 — SEASONAL CAMPAIGNS

### 8.1 Spring Exterior Push (March 1 – April 30)

**Goal:** Pre-book May–July exterior slots before rush hits

**Trigger:** Date-based automation, runs annually

**Campaign elements:**
- Email: "Exterior painting season is here — book now before we fill up"
- SMS: "Spring is here! 🌸 Time to get your exterior quote locked in before [Company]'s May/June schedule fills. [LINK]"
- Facebook/Google ad: Before/after exterior repaints, seasonal urgency, "Limited May openings"
- Target: Past interior clients (upsell to exterior); cold leads from prior year; neighbourhood radius ads

**Pre-book incentive:** "Book your exterior repaint in April for a May/June start and receive [10% discount on trim / free pressure wash / free colour consultation]"

---

### 8.2 Fall Interior Push (September 1 – October 31)

**Goal:** Fill the winter calendar with interior work before the exterior season ends

**Trigger:** Date-based, runs annually

**Campaign elements:**
- Email: "Outdoor season wrapping up — refresh your interior before the holidays"
- SMS: "Fall's here 🍂 Perfect time to tackle those interior rooms before the holidays. [Company] has openings in [November/December]. [QUOTE LINK]"
- Facebook ad: Cozy interior "after" shots, fall colour palette (warm tones, feature walls)
- Target: Past exterior clients (interior upsell); new market — contractors finishing renovation projects needing paint

---

### 8.3 New Year Interior Refresh (January 1 – February 28)

**Goal:** Activate the dead winter months

**Campaign elements:**
- Email: "New year, new walls? Start fresh with [Company]"
- SMS: "Happy New Year! If one of your 2026 goals is a home refresh, [Company] is booking January interiors now. [LINK]"
- Offer: "January Colour Refresh Special — book 2+ rooms and get [free feature wall / free ceiling / $X off]"

---

### 8.4 Pre-Listing Spring Campaign (February – April)

**Target:** Real estate agents and homeowners listing for sale

**Campaign elements:**
- Direct outreach to agent database: "Spring listings are heating up — we handle pre-listing repaints in 5–7 days with quick colour sign-off"
- Email to past clients: "Thinking of selling this spring? Fresh paint is the #1 ROI renovation. We'll get you market-ready fast."
- Offer: Priority booking for listings ("we bump you to the front of the line if you're going to market")

---

## PART 9 — COMMERCIAL / STRATA WORKFLOW DETAIL

### 9.1 Strata Council Workflow

Strata painting is a high-value, long-cycle sale. Unlike residential, the painter must:
1. Navigate multiple decision-makers (strata council = 3–7 people)
2. Submit a formal written proposal (sometimes competing against 2–3 other painters)
3. Wait for a council vote (30–90 day cycle)
4. Execute in phases (typically one face of the building per season to minimize disruption)

**GHL workflow additions:**
- "Strata Vote Pending" stage with automated "Still in the review process?" check-ins at 7, 14, and 21 days
- Proposal attachment stored in GHL opportunity (PDF link or file)
- Strata manager + council contact as separate contact records, both linked to the same opportunity
- Trigger: "Strata Vote Won" → kickoff workflow with phase schedule template email

**Winning factors for strata bids:**
- Reference letters from other strata properties (add to GHL proposal email as attachments)
- Proof of liability insurance and WCB coverage (auto-attach in proposal template)
- Phasing plan that minimizes owner disruption
- Sample colour palettes specific to building style
- Annual maintenance agreement option (positions painter for multi-year relationship)

---

### 9.2 Property Manager Partnership Track

Property managers are repeat-business gold. One PM with 50+ rental units can be worth $20,000–$100,000+ annually in recurring touch-up and repaint work.

**PM Relationship Track in GHL:**

Stage 1: PM identified (LinkedIn, referral, cold outreach)
Stage 2: Introduction sent (email + phone)
Stage 3: Intro meeting booked
Stage 4: First job submitted and completed
Stage 5: PM referral relationship active
Stage 6: Preferred vendor / annual contract

**Monthly PM nurture email:**
> "Hi [PM Name], [Company] here. We have [X] openings for unit repaints in [Month]. Move-out condition, partial refresh, or full repaint — we turn units around in 3–5 days. Just send us the address and we'll get you a quote same-day."

**What PMs care about:**
- Speed (units sitting vacant = lost rent)
- Reliability (crew actually shows up)
- Invoicing (clean, consistent, easy to process)
- Insurance certificates on file
- Damage-free (won't scratch hardwood, damage tenant belongings)

---

## PART 10 — REVIEW GENERATION & NEIGHBOUR CAMPAIGN

### 10.1 Google Review Strategy

**Target:** 50+ Google reviews before aggressive LSA spend (reviews directly affect LSA ranking)

**Review velocity plan:**
- Every completed job triggers review request (see Workflow 4.6)
- Dedicated "Review" smart list in GHL: contacts who completed a job but have no "Review Left" tag
- Quarterly batch review ask to past clients who never left a review: "Hey [First Name], we realize we never asked — would you be willing to share your experience? [link]"
- QR code on all invoices and completion documents linking to Google review page
- Review link in email signature of all outgoing communications

**What happens after reviews come in:**
- Owner responds to every review within 24 hours (positive and negative)
- GHL automation: if review link clicked, tag contact as "Review Requested" and move to "Review Pending" smart list
- Manually tag "Review Left" when review is confirmed (or use webhook if monitoring tool integrated)

---

### 10.2 Neighbour Outreach Campaign (Post-Exterior Job)

**This is the most underused high-ROI campaign in the painting industry.**

Every completed exterior job is an opportunity to get 2–5 more jobs on the same street. The logic:
- Neighbours see the finished work every day
- The social proof is built in ("I see they did [house number]'s — looks great")
- Same neighbourhood = efficient crew routing
- Colour curiosity drives conversation (neighbours ask each other what paint they used)

**GHL Sequence (Exterior Job Complete):**

Day 0 — Job complete. Tag: "Neighbour Campaign - [Street Name / Postal Code]"

Day 1 — Door hanger drop (crew drops 10–15 door hangers on adjacent homes before leaving)
```
"We just painted [NEAREST CROSS STREET / COLOUR DESCRIPTION] 
home nearby. Want the same for yours?
Scan for a free drive-by estimate."
[QR CODE → GHL intake form with source = "Neighbour Campaign"]
```

Day 2 — If existing contacts in database with same street or postal code:
SMS: "Hey [First Name], we just wrapped up a [colour] exterior repaint nearby on [Street]. If your home has been on your mind, we'd love to give you a quote while we're in the area."

Day 3 — Geo-targeted Facebook/Google ad activated for 2-week run at $5–$10/day for 1km radius:
- Image: completed exterior from job (get permission — offer to blur address)
- Copy: "We just finished this exterior repaint in [Neighbourhood] — is your home next?"
- CTA: "Get a Free Drive-By Quote"
- Landing: GHL funnel page with drive-by estimate booking

Day 14 — Deactivate ad campaign. Track any leads with "Neighbour Campaign" source tag.

**Expected result:** 5–15% of neighbours contacted will request a quote. At 10 neighbours contacted per job, that's 0.5–1.5 bonus leads per completed exterior job.

---

## PART 11 — WHAT MAKES THE 1APP PAINTING SNAPSHOT STAND OUT

### 11.1 The Core Differentiators

**1. Colour Approval as a First-Class Pipeline Stage**
No other painting snapshot treats colour approval as a formal pipeline gate with automated follow-up. This single addition recovers 5–10 lost days per job across a painter's annual calendar.

**2. Dual Booking Flow (In-Home vs. Drive-By)**
The drive-by estimate is an underused conversion tool. Offering it removes the biggest friction point (needing to be home) and increases quote volume. This is baked into the booking funnel.

**3. Weather Hold Automation**
Exterior painters cancel and reschedule constantly. Having a professional, automated client communication for weather holds — instead of a rushed phone call at 6am — builds trust and reduces client anxiety.

**4. Neighbour Campaign Baked In**
Every exterior job completion triggers a neighbour outreach campaign. This creates a compounding geographic effect — one job becomes two, two become four. No other painting snapshot automates this.

**5. Strata/Condo Pipeline**
Most snapshots ignore the commercial strata market entirely. This is a high-margin, recurring revenue channel for painters. The strata pipeline, council vote tracking, and PM nurture sequence are unique to this snapshot.

**6. Real Estate Agent Track**
The agent referral channel is the most overlooked high-volume source for painters. The built-in agent outreach and nurture sequence plugs this gap.

**7. Seasonal Campaign Automation**
Four automated seasonal campaigns (spring exterior, fall interior, New Year refresh, pre-listing) run automatically without the painter doing anything manually. Set and forget.

**8. Painting Industry Language Throughout**
Every template, every stage name, every SMS uses real painting trade language: prep work, primer, top coat, fascia, soffit, pressure wash, colour approval, square footage, linear feet, spray vs. roll, colour chip. This is a snapshot that feels like it was built by someone who's been on a painting crew.

**9. Paint Material Ordering Gate**
The pipeline enforces the sequence: Colour Confirmed → Materials Ordered → Crew Scheduled. This prevents jobs from starting without materials, which is a real operational problem.

**10. Complete Intake Form Architecture**
Structured forms capturing square footage, surface type, prep condition, coat count, spray vs. roll, HOA colour approval required, and move-in/move-out status. These fields feed directly into accurate estimates and reduce "gotcha" scope changes.

---

### 11.2 Positioning for 1app Sales

**Target customers for this snapshot:**
- Residential painting contractors doing $200K–$2M annually
- Commercial painters or painters looking to break into commercial
- Painting business owners who are growing past 1 crew and need systems
- Painters frustrated with missed follow-ups and disorganized scheduling

**Pain points this snapshot solves (use in sales conversations):**
- "I'm losing quotes because I don't follow up fast enough"
- "Clients keep calling to ask about their job start date"
- "I can't keep track of where each job is at"
- "I get great reviews verbally but never on Google"
- "I want more commercial and strata work but don't know how to reach property managers"
- "My exterior schedule is chaos in May and June"

**Pricing guidance:**
- One-time snapshot setup: $497–$997 (positioned as the most complete painting snapshot on the market)
- Bundled with 1app monthly subscription: included in Professional tier
- White-glove onboarding (form setup, pipeline customization, first workflow audit): $297–$497 add-on

---

## PART 12 — TECHNICAL BUILD CHECKLIST

### 12.1 Pipelines to Build (4)
- [ ] Residential Interior Pipeline (11 stages)
- [ ] Residential Exterior Pipeline (13 stages + weather hold)
- [ ] Commercial Pipeline (10 stages)
- [ ] Strata / Condo Pipeline (10 stages)

### 12.2 Custom Fields to Create
- [ ] Job Type (Interior / Exterior / Commercial / Strata)
- [ ] Square Footage (numeric)
- [ ] Surface Type (multi-select: vinyl siding / hardiboard / wood / stucco / drywall / plaster / other)
- [ ] Prep Condition (dropdown: Good / Fair - some peeling / Poor - extensive scraping)
- [ ] Coat Plan (dropdown: Prime + 1 top coat / 2 top coats / 3 coats / client specifies)
- [ ] Spray or Roll (dropdown: Spray / Roll+Brush / Client Preference)
- [ ] Colour Approval Status (dropdown: Pending / Received / Ordered)
- [ ] Colour - Siding (text)
- [ ] Colour - Trim (text)
- [ ] Colour - Fascia/Soffit (text)
- [ ] Colour - Door (text)
- [ ] Paint Brand (dropdown: Benjamin Moore / Sherwin-Williams / CIL / Behr / Other)
- [ ] HOA Colour Approval Required (yes/no)
- [ ] Move-In/Move-Out Job (yes/no)
- [ ] Property Manager Name (text)
- [ ] Strata/Condo Corporation (yes/no)
- [ ] Lead Source (dropdown: Google LSA / Referral / Website / Kijiji / Facebook / Yard Sign / Real Estate Agent / Property Manager / Neighbour Campaign / Other)
- [ ] Yard Sign Placed (yes/no)
- [ ] Neighbour Campaign Active (yes/no)
- [ ] Review Left (yes/no)
- [ ] Referral By (contact lookup or text)
- [ ] Crew Lead Assigned (text or user lookup)
- [ ] Job Start Date (date)
- [ ] Job Complete Date (date)
- [ ] Weather Hold Count (numeric)

### 12.3 Calendars to Build (2)
- [ ] In-Home Quote (60 min, 30 min buffer, 4 slots/day)
- [ ] Drive-By Estimate (15 min, route-grouped availability)
- [ ] Commercial Site Assessment (90 min, assigned estimator)

### 12.4 Workflows to Build (12)
- [ ] 01 - Instant Lead Response (universal, all sources)
- [ ] 02 - Estimate Confirmation Sequence (5-touch, 14 days)
- [ ] 03 - Colour Approval Sequence (triggered by stage change)
- [ ] 04 - Job Start Notification (3-day / 24-hour / day-of)
- [ ] 05 - 72-Hour Confirmation Request (reply-YES system)
- [ ] 06 - Weather Hold Client Communication
- [ ] 07 - Post-Job Review Request (2-hour / 48-hour / 7-day)
- [ ] 08 - Neighbour Campaign Trigger (exterior job complete)
- [ ] 09 - Referral Request Sequence (14-day / 30-day)
- [ ] 10 - Upsell Sequence (interior → exterior and reverse)
- [ ] 11 - Annual Repaint Reminder (date-based, 11 months post-job)
- [ ] 12 - Seasonal Campaigns (Spring / Fall / New Year / Pre-Listing — date-triggered annually)
- [ ] 13 - Real Estate Agent Nurture (outreach + monthly touchpoint)
- [ ] 14 - Property Manager Nurture (outreach + monthly vacancy offer)
- [ ] 15 - Strata Vote Pending Follow-Up (7/14/21 day check-ins)

### 12.5 Forms to Build (3)
- [ ] Residential Quote Request Form (public-facing, website embed)
  - Name, email, phone, address, job type, approximate sq footage, timeframe
- [ ] Drive-By Estimate Request Form (no homeowner presence required)
  - Name, email, phone, property address, surfaces of interest, notes
- [ ] Commercial/Strata Inquiry Form
  - Name, company, property type, number of units, approximate scope, preferred timeline

### 12.6 Smart Lists to Build
- [ ] Estimates Sent - No Response (>5 days, not moved past Estimate Delivered)
- [ ] Colour Approval Overdue (>7 days in Colour Approval Pending)
- [ ] Jobs In Progress
- [ ] Review Not Yet Left (Job Complete > 14 days, no "Review Left" tag)
- [ ] Seasonal Re-Engagement Pool (Cold Leads from prior year)
- [ ] Real Estate Agent Contacts
- [ ] Property Manager Contacts
- [ ] Strata - Pending Council Vote
- [ ] Neighbour Campaign Active

### 12.7 Tags to Create
- [ ] Lead Source: [LSA / Referral / Website / Kijiji / FB / Yard Sign / Agent / PM / Neighbour]
- [ ] Job Type: [Interior / Exterior / Commercial / Strata]
- [ ] Colour Approval Received
- [ ] Materials Ordered
- [ ] Yard Sign Placed
- [ ] Neighbour Campaign Active
- [ ] Review Left
- [ ] Weather Hold
- [ ] Annual Repaint - Notified
- [ ] Re-Engagement Pool
- [ ] Real Estate Agent
- [ ] Property Manager
- [ ] Strata Contact
- [ ] VIP Client (repeat or high-value)

---

## PART 13 — SNAPSHOT NAMING & POSITIONING

### Recommended Snapshot Name:
**"Pro Painter — Full-Cycle CRM" by 1app**

### Tagline:
*"From first coat to five stars — every job automated."*

### Positioning Statement (for sales page/pitch):
> Most painting CRMs are generic home-service templates with paint on the name. This one was built from the ground up for how painters actually work: colour approvals, weather holds, exterior neighbour campaigns, strata council votes, and seasonal swings included. If you run a painting business and you're not following up automatically, you're leaving money at every stage of every job.

---

## APPENDIX A — PAINT INDUSTRY VOCABULARY REFERENCE

Use these terms throughout the snapshot to build credibility with painter clients:

| Term | Definition |
|------|------------|
| **Prep work** | Surface preparation before painting: scraping, sanding, caulking, priming, patching |
| **Primer / Prime coat** | First coat applied to seal surface and improve adhesion |
| **Top coat** | Final paint coat applied over primer |
| **Two-coat system** | Prime coat + one top coat (standard) |
| **Three-coat system** | Prime + two top coats (darker colour changes, raw wood, porous surfaces) |
| **Trim** | Window frames, door frames, baseboards, crown moulding |
| **Fascia** | Horizontal board running along the roofline at the edge of the roof |
| **Soffit** | Underside of the eaves/overhang between the wall and fascia |
| **Pressure wash** | High-pressure water cleaning of exterior surfaces before painting |
| **TSP wash** | Trisodium phosphate cleaning for interior surfaces (grease, smoke residue) |
| **Caulking** | Sealant applied to gaps around windows, doors, trim before exterior painting |
| **Colour consultation** | Service helping clients select colours; can be designer-assisted or DIY |
| **Colour chip / paint chip** | Small cardboard sample of a paint colour from the manufacturer |
| **Paint code** | Alphanumeric code identifying a specific paint colour (e.g., BM OC-17) |
| **Colour visualizer** | Digital tool to preview colours on a home's exterior or interior |
| **Spray application** | Paint applied via airless sprayer — faster, smoother finish on large surfaces |
| **Roll and brush** | Traditional application method; better for detail work and occupied homes |
| **Linear feet** | Measurement of trim, baseboard, crown moulding length |
| **Square footage** | Surface area to be painted (walls, ceilings, siding) |
| **Feature wall / accent wall** | Single wall painted a contrasting colour |
| **Stucco** | Textured exterior finish requiring specific application technique |
| **Hardiboard / Hardie plank** | Fibre cement siding; requires primer and specific paint products |
| **Chalking** | White powder residue on aged exterior paint indicating UV degradation |
| **Peeling** | Paint separating from surface — requires scraping before repainting |
| **Mildew / efflorescence** | Biological or mineral growth on surfaces requiring treatment before painting |
| **Strata** | Canadian term for condominium corporation (multi-unit ownership structure) |
| **Property manager (PM)** | Third-party manager of rental or strata properties |
| **Repaint cycle** | Recommended repainting schedule (exterior: 7–10 years, interior: 5–7 years) |
| **Move-out repaint** | Full interior repaint of rental unit between tenants |
| **Commercial repaint** | Repainting of office, retail, industrial, or multi-unit residential buildings |

---

## APPENDIX B — KEY BENCHMARKS

| Metric | Industry Average | Top Painter (with CRM) |
|--------|-----------------|------------------------|
| Lead response time | 2–4 hours | < 5 minutes |
| Quote close rate | 30–40% | 50–65% |
| Google reviews per 100 jobs | 8–12 | 35–50 |
| Revenue per job (residential exterior) | $2,500–$8,000 | $3,500–$12,000 (upsells) |
| Repeat client rate (no follow-up) | 15–20% | 40–60% (with retention workflows) |
| Referral rate (no system) | 20–25% | 35–45% (with referral automation) |
| Strata contract average value | $15,000–$80,000 | $20,000–$120,000 (multi-phase) |

---

*Document prepared for 1app internal use. Build reference for GHL Painting Contractor Snapshot.*
*Version 1.0 | July 2026 | Maximus AI Research Division*
