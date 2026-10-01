# GHL Snapshot Research: Handyman / General Home Repair
## Build Document for 1app Agency
**Document Type:** Agency Build Research | Snapshot Architecture  
**Vertical:** Handyman / General Home Repair / Honey-Do Services  
**Audience:** 1app internal — snapshot builders and account managers  
**Version:** 1.0 | July 2026  

---

## Executive Summary

The handyman vertical is one of the most underserved home services niches in GHL automation. Most handymen run off word-of-mouth, a basic Facebook page, and a personal cell phone. They have no system for speed-to-lead, no review capture, no recurring client nurture, and no property manager pipeline — all of which are high-LTV opportunities.

A properly built handyman snapshot solves the three biggest killers of handyman revenue:
1. **Phone tag chaos** — leads who called but never got booked
2. **No follow-up** — completed jobs that never generated a review or repeat booking
3. **No property manager account workflow** — the highest-volume, lowest-cost-to-serve segment they're ignoring

This snapshot is built for general handyman operators: owner-operators doing $200K–$800K/year who take on honey-do lists, punch lists, minor renovations, fixture installs, drywall patches, door/window repairs, weatherstripping, tile repair, trim work, furniture assembly, and caulking. They are **not** licensed electricians or plumbers — but they handle everything in between.

---

## Section 1: Business Pain Points

### 1.1 Low Average Ticket

The average handyman job is $150–$450. Compared to HVAC ($800–$2,500) or roofing ($8,000+), this feels small — but handyman businesses win on **volume and retention**, not ticket size. A single property manager account can be worth $3,000–$8,000/month in recurring work orders.

**Automation opportunity:** Build a recurring client program that brings customers back every 90 days. One automated "honey-do list" reactivation campaign per quarter can generate $1,500–$3,000 in bookings from existing contacts with zero ad spend.

### 1.2 Wide Scope of Work = Hard to Quote

Handymen do everything from a 20-minute caulking job to a 3-day minor renovation. This makes online booking difficult — unlike an HVAC tune-up, there's no fixed price. Most operators handle this with a phone call or on-site assessment before quoting.

**Automation opportunity:** Build a two-track booking flow:
- **Track 1:** Small jobs (honey-do list, punch list items, assembly) → Online booking with flat-rate service menu
- **Track 2:** Larger assessments (drywall repair, tile work, door alignment, trim replacement) → Phone/video quote flow, then convert to booking

### 1.3 No Booking System = Scheduling Chaos

Most handymen run their schedule off text messages and memory. Double-bookings, forgotten jobs, no-shows from clients who didn't get a confirmation — all common. Every missed appointment is a lost $200–$400 job.

**Automation opportunity:** GHL calendar + automated booking confirmation + 24hr and 1hr reminders = nearly zero no-shows.

### 1.4 No Follow-Up = Zero Repeat Business

The average handyman completes a job and moves on. No post-job text, no review request, no "ready for your next project?" follow-up. Meanwhile, Google estimates that 70%+ of home services customers would use the same contractor again — if they remembered them.

**Automation opportunity:** Post-job review request (24hr after completion) + 90-day "honey-do check-in" campaign = compounding repeat business.

### 1.5 No Review Capture = Invisible on Google

Google LSA (Local Services Ads) and Google Maps ranking are dominated by reviews. Most handymen have 5–15 Google reviews. Even 50–100 reviews puts them in the top tier in most mid-size markets.

**Automation opportunity:** Automated 2-touch review request sequence (SMS + email, 24hr and 72hr post-job) = 3–5x more reviews than asking manually.

### 1.6 No Property Manager Pipeline

Property management companies and landlords need handymen constantly — drywall patches between tenants, door alignment after move-out, weatherstripping replacement, tile grout repair, fixture installation. This is high-volume, predictable, recurring work. Most property managers are desperately looking for a reliable handyman they can trust.

**Automation opportunity:** Dedicated property manager outreach workflow with a VIP account intake form, priority booking lane, and monthly invoice summary.

### 1.7 Senior Client Trust Gap

Senior clients (65+) represent a massive segment of handyman work — they need furniture assembly, grab bar installation, weatherstripping, honey-do list completion, and ongoing home maintenance. They are high-LTV but require more trust-building, slower sales, and phone-first communication.

**Automation opportunity:** Senior-specific nurture sequence emphasizing reliability, licensing/insurance proof, and referral encouragement to their community.

---

## Section 2: Existing GHL Handyman Snapshots — What's on the Market

### 2.1 What Exists

As of mid-2026, there are a limited number of dedicated handyman/general contractor snapshots available through:
- **GHL Marketplace (App Marketplace):** A handful of generic "home services" snapshots that cover HVAC, plumbing, roofing — handyman is almost always an afterthought or lumped into a catch-all
- **Third-party SaaS resellers:** Some agencies (Surefire Local, Hatch, etc.) offer home services snapshots but focus on licensed trades
- **Private agency builds:** Most solid handyman setups are built custom by GHL agencies and not publicly available

