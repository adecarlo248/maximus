# 1app GHL Solar Snapshot — Comprehensive Research & Build Document

**Prepared for:** 1app Technologies Inc. (GHL SaaS Agency)
**Date:** July 2026
**Classification:** Internal Agency Build Reference
**Vertical:** Residential Solar, Commercial Solar, Battery Storage, EV Charger Combos, Government Rebate Programs

---

## Executive Summary

The solar industry is one of the highest-intent, highest-ticket verticals in the home services space — average residential systems run $27,000–$44,000 before incentives, and commercial deals can reach $500K+. It is also one of the most automation-unfriendly verticals because of its unique sales dynamics: **solar leads go cold in minutes**, not hours; buyers take 30–90 days to decide; rebate programs create urgency windows; and the financing complexity rivals a mortgage.

Most solar CRM snapshots on the market today are generic home services templates rebadged with solar language. They miss the critical nuances:
- Speed-to-lead automation tuned to the 5-minute contact window
- Multi-pipeline architecture separating residential quote, commercial deal, battery add-on, and EV charger combo
- Rebate education sequences aligned to Canada Greener Homes, provincial programs, and net metering
- Long-cycle nurture (30–90 day cadence with educational content, not just "Are you still interested?")
- Post-install referral capture (solar customers are evangelist-level advocates)

This document defines every component of a world-class 1app Solar Snapshot that will stand apart in the GHL marketplace.

---

## Part 1: Industry Deep-Dive — The Solar Sales Problem

### 1.1 Why Solar Is Hard to Sell

Solar is not a commodity purchase. The average homeowner spends 30–90 days from first inquiry to signed contract. Here is why:

**Decision complexity:**
- Evaluating panel types (monocrystalline vs. polycrystalline), inverter types (string inverter vs. microinverter vs. power optimizer), roof mount vs. ground mount configurations, and battery storage (Tesla Powerwall, Enphase IQ, SolarEdge)
- Understanding net metering, feed-in tariff rates, and how kWh production maps to utility bill savings
- Navigating financing options: cash purchase, solar loan, lease, power purchase agreement (PPA)
- Calculating ROI: average payback period is 8–12 years; 25-year lifetime savings range $41,000–$155,000 in the U.S.

**Trust barriers:**
- High-pressure door-to-door sales has permanently scarred the industry's reputation
- Predatory solar loan terms (dealer fees, interest rate bait-and-switch) have created skeptical buyers
- Rebate complexity — homeowners don't understand what programs they actually qualify for
- Permit and inspection timelines (typically 3–6 months from contract to energized system) create doubt

**Competition saturation:**
- Every major metro has 20+ solar installers competing on price
- National players (SunPower, Sunrun, Tesla Energy, Freedom Solar) have massive marketing budgets
- Lead aggregators (EnergySage, SolarReviews, LendingTree) auction the same lead to 5–8 installers simultaneously

**Speed-to-lead crisis:**
- A 2018 MIT study found that solar lead conversion drops by 400% when contact is delayed beyond 5 minutes
- Leads purchased from aggregators arrive at multiple competitors simultaneously
- The company that calls first wins 35–50% more conversions

### 1.2 The Pain Points This Snapshot Must Solve

| Pain Point | How the Snapshot Addresses It |
|------------|------------------------------|
| Leads go cold in minutes | Instant automated SMS + call task within 60 seconds of lead submission |
| Long decision cycle (30–90 days) | Structured multi-touch nurture sequence with ROI education + rebate urgency |
| Financing confusion | Email/SMS sequence explaining cash, loan, lease, PPA with comparison content |
| Government rebate complexity | Dedicated rebate education workflow with province-specific program info |
| High quote drop-off | Automated proposal follow-up sequence (Day 1, 3, 7, 14, 30) |
| Permit/inspection anxiety | Post-contract milestone updates ("Your permit has been submitted!") |
| Referral capture is manual | Automated post-install referral request sequence |
| Commercial deals have different buyers | Separate pipeline with C-suite messaging + ROI/payback framing |
| Battery storage upsell timing | Trigger-based battery add-on workflow after quote |
| EV charger combo opportunity | EV + solar combo workflow for dual-product close |

### 1.3 Industry Cost & System Size Reference

(Source: EnergySage Marketplace, 2026 data)

| System Size | $/Watt | System Cost (Before Incentives) |
|-------------|--------|----------------------------------|
| 4 kW | $2.89/W | $11,560 |
| 6 kW | $2.68/W | $16,080 |
| 8 kW | $2.62/W | $20,960 |
| 10 kW | $2.58/W | $25,800 |
| 12 kW (avg) | $2.56/W | $30,720 |
| 15 kW | $2.47/W | $37,050 |

**Average residential system:** 12 kW at ~$31,135 before incentives
**Average 25-year savings:** $41,000–$155,000 depending on state/province and utility rates

**System cost breakdown:**
- Solar panels: 12% of total
- Inverter(s): 10%
- Racking and mounting: 3%
- Electrical wiring: 9%
- Supply chain/logistics: 9%
- Installation labor: 7%
- Sales & marketing: 18%
- Overhead: 11%
- Installer profit: 11%
- Permitting & interconnection: 8%

**Key insight for sales messaging:** The panels are only 12% of total cost. The installation, permitting, and company quality account for the rest. Premium installers can justify higher prices based on warranty, workmanship, and service.

---

## Part 2: GHL Solar Snapshot — What Exists & What's Missing

### 2.1 What's Currently on the Market

Existing GHL solar snapshots (from freelancers, Snapshots.io, GHL community) typically include:
- Basic contact form / landing page
- Single pipeline with 5–8 generic stages
- Simple auto-SMS and auto-email on lead creation
- Booking calendar for "solar consultation"
- Basic review request sequence after project completion

**What they're missing:**
1. Multi-pipeline architecture (residential vs. commercial vs. battery vs. EV)
2. Speed-to-lead workflows (real 60-second SMS + rep call task routing)
3. Rebate-specific education campaigns (Canada Greener Homes, provincial incentives, SRECs, feed-in tariffs)
4. Long-cycle nurture designed for 30–90 day decision timelines
5. Utility bill calculator integration hooks (webhook to external calculators)
6. Permit/milestone tracking sub-pipeline
7. Commercial solar workflow with different personas (CFO, Facilities Manager, Building Owner)
8. Battery storage upsell automation
9. EV charger combo workflow
10. Post-install referral program with tracking
11. Seasonal re-engagement campaigns ("Energy costs are up again this winter — you could be generating free power")
12. Social proof engine (review + case study capture)

### 2.2 The 1app Differentiation Opportunity

1app should position this snapshot as the **only complete solar operations system for GHL** — not just a CRM, but a complete front-to-back solar business automation platform. The pitch: "From the second a lead lands to the day they refer their neighbor — every touchpoint is automated."

---

## Part 3: Pipeline Architecture

### Pipeline 1: Residential Solar Quote Pipeline

**Target:** Homeowners inquiring about rooftop solar installation (roof mount standard; ground mount as needed)

