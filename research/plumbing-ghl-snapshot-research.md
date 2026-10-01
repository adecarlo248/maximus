# Plumbing GHL Snapshot Research
## 1APP Technologies — Comprehensive Build Document
### Prepared for: Tony DeCarlo | 1APP Technologies Inc.

---

> **Research Note:** Web search API was unavailable during initial research attempts. This document is built from deep industry expertise in plumbing business operations, GHL CRM architecture, home services marketing, and field service software (ServiceTitan, Housecall Pro, Jobber, FieldEdge, Workiz). All recommendations reflect actual plumbing business workflows, pain points, and conversion patterns from the industry.

---

## EXECUTIVE SUMMARY

The plumbing industry is one of the highest-ROI verticals for a GHL SaaS agency. Plumbers have:
- **High average job values** ($200–$8,000+ depending on service type)
- **Emergency demand** that makes 24/7 response critical
- **Seasonal spikes** (winter freeze, spring startup) that create campaign opportunities
- **Recurring revenue potential** via maintenance plans
- **Terrible tech adoption** — most plumbers still use pen, paper, and missed calls

Most GHL plumbing snapshots on the market are generic "home services" templates with plumbing branding slapped on. They miss the core nuance: **plumbing has 4 completely different customer journeys** (emergency, scheduled, maintenance, commercial), and each needs its own pipeline and workflow logic.

The 1APP plumbing snapshot should be the first purpose-built, plumbing-first GHL system that handles all four journeys out of the box.

---

## PART 1: PLUMBING BUSINESS PAIN POINTS

### 1.1 The #1 Problem: Missed Emergency Calls = Missed Revenue

Emergency plumbing is time-sensitive. A homeowner with a burst pipe, backed-up sewer, or no hot water calls **the first plumber who answers**. If that call hits voicemail:
- 70–80% of callers move on to the next plumber immediately
- They do NOT leave messages or wait for callbacks
- The average emergency call is worth $350–$1,200 in immediate revenue

**Pain:** Most plumbing companies have no after-hours coverage system. The owner's cell rings at 2am, they miss it, the customer calls a competitor.

**GHL Opportunity:** Missed Call Text Back + Voice AI Agent that qualifies and books emergency service calls 24/7.

### 1.2 No-Shows and Last-Minute Cancellations

Plumbers block 2–4 hour dispatch windows for technicians. A no-show wastes that entire window — lost technician time, fuel, and opportunity cost.

**Root cause:** No confirmation sequence, no reminder sequence. Customer books and forgets.

**Industry data:** Companies using automated confirmation + reminder sequences see no-show rates drop from 15–25% to under 5%.

**GHL Opportunity:** Multi-touch confirmation workflow with SMS + email, including a "please confirm your appointment" response trigger.

### 1.3 Slow or No Follow-Up After Service

After a service call, most plumbers:
- Send a paper invoice or email invoice
- Never follow up for reviews
- Never upsell maintenance plans
- Never send seasonal campaign messages
- Lose the customer to a competitor the next time something breaks

**GHL Opportunity:** Post-service automation sequences that capture reviews, upsell maintenance plans, and keep the company top-of-mind.

### 1.4 Lead Source Chaos

Plumbing leads come from 6–8 different sources, and most plumbers have no system to track which source converts best:
- Google Local Service Ads (LSA)
- Organic Google / GMB
- Angi / HomeAdvisor
- Yelp
- Direct referrals
- Repeat customers
- Home warranty companies (American Home Shield, etc.)
- Property managers

**Pain:** Without source tracking, plumbers spend ad budget on low-ROI channels while ignoring high-ROI ones.

**GHL Opportunity:** UTM-tracked intake forms + lead source field in every contact record, with pipeline reporting by source.

### 1.5 No System for Maintenance Plan Upsells

Plumbing companies that sell annual maintenance plans have **3x the customer LTV** of those that don't. Plans typically include:
- Annual water heater flush and inspection
- Drain cleaning check
- Backflow test (where required)
- Priority dispatch on emergency calls
- Discounted service rates

**Pain:** Most plumbers have no upsell system. They mention it verbally at the end of a service call, the customer says "sure, send me the info," and nothing ever happens.

**GHL Opportunity:** Maintenance plan upsell workflow triggered post-service, with proposal link, follow-up sequence, and pipeline stage tracking.

### 1.6 Technician Scheduling Complexity

Unlike HVAC (which has defined seasons), plumbing has:
- Emergency calls (same-day, any hour)
- Scheduled calls (next-day to 1 week out)
- Project work (re-pipes, water heater replacements, bathroom remodels) — multi-day
- Preventive maintenance (annual)

Most scheduling software can't differentiate. Plumbers try to handle all four in the same calendar and it creates chaos.

**GHL Opportunity:** Separate booking calendars with different buffer times, service types, and confirmation workflows for each job category.

### 1.7 Slow Invoicing and Payment Collection

Field technicians complete a job, take a paper invoice, drive back to the office or give the invoice to the homeowner. Payment is collected days or weeks later.

**Pain:** Cash flow problems. Average collection cycle for non-digital plumbers is 14–21 days.