### 2.2 Common Gaps in Existing Snapshots

Based on what's known about generic home services snapshots, the typical handyman setup is missing:

| Gap | What's Missing |
|-----|----------------|
| Dual booking track | No split between small jobs (book now) vs. larger assessments (quote first) |
| Property manager pipeline | No dedicated PM account workflow |
| Seasonal campaigns | No spring tune-up, fall weatherization, or pre-holiday punch list campaigns |
| Honey-do reactivation | No recurring client reminder system |
| Review capture timing | No optimized 24hr/72hr post-job review sequence |
| Senior client workflow | No trust-building nurture for older demographic |
| Pre-sale punch list track | No workflow for real estate agent/home seller referrals |
| Recurring client program | No "preferred customer" enrollment and loyalty track |
| Industry language | Templates use generic language; don't say "honey-do list," "punch list," "weatherstripping," "drywall patch," etc. |

### 2.3 What Would Make This Snapshot Stand Out

A best-in-class handyman snapshot for 1app must:

1. **Use real handyman language** in every template — prospects should feel like it was written by a guy who actually does the work
2. **Split booking intelligently** — online for simple jobs, phone/assessment track for complex ones
3. **Include a property manager workflow** that no generic snapshot has
4. **Have a seasonal campaign calendar** pre-loaded for spring, fall, and pre-holiday
5. **Include a pre-sale real estate punch list workflow** — one of the highest-LTV referral sources in the vertical
6. **Have a senior client nurture path** that's warm, patient, and builds trust
7. **Have a recurring client program** that maximizes LTV from every completed job

---

## Section 3: Pipeline Architecture

### 3.1 Pipeline Overview

Recommend **3 separate pipelines** inside GHL:

---

#### Pipeline A: New Lead → First Job Pipeline
For all inbound leads regardless of source.

| Stage | Name | Description |
|-------|------|-------------|
| 1 | 🟡 New Lead | Fresh inbound via form, phone, LSA, referral |
| 2 | 📞 Contact Attempted | Speed-to-lead attempted within 5 min |
| 3 | ✅ Contact Made | Spoke to lead — job scoped |
| 4 | 💬 Quote Sent | Estimate texted or emailed |
| 5 | 📅 Job Booked | Calendar confirmed |
| 6 | 🔨 Job In Progress | Day of work |
| 7 | ✔️ Job Completed | Work done — trigger review sequence |
| 8 | ❌ Lost / Not a Fit | Bad scope, out of service area, etc. |

---

#### Pipeline B: Recurring Client Pipeline
For clients who've completed at least one job — lifecycle management.

| Stage | Name | Description |
|-------|------|-------------|
| 1 | 🌱 Completed (Nurture Active) | Post-job, in review + re-engagement nurture |
| 2 | ⭐ Reviewed | Left a Google review — eligible for loyalty perks |
| 3 | 🔄 Reactivation Sent | 90-day honey-do check-in sent |
| 4 | 📅 Repeat Booked | Came back for another job |
| 5 | 🏆 Preferred Client | 3+ jobs — high-value, loyalty track |
| 6 | 💤 Gone Cold | No response to 2+ reactivations |

---

#### Pipeline C: Property Manager / Account Pipeline
For B2B relationships with property managers, landlords, and real estate agents.

| Stage | Name | Description |
|-------|------|-------------|
| 1 | 🏢 PM Prospect | Identified property manager — outreach not started |
| 2 | 📞 Outreach Active | Initial contact made, awaiting response |
| 3 | 🤝 Intro Meeting Booked | Discovery call or walkthrough scheduled |
| 4 | 📋 Trial Work Order | First job sent to test reliability |
| 5 | ✅ Active Account | Recurring work orders flowing |
| 6 | 🏆 VIP Account | High-volume PM, priority booking |
| 7 | ❌ Not a Fit | Budget mismatch, bad fit, or non-responsive |

---

## Section 4: Workflow Architecture

### 4.1 Speed-to-Lead Workflow
**Trigger:** New lead comes in via form, LSA click-to-call, or missed call  
**Goal:** Contact within 5 minutes — research shows 78% of jobs go to the first contractor who responds

```
TRIGGER: Lead Created or Missed Call

Step 1 (Immediate): SMS — "Hi [First Name], this is [Handyman Name] from [Business]. Got your message about [service type]. Quick question — is this a small job (couple hours) or more of a project? I'll shoot you a rough idea of timing and cost. 📲"

Step 2 (5 min if no reply): Voicemail Drop — "Hey [First Name], [Name] here from [Business]. Saw you reached out — just wanted to connect before my schedule fills up. Give me a call back at [number] or just reply to my text. Talk soon."

Step 3 (1 hour if no reply): SMS — "Still have some openings this week. Happy to do a quick call to talk through what you need. No obligation. Just reply 'YES' and I'll call you right now."

Step 4 (24 hours if no reply): Email — Subject: "Your home repair request — still have you saved"
Body: Personal, brief. "Hey, wanted to make sure this didn't slip through the cracks. I know life gets busy. When you're ready to talk through that [honey-do list / repair job], I'm here. No pressure."

Step 5 (72 hours if still no reply): Final SMS — "Last check-in — if timing isn't right, totally understand. Save my number for when you need us. We take care of [service area] homeowners and property managers. 🔨"

BRANCH: If response → Move to "Contact Made" stage → Route to booking
```

