# 🚪 Garage Door GHL Snapshot — Agency Build Research Document
**Prepared for:** 1app Technologies Inc.
**Document Type:** Comprehensive Snapshot Research & Build Specification
**Status:** Ready for Build
**Date:** July 2026

---

## Executive Summary

The garage door industry is one of the highest-intent, fastest-converting service verticals in home services. Customers searching for "garage door spring replacement near me" or "garage door won't open" are in **immediate buying mode** — often stranded in a driveway, late for work, or with a car trapped in their garage. The conversion window is measured in minutes, not days.

Despite this, **most garage door companies are running on phone calls, sticky notes, and zero follow-up systems.** They answer the call, dispatch a tech, collect payment, and never contact the customer again. No review request. No annual tune-up reminder. No smart opener upsell. No referral ask. Revenue left on every single job.

The **1app Garage Door Snapshot** is built to capture that revenue. This document defines every component of that snapshot — pipeline architecture, workflows, SMS/email templates, booking flows, and competitive differentiation.

---

## Section 1: Industry Overview & Market Context

### 1.1 Industry Size & Structure

- **Market size:** ~$5B+ annually (US) in garage door installation, repair, and replacement
- **Business type:** Primarily owner-operated companies with 1–10 technicians; some regional chains
- **Average ticket:** $150–$600 for repairs; $800–$3,500+ for new door installation; $2,500–$8,000 for commercial sectional doors
- **Emergency calls:** Represent 40–60% of all inbound volume; highest urgency, highest conversion rate
- **Seasonality:** Spring and fall are peak periods (torsion spring failures spike in temperature extremes); winter storm damage creates surges

### 1.2 Typical Customer Profiles

| Profile | Trigger | Urgency | Avg Ticket |
|---|---|---|---|
| Homeowner — Emergency | Spring broke, cable snapped, door won't open | Extreme | $200–$450 |
| Homeowner — Scheduled | Slow door, noisy operation, worn rollers | Low-Medium | $150–$350 |
| New Door Buyer | Old door, renovation, curb appeal | Low | $1,200–$3,500 |
| Commercial Property Manager | Sectional dock door, industrial opener, panel damage | Medium | $800–$8,000+ |
| New Home Builder | Builder-grade door needed on new construction | Pre-scheduled | $600–$1,800 |

### 1.3 Core Services (Language for Snapshot)

- **Torsion spring replacement** (most common emergency call)
- **Extension spring replacement**
- **Broken cable repair / cable replacement**
- **Garage door opener installation** (belt-drive, chain-drive, screw-drive)
- **Smart opener upgrade** (myQ, Chamberlain, LiftMaster 84501)
- **Panel replacement** (dented, cracked, or damaged steel panels)
- **Track repair / realignment**
- **Roller replacement** (steel or nylon)
- **Safety sensor alignment / replacement**
- **Weather seal replacement**
- **New door installation** (residential — single, double, carriage-style)
- **Commercial sectional door service** (dock doors, roll-up steel, fire doors)
- **Annual safety inspection & tune-up**
- **Keypad and remote programming**

---

## Section 2: Garage Door Business Pain Points

These are the specific problems 1app solves for garage door operators. Use these in sales conversations.

### 2.1 Emergency Call Management

**The problem:** A broken torsion spring at 7am means the homeowner can't get their car out. They call the first 3 companies they find on Google. Whoever answers first and gives a clear ETA wins the job. Most companies **miss the call** because the owner is on another job and the phone isn't answered.

**What gets lost:** If a company misses an emergency call, that lead is gone in under 2 minutes to a competitor. At $300/repair average, one missed call/day = $100K+ in lost annual revenue.

**What 1app fixes:**
- Missed Call Text Back fires instantly (within 60 seconds) with a "We got your message — a tech will call you back in 15 minutes. Want to book online?" message
- Emergency intake form captures name, address, door issue, and urgency level
- Dispatcher is notified immediately via internal task or notification workflow

### 2.2 No Follow-Up System

**The problem:** Garage door companies complete a service call and never contact the customer again. No review request. No "how was your service?" message. No annual reminder. No smart opener upsell.

