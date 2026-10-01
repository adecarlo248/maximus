# Fencing Company GHL Snapshot — Agency Build Research Document
**Prepared for:** 1app Technologies Inc.
**Purpose:** Comprehensive research and build specification for a fencing industry GoHighLevel snapshot
**Version:** 1.0
**Date:** July 2026

---

## Executive Summary

The fencing industry is a high-ticket, relationship-driven trade with strong seasonal demand and a long quote-to-close cycle. Fencing contractors — whether residential privacy fence installers, commercial chain link specialists, or farm/agricultural fence operators — share a common pain: they are excellent at putting posts in the ground and terrible at following up.

The gap in the market is not awareness. It is **speed-to-lead**, **structured follow-up**, and **referral capture** — specifically the neighbour campaign opportunity, which no existing snapshot leverages properly.

This document outlines the complete build specification for a best-in-class GHL fencing snapshot that 1app can sell, onboard, and support as a recurring SaaS product.

---

## Section 1: Industry Pain Points

### 1.1 Operational Pain Points

**Seasonal Demand Spikes**
- Fencing is intensely seasonal: 70–80% of residential installs happen April–October in Canadian and northern U.S. markets.
- Contractors go from zero to overwhelmed in 2–3 weeks in spring, then scramble again before the ground freezes in October/November.
- During peak season, quote requests pile up and follow-up collapses — contractors are in the field all day and have no system to manage leads coming in.
- Pain: No automated system = lost leads at the exact moment demand is highest.

**Long Quote-to-Close Cycle**
- The typical residential fencing project moves: inquiry → site measure → quote → homeowner deliberation → close. This cycle averages 7–21 days.
- Most fence companies send one quote and never follow up. Industry data suggests 80%+ of sales go to the company that follows up consistently.
- Multi-quote shoppers (homeowners getting 3+ quotes) are the norm — **whoever follows up best usually wins**, not whoever is cheapest.

**Permit Requirements**
- Most municipalities require a permit for fence installation above a certain height (typically 6ft or any fence on a property line).
- Homeowners often don't know permits are required. When they find out, the project stalls.
- Contractors have to track permit status for active projects — manual tracking is error-prone.
- Pain: No permit status communication workflow = homeowners go cold, feel like nothing is happening.

**Property Surveys**
- Many homeowners don't have a current property survey, which is required to identify property lines before installation.
- This creates delays: contractor books the job, then discovers no survey exists, has to pause while homeowner orders one.
- Pain: No pre-install checklist communication = surprise delays that destroy customer experience.

**Multi-Quote Shoppers**
- The fencing market is highly commoditized. Homeowners regularly get 3–5 quotes.
- The decision often comes down to trust and perceived professionalism, not price.
- Pain: A poorly followed-up quote loses to a slightly more expensive competitor who sends one text.

**No Follow-Up Culture**
- Most fencing companies are owner-operated or small crews. The owner is measuring fence lines, not sending follow-up texts.
- There is no admin staff, no CRM, and no system — just a pile of paper quotes and a vague intention to call back.
- Pain: This is the single biggest revenue leak in the fencing industry.

**Weather Delays**
- Rain, frost, frozen ground, and high winds all cause installation delays.
- Homeowners don't understand why their fence isn't getting installed. They feel ignored.
- Pain: No proactive communication workflow = service calls, bad reviews, cancellations.

**Referral Leakage**
- Fencing is one of the most visual trades — neighbours literally see the work being done.
- Yet most contractors have zero system to capture neighbours as leads at install time.
- Pain: The neighbour campaign is untapped gold and almost nobody has a GHL workflow for it.

### 1.2 Business Development Pain Points

- No consistent lead generation beyond word-of-mouth and Kijiji/Facebook Marketplace
- Zero review generation strategy
- No commercial fencing pipeline (property managers, construction sites, schools, municipalities)
- No off-season communication to keep past customers engaged
- No cross-sell into related services (gate openers, repairs, retaining walls)

---

## Section 2: Market Scan — Existing GHL Fencing Snapshots

### 2.1 What Exists

As of mid-2026, the GHL snapshot marketplace (both official HL Marketplace and third-party sites like SnapShotsByPros, SaaSPreneurs, and various agency offer libraries) has **limited dedicated fencing snapshots**. The few that exist tend to be:

- **Generic home services snapshots** rebranded with fencing terminology
- **Single-workflow speed-to-lead** funnels with no pipeline depth
- **Basic review generation** bolt-ons with no fencing-specific context

Key observed deficiencies in existing snapshots:
1. No permit tracking workflow
2. No neighbour campaign (the biggest missed opportunity in the space)
3. No seasonal urgency campaign logic (spring push + fall close)
4. No commercial fencing pipeline separation
5. No farm/agricultural fencing sub-pipeline
6. No pre-install checklist communication
7. No weather delay communication workflow
8. Generic SMS/email templates with no fencing industry vocabulary
9. No referral source tracking (LSA vs. Kijiji vs. neighbour vs. real estate agent)
10. No post-install cross-sell sequence (annual maintenance, gate repair, additional sections)

### 2.2 The Opportunity