| Stage # | Stage Name | Description | Trigger Actions |
|---------|-----------|-------------|-----------------|
| 1 | New Lead | Lead just came in (web form, Facebook ad, Google, door knock entry, referral) | Instant SMS + call task to rep within 60 seconds |
| 2 | Contacted | Rep made first contact | Follow-up task set for 24 hours |
| 3 | Energy Assessment Booked | Prospect booked free site evaluation / energy assessment | Confirmation SMS/email + calendar reminder |
| 4 | Energy Assessment Complete | Site evaluation done, roof assessment + shading analysis complete | Proposal prep task assigned |
| 5 | Proposal Sent | System proposal sent (kW system size, panel brand, inverter type, estimated kWh production, net metering credit estimate, payback period) | Proposal follow-up sequence begins |
| 6 | Proposal Reviewed | Prospect opened/acknowledged proposal | Scheduling task: "Book proposal review call" |
| 7 | Financing Discussion | Prospect is evaluating cash, loan, lease, or PPA options | Financing education email sequence |
| 8 | Permit Submitted | Contract signed, permit application submitted to AHJ | Milestone SMS: "Great news! Your permit application is in." |
| 9 | Permit Approved | Permit approved by Authority Having Jurisdiction | SMS: "Your permit is approved! Installation is being scheduled." |
| 10 | Installation Scheduled | Install date confirmed | Confirmation SMS/email + pre-install checklist |
| 11 | Installation Complete | Panels, racking, inverter installed | Inspection scheduling SMS |
| 12 | Inspection Passed | Final inspection approved by inspector | Grid interconnection SMS update |
| 13 | PTO / Energized | Permission to Operate granted, system live, net meter installed | Celebration SMS + review request + referral ask |
| 14 | Won — System Active | Customer is producing solar power | Monthly production update (if integrated) + referral sequence |
| 15 | Lost — No Interest | Prospect disqualified or not interested | 90-day re-engagement drip |
| 16 | Lost — Competitor | Lost to another installer | 6-month re-engagement ("How is your solar system performing?") |

---

### Pipeline 2: Commercial Solar Pipeline

**Target:** Business owners, property managers, facilities directors, CFOs for commercial rooftop solar, ground mount systems, carport canopies, and warehouse solar

**Key differences from residential:**
- Decision makers are multiple: CFO (ROI focus), Facilities Manager (operational), Business Owner (strategic)
- Deal size: $50K–$2M+
- Timeline: 3–18 months from inquiry to install
- Key incentives: ITC (Investment Tax Credit in U.S.), CCA (Capital Cost Allowance in Canada), CCUS credits, utility demand charge reduction
- Financing: C-PACE (Commercial Property Assessed Clean Energy), equipment financing, power purchase agreements

| Stage # | Stage Name | Notes |
|---------|-----------|-------|
| 1 | New Commercial Lead | Source tag (referral, cold outreach, government tender, broker) |
| 2 | Discovery Call Booked | Initial needs assessment |
| 3 | Site Survey Scheduled | Commercial site walk + roof/electrical assessment |
| 4 | Energy Audit Complete | 12 months of utility bills analyzed; demand charge profile reviewed |
| 5 | Preliminary Proposal | High-level ROI summary (payback, IRR, kWh offset, demand charge savings) |
| 6 | Engineering Assessment | Structural analysis, load calculations, single-line diagram |
| 7 | Detailed Proposal | Full engineering proposal with equipment specs, production modeling, incentive stack |
| 8 | Financial Review | CFO/ownership reviewing financing and incentive options |
| 9 | Contract Negotiation | Legal review, interconnection agreement, insurance requirements |
| 10 | Permit & Engineering Approval | AHJ submission, utility interconnection application |
| 11 | Construction / Installation | Timeline managed by milestone sub-pipeline |
| 12 | Commissioning | System tested and energized |
| 13 | Monitoring & Reporting Setup | SCADA or cloud monitoring configured |
| 14 | Won — Operational | Monthly reporting + expansion opportunity follow-up |
| 15 | Lost | Reason tagged; re-engage at renewal or competitor performance issues |

---

### Pipeline 3: Battery Storage Add-On Pipeline

**Target:** Existing solar customers OR new residential/commercial customers considering battery backup (Tesla Powerwall 3, Enphase IQ Battery, SolarEdge Energy Bank, Franklin Electric)

