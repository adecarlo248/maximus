# 🔐 1app GHL Snapshot Research: Locksmith Industry
## Comprehensive Build Document — Final Research Series

**Document Version:** 1.0  
**Prepared For:** 1app Technologies Inc. — GHL SaaS Agency  
**Research Date:** July 2026  
**Industry:** Locksmith Services (Emergency, Residential, Commercial, Automotive, Safe)  
**Document Type:** Agency Build Reference — Internal Use

---

## TABLE OF CONTENTS

1. [Executive Summary](#executive-summary)
2. [Industry Overview & Market Data](#industry-overview)
3. [Locksmith Business Pain Points](#pain-points)
4. [Market Landscape: Existing GHL Locksmith Snapshots](#market-landscape)
5. [Pipeline Architecture](#pipeline-architecture)
6. [Workflow Design](#workflow-design)
7. [Lead Sources & Acquisition Strategy](#lead-sources)
8. [SMS & Email Templates](#templates)
9. [Booking Flow Architecture](#booking-flow)
10. [Move-In Rekey Campaign — Real Estate Partner Program](#rekey-campaign)
11. [Commercial Master Key System Workflow](#commercial-master-key)
12. [Review Generation Strategy](#review-generation)
13. [Property Manager Account Workflow](#property-manager)
14. [Snapshot Differentiators](#differentiators)
15. [Full Snapshot Component Checklist](#component-checklist)
16. [Pricing & Packaging Recommendations for 1app](#pricing)

---

## 1. EXECUTIVE SUMMARY {#executive-summary}

The locksmith industry is one of the most underserved verticals in the GHL SaaS ecosystem. The typical locksmith owner is running a van, answering calls on a cell phone, and losing leads to competitors every single day — not because their service is worse, but because they have zero follow-up infrastructure.

**The core problem:** Locksmith leads are the most time-critical leads in the trades. A homeowner locked out at 11pm will call the first three numbers that answer. The locksmith who calls back 4 minutes later loses. GHL solves this if built correctly.

The access control market is also undergoing a transformation — from $10B to a projected $100B market. Locksmiths who build client relationships today own the path to recurring revenue in tomorrow's smart lock and access control ecosystem.

**The 1app locksmith snapshot opportunity:** Most existing GHL locksmith snapshots are generic "home services" templates with locksmith-sounding labels slapped on. They miss the emergency-first dispatch model, the scam trust gap, the real estate rekey partnership opportunity, and the commercial master key account pipeline. This snapshot fills those gaps and positions 1app as the category-defining solution.

**Snapshot revenue model for 1app:**  
- Onboarding: $500–$1,000 setup fee  
- Monthly SaaS: $197–$397/month  
- Add-on: Commercial account module, $97/month  
- Target ARR per client: $2,364–$4,764

---

## 2. INDUSTRY OVERVIEW & MARKET DATA {#industry-overview}

### Market Size & Structure
- **~20,000–22,000 locksmith businesses** in the United States
- **~2,500–3,000** in Canada
- Industry revenue (US): ~$3–4 billion annually
- **85–90% are owner-operator or small 1–5 person shops** — the exact GHL SaaS client profile
- Access control adjacent market growing from $10B to $100B (per ALOA 2026 keynote, Lee Odess / TACC)

### Business Model Mix
A typical locksmith generates revenue from multiple service categories:

| Service Type | % of Revenue | Lead Temperature |
|---|---|---|
| Emergency lockout (residential) | 35–45% | 🔥 EMERGENCY |
| Residential rekey / lock change | 20–25% | Warm |
| Commercial locks & access control | 15–20% | Planned |
| Automotive locksmith | 10–15% | 🔥 EMERGENCY |
| Safe opening / combination | 5–8% | Mixed |
| Key duplication | 3–5% | Walk-in |

### Average Ticket Values (North American market)
- **Emergency lockout (residential):** $75–$175 (basic); $150–$250 (after hours/weekends)
- **Rekey deadbolt:** $50–$100 per lock; $200–$400 for full home rekey (6–8 locks)
- **Schlage/Kwikset lock change:** $120–$250 installed
- **Mortise lock replacement:** $200–$500+
- **High-security lock upgrade (Mul-T-Lock, Medeco, ASSA Abloy):** $300–$800 per lock installed
- **Bump-resistant / pick-resistant installation:** $250–$600
- **Master key system (commercial):** $500–$5,000+ (depends on scale)
- **Access control system (commercial):** $2,000–$25,000+ (key fob, card reader, intercom)
- **Transponder key (automotive):** $150–$400 (OEM-quality)
- **Automotive lockout:** $75–$150
- **Safe opening (non-destructive):** $200–$600
- **Safe opening (destructive):** $500–$1,500+
- **Safe combination reset:** $150–$300

### Industry Growth Drivers (2024–2026)
- Move-in rekeying becoming standard for new homeowners
- Commercial access control retrofits (key fob, badge, smart lock)
- Apartment and multi-family security upgrades
- Post-break-in residential security consultations
- Automotive transponder key demand (used car sales, lockouts)
- Growing smart lock installations (Schlage Encode, August, Yale)

---

## 3. LOCKSMITH BUSINESS PAIN POINTS {#pain-points}

### Pain Point #1: The 30-Second Lead Window
**This is the single most critical pain point in the industry.**

Emergency locksmith leads — lockouts, broken keys, lost keys — are time-critical to a degree no other trade experiences. When a homeowner is locked out, they search "locksmith near me," and they call the first 2–3 results. They're not comparison shopping. They're panicking.

The locksmith who answers first wins. The one who calls back 8 minutes later gets voicemail.

**The problem:** Most locksmith shops are 1–2 person operations. The owner is *in the field*, doing a job. They physically cannot answer every call. They have no system to instantly text back missed calls with a response like "We got your call — on our way / what's your location?" They lose 20–40% of their emergency leads this way.

**The GHL solution:** Missed Call Text Back + AI Voice Agent = instant response while owner is on a job. This is table stakes for the locksmith snapshot. Without it, the snapshot is useless.

### Pain Point #2: The Fake Locksmith Scam Problem
The locksmith industry has a well-documented trust crisis. "Scam locksmiths" (also known as "Google locksmith scammers") operate networks of fake local listings, quote low prices over the phone, then charge $400–$800 on arrival. The FTC has investigated this, local news stations run exposés regularly, and consumers are now suspicious of any locksmith they don't know.

**This means:**
- A legitimate locksmith with 50+ five-star reviews has a massive competitive advantage
- Homeowners frequently Google the locksmith's name before letting them inside
- Reviews are not "nice to have" — they are **gatekeepers to the job**
- Trust signals (license number displayed, real photos, consistent business name) close deals before the van arrives

**The GHL solution:** Automated review request after every completed job. Proactive display of credentials in confirmation messages. Reputation management workflows.

### Pain Point #3: Zero Repeat Business Strategy
Locksmith is perceived as a low-repeat industry — "I only need them when something breaks." The truth is:
- Move-in buyers rekey the whole home (referral goldmine)
- Homeowners who got locked out this year are prime candidates for a hidden spare key service / smart lock upgrade
- Post-lockout clients often ask "how do I prevent this?" — perfect upsell moment
- Commercial clients need annual master key audits, rekeying after staff turnover, access control updates

But the average locksmith has no database of past clients. No CRM. No follow-up sequence. They did the job, took the cash, and drove away.

**The GHL solution:** Contact capture at every job, with post-job nurture sequences segmented by service type.

### Pain Point #4: Google Ads and LSA Competition
Emergency locksmith keywords are among the most expensive in local service advertising:
- "Locksmith near me" CPC: $15–$45 per click (varies by market)
- "Emergency locksmith [city]": $25–$60 per click
- Google Local Services Ads (LSA): $30–$80 per lead in major markets

Most locksmith shops are spending $1,000–$3,000/month on Google Ads with zero follow-up infrastructure. They're paying for leads they're not capturing or converting properly.

**The GHL solution:** Convert more of the leads they're already paying for. Every missed call, every unanswered web chat, every form submission needs instant automation to maximize the ad spend ROI.

### Pain Point #5: After-Hours Revenue Bleed
Locksmith emergencies do not respect business hours. Break-ins happen at 2am. Lockouts happen on Sunday mornings. Most locksmith shops either:
a) Answer 24/7 themselves (owner burnout, family strain)
b) Let after-hours calls go to voicemail (lost revenue)
c) Partner with a sketchy answering service that gives bad info

**The GHL solution:** AI Voice Agent + SMS automation handles after-hours intake, captures the lead, sets expectations, and either dispatches the owner or queues the lead for morning.

### Pain Point #6: No System for Commercial Account Development
Commercial clients — property managers, apartment complexes, office buildings, retail — are the holy grail for locksmiths. Recurring revenue, large-ticket master key systems, access control contracts, regular rekeying after staff changes.

But most locksmith shops stumble into commercial work by accident. They have no pipeline to nurture commercial prospects, no drip campaign for property managers, no proposal system.

**The GHL solution:** Dedicated commercial pipeline with separate stages, nurture sequences targeting property managers and commercial building owners, and automated touchpoints timed to common commercial need moments (end of lease season, staff changeover, annual audit).

### Pain Point #7: Review Management Neglect
Despite reviews being make-or-break in this industry, most locksmiths:
- Never ask for reviews
- Don't respond to negative reviews (which signals legitimacy to prospects)
- Have inconsistent Google Business Profile information
- Don't know their current review score without logging in manually

**The GHL solution:** Automated post-job review requests via SMS (2 hours after job completion), negative review interception (if 1–3 stars, routes to owner before going public where possible), and reputation dashboard.

### Pain Point #8: Key Duplication Revenue Commoditization
Home Depot, Walmart, and KeyMe kiosks have commoditized basic key duplication. The locksmith shop that only does key cutting is losing. The ones pivoting to high-security restricted key systems (Schlage Everest, Medeco, BEST CORMAX, Sargent), master key systems, and electronic credentials are growing.

**The GHL solution:** Educational email/SMS campaigns that position the locksmith as a security advisor, not just a key cutter. Upsell from basic duplication to restricted key systems.

---

## 4. MARKET LANDSCAPE: EXISTING GHL LOCKSMITH SNAPSHOTS {#market-landscape}

### What Currently Exists

A search of the GHL snapshot marketplace and third-party GHL template vendors (SnapShot Store, Extendly, Spiffy, ClawHub, etc.) reveals the following state of the market:

**Category: Generic Home Services Templates Rebranded as Locksmith**
- Most "locksmith snapshots" are generic home services pipelines with locksmith labels
- Standard pipeline stages: New Lead → Contacted → Quoted → Booked → Completed → Review Requested
- Basic missed call text back workflow
- Generic review request SMS
- No emergency dispatch logic
- No automotive-specific workflow
- No safe-opening workflow
- No commercial account pipeline
- No rekey campaign targeting real estate agents
- No property manager nurture sequence

**Category: Single-Purpose "Emergency Locksmith" Templates**
- Focus entirely on lockout emergency capture
- Strong missed call text back
- Basic booking flow
- Missing: commercial, automotive, safe, residential upgrade pathways

**What's Missing From Every Existing Solution:**
1. Emergency dispatch triage (residential vs automotive vs safe)
2. Real estate agent referral partnership workflow
3. Commercial master key system pipeline
4. Property manager account management
5. Post-job security upgrade upsell sequences
6. Trust-building sequences that address the scam problem directly
7. Automotive locksmith-specific intake (year/make/model, VIN, proof of ownership)
8. Safe opening workflow (type of safe, combination history, urgency)
9. Seasonal campaigns (spring security audit, move-in season rush)
10. Review interception / reputation protection workflow

**The Gap = The Opportunity**

No existing snapshot treats the locksmith as a multi-service security professional. They all treat it as "break-fix emergency." 1app can own the category by building the first comprehensive, full-lifecycle locksmith snapshot.

---

## 5. PIPELINE ARCHITECTURE {#pipeline-architecture}

### Philosophy: One CRM, Five Service Pipelines

The locksmith snapshot uses five dedicated pipelines — one per major service category. This is critical. Mixing emergency lockout leads with commercial account development leads in one pipeline creates workflow chaos and incorrect automation triggers.

---

### Pipeline 1: Emergency Lockout (Residential & After-Hours)

**Purpose:** Capture and convert the hottest, most time-critical leads in the industry.

| Stage | Description | Trigger |
|---|---|---|
| **New Emergency Lead** | Missed call, web chat, or inbound form | Instant — within 30 seconds |
| **Contacted — Awaiting Location** | Lead responded to SMS, technician gathering address | SMS response received |
| **Dispatched** | Technician en route, ETA confirmed | Manual or automated trigger |
| **Job in Progress** | On-site, job underway | Field update / technician status |
| **Job Complete — Awaiting Review** | Job done, payment collected, review request pending | 2-hour post-completion |
| **Review Received** | Review posted (4–5 stars) | Review monitoring trigger |
| **Upsell Sequence Active** | Residential security upgrade nurture started | 24 hours post-job |
| **Lost** | Lead went cold, went to competitor | No response after 3 contacts |

**Key Automation Points:**
- Stage 1→2: Instant missed call text back (30 seconds max — non-negotiable)
- Stage 4→5: Technician-triggered status update via mobile app
- Stage 5→6: 2-hour delay, automated review request SMS
- Stage 6→7: 24-hour delay, residential security audit offer

---

### Pipeline 2: Residential Lock Services (Scheduled)

**Purpose:** Manage planned residential jobs — rekey after move-in, deadbolt upgrade, lock change, smart lock installation, high-security lock upgrade.

| Stage | Description |
|---|---|
| **New Request** | Inbound call, referral, web form, real estate agent referral |
| **Qualified** | Service type confirmed (rekey, upgrade, install), address verified |
| **Estimate Sent** | Quote delivered via SMS or email |
| **Appointment Booked** | Confirmed date/time, reminder sequence active |
| **Job Scheduled — Day Before** | 24hr reminder sent |
| **Job Scheduled — Day Of** | 1hr reminder + technician GPS ETA |
| **Job Complete** | Payment, photos, work order signed |
| **Review Requested** | 2hr post-job SMS |
| **Security Upgrade Nurture** | Ongoing quarterly security tips / upsell |

**Key Service Tags (for segmentation):**
- `rekey-full-home`
- `rekey-single-lock`
- `deadbolt-upgrade`
- `schlage-installation`
- `kwikset-installation`
- `high-security-lock` (Mul-T-Lock, Medeco, ASSA)
- `smart-lock-install`
- `bump-resistant`
- `mortise-lock`

---

### Pipeline 3: Commercial Locksmith & Access Control

**Purpose:** Long-cycle sales pipeline for commercial accounts. Restaurants, offices, retail, multi-family residential, industrial facilities.

| Stage | Description |
|---|---|
| **Prospect Identified** | Property manager, business owner, facility director |
| **Outreach Sent** | Cold email / SMS intro, referral follow-up |
| **Initial Conversation** | Needs assessment call scheduled |
| **Needs Assessment Complete** | Master key requirements, access control scope, staff size, # of doors |
| **Proposal Sent** | Master key system proposal, access control quote, or lock audit |
| **Follow-Up Sequence** | 3-touch automated follow-up (Day 3, Day 7, Day 14) |
| **Proposal Accepted** | Contract signed, deposit collected |
| **Installation Scheduled** | Job timeline confirmed, materials ordered |
| **Installation Complete** | Final walkthrough, account setup |
| **Active Account — Recurring** | Annual audit scheduled, staff rekey reminders, renewal touchpoints |
| **Lost** | No response / went with competitor |

**Key Service Tags:**
- `master-key-system`
- `access-control-keyfob`
- `access-control-card-reader`
- `access-control-intercom`
- `commercial-deadbolt`
- `commercial-rekey-post-staff-change`
- `exit-device-panic-bar`
- `high-security-commercial`
- `multi-family-residential`
- `property-manager-account`

---

### Pipeline 4: Automotive Locksmith

**Purpose:** Emergency and scheduled automotive locksmith services. Lockouts, transponder key programming, key duplication, ignition cylinder replacement.

| Stage | Description |
|---|---|
| **Emergency — Locked Out** | Stranded motorist, immediate dispatch needed |
| **Location Confirmed** | Customer address/parking lot confirmed, ETA communicated |
| **En Route** | Technician dispatched, ETA SMS sent |
| **On-Site** | Vehicle verification (year/make/model, proof of ownership) |
| **Service Complete** | Key working, payment collected |
| **Review Requested** | 2hr post-job review ask |
| **Spare Key Offer** | 24hr follow-up — offer transponder key duplication before they need it again |
| **Scheduled Service** | Planned key replacement, programming, ignition work |

**Automotive Intake Requirements (compliance/liability):**
- Year / Make / Model / Trim
- VIN number (partial or full)
- Proof of ownership (registration or ID + registration photo)
- Color of vehicle + parking location

**Key Service Tags:**
- `auto-lockout`
- `transponder-key`
- `key-fob-replacement`
- `smart-key-programming`
- `ignition-cylinder`
- `broken-key-extraction`
- `duplicate-car-key`

---

### Pipeline 5: Safe Opening & Vault Services

**Purpose:** Manage safe opening, combination change, safe repair, and vault work.

| Stage | Description |
|---|---|
| **Intake — Safe Type Assessment** | Brand (SentrySafe, Fort Knox, Liberty, Gardall), lock type, issue type |
| **Triage — Emergency vs Scheduled** | Contents urgency determines response time |
| **Quote Sent** | Non-destructive attempt estimate vs destructive opening price |
| **Appointment Booked** | Date/time confirmed, technician scoped for job type |
| **Job Attempted — Non-Destructive** | Manipulation, scope probing, technical opening |
| **Job Complete** | Safe opened, combination reset or new lock installed |
| **Review Requested** | Standard review ask |
| **Combination Reset / New Safe Consult** | If destroyed: new safe recommendation and quote |

**Safe Categories (for intake and scoping):**
- **Gun safes:** Combination lock, biometric lock, electronic keypad
- **Fire safes:** Paper, media, data protection ratings
- **Floor safes:** Recessed floor installation
- **Wall safes:** Residential concealed
- **Commercial vault:** Bank-style, walk-in
- **Jewelry safe / cash safe:** Small format
- **Import safes:** SentrySafe, Honeywell (lower security, locksmith-friendly opening)
- **High-security safes:** Gardall, Fort Knox, American Security, AMSEC (requires safe cracking specialists)

**Key Information at Intake:**
- Safe brand and model number (if visible)
- Type of lock (combination dial, electronic keypad, biometric)
- Nature of problem (forgotten combination, dead battery, jammed bolt, broken dial)
- Contents urgency (emergency documents, firearms, cash)
- Last time safe was opened successfully

---

## 6. WORKFLOW DESIGN {#workflow-design}

### Workflow 1: Missed Call Text Back — Emergency Priority (CRITICAL)

**This is the single most important workflow in the snapshot.**

**Trigger:** Inbound missed call to the locksmith's GHL phone number

**Delay:** 0 seconds (immediate)

**Step 1 — Instant SMS (0 seconds after missed call):**
```
Hi, this is [Business Name] Locksmith! We just missed your call. Are you locked out or need emergency service? Reply YES and we'll call you right back within 2 minutes. 

— [Tech Name / Dispatch]
📍 Licensed & Insured | License #[XXXXX]
```

**Step 2 — If no reply after 3 minutes:**
```
Still there? We don't want to miss you. If you need a locksmith right now, reply HELP and we'll prioritize your call immediately.
```

**Step 3 — If no reply after 8 minutes:**
Internal notification to owner/dispatcher: "Lead went cold — [phone number] called at [time]. Consider calling back directly."

**Step 4 — If YES or HELP reply received:**
- Immediate internal alert to owner/tech (push notification + SMS)
- Automated SMS to customer: "Great — calling you back right now. One moment!"
- Lead moves to "Contacted — Awaiting Location" stage

**Branch: Automotive vs Residential vs Commercial**
If initial text response contains keywords like "car", "vehicle", "locked in", "keys inside" → tag `automotive-emergency` → trigger Automotive Intake SMS sequence

---

### Workflow 2: Emergency Dispatch Confirmation

**Trigger:** Lead moves to "Dispatched" stage

**SMS to Customer (immediate):**
```
[FIRST NAME], your locksmith is on the way! 

Technician: [Tech Name]
ETA: [X] minutes
Contact: [Tech Phone]

We'll text you when they're 5 minutes away. 

⭐ Licensed & Insured | [Business Name]
License #[XXXXX]
```

**SMS to Customer (5 minutes out):**
```
[FIRST NAME] — your locksmith is almost there! [Tech Name] is 5 minutes away. 

Please have your ID ready. We verify identity on all residential calls for your security. 🔐
```

---

### Workflow 3: Post-Job Review Request

**Trigger:** Lead moves to "Job Complete" stage  
**Delay:** 2 hours (allow customer to settle, test the key, get inside)

**Step 1 — SMS (2 hours post-job):**
```
Hi [FIRST NAME], thanks for trusting [Business Name] today! 

Quick favor — would you mind leaving us a Google review? It takes 60 seconds and helps families in [City] find a trustworthy locksmith instead of a scam company. 

👉 [Google Review Link]

— [Tech Name], [Business Name]
```

**Step 2 — If no review after 48 hours:**
```
[FIRST NAME] — one last ask! A quick review makes a huge difference for a local business like ours. Scam locksmiths have tons of fake reviews — your honest one helps real people. 🙏

[Google Review Link]

No pressure — just means a lot. Thanks!
```

**Step 3 — Negative Review Interception (if using GHL reputation management):**
If response/survey rating is 1–3 stars before posting → immediate internal alert → owner calls personally → attempt resolution before review goes public

---

### Workflow 4: Residential Security Upgrade Upsell Sequence

**Trigger:** Job type = Emergency Lockout OR Rekey  
**Delay:** 24 hours post-job (let customer get comfortable first)

**Step 1 — Email (Day 1):**
```
Subject: Quick security tip after today's lockout

Hi [FIRST NAME],

Glad we got you back in safely today! Now that you're in — one thing worth considering:

Most lockouts happen because standard Kwikset and Schlage locks are easy to pick, bump, or copy without authorization.

If you want to make sure this never becomes a security issue, we offer:

✅ Bump-resistant / pick-resistant deadbolts (starting at $X installed)
✅ High-security key systems — keys that can't be duplicated at Home Depot
✅ Smart lock installation — unlock with your phone, no keys needed
✅ Full home rekey to a master key system

Reply to this email or call [Phone] for a free security consult.

— [Tech Name]
[Business Name] | Licensed & Insured
```

**Step 2 — SMS (Day 4):**
```
[FIRST NAME] — did you know most lockouts are preventable? A bump-resistant deadbolt + restricted key system means you control exactly who has a copy. We install Schlage, Medeco, and Mul-T-Lock. Interested in a free estimate? Reply YES.
```

**Step 3 — Email (Day 10 — Seasonal angle if applicable):**
```
Subject: Spring security audit — is your home ready?

[FIRST NAME],

Spring is peak season for break-ins in [City]. It's also the most common time people realize their locks haven't been updated in years.

A quick home security audit covers:
🔐 Deadbolt condition and grade rating
🔑 Key control — who has copies?
🚪 Door frame strength (most break-ins are kick-in attacks, not lock picking)
📱 Smart lock readiness

30-minute visit, no obligation. Book here: [Calendar Link]
```

---

### Workflow 5: Automotive Locksmith Follow-Up — Spare Key Offer

**Trigger:** Automotive lockout job completed  
**Delay:** 24 hours

**SMS:**
```
[FIRST NAME] — glad we got you back in your [Vehicle] yesterday! 

Quick thought: a transponder key duplicate costs $[X] and could save you $[Y] next time. Most auto dealers charge 3x what we do. 

Want a spare key programmed? Usually takes under 30 minutes. Reply SPARE and we'll set it up. 🔑
```

**Email (Day 3):**
```
Subject: Don't get stranded again — [Vehicle] spare key offer

Hi [FIRST NAME],

Nobody plans to get locked out. But having a properly programmed transponder key or key fob spare means the next lockout is solved in 10 minutes — not a stressful roadside call.

For your [Year] [Make] [Model], we can program:
✅ Transponder key (chip key) — $[X]
✅ Smart key / proximity key fob — $[X]
✅ OBD programming (newer vehicles) — included

Most dealers charge $[Y]–$[Z]. We do it at our shop or at your location.

Book a spare key appointment: [Calendar Link]
```

---

### Workflow 6: Commercial Account Nurture — Property Manager

**Trigger:** Contact tagged `property-manager` or `commercial-prospect`  
**Delay:** Drip over 30 days

**Day 0 — SMS (initial outreach or post-meeting follow-up):**
```
Hi [FIRST NAME], it's [Your Name] from [Business Name]. Great connecting today! I'll send over some info on how we support property managers in [City] with master key systems and access control. Any questions, I'm at [Phone].
```

**Day 2 — Email:**
```
Subject: How [Business Name] supports property managers in [City]

Hi [FIRST NAME],

Managing [X] units means rekeying is a constant challenge — tenant turnover, lost keys, emergency lockouts at 2am.

Here's how we solve that for property managers like you:

🔑 Master Key System Setup — One master key for you, individual keys per unit. No more carrying 50 keys.

🔄 Priority Rekey Program — Tenant out by noon? Rekeyed by 3pm. Guaranteed turnaround for your portfolio.

🆘 24/7 Emergency Response — Your maintenance line gives us a call. We respond. No wake-up calls for you.

📋 Annual Key Audit — We document every key on your property annually. Huge for liability.

Can we schedule 20 minutes to walk through your portfolio needs?

[Calendar Link]

— [Your Name]
[Business Name]
```

**Day 7 — SMS:**
```
[FIRST NAME] — quick check-in from [Business Name]. Have you had a chance to look at the info I sent? Happy to do a free lock audit on one of your properties to show you how the master key system works. No obligation. — [Name]
```

**Day 14 — Email:**
```
Subject: Tenant lockout at 2am — does your property have a plan?

[FIRST NAME],

One of the most common calls we get from property managers: "I have a tenant locked out at 2am and I can't reach my maintenance guy."

We handle it.

24/7 availability for your portfolio. One call to our number, we're there.

Plus: if you set up a master key system with us, you always have a backup key without keeping a massive key ring. 

15 minutes on a call? [Calendar Link]
```

**Day 21 — SMS:**
```
[FIRST NAME] — not going to keep bugging you, but wanted to leave you with this: we're currently offering a free master key system consultation for property managers managing 10+ units in [City]. Worth 20 minutes. Interested? — [Name]
```

---

### Workflow 7: Move-In Rekey — Real Estate Agent Referral Program

**Trigger:** Contact tagged `real-estate-agent-referral` OR utm_source=realtor  
**Also:** Drip to realtor contacts to generate referrals

**For Homebuyers (referred by agent):**

**Immediate SMS after referral received:**
```
Hi [FIRST NAME]! [Agent Name] suggested we reach out — congrats on your new home! 🏡 

We're [Business Name] Locksmith. We specialize in move-in rekeying — changing all the locks so you know exactly who has keys to your new home. 

Takes about 60 minutes. Would you like a free quote? Reply YES or call [Phone].
```

**Email (Same Day):**
```
Subject: Move-in rekey — the first thing most homeowners forget

Hi [FIRST NAME],

Congratulations on your new home! [Agent Name] connected us because they want to make sure you're set up safely.

Here's the thing most buyers don't know: the sellers had keys. So did their contractor, their dog walker, and probably their ex. 

A move-in rekey costs $[X]–$[X] depending on how many locks you have, and it means you're the only person in the world with a working key to your home.

We can usually get out within 24–48 hours of closing. 

Quote request: [Form Link or Calendar Link]

— [Tech Name]
[Business Name] | Licensed & Insured
```

---

### Workflow 8: Safe Opening — Intake & Triage

**Trigger:** Safe opening form submitted or call tagged `safe-service`

**Intake SMS (immediate):**
```
Hi [FIRST NAME] — we received your safe service request! To make sure we send the right technician, can you tell us:

1. Safe brand (SentrySafe, Fort Knox, American Security, etc.)
2. Lock type: combination dial, electronic keypad, or biometric?
3. What's happening: forgotten combo, dead battery, jammed bolt, or broken dial?

Reply with 1–3 and we'll get you a quote and ETA immediately.
```

---

## 7. LEAD SOURCES & ACQUISITION STRATEGY {#lead-sources}

### Lead Source #1: Google Local Services Ads (LSA) — Emergency Search Dominated

**Reality:** 70–80% of emergency locksmith leads come from Google. When someone is locked out, they search "locksmith near me" on their phone. Google LSA (the "Google Guaranteed" green checkmark) dominates above organic results.

**LSA lead characteristics:**
- Pay per verified lead (not per click)
- Average $25–$80 per lead in major markets
- Lead arrives via phone call — needs instant response
- Competitive: 5–15 locksmiths bidding in most markets

**GHL integration:**
- GHL phone number used as LSA callback number
- All LSA calls trigger missed call text back workflow
- LSA leads tagged `lsa-google` for ROI tracking
- Weekly report: LSA spend vs booked jobs vs revenue

### Lead Source #2: Google Ads (Search & Display)

**Best-performing keywords (by intent):**
- "locksmith near me" (emergency, highest intent)
- "locked out of house" (emergency)
- "car locksmith [city]" (automotive emergency)
- "rekey house after moving" (residential planned)
- "master key system [city]" (commercial, planned)
- "transponder key [year make model]" (automotive planned)
- "safe opening locksmith" (safe, planned or emergency)

**GHL integration:**
- UTM parameters tracked in contact record
- Separate pipeline stages for Google Ads vs LSA vs organic
- Abandoned booking follow-up: if someone clicked, visited booking page, didn't book — retargeting SMS

### Lead Source #3: Referrals — Real Estate Agents

**This is the highest-LTV lead source and the most underutilized.**

When someone buys a home, they almost always need:
1. Move-in rekey (every lock on the property)
2. Often a deadbolt upgrade
3. Sometimes a smart lock or keypad entry
4. Average ticket: $250–$600

**Referral partner development:**
- Target: Buyer's agents (they interact with the buyer just before close)
- Pitch: "We make you look good to your clients. They get a safer home. You get a trusted vendor to refer."
- Incentive: Referral fee ($25–$50 per completed job), OR "We'll mention your name on every job and send a thank-you card to your client"

**GHL system for agent referral program:**
- Agent gets a unique referral link to a landing page
- Buyer fills out form → tagged with agent's name → enters move-in rekey pipeline
- Agent gets automatic notification when job is booked and completed
- Monthly report: "Here are the 3 families you helped this month"

### Lead Source #4: Property Managers & Apartment Complexes

**Why this matters:** One property manager = 20–200+ rekeying jobs per year. This is the commercial account that makes or breaks a locksmith's recurring revenue.

**How to find them:**
- Apartment association directories
- LinkedIn search: "property manager [city]"
- Drive neighborhoods — note management company signs on rental buildings
- Network through real estate agents (they know property managers)

**GHL outreach sequence:** Dedicated 30-day commercial nurture drip (see Workflow 6)

### Lead Source #5: Automotive Dealers — Spare Key Program

**Opportunity:** When a used car is sold, the buyer often doesn't have a second key. Dealers don't want the liability/cost of key programming. An aftermarket locksmith can offer a referral program:

- "We'll program a spare transponder key for your used car buyers at a discounted rate, same-day."
- Dealer refers buyers, locksmith does the work, dealer looks like a hero
- Average ticket: $150–$350

**GHL system:**
- Dealer gets referral landing page
- Buyer enters automotive pipeline
- Dealer gets monthly referral summary

### Lead Source #6: Insurance Referrals (Post-Break-In)

After a home break-in, insurance adjusters often recommend security upgrades. Locksmiths who establish relationships with insurance adjusters get a stream of post-claim security upgrade referrals.

- Target: Independent insurance agents, claims adjusters
- Service: Post-break-in security consultation + upgrade
- Ticket: $500–$2,500 (full lock replacement, high-security upgrade, door frame reinforcement)

---

## 8. SMS & EMAIL TEMPLATES {#templates}

### Emergency Response Templates

**Template E-1: Missed Call — Immediate (0 seconds)**
```
Hi! [Business Name] Locksmith here — we just missed your call. 

Are you locked out or need emergency help? Reply YES and we'll reach you in 2 minutes.

📞 Or call back: [Phone]
🔐 Licensed & Insured | [City]
```

**Template E-2: Emergency Confirmation (Dispatch)**
```
[FIRST NAME] — we're on our way! 

🔑 Tech: [Name]  
⏱ ETA: [X] minutes  
📱 Direct: [Tech Phone]  

Have your ID ready (we verify on all calls for your safety).
```

**Template E-3: 5-Minute ETA Warning**
```
[FIRST NAME] — almost there! Your locksmith is 5 minutes away. Please be at [Address] or reply with updated location. 🚐
```

**Template E-4: After-Hours Emergency (AI Voice or Auto-Response)**
```
[Business Name] — after hours emergency line. We handle lockouts 24/7. 

Reply your ADDRESS and we'll call you back within 5 minutes with ETA and pricing. 

⚠️ Note: After-hours rates apply. We'll quote before we come.
```

---

### Review Request Templates

**Template R-1: Primary Review Request (2hr post-job)**
```
[FIRST NAME] — hope you're all set! Quick favor: would you leave us a Google review? 

Fake locksmith scams are everywhere, and your honest review helps real families in [City] find a trustworthy tech. Takes 60 seconds:

⭐ [Google Review Link]

Thanks so much — [Tech Name]
```

**Template R-2: Follow-Up Review Request (48hr)**
```
Hi [FIRST NAME]! One more quick ask — a Google review from you would mean the world to a local locksmith trying to stand out from the scam companies. 

Even just a few words and a star rating helps! 

[Google Review Link]

No pressure. Thanks for your business! 🙏
```

**Template R-3: Internal Alert — Negative Review Risk**
```
⚠️ ALERT — [FIRST NAME] [LAST NAME] gave a low satisfaction score after their job at [Address] on [Date].

Service type: [Tag]
Technician: [Name]
Job notes: [Notes]

Recommend calling personally within 1 hour to resolve before a public review is posted.
```

---

### Residential Upgrade Templates

**Template U-1: Security Upgrade Offer (24hr post-lockout)**
```
[FIRST NAME] — now that you're back in, one quick thought:

Standard Kwikset/Schlage locks can be bumped or picked in under 60 seconds. Want to make sure your home is actually secure?

We install bump-resistant, pick-resistant deadbolts and high-security key systems where only YOU control who gets a copy.

Free estimate? Reply YES. 🔐
```

**Template U-2: Rekey Offer (post-move-in)**
```
[FIRST NAME] — congrats on the new home! 🏡 One thing most buyers forget: the sellers had keys. 

A full home rekey means fresh locks — you're the only keyholder. Takes 60 min, starts at $[X].

Interested? Book here: [Link] or reply YES.
```

**Template U-3: Smart Lock Upsell**
```
[FIRST NAME] — ever wish you could let the dog walker in without leaving a key? Or check if you locked up when you're already at work?

We install Schlage Encode, August, and Yale smart locks. Works with your phone. No keys, no copies, no lockouts.

Starting at $[X] installed. Worth a look? [Calendar Link]
```

---

### Automotive Templates

**Template A-1: Auto Lockout Response**
```
[Business Name] Auto Locksmith — got your request!

To get the right tech to you fast:

1. What's your vehicle? (year/make/model)
2. What's your exact location or cross streets?

Reply now — we're standing by. 🚗🔑
```

**Template A-2: Spare Key Follow-Up (24hr)**
```
[FIRST NAME] — glad we got you back in your [Vehicle]!

Quick tip: a transponder key spare costs $[X] and saves you a lockout fee next time. Most dealers charge $[Y]–$[Z]. We do it in 30 min.

Want a spare key? Reply SPARE and we'll get you booked. 🔑
```

**Template A-3: Key Fob / Smart Key Offer**
```
[FIRST NAME] — does your [Vehicle] use a key fob or push-to-start? 

If you only have one, you're one lost fob away from a tow truck. We program OEM-quality key fobs for most makes — usually cheaper than the dealer and faster.

Interested? [Calendar Link]
```

---

### Commercial Templates

**Template C-1: Initial Property Manager Outreach**
```
Hi [FIRST NAME] — I'm [Name] with [Business Name] Locksmith. We work with property managers in [City] on master key systems, tenant rekeys, and 24/7 emergency lockouts.

If you're juggling 10+ units, I'd love to show you how we make key management simple. 20-min call this week?

[Calendar Link]
```

**Template C-2: Commercial Account — Staff Changeover Trigger**
```
[FIRST NAME] — quick heads up from [Business Name]:

If you've had any staff changes recently, now's a good time to rekey or update your master key system. It's the #1 security risk most businesses don't address until it's too late.

We do priority commercial rekeying with same-day or next-day turnaround. Need it done? Call [Phone] or reply YES.
```

**Template C-3: Annual Audit Reminder**
```
[FIRST NAME] — your annual key audit is coming up!

Per our account agreement, we recommend reviewing your master key system annually to:

🔑 Document all outstanding keys
🔄 Rekey locks with high key turnover
📋 Update access levels for staff changes
🔒 Identify worn or compromised hardware

Schedule your audit: [Calendar Link]

— [Business Name] Commercial Team
```

---

### Safe Opening Templates

**Template S-1: Safe Intake Response**
```
[Business Name] Safe Tech here — got your request!

To quote you accurately and fast, I need:

1. Safe brand (SentrySafe, Fort Knox, Liberty, Gardall, etc.)
2. Lock type: combo dial 🔢 / electronic keypad 🔢 / biometric 👆
3. The issue: lost combo / dead battery / jammed / broken dial?

Reply with answers and I'll get you a quote in minutes. 🔐
```

**Template S-2: Safe Opening Quote Confirmation**
```
[FIRST NAME] — thanks for the info!

Based on your [Safe Brand] with [Lock Type], here's what we're looking at:

Non-destructive opening attempt: $[X]–$[X]
(We try to open without damage first — success rate ~[X]%)

If non-destructive isn't possible: $[X] (drilling/destructive entry — safe may need new lock installed)

Want to book? We can be there [Date/Time Options].

Reply to confirm or call [Phone]. 🔐
```

---

## 9. BOOKING FLOW ARCHITECTURE {#booking-flow}

### The Two-Track Booking Philosophy

The locksmith industry has two fundamentally different customer types that require completely different booking experiences:

**Track 1 — EMERGENCY (No Friction)**
- Customer is stressed, locked out, can't get to a computer
- Must work on mobile, single-hand operation
- Goal: Capture location and call back within 2 minutes
- Do NOT send them to a calendar. Do NOT make them fill out 10 fields.
- Ideal flow: Text "YES" → immediate callback → verbal intake

**Track 2 — SCHEDULED SERVICE (Normal Booking Flow)**
- Customer is planning ahead (rekey, commercial, upgrade)
- Can use a full booking form + calendar
- Wants price transparency before booking
- Follow-up sequences make sense here

---

### Emergency Booking Flow (Track 1)

```
[Customer calls → Missed Call Text Back FIRES INSTANTLY]
→ Customer replies YES/HELP
→ Internal alert to tech/dispatcher
→ Tech calls customer directly
→ Verbal intake: address, issue type, vehicle info if auto
→ Tech dispatched
→ Confirmation SMS auto-fires with ETA
→ 5-minute SMS fires when tech is close
→ Post-job: Stage moves to Complete → review request fires at +2hr
```

**Do NOT include:**
- A 10-question intake form for emergencies
- Calendar selection (they need someone NOW, not "book for Thursday")
- Pricing calculator that requires 15 minutes of research

**DO include:**
- One-click-to-call button in SMS (most will just call back)
- Simple reply options (YES, LOCATION, HELP)
- Real-time dispatch tracking if technician uses GHL mobile app

---

### Scheduled Service Booking Flow (Track 2)

```
[Customer fills form / clicks booking link]
→ Service type selector:
   - Residential Rekey
   - Lock Upgrade / Installation
   - Commercial Locksmith
   - Automotive (Spare Key / Programming)
   - Safe Service
   - Other
→ Service-specific intake questions load
→ Calendar availability (real-time via GHL calendar)
→ Confirmation email + SMS fire immediately
→ 24hr reminder email
→ 1hr reminder SMS
→ Post-job review sequence begins at +2hr
```

**Residential Rekey Form Fields:**
- Full name, address, phone, email
- Number of exterior doors
- Lock brand currently installed (Kwikset, Schlage, Deadbolt only, Mortise, Other)
- Reason for rekey (move-in, lost keys, security concern, after break-in, other)
- Access control interest (simple yes/no — for upsell tagging)

**Commercial Form Fields:**
- Business name, contact name, phone, email
- Property type (office, retail, multi-family, industrial, restaurant, other)
- Number of doors / units
- Current key system (single key, master key, access control, none/unknown)
- Primary need (rekey, master key, access control, emergency service account, other)
- Best time to call

**Safe Service Form Fields:**
- Name, phone, email, address
- Safe brand (dropdown)
- Lock type (combination dial, electronic keypad, biometric, unknown)
- Problem (forgot combo, dead battery, jammed/won't open, broken hardware, other)
- Urgency (today, within 3 days, within a week, flexible)

---

## 10. MOVE-IN REKEY CAMPAIGN — REAL ESTATE AGENT REFERRAL PROGRAM {#rekey-campaign}

### Program Overview: "Safe Keys for New Homeowners"

**Concept:** Every real estate agent in the area becomes a referral partner. When they close a sale, they hand the buyer a card or send a text saying "[Agent Name] recommends [Business Name] for your move-in rekey — here's a discount code." Buyer calls locksmith, locksmith rekeyes the home, agent looks good to their client.

**Why agents love this:**
- Adds value to their service at zero cost
- They look like they thought of everything
- Touchpoint to stay in front of the new homeowner (future re-listing?)
- Local agent community respects businesses that give back

**Why the locksmith loves this:**
- Average move-in rekey = $250–$600
- Very low cancellation rate (they're motivated — they just bought a house)
- Easy upsell to smart lock, deadbolt upgrade, keypad
- First service = relationship = future calls for lockouts, commercial, etc.

---

### Referral Partner Setup in GHL

**Step 1: Create Real Estate Agent Contact Type**
- Tag: `referral-partner-realtor`
- Custom field: Agent Name, Brokerage, Referral Count (tracked), Referral Revenue (tracked)
- Add to "Partner" pipeline (separate from client pipeline)

**Step 2: Create Unique Agent Landing Page**
- URL: `[businessname].com/agent/[agentname]`
- Page: Simple form — "Your agent [NAME] sent you here. Get your move-in rekey quote."
- Form captures: homebuyer name, address, closing date, phone, email
- Form auto-tags with agent name
- Confirmation: "We'll reach out within 2 hours to confirm your appointment!"

**Step 3: Homebuyer Entry Sequence**
- Immediate SMS: Welcome + intro (see Template R above)
- Day 0 email: Move-in rekey explainer + booking link
- Day 2 SMS: "Ready to book? Closes this week = we can be there the day you get keys."
- Day 5 (if no booking): Last nudge email

**Step 4: Agent Notification Automation**
- When homebuyer books: Agent gets SMS "Your referral [BUYER NAME] just booked a rekey at [Address] — thanks [AGENT NAME]!"
- When job completes: Agent gets SMS "Job done! [BUYER NAME] is all set. Thanks for the referral."
- Monthly: Agent gets email summary of their referrals, jobs, and impact

---

### Real Estate Agent Outreach Sequence (Cold Outreach to Build Partner Network)

**Day 1 — Cold SMS:**
```
Hi [AGENT NAME], it's [Your Name] at [Business Name]. I work with [X] realtors in [City] on move-in rekeying for their buyers. Would love 10 min to show you how it works — zero cost to you, big value for your clients. This week work? — [Name]
```

**Day 1 — Email:**
```
Subject: Something to offer your next buyer at closing

Hi [AGENT NAME],

One thing I've noticed working with realtors in [City]: buyers love it when their agent gives them a referral for a move-in rekey.

Here's why it lands well:
- It's a safety issue they haven't thought about (sellers had keys)
- It adds a real service to your closing experience
- You look organized and client-focused

We do move-in rekeying same-day or next-day, fully licensed, flat rate.

10 minutes on a call this week? I can show you how it works.

[Calendar Link]

— [Name]
[Business Name]
```

**Day 7 — Follow-Up SMS:**
```
[AGENT NAME] — any chance you had a minute to look at that move-in rekey program? We've been sending [X] referrals/month to agents in [City] who partner with us. Just wanted to make sure you had the info. — [Name]
```

---

## 11. COMMERCIAL MASTER KEY SYSTEM WORKFLOW {#commercial-master-key}

### What Is a Master Key System?

A master key system (MKS) is a mechanical keying arrangement where:
- **Individual keys** open only specific locks (a unit key opens only apartment 4B)
- **Master keys** open multiple or all locks (maintenance master opens all apartments)
- **Grand master keys** open everything in a multi-property system
- **Change keys** are the lowest level — one key per one lock

**Why property managers, offices, and schools love it:**
- Maintenance staff carries one key instead of 50
- Management has access to everything without carrying a jailhouse ring
- Tenant privacy maintained (their key only opens their unit)
- Can add submaster levels (floor master, building master, campus master)

**Lock brands used in commercial MKS:**
- **Schlage C keyway, D keyway** — commercial grade 1 and 2
- **Kwikset Titan** — lower-end commercial
- **Best CORMAX** — patented key system, high security, restricted
- **Medeco** — high security, UL listed, restricted
- **ASSA Abloy** — global leader, high security, commercial
- **Mul-T-Lock** — patented, anti-bump, anti-pick, high security
- **Sargent, Corbin Russwin** — heavy commercial, institutional

---

### Commercial Master Key System Pipeline (Detail)

**Stage 1: Prospect — Initial Contact**
- Source: cold outreach, referral, property manager drip, trade show
- Actions: Tag as `commercial-mks-prospect`, enter 30-day nurture sequence

**Stage 2: Needs Assessment Call**
- Collect: Property type, # of doors, # of locks, current key situation, key control issues
- Key questions:
  - "How many staff members need access to all areas vs limited areas?"
  - "Do you have unauthorized key copies floating around?"
  - "Have you ever had a security incident related to key access?"
  - "Are you interested in a system where keys can't be duplicated without your permission?"

**Stage 3: Site Survey (For Large Properties)**
- Walk-through of property
- Door count, lock inventory, hardware assessment
- Identify worn hardware, mismatched keyways, security gaps
- Photograph all hardware
- Deliver survey report (GHL document or PDF)

**Stage 4: Master Key System Design**
- Determine key hierarchy (1-level, 2-level, 3-level)
- Select lock series (brand, grade, keyway)
- Determine restricted key control (patented keyway vs standard)
- Pinning specification prepared

**Stage 5: Proposal Delivery**
- Itemized quote: labor + hardware
- Timeline: Installation schedule
- Warranty: Hardware + labor
- Key control policy recommendation

**Stage 6: Contract + Deposit**
- Proposal accepted
- 50% deposit collected
- Materials ordered
- Installation scheduled

**Stage 7: Installation**
- Rekeying or new lock installation per MKS design
- Key issuance log created (who received which key)
- Owner / manager receives master + grand master
- Each keyholder signs receipt

**Stage 8: Account Setup — Recurring Service**
- Annual audit scheduled (automatically created in GHL)
- Rekey reminders: tied to lease end dates (for multi-family)
- Staff turnover trigger: "Any staff changes? Time to review access."
- Emergency response account: Property manager gets 24/7 priority line

---

### Commercial MKS Upsell Path: Access Control Integration

Once a commercial client has a master key system:
- Next natural upgrade: key fob or card reader access control
- Eliminate physical keys entirely for high-traffic doors
- Add video intercom (buzzer system integration)
- Connect to property management software

**Products typically used:**
- **Schlage Engage** — cloud-based, smartphone management, no wiring
- **LiftMaster** — gate and parking access
- **Brivo** — cloud-based access control for commercial
- **Salto** — wireless electronic locks, suitable for hotel/multifamily
- **Dormakaba** — institutional access control, full credential management

---

## 12. REVIEW GENERATION STRATEGY {#review-generation}

### Why Reviews Are Existential in the Locksmith Industry

The locksmith industry has a documented scam problem. The FTC, FBI, and hundreds of local news stations have run investigations on "fake locksmith" operations — companies that create dozens of fake local business listings, quote $35 over the phone, then charge $400+ on arrival.

The consumer consequence: homeowners who search "locksmith near me" are suspicious. When they see a locksmith with 4 reviews vs one with 200+ five-star reviews, the choice is obvious. A legitimate locksmith with 150+ Google reviews wins over a technically superior locksmith with 12 reviews every single time.

**Review targets for GHL snapshot KPIs:**
- Month 1–3: 20+ new reviews (catching up to baseline)
- Month 3–6: 50+ cumulative reviews
- Month 6–12: 100+ reviews, 4.7+ average
- Ongoing: 5–10 new reviews per month minimum

---

### Review Generation System Architecture

**Step 1: Trigger — Job Complete Stage**
Every completed job triggers the review sequence. No exceptions.

**Step 2: Timing**
- 2 hours after job: Primary review SMS
- 48 hours after job: Secondary review SMS (if no review posted)
- 7 days after job: Review email (last attempt, softer tone)

**Step 3: Negative Review Interception**
Before the review goes public, collect a satisfaction signal:
- Immediately after job (in-person or SMS): "On a scale of 1–5, how was your experience today?"
- If 4–5: Thank them, immediately send review link
- If 1–3: Trigger internal alert, DO NOT send public review link, owner calls to resolve

**Step 4: Response Protocol (Manual, but templated)**
- Every 5-star review gets a personal response within 24 hours
- Every negative review gets a response within 2 hours (damage control)
- Template responses loaded in GHL conversation AI or notes

**Step 5: Platform Priority**
1. **Google Business Profile** — Primary. Most locksmith searches happen on Google.
2. **Yelp** — Secondary. Many cities use Yelp heavily for local services.
3. **Facebook** — For community-based referrals and trust.
4. **BBB** — Some commercial clients check BBB before signing contracts.

---

### Review Response Templates

**5-Star Response:**
```
Thank you so much, [NAME]! It was a pleasure helping you today. We know being locked out is stressful — glad we could get you sorted quickly. We appreciate you taking the time to share your experience. [Business Name] is always here when you need us! 🔐
```

**1–2 Star Response:**
```
Hi [NAME], we're very sorry to hear about your experience. This is not the standard of service we hold ourselves to. We'd like to make this right — please reach out to us directly at [Phone] so we can address your concerns personally. Thank you for the feedback.
```

---

## 13. PROPERTY MANAGER ACCOUNT WORKFLOW {#property-manager}

### Property Manager Account Tiers

**Tier 1 — Small Portfolio (5–20 units)**
- Likely self-managing or small management company
- Needs: Quick rekey on tenant turnover, 24/7 emergency response
- GHL approach: Add to commercial pipeline, automated rekey reminder at end of lease

**Tier 2 — Mid Portfolio (20–100 units)**
- Property management company (often manages multiple properties)
- Needs: Master key system, priority rekey SLA, annual audit
- GHL approach: Full commercial account setup, monthly reporting, dedicated contact

**Tier 3 — Large Portfolio (100+ units)**
- Professional property management company or HOA management
- Needs: Access control, ongoing account management, volume pricing
- GHL approach: Contract client, quarterly reviews, custom proposal

---

### Property Manager Automation — Lease Cycle Triggers

**Custom Field Setup:**
- Lease End Date (added to contact record)
- Number of Units
- Master Key System (yes/no)
- Priority Account (yes/no)
- Last Rekey Date

**Automated Triggers:**
- 60 days before lease end: "Tenant turnover coming up — ready to schedule your rekey?"
- 30 days before lease end: "Rekey reminder — want to book now to guarantee availability?"
- 7 days before lease end: "Your tenant moves out [DATE] — we're available [DATE+1 or DATE+2]. Confirm?"
- Post-rekey: "Unit rekeyed — new keys issued: [TENANT NAME] (2 keys). Master key retained by [MANAGER NAME]."

**Annual Audit Trigger:**
- 1 year after master key system installation: "Time for your annual key audit. Want to schedule?"
- 2-week reminder if not booked
- 1-week reminder if still not booked

---

### Property Manager Reporting (Monthly Email)**
```
Subject: [Business Name] — Your Monthly Locksmith Summary ([Month])

Hi [FIRST NAME],

Here's your locksmith activity summary for [Month]:

📋 Units Rekeyed: [X]
🔑 Keys Issued: [X]
🆘 Emergency Calls: [X]
⏱ Average Response Time: [X] minutes
📅 Upcoming Rekey Schedule: [List]

Next audit due: [Date]

Any questions or upcoming changes, reach out at [Phone].

— [Business Name] Commercial Team
```

---

## 14. SNAPSHOT DIFFERENTIATORS {#differentiators}

### What Makes the 1app Locksmith Snapshot Category-Defining

**1. Emergency-First Architecture**
Most snapshots treat all leads equally. This snapshot is built emergency-first. The missed call text back fires in 30 seconds. The pipeline stages are triage-based. The booking flow branches based on emergency vs scheduled. No other locksmith snapshot on the market does this correctly.

**2. The Trust Stack (Anti-Scam Positioning)**
Every automated message includes the business's license number. Confirmation messages mention identity verification. Review requests explicitly reference the fake locksmith problem to make the ask feel important, not annoying. This is differentiation baked into the copywriting.

**3. Five Dedicated Pipelines**
Emergency, Residential, Commercial, Automotive, Safe. Each service type has its own pipeline, workflow logic, and SMS/email sequences tailored to that customer's situation. Zero cross-contamination.

**4. Real Estate Agent Referral System**
Built-in partner program with agent-specific landing pages, automated referral tracking, and agent notification sequences. No other locksmith snapshot includes this. This is the highest-LTV lead source in the industry and it's completely ignored by every existing template.

**5. Commercial Master Key Account Management**
Lease-cycle triggers, annual audit automation, master key issuance logging, staff-turnover rekey reminders. Purpose-built for property managers and commercial clients.

**6. Automotive Locksmith-Specific Intake**
Proof of ownership capture, year/make/model/VIN intake, transponder key follow-up sequence, dealer referral program. Automotive is treated as its own service category with its own logic.

**7. Safe Opening Triage**
Non-destructive vs destructive quote logic, safe brand/type intake, urgency routing. No existing snapshot handles safe services properly.

**8. Reputation Protection System**
Pre-review satisfaction signal, negative review interception, manual escalation before public posting. This is critical in an industry where one fake-looking review pattern can destroy credibility.

**9. Property Manager Lifecycle Automation**
Lease-end triggers, annual audits, monthly reporting emails, priority SLA tracking. Turns one-time rekeying jobs into recurring commercial accounts.

**10. Google LSA + Google Ads ROI Tracking**
UTM tracking baked in, LSA lead tagging, cost-per-job attribution. Locksmith owners spending $2,000+/month on Google Ads with zero ROI visibility finally see which campaigns are working.

---

## 15. FULL SNAPSHOT COMPONENT CHECKLIST {#component-checklist}

### Pipelines (5)
- [ ] Emergency Lockout Pipeline (8 stages)
- [ ] Residential Lock Services Pipeline (9 stages)
- [ ] Commercial Locksmith & Access Control Pipeline (11 stages)
- [ ] Automotive Locksmith Pipeline (8 stages)
- [ ] Safe Opening & Vault Services Pipeline (7 stages)

### Workflows (15+)
- [ ] Missed Call Text Back — Emergency Priority (30-second trigger)
- [ ] After-Hours Emergency Intake (AI response / SMS)
- [ ] Emergency Dispatch Confirmation (ETA SMS)
- [ ] 5-Minute ETA Warning SMS
- [ ] Post-Job Review Request Sequence (2hr, 48hr, 7-day)
- [ ] Negative Review Interception Alert
- [ ] Residential Security Upgrade Upsell (3-touch: 24hr, Day 4, Day 10)
- [ ] Move-In Rekey — Homebuyer Entry Sequence
- [ ] Move-In Rekey — Real Estate Agent Onboarding Sequence
- [ ] Automotive Follow-Up — Spare Key Offer (24hr, Day 3)
- [ ] Commercial Account Nurture — Property Manager (30-day drip)
- [ ] Commercial Staff Changeover Rekey Alert
- [ ] Commercial Annual Audit Reminder Sequence
- [ ] Safe Opening Intake & Triage
- [ ] Property Manager Lease-Cycle Automation (60-day, 30-day, 7-day triggers)
- [ ] Post-Job Confirmation + Receipt Email
- [ ] Google LSA Lead Intake + Tagging Workflow
- [ ] Monthly Property Manager Report Email

### Booking Calendars (3)
- [ ] Emergency / Same-Day Calendar (call-first, minimal friction)
- [ ] Residential Scheduled Services Calendar (standard booking flow)
- [ ] Commercial Consultation Calendar (longer time slots, intake form)

### Forms (6)
- [ ] Emergency Intake Form (minimal — 3 fields max)
- [ ] Residential Scheduled Service Form
- [ ] Commercial / Property Manager Intake Form
- [ ] Real Estate Agent Referral Partner Registration Form
- [ ] Automotive Service Form (with vehicle info fields)
- [ ] Safe Service Intake Form (brand/type/issue)

### Landing Pages (5)
- [ ] Main Locksmith Home Page (trust signals, emergency CTA, services)
- [ ] Move-In Rekey Page (homebuyer focused)
- [ ] Commercial Locksmith Page (property managers, businesses)
- [ ] Real Estate Agent Referral Partner Page
- [ ] Emergency Locksmith Page (SEO-optimized, 24/7 CTA)

### SMS Templates (20+)
- [ ] All templates listed in Section 8 pre-loaded

### Email Templates (12+)
- [ ] All templates listed in Section 8 pre-loaded
- [ ] Post-job receipt / work order confirmation
- [ ] Monthly property manager report
- [ ] Seasonal campaign (spring security audit)
- [ ] Commercial proposal follow-up

### Custom Fields (Per Contact)
- [ ] Service Type (multi-select: Emergency, Residential, Commercial, Automotive, Safe)
- [ ] Lead Source (LSA, Google Ads, Referral, Realtor, Property Manager, Word of Mouth, Other)
- [ ] Vehicle Info (Year / Make / Model) — for automotive contacts
- [ ] Safe Brand — for safe service contacts
- [ ] Property Manager (yes/no)
- [ ] Number of Units (for PM contacts)
- [ ] Lease End Date (for PM contacts)
- [ ] Last Rekey Date
- [ ] Master Key System (yes/no)
- [ ] Referral Partner Name (agent or dealer)
- [ ] License Number Verified (yes/no — for automotive ID verification)
- [ ] Job Notes (free text)
- [ ] Google Review Posted (yes/no)
- [ ] Review Rating (1–5)

### Snapshots / Saved Replies (10)
- [ ] Emergency response (quick reply)
- [ ] ETA confirmation
- [ ] Price quote acknowledgment
- [ ] Appointment confirmation
- [ ] After-hours response
- [ ] Commercial proposal follow-up
- [ ] Dealer referral response
- [ ] Real estate agent onboarding
- [ ] Review request resend
- [ ] Escalation alert (for team use)

### Reports & Dashboards
- [ ] Lead Volume by Source (weekly)
- [ ] Revenue by Service Type (monthly)
- [ ] Review Count + Average Rating (monthly)
- [ ] Emergency Response Time Average (weekly)
- [ ] Commercial Account Pipeline Value
- [ ] Referral Partner Performance (by agent/dealer)
- [ ] Google Ads / LSA ROI (spend vs booked jobs)

### Tags (Pre-Built)
- `emergency-lockout`
- `residential-rekey`
- `deadbolt-upgrade`
- `smart-lock`
- `high-security-lock`
- `bump-resistant`
- `mortise-lock`
- `master-key-system`
- `access-control`
- `key-fob`
- `commercial-prospect`
- `property-manager`
- `auto-lockout`
- `transponder-key`
- `key-fob-replacement`
- `safe-opening`
- `safe-cracking`
- `after-hours`
- `google-lsa`
- `google-ads`
- `realtor-referral`
- `dealer-referral`
- `insurance-referral`
- `review-requested`
- `review-received`
- `negative-review-risk`
- `upsell-offered`
- `commercial-annual-audit-due`
- `lease-end-60-days`
- `automotive-verified`

---

## 16. PRICING & PACKAGING RECOMMENDATIONS FOR 1APP {#pricing}

### Recommended 1app Locksmith Snapshot Tiers

**Tier 1 — Emergency Core ($197/month)**
- Emergency Lockout Pipeline only
- Missed Call Text Back (30-second response)
- After-Hours SMS Response
- Post-Job Review Request Sequence
- Emergency Booking Calendar
- GBP Review Dashboard
- Setup: $497 one-time

**Best for:** Sole-operator locksmiths who primarily do emergency calls. Solves the most critical pain point immediately.

**Tier 2 — Full Residential & Commercial ($297/month)**
- All 5 pipelines
- All 15+ workflows
- All forms, landing pages, and booking calendars
- Residential upgrade upsell sequences
- Commercial account management
- Property manager lifecycle automation
- Real estate agent referral system
- Monthly reporting dashboard
- Setup: $797 one-time

**Best for:** Owner-operators doing mixed residential and some commercial work. Ready to build systems.

**Tier 3 — Enterprise Locksmith Agency ($397/month)**
- Everything in Tier 2
- Google LSA ROI tracking
- Automotive locksmith module (separate pipeline + forms)
- Safe service module
- Dealer referral program
- Commercial master key system workflow
- Custom branding on all pages/templates
- Quarterly strategy call with 1app team
- Setup: $997 one-time

**Best for:** Locksmith businesses with 3+ technicians, multiple service lines, active commercial book.

---

### Sales Talking Points for 1app Reps

**Pain Lead:** "Are you losing leads because you can't answer every call while you're on a job?"
**Pain Lead:** "How many times this month did someone call, go to voicemail, and hire someone else?"
**Pain Lead:** "Do your property manager clients ever complain about slow response on tenant turnover rekeying?"
**Benefit Bridge:** "Our locksmith system fires a text within 30 seconds of a missed call. While you're inside picking a lock, the next customer is already being handled automatically."
**Social Proof:** "We've built this for locksmiths specifically — not a generic home services template. You get emergency dispatch logic, automotive intake, commercial account management, and a real estate referral program built right in."
**Urgency:** "Every missed call is a lost $150–$250 job. At 5 missed calls a week, that's $3,000/month in revenue you're not capturing. Our system costs $297/month."

---

## APPENDIX: KEY INDUSTRY TERMINOLOGY REFERENCE

For agency reps writing copy, training materials, and sales scripts:

| Term | Definition |
|---|---|
| **Deadbolt** | Single cylinder lock with thumb turn, the primary residential security lock |
| **Mortise lock** | European-style lock built into the door body, common in commercial and older buildings |
| **Schlage** | Premium American lock brand; B-series deadbolts are standard residential |
| **Kwikset** | Consumer-grade lock brand; widely installed in new construction |
| **Rekey** | Changing the internal pins of a lock so old keys no longer work, new keys cut |
| **Master key system** | Keying arrangement where hierarchy of keys opens different levels of locks |
| **Restricted keyway** | Patented key profile that can only be duplicated by authorized dealers |
| **High-security lock** | Lock rated to resist picking, bumping, drilling; brands: Medeco, Mul-T-Lock, ASSA Abloy |
| **Bump-resistant** | Lock designed to resist bump key attacks (common forced entry method) |
| **Pick-resistant** | Lock with security pins that resist standard picking techniques |
| **Transponder key** | Car key with embedded chip that communicates with vehicle's immobilizer system |
| **Key fob** | Remote transmitter for vehicle door locks; may or may not contain transponder |
| **Smart key / proximity key** | Keyless entry system; car detects key in pocket, button starts engine |
| **OBD programming** | On-board diagnostics port used to program transponder keys on modern vehicles |
| **Safe cracking** | Non-destructive opening of a locked safe using manipulation or scoping techniques |
| **Non-destructive entry** | Opening a lock or safe without causing physical damage |
| **Destructive entry** | Drilling or cutting a lock/safe open (last resort, safe requires new hardware) |
| **Access control** | Electronic system managing who can enter specific areas (key fob, card, PIN, biometric) |
| **Key fob access** | Proximity card or RFID fob that unlocks door when held near reader |
| **Intercom** | Video or audio entry system at building entrance |
| **Grand master key** | Highest level in a master key hierarchy; opens all locks in a system |
| **Change key** | Lowest level key in a master key system; opens only one specific lock |
| **Submaster** | Intermediate key that opens a subset of locks (e.g., one floor of a building) |
| **Grade 1 lock** | Highest commercial security rating (ANSI/BHMA); required for commercial use |
| **Grade 2 lock** | Medium residential/light commercial security rating |
| **ALOA** | Associated Locksmiths of America — primary professional association |
| **LSA** | Google Local Services Ads — pay-per-lead advertising for local service businesses |
| **GBP** | Google Business Profile (formerly Google My Business) |
| **Schlage Encode** | Smart deadbolt with built-in Wi-Fi, no additional hub required |
| **ASSA Abloy** | Global lock manufacturer (owns Medeco, Sargent, Corbin Russwin, Yale) |
| **Mul-T-Lock** | Israeli high-security lock brand; patented telescoping pins, anti-bump, anti-pick |
| **Medeco** | American high-security lock brand; patented key control, UL listed |
| **Key control** | System ensuring keys cannot be copied without authorization |
| **Lock audit** | Professional inspection of all locks in a facility, documenting condition and key holders |
| **Pinning** | Internal adjustment of lock pins to match a specific key cut |
| **VIN** | Vehicle Identification Number — required for automotive key programming |
| **Immobilizer** | Electronic anti-theft system in vehicles; only programmed transponder key will start engine |

---

*This document is proprietary research prepared for 1app Technologies Inc. for internal use in snapshot development and sales enablement. Not for distribution.*

**Document Status:** Complete  
**Next Step:** Use as build brief for GHL snapshot development  
**Estimated Build Time:** 40–60 hours for full Tier 3 snapshot