A properly built fencing snapshot that addresses all of the above becomes the **default choice** in the space because:
- Competition is thin and what exists is weak
- Fencing contractors are increasingly tech-curious (younger owners, fleet vehicles with tablets)
- The ticket size ($3,000–$25,000+ per project) justifies a $197–$597/month SaaS fee
- Seasonality creates urgency selling windows twice a year

---

## Section 3: Pipeline Architecture

### 3.1 Primary Pipeline — Residential Fencing

**Stages:**

| Stage | Name | Description |
|-------|------|-------------|
| 1 | New Inquiry | Lead form, phone call, Kijiji DM, referral — unqualified |
| 2 | Site Measure Scheduled | Appointment booked for on-site estimate |
| 3 | Site Measure Complete | Estimator has been on site, measuring done |
| 4 | Quote Sent | Written quote delivered (email + SMS link) |
| 5 | Quote Follow-Up | Active follow-up sequence running (Days 1, 3, 7) |
| 6 | Verbal Yes | Homeowner said yes but hasn't signed/deposited yet |
| 7 | Deposit Received | Project confirmed — awaiting permit/materials/scheduling |
| 8 | Permit Applied | Permit application submitted |
| 9 | Permit Approved | Ready to schedule install |
| 10 | Install Scheduled | Date confirmed with homeowner |
| 11 | Install Complete | Fence installed — review + referral capture |
| 12 | Closed Won | Full payment received |
| 13 | Closed Lost | Lost — capture reason (price, competitor, timing, no response) |
| 14 | Nurture (Future) | Not ready now — 90-day re-engagement scheduled |

### 3.2 Secondary Pipeline — Commercial Fencing

**Stages:**

| Stage | Name | Description |
|-------|------|-------------|
| 1 | Commercial Lead | Property manager, GC, school board, municipality |
| 2 | Site Assessment | Commercial site walk-through |
| 3 | Spec Quote Prepared | Detailed spec quote with materials breakdown |
| 4 | Proposal Sent | Formal proposal delivered |
| 5 | Decision In Progress | Multiple stakeholders reviewing |
| 6 | Contract Signed | Project confirmed |
| 7 | Mobilization | Materials ordered, crew scheduled |
| 8 | In Progress | Installation underway (multi-day/multi-phase) |
| 9 | Complete + Invoiced | Punch list complete, final invoice sent |
| 10 | Closed Won | Payment received |
| 11 | Closed Lost | Lost (track: price, timeline, spec mismatch) |

### 3.3 Tertiary Pipeline — Repairs & Service

**Stages:**

| Stage | Name | Description |
|-------|------|-------------|
| 1 | Service Request | Repair inquiry (storm damage, rot, bent gate, broken post) |
| 2 | Assessment Scheduled | Quick on-site or photo assessment |
| 3 | Repair Quote Sent | Small job quote ($150–$800 typical) |
| 4 | Repair Approved | Homeowner green-lit |
| 5 | Repair Scheduled | Date set |
| 6 | Complete + Invoice | Work done, payment collected |
| 7 | Upsell Offered | Full replacement quoted if repair not cost-effective |

### 3.4 Sub-Pipeline — Farm & Agricultural Fencing

**Stages:**

| Stage | Name | Description |
|-------|------|-------------|
| 1 | Farm Lead | Acreage, pasture, horse paddock, perimeter |
| 2 | Property Walk | Large-scale site assessment (bring GPS, measure by footage) |
| 3 | Material Spec | Post type (wood, metal T-post, split rail), wire gauge, gates |
| 4 | Quote Sent | Typically quoted per linear foot with gate add-ons |
| 5 | Negotiating | Farm owners often negotiate — track concessions |
| 6 | Deposit Received | Project confirmed |
| 7 | Materials Ordered | Post, wire, concrete, gates |
| 8 | Installation Phases | Multi-phase tracking (perimeter first, internal dividers second) |
| 9 | Complete | Sign-off and final payment |

---

## Section 4: Workflow Architecture

### 4.1 Speed-to-Lead Workflow
**Trigger:** New lead form submission, missed call, or inbound SMS
**Goal:** Respond within 5 minutes

```
Trigger: Lead submitted
↓
Step 1: Immediate SMS (0 min)
"Hey [First Name]! Thanks for reaching out about your fencing project. 
I'll personally give you a call in the next few minutes to learn more 
about what you're looking for. — [Owner Name], [Company]"

↓
Step 2: Internal notification to owner/dispatcher (0 min)
"New fence lead: [First Name] [Last Name] | [Phone] | [Source] | [Service Type]"

↓
Step 3: Missed call text (if call not answered within 15 min)
"Tried reaching you — no worries! Click here to book your FREE on-site 
estimate: [Booking Link] 🏗️"

↓
Step 4: Email (1 hour if no response)
Subject: "Your free fence estimate — [Company Name]"
Body: Introduction + trust elements + booking link + photo gallery link

↓
Step 5: If no booking after 24 hours → Move to "Re-engage" sub-workflow
```

### 4.2 Free Estimate Confirmation Workflow
**Trigger:** Appointment booked via calendar