---

### 4.2 Booking Confirmation Workflow
**Trigger:** Appointment booked in GHL calendar  
**Goal:** Confirm job details, reduce no-shows, set client expectations

```
TRIGGER: Appointment Booked

Immediate: Booking Confirmation SMS
"✅ Booked! [First Name], you're confirmed with [Handyman Name] on [Date] at [Time]. We'll be handling: [job description]. See you then — and feel free to text this number anytime with questions."

Immediate: Booking Confirmation Email
Subject: "Your appointment is confirmed — here's what to expect"
Body: Full details — date, time, what's included, what to prepare (clear the work area, have materials ready if applicable), who to contact day-of.

24 Hours Before: Reminder SMS
"📅 Reminder: [Handyman Name] is scheduled at your place tomorrow, [Date] at [Time]. Reply 'C' to confirm or call us to reschedule. Looking forward to it!"

1 Hour Before: Final SMS
"🔨 On our way! We're [X] minutes out. If anything came up, just text us. See you soon."
```

---

### 4.3 Post-Job Review Request Workflow
**Trigger:** Job manually marked "Completed" in pipeline  
**Goal:** Capture Google review within 48 hours while the experience is fresh

```
TRIGGER: Pipeline Stage → "Job Completed"

24 Hours After: Review Request SMS
"Hey [First Name]! Hope everything looks great after yesterday. Quick favor — if you have 2 minutes, we'd really appreciate a Google review. It helps us a ton: [Google Review Link] 🙏 — [Handyman Name]"

48 Hours After (if no review): Review Request Email
Subject: "How'd we do? One quick favor..."
Body: More context. "We know there are a lot of options out there for home repairs. If we earned a great review, here's our Google page: [link]. If anything wasn't right, please reply here — we want to make it right."

72 Hours After (if no review): Final SMS
"[First Name], last ask — we'd love your feedback on Google. Even one sentence helps us a lot. [Review Link] Thanks for trusting us with your home. 🏠"
```

---

### 4.4 Honey-Do List Reactivation Workflow
**Trigger:** 90 days after last job completed (recurring automation)  
**Goal:** Generate repeat bookings from existing client base

```
TRIGGER: 90 Days Since Last Job Completed

Day 1: SMS
"Hey [First Name]! [Handyman Name] here. Checking in — it's been a few months. Got any projects piling up? Honey-do list getting longer? 😄 Reply and I'll grab a spot for you this week or next."

Day 3 (if no reply): Email
Subject: "Your home — is it ready for [season]?"
Body: Seasonal angle (see seasonal campaigns below). Friendly, not pushy. Offer to swing by for a walkthrough.

Day 7 (if no reply): SMS
"Quick one — got a small window coming up. If there's anything you've been putting off (caulking, door alignment, a few drywall patches, assembly projects), I can usually knock out a honey-do list in half a day. Interested?"
```

---

### 4.5 Property Manager Outreach Workflow
**Trigger:** Contact tagged as "Property Manager" — manual or form-based  
**Goal:** Land first trial work order and convert to active account

```
TRIGGER: Contact Tagged "Property Manager"

Day 1: Personalized SMS
"Hi [Name], this is [Handyman Name] from [Business]. We work with several property managers in [area] handling turnover punch lists, drywall patches, fixture installs, and general repairs between tenants. Do you have a few minutes this week to connect?"

Day 3 (if no reply): Email
Subject: "Reliable handyman for your properties in [area]"
Body: Position as a solution to their #1 problem — reliable, responsive contractors. Include: response time guarantee, types of work, availability for turnover work, basic rate structure. Keep it professional.

Day 7 (if no reply): SMS
"Following up — even if now isn't the right time, it's worth having a reliable handyman in your contacts. We specialize in turnover repairs, punch lists, and ongoing maintenance. No job too small. Happy to start with one unit as a trial."

Day 14 (if no reply): Final Email
Subject: "One last note from [Business Name]"
Body: Low-pressure final touch. Invite them to reach out when they're ready.

BRANCH: If positive response → Book Intro Meeting → Pipeline C Stage 3
```

---

### 4.6 Pre-Sale Punch List Workflow
**Trigger:** Contact tagged as "Real Estate Agent" or "Seller Referral"  
**Goal:** Convert pre-listing repairs into a completed job + referral relationship

