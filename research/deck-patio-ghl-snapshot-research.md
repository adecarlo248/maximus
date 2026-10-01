# GHL Snapshot Research: Deck & Patio Contractors
### 1APP Agency Build Document | Confidential Research

**Vertical:** Deck Building, Deck Repair, Deck Refinishing, Patio Installation, Pergola, Gazebo, Outdoor Living Spaces
**Document Type:** Snapshot Strategy & Build Specification
**Prepared For:** 1APP Technologies Inc.
**Date:** July 2026
**Status:** Ready for Build

---

## Executive Summary

The deck and patio vertical is a high-ticket, high-trust, visually-driven business with a long sales cycle, seasonal peaks, and strong referral and neighbour dynamics. Average project values range from $3,500 (repair/refinish) to $75,000+ (custom composite deck with pergola, outdoor kitchen, lighting). Contractors in this space are almost universally underserved by technology — they run on phone calls, paper quotes, and memory.

The gap is enormous. A purpose-built GHL snapshot that addresses the real pain points of this trade — permit complexity, design approval delays, multi-quote shoppers, material selection, seasonal urgency, and post-build neighbour campaigns — will win this vertical.

This document outlines the complete snapshot architecture for 1APP's deck and patio vertical offering.

---

## Section 1: Business Pain Points

### 1.1 Seasonal Revenue Concentration

Deck and patio work in Canada and the northern US is concentrated in a roughly 6-month window (April–October), with the peak quoting season being March through June. Contractors who fail to capture leads in spring often watch the entire season slip by. This creates:

- **Feast-or-famine revenue cycles** — huge summer, dead winter
- **Spring overwhelm** — too many leads, no system, leads fall through
- **Off-season dormancy** — no automated follow-up keeping the brand warm during winter planning season

**Snapshot opportunity:** Automated spring surge campaign triggered in February/March, off-season nurture keeping contractors top-of-mind during winter planning, and year-round refinishing/maintenance upsell for wood decks.

---

### 1.2 Permit Complexity and Approval Delays

Most deck builds over a certain height or square footage require:
- **Building permits** (structural)
- **Zoning approval** (setbacks, lot coverage)
- Sometimes **HOA approval**
- For ledger board attachment to the house: structural engineer review in some jurisdictions

Permit timelines vary from 2 weeks to 3+ months depending on the municipality. This creates:
- Long gaps between quote acceptance and construction start
- Customers losing confidence during the wait ("Did they forget about me?")
- Contractors losing clients to competitors who "start faster" (even if illegally without permits)

**Snapshot opportunity:** Automated permit status update workflow — proactive communication at milestones (permit submitted, permit approved, start date confirmed) that keeps the homeowner feeling managed, not forgotten.

---

### 1.3 Long Quote-to-Close Cycle

The average deck quote-to-close cycle is 14–45 days. Homeowners:
- Get 3–5 quotes minimum on large projects
- Research materials extensively (Trex vs. Fiberon vs. cedar vs. pressure treated)
- Show design ideas to spouses and family
- Wait for permits before committing
- Hesitate on composite vs. wood based on upfront cost

Without follow-up automation, most contractors lose leads simply because they stopped following up after the first call.

**Snapshot opportunity:** 14-day estimate follow-up sequence with value-add content (composite vs. wood lifespan calculator, material comparison, permit timeline FAQ) that keeps the contractor top-of-mind and educates the homeowner through the decision process.

---

### 1.4 Multi-Quote Shopping Behaviour

Homeowners getting deck quotes are almost always shopping multiple contractors. The first contractor to follow up consistently, provide detailed information, and demonstrate professionalism wins — not necessarily the cheapest.

Studies consistently show that the **first contractor to respond within 5 minutes** has a dramatically higher close rate. Most deck contractors respond within hours or days, if at all.

**Snapshot opportunity:** Speed-to-lead automation — immediate SMS response within 60 seconds of lead submission, instant AI voice agent callback, automated booking for design consultation within the same hour.

---

### 1.5 Design Approval Delays

Many deck projects require multiple rounds of design iteration:
- Homeowner changes dimensions after seeing initial design
- Spouse/partner has different vision
- City requires design changes for permit compliance
- Material costs come in over budget, requiring redesign

Each delay without communication = lost trust = cancelled project.

**Snapshot opportunity:** Design approval workflow with automated follow-up at 24h, 48h, and 72h after design submission, plus easy one-click approval via SMS link.

---

### 1.6 Material Lead Times