```
Step 1: Immediate confirmation SMS
"Your free fence estimate is confirmed! 📋
📅 [Date]
🕐 [Time]  
📍 We'll come to you — please have your property survey handy if you have one.
Questions? Reply to this message anytime."

Step 2: Confirmation email (includes what to expect, prep checklist)

Step 3: 24-hour reminder SMS
"Quick reminder — your fence estimate with [Company] is tomorrow at [Time].
We'll be measuring the area and discussing your options for:
✅ Privacy fence | Chain link | Split rail | Ornamental | Farm fencing

If you need to reschedule: [Link]"

Step 4: 2-hour reminder SMS
"On our way! Your fence estimate is in 2 hours at [Time].
One quick tip: know which sides of the property you want fenced — 
it speeds up the site measure. See you soon! 🏡"
```

### 4.3 Quote Follow-Up Workflow
**Trigger:** Deal stage moved to "Quote Sent"
**Duration:** 21-day sequence

```
Day 1 (same day as quote):
SMS: "Hey [First Name] — just sent over your fence quote! Total: $[Amount]
It includes [X linear feet] of [fence type] with [gate count] gate(s).
Any questions? Just reply here. Happy to walk you through it."

Day 3:
SMS: "Hi [First Name] — checking in on your fence quote. 
Have you had a chance to review it? 
A couple things homeowners usually ask about:
✅ Post depth (we do 4' minimum)
✅ Concrete footing on every post
✅ Permit included in quote
Let me know if you want to chat!"

Day 7:
SMS: "Hey [First Name] — I know life gets busy. 
Just want to make sure your fence quote isn't buried in your inbox.
We're booking [3-4 weeks] out right now — spots fill up fast in [month].
Worth a quick call? [Phone number]"

Email (Day 7):
Subject: "A few things to know before choosing your fence company"
Body: Educational content about what to look for (post depth, concrete footings, 
warranty, permit handling, linear foot pricing breakdown, material quality comparison)
+ soft CTA to book or reply

Day 14:
SMS: "Hi [First Name] — still happy to get your fence in the ground this season.
If price is a concern, we have some options worth discussing.
Reply YES and I'll call you today."

Day 21:
SMS: "Hey [First Name] — reaching out one last time on your fence quote.
If the timing isn't right, no worries at all — I'll check back in the spring.
If you're still considering it, I'd love to chat. [Phone]"

→ If no response after Day 21: Move to "Future Nurture" — 90-day sequence
```

### 4.4 Permit Tracking Workflow
**Trigger:** Deal stage moved to "Permit Applied"

```
Immediately:
SMS: "Great news, [First Name] — your fence permit has been applied for! 🏗️
Typical processing time in your area: 5–15 business days.
We'll keep you updated every step of the way."

Day 5:
SMS: "Permit update for [First Name]: Still in processing — no action needed from you.
We're monitoring it daily and will notify you the moment it's approved!"

Day 10 (if still pending):
SMS: "Quick update — permit is still being processed.
If there's any delay beyond 15 business days, we'll follow up with the municipality directly.
You're in good hands! 🏡"

On Approval (trigger: stage moved to "Permit Approved"):
SMS: "🎉 Your permit is APPROVED, [First Name]!
We're now scheduling your install. Expect a call from us within 24 hours to confirm your date."
Email: Full project summary + what happens next + weather policy
```

### 4.5 Pre-Install Checklist Workflow
**Trigger:** Deal stage moved to "Install Scheduled"

```
7 days before install:
SMS: "Your fence install is confirmed for [Date]! 📋
A few things to prepare:
✅ Mark any underground utilities (call 811/Ontario One Call)
✅ Clear the fence line of garden beds, debris, plants
✅ Ensure vehicle access to backyard if applicable
✅ Keep pets indoors on install day
Reply with any questions!"

48 hours before install:
SMS: "Your fence goes in the day after tomorrow! 🏗️
Crew arrives between [Time window].
One reminder: if it rains heavily tonight, we may need to adjust timing — 
we'll text you by 7 AM if anything changes."

Morning of install (7 AM):
SMS: "Good morning [First Name]! Your crew is heading your way today.
ETA: [Time window].
Crew lead: [Name] | [Phone]
Excited to get your new fence in the ground! 🏡"
```

### 4.6 Post-Install Review Workflow
**Trigger:** Deal stage moved to "Install Complete"

```
Day 1 (day of completion):
SMS: "Your fence is in! 🎉 Hope you love it, [First Name].
We'd really appreciate a quick Google review — it takes 2 minutes and 
means the world to a small local business:
[Google Review Link]
Thanks so much! — [Owner Name]"

Day 3 (if no review):
SMS: "Hey [First Name] — enjoying the new fence?
If you have a moment, your review on Google helps other homeowners find us:
[Google Review Link] ⭐⭐⭐⭐⭐"

Day 7 (if no review):
Email: 
Subject: "How did we do on your fence project?"
Body: Personalized note from owner + Google review link + ask for referral

Day 14:
SMS: "Hey [First Name] — any neighbours asking about your new fence?
We'd love to give you a $[50–100] referral credit for anyone you send our way.
Just have them mention your name when they call! 🏡"
```

### 4.7 Neighbour Campaign Workflow
**Trigger:** Deal stage moved to "Install Complete" (parallel to review workflow)
**This is the signature workflow — biggest differentiator**

