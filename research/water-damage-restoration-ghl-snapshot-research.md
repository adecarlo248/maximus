# Water Damage Restoration — GHL Snapshot Research Document
**1app Technologies Inc. | SaaS Agency Build Reference**
**Document Type:** Pre-Build Research & Architecture Brief
**Vertical:** Water Damage Restoration (Emergency Restoration Services)
**Date:** 2026-07-21
**Classification:** Internal Build Reference

---

## Executive Summary

Water damage restoration is one of the highest-value, highest-urgency home services verticals in North America. Average job value ranges from **$3,500 (minor water extraction) to $45,000+ (full structural drying + reconstruction)**. Emergency response windows are measured in minutes, not hours — the first company to answer wins the job 70–80% of the time.

The vertical is chronically underserved by marketing automation. Most operators run on phone calls, manual follow-up, and paper drying logs. No single GHL snapshot on the market fully solves the dual-track complexity of this business: **emergency dispatch speed** on one track and **insurance claim nurture patience** on the other.

This document is the foundation for 1app's water damage restoration snapshot — built to be the most operationally complete, highest-converting snapshot in this vertical.

---

## Table of Contents

1. [Industry Overview & Terminology](#industry-overview)
2. [Business Pain Points](#business-pain-points)
3. [Competitive Snapshot Landscape](#competitive-landscape)
4. [Pipeline Architecture](#pipeline-architecture)
5. [Workflow Architecture](#workflow-architecture)
6. [Lead Sources & Acquisition Strategy](#lead-sources)
7. [SMS & Email Templates](#sms-email-templates)
8. [Booking & Dispatch Flow](#booking-dispatch-flow)
9. [Insurance Claim Workflow](#insurance-claim-workflow)
10. [Plumber Referral Partnership System](#plumber-referral-system)
11. [Reconstruction Referral Workflow](#reconstruction-referral-workflow)
12. [Daily Monitoring Update Workflow](#daily-monitoring-workflow)
13. [Review Generation System](#review-generation)
14. [Snapshot Differentiators](#snapshot-differentiators)
15. [Technical Build Specs](#technical-build-specs)

---

## 1. Industry Overview & Terminology {#industry-overview}

### What These Companies Do

Water damage restoration companies respond to water intrusion events — burst pipes, flooding, sewage backups, appliance failures, roof leaks, and storm damage — and restore the property to pre-loss condition. Work is divided into:

- **Emergency Services / Mitigation:** Immediately stop the damage. Water extraction, structural drying, dehumidification, moisture mapping.
- **Structural Drying Phase:** Multi-day to multi-week process with daily monitoring. Equipment (dehumidifiers, axial fans, air movers) is placed and readings are taken.
- **Reconstruction:** After drying is certified complete, damaged materials (drywall, flooring, cabinets) are replaced. Often subcontracted or referred.
- **Contents Restoration:** Furniture, belongings removed and restored via pack-out or on-site cleaning.

### Essential Industry Terminology (Use Throughout All Copy)

#### Water Damage Classification (IICRC S500)
| Class | Description | Affected Area |
|-------|-------------|---------------|
| Class 1 | Slow evaporation rate | Part of a room, minimal moisture |
| Class 2 | Fast evaporation rate | Entire room, wall cavities wet |
| Class 3 | Fastest evaporation | Ceiling, walls, insulation, sub-floor |
| Class 4 | Specialty drying | Hardwood, concrete, plaster — low porosity materials |

#### Water Contamination Categories (IICRC S500)
| Category | Description | Common Sources |
|----------|-------------|----------------|
| Category 1 | Clean water | Burst pipe, supply line, rainwater |
| Category 2 | Gray water | Washing machine, dishwasher, sump pump |
| Category 3 | Black water | Sewage backup, floodwater, toilet overflow |

#### Technical Terminology for Credibility
- **IICRC S500** — Standard for Professional Water Damage Restoration (the industry bible)
- **IICRC S520** — Standard for Professional Mold Remediation
- **RH%** — Relative Humidity percentage; target drying standard typically <50% RH
- **GPP** — Grains Per Pound; measures moisture content in air
- **GPP removal rate** — Performance metric for LGR dehumidifiers
- **LGR Dehumidifier** — Low Grain Refrigerant dehumidifier; industry-standard equipment for structural drying
- **Desiccant dehumidifier** — Used for low-temperature or specialty drying situations
- **Axial fan / Air mover** — Directional fans placed to accelerate evaporation from structural surfaces
- **FLIR thermal imaging** — Infrared camera used for moisture mapping to detect hidden moisture behind walls/ceilings
- **Moisture mapping** — Documentation of moisture readings at all affected points, updated daily
- **Psychrometric calculations** — Science of air properties used to determine drying efficiency
- **Structural drying** — Process of removing moisture from structural components (framing, subfloor, drywall)
- **Water extraction** — Physical removal of standing water via truck-mounted or portable extractors
- **Dehumidification** — Removing moisture vapor from air during drying phase
- **Pack-out** — Removing contents (furniture, belongings) to restore off-site
- **Contents restoration** — Cleaning and restoring personal property
- **Sewage backup cleanup** — Category 3 contamination remediation; biohazard protocol required
- **Basement flooding** — Often combines Category 2/3 water with structural drying requirements
- **Scope of work** — Written documentation of all mitigation work performed
- **Certificate of completion** — Final document issued when drying standards are met
- **Xactimate** — Industry-standard estimating software used to price jobs for insurance
- **Xactimate line items** — The specific codes used in insurance estimates; critical for adjuster approval
- **ALE (Additional Living Expenses)** — Insurance coverage for temporary housing when home is uninhabitable
- **Direct billing** — When restorer bills insurer directly vs. homeowner out-of-pocket
- **Assignment of Benefits (AOB)** — Homeowner assigns insurance claim rights to restorer
- **TPA (Third Party Administrator)** — Insurance company programs that route claims to preferred contractors

---

## 2. Business Pain Points {#business-pain-points}

### Pain Point 1: 24/7 Emergency Response Is the Baseline, Not a Differentiator

Water doesn't wait for business hours. Burst pipes happen at 2am on Christmas Eve. Sewage backs up at 11pm on a Sunday. Restoration companies that don't answer within the first 5–15 minutes lose the job to competitors or national TPAs (ServiceMaster, Servpro).

**The problem:** Most small to mid-size operators have no automation to capture, acknowledge, and deploy on missed calls during off-hours. A homeowner in a water emergency who hits voicemail will call the next number immediately.

**What's missing:** Instant SMS response to any call that hits voicemail, with a live "we're on our way" impression even before a human calls back.

### Pain Point 2: Insurance Adjuster Dependency

60–80% of restoration jobs are insurance claims. This creates a dual-client problem: the homeowner is the emotional client, the insurance adjuster is the payment client.

**The problem:**
- Adjusters want documentation, photos, daily logs, and Xactimate estimates
- Operators manually call adjusters and email photos without any systematic follow-up
- No CRM tracking of where each claim is in the adjuster review process
- Slow adjuster approval = slow payment = cash flow pressure

**What's missing:** A separate insurance claim nurture sequence that speaks adjuster language (scope of work, line items, documentation packages) and systematically moves claims forward.

### Pain Point 3: Slow Payment Cycles

Restoration cash flow is brutal. Emergency services done in Day 1–3. Equipment rental running through Day 7–21. Invoice submitted. Adjuster review: 2–4 weeks. Payment: 4–8 weeks.

**The problem:**
- No automated follow-up on unpaid invoices
- No systematic "documentation package complete" notifications to adjusters
- No homeowner communication that sets payment timeline expectations

**What's missing:** Invoice follow-up automation and adjuster touchpoint sequences that accelerate claim approval.

### Pain Point 4: Equipment Utilization & Tracking

LGR dehumidifiers rent for $150–300/day. Axial fans at $50–100/day. A full Class 3 setup can have $2,000+/day of equipment on-site. Equipment sitting idle or placed on jobs incorrectly destroys margins.

**The problem:** No CRM connection to equipment placement, daily readings, or drying completion milestones.

**What's missing:** Daily monitoring workflow that prompts techs to log GPP/RH% readings and auto-notifies the homeowner.

### Pain Point 5: No Marketing System — Living on Word of Mouth and Insurance Networks

Most restoration companies have zero marketing infrastructure. They rely on:
- Insurance TPA networks (ServiceMaster Restore, Servpro, Belfor, FIRST OnSite)
- Referrals from plumbers and insurance agents
- Google searches when they can rank

**The problem:**
- TPA work gives the restorer 30–40% less than direct insurance billing
- No mechanism to build direct referral relationships with plumbers, insurance agents, property managers
- No system to convert emergency callers into review-generating, repeat-referral assets

**What's missing:** B2B referral partnership nurture (plumbers, agents, property managers) and a systematic Google review request after job completion.

### Pain Point 6: Referral Gaps — No Plumber Partnership System

A burst pipe = immediate water damage. Every plumber is a water damage referral machine. Yet 95% of restoration companies have no formal referral program, no tracking, and no follow-up with plumber partners.

**The problem:** The relationship is informal. A plumber might call once, the restorer shows up, and there's no systematic reinforcement to make that plumber call *every time*.

**What's missing:** A plumber referral partner onboarding workflow, referral tracking, and a monthly partner nurture sequence.

### Pain Point 7: No Homeowner Communication During the Drying Phase

Structural drying takes 3–10+ days. The homeowner's house is full of loud industrial equipment. They're displaced or displaced to another part of the home. They have no idea what's happening.

**The problem:**
- Homeowners call constantly asking "is it done?"
- No systematic daily update creates anxiety, complaints, and negative reviews
- Homeowners who feel ignored post negative Google reviews even when the work was excellent

**What's missing:** Daily automated update sequence during the drying phase that shares RH% progress and estimated completion.

### Pain Point 8: No Reconstruction Pipeline

Once drying is certified complete, the homeowner needs reconstruction (drywall, flooring, paint, cabinets). Most small restorers don't do reconstruction — they refer it out. That referral is worth $5,000–$30,000 and most companies track it nowhere.

**What's missing:** A reconstruction referral pipeline with partner tracking and a revenue-share notification system.

### Pain Point 9: Review Volume Gap

Google reviews are the #1 conversion factor for emergency restoration searches. Competitors with 200+ reviews win clicks over operators with 12 reviews. Yet asking for a review at the end of a stressful water damage event feels tone-deaf.

**The problem:** Timing is everything. Ask too early = feels inappropriate. Ask too late = homeowner has moved on. Most operators never ask systematically.

**What's missing:** A timed review request sequence at the point of peak satisfaction: when the homeowner gets their certificate of completion and their house is back to normal.

---

## 3. Competitive Snapshot Landscape {#competitive-landscape}

### What Exists in the Market

After evaluating available GHL marketplace snapshots for the restoration vertical, here's the honest assessment:

#### Generic "Home Services" Snapshots
- Pros: CRM pipeline, basic lead capture, appointment booking
- Cons: No emergency dispatch logic, no insurance claim workflow, no B2B referral partner system, no drying monitoring sequence
- Gap: Built for scheduled appointments, not emergency response

#### Basic "Restoration" Snapshots (Rare, Low Quality)
- Pros: Some restoration-specific language, basic pipeline
- Cons: Treat every job as a single-track appointment workflow, ignore the insurance claim process entirely, no plumber referral system, generic SMS templates
- Gap: Built by GHL generalists, not restoration industry operators

#### What the Best Available Snapshots Include
- 3–5 stage pipeline
- Generic appointment booking calendar
- Basic lead nurture (3–5 emails)
- Google review request (1 message)

#### What None of Them Include
- 24/7 emergency dispatch automation with escalation logic
- Insurance claim tracking pipeline (separate from mitigation pipeline)
- Daily drying monitoring update workflow
- Plumber referral partnership onboarding system
- Adjuster communication sequence
- Reconstruction referral pipeline with partner tracking
- Equipment placement reminders and drying completion triggers
- IICRC documentation package generation prompts
- Category/Class classification intake form

### The Market Gap

No snapshot on the market solves the core operational duality of water damage restoration:

> **Track 1:** Move fast (emergency dispatch in <5 minutes)  
> **Track 2:** Be patient and systematic (insurance claim nurture over 4–8 weeks)

The 1app snapshot will be the first to architect both tracks in parallel within a single GHL sub-account.

---

## 4. Pipeline Architecture {#pipeline-architecture}

### Recommended Pipeline Structure

Water damage restoration requires **four distinct pipelines** operating simultaneously within GHL:

---

### Pipeline 1: Emergency Response Pipeline
*Purpose: Capture inbound emergency calls/leads and convert to dispatched job*

| Stage | Name | Description | Avg Time in Stage |
|-------|------|-------------|-------------------|
| 1 | 🚨 Emergency Inbound | New call/web form/missed call captured | 0–5 min |
| 2 | 📞 Callback Attempted | Auto-SMS sent; human callback initiated | 5–15 min |
| 3 | ✅ Job Confirmed | Homeowner confirmed; tech dispatched | 15–30 min |
| 4 | 🚐 En Route | Tech on the way; ETA sent to homeowner | 30–90 min |
| 5 | 🏠 On-Site Assessment | Tech on-site; moisture mapping started | — |
| 6 | 📋 Scope Approved | Homeowner signed work authorization | — |
| 7 | ❌ Lost — Competitor | Did not convert | — |
| 8 | 🛑 Not Qualified | Out of service area / wrong job type | — |

**Key Automation Trigger:** Any missed call or web form submission instantly fires Stage 1 → Stage 2 workflow (SMS within 60 seconds).

---

### Pipeline 2: Mitigation & Drying Pipeline
*Purpose: Track active drying jobs from Day 1 through certificate of completion*

| Stage | Name | Description | Avg Time in Stage |
|-------|------|-------------|-------------------|
| 1 | 📦 Equipment Set | Equipment placed; daily monitoring begins | Day 1 |
| 2 | 📊 Day 2+ Monitoring | Daily GPP/RH% readings logged | Day 2–7+ |
| 3 | 🏁 Drying Target Met | RH% <50%, GPP at standard; cert ready | Day 5–14 |
| 4 | 📄 Certificate Issued | Certificate of completion delivered | — |
| 5 | 🛠️ Referring Reconstruction | Reconstruction referral sent to partner | — |
| 6 | ⭐ Review Requested | Google review request fired | — |
| 7 | ✅ Job Complete | File closed | — |

---

### Pipeline 3: Insurance Claim Pipeline
*Purpose: Track insurance claim status from FNOL through payment*

| Stage | Name | Description | Avg Time in Stage |
|-------|------|-------------|-------------------|
| 1 | 📋 Claim Filed | Homeowner filed claim; claim # captured | Day 1 |
| 2 | 🔍 Adjuster Assigned | Insurance adjuster name/contact captured | Day 1–3 |
| 3 | 📸 Documentation Sent | Photos, moisture maps, scope of work sent | Day 3–7 |
| 4 | 📝 Estimate Submitted | Xactimate estimate submitted to adjuster | Day 7–14 |
| 5 | 🔄 Estimate Under Review | Awaiting adjuster approval | Day 14–21 |
| 6 | ✅ Estimate Approved | Insurance approved scope and cost | — |
| 7 | 💰 Invoice Submitted | Final invoice sent to insurer | — |
| 8 | 💵 Payment Received | Claim closed | — |
| 9 | ⚠️ Dispute / Supplement | Adjuster pushed back; supplement filed | — |

---

### Pipeline 4: Referral Partner Pipeline
*Purpose: Manage plumber, insurance agent, and property manager referral relationships*

| Stage | Name | Description |
|-------|------|-------------|
| 1 | 👋 Partner Identified | New plumber/agent/PM contacted |
| 2 | 🤝 Partnership Pitched | Value proposition delivered |
| 3 | ✅ Partner Active | Sent first referral |
| 4 | 🔁 Partner Repeat | Sent 2+ referrals; ongoing relationship |
| 5 | ⭐ VIP Partner | Top referrer — white glove treatment |
| 6 | 😴 Partner Dormant | No referral in 60+ days |

---

## 5. Workflow Architecture {#workflow-architecture}

### Master Workflow List (14 Workflows)

| # | Workflow Name | Trigger | Purpose |
|---|---------------|---------|---------|
| 1 | 🚨 Emergency Dispatch — Missed Call | Missed call | Instant SMS response + internal alert |
| 2 | 🚨 Emergency Dispatch — Web Form | Form submission | Immediate callback sequence |
| 3 | 📞 Emergency Follow-Up — No Response | No callback response after 15 min | Escalation SMS + callback |
| 4 | 🏠 Job Confirmed — Tech Dispatch Notification | Pipeline stage move | ETA SMS to homeowner |
| 5 | 📦 Equipment Set — Drying Monitoring Start | Pipeline stage move | Day 1 homeowner intro + daily log prompt |
| 6 | 📊 Daily Drying Update | Daily trigger (per active job) | RH%/GPP update to homeowner |
| 7 | 🏁 Drying Complete — Certificate & Reconstruction | Pipeline stage move | Certificate delivery + reconstruction referral |
| 8 | ⭐ Review Request Sequence | Certificate issued + 24hr wait | Google review request (3-touch) |
| 9 | 📋 Insurance Claim Nurture | Claim filed trigger | Adjuster touchpoints + documentation nudges |
| 10 | 💰 Invoice Follow-Up | Invoice submitted trigger | Payment status follow-up sequence |
| 11 | 🔧 Plumber Partner Onboarding | New partner tag | Welcome + referral kit delivery |
| 12 | 🔁 Plumber Partner Monthly Nurture | Monthly recurring | Keep relationship warm |
| 13 | 🏘️ Property Manager Outreach | New PM contact | Referral partnership pitch |
| 14 | 😴 Win-Back — Lost / No Response | 30-day no activity | Re-engagement for cold leads |

---

### Workflow 1: Emergency Dispatch — Missed Call
**Trigger:** Missed call on main business line (connected to GHL phone)
**Goal:** Acknowledge immediately, create urgency, get callback within 5 minutes

```
Step 1: [Immediate — 0 minutes]
SMS to caller:
"Hi, this is [Company Name]. We just missed your call — we know water damage can't wait. We're calling you back RIGHT NOW. If you need immediate help, call us at [phone]. — [Owner Name]"

Step 2: [Immediate — 0 minutes]
Internal notification to on-call tech:
"🚨 MISSED CALL — potential water damage emergency. Call [contact name] at [phone] NOW. Lead in GHL: [link]"

Step 3: [If no response in 15 minutes]
SMS:
"Still here and ready to help. Water damage gets worse every hour — we want to get a crew to you ASAP. Call or reply with your address and we'll reach out immediately. — [Company Name]"

Step 4: [If no response in 30 minutes]
Email:
Subject: "We tried to reach you — water emergency help available 24/7"
[See full email template in Section 7]
```

---

### Workflow 2: Emergency Dispatch — Web Form
**Trigger:** Emergency contact form submitted
**Goal:** Immediate acknowledgment + human follow-up in <5 minutes

```
Step 1: [Immediate]
SMS:
"[First Name] — we got your message. Water damage emergency? Our team is standing by 24/7. We're calling you right now. — [Company Name]"

Step 2: [Immediate]
Internal alert:
"🚨 WEB FORM EMERGENCY LEAD — [First Name] [Last Name] — [Phone] — [Address if provided]. Call NOW."

Step 3: [2 minutes if no internal callback logged]
Escalation internal SMS to owner/manager:
"⚠️ Emergency lead NOT called back yet. [First Name] at [phone]. 2 minutes elapsed."
```

---

### Workflow 5: Equipment Set — Drying Monitoring Start
**Trigger:** Contact moved to "Equipment Set" stage in Mitigation Pipeline
**Goal:** Set homeowner expectations, establish daily communication rhythm

```
Step 1: [Immediate — Day 1 evening]
SMS:
"Hi [First Name], this is [Tech Name] from [Company]. Equipment is set and drying has started. Here's what to expect:

✅ Our LGR dehumidifiers and air movers are running 24/7
📊 We'll text you daily readings so you know progress
📅 Estimated drying time: 3–7 days depending on readings
🚫 Please don't move or unplug equipment — it's critical to your claim

Any questions? Reply here or call [phone]. We've got you."

Step 2: [Day 1 — separate homeowner care email]
[Full email with moisture map explanation, IICRC process overview, what to expect during drying, ALE information]
```

---

### Workflow 6: Daily Drying Update
**Trigger:** Daily at 6:00 PM for all contacts tagged "Active Drying"
**Goal:** Keep homeowner informed; reduce inbound calls; build trust

```
SMS Template (populated via custom fields):
"📊 [First Name] — Day {{drying_day}} Drying Update

📍 Address: {{property_address}}
💧 Moisture Readings: {{moisture_reading}}% RH (target: <50%)
💨 Air GPP: {{gpp_reading}} (decreasing = drying working ✅)
🔧 Equipment Running: {{equipment_count}} units

Status: {{drying_status}}

We'll update you again tomorrow. Questions? Reply anytime. — [Company Name]"
```

**Custom Fields Required:**
- `drying_day` (counter, increments daily)
- `moisture_reading` (RH% — tech logs via intake form or SMS reply)
- `gpp_reading`
- `equipment_count`
- `drying_status` (On Track / Needs Additional Time / Complete)

---

### Workflow 9: Insurance Claim Nurture
**Trigger:** Contact tagged "Insurance Claim"
**Goal:** Keep homeowner informed on claim status; prompt action steps; accelerate adjuster approval

```
Day 1 (Claim filed):
SMS: "Hi [First Name] — important next step: your claim number is your lifeline. Make sure you have it saved. Ours is on file as {{claim_number}}. If your adjuster calls, you can provide our company name and contact: [info]."

Day 3:
SMS: "Quick update — we've submitted your scope of work and moisture documentation to your adjuster. If they reach out to you directly, let us know immediately. We're tracking this daily."

Day 7 (if no adjuster approval):
SMS: "Still working on your claim. Adjuster reviews can take 7–14 days. We're following up on our end. Nothing you need to do today — we've got it covered."

Day 14 (if estimate still pending):
Email + SMS: "We've submitted a complete Xactimate estimate and documentation package. Adjuster: {{adjuster_name}}. We're following up today. If you hear from your insurance company, please forward any emails to us at [email] so we can respond quickly."

Day 21 (if still pending — escalation):
Email to homeowner:
"Your adjuster approval is taking longer than normal. Here's what we recommend..."
[Full escalation guidance — public adjuster referral, insurance commissioner complaint process if warranted]
```

---

## 6. Lead Sources & Acquisition Strategy {#lead-sources}

### Primary Lead Sources for Water Damage Restoration

#### A. Google Emergency Searches (Highest Intent)
- **Keywords:** "water damage restoration near me," "burst pipe cleanup," "basement flooding help," "emergency water removal," "sewage backup cleanup"
- **Search behavior:** Homeowner types on phone within minutes of the event
- **Conversion key:** Google Business Profile with 50+ reviews, 24/7 hours, and click-to-call
- **GHL action:** Track UTM source on all web forms; build Google Ads landing page that fires directly into Emergency Dispatch Workflow 1

#### B. Insurance Adjusters (Highest Volume for Established Operators)
- **Relationship:** Property insurance adjusters at Intact, Aviva, TD, Wawanesa, Economical, Gore Mutual (Canada) or State Farm, Allstate, Farmers (US)
- **TPA networks:** Contractor Connection, Xactware Network, Code Blue
- **GHL action:** Separate adjuster contact type in CRM; adjuster referral nurture (monthly newsletter on drying best practices, Xactimate documentation tips)

#### C. Plumbers (Burst Pipe — Immediate Referral)
- **Why:** Every burst pipe call a plumber takes is a potential water damage referral
- **Relationship:** Plumber turns water off; homeowner then needs extraction and drying
- **GHL action:** Plumber Partner Pipeline + Workflow 11 (partner onboarding)

#### D. Property Managers & Strata Managers
- **Why:** Multi-unit buildings have frequent water events; PM controls contractor selection
- **Volume:** One PM relationship = 10–50+ jobs per year
- **GHL action:** PM sub-pipeline within Referral Partner Pipeline; dedicated PM outreach sequence

#### E. Insurance Agents & Brokers
- **Why:** When homeowner calls agent after water event, agent recommends restorer
- **Relationship:** More advisory than adjuster, but high trust with homeowner
- **GHL action:** Agent referral nurture — provide educational resources, claim process guides

#### F. Restoration Networks (National Programs)
- **Examples:** Servpro (franchise), FIRST OnSite, BMS CAT, Belfor
- **Dynamic:** TPA work pays less but provides volume
- **GHL action:** Track TPA vs. direct jobs separately; use pipeline data to show direct billing ROI

#### G. Restoration Industry Associations
- **IICRC certified companies** get referrals from the IICRC directory
- **RIA (Restoration Industry Association)** — networking with adjusters and peers
- **GHL action:** Track where "IICRC search" leads come from

---

## 7. SMS & Email Templates {#sms-email-templates}

### Emergency SMS Templates

#### Template 1A: Missed Call — Immediate Response
```
[First Name] — you called [Company Name] and we just missed you. 

Water emergency? We're calling you RIGHT NOW. 

If it's urgent, don't wait — call [phone]. We're 24/7.

— [Company Name]
```

#### Template 1B: Web Form — Immediate Acknowledgment
```
Hi [First Name] — got your message. We're on it. Expect a call from us in the next 2 minutes.

Water damage doesn't wait — neither do we. 🚒

— [Company Name] Emergency Response
```

#### Template 1C: No Callback Response — 15 Min Escalation
```
[First Name] — still trying to reach you. 

Water damage worsens fast — every hour counts. Secondary damage (mold can start in 24hrs) adds cost and extends your claim.

Reply with your address and the best time to call. We'll dispatch immediately.

— [Company Name]
```

#### Template 1D: Confirmed Job — Tech En Route
```
✅ Great news, [First Name]!

[Tech Name] is heading to you now. ETA: approximately [X] minutes.

He'll arrive in a [Company] vehicle. He'll assess the water damage, walk you through the process, and get extraction started immediately.

Any questions before he arrives? Call or reply here.

— [Company Name]
```

---

### Drying Phase SMS Templates

#### Template 2A: Equipment Set — Day 1 Introduction
```
Hi [First Name] — [Tech Name] here from [Company].

Equipment is running at your property. Here's your Day 1 status:

💧 Moisture Level: {{moisture_reading}}% RH
🔧 Equipment: {{equipment_count}} units active
📅 Estimated dry time: {{estimated_days}} days

We'll text you daily progress reports so you always know where things stand. No need to call us — we'll come to you.

Questions? Reply anytime. — [Company Name]
```

#### Template 2B: Daily Monitoring Update (Days 2–7+)
```
📊 [First Name] — Day {{drying_day}} Update | [Company Name]

Property: {{property_address}}

Today's Readings:
• Structural RH: {{moisture_reading}}%  (target <50%)
• Air GPP: {{gpp_reading}} grains/lb
• Equipment running: {{equipment_count}} units

Status: {{drying_status}} {{status_emoji}}

{{custom_message}}

We'll check in again tomorrow. — [Company Name] | 24/7: [phone]
```

#### Template 2C: Drying Complete — Certificate Ready
```
🎉 Great news, [First Name]!

Your property has reached drying standard per IICRC S500 guidelines.

✅ Final moisture readings: {{final_reading}}% RH
✅ Certificate of Completion: Being prepared now
✅ All equipment will be removed within 24 hours

We'll send your certificate today. Once you receive it, your insurance company will need a copy for the claims file.

Next step: reconstruction of affected materials. We work with trusted contractors — want us to connect you? Just reply YES.

Thank you for trusting [Company Name]. — [Owner Name]
```

---

### Insurance Claim SMS Templates

#### Template 3A: Claim Number Capture
```
Hi [First Name] — quick question: do you have your insurance claim number handy?

Once we have it, we can coordinate directly with your adjuster and keep your claim moving. Reply with the number whenever you have it.

— [Company Name]
```

#### Template 3B: Documentation Package Sent
```
[First Name] — update on your claim:

📁 We've sent your adjuster ({{adjuster_name}}) a complete documentation package including:
• Moisture mapping photos
• Daily drying logs
• IICRC-compliant scope of work
• Xactimate estimate

Typical review time: 5–10 business days. We're following up on our end.

Questions? Reply or call [phone]. — [Company Name]
```

#### Template 3C: Adjuster Approval Confirmation
```
✅ Good news, [First Name]!

Your insurance company has approved the scope of work for your water damage claim.

Approved amount: {{approved_amount}}
Adjuster: {{adjuster_name}}

We'll submit our final invoice directly. If you have any questions about your deductible or ALE (additional living expenses), call your agent — that's handled separately.

You're almost done with the hard part. — [Company Name]
```

---

### Plumber Referral Partner Templates

#### Template 4A: Initial Plumber Outreach
```
Hey [Plumber Name] — [Your Name] from [Company Name]. 

Quick question: when you respond to a burst pipe, what do you do about the water damage?

We partner with plumbers in [City] to handle the extraction and drying — you focus on the pipe, we handle the water. No overlap, no competition.

If it's a good fit, I'd love to buy you a coffee. 5 minutes of your time. Interested?

— [Your Name] | [Company Name]
```

#### Template 4B: Partner Welcome (After Commitment)
```
Welcome aboard, [Plumber Name]! 

Here's how the referral works:
📞 When you hit a water damage job — call or text [Company Name] at [phone]
📍 We'll dispatch within [X] minutes
💼 You stay on your plumbing work; we handle everything else
🤝 Every referral gets tracked — we'll follow up with you on outcomes

Referral card attached. Keep it in your work truck.

Looking forward to working together. — [Owner Name] | [Company Name]
```

---

### Review Request Templates

#### Template 5A: Review Request — 24 Hours After Certificate
```
Hi [First Name] — hope you're settling back in after everything.

We know water damage is stressful. Our team worked hard to get your home back to normal as fast as possible — and we're glad it's done.

One quick favor: would you mind leaving us a Google review? It takes 60 seconds and helps other families in [City] find us when they need help.

[Google Review Link]

Thank you — genuinely means a lot to our team. — [Owner Name]
```

#### Template 5B: Review Follow-Up — Day 3 (if no review)
```
Hi [First Name] — just a quick follow-up. 

If you had a good experience with [Company Name], a Google review goes a long way. It helps us keep our local team busy and helps families find us in emergencies.

[Google Review Link]

No pressure — but it's appreciated. — [Company Name]
```

---

## 8. Booking & Dispatch Flow {#booking-dispatch-flow}

### Emergency Dispatch Philosophy

Water damage restoration does NOT work like a scheduled appointment service. The booking flow must be **zero-friction, maximum urgency**:

> Standard booking flow: "Choose a date and time" ← WRONG  
> Emergency dispatch flow: "We're coming NOW" ← RIGHT

### Emergency Dispatch Flow Architecture

```
INBOUND CHANNEL → IMMEDIATE ACKNOWLEDGMENT → HUMAN CALLBACK → JOB CONFIRMED → DISPATCH

Step 1: Lead Arrives
  - Source: Phone call / Missed call / Web form / Facebook Lead Ad / GMB call
  - GHL: Contact created, tagged "Emergency Inbound," added to Emergency Response Pipeline

Step 2: Instant Automation (0–60 seconds)
  - SMS sent to caller: Emergency acknowledgment (Template 1A or 1B)
  - Internal alert fired to on-call tech via SMS
  - Task created in GHL: "Call [contact] NOW — water emergency"

Step 3: Human Callback (Target: <5 minutes)
  - On-call dispatcher or tech calls back
  - Collects: Address, water source, contamination type (cat 1/2/3?), standing water present?
  - Confirms: We're coming. ETA [X] minutes.
  - Logs: Call notes in GHL contact record

Step 4: Job Confirmed (Pipeline Stage: "Job Confirmed")
  - Contact moved to "Job Confirmed" in Emergency Pipeline
  - Automated SMS: Tech on the way (Template 1D)
  - Internal dispatch: Tech gets full address + briefing via SMS

Step 5: On-Site
  - Tech signs in on GHL mobile app
  - Creates site assessment notes
  - Moves to "On-Site Assessment" stage
```

### Web Form Design for Emergency Landing Page

**Form Fields (Keep Short — They're in Crisis)**
1. First Name (required)
2. Phone (required)
3. Street Address (required)
4. What happened? (dropdown: Burst Pipe / Basement Flooding / Sewage Backup / Appliance Leak / Storm/Roof / Other)
5. Is there standing water? (Yes / No)
6. Submit button: **"GET HELP NOW →"**

**Do NOT Include:**
- Last name (get it on the call)
- Email (optional, get it later)
- Date/time picker (this is NOT a scheduled appointment)
- Long message field

### Scheduled Appointment Flow (Non-Emergency)

For assessments, estimates, or pre-scheduled jobs (e.g., post-construction moisture checks):

Use GHL Calendar with:
- Calendar name: "Assessment Booking"
- Duration: 45 minutes
- Buffer: 15 minutes
- Confirmation: Automated SMS + email (24h + 1h reminder)
- Post-appointment: Trigger appropriate workflow based on assessment outcome

---

## 9. Insurance Claim Workflow {#insurance-claim-workflow}

### The Insurance Claim Reality

Approximately 65–80% of water damage jobs involve an insurance claim. The workflow must account for:

1. **First Notice of Loss (FNOL):** Homeowner files claim with their insurer
2. **Adjuster Assignment:** Insurer assigns a claims adjuster (can take 24–72 hours)
3. **Site Inspection:** Adjuster may want to inspect before approving scope
4. **Estimate Review:** Restorer submits Xactimate estimate; adjuster reviews
5. **Supplement Cycle:** Adjuster may approve partial scope; restorer supplements
6. **Approval:** Full scope approved
7. **Payment:** Insurer issues payment (often to homeowner + mortgagee jointly)

### Insurance Claim Pipeline Workflow (GHL)

**Workflow 9 — Full Insurance Claim Nurture Sequence:**

```
TRIGGER: Contact tagged "Insurance Claim" OR custom field "Claim Filed" = Yes

Day 0 (Job confirmed):
→ SMS: Capture claim number (Template 3A)
→ Create task: "Get claim # from [Contact]"

Day 1:
→ Email: Full insurance process guide (sets expectations, builds trust)
→ Subject: "Your water damage claim — here's exactly what happens next"
→ Content: [Full timeline, adjuster process, what homeowner needs to do, what we handle]

Day 3:
→ SMS: Documentation package sent confirmation (Template 3B)
→ Internal task: "Upload photos + moisture maps to adjuster file"

Day 7 (if no adjuster approval yet):
→ SMS: Status update — working on it
→ Internal task: "Follow up with {{adjuster_name}} — claim {{claim_number}}"

Day 10:
→ Email: Secondary update with process education
→ SMS: "Quick update — we're in active communication with your adjuster..."

Day 14 (estimate still pending):
→ Email + SMS: Escalation guidance for homeowner
→ Internal alert: "⚠️ Claim {{claim_number}} — 14 days without approval. Manager review needed."

Day 21 (if still disputed):
→ Email: Public adjuster referral option
→ Internal: Escalate to owner

Day 28+:
→ Monthly check-in SMS until resolved
```

### Insurance Claim Custom Fields Required

| Field Name | Type | Notes |
|------------|------|-------|
| `claim_number` | Text | Homeowner's insurance claim number |
| `insurance_company` | Dropdown | Intact, Aviva, TD, Wawanesa, etc. |
| `adjuster_name` | Text | Claims adjuster full name |
| `adjuster_phone` | Phone | Direct line to adjuster |
| `adjuster_email` | Email | For documentation packages |
| `policy_number` | Text | Homeowner's policy number |
| `claim_status` | Dropdown | Pending / Under Review / Approved / Disputed / Closed |
| `estimate_amount` | Currency | Xactimate estimate total |
| `approved_amount` | Currency | Insurance-approved amount |
| `deductible_amount` | Currency | Homeowner deductible |
| `invoice_submitted_date` | Date | |
| `payment_received_date` | Date | |
| `supplement_required` | Yes/No | Was a supplement filed? |

---

## 10. Plumber Referral Partnership System {#plumber-referral-system}

### Why Plumbers Are the #1 Referral Source

- **Burst pipes = guaranteed water damage.** When a plumber arrives to fix the pipe, water has already spread. Extraction and structural drying are required.
- **Plumber authority:** When the plumber says "call these guys for the water damage," the homeowner calls.
- **No competition:** Plumbers don't do water damage restoration. It's a pure referral.
- **Volume:** A busy residential plumber does 3–8 emergency calls/day. Even 1 water damage referral per week = 50+ leads/year.

### Plumber Referral Pipeline (GHL)

**Stage 1: Prospect Identified**
- Plumbers pulled from Google Maps, Yelp, local trades directories
- Tagged: "Plumber Partner — Prospect"

**Stage 2: Initial Outreach**
- SMS or email sent (Template 4A)
- Task created: "Follow up in 3 days if no response"

**Stage 3: Meeting / Call Completed**
- Notes logged: who they are, volume, area
- Decision: Move to Active or Not a Fit

**Stage 4: Partner Onboarded**
- Partner agreement confirmed (can be informal verbal)
- Welcome sequence triggered (Workflow 11)
- Tagged: "Active Plumber Partner"
- Physical referral cards / co-branded materials sent

**Stage 5: Active Partner**
- Referral received and logged
- Thank-you SMS to plumber after each referral
- Monthly check-in sequence (Workflow 12)

**Stage 6: VIP Partner (3+ referrals)**
- White glove treatment
- Quarterly lunch / gift card
- Priority dispatch on any job they refer

### Workflow 11: Plumber Partner Onboarding

```
TRIGGER: Contact tagged "Active Plumber Partner"

Day 0:
→ SMS (Template 4B): Welcome + referral instructions
→ Email: Full partner welcome package
  - How to refer
  - What happens after you call
  - What the homeowner can expect
  - Your contact info

Day 3:
→ SMS: "Any questions about how the referral works? Happy to do a quick 5-minute walkthrough."

Day 14:
→ Task: "Drop off referral cards to {{plumber_name}} at {{plumber_address}}"

Day 30:
→ SMS: "Hey [First Name] — checking in. Had any burst pipe calls lately? Our team is standing by. — [Your Name]"
```

### Workflow 12: Monthly Partner Nurture

```
TRIGGER: Monthly, all contacts tagged "Active Plumber Partner"

Monthly SMS rotation (alternate each month):
Month 1: "Hey [First Name] — [Company] here. Water damage season is picking up. Give us a call whenever you hit a flood — we dispatch in [X] minutes. — [Your Name]"
Month 2: "Quick tip for your homeowners: after a burst pipe, running a dehumidifier for 1–2 days is NOT enough. Structural drying takes 5–10 days. We do it right. Call us anytime — [Your Name]"
Month 3: "Referral update — we've taken care of {{referral_count}} homeowners you've sent our way. Appreciate it. Anything we can do for you? — [Your Name]"
```

### Tracking Plumber Referral ROI

**Custom Fields for Plumber Partner:**
| Field | Type | Notes |
|-------|------|-------|
| `referral_count` | Number | Total referrals sent |
| `referral_value_total` | Currency | Total revenue from their referrals |
| `last_referral_date` | Date | Trigger "dormant" tag if >60 days |
| `partner_tier` | Dropdown | Standard / VIP |

---

## 11. Reconstruction Referral Workflow {#reconstruction-referral-workflow}

### The Reconstruction Revenue Opportunity

After structural drying is certified complete:
- Affected drywall must be replaced
- Flooring (hardwood, laminate, carpet) must be replaced
- Cabinets, trim, and paint affected by moisture damage must be restored
- Average reconstruction job: **$5,000–$30,000**

Most small restoration companies do NOT do reconstruction — they stop at drying. This referral is nearly always unmeasured and untracked.

### Reconstruction Partner System

**GHL Setup:**
- Create contact type: "Reconstruction Contractor"
- Separate sub-pipeline: "Reconstruction Referral Pipeline"

| Stage | Name |
|-------|------|
| 1 | 🏗️ Referral Sent |
| 2 | 📞 Contractor Contacted Homeowner |
| 3 | 📋 Estimate Provided |
| 4 | ✅ Job Won |
| 5 | 💵 Referral Fee Received |
| 6 | ❌ Job Lost |

### Workflow 7: Drying Complete — Reconstruction Referral

```
TRIGGER: Contact moved to "Certificate Issued" in Mitigation Pipeline

Step 1 [Immediate]:
SMS to homeowner (Template 2C — with reconstruction offer)

Step 2 [Same day]:
If homeowner replies YES to reconstruction referral:
→ SMS: "We'll connect you with [Contractor Name] today. They specialize in exactly this type of restoration and work directly with insurance. Expect a call from [number] within 2 hours."
→ Internal task: "Notify reconstruction partner of referral — [Contact name, address, scope notes]"
→ Move contact to Reconstruction Referral Pipeline Stage 1

Step 3 [3 days after referral sent]:
SMS to homeowner: "Did [Contractor] connect with you? Wanted to make sure you're taken care of."

Step 4 [After job confirmed]:
Tag: "Reconstruction Referral Won"
Custom field: `reconstruction_referral_value` = estimate amount
```

---

## 12. Daily Monitoring Update Workflow {#daily-monitoring-workflow}

### The Daily Update Problem

During the drying phase (Days 1–14+), homeowners are:
- Living in disrupted space with industrial equipment running 24/7
- Anxious about mold, property damage, and insurance
- Calling the office constantly asking "is it done yet?"

**Solution:** Proactive daily communication that delivers real data, reduces anxiety, and builds trust.

### How the Daily Update System Works

**Setup:**
1. When job enters "Equipment Set" stage, tag contact: "Active Drying"
2. Daily workflow fires at 6:00 PM for all "Active Drying" contacts
3. Tech logs daily readings via GHL form (accessible via SMS link)
4. Readings populate custom fields
5. Automated SMS sent to homeowner with real data

### Tech Daily Logging Form (GHL Survey/Form)

**Fields:**
- Contact lookup (auto-populated from GHL)
- Property address (confirmation)
- Day # of drying
- Moisture reading (RH%) — primary structure
- Moisture reading (RH%) — secondary structure (if applicable)
- GPP reading (air grains/pound)
- Equipment running (count)
- Status (On Track / Monitoring / Needs Extended Drying / Ready for Cert)
- Tech notes for homeowner (optional, 140 char max)

**Tech Access:**
- SMS link sent to tech at 4:00 PM daily: "Log your drying readings for [property address]: [form link]"
- Form submission triggers homeowner SMS at 6:00 PM

### Drying Day Counter Automation

```
TRIGGER: Contact moves to "Equipment Set" stage

→ Set custom field: drying_day = 1
→ Set custom field: drying_start_date = today

Daily (6 AM): Increment drying_day + 1 for all "Active Drying" contacts

When contact moves out of "Active Drying" tag:
→ Stop daily workflow
→ Log final drying_day as custom field: total_drying_days
```

---

## 13. Review Generation System {#review-generation}

### Timing Strategy for Restoration Reviews

The peak review window is **24–72 hours after certificate of completion**, when:
- Equipment is removed
- Home is returning to normal
- Homeowner relief is highest
- Insurance claim is still top of mind (review request feels natural)

Asking for a review during the drying phase = wrong timing (still stressed)  
Asking at equipment removal = best timing  
Waiting more than 7 days = homeowner has moved on

### Review Request Workflow (3-Touch Sequence)

**Trigger:** Contact moved to "Certificate Issued" AND tagged "Review Requested"

```
Touch 1 — 24 hours after certificate:
SMS (Template 5A) — warm personal tone, link to Google

Touch 2 — Day 3 (if no review posted):
SMS (Template 5B) — shorter, less pressure

Touch 3 — Day 7 (if no review posted):
SMS: "Last reach out, [First Name] — if you got good service from us, 60 seconds on Google makes a real difference. [Link]. No worries if not."

After Touch 3: Remove from review sequence. Do not over-message.
```

### Review Monitoring
- GHL trigger: "Review received" event (if connected to Google Business Profile)
- When review posted: Thank-you SMS to contact
- Update contact custom field: `review_posted = Yes` + `review_rating = [1-5]`

---

## 14. Snapshot Differentiators {#snapshot-differentiators}

### What Makes the 1app Water Damage Snapshot Stand Out

**1. Dual-Track Architecture**
No other snapshot separates the emergency response track from the insurance claim track. We handle both simultaneously, with separate pipelines, separate automations, and separate communication sequences.

**2. Daily Drying Monitoring System**
The only snapshot with a built-in tech logging workflow that feeds real moisture data into automated homeowner SMS updates. Homeowners get daily GPP/RH% updates — they feel informed and stop calling.

**3. Insurance Claim Nurture (Adjuster-Language)**
The insurance claim sequence uses actual adjuster terminology: Xactimate, scope of work, documentation package. It's written for operators who do direct insurance billing, not just homeowner retail.

**4. Plumber Referral Partner System**
A complete B2B referral system with onboarding, nurture, tracking, and VIP recognition — built into the snapshot from day one.

**5. Reconstruction Referral Pipeline**
Captures the most commonly missed revenue opportunity in the industry: reconstruction referrals after drying completion.

**6. Industry-Credible Language Throughout**
Every template, every form, every custom field uses IICRC-standard terminology. Adjusters who see the documentation know this company is professional.

**7. 24/7 Emergency Dispatch with Escalation Logic**
Missed call → instant SMS → internal alert → escalation if no callback in 15 minutes. The workflow doesn't let emergencies fall through.

**8. Complete Custom Field Library (35 Fields)**
From moisture readings to claim numbers to plumber referral tracking — every data point the business needs is captured in GHL.

---

## 15. Technical Build Specs {#technical-build-specs}

### Custom Fields Library (35 Fields)

**Job Classification:**
| Field | Type | Values |
|-------|------|--------|
| `water_damage_category` | Dropdown | Cat 1 / Cat 2 / Cat 3 |
| `water_damage_class` | Dropdown | Class 1 / Class 2 / Class 3 / Class 4 |
| `water_source` | Dropdown | Burst Pipe / Basement Flood / Sewage Backup / Appliance / Storm / Roof / Other |
| `standing_water_present` | Yes/No | |
| `estimated_affected_sqft` | Number | |
| `mold_present` | Yes/No | Triggers separate mold remediation workflow |
| `contents_restoration_required` | Yes/No | |
| `pack_out_required` | Yes/No | |
| `structure_unsafe_for_occupancy` | Yes/No | Triggers ALE conversation |

**Job Status:**
| Field | Type |
|-------|------|
| `job_status` | Dropdown: Emergency / Active Drying / Drying Complete / Reconstruction / Closed |
| `tech_assigned` | Text |
| `dispatch_time` | Date/Time |
| `arrival_time` | Date/Time |
| `work_authorization_signed` | Yes/No |

**Drying Monitoring:**
| Field | Type |
|-------|------|
| `drying_start_date` | Date |
| `drying_day` | Number |
| `moisture_reading` | Number (%) |
| `gpp_reading` | Number |
| `equipment_count` | Number |
| `drying_status` | Dropdown: On Track / Extended / Complete |
| `total_drying_days` | Number |
| `certificate_issued_date` | Date |

**Insurance Claim:**
| Field | Type |
|-------|------|
| `insurance_claim` | Yes/No |
| `insurance_company` | Dropdown (major carriers) |
| `claim_number` | Text |
| `policy_number` | Text |
| `adjuster_name` | Text |
| `adjuster_phone` | Phone |
| `adjuster_email` | Email |
| `claim_status` | Dropdown |
| `estimate_amount` | Currency |
| `approved_amount` | Currency |
| `deductible_amount` | Currency |
| `invoice_submitted_date` | Date |
| `payment_received_date` | Date |

**Referral Tracking:**
| Field | Type |
|-------|------|
| `referral_source` | Dropdown: Google / Plumber / Insurance Agent / Property Manager / Word of Mouth / TPA / Other |
| `referring_partner_name` | Text |
| `reconstruction_referral_sent` | Yes/No |
| `reconstruction_referral_value` | Currency |
| `review_posted` | Yes/No |
| `review_rating` | Number (1–5) |

---

### Tags Required

**Lead/Job Status Tags:**
- `Emergency Inbound`
- `Job Confirmed`
- `Active Drying`
- `Insurance Claim`
- `Certificate Issued`
- `Review Requested`
- `Review Posted`
- `Closed - Won`
- `Closed - Lost`

**Lead Source Tags:**
- `Source: Google Emergency`
- `Source: Plumber Referral`
- `Source: Insurance Agent`
- `Source: Property Manager`
- `Source: TPA`
- `Source: Word of Mouth`

**Partner Tags:**
- `Plumber Partner - Prospect`
- `Plumber Partner - Active`
- `Plumber Partner - VIP`
- `Plumber Partner - Dormant`
- `Insurance Agent Partner`
- `Property Manager Partner`
- `Reconstruction Partner`

**Compliance/Admin Tags:**
- `Mold Present`
- `Category 3 - Sewage`
- `Uninhabitable - ALE Active`
- `Supplement Filed`
- `Public Adjuster Involved`

---

### Calendars Required

| Calendar Name | Type | Use Case |
|---------------|------|---------|
| Assessment Booking | Round-robin or single | Non-emergency assessments |
| Post-Drying Inspection | Single tech | Final moisture verification appointments |
| Partner Meeting | Single owner | Plumber/agent partnership meetings |

**No emergency calendar.** Emergency dispatch is workflow-driven, not calendar-driven.

---

### Forms Required

| Form Name | Embed Location | Purpose |
|-----------|---------------|---------|
| Emergency Web Form | Landing page / website | Primary emergency lead capture |
| Tech Daily Log Form | Internal (SMS link to tech) | Daily drying readings input |
| Post-Assessment Intake | Sent after on-site visit | Capture full job details |
| Insurance Information Capture | Sent after job confirmed | Claim # / adjuster info |
| Partner Referral Form | Shared with plumber partners | Simple referral submission |
| Review Request Landing | Review email/SMS link | Soft landing before Google |

---

### Opportunity Values (Pipeline Tracking)

Set default opportunity values in GHL to track pipeline revenue:

| Job Type | Expected Value |
|----------|---------------|
| Minor water extraction (Cat 1, Class 1) | $1,500 |
| Standard mitigation (Cat 1-2, Class 2-3) | $5,000 |
| Full structural drying (Cat 1-2, Class 3-4) | $12,000 |
| Sewage backup (Cat 3) | $8,000 |
| Basement flooding | $10,000 |
| Reconstruction referral | $12,000 |

---

### Automation Calendar (Master Schedule)

| Time | Automation | Audience |
|------|-----------|---------|
| On trigger | Emergency Dispatch SMS | All emergency inbounds |
| 4:00 PM daily | Tech logging reminder | All active techs |
| 6:00 PM daily | Daily drying update SMS | All "Active Drying" contacts |
| 9:00 AM | Insurance claim follow-up tasks | Claims team |
| Day 1 of month | Partner nurture SMS batch | All active partners |
| 24h after cert | Review request Touch 1 | Completed jobs |
| 72h after cert | Review request Touch 2 | No review yet |
| 7d after cert | Review request Touch 3 | No review yet |
| 60 days no activity | Partner dormant tag | Plumber/agent partners |

---

### Snapshot Delivery Structure

**What to include in the snapshot:**

```
✅ Pipelines (4):
   - Emergency Response Pipeline
   - Mitigation & Drying Pipeline
   - Insurance Claim Pipeline
   - Referral Partner Pipeline

✅ Workflows (14):
   - All workflows listed in Section 5

✅ Custom Fields (35):
   - All fields listed in Section 15

✅ Tags (30+):
   - All tags listed in Section 15

✅ Forms (6):
   - All forms listed in Section 15

✅ Calendars (3):
   - Assessment Booking
   - Post-Drying Inspection
   - Partner Meeting

✅ Email Templates (8):
   - Insurance process guide (full)
   - Partner welcome package
   - Drying process explainer
   - Certificate + reconstruction offer
   - Monthly partner newsletter
   - Invoice follow-up
   - Review request email
   - Claim escalation guide

✅ SMS Templates (20+):
   - All templates in Section 7

✅ Landing Pages / Funnels (3):
   - Emergency response landing page
   - Plumber partner referral page
   - Review collection landing page

✅ Reporting Dashboards (2):
   - Job pipeline value dashboard
   - Referral partner performance dashboard

✅ Opportunities (default values set by job type)

✅ Custom Values (operator-fills on setup):
   - Company name
   - Owner name
   - On-call phone number
   - Google review link
   - Service area
   - Insurance company list (regional)
```

---

## Appendix A: Competitive Intelligence Notes

### Why ServiceMaster / Servpro Can't Be Easily Copied in GHL
- National franchise systems run proprietary tech stacks (DASH, Encircle)
- Their advantage is national brand, not local agility
- Independent operators can out-communicate them locally with proper automation
- The 1app snapshot gives independents the system nationals built over 20 years

### Why Generic Home Service Snapshots Fail in This Vertical
1. Appointment booking logic doesn't fit emergency dispatch
2. No insurance claim track — ignores 70% of the business model
3. No drying phase communication — the longest relationship phase
4. No B2B partner system — ignores the referral engine
5. Templates use retail language — adjusters and industry professionals need technical credibility

### What Operators Will Say When They See This
- "This is the first system that actually understands how our business works"
- "The daily drying updates alone are worth the subscription — we get 10 fewer calls a day from homeowners"
- "The plumber referral system is something I've been meaning to build for 3 years"

---

## Appendix B: Objection Handling (For 1app Sales)

**"We already have a CRM"**
"What does it do when you get a water damage call at midnight? Because ours texts the homeowner within 60 seconds, alerts your on-call tech, and creates a follow-up task — all before you wake up."

**"We're too busy to learn new software"**
"That's exactly why this exists. The system runs 24/7 without you. The busier you are, the more you need it."

**"We do most of our jobs through insurance TPAs"**
"TPA jobs pay 30–40% less than direct billing. This system helps you build your own referral pipeline — plumbers, agents, property managers — so you control your own leads."

**"We don't do a lot of marketing"**
"You don't have to. Your Google reviews become your marketing. This system gets you reviews automatically after every job. 50 five-star reviews means you stop paying for TPA volume."

---

## Document Metadata

| Field | Value |
|-------|-------|
| Research Depth | Deep — industry domain knowledge + operational best practices |
| Target Snapshot Tier | Full (not basic) |
| Recommended Pricing | $297–$497/month SaaS or $997 one-time + onboarding |
| Build Complexity | High (4 pipelines, 14 workflows, 35 custom fields, 6 forms) |
| Estimated Build Time | 40–60 hours (first build) |
| Duplicability | High — works for any regional water damage operator |
| Compliance Notes | No health/biohazard claims in templates; IICRC standards referenced but not guaranteed |
| Last Updated | 2026-07-21 |

---

*Document prepared by Maximus for 1app Technologies Inc. Internal use only.*