**What gets lost:** 
- Google reviews (5-star review pipeline is the #1 driver of new leads for local service companies)
- Repeat business (every customer is a future tune-up call, new opener, new door)
- Referrals (satisfied customers will refer if you give them a nudge)

**What 1app fixes:**
- Post-service review request sends 24 hours after job completed
- 6-month check-in: "It's been 6 months since your spring replacement — time for a quick safety check?"
- Annual tune-up campaign hits entire customer list in March (pre-season) and September

### 2.3 Torsion Spring Seasonality

**The problem:** Spring breaks spike in March–April (temperature changes affect tension) and November (cold weather, increased usage). Companies scramble, run out of stock, and can't handle call volume.

**What 1app fixes:**
- Pre-season campaign (February and August) to existing customers: "Before the busy season hits — book a tune-up now and we'll inspect your springs, cables, and safety sensors for free."
- Drives scheduled volume before the emergency surge; customers who get a tune-up are less likely to have an emergency call

### 2.4 Technician Scheduling Chaos

**The problem:** Dispatching is manual. Techs text the owner. Owners forget to confirm. Customers don't know when their tech is arriving. No-show rate is high.

**What 1app fixes:**
- Automated booking with calendar integration
- Confirmation SMS at booking + reminder 1 hour before appointment
- "Your tech is on the way" manual trigger option via GHL mobile app
- Post-appointment survey to flag issues before they become bad reviews

### 2.5 Parts Availability (Missed Upsell Window)

**The problem:** Technician arrives, fixes the torsion spring, leaves. Customer never hears about smart opener upgrades, new door options, or an insulation package. Tech doesn't upsell — they're focused on the next call.

**What 1app fixes:**
- Post-service email includes: "While we were at your home, we noticed your opener is X years old. Many of our customers upgrade to a smart opener at the same time — here's why that's worth it."
- Smart opener upsell workflow with FAQ-style email sequence

### 2.6 Zero Review Strategy

**The problem:** Garage door companies rarely have more than 20–50 Google reviews. Their LSA (Local Services Ads) rank is tanking because competitors are at 200+ reviews.

**What 1app fixes:**
- Every completed job triggers a review request sequence
- Timing is designed around the emotion window (ask when the customer is most grateful — right after the tech saves their day)
- Review request goes to Google, Facebook, or HomeAdvisor depending on client preference

---

## Section 3: Competitive Landscape — GHL Snapshots for Garage Door

### 3.1 What Currently Exists

Most GHL agencies serving home services build **generic "home services" snapshots** that include:
- Basic missed call text back
- Appointment confirmation sequence
- 1–2 follow-up SMS
- Simple 3-stage pipeline (New Lead → Appointment → Won)

These are sold to garage door companies with minor rebranding. They are not industry-specific, use no garage door language, and miss 60%+ of the revenue opportunity.

**Known garage door specific GHL snapshots in the market (as of 2025–2026):**
- A few Snapshots on the GHL marketplace branded as "home services" with garage door examples — but these are shallow
- Agencies like Niche Automations, AutomatePro, and local SaaS resellers have created niche variants, but none have deep garage door industry specificity (spring language, seasonal campaigns, commercial vs. residential split, smart opener sequences)

### 3.2 What's Missing in Existing Snapshots

| Missing Element | Why It Matters |
|---|---|
| Emergency vs. scheduled intake split | Emergency calls need a different response cadence than scheduled service |
| Torsion spring seasonal campaigns | Biggest revenue driver — completely ignored |
| Smart opener upsell workflow | $300–$800 avg ticket — easy to automate |
| Commercial vs. residential pipeline | Different timelines, decision-makers, ticket sizes |
| Annual safety inspection reminder | Lifetime value driver — creates recurring revenue |
| Google LSA review strategy | Tied directly to LSA rank and lead volume |
| Technician dispatch notification | Internal workflow — not just external customer comms |
| New door consultation funnel | Different buyer journey than repair customer |
| Post-emergency gratitude sequence | Highest review rate and upsell conversion timing |

### 3.3 The 1app Competitive Advantage

1app's Garage Door Snapshot is built **from the industry up**, not from a generic template down. Every pipeline stage name, every SMS template, every workflow trigger uses the language of a garage door technician, not a generic marketer. This snapshot can be demonstrated to a garage door company owner and they will immediately recognize their business in it.

---

## Section 4: Pipeline Architecture

### 4.1 Pipeline 1 — Emergency Repair Pipeline

**Purpose:** Capture and convert emergency inbound calls (broken spring, snapped cable, door off track, opener failure)

**Stages:**

| Stage | Description | SLA |
|---|---|---|
| 🚨 Emergency Inbound | Lead captured via missed call, web form, or LSA | 0–2 min response |
| 📞 Tech Dispatched | Owner/dispatcher confirmed tech is heading to site | <30 min |
| 🔧 On Site — Diagnosing | Tech at location, assessing spring, cable, opener | Active |
| 💰 Quote Presented | Tech has quoted repair (torsion spring, cable, etc.) | Active |
| ✅ Job Completed | Repair done, payment collected | Same day |
| ⭐ Review Requested | 24hr post-job review request sent | +24 hours |
| 🔄 Annual Reminder Set | Trigger set for 12-month follow-up | +12 months |

**Custom Fields for this pipeline:**
- Door Issue (dropdown): Torsion Spring | Extension Spring | Cable | Opener | Panel | Track | Sensor | Other
- Door Brand: Clopay | Wayne Dalton | Amarr | CHI | Raynor | LiftMaster | Other
- Opener Brand: LiftMaster | Chamberlain | Genie | Craftsman | Linear | Other
- Opener Age (dropdown): <5 years | 5–10 years | 10–15 years | 15+ years
- Door Type: Single Residential | Double Residential | Commercial Sectional | Roll-Up Steel
- Smart Opener Offered?: Yes / No
- Payment Method: Cash | Card | E-Transfer | Invoice

---

### 4.2 Pipeline 2 — Scheduled Service / Non-Emergency Repair Pipeline

**Purpose:** Manage non-emergency requests (noisy door, slow operation, worn rollers, weather seal replacement)

**Stages:**

| Stage | Description |
|---|---|
| 📋 Service Request Received | Non-emergency call/web form submitted |
| 📅 Appointment Booked | Date/time confirmed with customer |
| ⏰ Reminder Sent | 24hr + 1hr reminder sequence active |
| 🔧 Service In Progress | Tech on site |
| ✅ Service Completed | Work done, invoice sent |
| ⭐ Review & Referral | Review request + referral ask sent |
| 🔄 6-Month Follow-Up | Seasonal check-in trigger set |

---

### 4.3 Pipeline 3 — New Door Installation Pipeline

**Purpose:** Manage the longer sales cycle for new residential door installation (curb appeal, renovation, replacement of old door)

**Stages:**

| Stage | Description | Typical Timeline |
|---|---|---|
| 🏠 Free Estimate Request | Customer submits quote request | Day 0 |
| 📐 Estimate Scheduled | In-home or virtual consultation booked | Day 1–3 |
| 📋 Quote Sent | Door options, pricing, timeline sent via email | Day 2–5 |
| 💬 Follow-Up 1 | First follow-up call/text | Day 5–7 |
| 💬 Follow-Up 2 | Second follow-up with financing options | Day 10–14 |
| 🤝 Deal Closed | Customer commits, deposit collected | Day 7–21 |
| 📦 Order Placed | Door ordered from manufacturer | After deposit |
| 🔧 Installation Scheduled | Install date confirmed | Pre-install |
| ✅ Installation Complete | Door installed, customer walkthrough done | Install day |
| ⭐ Review + Before/After | Review request with before/after photo prompt | +24 hours |

**Custom Fields:**
- Door Style: Traditional Steel | Carriage House | Modern/Contemporary | Wood | Glass Accent
- Insulation: R-value 6 | R-value 12 | R-value 18 | Non-insulated
- Color: White | Almond | Desert Tan | Brown | Black | Custom
- Width x Height:
- Spring Type Needed: Torsion | Extension
- Opener Included: Yes / No / Upgrade to Smart
- Financing Offered: Yes / No

---

### 4.4 Pipeline 4 — Commercial / Property Manager Pipeline

**Purpose:** Manage commercial sectional door service, dock door repair, and property manager accounts

**Stages:**

| Stage | Description |
|---|---|
| 🏭 Commercial Inquiry | Property manager or business contacts for service |
| 📋 Site Assessment Requested | Scheduling walkthrough for multiple doors |
| 💼 Proposal Sent | Formal quote for commercial work |
| ✍️ Contract Signed | Service agreement executed |
| 🔧 Work Scheduled | Tech team dispatched |
| ✅ Work Completed | Sign-off, invoice sent |
| 🔄 Maintenance Contract Offered | Annual or quarterly inspection contract pitched |

---

## Section 5: Workflow Architecture

### 5.1 Workflow 1 — Emergency Missed Call Response (HIGHEST PRIORITY)

**Trigger:** Incoming call to business number — call NOT answered (missed call)

**Workflow Steps:**
1. **Immediate SMS (T+0:45 seconds):**
   > "Hey, it's [Company Name] — we just missed your call! If your garage door is stuck or you have an emergency, reply YES and we'll call you right back within 15 minutes. Or book a same-day slot here: [booking link]"

2. **If no reply in 5 minutes — Follow-up SMS (T+5 min):**
   > "Still here if you need us! A broken torsion spring or cable is something we handle daily — usually same-day. What's going on with your door?"

3. **Internal Task Created:** "⚠️ Missed Emergency Call — [Contact Name] — Call Back NOW" assigned to owner

4. **If reply received:** Branch into Emergency Intake sub-workflow
5. **If no reply in 30 minutes:** One final SMS:
   > "We'll be available until 7pm today if you still need help with your garage door. Call us at [phone] or book at [link]."

**Branch — Emergency Intake (after initial reply):**
- AI chat or SMS bot asks: "What's happening with your door? (spring broke / won't open / off track / other)"
- Captures address for dispatch
- Creates contact + opportunity in Emergency pipeline at "Emergency Inbound" stage
- Owner notified via GHL notification

---

### 5.2 Workflow 2 — Appointment Booking Confirmation & Reminder

**Trigger:** Appointment booked via calendar

**Workflow Steps:**
1. **Instant Booking Confirmation SMS:**
   > "You're booked! [First Name], your garage door appointment is confirmed for [Date] between [Time Window]. Your tech from [Company Name] will arrive ready to handle your [service type]. Questions? Call or text us at [phone]."

2. **Booking Confirmation Email:** Full appointment summary with:
   - Date, time window, address confirmation
   - What to have ready (garage access, any photos of the issue)
   - What to expect (tech will diagnose, provide quote, and complete work same visit if parts available)
   - Cancel/reschedule link

3. **24-Hour Reminder SMS:**
   > "Reminder: Your garage door appointment is TOMORROW between [Time Window]. Our tech will be there with common parts on the truck — no waiting for parts on most spring, cable, and roller replacements. See you then!"

4. **1-Hour Reminder SMS:**
   > "[First Name], your tech is on schedule for today between [Time Window]. They'll be calling ahead before arriving. If anything changes, reply here or call [phone]."

---

### 5.3 Workflow 3 — Post-Job Follow-Up & Review Request (Emergency Repair)

**Trigger:** Opportunity moved to "Job Completed" stage

**Timing:** Critical — this workflow capitalizes on the peak emotion window after an emergency rescue

**Workflow Steps:**

**Step 1 — Thank You SMS (T+2 hours after completion):**
> "Thanks for trusting [Company Name] today, [First Name]! Glad we could get your garage door working again. If you have any concerns in the next few days, just text us here. We stand behind every repair."

**Step 2 — Review Request SMS (T+22 hours):**
> "Quick favour — if [Tech Name] took good care of you today, would you mind leaving us a Google review? It takes 60 seconds and helps local families find a garage door company they can trust: [Google Review Link] 🙏"

**Step 3 — Review Request Email (T+24 hours, if no review click):**
Subject: "How did your garage door repair go, [First Name]?"
> Body includes: thank you, photo of completed work if uploaded, Google + Facebook review links, referral ask

**Step 4 — 6-Month Safety Check SMS (T+6 months):**
> "Hi [First Name], it's been 6 months since we replaced your torsion spring! Garage door springs and cables should be inspected annually. Want to book a quick safety check? We'll check your springs, cables, rollers, and sensors — usually takes 20 minutes. Book here: [link]"

**Step 5 — Annual Tune-Up Reminder (T+11 months):**
> "It's almost been a year since your garage door repair, [First Name]. Time for your annual safety inspection! Spring issues caught early prevent emergency calls. Book your tune-up: [link]"

---

### 5.4 Workflow 4 — Post-Job Follow-Up (Scheduled / Non-Emergency)

**Trigger:** Scheduled service opportunity moved to "Service Completed"

**Steps:**
1. **Thank You SMS (T+2 hours):** Casual, warm, not urgent
2. **Review Request (T+48 hours):** Slightly softer than emergency version (lower emotion peak)
3. **Smart Opener Check-In (T+7 days):** If opener age is 10+ years
4. **6-Month Follow-Up** (same as emergency sequence)

---

### 5.5 Workflow 5 — New Door Installation Lead Nurture

**Trigger:** Free estimate form submitted

**Purpose:** Educate and build confidence during the longer decision window for a new door purchase

**Sequence:**

**Day 0 — Confirmation SMS:**
> "Got it! [First Name], we received your request for a free garage door estimate. Someone from [Company Name] will reach out within 1 business hour to schedule your free consultation. Questions? Text here anytime."

**Day 0 — Confirmation Email:**
Subject: "Your Free Garage Door Estimate — What Happens Next"
> Body: What to expect during the consultation, door styles overview, financing options available, link to gallery of recent installs

**Day 1 — Education Email — "Which Door Is Right for You?"**
> Content: Steel vs. wood vs. composite, R-value insulation guide, carriage-house vs. traditional vs. modern styles, what affects pricing

**Day 3 (if no booking) — Follow-Up SMS:**
> "Still thinking about your new garage door, [First Name]? Happy to answer questions by text or schedule a quick call. What's most important to you — insulation, style, or price?"

**Day 7 — Social Proof Email:**
Subject: "What our customers say about their new garage door"
> 3–5 before/after stories from local customers, average installation timeline, satisfaction guarantee language

**Day 14 (if still no decision) — "Financing Available" SMS:**
> "Did you know we offer flexible financing on new door installations? Many customers pay as low as $X/month for a brand-new insulated carriage-style door. Want the details?"

**Day 21 — Final Follow-Up:**
> "We've saved your quote, [First Name]. If you're ready to move forward or want to revisit the options, we're here. No pressure — just don't want you to miss our current installation schedule availability."

---

### 5.6 Workflow 6 — Smart Opener / Smart Home Upsell

**Trigger:** Tag applied "Opener 10+ Years" OR "No Smart Opener" during service visit

**Purpose:** Create a second revenue event from every completed repair job

**Sequence:**

**Day 7 Post-Service — Education SMS:**
> "Quick tip from the team at [Company Name]: If your garage door opener is more than 10 years old, it likely doesn't have battery backup or smart connectivity. The new LiftMaster 84501 lets you open/close from your phone, get alerts, and even share access with family. We install these same-day — interested in a quick quote?"

**Day 7 Post-Service — Education Email:**
Subject: "Your Opener Is Working — But Is It Working FOR You?"
> Content: What smart openers can do (myQ app, real-time alerts, remote access for deliveries, auto-close timer), cost comparison, installation time (typically 45 minutes), special offer if bundled with a tune-up

**Day 14 — Follow-Up SMS (if no response):**
> "Just following up — smart opener installs are going fast this season. We can often do same-day. Price starts at $X installed. Want to lock in a time?"

---

### 5.7 Workflow 7 — Annual Safety Inspection Campaign (Seasonal Campaigns)

**Trigger 1:** Automation fires February 1 (pre-spring surge)
**Trigger 2:** Automation fires August 15 (pre-fall surge)

**Audience:** All contacts with tag "Past Customer" who have NOT booked in the last 90 days

**Spring Campaign — February:**

**Email:**
Subject: "Your Garage Door Is About to Work HARD — Is It Ready?"
> Body: Explain spring/cable stress from winter cold and spring temperature swings; torsion springs have a rated cycle life (typically 10,000–20,000 cycles); offer a spring-season tune-up including lubrication, spring inspection, cable check, safety sensor test, and balance test; time-limited scheduling offer

**SMS:**
> "Spring is coming and so is garage door season! [First Name], when did you last have your springs, cables, and rollers inspected? A 30-minute tune-up now can prevent a $300 emergency call later. Book your spring tune-up: [link]"

**Fall Campaign — August/September:**

**Email:**
Subject: "Before Winter Hits — Check Your Garage Door"
> Body: Cold weather makes springs brittle and grease thick; safety sensors can be knocked out of alignment from kids playing in the garage over summer; opener batteries drain faster in cold; offer fall tune-up package

**SMS:**
> "Fall tune-up season is here, [First Name]! Cold weather is the #1 cause of broken torsion springs and snapped cables. Let's inspect your door before winter — book now and we'll throw in a free lubrication service: [link]"

---

### 5.8 Workflow 8 — Commercial / Property Manager Nurture

**Trigger:** Commercial inquiry form submitted or tagged "Commercial Lead"

**Sequence:**

**Immediate Response (T+5 min):**
> "Hi [First Name] — thanks for reaching out to [Company Name] about your commercial door service. We work with property managers and businesses across [city] on sectional dock doors, roll-up steel doors, and commercial opener systems. Someone will contact you within 1 hour to discuss your needs and schedule a site visit."

**Site Assessment Confirmation:**
Email with: what to expect during the assessment, common commercial door issues addressed (dock door springs, counterbalance systems, safety edge sensors, high-cycle operators), link to request additional locations

**Post-Quote Follow-Up (3-day):**
> "Following up on the commercial door proposal we sent over for [Property/Location]. Any questions on the service plan or timeline? We can adjust scope if needed. [First Name], I'm available for a quick call at your convenience."

**Maintenance Contract Offer (Post-Work Completion):**
> "With commercial properties, preventive maintenance on sectional doors and high-cycle openers is far cheaper than emergency replacements. We offer quarterly or annual inspection contracts for multi-door properties. Want a proposal for an ongoing service agreement?"

---

### 5.9 Workflow 9 — Referral Generation

**Trigger:** Post-review confirmation (contact clicks review link) OR tag "5 Star Review"

**SMS (T+24 hours after review confirmed):**
> "Thank you for the review, [First Name] — it means the world to us! One more thing: do you know anyone else in [neighbourhood/city] who might need their garage door serviced? If you refer a friend and they book with us, we'll send you a $25 Amazon gift card as a thank-you. No limit on referrals 🙌"

---

## Section 6: Lead Sources & Intake Configuration

### 6.1 Lead Source Matrix

| Lead Source | Volume | Urgency | Conversion Rate | Notes |
|---|---|---|---|---|
| Google LSA (Local Services Ads) | ⭐⭐⭐⭐⭐ | Extreme | 60–80% | Highest intent; "garage door repair near me" |
| Google Ads (Standard) | ⭐⭐⭐⭐ | High | 40–60% | Spring keywords: "torsion spring replacement" |
| Google Maps / Organic | ⭐⭐⭐⭐ | High | 40–65% | Review-driven; 4.5+ stars critical |
| Referrals | ⭐⭐⭐ | Medium | 70–85% | Highest close rate; automated via referral workflow |
| HomeAdvisor / Angi | ⭐⭐⭐ | Medium-High | 25–40% | Shared leads; speed matters |
| Nextdoor | ⭐⭐ | Medium | 50–70% | Community-based; reviews/word of mouth |
| New Home Builders | ⭐⭐ | Pre-scheduled | 80–90% | Relationship sales; high volume |
| Property Managers | ⭐⭐ | Varies | 60–75% | Commercial accounts; recurring revenue |
| Facebook/Instagram Ads | ⭐⭐ | Low-Medium | 15–30% | Better for new door and smart opener offers |
| Direct Mail | ⭐ | Low | 2–8% | Seasonal campaign support only |

### 6.2 Intake Forms — Configuration

**Form 1 — Emergency Repair Intake (Short — Mobile First)**
Fields:
- First Name (required)
- Phone Number (required)
- Address (required — for dispatch)
- What's Wrong?: (dropdown) Spring Broke | Cable Snapped | Door Won't Open | Door Off Track | Opener Problem | Noisy/Slow | Panel Damage | Other
- How Urgent?: Same-Day Emergency | Today is Fine | Schedule for Later

**Form 2 — Scheduled Service Request**
Fields:
- First Name + Last Name
- Phone + Email
- Address
- Service Needed: (multi-select) Spring Tune-Up | Roller Replacement | Opener Service | Safety Sensor | Weather Seal | Track Adjustment | Other
- Preferred Date/Time
- Door Brand (optional)
- Opener Brand + Age (optional)

**Form 3 — Free New Door Estimate**
Fields:
- First Name + Last Name
- Phone + Email
- Address
- Current Door: Single | Double | Other
- Reason for Replacing: Old/Worn | Storm Damage | Renovation/Curb Appeal | Moving In | Other
- Preferred Style: Traditional Steel | Carriage House | Modern/Flush | Not Sure
- Budget Range: Under $1,500 | $1,500–$2,500 | $2,500–$4,000 | No Budget Set
- Financing Interest: Yes | No | Tell Me More
- Preferred Contact Method: Call | Text | Email

**Form 4 — Commercial Service Inquiry**
Fields:
- Contact Name + Company Name
- Phone + Email
- Property Address
- Door Type: Sectional Dock Door | Roll-Up Steel | Commercial Overhead | Fire Door | Other
- Number of Doors Needing Service
- Issue: Emergency Repair | Preventive Maintenance | Replacement | Annual Contract | Other
- Preferred Response Time: Within 1 Hour | Today | This Week

---

## Section 7: Booking Flow Architecture

### 7.1 Emergency Same-Day Booking

**Flow:** Missed call → SMS → "Reply YES" → Collect address + issue → Internal dispatch alert → Confirm ETA via SMS

**Key principles:**
- NO calendar booking widget for emergencies — too slow, too much friction
- SMS-first intake
- Human confirmation from owner/dispatcher required
- Time to first response: under 60 seconds (automated), under 15 minutes (human call-back)

### 7.2 Scheduled Service Booking

**Flow:** Web form or call → Booking calendar widget → Confirmation SMS/Email → 24hr + 1hr reminders

**Calendar setup:**
- Service duration: 1 hour (standard repair), 2 hours (opener install), 30 minutes (tune-up)
- Buffer time: 30 minutes between appointments (drive time)
- Available windows: 8 AM – 5 PM (customize per client)
- Same-day booking: Allow up to 2 PM for same-day
- Require address at booking for route planning

### 7.3 Free Estimate — New Door Installation

**Flow:** Landing page → Estimate form → Automated nurture starts → Manual call from owner within 1 business hour → Estimate appointment booked → In-home consultation

**Landing page elements:**
- Before/after gallery of installed doors (client photos)
- Door style selector
- Financing mention above the fold
- "Free estimate — no obligation" framing
- Trust signals: Google reviews count, years in business, license/insurance info

---

## Section 8: SMS & Email Templates

### 8.1 Emergency Response Templates

**SMS — Missed Call (Immediate):**
> "Hey! [Company Name] here — missed your call. Is this about your garage door? Reply YES and we'll call back in 15 min, or book here: [link] 🚪"

**SMS — Emergency Confirmed — Tech Dispatched:**
> "Great news — we have a tech heading your way, [First Name]. They should arrive between [time] and [time]. We'll text you when they're 15 min out. Spring or cable issue today?"

**SMS — Tech On The Way (15 min ETA):**
> "Your tech is about 15 minutes away, [First Name]! They have spring, cable, and opener parts on the truck for most same-day fixes. See you soon 🔧"

**SMS — Post-Dispatch Confirmation:**
> "Just confirming we're locked in for today. If anything changes on your end, text here or call [phone]. See you between [time window]."

---

### 8.2 Appointment Booking Templates

**SMS — Booking Confirmation:**
> "You're booked! [First Name] — [Date], [Time Window] for your garage door service. We'll send a reminder the day before. Questions? Text here. — [Company Name]"

**SMS — 24hr Reminder:**
> "Tomorrow is your garage door appointment ([Time Window]). Our tech carries common springs, cables, and opener parts — most repairs are same-visit. See you then! — [Company Name]"

**SMS — 1hr Reminder:**
> "Heads up, [First Name] — your tech is on schedule for [Time Window] today. They'll call ahead. — [Company Name]"

**Email — Booking Confirmation:**
Subject: "Your Garage Door Appointment is Confirmed ✅"
> Hi [First Name],
> Your appointment with [Company Name] is confirmed!
> 📅 **Date:** [Date]
> ⏰ **Time:** [Time Window]
> 📍 **Address:** [Address]
> 🔧 **Service:** [Service Type]
>
> What to have ready:
> - Clear access to the garage (move vehicles if possible)
> - Know the brand of your opener if possible
> - Any photos of the issue are helpful but not required
>
> Our techs carry common torsion springs, extension springs, cables, rollers, and sensors on the truck — most repairs are completed same-visit.
>
> Need to reschedule? Reply to this email or call [phone].
>
> See you [Date]!
> — The [Company Name] Team

---

### 8.3 Post-Service Templates

**SMS — Thank You (2 hours post-completion):**
> "Thanks for choosing [Company Name] today, [First Name]! Hope your door is working great. If you notice anything in the next few days, just text us here — we stand behind every repair. 🙏"

**SMS — Review Request (22 hours post-completion):**
> "Quick favour — if [Tech Name] took good care of you, a 60-second Google review helps us a ton! [Google Review Link] Thanks so much! — [Company Name]"

**SMS — 6-Month Safety Check:**
> "Hey [First Name] — it's been 6 months since your garage door repair! A quick annual inspection catches worn springs and cables before they become emergencies. Book your 30-minute safety check: [link] — [Company Name]"

**Email — Smart Opener Upsell (Day 7):**
Subject: "Is Your Garage Door Opener Keeping Up With Your Life?"
> Hi [First Name],
>
> Thanks again for choosing [Company Name] for your recent [service]. While we were there, we noticed your opener is [X] years old.
>
> Here's what a smart opener upgrade gives you:
> ✅ Open/close your door from anywhere with your phone
> ✅ Real-time alerts when your door opens or closes
> ✅ Share access with family members and delivery services
> ✅ Automatic close timer (never wonder if you left it open)
> ✅ Battery backup — works even during power outages
>
> **Most Popular Upgrade:** LiftMaster 84501 with myQ — installed in under an hour
>
> **Installed price: Starting at $X**
>
> Book your upgrade: [link]
>
> Have questions? Text us at [phone] — we're happy to chat through the options.
>
> — [Tech Name] & The [Company Name] Team

---

### 8.4 Seasonal Campaign Templates

**Spring Campaign — Email (February):**
Subject: "Your Torsion Springs Just Survived Winter — But For How Long?"
> Hi [First Name],
>
> Spring is coming — and so is the busiest season for garage door service calls.
>
> Here's why: Torsion springs (the big horizontal spring above your door) expand and contract with temperature. After a Canadian/northern winter, springs are under more stress than any other time of year. Most springs are rated for 10,000 cycles. After that, it's a matter of time.
>
> **Signs your springs may need attention:**
> - Door takes longer to open or close than it used to
> - You hear squeaking, popping, or grinding
> - The door doesn't sit level when partially open
> - Your opener seems to strain more than before
>
> **Book a spring season tune-up before the rush:**
> ✔ Full spring and cable inspection
> ✔ Roller and track lubrication
> ✔ Safety sensor alignment check
> ✔ Balance test
>
> **$X for existing customers | Book before March 15 for priority scheduling**
>
> [Book Your Tune-Up — Link]
>
> — [Company Name]

**Fall Campaign — SMS (August/September):**
> "Fall tune-up time, [First Name]! Cold weather = more broken springs. Our fall inspection special includes spring check, cable inspection, lubrication, and safety sensor test — $X for existing customers. Book before we fill up: [link] 🍂 — [Company Name]"

---

### 8.5 New Door Consultation Templates

**Email — Day 1 Education (Post-Inquiry):**
Subject: "Choosing the Right Garage Door — What You Need to Know"
> Hi [First Name],
>
> Thanks for reaching out about a new garage door! This is one of the best curb appeal investments you can make — and with the right information, you'll make a decision you're happy with for years.
>
> **The 3 things that matter most:**
>
> **1. Insulation (R-value)**
> If your garage is attached to your home, insulation matters for energy efficiency and noise reduction. R-12 or R-18 insulated doors can meaningfully reduce heating/cooling costs.
>
> **2. Style**
> Traditional raised-panel steel doors are the most affordable and durable. Carriage-house style (with crossbuck and decorative hardware) adds curb appeal without the maintenance of real wood. Modern flush-panel designs are popular in contemporary homes.
>
> **3. Material**
> Steel is the most popular — it's durable, low-maintenance, and available in dozens of colours. Wood composite offers the look of real wood with better weather resistance. Glass accent panels are popular for modern/contemporary homes.
>
> **Our consultation is free and takes about 30 minutes at your home.** We'll take measurements, walk through options, and give you a written quote before we leave.
>
> [Book Your Free Estimate — Link]
>
> Questions? Text us at [phone].
>
> — [Company Name]

---

## Section 9: Review Generation Strategy

### 9.1 Timing Science for Garage Door Reviews

The emotion window in garage door service is unique. Unlike other home services where satisfaction is gradual, garage door customers feel **immediate relief** — they're no longer stranded, late for work, or stressed about security.

**Best review request timing:**
- **Emergency repair:** 18–24 hours after completion (enough time to process, not so long the emotion fades)
- **Scheduled service:** 36–48 hours (lower initial emotion peak; give time for "it's still working" confirmation)
- **New door installation:** 48–72 hours (let them enjoy the curb appeal, show neighbours)

### 9.2 Review Platform Priority

| Priority | Platform | Why |
|---|---|---|
| 1 | Google Business Profile | Drives LSA rank and organic map rank — most important |
| 2 | HomeAdvisor / Angi | For companies running Angi leads |
| 3 | Facebook | Social proof, especially for referral and local audience |
| 4 | Yelp | Market-dependent |

### 9.3 Review Request Flow

1. **Job completed → Move to "Job Completed" stage**
2. **T+2 hours:** Warm thank-you SMS (no ask yet)
3. **T+22 hours:** Direct review request SMS with Google link
4. **T+24 hours:** Review request email (if SMS not clicked)
5. **T+72 hours:** If no review, final gentle reminder email
6. **Review confirmed → Referral workflow trigger**

### 9.4 Negative Review Prevention

Before the public review request fires, trigger an internal satisfaction check:

**T+6 hours — Internal Satisfaction SMS:**
> "Hi [First Name], quick check-in from [Company Name] — is everything working great with your garage door? Any concerns at all? Just reply here. — [Company Name]"

If customer replies with a concern → alert owner immediately → issue resolved before public review request fires.

---

## Section 10: Annual Maintenance / Tune-Up Campaign

### 10.1 Campaign Architecture

**Purpose:** Create predictable, recurring revenue from the existing customer base; reduce emergency call volume by catching issues early.

**Segments:**
1. **Past Emergency Customers** — Highest priority; spring-break history means higher recurrence risk
2. **Past Scheduled Service Customers** — Medium priority; moderate recurrence
3. **New Door Installation Customers** — Annual safety check pitch; protect their investment
4. **Dormant Customers (no contact 12+ months)** — Re-engagement campaign

### 10.2 Tune-Up Package Components (what to include in the snapshot)

Standard tune-up offer for snapshot should include:
- Torsion spring and extension spring visual inspection
- Cable fraying check
- Roller wear assessment (steel or nylon)
- Track alignment check
- Safety sensor test (reversal test)
- Auto-reverse force test
- Opener chain/belt/screw lubrication
- Weather seal visual inspection
- Balance test (door should hold at 3–4 feet when manually released)
- Keypad and remote test

**Upsell from tune-up:** If opener is 10+ years, offer same-day smart opener upgrade. If springs are near end-of-life, offer proactive spring replacement before failure.

### 10.3 Campaign Calendar (Built Into Snapshot)

| Month | Campaign | Audience |
|---|---|---|
| February | Pre-Spring Tune-Up Push | All past customers — spring focus |
| March | Last Chance — Spring Season Availability | Non-responders from February |
| August | Fall Tune-Up Booking Opens | All past customers |
| September | Fall Season Final Push | Non-responders from August |
| November | End-of-Year Safety Check | Dormant customers (re-engagement) |
| December | Holiday Gift: Free Lubrication with Opener Service | Past opener customers |

---

## Section 11: Smart Opener & Home Automation Upsell System

### 11.1 Upsell Trigger Points

- Opener age tagged as 10+ years during service visit
- Tech notes: "Opener serviced — candidate for smart upgrade"
- Customer asks about smart home during call
- New door installation completed (bundle opener upgrade)
- Safety inspection reveals opener out of compliance with UL 325 standards

### 11.2 Smart Opener Lineup (Build Into Email Templates)

| Model | Features | Installed Price Range |
|---|---|---|
| LiftMaster 84501 | myQ, battery backup, camera, WiFi | $X–$X |
| Chamberlain B2405 | myQ, belt drive, quiet | $X–$X |
| Genie 7155-TKV | Aladdin Connect, direct-to-drive | $X–$X |
| LiftMaster WLED | Commercial-grade, LED, camera | $X–$X |

*(Client fills in pricing during snapshot setup)*

### 11.3 Smart Opener Workflow Sequence

**Day 7:** Education SMS (as described in Section 5.6)
**Day 7:** Education email with feature comparison
**Day 14:** Follow-up SMS with scheduling CTA
**Day 21:** Final offer with bundle discount (if booked with tune-up)
**Day 30:** Removed from upsell sequence; tagged for next campaign cycle

---

## Section 12: What Makes This Snapshot Stand Out

This section is for the 1app sales pitch — use it when presenting to garage door prospects.

### 12.1 Industry-Specific vs. Generic

Every other home services snapshot uses language like "New Lead → Appointment → Won." The 1app Garage Door Snapshot uses:
- "Emergency Inbound → Tech Dispatched → On Site Diagnosing → Quote Presented → Job Completed"
- Door issue type capture at intake
- Opener age tracking for smart upgrade targeting
- Seasonal campaigns built around torsion spring failure cycles

A garage door owner looks at this snapshot and immediately thinks: *"These people know my business."*

### 12.2 The Revenue Stack

Most garage door companies run on one revenue event per customer. The 1app snapshot creates a **5-touchpoint revenue stack** per customer:

1. **Initial repair/service** — Primary job
2. **Review generation** — Fuels LSA rank, drives more inbound
3. **Smart opener upsell** — Secondary revenue event ($300–$800)
4. **Semi-annual safety check** — Recurring revenue touch
5. **Annual tune-up** — Prevents emergency, captures recurring spend
6. **Referral generation** — New customer from existing customer

That's potentially 3–5 revenue events per customer over 2 years from a single intake.

### 12.3 Emergency Response Architecture

No other snapshot in the market has a purpose-built emergency response workflow that:
- Responds within 60 seconds via SMS
- Collects issue type and address before human intervention
- Creates internal dispatch task automatically
- Keeps the conversation in a single SMS thread until resolved

This is the workflow that keeps the owner from losing a $300+ job every time they're on another call.

### 12.4 The Seasonal Campaign Engine

The spring and fall tune-up campaigns are a **built-in recurring revenue machine.** A garage door company with 500 past customers running a tune-up campaign at $X per tune-up generates meaningful revenue in weeks — revenue that didn't exist without the system.

### 12.5 Commercial Pipeline Differentiation

No generic home services snapshot has a commercial/property manager pipeline. The 1app snapshot includes a separate commercial pipeline with:
- Multi-door assessment workflow
- Formal proposal stage
- Annual maintenance contract pitch
- Property manager-specific communication cadence

This positions the garage door company for commercial accounts that most competitors don't systematically pursue.

---

## Section 13: Snapshot Build Checklist

### GHL Elements Required

**Pipelines:**
- [ ] Emergency Repair Pipeline (7 stages)
- [ ] Scheduled Service Pipeline (7 stages)
- [ ] New Door Installation Pipeline (10 stages)
- [ ] Commercial Pipeline (7 stages)

**Custom Fields:**
- [ ] Door Issue Type (dropdown)
- [ ] Door Brand (dropdown)
- [ ] Opener Brand (dropdown)
- [ ] Opener Age (dropdown)
- [ ] Door Type (dropdown)
- [ ] Smart Opener Offered (yes/no)
- [ ] Lead Source (dropdown)
- [ ] Tech Name (text)
- [ ] Job Completion Date (date)
- [ ] Door Style (dropdown)
- [ ] Insulation R-Value (dropdown)
- [ ] Commercial: Number of Doors (number)
- [ ] Annual Tune-Up Status (dropdown)

**Custom Tags:**
- [ ] Emergency Customer
- [ ] Scheduled Service Customer
- [ ] New Door Customer
- [ ] Commercial Account
- [ ] Smart Opener Candidate (Opener 10+)
- [ ] Review Requested
- [ ] 5 Star Review
- [ ] Referral Generated
- [ ] Tune-Up Completed
- [ ] Spring Campaign 2025
- [ ] Fall Campaign 2025
- [ ] Dormant (12+ months)

**Calendars:**
- [ ] Emergency Dispatch Calendar (internal)
- [ ] Scheduled Service Calendar (customer-facing)
- [ ] Free Estimate — New Door (customer-facing)
- [ ] Commercial Site Assessment (customer-facing)

**Workflows (9 total):**
- [ ] WF01 — Emergency Missed Call Response
- [ ] WF02 — Booking Confirmation & Reminder
- [ ] WF03 — Post-Job Follow-Up & Review (Emergency)
- [ ] WF04 — Post-Job Follow-Up & Review (Scheduled)
- [ ] WF05 — New Door Installation Nurture
- [ ] WF06 — Smart Opener Upsell
- [ ] WF07 — Seasonal Tune-Up Campaign (Spring)
- [ ] WF08 — Seasonal Tune-Up Campaign (Fall)
- [ ] WF09 — Referral Generation
- [ ] WF10 — Commercial / Property Manager Nurture

**Forms (4 total):**
- [ ] Emergency Repair Intake
- [ ] Scheduled Service Request
- [ ] Free Estimate — New Door
- [ ] Commercial Service Inquiry

**Email Templates (9 total):**
- [ ] Booking Confirmation
- [ ] Post-Service Thank You & Review
- [ ] Smart Opener Upsell Email
- [ ] New Door Education Day 1
- [ ] New Door Social Proof Day 7
- [ ] New Door Financing Day 14
- [ ] Spring Tune-Up Campaign
- [ ] Fall Tune-Up Campaign
- [ ] Commercial Maintenance Contract Offer

**SMS Templates (15+ total):**
- [ ] Missed Call — Immediate
- [ ] Missed Call — 5 min follow-up
- [ ] Emergency Confirmed — Tech Dispatched
- [ ] Tech 15-min ETA
- [ ] Booking Confirmation
- [ ] 24hr Reminder
- [ ] 1hr Reminder
- [ ] Post-Service Thank You
- [ ] Review Request
- [ ] Smart Opener Upsell
- [ ] 6-Month Safety Check
- [ ] Annual Tune-Up Reminder
- [ ] Spring Campaign
- [ ] Fall Campaign
- [ ] Referral Ask

**Landing Pages / Funnels:**
- [ ] Emergency Repair Landing Page (with form + phone)
- [ ] New Door Installation Landing Page (with gallery + estimate form)
- [ ] Seasonal Campaign Landing Page
- [ ] Commercial Services Landing Page

**Automation — Reporting Dashboard:**
- [ ] Total Leads This Month
- [ ] Emergency vs. Scheduled Split
- [ ] Review Requests Sent / Reviews Received Rate
- [ ] Smart Opener Upsell Conversion Rate
- [ ] Tune-Up Campaign Bookings
- [ ] Revenue by Pipeline

---

## Section 14: Onboarding Checklist (1app Client Setup)

When a garage door company signs up for 1app, the onboarding sequence should include:

**Week 1 — Foundation:**
- [ ] Connect their GHL phone number (or provision new number)
- [ ] Set up Missed Call Text Back with their business name
- [ ] Configure business hours and emergency after-hours response
- [ ] Import existing customer list (CSV) and tag appropriately
- [ ] Set up Google Business Profile review link
- [ ] Configure booking calendar with tech availability

**Week 2 — Workflows Live:**
- [ ] Activate Emergency Response workflow (WF01)
- [ ] Activate Booking Confirmation & Reminder workflow (WF02)
- [ ] Activate Post-Job Review workflow (WF03 + WF04)
- [ ] Train owner on pipeline stage movement (how to move a deal)
- [ ] Test full flow: missed call → response → booking → confirmation

**Week 3 — Revenue Workflows:**
- [ ] Activate Smart Opener Upsell workflow (WF06)
- [ ] Set up seasonal campaign dates for next cycle
- [ ] Import past customer list into tune-up campaign segment
- [ ] Launch referral workflow

**Week 4 — Review:**
- [ ] Check missed call response rate (should be under 60 seconds)
- [ ] Review first week of booking confirmations
- [ ] Review dashboard metrics
- [ ] Tune any workflow triggers based on actual call volume

---

## Section 15: Pricing Recommendations for 1app

### Snapshot-Only (White Label Sale)
- **One-time snapshot license:** $497–$997 for agencies purchasing to resell

### Managed Service Tiers (Monthly Recurring)

| Tier | Price | Included |
|---|---|---|
| Starter | $197/mo | Missed Call Text Back, Emergency Response, Booking Confirmation, Review Request |
| Growth | $397/mo | All Starter + Smart Opener Upsell, New Door Nurture, Seasonal Campaigns, Referral System |
| Full System | $597/mo | All Growth + Commercial Pipeline, Custom Landing Pages, Monthly Performance Report, 1hr onboarding support |

**Setup Fee:** $299–$497 (one-time) to cover snapshot installation and onboarding

**Upsell opportunities:**
- Google Ads management: $500–$1,500/mo
- LSA setup + management: $300–$500/mo
- Custom landing page builds: $497–$997 one-time
- Content/social media: $197–$397/mo

---

## Appendix A: Garage Door Industry Glossary (for Templates & Comms)

| Term | Definition |
|---|---|
| Torsion spring | Horizontal spring mounted above the door; most common spring type; typical failure point |
| Extension spring | Springs on either side of the door; older residential doors; lower cycle rating |
| Cable | Steel wire that winds around drums; works with torsion spring for lifting |
| Drum | Cylindrical spool at each end of the torsion bar; cable winds around it |
| Torsion bar | Horizontal steel shaft that transfers spring torque to the drums |
| Track | Vertical and horizontal rails that guide the door rollers |
| Roller | Wheels that run inside the track; steel or nylon; wear over time |
| Opener | Electric motor unit that automates door movement; chain, belt, or screw drive |
| Chain drive | Most common opener type; durable but louder; good for detached garages |
| Belt drive | Quieter opener; rubber belt; preferred for attached garages near bedrooms |
| Screw drive | Slower, quieter, fewer moving parts; good for extreme climates |
| Safety sensor | Photoelectric sensors at floor level; stop/reverse door if beam is broken |
| Auto-reverse | Safety feature; door reverses if it contacts an obstacle during closing |
| UL 325 | Safety standard for garage door openers; set by Underwriters Laboratories |
| myQ | LiftMaster/Chamberlain app platform for smart opener connectivity |
| LiftMaster 84501 | Popular residential smart opener with camera, battery backup, and myQ |
| Aladdin Connect | Genie's smart opener connectivity platform |
| Panel replacement | Replacing a single damaged section of the door (usually from vehicle impact) |
| Sectional door | Commercial door that opens in horizontal sections; most common commercial type |
| Roll-up door | Commercial door that rolls up into a coil; common for self-storage and service bays |
| Dock door | Sectional door at loading dock height; used by warehouses and distribution centers |
| Counterbalance | The spring system that balances the door's weight |
| Cycle | One complete open-and-close of the door; springs rated by cycle count |
| High-cycle spring | Springs rated 25,000+ cycles; commercial or high-use residential upgrade |
| Balance test | Testing if spring tension is properly set; door should hold at 3–4 feet when released |
| Weather seal | Rubber seal at bottom and sides of door; keeps out water, pests, and drafts |
| Keypad | External numeric keypad for code-based entry |
| Wall button | Interior push button to operate opener |
| Force setting | Opener setting that controls how much force is applied when raising/lowering |

---

## Appendix B: Competitive Research Notes

### What GHL Marketplace Snapshots Typically Include (Generic)
- 3-stage pipeline (New → Appointment → Won/Lost)
- Missed call text back (1 message)
- Booking confirmation (1 SMS + 1 email)
- 1–2 follow-up messages
- Basic review request

### What They're Missing (1app Advantage)
- Industry-specific pipeline stage names using garage door language
- Emergency vs. scheduled split workflow with different urgency tiers
- Door issue type capture at intake (torsion spring, cable, opener, etc.)
- Opener age tracking for automated smart upgrade sequence
- Seasonal campaigns triggered by months (spring and fall)
- Annual tune-up reminder (12-month post-service automation)
- Commercial/property manager pipeline
- Referral generation post-review confirmation
- Pre-season inbound call surge management
- Tech dispatch internal notification workflow
- Negative review prevention (internal satisfaction check before public request)

---

*Document prepared by 1app / Maximus | July 2026*
*Ready for GHL snapshot build — all workflows, pipelines, forms, templates, and custom fields defined above.*