```
Concept:
When a fence goes in, 3–6 immediate neighbours can see it.
We capture those neighbours via door-knock card OR automated radius text 
(if using a tool like Hatch/Angi local data) AND by asking the homeowner directly.

Homeowner SMS (Day 1 of install):
"Hey [First Name] — while we're here today, would you mind if we left a 
few door hangers for your neighbours? Lots of folks see the work and get curious! 
We'd love to connect with them."

Neighbour Door Hanger Text (leave at 3 properties):
---
"Your neighbour at [Street] just had their fence installed by [Company Name].
We'd love to give you the same quality at a special neighbour rate.
Free estimate: [Phone] | [Booking Link]
Ask for [Owner Name] — mention '[Street Neighbour]' for priority scheduling."
---

If homeowner provides a neighbour's number:
→ Auto-SMS to neighbour:
"Hi! I'm [Owner Name] from [Company]. Your neighbour [First Name] at [Street] 
suggested I reach out — we just finished their fence and they thought you might 
be interested in a free estimate for yours.
When would be a good time to chat? 😊"
```

### 4.8 Seasonal Campaign Workflows

**Spring Launch Campaign (March 15 – April 15)**
*Sent to: All past customers + opt-in list*

```
SMS 1 (March 15):
"Spring is almost here, [First Name]! ☀️
Fence season is just around the corner and our calendar fills up FAST.
If you've been thinking about a new fence, now is the time to lock in your spot.
Free estimate: [Booking Link] | [Phone]"

SMS 2 (April 1 — if no booking):
"Hey [First Name] — just a reminder that we're already booking into [May/June].
Don't get pushed to the fall! 
Reply YES and I'll have someone call you today to book your free estimate."

Email (April 1):
Subject: "Spring Fence Season Is Here — Don't Get Left Out"
Body: Photos of recent installs, seasonal urgency, booking CTA, testimonials
```

**Fall Urgency Campaign (September 1 – October 15)**
*Sent to: All quote-sent leads from spring/summer who didn't close*

```
SMS 1 (September 1):
"Hey [First Name] — the ground is still workable for about 6–8 more weeks.
After that, we can't safely install your fence posts until spring.
If you want it done this year: [Booking Link]
— [Company Name]"

SMS 2 (October 1):
"Last call for 2026 fence installs, [First Name].
We have [X] spots left before winter.
Once those are filled, earliest availability is April.
Want to lock one in? Reply FENCE and I'll call you today."

SMS 3 (October 15 — Final):
"[First Name] — final message on 2026 fence season.
Ground freeze is coming fast.
If you want your fence this year, I need to hear from you today.
Call me: [Phone] — [Owner Name]"
```

### 4.9 Commercial Fencing Outreach Workflow
**Trigger:** New commercial lead added

```
Step 1: Immediate email (not SMS for commercial — professional first impression)
Subject: "Commercial Fence Inquiry — [Company Name] | [Date]"
Body: Professional introduction, list of commercial capabilities 
(chain link, ornamental, security fence, construction hoarding, temporary fencing),
request for site walk details

Step 2 (Day 2): LinkedIn or phone follow-up (internal task to owner)

Step 3 (Day 5): SMS to property manager
"Hi [First Name] — [Your Name] here from [Company]. 
Sent over some info on our commercial fence services — did you get a chance to review?
Happy to come by for a site walk this week. What works for you?"

Step 4 (Day 10): Final follow-up email with project portfolio/references
```

### 4.10 Referral Re-Engagement Workflow (90-Day Nurture)
**Trigger:** Lead goes cold (Day 21 no response) OR "Closed Lost - Timing"

```
30-day check-in SMS:
"Hey [First Name] — [Owner Name] here. Checking back in on your fence project.
Still thinking about it? We'd love to earn your business when the timing is right.
Any questions? Just reply!"

60-day:
SMS: "Hi [First Name] — fence season is in full swing!
Still have a few spots open if you're ready to move forward.
Your original quote is still valid — want to revisit it?"

90-day:
SMS: "Hey [First Name] — last check-in. 
If you're still planning a fence project, we'd love to be your company.
Want a fresh site measure and updated quote? Things may have changed."
→ If no response: Tag as "Cold Lead" — move to annual re-engage list
```

---

## Section 5: Lead Sources & Capture

### 5.1 Lead Source Categories (Custom Field)

Set up a **Lead Source** custom field with these values:
- Google LSA (Local Services Ads)
- Google Ads
- Google Organic
- Facebook/Instagram Ad
- Kijiji / Facebook Marketplace
- Referral — Customer
- Referral — Neighbour (neighbour campaign)
- Referral — Real Estate Agent
- Referral — Property Manager
- Door-to-Door / Door Hanger
- Home Show / Trade Show
- Repeat Customer
- Other

### 5.2 Lead Source Notes

**Google LSA (Local Services Ads)**
- Highest intent — homeowner actively searching "fence company near me"
- Speed-to-lead is critical: LSA penalizes slow response with lower placement
- Integration: Use GHL webhook or Zapier to capture LSA leads directly into snapshot
- Auto-tag: "Hot Lead" — trigger speed-to-lead workflow immediately