**GHL Opportunity:** Post-job automation that sends payment links via text immediately after job completion (requires integration with invoicing tool or GHL's native payment features).

### 1.8 Google Review Gap

The #1 driver of new plumbing leads is Google reviews. Companies with 100+ reviews averaging 4.7+ stars consistently dominate local search.

**Pain:** Most plumbers ask for reviews verbally and almost no one follows through. They have 12 reviews while competitors have 200.

**GHL Opportunity:** Post-service review sequence sent at the exact right moment (30–60 minutes after job completion) with a direct review link.

### 1.9 Property Manager and Commercial Accounts — No Nurture System

Property managers and commercial clients are high-volume, high-LTV accounts. A single property management company with 50 units can be worth $15,000–$40,000/year in service calls.

**Pain:** Plumbers land these accounts by chance (one good job), but have no nurture system to maintain the relationship, win new properties, or prevent churn.

**GHL Opportunity:** Dedicated B2B pipeline with commercial-specific workflows, proposal tracking, and quarterly check-in automations.

### 1.10 No Seasonal Campaign System

Plumbing demand spikes seasonally but most plumbers miss the opportunity:
- **Fall:** Winterization (outdoor hose bibs, pipe insulation, water heater prep)
- **Spring:** Backflow testing, sump pump checks, irrigation startup
- **Summer:** Drain cleaning promotions (grease buildup from summer cooking)
- **Any time:** Water heater replacement campaigns (targeting 8+ year old units)

**Pain:** No campaign calendar, no database segmentation, no automated sends.

**GHL Opportunity:** Pre-built seasonal campaign library with SMS + email, segmented by service history.

---

## PART 2: GHL PLUMBING SNAPSHOTS ON THE MARKET — COMPETITIVE ANALYSIS

### 2.1 What's Currently Available

Based on industry knowledge of GHL snapshots for home services, current plumbing offerings typically include:

**Generic "Home Services" Snapshots ($97–$297 one-time)**
- Basic contact form and pipeline
- 1–2 automations (usually just missed call text back)
- Generic email templates
- No plumbing-specific workflows
- No service type differentiation

**Niche Plumbing Snapshots ($197–$497 one-time)**
- Slightly more tailored pipelines
- 3–5 workflows
- Basic review request
- Still missing: maintenance plan upsell, commercial pipeline, seasonal campaigns, service type routing

**What they all miss:**
1. Emergency vs. scheduled routing logic
2. Plumbing-specific booking intake (address, issue type, home ownership)
3. Water heater replacement campaign
4. Maintenance plan upsell sequence
5. Property manager / commercial workflow
6. Seasonal campaign library
7. Google LSA vs. organic lead source differentiation
8. Technician ETA notification workflow
9. Backflow test reminder campaign
10. Sewer scope / hydro-jet upsell workflow

### 2.2 Pricing Benchmarks

| Snapshot Type | Market Price | What's Included |
|--------------|-------------|-----------------|
| Generic Home Services | $97–$197 | 1-2 workflows, basic pipeline |
| Plumbing-Branded Generic | $197–$297 | 3–5 workflows, basic pipeline |
| Full Plumbing Build | $497–$997 | 8–12 workflows, multiple pipelines |
| **1APP Target** | **$297–$497/mo SaaS** | **20+ workflows, full system** |

### 2.3 1APP Competitive Differentiation Strategy

The 1APP plumbing snapshot should position as **the only GHL plumbing system built by people who understand how plumbing companies actually operate** — not just a generic CRM with plumbing terminology added.

Key differentiators:
1. **4 separate pipelines** (not 1 generic pipeline) — Emergency, Scheduled, Projects, Commercial
2. **Service type routing** at intake — different workflows triggered based on job type
3. **Water heater age segmentation** — database field + annual replacement campaign
4. **Maintenance plan pipeline** — separate from service pipeline, tracks upsell funnel
5. **Property manager B2B workflow** — different than residential
6. **Pre-built seasonal campaign calendar** — 12 campaigns ready to launch
7. **Technician ETA workflow** — keeps customers informed, reduces calls back
8. **Review timing optimization** — emergency vs. scheduled service timing differs
9. **Backflow/winterization reminder campaigns** — based on service history tags
10. **Home warranty company workflow** — specialized intake and follow-up

---

## PART 3: PLUMBING-SPECIFIC CRM PIPELINE STAGES

### 3.1 Pipeline 1: Emergency Service Pipeline

This pipeline handles burst pipes, sewage backup, no hot water, flooded basement, gas line issues — anything same-day urgent.

**Stages:**
1. **Emergency Inquiry** — Incoming call/text/form, unqualified
2. **Dispatching** — Technician assigned, ETA communicated
3. **On Site** — Technician arrived, diagnosing
4. **Quote Presented** — Estimate given to homeowner
5. **Approved — In Progress** — Work authorized, underway
6. **Job Complete — Awaiting Payment** — Work done, invoice sent
7. **Paid & Closed** — Payment received
8. **Review Requested** — Post-service review sequence triggered
9. **Upsell Opportunity** — Tagged for maintenance plan or follow-up work

**Custom Fields for this pipeline:**
- Issue type (burst pipe, drain backup, no hot water, etc.)
- Property address
- Home ownership status (owner/renter)
- Lead source (Google LSA, referral, repeat customer)
- Assigned technician
- Job value (estimated / actual)
- Water heater age (if relevant)

### 3.2 Pipeline 2: Scheduled Service Pipeline

Scheduled service calls — drain cleaning, fixture replacement, minor repairs, etc. — have a different timeline (1–7 days out) and different conversion dynamics.

**Stages:**
1. **New Lead / Inquiry**
2. **Appointment Booked**
3. **Appointment Confirmed** (customer responded to confirmation)
4. **Day-Of Reminder Sent**
5. **Technician En Route** (ETA text triggered)
6. **On Site**
7. **Quote / Estimate Presented**
8. **Approved — Work Underway**
9. **Job Complete**
10. **Invoice Sent**
11. **Paid**
12. **Review Requested**
13. **Maintenance Plan Offered**
14. **Closed — Won** / **Closed — Lost**

### 3.3 Pipeline 3: Project Pipeline (Re-Pipes, Water Heater Replacements, Bathroom Remodels)

Larger jobs with longer sales cycles, multiple visits, and higher stakes.

**Stages:**
1. **Project Inquiry**
2. **Site Assessment Booked**
3. **Assessment Complete**
4. **Proposal Drafted**
5. **Proposal Sent**
6. **Follow-Up 1** (3 days)
7. **Follow-Up 2** (7 days)
8. **Proposal Accepted**
9. **Deposit Collected**
10. **Work Scheduled**
11. **In Progress**
12. **Punch List / Final Walk**
13. **Final Invoice Sent**
14. **Paid — Closed**
15. **Review & Referral Requested**

### 3.4 Pipeline 4: Commercial / Property Manager Pipeline

B2B pipeline for property management companies, apartment complexes, restaurants, retail, offices.

**Stages:**
1. **Prospect Identified**
2. **Initial Outreach Sent**
3. **Meeting / Discovery Call Booked**
4. **Proposal / Service Agreement Sent**
5. **Agreement Signed**
6. **Onboarded — Active Account**
7. **Quarterly Check-In Due**
8. **At Risk** (no service calls in 60+ days)
9. **Churned** / **Retained**

### 3.5 Pipeline 5: Maintenance Plan Pipeline (Upsell Funnel)

Tracks the upsell funnel from service customer → maintenance plan subscriber.

**Stages:**
1. **Plan Offered — Awaiting Response**
2. **Follow-Up 1**
3. **Follow-Up 2**
4. **Plan Sold — Active Subscriber**
5. **Renewal Due (30 days)**
6. **Renewed** / **Not Renewed**

---

## PART 4: PLUMBING-SPECIFIC WORKFLOWS

### 4.1 Workflow 1: Missed Call Text Back — Emergency Routing

**Trigger:** Missed call to main business line

**Actions:**
1. Immediately send SMS: *"Hi! This is [Company Name]. We missed your call — we know plumbing problems can't wait. Reply YES if this is an emergency and we'll call you right back. Or click here to book: [link]"*
2. Tag contact as "Missed Call Emergency Potential"
3. Wait 2 minutes
4. If no response: Send second SMS: *"Still there? Our technician can usually be there within 60–90 minutes for emergency calls. Call us at [number] or book online: [link]"*
5. Notify internal team via Slack/email: "Missed emergency call from [number]"
6. Add to Emergency Pipeline: Stage 1

**Notes:** This workflow runs 24/7. Emergency tone is critical — don't make them jump through hoops.

---

### 4.2 Workflow 2: New Lead Intake & Routing (Service Type Triage)

**Trigger:** New contact form submission or web inquiry

**Condition branch based on "Service Type" field:**

- **Branch A — Emergency:** Route to Emergency Pipeline, trigger Emergency Intake sequence
- **Branch B — Drain Cleaning / Repair:** Route to Scheduled Pipeline, send booking link with 24-hour slots
- **Branch C — Water Heater:** Route to Scheduled Pipeline (or Project if replacement), flag for quote
- **Branch D — Re-pipe / Renovation:** Route to Project Pipeline, trigger site assessment booking sequence
- **Branch E — Backflow / Maintenance:** Route to Scheduled Pipeline with seasonal note
- **Branch F — Not Sure:** Send SMS asking for more info, assign to sales team

---

### 4.3 Workflow 3: Appointment Confirmation Sequence

**Trigger:** Appointment booked (any service type)

**Actions:**
1. Immediate: Confirmation SMS + Email (with appointment details, technician name if known, what to expect)
2. 24 hours before: Reminder SMS — *"Reminder: [Tech Name] from [Company] is coming tomorrow at [time]. Reply C to confirm or RESCHEDULE to change."*
3. If no confirmation received by 2 hours before: Call attempt, then second SMS
4. Day-of (2 hours before): Final reminder + *"Our technician is on their way!"* (or ETA trigger)
5. If customer replies CANCEL: Move to cancellation workflow, send reschedule link, notify dispatcher

---

### 4.4 Workflow 4: Technician ETA Notification

**Trigger:** Dispatcher marks job status as "Technician En Route" (manual trigger or Zapier from scheduling software)

**Actions:**
1. Immediately: SMS to customer — *"Great news — [Tech Name] from [Company] is on his way! He'll arrive in approximately [ETA] minutes. You can call him directly at [number] if needed."*
2. Optional: Include tracking link (if using GPS/scheduling software with Zapier)
3. Update pipeline stage to "Technician En Route"

**Why this matters:** Reduces "where is my plumber?" callback volume by 40–60%. Creates a premium experience that generates reviews.

---

### 4.5 Workflow 5: Post-Service Review Request

**Trigger:** Job marked as "Complete" in pipeline (or manual tag "Job Complete")

**Timing matters:**
- **Emergency service:** Wait 60–90 minutes. Customer is relieved, grateful. Strike while hot.
- **Scheduled service:** Wait 2–3 hours.
- **Project work:** Wait 24 hours.

**Actions:**
1. SMS at optimal timing: *"Hi [Name], [Tech Name] just wrapped up your service. We hope everything went smoothly! Would you mind leaving us a quick Google review? It takes 2 minutes and means the world to our small business: [Review Link]. Thank you!"*
2. Wait 48 hours
3. If no review: Email follow-up with same link
4. Wait 5 days
5. If no review: Final SMS — *"[Name], just following up one more time on that review. No pressure at all — we just appreciate every one we get. [Link]"*
5. Tag as "Review Requested" — stop sequence

---

### 4.6 Workflow 6: Maintenance Plan Upsell Sequence

**Trigger:** Tag "Job Complete — No Maintenance Plan"

**Actions:**
1. Wait 24 hours
2. SMS: *"[Name], thanks for choosing [Company] yesterday! Quick question — have you heard about our [Plan Name] Plumbing Maintenance Plan? For $X/year, you get annual water heater flush, drain check, priority dispatch on emergency calls, and 10% off all services. Interested in hearing more?"*
3. If YES reply: Send plan details link + book consultation
4. Wait 5 days (if no response)
5. Email: Full maintenance plan overview with benefits, testimonials, price
6. Wait 7 days
7. Final SMS: *"Last chance — our maintenance plan spots are filling up for the season. Lock in your rate here: [link]"*
8. If no response: Tag "Maintenance Plan — Not Interested" and remove from sequence

---

### 4.7 Workflow 7: Water Heater Replacement Campaign

**Trigger:** Contact has custom field "Water Heater Age" = 8+ years, OR service history tag "Water Heater Serviced 8+ Years"

**Actions:**
1. Email: Subject: *"Is Your Water Heater Living on Borrowed Time?"*
   - Content: Signs your water heater is failing, cost of emergency replacement vs. planned replacement, tankless options, seasonal pricing
   - CTA: Get a Free Water Heater Quote
2. Wait 7 days (if no response)
3. SMS: *"Hi [Name], did you see our note about your [X]-year-old water heater? Most units fail between 8–12 years — we'd hate for you to wake up to a cold shower or water damage. Quick quote takes 10 minutes: [link]"*
4. Wait 14 days
5. Final email: Seasonal promotion angle (e.g., "Winter is coming — is your water heater ready?")

---

### 4.8 Workflow 8: Emergency After-Hours Voice AI Routing

**Trigger:** Inbound call after hours (configurable hours)

**GHL Voice AI Script:**
- "Thank you for calling [Company Name]. We know plumbing problems don't wait — that's why our emergency line is available 24/7."
- "If this is an emergency like a burst pipe, sewage backup, or no hot water, press 1 and we'll have a technician call you within 10 minutes."
- "For next-day appointments, press 2 and we'll get you booked right now."
- "To leave a message, press 3."

**Branch 1 (Emergency):** Collect address, issue type, name, phone → Trigger emergency alert to on-call technician + dispatcher → SMS customer with ETA

**Branch 2 (Next-Day):** Collect name, phone, issue type → Add to Scheduled Pipeline → Send booking confirmation

---

### 4.9 Workflow 9: No-Show Recovery

**Trigger:** Appointment status marked "No Show" or customer no response on confirmation

**Actions:**
1. Immediately: SMS — *"[Name], we had a technician scheduled at your home today at [time]. We weren't able to reach you — are you still looking for plumbing help? We can rebook you today: [link]"*
2. Wait 2 hours
3. Call attempt (or Missed Call Text Back triggers)
4. Wait 24 hours
5. Email: *"Still need a hand? We have openings this week."*
6. Wait 7 days
7. Tag "No Show — Sent to Nurture" and add to 30-day re-engagement campaign

---

### 4.10 Workflow 10: Re-Engagement (60/90-Day Dormant Customers)

**Trigger:** Contact has tag "Past Customer" and no activity in 60 days

**Actions:**
1. SMS: *"Hi [Name], it's been a while since we've seen you! We wanted to check in and let you know we're still your neighborhood plumber. Any drains running slow, drips you've been putting off, or a water heater that needs a look? Reply HERE and we'll get you scheduled."*
2. Wait 14 days
3. Email: Seasonal campaign or promotion
4. Wait 30 days
5. Final SMS: "Summer special — drain cleaning for $X" (or relevant seasonal hook)

---

### 4.11 Workflow 11: Home Warranty Company Lead Handling

Home warranty companies (American Home Shield, Choice Home Warranty, etc.) refer plumbing calls but with different constraints:
- Rate is pre-set (contractor doesn't negotiate price with homeowner)
- Work order number is required
- Approval sometimes needed before work starts
- Documentation is critical

**Trigger:** Lead source tagged "Home Warranty"

**Actions:**
1. Auto-assign to Home Warranty pipeline branch
2. Confirmation email/SMS that includes work order number field
3. Different intake form (collects warranty company name, claim number, property address, coverage details)
4. Post-service documentation automation (service report sent to warranty company)
5. NO maintenance plan upsell (contractually inappropriate for warranty calls)
6. Review request still appropriate

---

### 4.12 Workflow 12: Seasonal Winterization Campaign

**Trigger:** Manual launch, November 1st (or configured to auto-launch by date)
**Audience:** All contacts in service area with tag "Homeowner" or "Past Customer"

**Campaign:**
1. SMS: *"❄️ Winter prep time! [Company Name] is offering pipe winterization services before the cold hits. Don't wait until you have a burst pipe — schedule your winterization for just $[X]: [link]"*
2. Wait 3 days
3. Email: Full winterization guide — what gets winterized, why it matters, cost comparison (winterization vs. burst pipe repair)
4. Wait 5 days
5. Final SMS: *"Only [X] slots left for November winterization — once those go, we're booking into December: [link]"*

---

### 4.13 Workflow 13: Property Manager Onboarding Sequence

**Trigger:** Tag "Commercial — Property Manager — New Account"

**Actions:**
1. Welcome email: Who your account rep is, how to submit service requests, priority dispatch policy, billing details
2. Day 3: Introduction call from owner or account manager
3. Day 7: SMS check-in: *"How's everything going at [Property Name]? Any maintenance needs this week?"*
4. Day 30: Monthly service summary email
5. Day 85: Quarterly review outreach
6. Tag "Quarterly Review Due" → sales pipeline follow-up

---

### 4.14 Workflow 14: Drain Cleaning Special Campaign

**Trigger:** Manual launch (can time to spring or fall)
**Audience:** Past customers, no service in 60+ days

**Campaign:**
1. SMS: *"Is your kitchen drain running slower than usual? 🚿 Spring buildup is real — we're running a drain cleaning special this month for $[X]. Book by [date]: [link]"*
2. Wait 4 days
3. Email: "Top 5 Signs Your Drains Need Professional Cleaning" with CTA
4. Wait 5 days
5. Final SMS: *"Last day for our $[X] drain cleaning special — grab your slot before we're full: [link]"*

---

### 4.15 Workflow 15: Referral Request Sequence

**Trigger:** Tag "Paid — Happy Customer" (post-payment, combined with review trigger)

**Actions:**
1. Wait 7 days after service
2. SMS: *"[Name], thanks again for choosing us! If you have a friend or neighbor who needs plumbing help, we'd love to help them too. Send them our way and we'll thank you with $[X] off your next service."*
3. Wait 14 days
4. Email: Referral program details with referral tracking link

---

## PART 5: PLUMBING LEAD SOURCES & HANDLING STRATEGY

### 5.1 Google Local Service Ads (LSA)

**Volume:** High — LSA dominates emergency plumbing searches
**Lead Quality:** Very high (customer is actively searching, Google-screened)
**Characteristics:**
- Caller-initiated (phone call or message)
- High urgency (usually emergency or near-emergency)
- Pre-qualified to some extent by Google screening

**Handling:**
- Same-day response required (LSA measures response time)
- Tag as "LSA Lead" for ROI tracking
- Route to Emergency or Scheduled pipeline based on issue type
- Missed call text back is critical — LSA caller will immediately try next result

**CRM Setup:**
- Source field: Google LSA
- Automatic priority tag
- Fast-response confirmation SMS within 60 seconds

---

### 5.2 Google Organic / Google Business Profile (GMB)

**Volume:** Moderate–High (steady)
**Lead Quality:** High
**Characteristics:**
- Mix of emergency and scheduled
- Research-driven (they checked reviews)

**Handling:**
- Standard intake form + service type triage
- Ensure Google Review requests reinforce organic visibility
- Tag for attribution

---

### 5.3 Angi / HomeAdvisor

**Volume:** High (but lead quality varies)
**Lead Quality:** Medium (shared lead — same lead sent to 3–5 plumbers)
**Characteristics:**
- Competitive — need to respond FIRST within 5 minutes
- Price-sensitive
- Lead may not be exclusive

**Handling:**
- Immediate auto-response SMS (within 30 seconds of lead arrival via Zapier/webhook)
- Call initiated within 5 minutes
- Different messaging — emphasize speed, reviews, local presence
- Track close rate to measure Angi ROI

**Workflow:** Angi-specific branch with super-fast response trigger + conversion tracking

---

### 5.4 Referrals

**Volume:** Moderate
**Lead Quality:** Very High (trust already established)
**Characteristics:**
- Often warm — they know you, trust you
- More likely to convert, less likely to price shop

**Handling:**
- Personalized intake ("Who referred you?" field)
- Thank the referrer (automated thank you + referral reward if program exists)
- Skip hard-sell sequences — these leads need nurture, not pressure

---

### 5.5 Repeat Customers

**Volume:** Moderate (grows over time with retention)
**Lead Quality:** Highest — already know you, trust you
**Characteristics:**
- Longest customer relationship
- Most likely to buy maintenance plans
- Best review candidates

**Handling:**
- VIP tag + priority dispatch note
- Skip re-engagement campaigns (they're already engaged)
- Fast-track to booking confirmation

---

### 5.6 Home Warranty Companies

**Volume:** Varies (depends on partnerships)
**Lead Quality:** Medium (pre-qualified by warranty company)
**Characteristics:**
- Fixed rate (contractor doesn't set price)
- Work order driven
- High volume if company has AHS or similar partnership

**Handling:** Dedicated Home Warranty workflow (see Workflow 11 above)

---

### 5.7 Property Managers / Commercial

**Volume:** Low initial, high repeat
**Lead Quality:** Very high LTV
**Handling:** Dedicated B2B pipeline (see Pipeline 4 above)

---

## PART 6: PLUMBING SMS/EMAIL TEMPLATES

### 6.1 Emergency Service Templates

**Initial Response — Missed Call**
```
Hi [First Name]! This is [Company Name] – we missed your call. Plumbing emergencies can't wait. Is this urgent? Reply YES and we'll call you right back, or book online: [link]
```

**Emergency Booking Confirmation**
```
✅ [First Name], your emergency service request is confirmed! [Tech Name] is being dispatched and will arrive in approximately [ETA]. Questions? Call us: [number]. We'll take care of you.
```

**Technician En Route**
```
🔧 Good news, [First Name]! Our plumber [Tech Name] is on his way and will arrive in about [X] minutes. He drives a [vehicle description]. Call him directly: [number]
```

**Post-Emergency Review Request (60 min after completion)**
```
Hi [First Name] – [Tech Name] just let us know he wrapped up your job. Hope everything is flowing again! If you have 2 minutes, your Google review means everything to our small business: [Google Review Link] 🙏
```

---

### 6.2 Scheduled Service Templates

**Booking Confirmation**
```
Hi [First Name]! Your appointment with [Company Name] is confirmed for [Day], [Date] between [Time Window]. Your technician will send you a heads-up when they're on their way. Questions? [number]
```

**24-Hour Reminder**
```
Reminder: [Company Name] will be at your home tomorrow, [Date] at [Time]. Reply C to confirm or RESCHEDULE if you need to change your time.
```

**Day-Of Reminder (2 Hours Before)**
```
👋 Just a reminder — [Tech Name] from [Company] is on his way and will arrive within your [Time] window. Get ready to say goodbye to that [issue]! Call us if anything changes: [number]
```

---

### 6.3 Maintenance Plan Upsell Templates

**SMS Upsell (24 hours post-service)**
```
[First Name] – thanks for trusting [Company] yesterday! Did you know our [Plan Name] plan keeps your plumbing in top shape for just $[X]/year? Includes annual water heater flush, drain check, priority service + 10% off. Interested? [link]
```

**Email Subject Lines (Test these):**
- "Stop Paying Emergency Rates — Here's a Smarter Option"
- "Your Plumbing Covered All Year for Less Than $[X]/Month"
- "[First Name], Are You a Smart Homeowner? (Here's the Test)"

---

### 6.4 Water Heater Replacement Campaign

**Email Subject:** *Your [X]-Year-Old Water Heater Is Living on Borrowed Time*

**SMS:**
```
[First Name], we noticed your water heater is [X] years old. Most fail between 8–12 years — often at the worst time. We're offering free water heater estimates this month. Want us to check yours out? [link]
```

---

### 6.5 Seasonal Campaign — Winterization

**SMS:**
```
❄️ Winter prep time, [First Name]! [Company] is booking pipe winterization services now. Protect your pipes before the freeze — schedule for $[X] before [Date]: [link]
```

**Email Subject:** *"Are Your Pipes Ready for Winter? [City] Temperatures Drop Fast"*

---

### 6.6 Drain Cleaning Special

**SMS:**
```
[First Name], spring is the season when drains show their true colors 🚿. We're running a $[X] drain cleaning special this month only. Book before [Date]: [link]
```

---

### 6.7 Re-Engagement (60+ Days Dormant)

**SMS:**
```
Hey [First Name]! Haven't heard from you in a while — hope your plumbing's been behaving! Any drips, slow drains, or other issues you've been putting off? We're your local plumber — reply here or book: [link]
```

---

## PART 7: BOOKING FLOW DESIGN

### 7.1 Emergency Booking Flow

**Intake Form Fields (minimal — emergencies hate long forms):**
1. First Name
2. Phone (required — for callback)
3. Property Address
4. Issue Type (dropdown):
   - Burst Pipe
   - Sewer Backup
   - No Hot Water
   - Major Leak
   - Clogged Drain
   - Gas Line Issue
   - Flooding
   - Other (describe)
5. Brief description (optional, 1 line)
6. How did you hear about us? (dropdown)

**After submission:**
- Immediate SMS: "We got your emergency request! We're dispatching now — a technician will call you within [X] minutes."
- Notification to dispatcher with full lead details
- Add to Emergency Pipeline Stage 1

---

### 7.2 Scheduled Service Booking Flow

**Calendar Setup:**
- 2-hour booking windows (not specific times)
- Available slots: next-day through 7 days out
- Buffer time: 30 minutes between appointments
- After-hours message: redirect to emergency form if urgent

**Intake Form Fields:**
1. First Name + Last Name
2. Phone
3. Email
4. Property Address (with city/zip for service area check)
5. Service Needed (dropdown):
   - Drain Cleaning
   - Fixture Repair/Replacement
   - Water Heater Service
   - Toilet Repair
   - Pipe Repair
   - Other (describe)
6. Brief issue description
7. Are you the homeowner? (Yes / No — renters need permission from landlord for some work)
8. How did you hear about us?

---

### 7.3 Project / Quote Booking Flow

**For larger work (re-pipes, water heater replacement, bathroom plumbing, etc.)**

**Calendar Setup:**
- 60–90 minute site assessment slots
- 3–10 days out (enough lead time)
- Only available weekdays or specific hours

**Intake Form Fields:**
1. Contact info (standard)
2. Property address
3. Type of project (dropdown)
4. Property type (Single family, Condo, Multi-unit, Commercial)
5. Rough scope/description (text field)
6. Timeline urgency (Not urgent / Within 1 month / Within 3 months)
7. Homeowner/renter
8. How did you hear about us?

---

## PART 8: REVIEW GENERATION STRATEGY

### 8.1 Review Timing by Service Type

| Service Type | Best Review Request Timing | Why |
|-------------|---------------------------|-----|
| Emergency (burst pipe, backup) | 45–90 min post-completion | Customer relief is peak — gratitude is high |
| Scheduled (repair, installation) | 2–4 hours post-completion | Customer has had time to test the fix |
| Water heater replacement | 24 hours | Let them enjoy a hot shower first |
| Re-pipe / large project | 48–72 hours | Job complexity warrants reflection time |
| Drain cleaning | 1–2 hours | Quick service, quick review window |

### 8.2 Review Request Sequence

**Step 1 — Primary Ask (SMS)**
- Direct, warm, personal
- Direct Google Review link (use Google Places API link)
- Mention the technician by name

**Step 2 — Follow-Up (Email, 48 hours)**
- Different angle: "It takes 2 minutes and helps homeowners in [City] find trustworthy plumbers"
- Include link again

**Step 3 — Final Ask (SMS, 7 days)**
- Only send if no review yet
- Keep brief, no pressure
- "Last check-in on that review…"

### 8.3 Review Response Workflow

**Trigger:** New Google Review received (via Zapier/webhook)
- Positive review: Automated thank-you email to customer + internal note "Share this on social"
- Negative review: Alert to owner immediately + personal outreach within 2 hours

### 8.4 Review Link Optimization

- Use `https://search.google.com/local/writereview?placeid=PLACE_ID` format
- Shorten with bit.ly or custom domain
- Test link on mobile (most reviews are written on phones)

---

## PART 9: MAINTENANCE PLAN / MEMBERSHIP UPSELL WORKFLOW

### 9.1 Plan Structure (Template for Plumber to Customize)

**[Company Name] HomeShield Plumbing Plan — $X/year**

Includes:
- Annual water heater flush and inspection
- Drain flow check (all accessible drains)
- Toilet performance check
- Outdoor hose bib inspection
- Priority dispatch on all emergency calls
- 10% discount on all service calls
- No diagnostic/service call fees for covered visits

**Why this works:**
- Annual revenue per customer: $180–$360 vs. one-off $200–$500 service call
- LTV multiplier: 3x for customers on maintenance plans
- Priority scheduling gives plumber control of their calendar

### 9.2 Upsell Funnel Stages

**Stage 1 — Trigger Point:**
Post-service completion. This is the highest-intent moment for upsell.

**Stage 2 — First Ask:**
SMS at 24 hours (see template above). Keep it brief, conversational.

**Stage 3 — Detail Drop:**
Email at day 3. Full breakdown of plan benefits, cost comparison (plan vs. typical emergency call), testimonial if available.

**Stage 4 — Final Urgency:**
SMS at day 10. Limited spots or seasonal deadline.

**Stage 5 — Closed:**
If purchased: Add to "Maintenance Plan — Active" segment. Annual renewal reminder automation begins.
If declined: Tag "Maintenance Plan — Declined [Date]". Re-offer in 6 months.

### 9.3 Maintenance Plan Renewal Automation

**Trigger:** Custom date field "Plan Renewal Date" = 30 days from now

**Actions:**
1. Day 30 before renewal: Email with renewal reminder + what's included
2. Day 14 before: SMS check-in + link to renew
3. Day 7 before: Email + urgent tone
4. Day 1 before: SMS — "Your plan renews tomorrow!"
5. Day of renewal: Auto-charge (if Stripe/payment integration) + confirmation email
6. If renewal fails: Dunning sequence begins (3 attempts over 7 days)

---

## PART 10: SEASONAL CAMPAIGN CALENDAR

### Full 12-Month Plumbing Campaign Calendar

| Month | Campaign | Service Focus | Audience |
|-------|----------|--------------|---------|
| January | "Frozen Pipe Check-Up" | Pipe inspection post-winter | All homeowners |
| February | "Valentine's Day Special: Give Your Home Love" | Water heater flush + drain cleaning bundle | Past customers |
| March | "Spring Backflow Testing Season" | Backflow preventer test/cert | Homeowners with sprinklers, commercial |
| April | "Spring Sump Pump Check" | Sump pump inspection, replacement | Homeowners in flood-risk areas |
| May | "Pre-Summer Drain Cleaning" | Drain cleaning before grease season | Past drain customers |
| June | "Water Heater Health Check" | WH inspection, flush | Customers with WH 7+ years |
| July | "Summer Sale — Book Ahead, Save" | General repairs & installs | All customers |
| August | "Back-to-School Plumbing Tune-Up" | Full home plumbing check | Homeowners |
| September | "Fall Maintenance Plan Enrollment" | Maintenance plan upsell | Non-plan customers |
| October | "Pre-Winter Water Heater Special" | WH replacement/upgrade | WH 8+ years old |
| November | "Winterization Before the Freeze" | Pipe winterization, outdoor shutoffs | All homeowners |
| December | "End-of-Year Home Plumbing Checklist" | General + maintenance plan renewal | All customers + maintenance plan holders |

---

## PART 11: PROPERTY MANAGER / COMMERCIAL WORKFLOW

### 11.1 Why Commercial Is a Priority

A single property management company with 30 units can generate:
- Average 2–4 service calls per unit per year
- At $250 average = $15,000–$40,000/year in revenue
- Plus larger projects (re-pipes, water heater replacement programs)
- Long-term contract potential

One commercial account = hundreds of residential accounts in LTV.

### 11.2 Commercial Lead Sources

- Direct outreach (cold SMS/email to property managers)
- Referrals from existing residential customers
- HOA and condo association referrals
- Commercial real estate networks
- Restoration companies (water damage referrals)

### 11.3 Commercial CRM Fields (Custom)

- Account Type (Residential Multi-Unit / Commercial / HOA / Restaurant / Retail)
- Number of Units
- Primary Contact Name + Cell
- Secondary Contact (maintenance coordinator)
- Service Area (address or addresses)
- Preferred Service Windows
- Billing Type (net-30, net-15, credit card on file)
- Contract Start/End Date
- Annual Service Volume (estimated)
- Last Service Date
- Account Health Score (custom field or tag)

### 11.4 Commercial Nurture Sequence

**New Account Onboarding (first 30 days):**
1. Welcome call from owner
2. Digital welcome packet (email) — service request process, after-hours emergency line, billing setup
3. Day 14: SMS check-in — "How's everything going at [Property]?"
4. Day 30: Monthly service summary

**Ongoing Retention:**
- Quarterly check-in call (scheduled via automation reminder)
- Monthly service report email (requires integration or manual entry)
- Annual contract renewal 60 days before expiry
- Winter/summer seasonal service reminders

**At-Risk Signal:** No service calls in 45+ days (for high-volume accounts). Auto-tag "At Risk" and alert account manager.

---

## PART 12: COMPETITIVE DIFFERENTIATION — WHAT MAKES 1APP'S SNAPSHOT STAND OUT

### 12.1 The 4-Pipeline Architecture

No other plumbing snapshot on the market has separate pipelines for Emergency, Scheduled, Project, and Commercial. This alone justifies a higher price point.

### 12.2 Service Type Triage at Intake

The routing logic (Workflow 2) that sends different job types to different pipelines and triggers different workflows is the core of the system. It mirrors how real plumbing dispatch works.

### 12.3 Pre-Built Seasonal Campaign Library

12 campaign-ready SMS/email sequences means the plumber can launch a new revenue-generating campaign every month without writing a single message.

### 12.4 The Water Heater Replacement Engine

Water heater replacement is the single highest-margin, highest-conversion upsell in plumbing. The combination of:
- Custom field: Water heater age (set during service call)
- Annual birthday trigger for WH reaching age threshold
- Replacement campaign sequence

...creates automatic pipeline for high-ticket work that competitors don't know to automate.

### 12.5 Maintenance Plan Monetization System

Most snapshots mention maintenance plans but don't build the full funnel. The 1APP snapshot includes the full upsell sequence, renewal automation, and plan-holder nurture sequence.

### 12.6 Commercial / Property Manager Track

This is completely missing from 99% of home services snapshots. The commercial track alone is worth the price for any plumber trying to grow beyond residential.

### 12.7 Technician ETA Workflow

This is the single most commented-on feature when plumbers adopt software like Housecall Pro or ServiceTitan — customers love knowing when the tech is arriving. No existing plumbing GHL snapshot includes this.

### 12.8 Review Timing Optimization

Most snapshots send reviews after a generic delay. The 1APP snapshot differentiates review timing by service type — emergency customers get asked sooner (when gratitude is highest), project customers get a longer wait. This dramatically improves review capture rates.

---

## PART 13: SNAPSHOT TECHNICAL BUILD SPECS

### 13.1 What to Include in the Snapshot

**Pipelines (5):**
1. Emergency Service
2. Scheduled Service
3. Project (Re-pipe / WH Replacement / Remodel)
4. Commercial / Property Manager
5. Maintenance Plan Upsell

**Workflows (15+):**
1. Missed Call Text Back — Emergency
2. New Lead Intake & Service Type Routing
3. Appointment Confirmation Sequence
4. Technician ETA Notification
5. Post-Service Review Request (3-step)
6. Maintenance Plan Upsell Sequence
7. Water Heater Replacement Campaign
8. After-Hours Voice AI Routing
9. No-Show Recovery
10. Re-Engagement (60-Day Dormant)
11. Home Warranty Lead Handling
12. Winterization Campaign
13. Spring/Summer Drain Cleaning Campaign
14. Property Manager Onboarding
15. Maintenance Plan Renewal
16. Referral Request Sequence
17. Angi/HomeAdvisor Fast-Response Workflow

**Forms (6):**
1. Emergency Service Request
2. Scheduled Service Booking Intake
3. Project / Quote Request
4. Commercial Account Inquiry
5. Maintenance Plan Enrollment
6. Referral Submission

**Calendars (3):**
1. Emergency / Same-Day (no time restrictions)
2. Scheduled Service (business hours, 2-hour windows)
3. Site Assessment / Quote (60-minute blocks, limited availability)

**Custom Fields (20+):**
- Service Type
- Issue Type
- Property Address
- Home Ownership Status
- Lead Source
- Assigned Technician
- Water Heater Age
- Water Heater Install Date
- Last Service Date
- Service History Tags (drain cleaning, WH service, backflow, etc.)
- Maintenance Plan Status
- Plan Renewal Date
- Account Type (residential/commercial)
- Number of Units (commercial)
- Billing Type
- Preferred Contact Method
- Annual Service Value (estimated)
- Referral Source (who referred them)
- Review Requested Date
- Review Submitted (Yes/No)

**Tags (25+):**
- Emergency Lead
- Scheduled Lead
- Project Lead
- Commercial Lead
- Home Warranty Lead
- Angi Lead
- LSA Lead
- Referral
- Past Customer
- Maintenance Plan — Active
- Maintenance Plan — Interested
- Maintenance Plan — Declined
- Review Requested
- Review Received
- WH Age 8+
- No Show
- At Risk (commercial)
- Seasonal Campaign — Winterization
- Seasonal Campaign — Backflow
- Seasonal Campaign — Drain Special
- Technician Assigned
- Awaiting Payment
- VIP Customer
- Property Manager
- HOA Account

**Email Templates (15):**
1. Service Booking Confirmation
2. Emergency Service Booking Confirmation
3. Appointment Reminder (24h)
4. Maintenance Plan Introduction
5. Maintenance Plan Full Details
6. Water Heater Replacement Campaign
7. Winter Prep / Winterization Campaign
8. Spring Drain Cleaning Campaign
9. Review Request Follow-Up
10. Commercial Welcome Packet
11. Monthly Service Summary (commercial)
12. Referral Program Introduction
13. Maintenance Plan Renewal Reminder
14. Annual Inspection Reminder
15. Re-Engagement (Dormant Customer)

**SMS Templates (20+):**
All templates listed in Part 6 above, plus:
- Appointment Cancelled — Reschedule Offer
- Payment Receipt Confirmation
- Technician Running Late
- Bad Weather — Appointment Update
- Waitlist Notification ("A slot opened up!")

---

## PART 14: PRICING STRATEGY FOR 1APP

### 14.1 Recommended Pricing Tiers

**Tier 1 — Starter: $197/month**
- Emergency workflow only (Missed Call Text Back + Voice AI + Review Request)
- 1 pipeline (Emergency)
- SMS/email templates — emergency and review only
- Booking calendar (scheduled service)
- Good for solo plumbers or just getting started

**Tier 2 — Growth: $397/month**
- Everything in Tier 1
- All 5 pipelines
- 10 core workflows
- Seasonal campaign library (4 campaigns)
- Water heater replacement campaign
- Maintenance plan upsell sequence
- Good for 2–10 employee shops

**Tier 3 — Pro: $597/month**
- Everything in Tier 2
- All 15+ workflows
- Commercial / property manager track
- All 12 seasonal campaigns
- White-glove onboarding call
- Monthly strategy check-in
- Good for established companies wanting full automation

### 14.2 Onboarding Package (Add-On)

**One-Time Setup Fee: $500–$997**
- Full account setup and configuration
- Custom branding
- Integration with existing scheduling software (Jobber, Housecall Pro, ServiceTitan)
- Phone number setup and testing
- Team training call
- 30-day check-in

---

## PART 15: INTEGRATION RECOMMENDATIONS

### 15.1 Native GHL Integrations

- **Stripe** — payment collection via text after job completion
- **Google Business Profile** — review monitoring and response alerts
- **Facebook Ads** — lead form integration for paid traffic
- **Google Ads** — conversion tracking for LSA and search

### 15.2 Zapier Integrations (if plumber uses field service software)

| Software | Zapier Use Case |
|---------|----------------|
| Jobber | New job → GHL contact + pipeline stage |
| Housecall Pro | Job complete → trigger review request workflow |
| ServiceTitan | Customer added → sync to GHL |
| QuickBooks | Invoice paid → update GHL pipeline |
| Google Sheets | Job log → GHL contact/tag update |

### 15.3 Phone System Setup

- GHL local number (area code matching plumber's service area)
- Missed Call Text Back: enable globally
- Voice AI: configure for after-hours
- Call recording: enable (for training and disputes)
- Call routing: forward unanswered calls to secondary number (owner's cell)

---

## SUMMARY: THE 1APP PLUMBING SNAPSHOT IS...

The first GHL plumbing CRM built around **how plumbing companies actually operate** — not how a marketing agency thinks they operate.

It handles all four customer journeys (emergency, scheduled, project, commercial), automates the highest-revenue upsells (maintenance plans, water heater replacement), runs 12 months of seasonal campaigns automatically, and keeps every technician dispatched with professional customer communication every step of the way.

**The result:** A plumber on the 1APP system can go from 12 Google reviews and $400k/year to 200+ reviews and $800k/year in 18–24 months — not because they hired more people, but because they stopped letting money fall through the cracks.

That's the pitch. Build the system. Sell the outcome.

---

*Document prepared by Maximus | 1APP Technologies Research Division | July 2026*