**Key pain points battery solves:**
- Grid outages / power reliability (major driver in rural areas, wildfire zones, ice storm regions in Canada)
- Time-of-use (TOU) rate optimization (charge during off-peak, discharge during peak pricing)
- Net metering rate cuts (California NEM 3.0, Ontario's reduced FIT rates) — battery makes you grid-independent
- Emergency backup for medical equipment, sump pumps, EV charging

| Stage # | Stage Name | Notes |
|---------|-----------|-------|
| 1 | Battery Interest — New | Lead specifically asking about battery + solar |
| 2 | Battery Upsell — Existing Solar | Trigger: existing customer reopened or contacted; battery add-on opportunity |
| 3 | Site Assessment | Existing electrical panel load assessment; backup load selection |
| 4 | Proposal — Battery Only | If they have panels, battery retro-fit quote |
| 5 | Proposal — Solar + Battery Combo | Full system quote with Powerwall / IQ Battery spec'd |
| 6 | Financing Discussion | Battery-specific financing (Enphase Pay, Tesla financing, third-party) |
| 7 | Contract Signed | |
| 8 | Permit + Electrical Inspection | Battery installation requires separate permit in most jurisdictions |
| 9 | Installation Complete | |
| 10 | Won | Post-install: monitor setup, rate optimization education |
| 11 | Lost | |

---

### Pipeline 4: Solar + EV Charger Combo Pipeline

**Target:** Homeowners or businesses with EVs (or planning to buy one) who want to combine solar with Level 2 (L2) EVSE (Electric Vehicle Supply Equipment) or DC fast charging

**The combo pitch:**
- EV drivers spend $1,500–$3,000/year on home charging electricity
- Solar + EV = charge your car for free
- Government EV charger rebates stack with solar rebates (e.g., Canada's ZEVIP program, Ontario EVCO grants, BC's CleanBC EV charger rebate up to $350)
- Installing both together saves on dual permit/inspection costs

| Stage # | Stage Name | Notes |
|---------|-----------|-------|
| 1 | EV + Solar Lead | Entry source tagged (EV dealership referral, social ad, Google "home EV charger + solar") |
| 2 | Combo Consultation Booked | |
| 3 | Site Assessment | EV charger amp requirements + solar roof assessment |
| 4 | Combo Proposal | Solar system + L2 EVSE or bidirectional charger (V2H capable) |
| 5 | EV Rebate Education | Confirm applicable provincial/federal rebates for both products |
| 6 | Contract Signed | |
| 7 | Permit Submitted | Combined permit or dual applications |
| 8 | Installation — Panels | |
| 9 | Installation — EV Charger | |
| 10 | Commissioning | |
| 11 | Won — Driving on Sunshine | Celebration + referral sequence |
| 12 | Lost | |

---

### Pipeline 5: Rebate Inquiry / Lead Nurture Pipeline

**Target:** Prospects who are not yet ready to commit but are researching government rebates (Canada Greener Homes, provincial programs, U.S. IRA credits)

| Stage # | Stage Name | Notes |
|---------|-----------|-------|
| 1 | Rebate Inquiry | Prospect filled out form asking "what rebates am I eligible for?" |
| 2 | Rebate Assessment Sent | Automated email/SMS with relevant rebate info based on location |
| 3 | Consultation Booked | Rep call to walk through rebate eligibility + system sizing |
| 4 | Proposal Sent | Moved to residential pipeline |
| 5 | Nurture — 30 Day | Not ready yet; enters 90-day rebate education sequence |
| 6 | Rebate Deadline Triggered | If a rebate program has an expiry, trigger urgent outreach |
| 7 | Converted to Quote | |
| 8 | No Response — Long Term Nurture | Quarterly check-in for 18 months |

---

## Part 4: Workflows — Complete Library

### Workflow 1: Speed-to-Lead (CRITICAL — Must-Deploy Day One)

**Trigger:** Any new lead enters CRM (Facebook Lead Ad, Google form, website form, landing page)

**Sequence:**
- T+0:00 — Internal notification to assigned rep (SMS + email)
- T+0:00 — Auto-SMS to prospect: "Hi [First Name]! Thanks for your interest in solar — I'm [Rep Name] and I'll be reaching out in just a moment to answer your questions. 🌞 — [Company Name]"
- T+0:30 — Call task created and assigned to rep (5-minute window)
- T+5:00 — If no rep response: escalation SMS to manager
- T+30:00 — If lead still uncontacted: second automated SMS to prospect + second call task
- T+2hr — If still uncontacted: automated voicemail drop
- T+4hr — Final attempt SMS: "Hey [First Name], we've been trying to reach you about your solar inquiry — would [time A] or [time B] work for a quick 10-minute call? [Booking Link]"
- T+24hr — If no contact: email with solar savings calculator + booking link

**Speed-to-lead is the single highest-ROI workflow in any solar snapshot. Document this clearly to clients.**

---

### Workflow 2: Energy Assessment Booking Confirmation

**Trigger:** Lead moves to "Energy Assessment Booked" stage

**Sequence:**
- Immediate — Confirmation email with:
  - Date/time of appointment
  - What to expect (45-min roof/attic assessment, utility bill review, no-obligation)
  - What to have ready (12 months of utility bills or access to utility app)
  - Meet-the-team intro (rep name, photo, credentials)
- Day before appointment — SMS reminder: "Reminder: Your free solar energy assessment is tomorrow at [time]. [Rep Name] will be there to evaluate your roof and show you exactly how much you could save. See you then! ☀️"
- Morning of appointment — SMS reminder: "Good morning [First Name]! We'll be at your home today at [time] for your solar assessment. Reply CONFIRM or call [number] if you need to reschedule."
- Post no-show — SMS: "We missed you at your solar assessment today! Life gets busy — would [date] or [date] work better for you?"

---

### Workflow 3: Proposal Follow-Up Sequence

**Trigger:** Lead moves to "Proposal Sent" stage

**Sequence:**
- Day 0 (send day) — Email: Full proposal with system specs, production estimate in kWh/year, estimated utility bill savings, payback period, incentive stack
- Day 1 — SMS: "Hi [First Name], just checking — did you get a chance to review your solar proposal? Happy to walk through any questions on a quick call. [Booking Link]"
- Day 3 — Email: "The #1 question homeowners ask after seeing their solar proposal" — FAQ email addressing: Is this realistic? What's the catch? What if I sell my home? What warranties are included?
- Day 7 — SMS: "[First Name], solar prices have stayed stable but some rebate programs have limited enrollment — just wanted to flag that before your decision window closes. Reply YES to schedule a 15-min call."
- Day 14 — Email: Case study email — "How the [local family] is saving $185/month with their 10 kW system"
- Day 21 — SMS: "Hey [First Name] — [Rep Name] here. Still here if you want to talk through the numbers. No pressure. What's your biggest hesitation right now?"
- Day 30 — Email: Rebate expiry reminder (if applicable) + final call to action

**If no response by Day 30:** Move to long-cycle nurture (see Workflow 7)

---

### Workflow 4: Financing Education Sequence

**Trigger:** Lead moves to "Financing Discussion" stage

**Email 1 — The Four Ways to Go Solar:**
Subject: The four ways to pay for solar (and which one is right for you)

```
There is no one-size-fits-all answer when it comes to paying for solar. Here's a quick breakdown:

1. CASH PURCHASE — Best long-term ROI. You own the system immediately. All incentives/SRECs/rebates go directly to you.

2. SOLAR LOAN — Low or zero down. Monthly payment often less than your current utility bill. You own the system and claim all incentives.

3. SOLAR LEASE — No upfront cost. Fixed monthly payment. Company owns the system. You don't claim incentives but have zero maintenance responsibility.

4. POWER PURCHASE AGREEMENT (PPA) — You buy the power the panels produce at a fixed rate (lower than utility). Company owns system and handles everything.

For most homeowners, a $0-down solar loan is the sweet spot — lower monthly payments than your utility bill on Day 1, and you own the system by year 10–12.

Want to run the numbers for your specific situation? [Book a financing call]
```

**Email 2 — The Hidden Solar Loan Trap:**
Explain dealer fees, APR increases after promotional period, and how to evaluate loan terms. This builds massive trust because you're educating against bad actors in your own industry.

**Email 3 — Net Metering Explained:**
How net metering works, what credits look like on a utility bill, and why it dramatically changes the ROI math.

---

### Workflow 5: Government Rebate Education Campaign

**Trigger:** Lead tagged with Canada or specific province; or lead enters "Rebate Inquiry" pipeline stage

**CANADA GREENER HOMES (Federal):**
- Canada Greener Homes Loan: Up to $40,000 at 0% interest for 10 years (as of last known program data — always verify current status)
- Note: The original Canada Greener Homes Grant program closed to new applicants in 2023. The loan component continued. **Always verify current status before communicating with prospects.**
- Requires pre- and post-retrofit EnerGuide assessment
- Eligible upgrades include solar PV panels

**SMS Template — Rebate Alert:**
```
[First Name], did you know Ontario homeowners may qualify for federal and provincial programs that can reduce your solar investment significantly? I can walk you through exactly what you qualify for in your area — takes 10 minutes. Want me to run the numbers? [Booking Link]
```

**PROVINCIAL PROGRAMS (verify current status for each province):**

| Province | Program | Notes |
|----------|---------|-------|
| Ontario | Net Metering (Hydro One, OPG, LDCs) | Varies by LDC; bill crediting at retail rate in some jurisdictions |
| Ontario | IESO Net Metering | For systems up to 10 kW (residential), up to 500 kW (commercial) |
| BC | BC Hydro Net Metering | Systems up to 100 kW; excess credits at avoided cost rate |
| Alberta | Micro-Generation Regulation | Systems up to 5 MW; export at avoided cost |
| Nova Scotia | Net Metering Program | Limited enrollment |
| Saskatchewan | SaskPower Net Metering | |
| Quebec | Hydro-Québec Self-Generation | Currently limited availability |

**U.S. FEDERAL INCENTIVES:**
- Investment Tax Credit (ITC / Residential Clean Energy Credit): 30% federal tax credit on total system cost (panels, labor, inverter, battery if paired with solar)
- No cap on residential systems
- Applies through 2032 at 30%; steps down to 26% in 2033

**SREC Markets (select U.S. states):**
Homeowners earn one SREC per MWh of solar production. Values by state (2026):
- Washington D.C.: ~$383/SREC (~$4,200–$5,700/year for 10 kW system)
- New Jersey: ~$175/SREC (~$1,900–$2,600/year)
- Maryland: ~$48/SREC (~$440–$880/year)

**Rebate Urgency Email Template:**
```
Subject: [Time-sensitive] Your solar rebate eligibility window

[First Name],

Government rebate programs for solar have enrollment windows, and some have already closed to new applicants.

Here's what we know is currently available in [Province/State]:
• [Specific current program] — [amount]
• [Net metering program] — [rate/policy]
• [Federal program] — [status]

We can walk you through exactly which programs you qualify for and how to claim them — this typically takes 15 minutes on a call.

[Book Your Rebate Review Call]

Note: We always verify current program availability before any client communication. Programs change frequently.

[Rep Name]
[Company Name]
```

---

### Workflow 6: Post-Contract Milestone Tracking

**Trigger:** Contract signed / moved to "Permit Submitted" stage

**Milestone SMS/Email Sequence:**
- Permit Submitted: "Great news, [First Name]! Your solar permit has been submitted to [Municipality]. This typically takes 2–4 weeks. We'll keep you updated every step of the way."
- Permit Approved: "Your solar permit has been APPROVED! 🎉 Your installation is now being scheduled. You'll hear from us within [X] business days to confirm your installation date."
- Install Date Confirmed: "Your installation is confirmed for [Date]. Our crew will arrive between [Time Window]. Here's what to expect on install day: [Link to prep guide]."
- Installation Complete: "Your solar panels are up! ☀️ Our team just finished your installation. The next step is your electrical inspection — we'll schedule that now."
- Inspection Passed: "Inspection passed! 🎉 We're now submitting for utility interconnection / Permission to Operate (PTO). This is the final step before your system goes live."
- PTO Granted / System Live: "Your system is LIVE! 🌞 You are now generating clean solar power. Your first net metering statement will arrive with your next utility bill. [Monitoring app setup instructions]"

---

### Workflow 7: Long-Cycle Nurture Sequence (30–90 Day Decision Cycle)

**Trigger:** Prospect has been in CRM 30+ days without conversion; or manually enrolled by rep

**Goal:** Stay top of mind without being annoying. Educate, not harass. Each touch adds value.

| Day | Channel | Content |
|-----|---------|---------|
| Day 1 | Email | Welcome to the solar education series — "How Solar Actually Works" |
| Day 7 | SMS | Quick stat: average solar homeowner saves $X per month in [City/Province] |
| Day 14 | Email | "The Solar Payback Period Calculator" — personalized savings estimate |
| Day 21 | SMS | "[First Name], utility rates in Ontario increased X% this year. Just a thought." |
| Day 30 | Email | "5 Questions to Ask Any Solar Company Before You Sign" (trust-building, positions you as the honest option) |
| Day 45 | SMS | Case study text: "Our clients in [Neighbourhood] just passed their system inspection — 10.8 kW system, $0 down, saving $210/month." |
| Day 60 | Email | Rebate update email — "Here's what's changed in solar incentives this month" |
| Day 75 | SMS | "[First Name], spring is the best time to install solar — systems installed before [date] qualify for the full production season this year." |
| Day 90 | Phone task | Rep attempts personal outreach — final decision nudge |
| Day 120 | Email | Seasonal re-engagement — "Your neighbours are going solar. Here's what they told us." |
| Day 180 | SMS | "6 months ago you asked about solar. Utility rates are up again. Want to revisit the numbers?" |
| Day 365 | Email | Annual re-engagement — "Your solar savings estimate from last year has actually improved." |

---

### Workflow 8: Battery Storage Upsell Sequence

**Trigger:** Existing client OR prospect who completed proposal review; tag = "Battery Candidate"

**Qualification triggers:**
- Homeowner mentions power outages
- Homeowner is on time-of-use (TOU) rates
- Net metering rates were reduced in their utility territory
- Homeowner has an EV (bidirectional charging opportunity)

**SMS Day 0:** "Hey [First Name] — have you heard about the new battery storage options we're pairing with solar systems? Homeowners with batteries are now completely grid-independent during outages. Worth a 10-min chat? [Booking Link]"

**Email Day 1 — The Case for Battery Storage:**
```
Subject: Why more solar homeowners are adding batteries in 2026

[First Name],

When we designed your solar system, we focused on maximizing your daytime kWh production and net metering credits.

But something has changed in [region]:
- Grid outages are up [X]% in the past 3 years
- Time-of-use rates mean your grid power costs [X]x more during peak hours (5–9 PM)
- Net metering rates in Ontario dropped from retail to [current rate] for new systems

A Tesla Powerwall 3 (13.5 kWh) or Enphase IQ Battery paired with your panels changes this equation:
• Store excess solar instead of exporting at low feed-in tariff rates
• Draw from your battery during peak TOU pricing (5–9 PM)
• Full backup power during grid outages (power your entire home for 12–24+ hours)
• EV charging from battery overnight

The math often pays for itself in 5–7 years with TOU optimization alone.

Want to run the numbers for your system? [Book Battery Consultation]
```

---

### Workflow 9: EV Charger Combo Campaign

**Trigger:** Lead or existing client has tag "EV Owner" or "EV Interested"

**Entry points:**
- EV dealership referral partner (Rivian, Tesla, GM EV, Hyundai IONIQ dealerships)
- Web ad targeting EV owners: "Already have an EV? You're leaving money on the table if you're not charging with solar."
- Existing solar client who mentions getting an EV

**Email 1 — "You're charging your EV wrong":**
```
Subject: EV owners: you're paying too much to charge

If you're charging your EV on grid power, you're spending approximately $1,800–$3,000/year in electricity just to drive.

Here's a better calculation:

A 10 kW solar system generates roughly 11,000–14,000 kWh/year.
The average EV uses 3–4 miles per kWh.
A typical Canadian/American driver logs 15,000 km/year = ~5,000 kWh of EV charging.

Result: Your solar system more than covers your entire year of driving AND your home electricity — at zero marginal cost.

The math gets even better when you layer in:
• Level 2 home EV charger (full charge overnight vs. 3 days on a standard outlet)
• Federal EV charger rebates (Canada: ZEVIP up to $5,000 for Level 2)
• Solar rebates (federal + provincial stack)

We install the solar system AND the EV charger in one visit, saving you a second permit and inspection cycle.

[Calculate Your EV + Solar Combo Savings]
```

---

### Workflow 10: Post-Install Review & Referral Campaign

**Trigger:** Lead moves to "PTO / Energized" or "Won — System Active"

**This is your highest-ROI workflow after speed-to-lead. Solar customers are the best referrers in home services.**

**Day 0 — Celebration SMS:**
"🌞 CONGRATULATIONS [First Name]! Your solar system is officially live and generating clean energy. Welcome to the solar family!"

**Day 3 — Review Request Email:**
```
Subject: How was your experience? (30 seconds)

[First Name],

Your [X] kW solar system has been generating power for 3 days. By our estimate, you've already produced approximately [X] kWh of clean energy — equivalent to [X trees planted / X pounds of CO₂ avoided].

We'd love to hear how the experience was from your perspective. A quick Google review helps other homeowners in [City] find a trustworthy solar installer:

[Leave a Google Review — 30 seconds]

Thank you for choosing [Company Name].

[Rep Name]
```

**Day 14 — Referral Ask SMS:**
"Hey [First Name] — know any neighbours or friends who've mentioned wanting to go solar? We give you $[250–500] cash when anyone you refer installs with us. Just reply with their name and I'll take it from there."

**Day 30 — Referral Email:**
```
Subject: Your solar system just completed its first full month ☀️

[First Name],

Your system stats for Month 1:
• Estimated production: [X] kWh
• Estimated utility savings: $[X]
• CO₂ offset equivalent: [X trees / X lbs of emissions]

Your referral link: [unique referral link]
For every friend or neighbour who installs solar through your referral, you earn $[amount].

Your neighbours are probably already asking you about it. Here's what to tell them:
"I'm saving about $[X]/month and [Company Name] handled everything. Here's their info: [link]"

[Share Your Referral Link]
```

**Day 90 — Annual Review Set:**
"[First Name], your system is almost 3 months old! Let's schedule a quick check-in to review your production numbers and make sure your net metering is set up correctly. [Booking Link]"

---

## Part 5: Forms & Landing Pages

### Form 1: Free Energy Assessment Request (Primary Lead Capture)

**Fields:**
- First Name ✓
- Last Name ✓
- Email ✓
- Phone ✓ (required — for speed-to-lead SMS)
- Street Address ✓ (for Google Maps roof analysis / solar potential pre-check)
- Average Monthly Electricity Bill (dropdown: <$100, $100–$150, $150–$200, $200–$300, $300+)
- Do you own or rent your home? (Owner/Renter — filter renters to landlord/commercial path)
- How soon are you looking to install? (ASAP / 3–6 months / 6–12 months / Just researching)
- How did you hear about us? (Google, Facebook, Neighbour referral, Door knock, Other)

**Hidden fields:**
- UTM source, medium, campaign, ad name (for lead source tracking)
- Referring rep / referral code

**Thank you page:**
- "Your free energy assessment is being matched to a solar advisor in your area — expect a call or text within [5 minutes / same day]."
- Option to book directly via calendar embed
- Trust elements: BBB rating, certifications (NABCEP, CEC), review count

---

### Form 2: Battery Storage Interest Form

**Fields:**
- First Name, Last Name, Email, Phone
- Do you already have solar panels? (Yes/No)
- If yes: Who installed them? Approximate system size?
- What is your main interest in battery storage? (Backup power / Bill reduction / Both)
- Have you experienced power outages in the past year? (Yes/No)
- Do you own an EV? (Yes/No)

---

### Form 3: Commercial Solar RFI (Request for Information)

**Fields:**
- First Name, Last Name, Email, Phone
- Company Name
- Property Type (Warehouse / Office / Retail / Agricultural / Multi-unit Residential / Other)
- Approximate Monthly Electricity Bill ($)
- Average kWh usage per month (if known)
- Roof size estimate (sq ft, if known)
- Are you the property owner or tenant? (Owner / Tenant with long-term lease / Other)
- Timeline for decision
- How did you hear about us?

---

### Form 4: Referral Submission Form

**Fields:**
- Your Name
- Your Email (existing client)
- Referral's Name
- Referral's Phone or Email
- Any notes (e.g., "They have a south-facing roof and mentioned high bills")

**On submit:** Assign to referral source rep, create new contact, trigger speed-to-lead workflow, log referral source for commission tracking

---

### Landing Page Library

| Page | Purpose | Headline Concept |
|------|---------|-----------------|
| Solar Savings Calculator | Top-of-funnel lead capture | "Find out how much you could save on electricity in 60 seconds" |
| Free Energy Assessment | Mid-funnel action | "We'll evaluate your roof, your bill, and your rebate eligibility — free, no obligation" |
| Battery Storage | Battery lead capture | "Never lose power again: Solar + Battery Storage for Canadian Homes" |
| EV + Solar Combo | EV owner targeting | "Charge your EV for free: The solar + EV charger combination" |
| Commercial Solar | Commercial lead capture | "Reduce your facility's electricity costs by 60–80% with commercial solar" |
| Rebate Guide | Rebate inquiry capture | "What government solar rebates are you leaving on the table?" |
| Referral Portal | Referral tracking | "Share solar. Earn cash. [Client Portal Login]" |

---

## Part 6: SMS & Email Templates — Complete Library

### 6.1 Speed-to-Lead SMS Templates

**Instant SMS (T+0):**
```
Hi [First Name]! Got your solar inquiry — I'm [Rep Name] from [Company]. I'll be calling you in the next few minutes. If now isn't a good time, reply with a better time and I'll reach out then. ☀️
```

**Second Attempt (T+30 min):**
```
[First Name], still trying to connect with you about your solar savings estimate. We're seeing [City/Province] homeowners saving avg $185/month. When's a good time to chat? — [Rep Name]
```

**Booking Link SMS (T+4hr):**
```
Hey [First Name] — wanted to make this easy. You can pick a time that works for you right here: [Booking Link]. Looking forward to showing you the numbers. — [Rep Name]
```

---

### 6.2 ROI Education SMS Templates

**Utility Rate Spike:**
```
[First Name], Ontario electricity rates are going up again in [Month]. Homeowners with solar lock in their rate today — they produce their own power. Worth a 10-min call? [Booking Link]
```

**Neighbour Social Proof:**
```
[First Name] — just finished installing a 9.6 kW system on [Street/Area] last week. Homeowner will save ~$210/month. Your house has similar solar potential. Want to see your numbers? Reply YES.
```

**Payback Period Hook:**
```
Quick math: avg solar system in Ontario pays for itself in 8–10 years. Average system lifespan: 25–30 years. That's 15–20 years of essentially free electricity. Worth a conversation? [Rep Name]
```

---

### 6.3 Proposal Follow-Up Email Templates

**Day 3 — FAQ Email:**
```
Subject: The 5 questions every homeowner asks after seeing a solar proposal

[First Name],

After sharing hundreds of solar proposals, here are the questions we hear most:

1. "Is the production estimate realistic?"
We model based on your actual roof orientation, pitch, and local irradiance data (kWh/m²/day for your postal code). We're conservative by design — we'd rather over-deliver than overpromise.

2. "What if I sell my house?"
Solar increases home resale value by an average of 3–4% (Lawrence Berkeley National Laboratory study). Buyers often pay a premium for homes with owned solar systems. Leased systems require transfer — another reason we recommend purchase or loan over lease.

3. "What happens if a panel or inverter fails?"
Your system comes with [X]-year panel performance warranty (most tier-1 manufacturers: 25 years), [X]-year microinverter/string inverter warranty, and our [X]-year workmanship warranty. Production monitoring alerts us (and you) to any issues automatically.

4. "How do I actually read my net metering bill?"
We'll walk you through this on our review call. Net metering means you see credits on your bill for every kWh your panels send back to the grid — it runs your meter backward.

5. "What's my actual payback period?"
Based on your utility bill and our proposal, your estimated payback is [X] years. After that, you're generating free power for another 15–20 years.

Ready to move forward? [Book Your Proposal Review Call]

[Rep Name]
```

---

### 6.4 Rebate Campaign Email Templates

**Canada Greener Homes Email:**
```
Subject: Government solar programs in [Province] — here's what you qualify for

[First Name],

Federal and provincial programs make solar more affordable than most homeowners realize. Here's a summary of what's currently available in [Province]:

FEDERAL:
• Canada Greener Homes Loan: Up to $40,000 at 0% interest (verify current availability)
• Requires a pre-retrofit EnerGuide home energy assessment (~$400–$600)

PROVINCIAL — [PROVINCE]:
• [Current program name and details — verified before sending]
• Net metering with [Local Utility]: [Rate and policy]

WHAT THIS MEANS FOR YOUR SYSTEM:
• Estimated system cost before programs: $[X]
• After applicable incentives: $[X]
• Your effective out-of-pocket (if financing at 0%): $[X]/month

We handle the program paperwork as part of your installation — you don't need to navigate the government websites yourself.

Want me to confirm exactly which programs you qualify for?

[Book Your Rebate Eligibility Call — 15 minutes]

[Rep Name]

DISCLAIMER: Government programs change frequently. All program details will be verified at time of your consultation. This email is for educational purposes only.
```

---

### 6.5 Commercial Solar Outreach Templates

**Cold Email — Business Owner:**
```
Subject: [Company Name]'s electricity bill — a question

[First Name],

I noticed [Company Name] operates a [warehouse/facility/retail location] in [City]. Businesses like yours typically spend $[X,000]–$[X,000]/month on electricity.

Commercial solar + battery storage can reduce that by 60–80% — and in most cases, the monthly financing payment is less than your current utility bill from Day 1.

A few quick questions before I waste your time with a full proposal:
• Do you own the building or are you on a long-term lease (10+ years)?
• Is your average monthly electricity bill above $3,000?
• Are you open to a 10-minute call to see if the numbers work for your location?

No pressure — if it doesn't pencil out, I'll tell you that on the call.

[Rep Name]
[Company Name]
[Phone]
```

**Commercial Follow-Up SMS:**
```
Hi [First Name] — [Rep Name] from [Company]. I sent an email about your facility's electricity costs earlier this week. Commercial solar is saving businesses in [City] 60–80% on power. 10-minute call worth your time? [Booking Link]
```

---

### 6.6 Referral Campaign Templates

**SMS — Asking for Referrals:**
```
[First Name] — your solar system has been generating power for [X] weeks now! Quick question: do you know anyone who's been talking about going solar? We pay $[amount] in cash for successful referrals. Just reply with their name and I'll handle the rest.
```

**Email — Monthly Referral Reminder:**
```
Subject: ☀️ Your system is running great — and you can earn $[amount]

[First Name],

Your [X] kW solar system has now generated approximately [X] kWh since installation — that's roughly [X trees / X miles of CO₂ offset].

A reminder: for every person in your network who goes solar through your referral, you earn $[amount] in cash (or [store credit / Amazon gift card — your choice]).

Your referral link: [Link]

Solar customers like you are our best marketing. Your neighbours trust your experience more than any ad.

[Rep Name]
```

---

## Part 7: Calendar & Booking Flow

### Calendar 1: Free Energy Assessment / Site Evaluation
- **Name:** Free Solar Energy Assessment
- **Duration:** 45–60 minutes (in-home) or 30 minutes (virtual)
- **Availability:** Monday–Saturday, 9 AM–6 PM
- **Buffer:** 15 minutes post-appointment for drive time / notes
- **Confirmation:** SMS + email immediately on booking
- **Reminders:** 48 hours before, 2 hours before
- **Pre-appointment form:** Address, utility company, average bill
- **Post-appointment task:** Create opportunity in CRM, send proposal within 24 hours

### Calendar 2: Proposal Review Call
- **Name:** Solar Proposal Review — 30 Minutes
- **Duration:** 30 minutes
- **Meeting type:** Video (Zoom) or phone
- **Trigger:** Automatically surfaced in Day 1 proposal SMS and Day 3 FAQ email

### Calendar 3: Commercial Discovery Call
- **Name:** Commercial Solar Discovery Call
- **Duration:** 30 minutes
- **Pre-call form:** Company name, facility type, utility bill range, decision-making authority

### Calendar 4: Battery Storage Consultation
- **Name:** Battery Storage Consultation
- **Duration:** 30 minutes
- **Focus:** TOU optimization, backup load calculation, payback for battery-only or combo

### Calendar 5: Rebate Eligibility Review
- **Name:** Free Rebate Eligibility Check
- **Duration:** 15 minutes
- **Low-pressure entry point:** Perfect for fence-sitters who are interested but not ready to commit to a full assessment

---

## Part 8: Custom Fields & Contact Tags

### Custom Fields (Contact Level)

| Field Name | Type | Purpose |
|-----------|------|---------|
| Monthly Electricity Bill | Dropdown | Lead qualification |
| Roof Type | Dropdown (Asphalt shingle, Metal, Tile, Flat/TPO) | Installation planning |
| Roof Age | Number | Replacement timing |
| Home Ownership | Dropdown (Owner / Renter) | Qualification |
| Annual kWh Usage | Number | System sizing |
| System Size Quoted (kW) | Number | Proposal tracking |
| Estimated Annual Production (kWh) | Number | |
| Proposal Amount ($) | Currency | Deal value |
| Estimated Savings/Month ($) | Currency | |
| Estimated Payback Period (years) | Number | |
| Incentives Applied | Text | Program names |
| Financing Type | Dropdown (Cash / Loan / Lease / PPA) | |
| Panel Brand | Text | Equipment tracking |
| Inverter Type | Dropdown (String / Microinverter / Power Optimizer) | |
| Battery Interest | Yes/No | Upsell flag |
| EV Owner | Yes/No | EV combo flag |
| Permit Number | Text | |
| Installation Date | Date | |
| PTO Date | Date | |
| Referral Source | Text | Attribution |
| Referral Code | Text | Referral tracking |
| Net Metering Account # | Text | Post-install |

### Custom Fields (Opportunity Level)

| Field Name | Type |
|-----------|------|
| System Type | Dropdown (Residential / Commercial / Battery-Only / EV Combo) |
| System Size (kW) | Number |
| Battery Included? | Yes/No |
| EV Charger Included? | Yes/No |
| Proposal Version | Number |
| Deal Stage Notes | Text |
| Expected Close Date | Date |
| Install Crew Assigned | Text |
| Permit Status | Dropdown |

### Contact Tags

```
lead-residential
lead-commercial
lead-battery
lead-ev-combo
lead-rebate-inquiry
source-facebook
source-google
source-door-knock
source-referral
source-ev-dealership
source-utility-bill-campaign
qualified
unqualified-renter
unqualified-no-roof
battery-candidate
ev-owner
proposal-sent
proposal-reviewed
contract-signed
permit-submitted
permit-approved
installed
pto-granted
review-requested
review-completed
referral-requested
referrer
won
lost-competitor
lost-no-interest
lost-financing
nurture-30day
nurture-90day
long-term-nurture
re-engage-q1
re-engage-q3
commercial-owner
commercial-cfo
commercial-facilities
```

---

## Part 9: Reporting & Dashboard

### Dashboard 1: Sales Performance

**Widgets:**
- New leads this week / month (by source)
- Leads contacted within 5 minutes (speed-to-lead rate)
- Opportunities in each pipeline stage
- Proposal conversion rate (proposals sent → contracts signed)
- Average deal value by product type
- Won deals this month vs. goal
- Revenue booked vs. pipeline forecast

### Dashboard 2: Marketing Attribution

**Widgets:**
- Leads by source (Facebook, Google, door knock, referral, EV dealer)
- Cost per lead by source (if ad spend data connected)
- Lead-to-appointment rate by source
- Lead-to-close rate by source
- Best-performing lead source by close rate (not just volume)

### Dashboard 3: Operations Pipeline

**Widgets:**
- Permits pending
- Permits approved this week
- Installations scheduled this week
- Inspections pending
- PTO applications submitted
- Overdue milestones (permit > 30 days, inspection > 14 days)

### Dashboard 4: Referral Program

**Widgets:**
- Total referrals submitted this month
- Referral conversion rate
- Revenue attributed to referrals
- Top referrers (customers)
- Referral commissions owed

---

## Part 10: Automation Triggers — Integration Hooks

### Webhook Integrations to Document for Clients

| Integration | Purpose | GHL Implementation |
|------------|---------|-------------------|
| Google Ads Conversions | Track form fills as conversions | GHL webhook → Google Ads API |
| Facebook Lead Ads | Auto-import leads from FB campaigns | GHL Facebook Ads integration |
| Aurora Solar / OpenSolar | Proposal generation trigger | Webhook to proposal tool on "Energy Assessment Complete" |
| DocuSign / PandaDoc | Contract signature trigger | Stage change on signed notification webhook |
| QuickBooks / Xero | Invoice creation on contract signed | Webhook on stage change |
| Google Reviews | Review request automation | Automated SMS/email with Google Review link |
| Sunburst / AlsoEnergy / Enphase Enlighten | Production monitoring alerts | API webhook on production anomaly |
| Permit Tracking Apps | Permit status updates | Webhook from permit software to GHL stage change |

---

## Part 11: What Would Make This Snapshot Stand Out

### Differentiators vs. Generic Solar Snapshots on the Market

1. **Multi-pipeline architecture** — Most have one generic pipeline. 1app's snapshot has 5 distinct pipelines for residential, commercial, battery, EV combo, and rebate inquiry.

2. **Speed-to-lead workflow built for the 5-minute window** — Includes escalation logic, rep accountability tracking, and fallback automation when reps miss the window.

3. **Canadian-specific content** — Canada Greener Homes, provincial net metering policies, IESO rules, provincial program matrix. Most GHL snapshots are U.S.-only.

4. **Rebate education as a conversion tool** — Full email + SMS sequences around rebate complexity, using government programs as urgency drivers. This is the single biggest trust-building opportunity in solar sales.

5. **Financing education sequence** — Full 3-email sequence explaining cash, loan, lease, PPA with the "hidden solar loan trap" email that builds massive differentiation trust.

6. **Post-contract milestone tracking** — Permit submitted → approved → install scheduled → installed → inspection → PTO. Clients stay informed and don't call to check in constantly.

7. **Commercial solar as a full separate workflow** — CFO vs. Facilities Manager vs. Business Owner personas. Different messaging, different pipeline, different timeline expectations.

8. **Battery storage upsell automation** — Triggered by TOU rate changes, power outage mentions, or net metering rate reduction in their utility territory.

9. **EV + solar combo workflow** — A growing market segment with referral partnerships at EV dealerships.

10. **Referral engine built in** — With a dedicated referral tracking form, unique referral links, automated commission tracking, and 3-touch referral request sequence.

11. **Dashboard trilogy** — Sales performance, marketing attribution, AND operations pipeline tracking (permit/inspection/PTO milestones). Most solar snapshots have none of this.

12. **Industry-standard language throughout** — kWh, kW, kilowatt, microinverter, string inverter, power optimizer, net metering, net energy metering, feed-in tariff, PTO, AHJ, NABCEP, ITC, SREC, LDC, EnerGuide, FIT, IESO, TOU. Clients buy this from someone who speaks the language.

---

## Part 12: Snapshot Delivery Recommendations for 1app

### Package Structure

**Tier 1: Solar Starter Snapshot — $497 one-time or included in base plan**
- Residential pipeline (stages 1–14)
- Speed-to-lead workflow
- Energy assessment booking + confirmation
- Basic proposal follow-up (7-day sequence)
- Post-install review request
- Landing page: Free energy assessment
- Core custom fields + tags
- Sales performance dashboard

**Tier 2: Solar Pro Snapshot — $997 one-time or Pro plan**
Everything in Starter, plus:
- Commercial pipeline
- Battery storage pipeline
- Long-cycle nurture sequence (full 365-day)
- Financing education sequence
- Rebate campaign (generic + province-selectable)
- Referral program full build
- Post-contract milestone tracking
- EV + solar combo pipeline
- Full 5-dashboard reporting suite
- All SMS/email templates (complete library)
- All 5 landing pages + 4 forms

**Tier 3: Solar Enterprise — Custom + setup fee**
Everything in Pro, plus:
- White-glove setup and customization
- Province-specific rebate content built and verified
- Integration setup (Google Ads, Facebook Lead Ads, DocuSign)
- Training videos for sales team
- Custom ROI dashboard
- Quarterly snapshot updates as programs change

### Onboarding Checklist for Solar Clients

```
□ Connect Facebook Lead Ads integration
□ Connect Google Ads conversion tracking
□ Set up speed-to-lead rep routing (assign reps to lead sources)
□ Customize SMS sender name + number
□ Set up booking calendars (5 total)
□ Verify government rebate content for client's province/state
□ Connect review platform (Google Business Profile)
□ Set up referral tracking custom field + unique links
□ Configure pipeline automation triggers
□ Test speed-to-lead workflow end-to-end
□ Set up dashboard access for client + sales manager
□ Record loom walkthrough video for client team
□ Schedule 30-day check-in call
```

---

## Part 13: Competitive Intelligence — What Competitors' Snapshots Lack

Based on market research of GHL snapshot libraries, freelancer offerings, and solar CRM forums:

**Common gaps in existing solar snapshots:**
- No speed-to-lead escalation workflow (single SMS and done)
- No commercial pipeline at all
- No battery storage or EV combo consideration
- Rebate content either missing or US-only
- Generic home services messaging (not solar-specific)
- No milestone tracking after contract signing
- No financing education sequence
- No long-cycle nurture beyond 30 days
- Single dashboard or none

**1app's positioning:**
"The only GHL solar snapshot built by people who understand the actual solar sales cycle — from lead in to system live."

---

## Appendix A: Solar Glossary (For Client Onboarding & Template Context)

| Term | Definition |
|------|-----------|
| kW (kilowatt) | Unit of power; system capacity (e.g., 10 kW system) |
| kWh (kilowatt-hour) | Unit of energy; how electricity is billed and solar production is measured |
| kWh/m²/day | Solar irradiance — average daily solar energy available at a location |
| Net Metering | Utility billing system where excess solar production earns bill credits |
| Feed-in Tariff (FIT) | Rate utilities pay for solar power fed to the grid |
| NEM (Net Energy Metering) | U.S. term for net metering |
| SREC | Solar Renewable Energy Certificate — one per MWh of production |
| ITC | Investment Tax Credit — 30% federal tax credit on solar in the U.S. |
| PTO | Permission to Operate — utility approval to turn on solar system |
| AHJ | Authority Having Jurisdiction — local building/electrical authority |
| Microinverter | Per-panel inverter (Enphase) — best for shading or complex roofs |
| String Inverter | Single central inverter for entire array — lowest cost, best for simple roofs |
| Power Optimizer | Per-panel device paired with string inverter (SolarEdge) |
| Roof Mount | Standard solar installation attached to roof rafters |
| Ground Mount | Free-standing panel array on racking in yard/field |
| Monocrystalline | High-efficiency solar panel type — most common in residential |
| Polycrystalline | Lower efficiency but lower cost solar panel type |
| Tesla Powerwall | 13.5 kWh AC-coupled battery storage system |
| Enphase IQ Battery | DC-coupled battery storage, pairs with Enphase microinverters |
| SolarEdge | Inverter brand using power optimizers; common in residential |
| EnerGuide | Canadian home energy assessment program (NRCan) |
| IESO | Independent Electricity System Operator (Ontario grid authority) |
| LDC | Local Distribution Company (Ontario utilities: Hydro One, Toronto Hydro, etc.) |
| TOU | Time-of-Use — electricity pricing that varies by time of day |
| PPA | Power Purchase Agreement — third-party owns system, you buy power |
| C-PACE | Commercial Property Assessed Clean Energy financing |
| NABCEP | North American Board of Certified Energy Practitioners — solar installer certification |
| ZEVIP | Zero Emission Vehicle Infrastructure Program (Canada EV charger rebate) |
| SolarApp+ | DOE permit automation platform to streamline residential solar permitting |
| V2H | Vehicle-to-Home — bidirectional EV charger technology |
| EVSE | Electric Vehicle Supply Equipment (EV charger) |

---

## Appendix B: Canada-Specific Rebate & Policy Reference

**IMPORTANT DISCLAIMER:** Government programs in Canada change frequently. Always verify current availability, amounts, and eligibility requirements with official sources (NRCan, provincial energy ministries) before communicating specific numbers to clients or prospects.

### Federal Programs

**Canada Greener Homes Initiative (Federal)**
- Original Grant: Closed to new applicants in 2023 (up to $5,000 for solar)
- Loan component: Canada Greener Homes Loan — up to $40,000 at 0% interest for 10 years (verify current availability with NRCan)
- Requires: Pre- and post-retrofit EnerGuide home energy assessment by registered energy advisor
- Eligible upgrades: Solar PV panels, insulation, windows, heat pumps, and more

**Canada Greener Affordable Housing (CGAH)**
- Targeted at affordable housing providers and social housing organizations
- Not residential homeowner-facing

### Provincial Programs (Summary — verify before client use)

**Ontario:**
- Net Metering through local LDCs (Hydro One, Toronto Hydro, etc.) — systems up to 10 kW residential, up to 500 kW commercial
- Excess generation credited at retail rate within billing period; larger excess credited at lower avoided cost rate
- No provincial solar grant program currently (FIT/microFIT programs closed to new applicants)

**British Columbia:**
- BC Hydro Net Metering — systems up to 100 kW; monthly billing with excess credited at avoided cost
- CleanBC EV Charger Rebate — up to $350 for Level 2 EV charger (residential)
- ZEVIP (federal, NRCan) — up to $5,000 for Level 2 or DCFC at eligible locations

**Alberta:**
- Micro-Generation Regulation — up to 5 MW; export credited at utility avoided cost
- No provincial solar grant
- Energy Efficiency Alberta programs (verify current status)

**Quebec:**
- Hydro-Québec Self-Generation — limited net metering availability; complicated by high hydro rates making solar economics challenging in Quebec

**Nova Scotia:**
- Net Metering Program (Nova Scotia Power) — 100 kW max
- PACE NS financing available in some municipalities

**Manitoba:**
- Manitoba Hydro Net Metering — systems up to 100 kW

**Saskatchewan:**
- SaskPower Net Metering — 100 kW max

### Canadian Solar Industry Associations (Client Resources)

- **CanSIA** — Canadian Solar Industries Association (cansol.ca)
- **NRCan** — Natural Resources Canada (nrcan.gc.ca) — official rebate portal
- **IESO** — Independent Electricity System Operator (ieso.ca) — Ontario grid/net metering rules

---

## Appendix C: Snapshot Build Checklist

### Pipelines
- [ ] Pipeline 1: Residential Solar Quote (16 stages)
- [ ] Pipeline 2: Commercial Solar (15 stages)
- [ ] Pipeline 3: Battery Storage Add-On (11 stages)
- [ ] Pipeline 4: Solar + EV Charger Combo (12 stages)
- [ ] Pipeline 5: Rebate Inquiry / Lead Nurture (8 stages)

### Workflows
- [ ] Workflow 1: Speed-to-Lead (60-second trigger)
- [ ] Workflow 2: Energy Assessment Booking Confirmation
- [ ] Workflow 3: Proposal Follow-Up (30-day sequence)
- [ ] Workflow 4: Financing Education (3-email series)
- [ ] Workflow 5: Government Rebate Education Campaign
- [ ] Workflow 6: Post-Contract Milestone Tracking
- [ ] Workflow 7: Long-Cycle Nurture (12-month sequence)
- [ ] Workflow 8: Battery Storage Upsell Sequence
- [ ] Workflow 9: EV Charger Combo Campaign
- [ ] Workflow 10: Post-Install Review & Referral

### Forms
- [ ] Form 1: Free Energy Assessment Request
- [ ] Form 2: Battery Storage Interest Form
- [ ] Form 3: Commercial Solar RFI
- [ ] Form 4: Referral Submission Form

### Landing Pages
- [ ] Solar Savings Calculator (top-of-funnel)
- [ ] Free Energy Assessment
- [ ] Battery Storage
- [ ] EV + Solar Combo
- [ ] Commercial Solar
- [ ] Rebate Guide
- [ ] Referral Portal

### Calendars
- [ ] Calendar 1: Free Energy Assessment (60 min, in-home/virtual)
- [ ] Calendar 2: Proposal Review Call (30 min, video/phone)
- [ ] Calendar 3: Commercial Discovery Call (30 min)
- [ ] Calendar 4: Battery Storage Consultation (30 min)
- [ ] Calendar 5: Rebate Eligibility Review (15 min)

### Custom Fields
- [ ] All 24 contact-level custom fields
- [ ] All 9 opportunity-level custom fields

### Tags
- [ ] All 40+ contact tags implemented
- [ ] Tag-based workflow triggers configured

### Dashboards
- [ ] Dashboard 1: Sales Performance
- [ ] Dashboard 2: Marketing Attribution
- [ ] Dashboard 3: Operations Pipeline
- [ ] Dashboard 4: Referral Program

### SMS/Email Templates
- [ ] Speed-to-lead SMS sequence (3 templates)
- [ ] ROI education SMS (3 templates)
- [ ] Proposal follow-up email series
- [ ] Financing education series (3 emails)
- [ ] Rebate campaign email templates
- [ ] Commercial outreach templates
- [ ] Post-install review + referral templates

---

*Document prepared by Maximus | 1app Technologies Research Division | July 2026*
*All government program details require verification before use in client-facing communications.*
*Industry cost data sourced from EnergySage Marketplace 2026 dataset.*