**Kijiji / Facebook Marketplace**
- High volume, lower intent — price-sensitive, multi-quoting is universal
- Capture: Manual add or Facebook Lead Ad integration
- Key insight: These prospects respond to social proof and visual content (photos of recent work)
- Workflow: Include "here's our recent work" gallery link in Day 1 follow-up

**Real Estate Agents (New Home / Landscaping)**
- Referral pipeline worth building systematically
- New homeowners frequently fence their new property within the first year
- Tactic: Build a realtor outreach sequence — offer agents a referral gift ($50 restaurant card per referred close)
- Workflow: Agent referral → "Priority booking" framing to homeowner

**Property Managers (Commercial)**
- Manage multiple properties = recurring revenue potential
- A single property management company can be worth $5,000–$50,000/year in fence work
- Tactic: Direct outreach campaign via email (not SMS initially)
- Integration: LinkedIn prospecting → GHL manual entry → commercial nurture sequence

**Door Knocking / Neighbour Campaign**
- Extremely high conversion when done during an active install
- Contractor is on site, work is visible, social proof is immediate
- Tactic: Print door hangers, enter neighbour number into GHL on the spot
- Workflow: Neighbour campaign (Section 4.7) triggers immediately

---

## Section 6: Custom Fields Required

### 6.1 Contact-Level Custom Fields

| Field Name | Type | Values/Notes |
|------------|------|-------------|
| Fence Type | Dropdown | Privacy, Chain Link, Split Rail, Ornamental/Wrought Iron, Aluminum, Vinyl, Farm Wire, Temporary |
| Property Type | Dropdown | Residential, Commercial, Agricultural, Industrial |
| Lead Source | Dropdown | (See Section 5.1) |
| Linear Feet (Estimated) | Number | Estimated project scope |
| Number of Gates | Number | Standard, double, automated gate |
| Quote Amount | Currency | Dollar value of quote sent |
| Permit Required | Checkbox | Yes / No / TBD |
| Permit Number | Text | Tracking number from municipality |
| Property Survey On File | Dropdown | Yes / No / Ordered |
| Install Date | Date | Confirmed install date |
| Crew Lead | Text | Name of crew assigned |
| Post Material | Dropdown | Pressure-treated wood, steel, aluminum, concrete |
| Lost Reason | Dropdown | Price, Competitor, Timing, No Response, Project Cancelled |
| Review Left | Checkbox | Google review status |
| Referral Source Name | Text | Who referred them |

### 6.2 Opportunity-Level Custom Fields

| Field Name | Type | Notes |
|------------|------|-------|
| Fence Type | Dropdown | Same as contact |
| Linear Footage | Number | Confirmed measurement |
| Post Count (Estimated) | Number | For materials |
| Gate Count | Number | Single / Double / Automated |
| Quote Sent Date | Date | For follow-up timing |
| Deposit Amount | Currency | Track partial payments |
| Permit Status | Dropdown | Not Required / Applied / Pending / Approved / Denied |
| Materials Ordered | Checkbox | Posts, pickets, rails, hardware, concrete |
| Project Phase | Dropdown | Single Phase / Multi-Phase (for commercial/farm) |

---

## Section 7: SMS & Email Templates

### 7.1 Estimate Follow-Up Templates

**Template: "Still Thinking?" (Day 7 SMS)**
```
Hey [First Name] — [Owner Name] here from [Company].
Just checking in on your fence quote for $[Quote Amount].
We're booking [3-4 weeks] out right now — a lot of homeowners are 
locking in their spring/summer spot early.
Happy to answer any questions — reply anytime!
```

**Template: "Quote Comparison Tips" (Day 7 Email)**
```
Subject: "How to compare fence quotes (what most homeowners miss)"

Hi [First Name],

Getting multiple quotes is smart — here's what to look for beyond price:

🔩 POST DEPTH: We set posts 4 feet deep minimum. Shallow posts heave in frost.
🏗️ CONCRETE FOOTING: Every post should be set in concrete, not backfilled dirt.
📋 PERMIT HANDLING: We pull the permit — it's included in your quote.
🪵 MATERIAL GRADE: We use [Grade X] pressure-treated posts rated for ground contact.
⚖️ LINEAR FOOT PRICE: Ask every company to quote the same linear footage so you're comparing apples to apples.
🔒 WARRANTY: We warranty our installs for [X] years.

Your quote from us covers all of this.

Any questions? Hit reply — I read every message personally.

— [Owner Name]
[Company]
[Phone]
```

### 7.2 Seasonal Urgency Templates

**Template: Spring Push (March)**
```
Subject: "Fence season just opened — here's why you should book now"

Hi [First Name],

Every spring it's the same story: homeowners wait until May/June to book, 
then find out we're booked until August.

Here's where we're at right now:
📅 Currently booking: [Late April / Early May]
⏳ Wait after May 1: 6–10 weeks

If you want your [fence type] installed before summer — now is the time.

[BOOK FREE ESTIMATE →]

— [Owner Name]
```

**Template: Fall Ground Freeze Urgency**
```
Hey [First Name] — [Owner Name] here.

Quick heads up: we can only set fence posts in unfrozen ground.
In [Region], that window closes around [October 31 / November 15].

Once the ground freezes, next availability is April.

We have [X] install slots left this fall.

If you want your fence done this year, reply YES and I'll call you within the hour.
```