```
TRIGGER: Contact Tagged "Pre-Sale / Realtor Referral"

Immediate: SMS
"Hi [First Name]! Thanks for reaching out about pre-listing work. We specialize in pre-sale punch lists — drywall patches, fresh caulking, door alignment, fixture upgrades, touch-up trim work — the stuff buyers notice. Want to schedule a walkthrough?"

Within 24 Hours: Email
Subject: "Pre-listing prep — here's how we help sellers get top dollar"
Body: Explain the pre-sale punch list process. Typical items: drywall patch and paint touch-up, caulking around tubs/windows, door and window alignment, weatherstripping, fixture swap (light fixtures, cabinet hardware), minor tile repair. Position as a fast turnaround service — "most listings we turn around in 2–3 days."

Post-Job: Realtor Referral Ask SMS
"[Realtor Name], thanks for trusting us with [seller's] place. If you have other listings that need pre-sale work, we'd love to be your go-to. Can I send you a referral card or a simple checklist you can hand to sellers?"
```

---

## Section 5: Lead Sources & Forms

### 5.1 Primary Lead Sources for Handymen

| Source | Volume | Quality | CPL (Est.) | Notes |
|--------|--------|---------|------------|-------|
| Google LSA | High | High | $15–$45 | Best for handyman — pay per lead, not per click |
| Google Maps (organic) | High | Very High | $0 | Review volume is the #1 ranking factor |
| Referrals | Medium | Very High | $0 | Best close rate — needs systemized ask |
| Nextdoor | Medium | High | $0–$20 | Hyperlocal — great for trust |
| Kijiji / Facebook Marketplace | High | Medium-Low | $0 | Volume but lower quality — price shoppers |
| TaskRabbit | Medium | Medium | 15–20% commission | Platform dependency risk |
| Property Managers | Low (outreach) | Very High | Low | $3K–$8K/mo accounts |
| Real Estate Agents | Low (outreach) | High | Low | Pre-sale punch list referrals |
| Senior Community Referrals | Low | Very High | $0 | Extremely loyal, high LTV |
| Facebook/Instagram Ads | Medium | Medium | $20–$60 | Works for seasonal campaigns |

### 5.2 GHL Form Architecture

**Form 1: General Contact / New Lead Form**
Fields: First Name, Last Name, Phone, Email, Service Type (dropdown), Brief Description, Best Time to Contact, How Did You Hear About Us?

Service Type Dropdown Options:
- Honey-do list (multiple small repairs)
- Drywall patch / repair
- Caulking (bath, kitchen, windows, exterior)
- Door repair / alignment
- Window repair / weatherstripping
- Fixture installation (lights, fans, faucets)
- Furniture / shelving assembly
- Tile repair / grout
- Trim and baseboard work
- Minor renovation / other

**Form 2: Property Manager Intake Form**
Fields: First Name, Last Name, Company Name, Phone, Email, # of Units Managed, Types of Repairs Needed Most, Preferred Response Time, Current Handyman (yes/no), What's Your Biggest Frustration With Current Setup?

**Form 3: Pre-Sale Punch List Request**
Fields: First Name, Last Name, Phone, Email, Property Address, Listing Date (target), Realtor Name (if applicable), Known Items Needing Repair (text), Preferred Walkthrough Date

---

## Section 6: SMS/Email Templates

### 6.1 Booking Confirmation Templates

**SMS — Booking Confirmed:**
```
✅ [First Name], you're booked with [Business] on [Date] at [Time]. 
We'll be handling: [Job Description]. 
Text us anytime at this number. See you then! 🔨
```

**SMS — 24hr Reminder:**
```
📅 Reminder: [Handyman Name] is at your place tomorrow at [Time]. 
Reply 'C' to confirm, or call [Phone] to reschedule. 
Looking forward to it!
```

**SMS — Day-Of / En Route:**
```
We're on our way! Should be there around [Time]. 
If anything changed, text us. See you soon. 🔨
```

---

### 6.2 Post-Job Review Templates

**SMS — 24hr Post-Job:**
```
Hey [First Name]! Hope everything looks great. 
Quick favor — 2-minute Google review would mean a lot: 
[Google Review Link] 🙏 
Thanks for trusting us! — [Name]
```

**Email — Subject:** "How'd we do? One quick ask..."
```
Hi [First Name],

Thanks again for having us out [yesterday/this week]. Hoped we left things looking clean and solid.

If you have 2 minutes, a Google review helps us a ton — especially for finding more homeowners like you in [area].

👉 Leave a review here: [Google Review Link]

If anything wasn't right, just reply to this email and I'll make it right.

Thanks,
[Handyman Name]
[Business Name]
[Phone]
```

---

### 6.3 Honey-Do List Reactivation Templates

**Spring Honey-Do Campaign SMS:**
```
Hey [First Name]! 🌱 Spring is here and the honey-do list is probably growing. 
Got openings in [Month] for: caulking, weatherstripping, drywall patches, 
door alignment, fixture swaps, and more. 
Want to knock out the list? Text me back!
```