Composite decking (Trex, Fiberon, TimberTech) has had supply chain disruptions causing 4–8 week lead times. Pressure treated lumber fluctuates with market pricing. Cedar is seasonal. This affects:
- Project scheduling (contractor can't start without materials)
- Homeowner expectations
- Cash flow (deposit paid, materials not yet arrived)

**Snapshot opportunity:** Material status workflow — automated updates when materials are ordered, arrived at supplier, and staged for delivery. Homeowners who feel informed don't cancel.

---

### 1.7 No Follow-Up System

The most common reason deck contractors lose money: they give a quote, hear "let us think about it," and never follow up again. This is universal in the trade.

The homeowner who said "we're thinking about it" in May is still thinking about it in August — but they hired the contractor who texted them in June.

**Snapshot opportunity:** This is the core value prop. A multi-touchpoint follow-up sequence that works automatically is worth thousands per month in recovered revenue for a typical deck contractor.

---

## Section 2: Existing GHL Snapshots — Market Gap Analysis

### 2.1 What Currently Exists

As of 2025-2026, the GHL snapshot marketplace and third-party providers (ClawHub, Highlevel Marketplace, independent agencies) offer:

**Home Service / Contractor Snapshots (Generic):**
- Generic "home services contractor" snapshots designed for roofing, HVAC, plumbing
- Standard lead capture → appointment → close pipelines
- Basic missed call text back
- Not tailored to the visual/design nature of deck and outdoor living work
- No composite vs. wood upsell logic
- No seasonal campaign architecture
- No permit tracking
- No neighbour campaign

**Landscaping Snapshots:**
- Some landscaping-adjacent snapshots exist
- Focus on lawn care, tree service, and general outdoor maintenance
- Not built for high-ticket custom construction projects
- Missing design approval workflow, material selection, post-build review logic

**Custom Build / General Contractor Snapshots:**
- Heavy on project management
- Often overly complex for a small deck contractor team
- Missing visual portfolio integration, Houzz/Pinterest/Instagram lead source routing, and the homeowner education sequences specific to composite decking and outdoor living

### 2.2 What's Missing

The market has **zero purpose-built deck and patio snapshots** that include:

1. ✅ Composite vs. wood upsell workflow
2. ✅ Permit tracking communication sequence
3. ✅ Design consultation booking with portfolio showcase
4. ✅ Neighbour campaign (leveraging project visibility)
5. ✅ Seasonal spring push + fall before-winter urgency campaign
6. ✅ Annual wood deck refinishing/maintenance upsell
7. ✅ Material status update workflow
8. ✅ Segmented pipelines for new build vs. repair vs. refinishing vs. pergola vs. outdoor kitchen
9. ✅ Real estate agent / pre-sale referral pipeline
10. ✅ Industry-specific SMS/email templates with authentic contractor voice

**This is the opportunity.** The 1APP deck and patio snapshot fills a vacant niche with a highly specific, professional-grade build that no generic template can replicate.

---

## Section 3: Pipeline Architecture

### 3.1 Primary Pipelines

The snapshot includes **five distinct pipelines** corresponding to the major service categories of a full-service deck and patio contractor.

---

#### Pipeline 1: New Deck Build (Composite & Wood)

**Average Project Value:** $15,000–$75,000+

| Stage | Name | Description |
|-------|------|-------------|
| 1 | New Lead — Speed to Contact | Lead enters. Immediate SMS + AI voice call. Goal: book design consultation within same day. |
| 2 | Design Consultation Booked | Free on-site design consultation scheduled. Pre-consult info package sent. |
| 3 | Design Consultation Completed | Post-consult follow-up. Design concept in progress. |
| 4 | Design Submitted for Approval | Homeowner reviewing deck design/plans. Follow-up sequence active. |
| 5 | Design Approved — Quote Issued | Full quote/estimate sent. Estimate follow-up sequence active. |
| 6 | Permit Application Submitted | Permit filed with municipality. Homeowner notified with expected timeline. |
| 7 | Permit Approved — Deposit Collected | Permit in hand. Deposit invoice sent. Materials ordered. |
| 8 | Materials on Order | Material status update sequence active. |
| 9 | Build in Progress | Weekly check-in SMS to homeowner. |
| 10 | Project Complete — Final Invoice | Final walkthrough. Invoice sent. Review request triggered. |
| 11 | Post-Build Nurture | Review collected. Neighbour campaign launched. Annual maintenance upsell enrolled. |
| 12 | Closed Lost | Lost lead tagged with reason (price, timing, competitor, no response). Re-engagement campaign enrolled. |

---

#### Pipeline 2: Deck Repair & Board Replacement

**Average Project Value:** $800–$8,000

| Stage | Name | Description |
|-------|------|-------------|
| 1 | New Lead — Repair Request | Lead enters. Immediate contact. Same-day or next-day site visit offered. |
| 2 | Site Assessment Booked | Appointment confirmed. Pre-visit SMS with what to expect. |
| 3 | Site Assessment Completed | Assessment done. Quote being prepared. |
| 4 | Quote Issued | Quote sent. 3-touch follow-up sequence. |
| 5 | Repair Approved — Deposit | Job approved. Scheduling confirmed. |
| 6 | Repair Completed | Job done. Review requested. Upgrade to composite upsell offered. |
| 7 | Closed Lost | Re-engage in 30/60/90 days. |

---

#### Pipeline 3: Deck Refinishing & Staining

**Average Project Value:** $1,200–$6,000

| Stage | Name | Description |
|-------|------|-------------|
| 1 | New Lead | Lead enters. Immediate response. |
| 2 | Quote Requested / Site Visit | On-site estimate or photo quote offered. |
| 3 | Quote Issued | Quote sent. Spring/fall urgency language active if seasonal. |
| 4 | Approved — Scheduled | Job booked. Pre-work prep instructions sent (clear deck, patio furniture). |
| 5 | Work Completed | Before/after photos requested. Review triggered. |
| 6 | Annual Maintenance Enrolled | Enrolled in annual refinish reminder campaign. |

---

#### Pipeline 4: Pergola / Gazebo / Shade Structure

**Average Project Value:** $8,000–$35,000

| Stage | Name | Description |
|-------|------|-------------|
| 1 | New Lead | Immediate contact. Material options (cedar, composite, aluminum, vinyl) discussed. |
| 2 | Consultation Booked | Free design consultation scheduled. |
| 3 | Design Review | Pergola/gazebo design submitted. Approval follow-up sequence. |
| 4 | Quote Issued | Comprehensive quote with material options. |
| 5 | Permit (if required) | Permit filed. Status updates sent. |
| 6 | Job Complete — Review | Post-build review + neighbour campaign. |

---

#### Pipeline 5: Outdoor Kitchen / Outdoor Living Spaces

**Average Project Value:** $20,000–$150,000+

| Stage | Name | Description |
|-------|------|-------------|
| 1 | New Lead | High-value lead. Immediate personal outreach priority tag. |
| 2 | Premium Consultation Scheduled | In-depth design consultation with portfolio walk. |
| 3 | Design & Engineering Phase | Complex design phase. Multiple approval touchpoints. |
| 4 | Permitting & HOA | Multi-jurisdictional permit tracking. |
| 5 | Material Selection Approval | Customer approves materials (countertop, cabinetry, grilling station, lighting). |
| 6 | Build Phase — Phase Updates | Weekly project photos/updates to homeowner. |
| 7 | Project Complete | Final walkthrough, review, referral request, neighbour campaign. |

---

## Section 4: Workflow Architecture

### 4.1 Speed-to-Lead Workflow (All Pipelines)

**Name:** `DECK — Speed to Lead`
**Trigger:** New lead created (any source)
**Delay:** 0 minutes

```
Step 1 (0 min): SMS — "Hi [First Name], thanks for reaching out about your deck project! 
I'm [Contractor Name] from [Company]. I'm reviewing your request now and will 
call you within the next few minutes. — [Company Name]"

Step 2 (0 min): AI Voice Call — Attempt #1 (voicemail drops with callback instructions)

Step 3 (5 min): If no answer — SMS #2:
"Hey [First Name] — I just tried calling. I'd love to chat about your outdoor 
living project. What time works best for a quick call today? Or you can book 
directly here: [calendar link]"

Step 4 (1 hour): If no response — Email:
Subject: "Your [City] Deck Project — Let's Talk"
Body: portfolio showcase + booking link

Step 5 (24 hours): SMS #3:
"Still thinking about your deck? We're booking [Month] projects now — 
spots fill up fast once spring hits. Here's our portfolio: [link]"

Step 6 (72 hours): Final SMS + email:
"[First Name] — last reach out before I close your file. If you're still 
considering a deck or patio this season, here's our availability: [booking link]. 
No pressure either way — just don't want you to miss the season."
```

---

### 4.2 Design Consultation Confirmation & Reminder Workflow

**Name:** `DECK — Design Consultation Confirmation`
**Trigger:** Stage moves to "Design Consultation Booked"

```
Immediately: Email — Full confirmation with appointment details
+ "What to expect" (we'll walk your yard, discuss layout, sun patterns, 
traffic flow, ledger board attachment point, joist span, railing style)

-24 hours: SMS reminder:
"Reminder: Your free deck design consultation is tomorrow at [Time]. 
[Contractor Name] will be at [Address]. Have any inspiration photos ready 
(Houzz, Pinterest, or Instagram) — it helps us nail your vision. See you then!"

-2 hours: SMS:
"On my way shortly for your deck consultation at [Time]. 
Looking forward to seeing your space!"

Post-visit (2 hours after appointment): SMS:
"Great meeting you today, [First Name]! I'm putting together your 
design concept — you'll have it within [X] business days. 
Any questions in the meantime, text me here."
```

---

### 4.3 Estimate Follow-Up Workflow

**Name:** `DECK — Estimate Follow-Up Sequence`
**Trigger:** Stage moves to "Design Approved — Quote Issued"
**Duration:** 21 days

```
Day 0: Email — Estimate delivered with full project scope
+ breakdown by category (decking boards, framing, footings, 
railing system, stairs, fascia boards, lighting rough-in)
+ material spec sheet (composite vs. pressure treated comparison)
+ project timeline overview
+ FAQ: "What happens next"

Day 1: SMS:
"Hey [First Name] — just wanted to make sure the estimate came through okay. 
Any questions on the materials or scope? Happy to jump on a call anytime."

Day 3: Email — Value add:
Subject: "Composite vs. Pressure Treated — What's Right for You?"
(educational content on composite lifespan, warranty, maintenance costs, 
ROI on home value — positions contractor as expert, not salesperson)

Day 5: SMS:
"[First Name] — just checking in. We're still holding your preferred 
start date. Spring/summer slots are filling up — just give me the heads 
up when you're ready to move forward."

Day 10: SMS — social proof:
"Just finished this deck in [Neighbourhood Name] last week — 
thought you'd love to see it: [photo link]. 
Your project would have a similar scope. Still available if you want to go!"

Day 14: Email:
Subject: "Are you still interested in your deck project?"
Body: Simple, direct. "I want to make sure I hold time in our schedule 
for your project. Can you let me know if you're still moving forward, 
need more time, or went a different direction? No hard feelings — 
just helps me plan my season. — [Name]"

Day 21: SMS — final follow-up:
"[First Name] — I'll close your file after today since we haven't 
heard back. If the timing wasn't right, no worries — give me a call 
when you're ready. I'd love to build something great for you."

[If no response: Tag as "Cold — Re-engage Q1 Next Year" 
and enroll in winter planning campaign]
```

---

### 4.4 Permit Tracking Workflow

**Name:** `DECK — Permit Status Updates`
**Trigger:** Stage moves to "Permit Application Submitted"

```
Day 0: SMS:
"Great news — we've submitted your building permit to [Municipality]. 
Expected review time is approximately [X] weeks. 
I'll keep you updated at every step. No news is good news!"

Day 7: SMS:
"Week 1 update on your permit: Still in review at [Municipality]. 
These things take time — we're monitoring it daily. 
In the meantime, we're finalizing your materials and pre-staging. 
You'll be one of the first jobs we start once approval comes in."

Day 14: SMS (if permit still pending):
"Still waiting on your building permit — [Municipality] is running 
about [X] weeks right now, which is typical for the season. 
We haven't forgotten you — the moment it's approved, 
we'll be in contact within the hour to get your start date locked in."

[Permit Approved Trigger]:
SMS (immediate):
"GREAT NEWS! Your building permit has been approved! 🎉 
We're locking in your start date now. Expect a call from me 
within the next 2 hours to confirm your schedule."
```

---

### 4.5 Material Selection & Approval Workflow

**Name:** `DECK — Material Approval`
**Trigger:** Material selection package sent to homeowner

```
Day 0: Email — Material selection package:
- Composite decking options: Trex Transcend, Fiberon Paramount, TimberTech AZEK
- Wood options: cedar, pressure treated Southern Yellow Pine
- Railing systems: glass panel, cable railing, aluminum balusters, wood balusters
- Colour boards and sample options
- Lead time per option (CRITICAL for scheduling)

Day 1: SMS:
"Hey [First Name], just wanted to make sure you got the material samples 
I sent over. The colour board really does make a difference — 
Trex Transcend in [colour] is our most popular right now. 
Any questions on lead times or pricing differences?"

Day 3: SMS (if not approved):
"Quick reminder — we need your material selection confirmed by [Date] 
to hold your build slot and order materials with enough lead time. 
Some composite options have 3-4 week lead times right now."

Day 5: Call + SMS:
"[First Name] — I want to make sure we don't lose your build spot. 
Can you confirm your material choice by end of day today? 
Trex, Fiberon, or cedar — even a ballpark helps us hold your date."
```

---

### 4.6 Post-Build Review Workflow

**Name:** `DECK — Post-Build Review & Referral`
**Trigger:** Stage moves to "Project Complete"

```
Day 0 (Build complete): SMS:
"[First Name] — your deck/patio is done! 🎉 
It was a pleasure working with you. 
Can we grab a few final photos for our portfolio? 
Also, we'd love it if you left us a quick Google review — 
it takes 60 seconds and helps us a lot: [Google Review Link]"

Day 1: Email:
Subject: "Your Care Guide for Your New [Composite/Wood] Deck"
Body: Professional post-build care guide
- Composite: annual wash, avoid rubber mats trapping moisture, avoid wire brush
- Pressure treated: annual inspection, stain/seal every 2-3 years, check joist hangers
- Cedar: seal within 30 days, annual maintenance staining
+ warranty information for Trex (25-year fade/stain), Fiberon (50-year), etc.

Day 3: SMS:
"Hope you're enjoying your new [deck/patio/pergola]! 
Would you mind leaving us a Google review? 
We'd really appreciate it: [link]"

Day 7: SMS — referral request:
"[First Name] — we noticed your neighbours seem to be checking 
out your new deck! 😄 If any of them ask about it, 
we'd love the referral. We're offering a $250 referral credit 
for every neighbour you send our way this season."
```

---

### 4.7 Neighbour Campaign Workflow

**Name:** `DECK — Neighbour Campaign`
**Trigger:** Project marked complete in pipeline
**Trigger also:** Manual entry via "Neighbour Campaign" tag

```
Step 1: Door Hanger + Postcard (Manual task triggered):
[Contractor notified via GHL task to drop door hangers 
within a 5-house radius of completed project]
Door hanger copy: "We just built the deck at [nearby address]. 
Want to see what we can do for your backyard? 
Free design consultation: [QR code / booking link]"

Step 2 (automated): Facebook/Google Retargeting:
[Lead tag triggers ad audience update in geographic area of completed job]
Ad creative: before/after of completed deck
"We just finished this deck in YOUR neighbourhood. 
Want to see what we can do for yours? Free design consultation →"

Step 3: Neighbourhood-specific SMS/email campaign:
[If neighbour leads come in via "how did you hear about us" → neighbour referral]
"Hi [First Name] — [Neighbour Name] recommended us after we built 
their new composite deck on [Street Name]. 
We'd love to bring the same quality to your backyard. 
Book your free design consultation here: [link]"
```

---

### 4.8 Annual Wood Deck Refinishing Upsell

**Name:** `DECK — Annual Refinishing Reminder`
**Trigger:** Enrolled after wood deck project completed
**Fires:** Every year in early April

```
April 1 (Year 1, 2, 3...): SMS:
"Hey [First Name]! Spring is here — time for your annual deck inspection. 
Pressure treated and cedar decks need a fresh stain/seal every 1-3 years 
to prevent cracking, warping, and rot. 
Want us to come take a look? We're booking April/May slots now: [link]"

April 3: Email:
Subject: "Is Your Wood Deck Ready for Another Summer?"
Body: Educational content on wood deck maintenance
- Signs your deck needs refinishing (graying, raised grain, water not beading)
- Consequences of skipping (rot, structural damage, shortened lifespan)
- Our refinishing process (power wash, sand, stain, seal)
- Special offer for past customers: $X discount / priority booking

April 7: SMS (if no response):
"[First Name] — last reminder about spring deck maintenance. 
We have a few slots left in April before we go into build season. 
Want to lock one in? [link]"
```

---

### 4.9 Composite Upsell Workflow (From Repair/Refinishing Pipeline)

**Name:** `DECK — Composite Upgrade Pitch`
**Trigger:** Repair or refinishing job completed on wood deck

```
Post-project (Day 7): Email:
Subject: "Is It Time to Upgrade to Composite? (Honest Answer)"
Body:
"[First Name] — we just finished your deck repair/refinish, 
and it looks great. But I want to be straight with you: 
if your deck is more than 10 years old and pressure treated, 
you're going to keep spending money on it every couple of years.

Here's the math:
- Pressure treated deck: $X/year in maintenance x 15 years = $XX,XXX
- Composite deck (Trex, Fiberon): $0 maintenance, 25-50 year warranty, 
  adds more to home resale value

We can often apply what you've already paid toward a new composite build.
Want me to put together a quote to show you the comparison? 
No obligation — just the numbers so you can make an informed decision."

Day 14: SMS:
"[First Name] — did you get the composite upgrade info I sent? 
A lot of our clients who started with repairs ended up going composite 
and said it was the best decision they made. 
Happy to answer any questions: [phone/text]"
```

---

### 4.10 Seasonal Campaign — Spring Build Push

**Name:** `DECK — Spring Surge Campaign`
**Trigger:** Automated — fires February 1 each year to cold leads + past clients + no-decision prospects from prior year

```
February 1: Email blast + SMS:
Subject: "Spring Deck Season is Almost Here — Lock In Your Spot Now"
"[First Name] — We start booking our spring build calendar in February. 
Last year we were fully booked by April 15. 
If you've been thinking about a new deck, patio, or pergola for this summer, 
now is the time to secure your spot. 
Early bookings also lock in current pricing before material costs go up. 
Free design consultation: [link]"

February 15: SMS:
"Deck season spots filling fast. 
We're already 40% booked for April/May. 
Book your free consultation: [link]"

March 1: SMS:
"[First Name] — March is here. Time to get your deck done before summer. 
We can usually get permits filed, materials ordered, and build started 
within 6-8 weeks of signing. Want a May deck? 
Book now: [link]"

March 15: Email:
Subject: "Last Call for a May/June Deck Build"
Body: Urgency + social proof photos of recent builds + booking link
```

---

### 4.11 Seasonal Campaign — Fall Before-Winter Urgency

**Name:** `DECK — Fall Urgency Campaign`
**Trigger:** Automated — fires August 15 each year to open leads + unbooked prospects

```
August 15: Email:
Subject: "Get Your Deck Done Before the Snow Hits"
"[First Name] — summer isn't over yet. 
We have limited spots left in our September/October build calendar. 
A fall deck build means you're ready to enjoy it the minute next spring hits — 
and you lock in this year's pricing.
Here's our current availability: [link]"

September 1: SMS:
"[First Name] — last realistic window to start and finish a deck before winter. 
We have [X] spots left in September. Want one? [link]"

September 15: SMS:
"Weather window closing. 
Our last build slots of the season are almost gone. 
Contact us today if you want a deck ready for next spring: [phone/link]"
```

---

## Section 5: SMS & Email Templates

### 5.1 Speed-to-Lead SMS Templates

**SMS-SL-01: Immediate Response**
```
Hi [First Name]! Thanks for reaching out to [Company Name] 
about your deck/patio project. I'm reviewing your request now 
and will call you in the next few minutes. — [Name]
```

**SMS-SL-02: No Answer Follow-Up**
```
Hey [First Name] — I just tried calling. 
Still want to chat about your outdoor project. 
Best time to connect? Or book here: [link]
```

**SMS-SL-03: 24-Hour Follow-Up**
```
[First Name] — still thinking about your deck? 
Spring/summer spots are going fast. 
Here's our latest work: [portfolio link]. 
Happy to answer any questions!
```

---

### 5.2 Estimate Follow-Up SMS Templates

**SMS-EF-01: Day 1 Check-In**
```
Hey [First Name], just making sure the estimate arrived okay. 
Any questions on the materials or scope? 
Happy to walk you through it anytime — just text back.
```

**SMS-EF-02: Day 5 Urgency (Soft)**
```
[First Name] — still holding your preferred start date for now. 
Spring/summer slots fill up quick around here. 
Let me know when you're ready to move forward!
```

**SMS-EF-03: Social Proof Day 10**
```
Just finished this deck nearby — thought you'd love it: [photo/link]. 
Your project scope is very similar. 
Still available to build yours!
```

**SMS-EF-04: Day 14 Gut-Check**
```
[First Name] — last check-in before I have to open this slot to other clients. 
Are you still thinking about the project? No pressure either way — 
just want to make sure you don't lose your spot!
```

**SMS-EF-05: Day 21 Final**
```
[First Name] — closing your file today. 
If the timing wasn't right, no worries at all — 
give me a call whenever you're ready. 
Would love to build something great for you when the time comes.
```

---

### 5.3 Material Selection Templates

**SMS-MAT-01: Material Approval Reminder**
```
Hey [First Name] — just a reminder to confirm your material choice 
(Trex, Fiberon, cedar, or pressure treated). 
Need it by [Date] to hold your build slot and beat the lead times. 
Questions? Text me back!
```

**SMS-MAT-02: Lead Time Urgency**
```
[First Name] — heads up: composite decking has 3-4 week lead times right now. 
If you want an [Month] start, we need your material selection 
confirmed by end of this week. 
Which way are you leaning?
```

---

### 5.4 Seasonal Urgency Templates

**SMS-SPRING-01: February Push**
```
[First Name] — spring deck season is almost here! 
We're already booking April/May slots. 
Want to lock in your spot before they're gone? 
Free design consultation: [link]
```

**SMS-FALL-01: September Urgency**
```
[First Name] — last call for fall builds. 
A few spots left in September. 
Perfect time to get the deck done before winter! [link]
```

---

### 5.5 Review Request Templates

**SMS-REV-01: Immediate Post-Build**
```
[First Name] — your deck looks incredible! 
Would you mind leaving us a quick Google review? 
It really helps us out: [Google Review Link] 🙏
```

**SMS-REV-02: Day 3 Reminder**
```
Hey [First Name] — hope you're enjoying the new [deck/patio/pergola]! 
If you have 60 seconds, a Google review means the world to us: [link]
```

---

### 5.6 Referral / Neighbour Templates

**SMS-REF-01: Referral Ask**
```
[First Name] — if your neighbours ask about your deck, 
send them our way! We're offering a $250 referral credit 
for every project you refer us to this season. 
Thanks for being such a great client! 🙏
```

**SMS-NEIGH-01: Neighbour Outreach**
```
Hi [First Name] — we just finished the deck on [Nearby Street]. 
Noticed you might be in the neighbourhood! 
We'd love to give you a free design consultation. 
Portfolio: [link] | Book: [link]
```

---

## Section 6: Booking Flow Architecture

### 6.1 Calendar: Free Design Consultation / Site Assessment

**Calendar Name:** `Free Deck Design Consultation`
**Duration:** 60 minutes
**Location:** Client's property (service area)
**Buffer after:** 30 minutes (travel time)
**Max per day:** 3 consultations
**Booking window:** 2 days out to 4 weeks

**Pre-booking form fields:**
- First Name (required)
- Last Name (required)
- Email (required)
- Phone (required)
- Property address (required)
- Type of project (dropdown: New Deck Build / Deck Repair / Deck Refinishing / Pergola or Shade Structure / Patio Installation / Outdoor Kitchen / Not Sure Yet)
- Approximate square footage or yard size (dropdown: Under 200 sq ft / 200-400 sq ft / 400-600 sq ft / 600+ sq ft)
- Preferred decking material (dropdown: Composite - Trex/Fiberon/TimberTech / Cedar / Pressure Treated / Not Sure — Need Guidance)
- How did you hear about us? (dropdown: Google / Referral from Friend or Neighbour / Houzz / Instagram/Pinterest / Facebook / Door Hanger / Other)
- Any inspiration photos or ideas? (text field — optional)

**Confirmation message:**
```
"Thanks for booking your free deck design consultation with [Company Name]! 
[Contractor Name] will be at your property on [Date] at [Time].

To make the most of our consultation, feel free to:
• Gather any inspiration photos (Houzz, Pinterest, Instagram)
• Think about how you plan to use the space (dining, lounging, grilling, entertaining)
• Note any concerns about sun exposure, privacy, or neighbour sightlines

We're looking forward to helping you build your dream outdoor living space!

— [Company Name]
[Phone] | [Email] | [Website]"
```

---

### 6.2 Calendar: Quick Estimate Call (Phone/Virtual)

**Calendar Name:** `Free 20-Minute Estimate Call`
**Duration:** 20 minutes
**Format:** Phone or Zoom
**Purpose:** Qualify lead, gather project details, schedule site visit
**Booking window:** Same day to 2 weeks

---

## Section 7: Lead Source Tagging & Attribution

### 7.1 Custom Fields (Contact Level)

| Field Name | Type | Values |
|-----------|------|--------|
| Lead Source | Dropdown | Google LSA / Google Search Ad / Google Organic / Referral / Neighbour Campaign / Houzz / Instagram / Pinterest / Facebook / Door Hanger / Real Estate Agent / Other |
| Project Type | Dropdown | New Deck Build / Deck Repair / Deck Refinishing / Pergola / Patio / Outdoor Kitchen / Gazebo / Multi-Project |
| Material Preference | Dropdown | Composite (Trex) / Composite (Fiberon) / Composite (TimberTech) / Cedar / Pressure Treated / Not Decided |
| Project Size (sq ft) | Number | |
| Permit Required | Dropdown | Yes / No / Unknown |
| Permit Status | Dropdown | Not Submitted / Submitted / In Review / Approved / Rejected |
| Quote Value | Currency | |
| Quote Sent Date | Date | |
| Job Start Date | Date | |
| Job Completion Date | Date | |
| Review Requested | Checkbox | |
| Review Received | Checkbox | |
| Referral Given | Checkbox | |
| Neighbour Campaign Active | Checkbox | |
| Annual Maintenance Enrolled | Checkbox | |
| Composite Upsell Offered | Checkbox | |

---

### 7.2 Lead Source-Specific Workflows

**Google LSA Leads:**
- Highest intent — immediate voice call priority
- "You called Google for deck services in [City]" personalized SMS
- Tag: `GLS-LSA`

**Houzz Leads:**
- Design-focused homeowner — visual portfolio emphasis
- Send portfolio link in first SMS
- Tag: `Source-Houzz`

**Referral from Neighbour:**
- Warm lead — reference completed project
- "We just finished [Neighbour Name]'s deck on [Street] — [Neighbour] thought we might be a great fit for you"
- Tag: `Referral-Neighbour`

**Real Estate Agent Referral:**
- Pre-sale urgency — deck needs to look good for listing
- Expedited timeline messaging
- Agent gets automatic CC on all communication (if opted in)
- Tag: `Source-Realtor`

**Pinterest/Instagram Leads:**
- Aspirational buyer — high design interest
- Portfolio-heavy email sequence
- "Inspired by what you saw? Let us bring it to life in your backyard"
- Tag: `Source-Social-Visual`

---

## Section 8: Tags — Full Tag Library

### Lead Status Tags
- `New Lead`
- `Contacted - No Response`
- `Consultation Booked`
- `Consultation Completed`
- `Quote Issued`
- `Quote Follow-Up Active`
- `Closed Won`
- `Closed Lost - Price`
- `Closed Lost - Timing`
- `Closed Lost - Competitor`
- `Closed Lost - No Response`
- `Cold Lead - Re-engage`

### Project Type Tags
- `Project - New Deck Build`
- `Project - Repair`
- `Project - Refinishing`
- `Project - Pergola`
- `Project - Patio`
- `Project - Outdoor Kitchen`
- `Project - Gazebo`

### Material Tags
- `Material - Composite`
- `Material - Trex`
- `Material - Fiberon`
- `Material - TimberTech`
- `Material - Cedar`
- `Material - Pressure Treated`
- `Material - Undecided`

### Campaign Tags
- `Campaign - Spring Push Active`
- `Campaign - Fall Urgency Active`
- `Campaign - Neighbour Campaign Active`
- `Campaign - Annual Refinish Reminder`
- `Campaign - Composite Upsell`
- `Campaign - Review Requested`
- `Campaign - Referral Program`

### Permit Tags
- `Permit - Required`
- `Permit - Submitted`
- `Permit - Approved`
- `Permit - Rejected`

### Lifecycle Tags
- `Past Client - Wood Deck`
- `Past Client - Composite`
- `Past Client - Repair`
- `Past Client - Pergola`
- `Review Given - Google`
- `Referral Given`
- `Annual Maintenance Client`

---

## Section 9: Snapshot Differentiators — What Makes This Win

### 9.1 The 7 Differentiators No Generic Snapshot Has

**1. Material-Aware Upsell Logic**
The composite vs. wood upsell isn't just a marketing pitch — it's embedded into the CRM logic. After every wood repair or refinishing job, an automated sequence activates with the honest ROI math. This alone closes additional jobs.

**2. Permit Communication Sequence**
No other snapshot tracks permits. Deck contractors lose clients during the 4-8 week permit wait because they go silent. This snapshot keeps the homeowner engaged every week with proactive updates, dramatically reducing ghosting during permit wait periods.

**3. The Neighbour Campaign**
Decks are the most visible home improvement product. They sit in backyard spaces where entire neighbourhoods can see them. The neighbour campaign — combining automated door hanger tasks, geographic ad retargeting, and SMS outreach to referred neighbours — turns every completed deck into a lead-generation engine. One deck can generate 2-3 neighbour inquiries.

**4. Seasonal Campaign Architecture**
The spring push (February) and fall urgency (August/September) campaigns are pre-built and fire automatically every year. The contractor doesn't have to remember — it just happens. This alone is worth the monthly subscription.

**5. Annual Refinishing Reminder**
For every wood deck installed or repaired, the homeowner is automatically enrolled in an annual spring refinishing reminder. This creates a recurring revenue stream the contractor didn't have to think about.

**6. Real Estate Agent Pipeline**
Realtors who need decks refreshed before listing are a massive, underserved lead source for deck contractors. This snapshot includes a dedicated pipeline stage, agent-specific SMS/email templates, expedited timeline messaging, and a referral tracking system for agents.

**7. Industry Vocabulary**
Every template uses real industry language: ledger board, joist, beam, footing, railing, baluster, fascia board, picture frame border, composite, pressure treated, cedar, Trex, Fiberon, TimberTech. Homeowners and contractors recognize this as a company that knows their industry — not a generic CRM template.

---

### 9.2 Composite vs. Wood Upsell — The $15,000 Decision

This is the highest-margin differentiator in the snapshot. Here's why:

**The Math:**
- Pressure treated deck (400 sq ft): ~$12,000 installed
- Annual maintenance (stain, seal, minor repairs): ~$800/year
- Over 15 years: $12,000 + $12,000 maintenance = $24,000

- Composite deck (400 sq ft, Trex Transcend): ~$22,000 installed
- Annual maintenance: $0 (wash with soap and water)
- Over 15 years: $22,000
- Savings: $2,000 — plus no hassle, better aesthetics, 25-50 year warranty

The contractor who can present this math (automated, in the CRM workflow) sells more composite jobs. Composite = higher margin, lower service callbacks, happier long-term clients.

**The workflow:** After sending a repair or refinishing quote, an automated email titled *"Composite vs. Pressure Treated — What's Right for You? (Honest Answer)"* goes out 7 days post-job completion. It presents the math neutrally and invites a conversation. No hard sell — just the numbers.

---

## Section 10: Snapshot Technical Specifications

### 10.1 Required GHL Features

| Feature | Purpose |
|---------|---------|
| Pipelines (5) | Track each project type separately |
| Workflows (12+) | Automate all communication sequences |
| Calendar (2) | Design consultation + quick estimate call |
| Custom Fields (20+) | Track project details, permit status, material selection |
| Tags (40+) | Segment leads for targeted campaigns |
| SMS Automation | Speed-to-lead, follow-up, reminders |
| Email Automation | Estimate follow-up, care guides, seasonal campaigns |
| Forms (1-2) | Pre-booking questionnaire, lead capture |
| Opportunities | Track quote values, project value |
| Conversations | Unified inbox for SMS/email/calls |
| Trigger Links | Review requests, booking links, portfolio links |

---

### 10.2 Integration Points

| Integration | Purpose |
|------------|---------|
| Google Business Profile | Review request links |
| Google LSA | Lead routing and attribution |
| Houzz | Lead form integration (if available) |
| Facebook/Instagram | Ad audience sync for retargeting |
| QuickBooks / Invoice Ninja | Invoice trigger post-job (optional) |
| AI Voice Agent | Speed-to-lead call automation |
| Google Calendar | Contractor schedule sync |

---

### 10.3 Snapshot Setup Time Estimate

| Component | Time |
|-----------|------|
| Pipeline creation (5) | 2 hours |
| Workflow build (12) | 6 hours |
| SMS/email copy (40+ templates) | 4 hours |
| Custom fields setup | 1 hour |
| Calendar configuration (2) | 1 hour |
| Tag library | 30 minutes |
| Forms (2) | 1 hour |
| Testing and QA | 2 hours |
| **Total build time** | **~17-18 hours** |

---

## Section 11: Onboarding Checklist for Deck & Patio Clients

When onboarding a deck/patio contractor to this snapshot, complete the following customization:

### Information to Collect from Client

- [ ] Business name, phone number, email
- [ ] Service area (city/cities, radius)
- [ ] GHL phone number (for SMS/calls)
- [ ] Google Review link
- [ ] Booking calendar availability preferences
- [ ] Materials they specialize in (composite? pressure treated? cedar? all?)
- [ ] Do they handle permits themselves or recommend client hire permit expeditor?
- [ ] Service types offered (check all that apply: new builds / repair / refinishing / pergola / patio / outdoor kitchen)
- [ ] Preferred contractor name/voice for SMS templates (first person or company name?)
- [ ] Portfolio photos for email templates (minimum 5-10 project photos)
- [ ] Referral incentive amount (default: $250)
- [ ] Do they work with realtors? (yes/no — activates agent-specific pipeline)
- [ ] Off-season services? (winter deck inspections, spring cleaning, any year-round work?)

### Customization Required

- [ ] Replace all `[Company Name]` and `[Contractor Name]` placeholders
- [ ] Set service area in calendar settings
- [ ] Upload portfolio photos to email templates
- [ ] Set seasonal campaign trigger dates (adjust for local climate/frost dates)
- [ ] Configure AI voice agent intro script (if using GHL AI)
- [ ] Set Google Review link in all review request templates
- [ ] Adjust referral credit amount if client prefers different incentive
- [ ] Set lead notification email/SMS to contractor's phone

---

## Section 12: Positioning — How to Sell This to Deck Contractors

### 12.1 The Pitch

> "Most deck contractors lose 30-40% of their leads simply because they stopped following up. This system follows up automatically — for 21 days — so you never lose a lead you worked to get. It books your design consultations, tracks your permits, updates your clients while you're on the job site, and even campaigns to your clients' neighbours after every build. We built this specifically for deck and outdoor living companies — not a generic contractor template."

### 12.2 ROI Story

- Average deck contractor: 40-60 leads per season, closes 25-35%
- With automated follow-up at 5-minute speed-to-lead + 21-day sequence: close rate typically increases 8-15%
- At $18,000 average project value, closing 3 additional projects per season = $54,000 in recovered revenue
- 1APP monthly subscription: $197-$397/month
- **ROI: One closed job covers 18-24 months of subscription cost**

### 12.3 Trial Story for Prospect

> "You spent $500 on that Google ad. A lead came in, you called them back the next morning, and they'd already gone with someone else. Our system would have texted them within 60 seconds of that inquiry, called them automatically, and had a booking link in their hands before your coffee was done. That one lead paid for 12 months of this system."

---

## Section 13: Competitive Moat

### Why This Snapshot Wins Long-Term

1. **Depth of industry knowledge** — generic templates don't know what a ledger board is, what Trex Transcend costs, or that cedar needs to be sealed within 30 days. This one does. Contractors recognize expertise immediately.

2. **Seasonal automation** — the spring/fall campaigns fire automatically every year without the client lifting a finger. This is "set it and forget it" marketing that compounds over time.

3. **Neighbour campaign compound effect** — each completed job creates 2-3 new neighbour leads through the automated campaign. Over a 3-year subscription, a contractor with 30 builds/year generates 60-90 additional neighbour leads from the automation alone.

4. **Annual refinishing revenue stream** — every wood deck client is on a perpetual annual reminder campaign. After 3 years, a contractor has hundreds of past clients receiving spring refinishing outreach without any manual effort.

5. **The upgrade flywheel** — repair clients → composite upsell → new build → neighbour campaign → more repair clients. The snapshot creates a self-reinforcing loop of revenue from a single client relationship.

---

## Appendix A: Industry Glossary (For Template Writing Reference)

| Term | Definition |
|------|-----------|
| Ledger board | The board bolted to the house structure that supports one end of the deck frame |
| Joist | The horizontal framing members that span the width of the deck and support the decking boards |
| Beam | The main horizontal structural member spanning between posts |
| Footing | Concrete piers dug into the ground below frost line that support the posts |
| Post | Vertical structural member sitting on footings, supporting the beam |
| Decking board | The surface boards you walk on — can be composite, cedar, or pressure treated |
| Fascia board | The finishing boards on the perimeter of the deck that hide the rim joists |
| Picture frame | A decking pattern where boards run perpendicular to the field boards as a border |
| Railing | The safety barrier around elevated decks — includes posts, top rail, bottom rail, and infill |
| Baluster | The vertical spindles in the railing infill between posts |
| Post cap | Decorative cap on top of railing posts |
| Composite decking | Engineered wood-plastic composite material — brands include Trex, Fiberon, TimberTech, AZEK |
| Pressure treated (PT) | Kiln-dried lumber treated with preservatives to resist rot and insects — often Southern Yellow Pine |
| Cedar | Naturally rot-resistant softwood — common for decks, often has natural reddish hue |
| Trex | Most recognized composite decking brand — products include Select, Enhance, Transcend |
| Fiberon | Premium composite brand — Paramount, Horizon, Pro series — 50-year fade/stain warranty |
| TimberTech / AZEK | Premium composite and PVC decking brand — AZEK is 100% PVC |
| Pergola | Open overhead lattice structure with beams and rafters — provides partial shade |
| Gazebo | Fully roofed, usually octagonal freestanding structure |
| Outdoor kitchen | Built-in cooking station with grilling, countertops, cabinetry, sometimes refrigeration |
| Frost line | The depth below which the ground doesn't freeze — footings must go below this |
| Joist hanger | Metal connector bracket that joins joists to the ledger or rim joist |
| Rim joist | The perimeter joist that runs around the outside of the deck frame |
| Setback | Minimum distance a structure must be from property lines — set by municipal zoning |
| Lot coverage | Maximum percentage of a property that can be covered by structures — affects deck size |
| Building permit | Municipal approval required for decks above a certain height or size |
| Cable railing | Modern railing style with horizontal stainless steel cable infill |
| Glass panel railing | Railing with tempered glass panels — premium, unobstructed view |
| Decking hidden fastener | Proprietary clip system that fastens boards without visible screws — used with most composite |
| Staining | Applying penetrating stain to wood to protect and colour it |
| Power washing | High-pressure wash used to clean and prepare decks for staining |

---

## Appendix B: Recommended GHL AI Voice Agent Script (Deck Vertical)

**Agent Name:** "Alex from [Company Name]"
**Voice:** Professional, warm, local

```
"Hi, this is Alex calling from [Company Name] — you just reached out about a 
deck or outdoor living project. I just wanted to make sure we caught you right 
away. Are you still looking for help with your project?

[If yes]: Perfect! Can I get your name and a quick description of what you're 
thinking — new deck build, repair, pergola, or something else?

[After capture]: Great. I'm going to get [Contractor Name] on the line with you 
or have them call you back within the next 15 minutes. 
In the meantime, can I send you a link to our portfolio?

[If no answer]: No problem at all. I'll have [Contractor Name] try you back 
in about 30 minutes. We're looking forward to helping you build 
something great for your backyard. Talk soon!"
```

---

*End of Research Document*

**Document Version:** 1.0
**Last Updated:** July 2026
**Prepared By:** 1APP Technologies — Snapshot Research Team