### 7.3 Permit Status Templates

**Template: Permit Submitted**
```
Hi [First Name]! Quick update — your fence permit has been submitted to [Municipality].
Standard processing: 5–15 business days.

We'll message you the moment it's approved. No action needed from you!
— [Company Name] 🏗️
```

**Template: Permit Approved**
```
🎉 Great news, [First Name] — your fence permit is APPROVED!

We're now scheduling your installation. Expect a call from us within 24 hours 
to lock in your date.

So excited to get your [fence type] in the ground!
— [Owner Name], [Company]
```

### 7.4 Review Request Templates

**Template: Review Request (Day 1 Post-Install)**
```
Hey [First Name]! Your new fence looks amazing 🏡

We'd love a quick Google review — even just a sentence or two helps other 
homeowners find us and trust us.

Takes 2 minutes: [Google Review Link]

Thank you so much — you're the reason we do this work!
— [Owner Name]
```

**Template: Referral Ask (Day 14)**
```
Hey [First Name] — any neighbours been asking about your fence?

We pay a $[75] referral credit to every customer who sends us a paying job.
Just have them mention your name when they call!

[Phone] | [Booking Link]

Thanks for trusting us with your home! 🏡
```

---

## Section 8: Booking Flow

### 8.1 Calendar Setup

**Calendar Name:** Free Fence Estimate / Site Measure

**Settings:**
- Duration: 60 minutes (30 min for small residential, 60+ for commercial/farm)
- Buffer: 30 minutes between appointments (travel time)
- Max per day: 6 (for solo estimator), adjust based on crew
- Availability: Monday–Saturday, 8 AM – 5 PM

**Pre-Booking Form Fields (required):**
1. First Name (required)
2. Last Name (required)
3. Phone (required)
4. Email (required)
5. Property Address (required — needed for route planning)
6. Fence Type (dropdown: Privacy, Chain Link, Split Rail, Ornamental, Farm, Other)
7. Approximate Linear Footage (dropdown: Under 100 ft / 100–300 ft / 300–500 ft / 500+ ft)
8. Number of Gates (number)
9. How did you hear about us? (dropdown — lead source)
10. Describe your project (text area — optional)

**Confirmation Page:**
- What to expect on the site visit
- "Please mark any underground utilities or have Utility Locate completed"
- Owner's personal photo + brief bio (builds trust before they meet)
- Link to recent fence project gallery

**Post-Booking Sequence:** (Section 4.2)

### 8.2 Call-In Flow

**Missed Call Text-Back:**
```
"Hey! You just tried to reach [Company Name].
We're probably out installing someone's fence right now 😄
Reply here or book a free estimate: [Booking Link]
We respond within 15 minutes!"
```

**IVR Option (if using GHL phone):**
- Press 1: Book a free estimate
- Press 2: Speak to estimator
- Press 3: Project update / existing customer

---

## Section 9: Reporting & Dashboard

### 9.1 Recommended Dashboard Widgets

| Widget | Metric |
|--------|--------|
| New Leads This Month | Contact count |
| Site Measures Booked | Appointment count |
| Quotes Sent | Opportunity count |
| Quote-to-Close Rate | % (Closed Won / Quotes Sent) |
| Average Job Value | Revenue / Closed Won count |
| Revenue This Month | Sum of Closed Won |
| Leads by Source | Breakdown by lead source field |
| Pipeline Value | Sum of all open opportunity values |
| Reviews Requested vs. Received | Review workflow completion % |

### 9.2 Key Fencing Business Metrics

- **Quote-to-close rate target:** 35–50% (industry average is 20–25%; good follow-up gets to 40%+)
- **Average residential job:** $4,000–$12,000 (varies by fence type and linear footage)
- **Average commercial job:** $8,000–$50,000+
- **Speed-to-lead benchmark:** Under 5 minutes = 2x higher close rate
- **Review conversion target:** 30%+ of completed installs leave a review

---

## Section 10: Snapshot Differentiators — What Makes This Stand Out

### 10.1 The Neighbour Campaign (Biggest Differentiator)
No other fencing snapshot has a systematic neighbour capture workflow. This alone can generate 2–4 additional leads per install. At 20 installs/month, that's 40–80 warm neighbours touched — with the highest social proof possible ("your neighbour just used them and their fence looks great").

### 10.2 Permit Tracking Workflow
Permits are the most common reason fence projects stall after the deposit is paid. A workflow that proactively communicates permit status eliminates the most common complaint fencing companies receive and dramatically reduces "where is my fence?" calls.

### 10.3 Seasonal Campaign Logic
The snapshot includes two built-in seasonal campaigns (spring launch + fall ground freeze urgency) that can be deployed with one click. Most snapshots are evergreen only — they miss the single biggest urgency lever in the fencing business.

### 10.4 Industry-Specific Vocabulary
Every SMS and email template uses fencing industry language: post depth, concrete footing, linear feet, picket, rail, panel, gate, post hole, pre-galvanized chain link, ornamental, property line, survey, permit number. This builds immediate credibility with fencing contractors who are tired of generic "home services" software that clearly wasn't built for them.