**Fall Weatherization Campaign SMS:**
```
Hey [First Name]! 🍂 Quick heads-up — fall is the best time to tackle 
weatherstripping, door seals, window caulking, and any exterior punch list 
items before winter hits. 
Got a few slots open. Interested?
```

**Pre-Holiday Punch List Campaign SMS:**
```
Hey [First Name]! 🏠 Getting ready for the holidays? 
We're booking pre-holiday punch lists now — shelf installs, 
furniture assembly, fixture swaps, door alignment, touch-up caulking. 
Want to get the house looking sharp before the family arrives?
```

**General Reactivation SMS (Evergreen):**
```
Hey [First Name]! [Handyman Name] here — it's been a while. 
Got a growing punch list? 
We do everything from drywall patches to furniture assembly to door alignment. 
Usually can fit small jobs in within a week. Want to book?
```

---

### 6.4 Property Manager Templates

**Initial Outreach SMS:**
```
Hi [Name], this is [Handyman Name] from [Business]. 
We handle turnover punch lists, drywall repairs, fixture installs, 
and ongoing maintenance for property managers in [area]. 
Have a quick 10 minutes to connect this week?
```

**PM Welcome Email — New Account:**
```
Subject: Welcome to [Business Name] — here's how our PM accounts work

Hi [Name],

Thanks for giving us a shot. Here's how we work for property manager accounts:

📋 Work Requests: Just text or email us the address and a description.
⚡ Response: We'll confirm availability within 2 hours.
🔧 Common Jobs: Drywall patches, door alignment, weatherstripping, 
   fixture installs, caulking, tile grout, trim work, lock hardware.
📅 Turnaround: Most turnover jobs completed within 48–72 hours of booking.
🧾 Invoicing: We invoice weekly for completed jobs.

Looking forward to making your life easier.

[Handyman Name]
[Business Name | Phone]
```

---

## Section 7: Booking Flow Design

### 7.1 Dual-Track Booking System

The key insight for handyman booking: **not every job can be booked online with a fixed price.** Build two tracks:

---

**Track 1 — Small Job / Flat Rate (Online Booking)**

