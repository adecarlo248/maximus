# 🐛 1app GHL Snapshot Research: Pest Control Industry
**Build Document — Agency Use Only**
**Version:** 1.0 | **Date:** July 2026 | **Prepared for:** 1app Technologies Inc.

---

## Table of Contents

1. [Industry Overview & Opportunity](#1-industry-overview--opportunity)
2. [Pest Control Business Pain Points](#2-pest-control-business-pain-points)
3. [Competitive Snapshot Landscape](#3-competitive-snapshot-landscape)
4. [Pipeline Architecture](#4-pipeline-architecture)
5. [Workflow Architecture](#5-workflow-architecture)
6. [SMS & Email Template Library](#6-sms--email-template-library)
7. [Lead Sources & Intake Strategy](#7-lead-sources--intake-strategy)
8. [Booking Flow Design](#8-booking-flow-design)
9. [Recurring Service Plan Engine (Highest LTV)](#9-recurring-service-plan-engine-highest-ltv)
10. [Seasonal Campaign Calendar](#10-seasonal-campaign-calendar)
11. [Commercial & Property Manager Track](#11-commercial--property-manager-track)
12. [Review Generation System](#12-review-generation-system)
13. [Snapshot Differentiation Strategy](#13-snapshot-differentiation-strategy)
14. [Full Build Checklist](#14-full-build-checklist)
15. [Custom Fields & Tags Reference](#15-custom-fields--tags-reference)

---

## 1. Industry Overview & Opportunity

### Why Pest Control is a Prime GHL Niche

The pest control industry is a **$26 billion+ market in North America** with several structural characteristics that make it ideal for a GHL snapshot:

- **Emergency-driven demand:** Infestations don't schedule themselves. When a homeowner sees bed bugs or discovers a termite swarm, they call immediately — and call whoever answers first or has the best reviews.
- **Recurring revenue model:** The real money isn't in one-time exterminations — it's in quarterly general pest control (GPC) plans, monthly mosquito barrier sprays, and annual termite prevention plans. These recurring service agreements are the lifeblood of any mid-to-large pest control operator.
- **Extremely high missed call loss rate:** Industry research consistently shows 60–75% of pest control callers who hit voicemail do not leave a message — they call the next company on the list. Missed call text back is not a "nice to have" for this niche; it is the single highest-ROI automation possible.
- **Seasonal spikes with predictable patterns:** Spring (ants, wasps, termite swarms), summer (mosquitoes, fleas), fall (rodents seeking warmth, stink bugs), winter (exclusion, rodents) — each season has a campaign playbook.
- **Underserved by legacy software:** Most pest control operators are running on ServicePro, PestPac, or QuickBooks with zero marketing automation. They are not running CRM sequences, post-treatment follow-ups, or review campaigns. The bar is low, and the upside is massive.
- **Google LSA dominance:** Pest control is one of the top-performing categories for Google Local Services Ads — operators need a system to instantly follow up on LSA leads before competitors do.

### Target Customer Profile

**Primary:** Independent pest control operators, regional operators with 2–15 technicians, new companies wanting to build recurring plan revenue from day one.

**Secondary:** Mid-size operators ($1M–$5M revenue) wanting to modernize and reduce no-shows.

**Tertiary:** Franchise operators (Orkin, Terminix licensees) needing supplemental automation their corporate platform doesn't cover.

---

## 2. Pest Control Business Pain Points

These are the real complaints from pest control operators. Build every workflow around solving these.

### 2.1 Missed Calls = Lost Revenue
**Pain:** An infestation call at 7 PM hits voicemail. The homeowner calls the next result on Google. That's a $400–$2,000 job gone permanently.
**Solution:** Missed Call Text Back fires within 60 seconds. Captures the lead. Books the appointment before the competitor even answers.

### 2.2 Recurring Plan Churn
**Pain:** Technician does a great one-time ant treatment. Customer is satisfied. Company never calls again. Customer doesn't renew. Six months later, the ants are back and they're calling a different company.
**Solution:** Automatic post-treatment upsell sequence. Get them on the quarterly general pest control plan while their pain is still fresh (within 24–72 hours of service).

### 2.3 Seasonal Outbreak Volume Spikes
**Pain:** Every spring, the phones ring off the hook with ant and wasp calls. Every fall, rodent exclusion requests spike. Companies have no proactive system — they're purely reactive.
**Solution:** Pre-built seasonal outbreak campaigns hit the entire customer database 2–3 weeks before the expected spike, booking appointments in advance and smoothing technician schedules.

### 2.4 Emergency Call Volume Management
**Pain:** Bed bug calls, active wasp nest emergencies, and cockroach infestations all want same-day or next-day service. These calls overwhelm schedulers, disrupt route efficiency, and cannibalize planned stops.
**Solution:** Emergency intake pipeline with dedicated "Emergency/Same-Day" stage, automated priority SMS, and calendar logic for emergency slots.

### 2.5 No-Shows & Last-Minute Cancellations
**Pain:** Technician drives to a job site — customer forgot, no answer, locked gate. That's 45–90 minutes of technician time plus fuel wasted. In pest control, technician time is the primary cost driver.
**Solution:** 3-touch appointment confirmation sequence: 48-hour, 24-hour, and 2-hour reminders. Two-way SMS confirmations. Auto-reschedule trigger if no confirmation received.

### 2.6 Technician Routing Inefficiency
**Pain:** Sales rep books appointments without regard for technician zones. Technicians are crisscrossing service areas, adding unnecessary drive time and reducing daily stop counts.
**Solution:** GHL calendar booking logic with zone-based availability (Custom Fields: Service Zone A/B/C), allowing geographic routing by technician assignment.

### 2.7 Upselling One-Time to Recurring
**Pain:** The "impulse buy" pest control customer just wants their current problem solved. They're not thinking about a recurring service plan until you remind them at the right moment.
**Solution:** Post-service workflow triggers at 24 hours, 72 hours, and 7 days post-treatment. Frame the upsell as "protecting the investment we just made" — not as a sales pitch.

### 2.8 Review Generation Failure
**Pain:** Pest control operators provide excellent service but never ask for reviews at the right moment. The customer who called in a panic, got their bed bug issue resolved, and is now relieved is the BEST review candidate — but the window is 24–48 hours post-resolution.
**Solution:** Post-treatment review request workflow timed precisely at customer peak relief (24 hours after service confirmation). Two-step: text first, email follow-up if no click.

### 2.9 Property Manager & Commercial Account Management
**Pain:** Commercial accounts (restaurants, hotels, multi-family units, food processing, schools) require service logs, compliance documentation, and consistent monthly visits. Most pest control operators manage these manually.
**Solution:** Dedicated commercial pipeline with monthly service workflow, compliance report automation trigger, and property manager contact loop.

### 2.10 Re-Engagement of Lapsed Customers
**Pain:** One-time treatment customers from 6–18 months ago are forgotten. They're either having new pest problems and calling competitors, or they haven't thought about pest prevention at all.
**Solution:** 6-month and 12-month re-engagement campaigns. "We haven't heard from you in a while — here's what's active in your area this season."

---

## 3. Competitive Snapshot Landscape

### What Exists on the Market

Most GHL snapshots marketed to pest control fall into two categories:

**Generic Home Services Snapshots** (re-skinned plumber/HVAC templates):
- Missed call text back
- Basic appointment booking
- Single pipeline
- No industry language
- No recurring plan logic
- No seasonal campaigns
- No commercial/property manager track

**Entry-Level Pest Control Snapshots** (seen on HighLevel Marketplace and SaaS agency Skool groups):
- Slightly better terminology ("pest inspection" vs. "service call")
- Usually 1–2 pipelines
- Basic appointment confirmation sequence
- No post-treatment upsell logic
- No termite/specialty service separation
- No bed bug or heat treatment workflow
- No Integrated Pest Management (IPM) language for commercial clients
- No seasonal campaign templates

### What's Missing in Every Current Snapshot

This is the gap 1app fills:

1. **Dedicated emergency/one-time vs. recurring plan pipeline split** — most snapshots treat all jobs the same
2. **Recurring service plan enrollment workflow** — the highest-LTV conversion in pest control
3. **Post-treatment upsell timing logic** — the 24–72 hour window is critical and universally ignored
4. **Termite inspection + bait station follow-up workflow** — termite is a separate service with a $1,500–$5,000 ticket
5. **Bed bug heat treatment workflow** — multiple-visit service requiring specific communication cadence
6. **Seasonal outbreak campaign calendar** — pre-built, ready to deploy each quarter
7. **Commercial/property manager pipeline** — entirely separate track with compliance language
8. **Zone-based technician routing logic** via custom fields
9. **Review generation timed to customer emotional peak**
10. **Real estate/pre-sale inspection pipeline** — agents need quick turnaround and specific report language

---

## 4. Pipeline Architecture

### Pipeline 1: General Pest Control — Residential (One-Time & Recurring)

This is the primary pipeline handling 70–80% of inbound volume.

```
[NEW LEAD / INQUIRY]
        ↓
[CONTACTED — Speed-to-Contact (<5 min)]
        ↓
[INSPECTION SCHEDULED]
        ↓
[TREATMENT COMPLETED]
        ↓
[RECURRING PLAN OFFERED]
        ↓
[PLAN ENROLLED] ← WIN ★
        ↓
[ONE-TIME CLOSED] ← WIN (with upsell sequence active)
        ↓
[LOST — DNQ / Price / Competitor]
```

**Stage Definitions:**

| Stage | Description | Automation Trigger |
|-------|-------------|-------------------|
| **New Lead / Inquiry** | Form submission, LSA lead, missed call text back reply, web chat | Tag: `new-lead`; assign to intake rep |
| **Contacted** | Two-way SMS exchange initiated; lead responded | Tag: `contacted`; start speed-to-contact timer |
| **Inspection Scheduled** | Booking confirmed in GHL calendar | Confirmation sequence fires |
| **Treatment Completed** | Technician marks job done in GHL | Post-treatment follow-up workflow fires |
| **Recurring Plan Offered** | Rep or automation sent plan pitch | Wait 48h, send follow-up |
| **Plan Enrolled** | Customer confirmed recurring plan | Tag: `recurring-plan`; add to plan management pipeline |
| **One-Time Closed** | Paid one-time only | Enter 90-day re-engagement workflow |
| **Lost** | No response / competitor / unaffordable | Enter 6-month win-back campaign |

---

### Pipeline 2: Termite & Specialty Services

Termite inspection → treatment → monitoring is a high-ticket, multi-step service track requiring its own pipeline.

```
[TERMITE INSPECTION INQUIRY]
        ↓
[INSPECTION SCHEDULED]
        ↓
[INSPECTION COMPLETE — Report Delivered]
        ↓
[TREATMENT PROPOSAL SENT]
        ↓
[TREATMENT APPROVED — Work Ordered]
        ↓
[LIQUID TREATMENT / FUMIGATION / BAIT STATION INSTALLED]
        ↓
[MONITORING PLAN ENROLLED] ← WIN ★
        ↓
[ANNUAL INSPECTION RENEWAL ENROLLED] ← WIN ★
        ↓
[CLOSED — ONE-TIME ONLY]
        ↓
[LOST]
```

**Service types tracked in this pipeline:**
- Subterranean termite treatment (liquid barrier)
- Drywood termite fumigation (tent fumigation / whole-structure)
- Bait station installation & monitoring (Sentricon, Advance, etc.)
- Wood-destroying organism (WDO) inspection for real estate
- Termite bond/warranty enrollment

**Custom Fields:**
- `Termite Service Type` (dropdown: inspection / liquid treatment / fumigation / bait station / WDO report)
- `Treatment Completion Date`
- `Warranty Expiration Date`
- `Annual Renewal Due Date`

---

### Pipeline 3: Bed Bug Track

Bed bug treatment is a high-anxiety, multi-visit service. Customers are emotionally stressed and need constant communication.

```
[BED BUG INQUIRY / EMERGENCY]
        ↓
[SAME-DAY / NEXT-DAY INSPECTION BOOKED]
        ↓
[INSPECTION COMPLETE — Infestation Confirmed]
        ↓
[TREATMENT QUOTE APPROVED]
        ↓
[HEAT TREATMENT / CHEMICAL TREATMENT SCHEDULED]
        ↓
[TREATMENT SESSION 1 COMPLETE]
        ↓
[FOLLOW-UP INSPECTION SCHEDULED (14–21 Days)]
        ↓
[TREATMENT CONFIRMED SUCCESSFUL — All Clear] ← WIN ★
        ↓
[MONITORING PLAN OFFERED]
```

**Key differentiator:** Bed bug customers are extremely anxious. Every stage transition should trigger a reassurance SMS/email. Use empathetic, calm language. No generic pest control copy.

**Service types:**
- Bed bug heat treatment (whole-room or whole-home)
- Chemical/residual treatment (multi-visit)
- K-9 detection inspection
- Encasements and monitoring traps

---

### Pipeline 4: Commercial / Property Manager

```
[COMMERCIAL INQUIRY]
        ↓
[SITE ASSESSMENT SCHEDULED]
        ↓
[PROPOSAL DELIVERED]
        ↓
[CONTRACT SIGNED — SERVICE AGREEMENT ACTIVE] ← WIN ★
        ↓
[MONTHLY SERVICE ACTIVE]
        ↓
[COMPLIANCE REPORT DELIVERED]
        ↓
[ANNUAL CONTRACT RENEWAL]
```

**Account types in commercial track:**
- Restaurants / food service
- Hotels / hospitality
- Multi-family / apartment complexes
- Schools / daycares
- Food processing / warehousing
- Retail / office buildings
- Healthcare facilities

---

### Pipeline 5: Recurring Service Plan Management

This is the **plan retention and renewal pipeline** — separate from acquisition. Every enrolled recurring customer lives here.

```
[PLAN ACTIVE — Quarterly / Monthly]
        ↓
[SERVICE UPCOMING — 1 Week Out]
        ↓
[SERVICE COMPLETED — This Quarter]
        ↓
[FEEDBACK REQUESTED]
        ↓
[PLAN RENEWAL DUE — 30 Days]
        ↓
[RENEWAL CONFIRMED] ← WIN ★
        ↓
[CHURNED — Needs Win-Back Campaign]
```

**Plan types:**
- General Pest Control (GPC) Quarterly — 4x/year
- GPC Monthly — 12x/year (premium)
- Mosquito Barrier Spray — Monthly, April–October
- Rodent Exclusion Monitoring — Quarterly
- Termite Monitoring / Bond — Annual
- Bed Bug Monitoring — Quarterly

---

### Pipeline 6: Real Estate / Pre-Sale Inspection Track

Real estate agents and sellers need fast turnaround on WDO (Wood-Destroying Organism) reports and general pest inspections for closings.

```
[REAL ESTATE INSPECTION REQUEST]
        ↓
[INSPECTION BOOKED — Within 48 Hours]
        ↓
[INSPECTION COMPLETE]
        ↓
[REPORT DELIVERED (same day / next morning)]
        ↓
[TREATMENT RECOMMENDED — Quote Sent]
        ↓
[TREATMENT BOOKED / DECLINED]
        ↓
[AGENT REFERRAL NETWORK — Added to nurture]
```

---

## 5. Workflow Architecture

### Workflow 1: Missed Call Text Back — Emergency Mode

**Trigger:** Incoming call → not answered within 3 rings

**Sequence:**
- **Immediately (0 min):** SMS fires to caller
  > *"Hey, sorry we missed your call! This is [Company Name]. Pest problem? We can help fast. What's going on? 🐛"*

- **If no reply in 15 minutes:** Second SMS
  > *"Still here if you need us. What pest are you dealing with? We do same-day service for emergencies."*

- **If reply received:** Trigger lead intake form link + booking calendar
- **Tag lead:** `missed-call-recovered` or `missed-call-lost` depending on response

**Performance target:** 40–60% missed call recovery rate

---

### Workflow 2: New Lead Speed-to-Contact (LSA / Web Form / Chat)

**Trigger:** New contact created via LSA integration, website form, or web chat

**Sequence:**
- **Immediately (0 min):** Auto-SMS
  > *"Hi [First Name]! Got your message about a pest issue. What are you dealing with and what's your address? We'll get you taken care of. — [Company Name]"*

- **Immediately (0 min):** Internal notification to assigned rep (push notification + task assignment)

- **3 minutes:** If no internal action taken, escalation ping to manager

- **5 minutes:** If no reply from lead, follow-up SMS
  > *"We have openings today and tomorrow. Want us to pop by for a quick inspection? Takes about 20 minutes."*

- **1 hour:** If still no reply, email with booking link

- **3 hours:** If no booking, final SMS attempt
  > *"Last message from us today — if you're still dealing with [pest type], we're here. Book at [link] or call [number]."*

**Performance target:** First contact within 5 minutes = 78% higher conversion vs. 30+ minutes

---

### Workflow 3: Appointment Confirmation Sequence

**Trigger:** Appointment booked in GHL calendar

**Sequence:**
- **Immediately:** Booking confirmation SMS + email
  - SMS: *"Confirmed! Your pest inspection is set for [Day], [Date] between [Time Window]. Our tech will call/text 30 min before arrival. Reply STOP to cancel or RESCHEDULE to change. — [Company Name]"*
  - Email: Full confirmation with prep instructions (clear clutter, secure pets, etc.)

- **48 hours before:** Reminder SMS
  > *"Reminder: Your pest service is in 2 days — [Day] between [Time Window]. Need to make changes? Reply RESCHEDULE or call [Number]."*

- **24 hours before:** Reminder + prep instruction SMS
  > *"Your technician is coming tomorrow! Quick prep: remove pet dishes from treated areas, clear under sinks, keep kids/pets out for 2–4 hours post-treatment. See you [Day]! — [Company]"*

- **2 hours before:** Day-of reminder
  > *"Your tech is on their way today! Estimated arrival: [Time Window]. Any access notes we should know? Reply here."*

- **If no confirmation reply received by 24-hour mark:** Trigger "unconfirmed appointment" internal task — rep calls to confirm

---

### Workflow 4: Post-Treatment Follow-Up + Recurring Plan Upsell

**Trigger:** Job status updated to "Treatment Completed" (technician marks complete)

**Sequence:**
- **1 hour after completion:** Thank you SMS
  > *"Treatment complete! Thanks for trusting [Company Name] with your home. The treatment is now working — give it 5–7 days for full effect. Any questions? Reply here."*

- **24 hours:** Check-in SMS + first upsell mention
  > *"Hi [First Name]! How's everything looking post-treatment? Any pest activity? Also — if you want to make sure they don't come back, ask us about our Quarterly Protection Plan. We'll keep your home pest-free all year. Worth a quick chat?"*

- **72 hours:** Plan pitch SMS with offer
  > *"[First Name], most pest problems come back within 3–6 months without a protection plan. Our Quarterly Service keeps you covered year-round for less than a cup of coffee a day. Want me to lock in a rate for you? Reply YES and I'll send details."*

- **7 days:** Final upsell attempt via email
  > Subject: *"One more thing before [pest type] season hits..."*
  > Body: Seasonal context + plan benefits + clear CTA to book free plan consultation

- **If no enrollment:** Tag `upsell-declined`, enter 90-day re-engagement

---

### Workflow 5: Recurring Plan Renewal Sequence

**Trigger:** Custom Field `Plan Renewal Date` = 30 days from today

**Sequence:**
- **30 days before renewal:** Renewal announcement email
  > *"Your annual pest protection plan renewal is coming up. We'll automatically schedule your next quarterly treatment soon. Same great coverage. Want to review your plan or add services?"*

- **14 days before:** SMS check-in
  > *"Hi [First Name]! Your quarterly service is coming up in 2 weeks. Any new pest concerns we should know about before the visit?"*

- **7 days before:** Booking confirmation for renewal visit

- **If renewal NOT booked by 7-day mark:** Escalate to rep with task: "Call to confirm renewal"

- **After service complete:** Retention SMS
  > *"Another year of protection locked in! Thanks for sticking with [Company]. Let us know if you ever notice anything between visits — that's what we're here for."*

---

### Workflow 6: Bed Bug Anxiety Management Sequence

**Trigger:** Lead tagged `bed-bug`

**Tone:** Calm, empathetic, clinical. These customers are stressed. No humor. No generic pest language.

**Sequence:**
- **Inquiry received:** Immediate response
  > *"Hi [First Name]. Thank you for reaching out. We understand bed bug situations are urgent and stressful. We specialize in complete bed bug elimination. Can I ask — are you seeing active bugs or just bites/evidence?"*

- **Post-inspection (same day):** Report summary SMS
  > *"We completed your inspection. [Tech Name] has documented findings and will call you within the hour to walk through treatment options. We'll take care of this."*

- **Post-treatment Session 1 (24 hours):** Reassurance SMS
  > *"Day 1 post-treatment check-in. You may see increased activity in the first 48–72 hours — that's normal and means the treatment is working. Keep bedding clear and don't vacuum treated areas yet. Questions? Reply here."*

- **Day 7:** Mid-cycle check
  > *"One week post-treatment. Activity should be noticeably reduced. Any concerns? We want to know."*

- **Day 14–21:** Follow-up inspection confirmation

- **All-clear confirmation:** Relief + review request
  > *"Great news — your follow-up inspection came back clear. Your home is bed bug free. We're glad we could help. Would you mind sharing your experience? It helps other families in your situation find us."* → Review link

---

### Workflow 7: Seasonal Outbreak Campaign

**Trigger:** Manual send (or date-based trigger) 3 weeks before seasonal peak

**Segments:**
- All customers → full database blast
- Recurring plan customers → early booking priority SMS
- Lapsed customers (no service in 12+ months) → win-back angle

*(See Section 10 for full seasonal campaign scripts)*

---

### Workflow 8: Review Generation

**Trigger:** Job status = "Treatment Completed" AND service type ≠ "Emergency/First-Visit-Only"

**Timing Logic:**
- General pest treatment: 24 hours post-completion
- Bed bug: After all-clear confirmation (not Day 1 — too early)
- Termite treatment: 48 hours post-completion
- Recurring quarterly visit: 2 hours post-completion (routine = quick ask)

**Sequence:**
- **SMS (Step 1):**
  > *"Hi [First Name]! [Tech Name] wanted to check — how'd everything go today? If we knocked it out of the park, would you mind leaving us a quick Google review? It means the world to our team: [Review Link]"*

- **Email (Step 2, 24 hours later if no click):**
  > Subject: *"Quick question about your service..."*
  > *"We want to make sure you're 100% satisfied. Did we solve your [pest type] problem? If yes, could you share a quick review on Google? Takes 90 seconds and helps families in [City] find us when they need help: [Review Link]*

- **If review link clicked:** Tag `review-requested`, remove from sequence
- **If no action after 5 days:** Remove from sequence, do not push further

---

### Workflow 9: Lapsed Customer Win-Back

**Trigger:** Last service date > 180 days AND no active plan

**Sequence:**
- **Day 180:** Win-back SMS
  > *"Hi [First Name]! It's been a while since we treated your home. [Current Season] is prime time for [seasonal pest] in [City]. Want us to do a quick check? No pressure — just looking out for our past customers."*

- **Day 210:** Seasonal alert email
  > Subject: *"[City] is seeing a surge in [pest type] this season"*

- **Day 240:** Final attempt SMS
  > *"Last message — we'd love to have you back. If you've had any pest activity since we last visited, reply YES and we'll set up a free re-inspection."*

---

### Workflow 10: Commercial Monthly Service Reminder

**Trigger:** Monthly, 5 days before scheduled commercial service date

**Sequence:**
- **5 days before:** Notification to property manager contact
  > *"Hi [Contact Name], this is [Company]. Your monthly pest service for [Property Name] is scheduled for [Date] at [Time]. Please ensure access to [areas]. Questions? Reply here."*

- **1 day before:** Confirmation request
  > *"Confirming tomorrow's service at [Property]. Any new concerns or areas to focus on this visit?"*

- **After service:** Compliance summary
  > *"Service complete for [Property Name] — [Date]. Technician: [Name]. Areas treated: [list]. No issues / Issues found: [note]. Full service log attached / available on request."*

---

## 6. SMS & Email Template Library

### Emergency / Urgency SMS Templates

**Emergency Ant/Roach/Rodent:**
> *"🚨 Emergency pest service available TODAY. Seeing [ants/roaches/mice]? We can dispatch a tech this afternoon. Reply HELP or call [Number]."*

**Wasp Nest Emergency:**
> *"Active wasp or hornet nest? DO NOT disturb it. We handle emergency nest removal same-day. Reply NOW to book — limited slots available."*

**Bed Bug Emergency:**
> *"Bed bugs are one of the hardest infestations to eliminate without professional heat treatment. Don't wait — every day makes it worse. We can inspect today. Reply INSPECT to book."*

---

### Seasonal Warning Campaign Templates

**Spring — Ant Surge:**
> *"⚠️ Spring Ant Alert for [City]: [Month] is when ant colonies explode in size as queens start new trails. We're already seeing calls in your area. Want to get ahead of it? Early bookings fill fast."*

**Spring — Termite Swarm Season:**
> *"Termite swarm season is here. If you've seen winged insects near windows or foundation, those could be termite reproductives — a sign of an active colony. Free termite inspection this month. Want in?"*

**Summer — Mosquito:**
> *"Summer mosquito season is peaking. Our barrier spray treatment gives you 3–4 weeks of yard protection. Perfect before outdoor events. Book before [Date] — this month's spots are almost gone."*

**Fall — Rodent Exclusion:**
> *"🐀 Fall rodent warning: As temps drop, mice and rats start looking for warm places — like your walls and attic. Now is the time to seal up before they get in. Our exclusion service closes entry points permanently."*

**Winter — Indoor Pests:**
> *"Winter pests don't take a season off. Cockroaches, silverfish, and stored product pests thrive indoors all year. Haven't had a service in 6+ months? Let's get you checked before anything takes hold."*

---

### Recurring Plan Upsell Templates

**SMS — Soft Upsell (24h post-treatment):**
> *"Your [pest type] treatment should be fully active now. One thing to know: most pest problems return within 90–180 days without a maintenance plan. Our Quarterly Service is designed exactly for this. Want to know more?"*

**SMS — Direct Offer (72h):**
> *"[First Name] — I wanted to follow up on your recent service. We have a Quarterly Protection Plan that covers unlimited callbacks + quarterly treatments for [price]/quarter. Want me to add you? Reply YES and I'll get it set up."*

**Email — Plan Benefits:**
> **Subject:** *Stop dealing with the same problem every 6 months*
>
> *Hi [First Name],*
>
> *You called us because you had a [pest type] problem. We fixed it. But here's the truth: without a maintenance plan, there's a good chance you'll deal with the same thing next season.*
>
> *Our [Plan Name] Quarterly Service covers:*
> - *4 scheduled treatments per year*
> - *All covered pest types (ants, roaches, spiders, silverfish, and more)*
> - *Unlimited callbacks between visits at no extra charge*
> - *Priority scheduling during outbreak season*
>
> *Starting at just [$X/quarter]. That's [$/month] to never deal with this again.*
>
> *[Book Your Plan → Button]*
>
> *— [Company Name]*

---

### Post-Treatment Reassurance Templates

**General Post-Treatment (1 hour):**
> *"Treatment done! You might see increased pest activity in the next 24–48 hours as the treatment works — that's completely normal. Give it 5–7 days for full effect. Questions? Just reply."*

**Termite Treatment (48 hours):**
> *"Following up on your termite treatment. The [liquid barrier / bait stations] are now active. It can take 30–90 days for a full colony elimination through bait stations — we'll check in regularly. Your home is protected."*

---

### Review Request Templates

**SMS (Primary):**
> *"[First Name] — [Tech Name] here from [Company]. Hope we solved that [pest] problem! If we did a good job, a quick Google review helps a lot. 30 seconds: [Review Link] 🙏"*

**Email (Follow-up):**
> **Subject:** *How did we do?*
>
> *Hi [First Name], your service was [X] days ago and we want to make sure everything is still looking good. If [Tech Name] solved your [pest] issue, would you take 60 seconds to leave us a Google review? It helps other [City] families find us when they need help most. [Leave a Review → Button]. Thank you!*

---

## 7. Lead Sources & Intake Strategy

### Lead Source Breakdown by Priority

| Lead Source | Speed Requirement | Conversion Rate | Automation Priority |
|-------------|-------------------|-----------------|-------------------|
| **Google LSA (Local Services Ads)** | <2 min | Very High | Critical |
| **Emergency Google Search (organic)** | <5 min | High | Critical |
| **Missed Call (existing customer)** | <60 sec | Very High | Critical |
| **Missed Call (new customer)** | <60 sec | Medium-High | Critical |
| **Referrals** | <24 hours | Very High | High |
| **Property Manager / Commercial** | <4 hours | High | High |
| **Real Estate Agent** | <1 hour | High | High |
| **Angi / HomeAdvisor** | <5 min | Medium | High |
| **Facebook / Instagram Ads** | <5 min | Medium | Medium |
| **Web Chat / Chatbot** | Instant | Medium | Medium |
| **Nextdoor / Community Referral** | <2 hours | High | Medium |

### LSA Integration Setup

- Connect GHL to Google LSA via Zapier or native integration
- All LSA leads trigger `Workflow 2: New Lead Speed-to-Contact` immediately
- Tag all LSA leads `source-lsa` for attribution tracking
- LSA leads that book within 24 hours → mark as "LSA Converted" for ROI reporting

### Website Lead Intake Forms

**Recommended form fields:**
1. First Name
2. Last Name
3. Phone (required — primary contact)
4. Email (required — secondary contact)
5. **Pest Type** (dropdown: Ants / Roaches / Bed Bugs / Termites / Rodents / Mosquitoes / Wasps / Other)
6. **Urgency** (dropdown: Emergency — Same Day / This Week / Just Getting a Quote)
7. **Property Type** (dropdown: Residential / Commercial / Rental Property)
8. Address (for zone routing)
9. Brief description (text area, optional)

**Conditional logic:** If Urgency = "Emergency — Same Day" → trigger emergency pipeline, escalate to rep immediately

---

## 8. Booking Flow Design

### Booking Flow 1: Emergency / Same-Day Service

**Calendar:** "Emergency Service" calendar — dedicated slots held each day for emergency dispatch
- 4–6 emergency slots per day, per service zone
- Slots: 8–10 AM / 10 AM–12 PM / 1–3 PM / 3–5 PM (2-hour arrival windows)
- Calendar auto-shows only today's and tomorrow's availability

**Intake:** Pest type + address confirmation first; then calendar selection
**Confirmation:** SMS within 30 seconds of booking
**Pre-arrival:** 30-minute "tech on the way" SMS trigger

---

### Booking Flow 2: Scheduled Service / Free Inspection

**Calendar:** "General Pest Inspection" calendar — 5–7 day booking window
- 30-minute inspection slots
- 2-hour arrival windows for homeowner convenience
- Available Mon–Sat, 8 AM–5 PM

**Qualification questions:**
- Pest type observed
- How long has this been an issue?
- Property type and approximate square footage

**Confirmation:**
- Immediate booking confirmation SMS + email
- Prep instructions in confirmation email
- Reminder sequence (48h / 24h / 2h)

---

### Booking Flow 3: Free Termite Inspection

**Separate calendar** — "Termite Inspection" — assigned to termite-certified technicians only

**Special handling:**
- 60-minute inspection slots (vs. 30-minute for general)
- Post-inspection, tech sends photo report via GHL conversation
- Follow-up proposal via GHL proposal tool within 24 hours

---

### Booking Flow 4: Recurring Plan Service Visit

**Calendar:** "Recurring Plan Service" — auto-scheduled quarterly or monthly
- System auto-books each service visit 7 days before due date
- Customer receives booking notification + option to reschedule

---

## 9. Recurring Service Plan Engine (Highest LTV)

This is the most important section. Recurring plan revenue is what separates a $300K/year pest control company from a $1.5M one.

### Why Recurring Plans Win

- **LTV comparison:** One-time treatment = $150–$400. Quarterly plan customer = $600–$900/year, year-over-year. 5-year LTV on a quarterly plan customer = $3,000–$4,500+.
- **Referral quality:** Recurring plan customers refer more. They've had multiple positive touchpoints with the company.
- **Churn economics:** 85–90% of quarterly plan customers renew if they've had zero pest issues between visits. That's the job — keep them pest-free and they stay forever.
- **Technician route efficiency:** Recurring plan customers are geographically clustered and scheduled in advance, dramatically reducing drive time and fuel cost.

### Plan Tiers to Offer in CRM

| Plan Name | Frequency | Price Range | Coverage |
|-----------|-----------|-------------|----------|
| **Basic Shield** | Quarterly (4x/year) | $99–$149/quarter | General pest control: ants, roaches, spiders, silverfish, earwigs |
| **Total Protection** | Bi-monthly (6x/year) | $79–$99/bi-month | All Basic + stinging insects, fleas, ticks |
| **Premium Guard** | Monthly (12x/year) | $59–$89/month | All Total + priority same-day service, free callbacks |
| **Mosquito Barrier** | Monthly (April–October) | $49–$89/month | Yard mosquito barrier spray only |
| **Rodent Shield** | Quarterly | $79–$99/quarter | Interior/exterior rodent monitoring + exclusion maintenance |
| **Termite Monitoring** | Annual inspection + continuous bait station monitoring | $199–$399/year | Termite bond / warranty coverage |

### Upsell Conversion Funnel

**Optimal conversion timing:**
1. **During initial inspection** — before treatment. Technician discusses plan options while the customer is already in "fix this now" mode.
2. **24–72 hours post-treatment** — peak relief period. Problem is solved, trust is high, customer is receptive.
3. **30 days post-one-time service** — first follow-up check-in. "Noticing anything?"

**Objection handlers (for rep training + chatbot scripting):**

*"I can just call when I need you."*
> *"Totally — and we'll always be here. The thing is, quarterly service is cheaper per visit than emergency calls, and you never have to deal with an active infestation again. Most customers say they wished they'd done it sooner."*

*"It's too expensive."*
> *"I understand. Our Basic Shield plan works out to about [$X/month] — less than a cup of coffee a day to never worry about [pest type] again. And if you see anything between visits, callbacks are free."*

*"We've never really had a serious problem."*
> *"That's exactly the right time to start — before it becomes serious. Preventive treatment is always cheaper than emergency treatment."*

---

## 10. Seasonal Campaign Calendar

### Spring Campaign — Ants, Termites, Wasps (March–April)

**Target:** Full database + lapsed customers (no service in 6+ months)
**Message angle:** "They're already active. Don't wait until you see them inside."

**Week 1 (March):** Email blast
- Subject: *"[City]'s Ant Season Starts Earlier Every Year — Here's How to Beat It"*
- Body: Educational content + quarterly plan offer + booking CTA

**Week 2 (March):** SMS blast
> *"Spring ant season hits [City] hard in [Month]. We're already seeing calls in your area. Book before our schedule fills — [Link]"*

**Week 3 (April):** Termite swarm alert
> *"Termite swarm season is officially here. Seeing winged insects near lights or windows? That's a warning sign. Free termite inspection — book this week: [Link]"*

**Week 4 (April):** Wasp nest early treatment
> *"Queen wasps are building new nests RIGHT NOW. Treating early (before the colony grows to 1,000+) is cheaper and safer. Limited early-season slots available."*

---

### Summer Campaign — Mosquitoes, Fleas, Ticks (May–July)

**Target:** Homeowners with yards, pet owners, families with children

**Email — Mosquito Barrier:**
> **Subject:** *"Enjoy your backyard this summer (without DEET)"*
>
> *Your yard should be a place you actually want to spend time. Our mosquito barrier spray keeps mosquitoes out for 3–4 weeks per application, all season long. Book your first treatment before [Date] and get [X% off / free inspection].*

**SMS — Flea/Tick Season:**
> *"Flea and tick season is peaking. One hitchhiker from the yard can turn into a full infestation inside. Pet owner? We have a targeted treatment that's safe for animals. Interested?"*

---

### Fall Campaign — Rodents, Exclusion (September–October)

**Target:** Homeowners with history of rodent issues + full database

**SMS — Rodent Warning:**
> *"🐭 FALL RODENT ALERT: Mice and rats start moving indoors as temps drop below 50°F. They can fit through a hole the size of a dime. Our exclusion service permanently seals entry points. Spots are limited — book now."*

**Email — Exclusion Campaign:**
> **Subject:** *"Seal your home before winter — rodents are already looking"*
>
> *Every fall, we get emergency calls from homeowners who waited too long. Mice in walls, droppings in the kitchen, chewed wires. Our exclusion service physically seals every entry point so they can't get in. Here's what we do: [bullet list of exclusion steps]. Book your fall exclusion inspection before October: [CTA Button]*

---

### Winter Campaign — Indoor Pests, Cockroaches, Overwintering Insects (November–February)

**Target:** Lapsed customers + general newsletter list

**SMS — Winter Indoor Pest:**
> *"Winter pests don't go away — they move inside. Roaches, silverfish, and stored product pests thrive in heated homes. Last service was a while ago? Book a winter check-up."*

**Email — Year-End Plan Push:**
> **Subject:** *"Start [New Year] pest-free"*
>
> *New year, fresh start. Our annual protection plan keeps your home pest-free all 12 months. Lock in this year's pricing before rates go up in [Month]. [See Plan Options → Button]*

---

## 11. Commercial & Property Manager Track

### Why Commercial Is Worth a Dedicated Pipeline

- Commercial accounts pay monthly (recurring revenue guaranteed)
- Higher ticket: $200–$2,000+/month depending on facility type and square footage
- Contract-based: 1–3 year service agreements are standard
- Requires different documentation: MSDS sheets, service logs, compliance records, IPM reports
- Referral network: one property management company can mean access to 10–50 properties

### Commercial Contact Strategy

**Decision makers to target:**
- Property managers (apartments, commercial buildings)
- Restaurant owners / food service managers
- Hotel general managers / facility managers
- School district facilities directors
- Warehouse / food processing facility safety managers

**Outreach message (initial commercial inquiry SMS):**
> *"Hi [Contact Name], this is [Rep] from [Company]. We specialize in commercial pest management for [property type] in [City]. We use an IPM-based approach — documentation, compliance records, and monthly service logs included. Would a 15-minute call make sense? We work with [X] properties in your area."*

### IPM (Integrated Pest Management) in Commercial Context

Commercial clients — especially food service, healthcare, and schools — require an IPM framework. GHL custom fields and notes should capture:

- **Inspection frequency:** Monthly / bi-monthly / quarterly
- **Service log delivery:** PDF report after each service (trigger from workflow)
- **Pest exclusion points identified:** Tracked and updated per visit
- **Chemical use documentation:** Product name, application rate, target pest, treated area
- **HACCP compliance flag** (for food service clients)
- **Pest pressure rating:** Low / Moderate / High / Critical (tracked per visit)

### Commercial Service Workflow

**Monthly service workflow trigger:** 5 days before scheduled visit

1. Pre-service notification to property manager contact
2. Day-of confirmation (2 hours before arrival)
3. Post-service: Automated service log delivery via email
4. 48 hours post-service: Manager check-in SMS
5. Monthly: Automated pest pressure summary report

---

## 12. Review Generation System

### The Pest Control Review Opportunity

The average pest control company has 15–40 Google reviews. The market leaders in any given city have 200–800+. Reviews are the #1 trust signal for emergency buyers. The gap between "20 reviews" and "300 reviews" is 6–12 months of consistent review automation.

### Review Request Timing by Service Type

| Service Type | Optimal Request Timing | Reason |
|--------------|----------------------|--------|
| Emergency (same-day wasp/ant) | 3–4 hours post-service | Immediate relief = peak satisfaction |
| General quarterly treatment | 2 hours post-service | Routine + positive = quick ask |
| Termite treatment | 48 hours post-service | Give time to feel secure |
| Bed bug — all clear | After all-clear confirmation only | Never ask during treatment cycle |
| Commercial monthly | Day after service | Give time to review service log |
| Rodent exclusion | 1 week post-service | Customer needs to observe the results |

### Review Routing Logic

- If customer rating is high (positive response) → route to Google review link
- If customer expresses a concern → route to internal feedback form (NEVER to Google)
- Internal feedback form → triggers rep task to call and resolve before issue escalates online

### Review Response Automation

- **5-star review received:** Trigger internal notification to manager; send thank-you SMS to customer
- **3-star or below via internal form:** Trigger immediate rep escalation task; do NOT send to public review platforms

### Platform Priority

1. **Google Business Profile** (primary — highest visibility for emergency searches)
2. **Yelp** (secondary — strong in certain markets)
3. **Angi / HomeAdvisor** (tertiary — if they use Angi for leads)
4. **Nextdoor** (community referral amplifier)

---

## 13. Snapshot Differentiation Strategy

### What Makes the 1app Pest Control Snapshot Different

**vs. Generic Home Services Template:**
- Full pest control language throughout (infestation, treatment, fumigation, exclusion, IPM, bait station, colony elimination, heat treatment)
- 6 dedicated pipelines vs. 1 generic pipeline
- Seasonal campaign calendar built in and ready to deploy
- Recurring plan management pipeline (the #1 revenue driver for the niche)

**vs. Entry-Level Pest Control Snapshots:**
- Bed bug anxiety management workflow (distinct tone, multi-step)
- Termite inspection + bait station monitoring pipeline
- Commercial / property manager track with IPM language and service log automation
- Real estate / WDO inspection pipeline
- Seasonal campaign templates pre-written and ready
- Review generation with timing logic by service type (not a generic "please review us" blast)
- Zone-based technician routing via custom fields
- Emergency vs. scheduled booking calendar separation

### Positioning for 1app Sales Conversations

**Headline:** *"The only GHL snapshot built by people who understand the difference between a termite swarm and a carpenter ant infestation."*

**Value proposition (to pest control prospect):**
> *"Most CRMs treat pest control like plumbing. They don't know what a bait station is, or that bed bug customers are panicking, or that missed calls in your industry go to the competitor. We built our system specifically for pest control operators. Your pipeline tracks emergency calls separately from recurring plan signups. Your technicians get zone-based routing. Your customers get a post-treatment upsell sequence that runs automatically. And when Google reviews come in, they go up at the exact moment your customer feels the most relief — not 30 days later when they've forgotten you."*

---

## 14. Full Build Checklist

### Pipelines
- [ ] Pipeline 1: General Pest Control — Residential
- [ ] Pipeline 2: Termite & Specialty Services
- [ ] Pipeline 3: Bed Bug Track
- [ ] Pipeline 4: Commercial / Property Manager
- [ ] Pipeline 5: Recurring Service Plan Management
- [ ] Pipeline 6: Real Estate / Pre-Sale Inspection

### Calendars
- [ ] Emergency / Same-Day Service (zone A)
- [ ] Emergency / Same-Day Service (zone B — if applicable)
- [ ] General Pest Inspection — Scheduled
- [ ] Termite Inspection (certified tech only)
- [ ] Recurring Plan Service (auto-scheduled)
- [ ] Free Commercial Site Assessment

### Workflows
- [ ] WF-01: Missed Call Text Back (Emergency Mode)
- [ ] WF-02: New Lead Speed-to-Contact
- [ ] WF-03: Appointment Confirmation (3-touch)
- [ ] WF-04: Post-Treatment Follow-Up + Plan Upsell
- [ ] WF-05: Recurring Plan Renewal Sequence
- [ ] WF-06: Bed Bug Anxiety Management
- [ ] WF-07: Seasonal Outbreak Campaign (spring/summer/fall/winter — 4 versions)
- [ ] WF-08: Review Generation (by service type logic)
- [ ] WF-09: Lapsed Customer Win-Back (180-day trigger)
- [ ] WF-10: Commercial Monthly Service Reminder
- [ ] WF-11: Real Estate Agent Referral Nurture
- [ ] WF-12: Plan Churn Recovery (canceled plan re-activation)

### Forms
- [ ] General Pest Inquiry Form (residential)
- [ ] Emergency Service Request Form
- [ ] Free Termite Inspection Form
- [ ] Commercial Pest Assessment Form
- [ ] Real Estate / WDO Inspection Request Form
- [ ] Internal Customer Feedback Form (complaint routing — does NOT go to Google)

### Email Templates
- [ ] Booking Confirmation (general)
- [ ] Booking Confirmation (termite)
- [ ] Booking Confirmation (bed bug — empathetic tone)
- [ ] Prep Instructions (day-before reminder)
- [ ] Post-Treatment Summary
- [ ] Recurring Plan Upsell (benefits-focused)
- [ ] Seasonal Campaign (4 versions: spring / summer / fall / winter)
- [ ] Renewal Reminder
- [ ] Win-Back Campaign (6-month lapsed)
- [ ] Review Request
- [ ] Commercial Service Log Delivery

### SMS Templates
- [ ] Missed call text back (emergency tone)
- [ ] Speed-to-contact (new lead)
- [ ] Booking confirmation
- [ ] 48-hour appointment reminder
- [ ] 24-hour reminder + prep instructions
- [ ] 2-hour day-of reminder
- [ ] Post-treatment (1 hour)
- [ ] Post-treatment check-in + soft upsell (24 hours)
- [ ] Plan upsell direct offer (72 hours)
- [ ] Seasonal alert (4 versions)
- [ ] Review request
- [ ] Win-back (180-day)
- [ ] Commercial pre-service notification
- [ ] Bed bug day-1 reassurance
- [ ] Bed bug week-1 check-in
- [ ] Bed bug all-clear + review request

### Custom Fields
*(See Section 15 for full list)*

### Tags
*(See Section 15 for full list)*

### Reporting / Dashboard
- [ ] Active leads by pipeline stage
- [ ] Speed-to-contact average (target: <5 min)
- [ ] Recurring plan enrollment rate (target: 20–35% of one-time customers)
- [ ] Appointment confirmation rate (target: >85%)
- [ ] No-show rate (target: <10%)
- [ ] Review request click rate (target: >30%)
- [ ] Monthly revenue by service type
- [ ] Seasonal campaign performance (before vs. after)
- [ ] Lapsed customer re-engagement rate

---

## 15. Custom Fields & Tags Reference

### Custom Fields

**Contact-Level:**
| Field Name | Type | Values / Notes |
|-----------|------|----------------|
| `Pest Type(s)` | Multi-select | Ants / Roaches / Termites / Bed Bugs / Rodents / Mosquitoes / Wasps / Spiders / Other |
| `Service Type` | Dropdown | One-Time / Recurring Plan / Termite / Bed Bug / Commercial / Real Estate |
| `Plan Type` | Dropdown | None / Basic Shield / Total Protection / Premium Guard / Mosquito Barrier / Rodent Shield / Termite Monitoring |
| `Plan Renewal Date` | Date | Used to trigger renewal workflow |
| `Last Service Date` | Date | Used for lapsed customer trigger |
| `Service Zone` | Dropdown | Zone A / Zone B / Zone C (map to technician territories) |
| `Property Type` | Dropdown | Residential / Commercial / Multi-Family / Rental |
| `Preferred Technician` | Text | Technician name for recurring customers |
| `Lead Source` | Dropdown | Google LSA / Google Organic / Missed Call / Referral / Angi / Facebook / Real Estate / Other |
| `Review Requested` | Checkbox | Yes / No |
| `Review Completed` | Checkbox | Yes / No |
| `Urgency Level` | Dropdown | Emergency / This Week / Flexible |

**Opportunity-Level:**
| Field Name | Type | Values / Notes |
|-----------|------|----------------|
| `Treatment Type` | Dropdown | General GPC / Termite Liquid / Termite Fumigation / Bait Station / Bed Bug Heat / Bed Bug Chemical / Mosquito Barrier / Rodent Exclusion / WDO Inspection |
| `Estimated Job Value` | Currency | Auto-populate from service tier |
| `Infestation Severity` | Dropdown | Light / Moderate / Severe |
| `Treatment Date` | Date | Completion date for post-treatment workflow trigger |
| `Follow-Up Inspection Date` | Date | For termite/bed bug multi-visit services |
| `Proposal Sent Date` | Date | For termite/commercial proposals |
| `Contract End Date` | Date | For commercial accounts |

---

### Tags

**Source Tags:**
- `source-lsa` — Google Local Services Ad lead
- `source-missed-call` — Recovered from missed call text back
- `source-referral` — Word-of-mouth referral
- `source-angi` — Angi/HomeAdvisor lead
- `source-facebook` — Facebook/Instagram ad
- `source-real-estate` — Real estate agent referral
- `source-commercial-direct` — Commercial prospect direct outreach

**Service Tags:**
- `new-lead` — Just entered system
- `contacted` — Two-way communication initiated
- `appointment-booked`
- `no-show`
- `treatment-complete`
- `recurring-plan` — Enrolled in a recurring plan
- `termite` — Active termite case
- `bed-bug` — Bed bug case (triggers special workflow)
- `commercial` — Commercial account
- `property-manager` — Property management contact
- `real-estate` — Real estate inspection client

**Status Tags:**
- `upsell-accepted` — Enrolled in plan after one-time
- `upsell-declined` — Declined plan (enter re-engagement)
- `plan-churned` — Canceled recurring plan
- `lapsed-180` — No service in 180+ days
- `win-back-active` — Currently in win-back sequence
- `review-requested`
- `review-completed`
- `do-not-contact`

**Seasonal Campaign Tags:**
- `spring-campaign-sent`
- `summer-campaign-sent`
- `fall-campaign-sent`
- `winter-campaign-sent`

---

## Appendix: Glossary of Pest Control Industry Terms

*(For agency team members building or customizing the snapshot)*

| Term | Definition |
|------|-----------|
| **GPC (General Pest Control)** | Standard recurring treatment covering common household pests |
| **Infestation** | Active, established pest population in a structure |
| **Extermination** | Elimination of a pest population (often one-time) |
| **Treatment** | Professional pest control application (chemical, heat, physical) |
| **Exclusion** | Physical sealing of entry points to prevent pest ingress |
| **IPM (Integrated Pest Management)** | Environmentally sensitive approach combining monitoring, biological controls, and targeted chemical use |
| **Fumigation** | Whole-structure gas treatment, typically for drywood termites |
| **Heat Treatment** | Raising structure temperature to 120°F+ to eliminate bed bugs |
| **Bait Station** | In-ground or above-ground station containing termite bait matrix |
| **Termite Bond** | Service warranty ensuring re-treatment if termites return |
| **WDO Inspection** | Wood-Destroying Organism inspection (required for real estate closings in many states) |
| **Quarterly Spray** | Routine preventive treatment performed 4x per year |
| **Swarmer / Reproductive** | Winged termite or ant leaving a colony to establish a new one — a key warning sign |
| **Residual Treatment** | Chemical treatment that remains active for weeks after application |
| **Moisture Barrier** | Physical treatment applied in crawl spaces to deter subterranean termites |
| **HACCP** | Hazard Analysis Critical Control Point — food safety standard requiring pest documentation in food service |
| **Colony Elimination** | Complete destruction of a pest colony (vs. surface treatment) |
| **Callback** | Free return visit when pests return between scheduled treatments |

---

*Document prepared by 1app Technologies Inc. — GHL SaaS Agency*
*For internal agency use and client onboarding. All templates are customizable for individual operator branding.*
*Review and update seasonal campaign dates per client geography and climate zone.*