### 10.5 Multi-Pipeline Architecture
Three separate pipelines (residential, commercial, repair/service) + one sub-pipeline (farm/agricultural) — each with appropriate stages and workflows. Most snapshots dump everything into one pipeline, creating chaos for contractors who do both residential and commercial work.

### 10.6 Pre-Install Communication
The pre-install checklist workflow (mark utilities, clear fence line, pet containment) reduces day-of delays by 30–40%. This alone justifies the monthly fee — fewer phone calls, fewer "we couldn't start because the dog was loose" service issues.

### 10.7 Lost Reason Tracking
Capturing why deals are lost (price, competitor, timing, no response) allows the contractor to identify patterns. If 60% of losses are "price" — that's a positioning problem. If 60% are "no response" — that's a follow-up problem the snapshot can solve.

---

## Section 11: 1app Implementation Notes

### 11.1 Snapshot Components Checklist

**Pipeline:**
- [ ] Residential Fencing (14 stages)
- [ ] Commercial Fencing (11 stages)
- [ ] Repair & Service (7 stages)
- [ ] Farm & Agricultural (9 stages)

**Workflows (Automations):**
- [ ] Speed-to-Lead (5-minute response)
- [ ] Missed Call Text-Back
- [ ] Estimate Booking Confirmation
- [ ] Estimate Reminder (24hr + 2hr)
- [ ] Quote Follow-Up Sequence (Days 1, 3, 7, 14, 21)
- [ ] Permit Submitted Notification
- [ ] Permit Update (Day 5, Day 10)
- [ ] Permit Approved Trigger
- [ ] Pre-Install Checklist (7 days, 48hr, morning-of)
- [ ] Post-Install Review Request (Days 1, 3, 7)
- [ ] Referral Ask (Day 14)
- [ ] Neighbour Campaign Trigger
- [ ] 90-Day Nurture Sequence
- [ ] Spring Campaign (activate March 15)
- [ ] Fall Ground Freeze Campaign (activate September 1)
- [ ] Commercial Lead Nurture
- [ ] Weather Delay Communication (manual trigger)

**Custom Fields:**
- [ ] All contact-level fields (Section 6.1)
- [ ] All opportunity-level fields (Section 6.2)

**Calendar:**
- [ ] Free Estimate / Site Measure calendar
- [ ] Pre-booking form with all fields
- [ ] Confirmation page with trust elements

**Forms:**
- [ ] Website lead capture form (embedded)
- [ ] Commercial inquiry form (separate — professional framing)
- [ ] Referral form ("Someone referred me" landing page)

**Tags:**
- [ ] hot-lead, warm-lead, cold-lead
- [ ] residential, commercial, agricultural, repair
- [ ] spring-campaign-2026, fall-campaign-2026
- [ ] neighbour-lead, referral-lead, lsa-lead
- [ ] permit-pending, permit-approved
- [ ] review-requested, review-received
- [ ] no-survey, survey-ordered, survey-confirmed

**Snapshots/Templates:**
- [ ] Estimate follow-up email template (with fence comparison guide)
- [ ] Seasonal campaign email templates (spring + fall)
- [ ] Post-install review email
- [ ] Commercial proposal follow-up email
- [ ] Referral program explanation email

**Landing Pages:**
- [ ] "Book Free Estimate" page (with gallery + testimonials)
- [ ] Referral landing page ("You were referred by [Name]")
- [ ] Neighbour offer page ("Your neighbour just had their fence done...")

### 11.2 Onboarding Customization Points

When onboarding a fencing client, the following must be customized:

1. **Company name** throughout all templates
2. **Owner name** in all personal SMS/emails
3. **Phone number** in all templates
4. **Booking link** in all templates
5. **Google review link** in review workflow
6. **Referral credit amount** (suggest $50–$100)
7. **Service area** in any location-specific language
8. **Seasonal dates** (adjust for Southern vs. Northern markets — ground freeze timing varies)
9. **Average booking window** ("we're booking X weeks out" — update quarterly)
10. **Permit lead time** (varies by municipality — 5 days vs. 30 days)
11. **Fence material specialties** (if they only do wood, remove chain link/ornamental references)
12. **Crew lead name(s)** for install day SMS

### 11.3 Pricing Recommendation for 1app

| Tier | Included | Monthly Price |
|------|----------|---------------|
| Starter | Residential pipeline + speed-to-lead + quote follow-up + review workflow | $197/mo |
| Growth | All pipelines + seasonal campaigns + neighbour campaign + permit tracking | $397/mo |
| Pro | Everything + custom landing pages + referral system + reporting dashboard | $597/mo |

**Recommended upsell:** Monthly maintenance call ($99–$199/mo) to review pipeline health, update seasonal campaigns, and coach on follow-up. This positions 1app as a strategic partner, not just a software vendor.

---

## Section 12: Compliance & Privacy Notes

- All SMS workflows must include opt-out language (STOP to unsubscribe) — this is Canadian CASL and US TCPA compliant
- Lead forms must include clear consent checkbox for marketing communications
- Referral program must not constitute a "kickback" under contractor licensing regulations — position as customer appreciation credit, not a finder's fee
- Review requests must not offer incentives in exchange for positive reviews (violates Google policy) — the referral credit is for referrals, not for reviews