Eligible jobs: Honey-do list, caulking, weatherstripping, furniture assembly, basic fixture swap, door adjustment, minor drywall patch (under 6")

Flow:
1. Lead visits booking page
2. Selects service type from menu
3. Sees flat-rate pricing (or hourly rate minimum)
4. Books time slot directly from GHL calendar
5. Receives auto-confirmation + reminders

GHL Setup: Standard appointment booking calendar with service menu categories and pricing displayed.

---

**Track 2 — Quote Required (Assessment Flow)**

Eligible jobs: Larger drywall repairs, tile work, window replacement, door frame repair, trim installation, minor renovation

Flow:
1. Lead visits booking page or contacts by phone/form
2. Selects "Get a Free Quote" option
3. Fills out job description form (or calls)
4. Receives callback to scope job within 2 hours (business hours)
5. Quote sent via SMS/email
6. If accepted → books job via standard calendar

GHL Setup: Separate "Quote Request" calendar type + quote-to-booking pipeline stage.

---

### 7.2 Calendar Setup Recommendations

| Calendar | Type | Duration | Purpose |
|----------|------|----------|---------|
| Honey-Do List Appointment | Appointment | 2–4 hrs | Small multi-task jobs |
| Single Job Booking | Appointment | 1–2 hrs | Focused single repair |
| On-Site Assessment | Appointment | 30 min | Free quote for larger jobs |
| Property Manager Work Order | Appointment | Flexible | PM-assigned jobs |
| Senior Home Visit | Appointment | 2–3 hrs | Senior client focused |

---

## Section 8: Recurring Client Program

### 8.1 The Handyman LTV Problem

Low-ticket services feel transactional. A handyman who completes a $250 honey-do list and never follows up leaves $2,000+ in annual repeat business on the table. The average homeowner has 6–12 handyman-type jobs per year. They just need someone to remind them.

### 8.2 Preferred Client Program Structure

**Enrollment Trigger:** 2nd completed job OR manual tag "Preferred Client"

**Program Benefits (communicated in enrollment message):**
- Priority booking (preferred client slots available before general public)
- Seasonal check-in reminders (spring, fall, pre-holiday)
- Preferred response time: 24-hour callback guarantee
- Annual home walkthrough offer (spring or fall — identify issues before they become expensive)

**Enrollment SMS:**
```
[First Name], you're now a Preferred Client with [Business]! 🏠
That means priority booking, seasonal reminders, and faster response times.
We'll reach out each season with a check-in — or you can always text us directly.
Thanks for trusting us with your home!
```

**Annual Home Walkthrough Offer SMS (April):**
```
Hey [First Name]! 🌿 Spring is a great time for a quick home walkthrough. 
We'll check caulking, weatherstripping, door alignment, and flag anything 
that should be on your summer punch list. 
Usually about 30 minutes — totally free for Preferred Clients. 
Want to grab a slot?
```

### 8.3 LTV Projection

| Scenario | Jobs/Year | Avg Ticket | Annual LTV |
|----------|-----------|-----------|------------|
| One-time client, no follow-up | 1 | $300 | $300 |
| Reactivation campaign (no program) | 2–3 | $300 | $600–$900 |
| Preferred Client Program active | 4–6 | $320 | $1,280–$1,920 |
| Property Manager Account | 20–40 | $250 | $5,000–$10,000 |

---

## Section 9: Property Manager Account Workflow (Full Detail)

### 9.1 Why Property Managers Are the Goldmine

- They have predictable, recurring needs (turnover repairs, ongoing maintenance)
- They don't price-shop as aggressively as individual homeowners
- Once you're trusted, they send work automatically — no marketing cost
- One PM managing 50 units = 100+ work orders per year at your shop

### 9.2 PM Identification & Outreach

**Sources to identify PMs:**
- Google "property management [your city]"
- Kijiji/Craigslist rental listings — look for multi-property posters
- LinkedIn — search "property manager [city]"
- Local real estate investment groups (Facebook, BiggerPockets)
- Chamber of Commerce member lists

**GHL Outreach Sequence:** (See Section 4.5 above)

### 9.3 PM Account Management Workflow

Once a PM is active:
1. Dedicated "PM Work Order" tag in GHL contact
2. Work orders created as appointments with property address, unit number, issue description
3. Status updates via SMS at job start and completion
4. Weekly invoice summary email (can integrate with invoicing tool)
5. Monthly check-in call/text: "Any upcoming turnovers or repairs in the next 2–4 weeks?"

**Monthly PM Check-In SMS:**
```
Hey [Name]! [Handyman Name] here — heading into [Month]. 
Any turnovers or repairs coming up at your properties? 
Happy to get them on the schedule now. 🔧
```

**Post-Work-Order Completion SMS to PM:**
```
✅ Done at [Property Address], Unit [X]. 
Work completed: [brief description]. 
Let me know if you need anything else or want photos sent over.
```

### 9.4 PM Referral Expansion

Active PM accounts are the best source of additional PM referrals. Build a simple referral ask into the 3-month anniversary of the PM relationship:

**PM Referral Ask SMS:**
```
[Name], we've been working together for a few months now and it's been great. 
If you know any other property managers who need a reliable handyman, 
I'd love the introduction. Happy to return the favor however I can. 🤝
```

---

## Section 10: Seasonal Campaign Calendar

### 10.1 Campaign Calendar Overview

| Month | Campaign | Target | Message Theme |
|-------|----------|--------|---------------|
| February | Pre-Spring Advance Booking | All clients | "Book your spring punch list before the rush" |
| April | Spring Tune-Up | All clients | "Winter damage, honey-do backlog, exterior caulking" |
| August | Pre-Fall Prep | Preferred Clients + PM accounts | "Before leaves fall — weatherstripping, door seals, exterior" |
| October | Fall Weatherization | All clients | "Seal up before winter — weatherstripping, caulking, drafts" |
| November | Pre-Holiday Punch List | All clients | "Get the house ready before family arrives" |
| January | New Year Refresh | Reactivation (cold leads) | "Fresh year, fresh house — knock out the list" |

---

### 10.2 Campaign Templates

**February — Advance Spring Booking:**
```
SMS: "Hey [First Name]! Spring fills up fast. 
If you've got a punch list building — drywall patches, 
door alignment, exterior caulking, fixture swaps — 
book now before April slots fill up. 
Want to grab a spot? 📋"

Email Subject: "Beat the spring rush — book your punch list now"
```

**April — Spring Tune-Up:**
```
SMS: "🌱 Spring is here — perfect time to tackle that honey-do list! 
Caulking around tubs and windows, door/window alignment, 
weatherstripping refresh, drywall touch-ups. 
Got openings this week. Interested?"

Email Subject: "Spring home tune-up checklist — we handle all of it"
Body: List of 8–10 common spring repairs. CTA to book.
```

**October — Fall Weatherization:**
```
SMS: "🍂 Fall weatherization time! 
Drafty doors? Windows leaking air? 
We do weatherstripping, door seals, window caulking, 
and anything else on your fall punch list. 
Book before the cold hits — slots going fast."

Email Subject: "Is your home winter-ready? We'll make sure it is."
Body: Weatherization checklist (weatherstripping, caulking, door adjustments, 
insulation, etc.) CTA: free walkthrough offer.
```

**November — Pre-Holiday Punch List:**
```
SMS: "🏠 Holiday prep time! 
Before family arrives — shelf installs, furniture assembly, 
fixture upgrades, door alignment, touch-up caulking. 
We can usually knock out a full punch list in a day. 
Want to get it done?"

Email Subject: "Get the house holiday-ready — we'll handle the punch list"
```

---

## Section 11: Senior Client Workflow

### 11.1 Senior Client Characteristics

- Higher LTV than average (loyal, pay promptly, refer neighbors)
- Need more reassurance before booking — phone call preferred over text booking
- Value reliability and punctuality above price
- Common jobs: grab bar installation, door hardware, weatherstripping, furniture assembly, caulking, light fixture swaps, shelving installation
- Often referred through senior communities, faith communities, family members

### 11.2 Senior-Specific Workflow

**Initial Contact — Phone-First Approach:**
- All senior leads should get a direct phone call within 2 hours (not just a text)
- Voicemail if no answer: warm, slow, clear — not fast-talking or jargon-heavy

**Senior Client Welcome SMS (post-booking, after phone confirmation):**
```
Hi [First Name], this is [Handyman Name] from [Business]. 
Just confirming your appointment for [Date] at [Time]. 
We're fully insured and background checked. 
Feel free to call me directly at [number] if you have any questions. 
Looking forward to meeting you!
```

**Senior Client Nurture Sequence:**
- 90-day check-in: Gentle text or card (physical postcard for highest-LTV seniors)
- Annual safety walkthrough offer: "We do a free home safety check for long-term clients — grab bars, handrails, door hardware, lighting"

**Trust-Building Email Template:**
```
Subject: A few things you should know about us before we meet

Hi [First Name],

I wanted to send a quick note before our appointment [Date].

A few things that might put your mind at ease:
✅ We're fully licensed and insured in [Province/State]
✅ Background-checked — I can provide documentation on request
✅ We've served [X] homeowners in [area] since [year]
✅ If you have any concerns during or after the job, just call me directly: [number]

We'll arrive at [Time]. Please don't feel like you need to prepare anything — just let us in and show us what needs to be done.

Looking forward to helping out,
[Handyman Name]
[Business Name]
```

### 11.3 Senior Referral Network

Seniors are the most powerful referral source in the handyman vertical — they refer neighbors, friends from church, and family members. Build a referral ask into the relationship:

**Senior Referral Ask (30 days post-job):**
```
Hi [First Name]! Hope everything is still holding up perfectly. 
If any of your neighbors or friends ever need a reliable handyman, 
please pass along our number. 
We always take good care of folks you send our way. 😊
— [Handyman Name]
```

---

## Section 12: Snapshot Standout Features Summary

### 12.1 What Makes This Build Different

| Feature | Generic Snapshot | 1app Handyman Snapshot |
|---------|-----------------|----------------------|
| Industry language | Generic ("home services") | Real handyman language throughout — punch list, honey-do, drywall patch, weatherstripping, fixture install, door alignment |
| Booking track | Single flow | Dual-track: online for small jobs, phone/assessment for larger work |
| Property manager pipeline | Missing | Full PM outreach → trial → VIP account workflow |
| Seasonal campaigns | Maybe 1 generic | 6 seasonal campaigns pre-loaded (Feb, Apr, Aug, Oct, Nov, Jan) |
| Senior client workflow | Missing | Dedicated phone-first nurture + trust-building sequence |
| Pre-sale punch list | Missing | Real estate agent / seller referral workflow |
| Recurring client program | Missing | Preferred Client enrollment with LTV-building sequences |
| Review capture timing | Generic (immediate) | Optimized 24hr/72hr post-job sequence with 2-touch approach |
| PM check-in | Missing | Monthly auto check-in to active PM accounts |
| LTV architecture | Single pipeline | 3 pipelines: New Lead, Recurring Client, Property Manager |
| Referral system | Missing | 3 referral workflows: post-job, senior community, PM expansion |

### 12.2 Feature Checklist for Build

**Core GHL Components:**
- [ ] 3 pipelines (New Lead, Recurring Client, Property Manager)
- [ ] 5 calendars (Honey-do, Single Job, Assessment/Quote, PM Work Order, Senior)
- [ ] 3 intake forms (General, PM Intake, Pre-Sale Punch List)
- [ ] Speed-to-lead workflow (5 min, 1 hr, 24 hr, 72 hr)
- [ ] Booking confirmation workflow (immediate, 24hr, 1hr pre)
- [ ] Post-job review workflow (24hr, 48hr, 72hr)
- [ ] Honey-do reactivation workflow (90-day trigger)
- [ ] Property manager outreach workflow
- [ ] Pre-sale punch list workflow
- [ ] Senior client workflow (phone-first variant)
- [ ] Preferred Client enrollment workflow
- [ ] 6 seasonal campaign sequences (pre-built, manually triggered)
- [ ] Monthly PM check-in automation
- [ ] 3 referral request sequences

**Tags to Build:**
- New Lead | Quote Requested | Active Client | Preferred Client
- Property Manager | VIP Property Manager | Real Estate Agent
- Senior Client | Referral Source | Pre-Sale Seller
- Spring Campaign Enrolled | Fall Campaign Enrolled
- Reactivation Active | Gone Cold | Do Not Contact

**Custom Fields:**
- Job Type (dropdown)
- Property Address (text)
- Unit Number (text — for PM work orders)
- Estimated Job Duration (dropdown: 1hr / Half Day / Full Day / Multi-Day)
- Preferred Contact Method (Phone / Text / Email)
- Number of Properties Managed (PM only)
- Last Job Date (date — for reactivation trigger)
- Review Left (yes/no — for review workflow exit)
- Preferred Client (yes/no)

---

## Section 13: Competitive Positioning for 1app Sales

### 13.1 Sales Pitch for Handyman Clients

**Pain → Solution Framework:**

*"You're probably answering your phone between jobs, losing leads when you don't pick up, and doing all your follow-up from memory. We set up a system that responds to new leads in under 5 minutes, sends appointment reminders automatically, follows up after every job for a Google review, and re-engages past clients every 90 days. Most handymen we work with see 20–40% more bookings from their existing contact list within 60 days — without spending a dollar on ads."*

### 13.2 Objection Handling

**"I'm too busy to learn a new system"**
→ "That's exactly why we build it for you. You don't touch anything. We set it up, you approve the messages, and it runs. Your only job is showing up to jobs — we handle everything else."

**"I get all my work from referrals"**
→ "Referral businesses are the best kind — and this makes your referral system 10x more powerful. You'll have automated follow-ups that ask every happy client to send you a referral. Right now you're probably only asking when you remember."

**"I already have too many leads"**
→ "Then this is about making sure none of them fall through the cracks. How many leads did you lose last month because you couldn't answer the phone? Even one missed $500 job per week is $26,000/year."

### 13.3 Demo Scenario for Sales Calls

Walk through:
1. A new lead comes in from Google LSA → automatic 5-minute text response
2. Lead books a honey-do list appointment → confirmation + reminders
3. Job completes → Google review request auto-sent
4. 90 days later → reactivation text triggers

Total talking time: 10 minutes. Show the automation doing the work.

---

## Appendix A: GHL Snapshot Build Order (Recommended)

For efficient snapshot construction, build in this order:

1. **Custom Fields** — foundation for all forms and workflows
2. **Tags** — needed before workflows reference them
3. **Calendars** (5 total)
4. **Pipelines** (3 total) with stages
5. **Forms** (3 total) linked to calendars and pipelines
6. **Email Templates** (store in GHL templates library)
7. **SMS Templates** (store in GHL templates library)
8. **Workflows** — in dependency order:
   - Speed-to-Lead (no dependencies)
   - Booking Confirmation (needs calendar)
   - Post-Job Review (needs pipeline stage trigger)
   - Honey-Do Reactivation (needs date field + pipeline)
   - PM Outreach (needs tags)
   - Pre-Sale Workflow (needs tags)
   - Senior Client Variant (needs tags)
   - Preferred Client Enrollment (needs pipeline)
   - Seasonal Campaigns (manual trigger — build last)
9. **Reporting Dashboard** — track bookings, pipeline conversion, review volume

---

## Appendix B: Industry Language Glossary

Use these terms naturally in all client-facing templates — do not use generic language.

| Term | Definition | Use In |
|------|-----------|--------|
| **Honey-do list** | Homeowner's accumulated list of small repairs | Reactivation campaigns, booking page |
| **Punch list** | Final repair list before project completion / pre-sale repair list | Pre-sale workflow, PM workflow |
| **Drywall patch** | Repair of holes or damage in drywall | Service menu, intake form |
| **Caulking** | Sealing gaps around tubs, windows, doors, exterior | Seasonal campaigns, service menu |
| **Weatherstripping** | Seals around door and window frames to prevent drafts | Fall campaign, PM workflow |
| **Fixture install** | Installing light fixtures, ceiling fans, faucets, hardware | Service menu, booking page |
| **Door alignment** | Adjusting doors that stick, won't latch, or have gaps | Service menu, seasonal |
| **Trim work / baseboard** | Installing or repairing interior trim and baseboards | Service menu |
| **Tile repair / grout** | Replacing cracked tile or re-grouting | Service menu, PM workflow |
| **Assembly** | Furniture, shelving, equipment assembly | Service menu |
| **Turnover repairs** | Work done between tenants in a rental property | PM workflow |
| **Work order** | A single job request from a property manager | PM account workflow |
| **Pre-sale prep** | Repairs done before listing a home for sale | Pre-sale workflow |
| **Walkthrough** | On-site visit to assess job scope or conduct safety check | Assessment track, senior workflow |
| **Grab bar** | Safety bar installed for seniors/accessibility | Senior workflow |

---

*Document prepared by Maximus for 1app agency — internal use only.*  
*Last updated: July 2026*