---

## Appendix A: Fencing Industry Vocabulary Reference

**Fence Components:**
- **Post:** The vertical member set in the ground — typically wood (pressure-treated 4x4), steel, or aluminum
- **Post hole:** The excavated hole, typically 3–4 feet deep depending on frost line
- **Concrete footing:** Concrete poured around each post base for stability
- **Rail:** Horizontal member that connects posts — typically 2x4 pressure-treated
- **Picket:** Individual vertical boards attached to rails (for privacy fence and split rail)
- **Panel:** Pre-assembled fence section, typically 6–8 feet wide
- **Gate:** Opening section of fence — single, double (drive-through), or automated
- **Linear feet:** How fencing is measured and quoted — total run of fence in feet
- **Frost line:** Depth below which the ground doesn't freeze — determines post depth

**Fence Types:**
- **Privacy fence:** Solid panel, typically 6ft, cedar or pressure-treated wood — most common residential
- **Chain link:** Galvanized or vinyl-coated steel mesh — residential and commercial
- **Split rail:** Rustic log-look fence, 2 or 3 rail — decorative/farm
- **Ornamental:** Decorative steel or aluminum, often wrought iron look — commercial, upscale residential
- **Aluminum:** Powder-coated aluminum panels — low maintenance, pool-approved
- **Vinyl/PVC:** Plastic fence panels — no maintenance, no rot, premium price
- **Farm wire:** High-tensile wire on T-posts or wood posts — agricultural perimeter
- **Temporary fence:** Panel fencing for construction sites, events

**Project Terms:**
- **Property line:** Legal boundary of the property — determines where fence can be placed
- **Survey / Property survey:** Legal document showing property boundaries — required before fencing property line
- **Easement:** Right-of-way on a portion of the property — fencing may not be permitted in easements
- **Setback:** Required distance from property line to fence — varies by municipality
- **Permit:** Municipal building permit required for most permanent fences
- **Utility locate:** Service to mark underground utilities before post holes are dug (call 811 in US, Ontario One Call / Utilities Kingston in Ontario)

---

## Appendix B: Competitor Snapshot Analysis

### What Competitors Are Missing (Your Advantage)

| Feature | Generic Home Services Snapshot | Basic Fencing Snapshot | **1app Fencing Snapshot** |
|---------|-------------------------------|----------------------|--------------------------|
| Neighbour campaign | ❌ | ❌ | ✅ |
| Permit tracking workflow | ❌ | ❌ | ✅ |
| Seasonal campaigns (spring + fall) | ❌ | ❌ | ✅ |
| Farm/agricultural pipeline | ❌ | ❌ | ✅ |
| Pre-install checklist | ❌ | Partial | ✅ |
| Industry-specific vocabulary | ❌ | Partial | ✅ |
| Multi-pipeline (residential + commercial) | ❌ | ❌ | ✅ |
| Lost reason tracking | Partial | ❌ | ✅ |
| Referral program workflow | ❌ | ❌ | ✅ |
| Weather delay communication | ❌ | ❌ | ✅ |
| Commercial-specific nurture | ❌ | ❌ | ✅ |
| Property survey communication | ❌ | ❌ | ✅ |

---

## Appendix C: Sample Workflow Trigger Map

```
Lead Source → CRM Entry
     │
     ├─ Form Submission → Speed-to-Lead Workflow (0 min)
     ├─ Missed Call → Missed Call Text-Back (immediate)
     ├─ Manual Entry (Kijiji, referral) → Speed-to-Lead (triggered manually)
     │
     ↓
Stage: "New Inquiry"
     │
     ↓ (appointment booked)
Stage: "Site Measure Scheduled"
     → Booking Confirmation Workflow
     → 24hr Reminder
     → 2hr Reminder
     │
     ↓ (estimator marks complete)
Stage: "Site Measure Complete"
     → Internal task: "Send quote within 24 hours"
     │
     ↓ (quote sent)
Stage: "Quote Sent"
     → Quote Follow-Up Sequence (Days 1, 3, 7, 14, 21)
     │
     ├─ Response: YES → Move to "Verbal Yes"
     │    → Internal task: "Get deposit"
     │
     └─ No Response Day 21 → Move to "90-Day Nurture"
          → Nurture Sequence (30, 60, 90 days)
          → If still cold: Tag "Cold Lead" → Annual campaign list
     │
     ↓ (deposit received)
Stage: "Deposit Received"
     │
     ├─ Permit Required = YES → "Permit Applied" workflow
     └─ Permit Required = NO → "Install Scheduled" workflow
     │
     ↓
Stage: "Install Scheduled"
     → Pre-Install Checklist (7 days, 48hr, morning-of)
     │
     ↓ (install done)
Stage: "Install Complete"
     → Review Workflow (Days 1, 3, 7)
     → Neighbour Campaign (parallel)
     → Referral Ask (Day 14)
     │
     ↓ (payment collected)
Stage: "Closed Won"
     → Add to "Past Customer" list
     → Add to Spring/Fall campaign list
     → Annual check-in scheduled (12 months out)
```

---

*Document prepared by 1app Technologies Inc. | Internal research use only*
*This document represents a build specification and market analysis — not a final delivered snapshot.*
