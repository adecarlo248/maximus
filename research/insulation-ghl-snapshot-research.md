# Insulation Contractor GHL Snapshot — 1app Agency Build Research
**Document Type:** Comprehensive Snapshot Research & Build Specification  
**Prepared For:** 1APP Technologies Inc. — SaaS Agency Division  
**Industry:** Residential & Commercial Insulation Contractors  
**Date:** July 2026  
**Status:** Agency Build Reference — Pre-Production

---

## EXECUTIVE SUMMARY

The insulation industry is one of the most underserved verticals in the GHL SaaS ecosystem. While HVAC, roofing, and plumbing have multiple mature snapshots, insulation contractors are largely running on spreadsheets and phone calls, losing leads daily to speed-to-lead failures and zero follow-up systems.

The opportunity is significant: Canada's insulation market is driven by a combination of government rebate programs (Canada Greener Homes, Enbridge HER+, BC Hydro, Hydro Québec), aging housing stock, rising energy costs, and new construction growth. Insulation jobs are high-ticket ($3,000–$30,000+), rarely repeat, but have massive referral potential if you understand the neighbourhood dynamics.

The 1app snapshot for insulation contractors needs to do what no other snapshot currently does: **combine speed-to-lead for emergency situations, a rebate education engine, a multi-pipeline by job type, and a neighbour referral campaign** — all in one ready-to-launch package.

---

## SECTION 1: INDUSTRY PAIN POINTS

### 1.1 The Invisible Product Problem

Insulation is the single biggest sales psychology challenge in home improvement. Unlike a kitchen renovation or a new roof, nobody sees insulation. Homeowners experience the *results* (warm in winter, cool in summer, lower energy bills), not the product itself.

**What this means for GHL:**
- Lead nurture must sell **outcomes**, not features
- R-value education needs to happen before and after the quote, not just at the quote stage
- Before/after content (thermal imaging, energy bill comparisons) must be embedded in follow-up sequences
- Price objections are common because homeowners can't see what they're paying for — the ROI sequence must bridge this gap

### 1.2 Government Rebate Complexity

Canada Greener Homes (federal), Enbridge Home Efficiency Rebate Plus (Ontario), BC Hydro, Hydro Québec, and various municipal programs create a confusing landscape. Homeowners who want the rebate don't know:
- Whether they qualify
- What energy audit they need first (EnerGuide)
- What minimum R-value upgrades trigger payment
- Whether to get pre-approval before or after the work
- How long reimbursement takes (8–20 weeks typically)

**What this means for GHL:**
- A "rebate qualification" funnel is a massive lead magnet
- Contractors who can explain the rebate process capture leads competitors miss
- Follow-up sequences must educate on timelines to prevent buyer's remorse ("why haven't I gotten my rebate yet?")
- The booking funnel should lead with "Free Energy Assessment + Rebate Review" not "Free Quote"

### 1.3 Long Quote-to-Close Cycle

Insulation quotes often involve:
1. An initial site visit or phone consultation
2. A formal written estimate (R-value recommendations, scope of work)
3. A homeowner decision process (often 2–6 weeks)
4. Possible energy audit requirement before government rebate work can begin

**What this means for GHL:**
- Multiple touchpoints are required between first contact and close
- Automated follow-up sequences at 1 day, 3 day, 1 week, 2 week, and 30 day intervals are essential
- The pipeline needs stages that reflect actual contractor workflow (not generic CRM stages)
- Stalled estimates need a specific re-engagement workflow

### 1.4 Seasonal Demand Spikes

Insulation is a shoulder-season business (Sept–Nov and Feb–April in Canada). The rush is real — homeowners panic when their energy bills spike in November and start booking attic insulation jobs in October.

**What this means for GHL:**
- Proactive campaigns need to fire 6–8 weeks before peak season
- Summer is slow — need a "now is the time to book before the rush" campaign
- Appointment booking should be tied to capacity (calendar limits by crew size)
- Off-season is when new construction and commercial work fills the gap

### 1.5 No Repeat Business Model

Unlike HVAC (annual maintenance) or lawn care (weekly visits), insulation is a once-in-20-years purchase for most homeowners. After the job, the contractor has no natural reason to contact the customer again.

**What this means for GHL:**
- Post-install value must come from referrals, not repeat service
- Review campaigns are critical — one Google review per job compounds over time
- "Neighbour targeting" (same street, same house vintage) is the highest-ROI referral play
- Annual "how's your energy bill?" check-in emails maintain relationship without being salesy

### 1.6 No Referral Capture System

Most insulation contractors are 100% reliant on Google and word of mouth, with no systematic way to capture, encourage, or reward referrals.

**What this means for GHL:**
- Post-install referral campaigns with a clear ask and easy mechanism are gold
- Neighbourhood campaigns (mailers + digital retargeting) targeting same house vintage are highly effective
- Builder and contractor relationships need their own CRM track (B2B pipeline)

---

## SECTION 2: GHL SNAPSHOT MARKET ANALYSIS

### 2.1 What Exists

As of mid-2026, the GHL snapshot marketplace includes several home services snapshots, but the insulation-specific landscape is thin:

**Generic Home Services Snapshots:**
- Focus on roofing, HVAC, plumbing, and general contracting
- Pipeline stages are too generic (New Lead → Quoted → Closed) to handle rebate workflows
- No understanding of energy audit requirements or multi-program rebate tracking
- Booking flows focus on "Free Quote" — not differentiated for insulation

**What's been attempted in the community:**
- Some HVAC snapshots have been partially adapted for insulation
- The borrowing tends to fail because HVAC has maintenance repeat business; insulation does not
- No known snapshot specifically handles the Canada Greener Homes workflow

### 2.2 What's Missing

The gap in the market is significant across every dimension:

| Dimension | Generic Snapshot | What's Needed |
|---|---|---|
| Pipeline | Generic 5-stage | Job-type pipelines (attic/basement/spray/new build/commercial) |
| Lead Source Tracking | Basic | Google LSA, Enbridge referral, energy auditor, builder, Facebook |
| Booking CTA | "Free Quote" | "Free Energy Assessment & Rebate Review" |
| Follow-up | Basic 3-email | Rebate education, ROI sequence, stalled estimate re-engagement |
| Post-Install | Minimal | Review → Referral → Neighbour campaign chain |
| B2B Track | None | Builder/GC/energy auditor partner pipeline |
| Rebate Education | None | Full rebate drip sequence with program-specific links |
| Seasonal Campaigns | None | Pre-season booking rush + off-season capacity fill |
| Commercial | None | Commercial/ICI pipeline for larger commercial jobs |

### 2.3 The Differentiation Opportunity

A well-built 1app insulation snapshot wins on three fronts:

1. **Rebate intelligence** — No other snapshot educates contractors AND homeowners on the Canada Greener Homes / Enbridge HER+ workflow
2. **Multi-pipeline by job type** — Matching contractor reality (attic upgrade looks nothing like spray foam new construction)
3. **Neighbour referral engine** — The highest ROI campaign for any insulation company, completely absent in existing snapshots

---

## SECTION 3: PIPELINE ARCHITECTURE

### 3.1 Pipeline 1 — Residential Attic Upgrade

The highest-volume pipeline. Blown-in and batt replacement is the bread-and-butter for residential insulation companies.

**Stages:**
1. New Lead (Web, LSA, Facebook, Referral)
2. Free Assessment Booked
3. Assessment Completed — Awaiting Quote
4. Quote Sent
5. Quote Follow-Up (auto-trigger at 72 hrs if no response)
6. Rebate Review Required (trigger when homeowner mentions government program)
7. Estimate Approved — Awaiting Deposit
8. Deposit Received — Job Scheduled
9. Job Completed
10. Review Requested
11. Referral Requested
12. Closed Won
13. Not a Fit / No Budget (with 6-month re-engage)

**Key Custom Fields:**
- Current attic R-value (e.g., R-12 existing)
- Target R-value (e.g., R-60 recommended)
- Attic sq footage
- Access type (pull-down stairs / attic hatch / none)
- Thermal bridging concerns (Y/N)
- Air sealing required (Y/N)
- Rebate program interested in (Greener Homes / Enbridge HER+ / None)
- EnerGuide audit completed (Y/N/Booked)
- Quote amount
- Deposit received date
- Install date
- Post-install R-value achieved

### 3.2 Pipeline 2 — Basement & Crawlspace Insulation

Often triggered by moisture concerns, finishing the basement, or foundation issues.

**Stages:**
1. New Lead
2. Assessment Booked
3. Assessment Completed
4. Moisture Assessment Required (sub-workflow trigger)
5. Quote Sent
6. Vapour Barrier Discussion (separate line item education)
7. Approved — Awaiting Deposit
8. Deposit Received — Scheduled
9. Job Complete
10. Review / Referral Request
11. Closed Won

**Key Custom Fields:**
- Basement type (poured concrete / block / ICF)
- Current insulation type (none / fibreglass / rigid foam)
- Moisture issues present (Y/N — critical for vapour barrier decision)
- Vapour barrier required (6-mil poly / Delta-MS / other)
- Heated or unheated crawlspace
- Radon mitigation concern (Y/N — cross-sell flag)

### 3.3 Pipeline 3 — Spray Foam (Open-Cell & Closed-Cell)

Higher ticket, more complex, often commercial or new build.

**Stages:**
1. New Lead (specify: residential/commercial/new construction)
2. Site Assessment Booked
3. Site Assessment Completed — Scope Defined
4. Open-Cell vs Closed-Cell Discussion Required
5. Quote Sent (detailed with product spec)
6. Quote Revision Request
7. Approved — Awaiting Deposit
8. Material Lead Time Confirmed
9. Job Scheduled
10. Job Complete — Cure Time Notification Sent
11. Post-Install Inspection
12. Review / Referral
13. Closed Won

**Key Custom Fields:**
- Application type (roof deck / rim joists / crawlspace / wall cavity / commercial)
- Product type (open-cell 0.5 lb / closed-cell 2 lb)
- Target R-value per inch required
- Vapour control layer needed (closed-cell acts as VB; open-cell does not)
- Cure time communicated to client (Y/N — critical for occupation re-entry)
- Application thickness (inches)
- Square footage + board footage
- Air sealing compliance (NBC 2020 / local code)

### 3.4 Pipeline 4 — New Construction (Builder/GC)

B2B relationship pipeline. Longer sales cycle, higher volume, repeat business.

**Stages:**
1. Builder Prospect Identified
2. Initial Meeting Booked
3. Meeting Completed — Relationship Established
4. First Project Quoted
5. First Project Won
6. Active Relationship (ongoing work)
7. Preferred Supplier Designation
8. Lost to Competitor (with re-engagement at 90 days)

**Key Custom Fields:**
- Company name and primary contact
- Number of annual builds
- Current insulation supplier
- Spec requirements (R-24 walls / R-60 attic / code minimum)
- Payment terms (30/60/net)
- Preferred product brands

### 3.5 Pipeline 5 — Rebate-Driven Lead

Leads who found the contractor specifically through government rebate research. Require different handling — they're educated, motivated, but often confused about process.

**Stages:**
1. Rebate Lead — Program Identified
2. EnerGuide Audit Required — Referral Sent
3. Audit Completed — Pre-Approval Received
4. Scope of Work Finalized
5. Pre-Approved Work Quote Sent
6. Approved — Deposit Received
7. Work Completed
8. Post-Work Documentation Package Sent to Client
9. Rebate Submitted (client-side)
10. Rebate Received — Follow-Up
11. Review / Referral
12. Closed Won

**Key Custom Fields:**
- Rebate program (Canada Greener Homes / Enbridge HER+ / BC Hydro / Hydro Québec / Municipal)
- Energy advisor name + license number
- Pre-approval reference number
- Maximum rebate eligible amount
- Pre-work EnerGuide score
- Post-work EnerGuide score (after completion)
- Rebate submitted date
- Rebate received date

### 3.6 Pipeline 6 — Commercial / ICI

Separate track for commercial buildings, multi-res, and industrial.

**Stages:**
1. New Commercial Lead
2. RFQ / Tender Identified
3. Site Visit / Bid Meeting
4. Bid Submitted
5. Awaiting Award
6. Award — Contract Execution
7. Project Active
8. Project Complete — Deficiencies Cleared
9. Invoice Issued
10. Payment Received
11. Relationship Maintained

---

## SECTION 4: WORKFLOW ARCHITECTURE

### 4.1 Speed-to-Lead Workflow

**Trigger:** New lead submitted via any source (web form, Facebook lead ad, Google LSA, phone call missed)

**Sequence:**
- **0 minutes:** Instant SMS — "Hi [Name], this is [Business]. We got your request! We do free energy assessments for attic insulation and can often get out within 48 hours. What's a good time? Reply here or call us at [number]."
- **0 minutes:** Assign to rep + create task "Call new lead within 5 minutes"
- **5 minutes:** If no SMS reply, trigger follow-up call task notification
- **1 hour:** If no contact made, second SMS — "We want to make sure we connect! Did you want us to reach out in the morning instead? Just reply YES."
- **4 hours:** If still no contact, email with booking link + rebate overview PDF attachment
- **Next business day:** Final auto-outreach SMS — "Last attempt — wanted to make sure you didn't miss out on booking your free home energy assessment. Reply STOP to opt out."

**Lead source tagging:**
- Google LSA → Tag "LSA" → Priority routing (LSA leads are high intent, must respond in 5 min)
- Facebook Lead Ad → Tag "FB Cold" → Standard speed-to-lead (30-min acceptable)
- Referral → Tag "Referral [Source]" → Warm welcome workflow variant
- Energy Auditor Referral → Tag "Auditor Referral" → Rebate pipeline route

### 4.2 Free Energy Assessment Booking Confirmation Workflow

**Trigger:** Appointment booked via calendar (Free Energy Assessment)

**Sequence:**
- **Immediately:** Booking confirmation email with:
  - Appointment details
  - What to expect (10–15 min walkthrough, no obligation)
  - Prep instructions (access to attic, note current energy bills)
  - Link to rebate info page
- **Immediately:** SMS confirmation — "Your free energy assessment is confirmed for [Date/Time]. Our assessor [Name] will arrive in a [Colour] truck. Any questions? Reply here."
- **24 hours before:** Email reminder with "What we'll check during your visit" (thermal bridge points, attic hatch, existing R-value)
- **2 hours before:** SMS reminder — "See you in 2 hours! [Tech name] will be there. If you need to reschedule, reply CHANGE."
- **1 hour after no-show:** SMS — "We missed you today! Did something come up? We can rebook for [Next Available Slot]. Reply here."
- **Post-visit trigger (manual):** Rep marks appointment complete → triggers Quote Follow-Up workflow

### 4.3 Rebate Education Sequence

**Trigger:** Lead tagged with any rebate program interest OR lead enters Rebate Pipeline

**Sequence (email + SMS hybrid):**

- **Day 0 (immediately):** Email — "Your Guide to Getting Paid to Insulate"
  - Subject: "You could get up to $5,000 back — here's how it works"
  - Body: Plain-language breakdown of Canada Greener Homes / Enbridge HER+, what's eligible, the energy audit requirement, and timeline
  - CTA: Book Free Assessment (we handle the paperwork)

- **Day 2:** SMS — "Did you get our rebate guide? The Enbridge Home Efficiency Rebate is live right now and has a limited budget. Worth booking your assessment soon — it only takes 30 min. [Link]"

- **Day 4:** Email — "The #1 mistake people make with the Canada Greener Homes rebate"
  - Body: Explains that work must be pre-approved BEFORE it starts (common mistake that disqualifies homeowners), positions contractor as the expert guide

- **Day 7:** Email + SMS — "How much could YOU save? Let's calculate it."
  - Include an ROI calculator link or image showing: average energy savings (15–25% on heating bills), average rebate amount ($1,500–$5,600), average payback period (3–7 years for attic insulation)

- **Day 14:** Email — "What happens after we insulate? Real customer results."
  - Testimonial format: before/after energy bill, R-value before/after, rebate received, satisfaction quote

- **Day 21:** SMS — "One last thing about the rebate — [Name], the program funding gets used up seasonally. Families who book early lock in their spot. Would you like to move forward? [Book Link]"

- **Day 30:** Email — "Checking in — did you get your questions answered?"
  - Soft ask with direct phone number + booking link

### 4.4 Estimate Follow-Up Sequence

**Trigger:** Quote marked "Sent" in CRM

**Sequence:**
- **Day 1:** Email — "Your [Property Address] Insulation Estimate — Reference #[Job#]"
  - Attach PDF quote
  - Include 3 key benefits and ROI summary
  - CTA: "Questions? Call or text [number]"

- **Day 2:** SMS — "Hi [Name], just wanted to make sure you received your estimate! Any questions on the R-value recommendation or the rebate eligibility? Happy to chat."

- **Day 4:** Email — "Something most homeowners don't know about their attic..."
  - Educational content: how thermal bridging over joists can reduce effective R-value by 10–15%, why R-60 is the sweet spot for Ontario, why blown-in is better than batts for existing attics
  - CTA: "Your estimate already accounts for this — want to review it together?"

- **Day 7:** SMS — "Hi [Name] — our schedule fills up fast going into the heating season. Just checking in on your estimate. Still interested? Reply YES and I'll reach out."

- **Day 10:** Email — "[Name], we're holding your spot — but not for much longer"
  - Creates urgency around booking window
  - Includes link to accept estimate or request a call

- **Day 21:** SMS — "It's been a few weeks. [Name], are you still looking at upgrading your attic insulation this season? We have some openings and can often get you in within the week."

- **Day 30:** Email — "Last follow-up from [Business Name]"
  - Low-pressure, clear CTA
  - Option to opt out or "not right now — contact me in 3 months"
  - If "not right now" — move to 90-day re-engage trigger

### 4.5 Post-Install Review & Referral Campaign

**Trigger:** Job marked "Complete" in CRM

**Sequence:**
- **Day 1:** Email — "Your insulation is done! Here's what we did."
  - Summary of work (R-value installed, areas covered, products used)
  - Rebate documentation attached (if applicable)
  - Link to submit Google review
  - Subject: "Your attic is now at R-[X] — what happens next"

- **Day 2:** SMS — "Hi [Name], hope you're already noticing the difference! We'd love a quick Google review — it takes 60 seconds and helps families like yours find us. [Direct Google Review Link]"

- **Day 7:** Email — "It's been one week — what do you think?"
  - Ask for honest feedback (2-question form)
  - If positive (4-5 stars) → trigger referral ask
  - If negative (1-3 stars) → trigger service recovery workflow (call owner immediately)

- **Day 14 (referral ask):** SMS — "Hi [Name], glad the job went well! Do you know any neighbours who might benefit? If they book with us, we'll [offer: $50 gift card / 10% referral discount / donate $25 to local charity in their name]. Just reply with their name and number!"

- **Day 14:** Email — "Your neighbours might have the same problem"
  - Subject: "Houses built in [decade] in your area often have the same insulation gaps"
  - Explains that similar vintage homes on the same street share the same insulation shortfalls
  - "Share this with your neighbours" CTA with referral tracking link

- **Day 30:** Email — "Your rebate checklist" (if applicable)
  - Status of rebate submission, documents needed, expected timeline
  - Positions contractor as ongoing support, not just a one-time vendor

### 4.6 Energy Savings ROI Sequence

**Trigger:** Lead at Quote stage with no response after 4 days OR tagged "Price Objection"

**Sequence:**
- **Email 1:** "What does upgrading your insulation actually save you?"
  - ROI table: Cost of upgrade vs annual energy savings vs payback period
  - Example: $4,500 attic job → saves $600–$900/year → payback 5–7 years (+ rebate reduces to 3–4 years)
  - Visual: bar chart showing pre/post energy cost

- **Email 2:** "Why natural gas prices are making insulation more valuable, not less"
  - Position insulation as a hedge against energy cost increases
  - "Every $1 you spend on insulation today is worth more as energy costs rise"

- **SMS (Day 3):** "Hi [Name] — just sent you some numbers on the savings. Want me to walk you through the math quickly? Usually takes 5 min. Reply here."

- **Email 3:** "What a customer in [City/Neighbourhood] saved last winter"
  - Testimonial-style case study with real numbers
  - Before: R-12 attic, $280/month winter heating bill
  - After: R-60 attic, $195/month — saved $85/month = $1,020/year
  - Plus $2,500 Enbridge rebate = paid back in 2 years

### 4.7 Neighbour Referral Campaign

**Trigger:** 14 days post-install + Positive review confirmed

**Sequence:**
- **Week 2:** SMS to client — "Since we were in your neighbourhood, we're offering [discount/gift] to any neighbours you send our way. Know anyone?"
- **Week 3:** Client receives referral cards (physical) + digital referral link
- **Parallel:** Geo-targeted Facebook ad to same postal code with creative like "We just upgraded your neighbour's attic — is yours next?"
- **30-Day follow-up:** SMS to client — "Has anyone taken you up on the referral? We've been getting calls from [Street Name] area lately. Enjoy your lower bills!"

### 4.8 New Construction Builder Workflow

**Trigger:** New builder contact added to Builder Pipeline

**Sequence:**
- **Day 0:** Welcome email with company overview, product specs, and case studies
- **Day 3:** SMS — "Hi [Contact], this is [Rep] from [Company]. We specialise in insulation packages for new construction — is it worth a quick 15-minute call to see if we can save you time on your next project?"
- **Day 7:** Email — "Insulation spec sheet + NBC 2020 compliance guide for [Province]"
  - Position as resource, not sales pitch
- **Day 14:** Follow-up call task created in CRM
- **Day 30:** Email — "Our availability for Q[X] new construction — are you planning any starts?"
- **Day 45:** Task — "Personal follow-up call to check in on pipeline"
- **Quarterly:** Newsletter — new products, rebate program updates, code changes

---

## SECTION 5: LEAD SOURCES & ROUTING

### 5.1 Google Local Services Ads (LSA)

- **Volume potential:** High — insulation is a searched-for service, especially in peak season
- **Lead quality:** Very high — intent-based, already looking for an insulation contractor
- **Critical requirement:** 5-minute response time (LSA penalizes slow responders)
- **GHL setup:** Dedicated webhook + Zapier/Make integration → instant lead → Speed-to-Lead Workflow fires immediately
- **Custom tag:** "LSA" — triggers LSA priority lane in pipeline
- **Tip for contractors:** Enable Google Guaranteed badge — massive conversion lift

### 5.2 Government Rebate Programs (Canada Greener Homes / Enbridge HER+)

**Canada Greener Homes Grant/Loan:**
- Federal program — up to $5,600 in grants for qualifying upgrades
- Requires pre- and post-retrofit EnerGuide energy audit
- Eligible upgrades include attic insulation, basement insulation, air sealing
- Program has had funding pauses — contractor must stay current
- **GHL opportunity:** Build a "Rebate Qualification" landing page / chatbot funnel that qualifies leads and books the energy assessment — this is a top-of-funnel lead magnet

**Enbridge Home Efficiency Rebate Plus (Ontario):**
- Up to $10,000 in incentives for Ontario homeowners with Enbridge gas
- Insulation upgrades are a major eligible category
- Works alongside Canada Greener Homes (can stack programs)
- **GHL opportunity:** Facebook ads targeting Ontario Enbridge customers with "Get up to $10,000 to insulate your home" — extremely high CTR in market testing

**Hydro Québec / BC Hydro:**
- Province-specific programs with similar structure
- Tailor landing pages and ad creative per province

**Setup in GHL:**
- Create separate landing page per rebate program
- Form captures: postal code, home type, current heating fuel, current insulation state
- Webhook → CRM → Rebate Pipeline → Rebate Education Sequence fires

### 5.3 Energy Auditors / EnerGuide Advisors

One of the most underutilized lead sources. Energy advisors who complete EnerGuide audits regularly see insulation that needs upgrading. A formal referral partnership with 2–3 local energy advisors can generate 5–15 qualified leads per month.

**GHL Setup:**
- Create B2B contact record for each energy advisor
- Track referrals from each advisor with custom tag "Auditor Ref — [Name]"
- Monthly report to each advisor showing referrals sent + jobs completed
- Referral fee or reciprocal referral (contractor sends clients needing audits back to advisor)

### 5.4 Real Estate Agents

Buyers of older homes (pre-1980) often need insulation upgrades. Agents who know their clients will need this service can be a consistent referral source.

**GHL Setup:**
- Separate B2B pipeline for Realtor relationships
- Monthly email to Realtor contacts: "Is your next listing ready for inspection? Attic insulation is one of the top items flagged in home inspections. We offer priority booking for Realtor referrals."
- After every Realtor-referred job: thank-you email with referral tracking + offer

### 5.5 Facebook / Meta Ads

**Audiences that convert for insulation:**
- Homeowners 35–65, Ontario / BC / Alberta, own their home
- Lookalike audiences based on past customers
- Retargeting website visitors (Facebook Pixel on all GHL landing pages)
- Seasonal: September–November targeting cold + energy cost anxiety

**Top-performing creative concepts:**
- "Your attic is losing $[X] every month" (curiosity hook)
- "Government is paying up to $5,600 to insulate Ontario homes — does your home qualify?"
- Before/after thermal imaging (infrared shows heat loss — visually compelling)
- "Your neighbours at [Neighbourhood] just upgraded — see what they saved"

**GHL Facebook Lead Ad Integration:**
- Native integration pulls leads directly into GHL
- Assign to Rebate Pipeline if rebate ad → fires Rebate Education Sequence
- Assign to Attic Pipeline if generic ad → fires Speed-to-Lead Workflow

### 5.6 Referrals (Existing Customers)

Tracked as a formal channel in GHL:
- Custom tag "Referred by [Contact Name]"
- Source field: "Customer Referral"
- Auto-trigger "referrer thank-you" SMS when referral closes

---

## SECTION 6: SMS/EMAIL TEMPLATES

### 6.1 Rebate Education Templates

**SMS — Rebate Awareness (Cold Lead):**
```
Hi [Name], this is [Business]. Did you know the Enbridge Home Efficiency Rebate is offering up to $10,000 for Ontario homeowners who upgrade their insulation? 

We handle everything — the paperwork, the audit coordination, the whole process. 

Want a free 15-min assessment to see if you qualify? [Booking Link]
```

**SMS — Rebate Urgency (Warm Lead — 7 days no response):**
```
[Name] — quick note on the rebate. Program budgets do run out seasonally, and we're heading into fall booking season. We'd hate for you to miss it. 

Can we get 15 minutes on the calendar this week? [Link]
```

**Email — Rebate Guide (Subject: "How to get up to $5,600 back on your insulation upgrade"):**
```
Hi [Name],

The Canada Greener Homes program and Enbridge HER+ can cover a significant portion of your insulation upgrade — but there are rules, and most homeowners don't know them until it's too late.

Here's what you need to know:

1. THE AUDIT COMES FIRST
You need an EnerGuide energy audit BEFORE the work starts. We can refer you to a certified energy advisor — or if you've already had one, we can start right away.

2. THE MINIMUM R-VALUE MATTERS
To qualify for maximum rebates, your attic needs to reach at least R-50 or R-60 (we recommend R-60 for Ontario winters). We'll confirm your current R-value during our free assessment.

3. THE REBATE TIMELINE
After the work is complete, you submit your application and typically receive payment within 8–20 weeks. We provide all the documentation you'll need.

We've walked dozens of families through this process. It's not complicated when you have someone who knows the system.

[BOOK YOUR FREE ASSESSMENT — WE'LL EXPLAIN THE WHOLE THING]

Warm regards,
[Rep Name]
[Business Name]
```

### 6.2 Energy Savings Hook Templates

**SMS — Energy Savings Hook:**
```
Hi [Name], most attics in homes built before 1990 are running at R-12 or less. The recommended level for Ontario is R-60. That gap can cost $600–$1,200 a year in heating. 

We can check your attic for free — no sales pressure. Want to book a quick visit? [Link]
```

**Email — "What does R-60 actually mean?" Subject: "The number on your attic that's costing you money":**
```
Hi [Name],

R-value measures how well your insulation resists heat transfer. The higher the number, the better the protection.

Here's the problem: most homes built before 1990 have R-12 to R-20 in the attic. Ontario building code now requires R-60 for new construction. That gap is costing you money every single month.

Quick math:
- Upgrading from R-20 to R-60: average cost $3,500–$5,500
- Average annual heating savings: $600–$900/year
- Canada Greener Homes rebate: up to $2,500
- Enbridge HER+ rebate: up to $2,000

Net cost after rebates: often under $2,000
Payback period: 2–4 years
Benefit: 20+ years of lower energy bills and a more comfortable home

[Book your free attic assessment — we check your current R-value at no charge]
```

### 6.3 Estimate Follow-Up Templates

**SMS — Day 2 Estimate Follow-Up:**
```
Hi [Name], just checking in on the estimate we sent for [property/service]. Any questions on the R-value recommendation or the Enbridge rebate option? Happy to jump on a 5-min call. — [Rep Name]
```

**SMS — Day 7 Re-Engagement:**
```
[Name] — our fall schedule is filling up. We're still holding a spot for you, but don't want you to lose it to another booking. Want to lock it in? Just reply YES and I'll get you confirmed. 🏠
```

**Email — Stalled Estimate Re-Engagement (Subject: "We're holding your spot — but not much longer"):**
```
Hi [Name],

It's been [X] days since we sent over your estimate. We get it — it's a big decision and timing matters.

But we wanted to give you a heads up: our October/November schedule is booking up, and families who wait often end up doing the job in February (which means a cold winter in between).

Three things that might help you decide:

✅ The Enbridge HER+ rebate is still active — we can confirm your eligibility during the booking call
✅ We offer a 10-day payment window after job completion  
✅ We warranty all our work for [X] years

[Ready to book? Click here to confirm your spot] or [Want to ask a question? Reply to this email]

No pressure — we just want to make sure you're taken care of before the season rush.

[Signature]
```

### 6.4 Post-Install Review Request Templates

**SMS — Review Request (Day 2):**
```
Hi [Name]! It was great working on your home. If you're happy with the job, a quick Google review would mean the world to us — it's how other families find us. 

Takes 60 seconds: [Direct Google Review Link]

Thanks so much! — [Tech Name] & the [Business] team
```

**Email — Review Request (Subject: "How did we do?"):**
```
Hi [Name],

Your attic is now insulated to R-[X] — a big upgrade from where you started.

We pride ourselves on getting it right, and we'd love to know how we did. 

Would you mind leaving us a quick Google review? It helps other homeowners in [City] find us when they're facing the same heating costs you were.

[Leave a Review on Google] ← takes 60 seconds

And if anything wasn't perfect — reply to this email. We want to make it right.

Thanks for trusting us with your home.
[Signature]
```

---

## SECTION 7: BOOKING FLOW ARCHITECTURE

### 7.1 Primary Booking CTA

**Name:** Free Home Energy Assessment (Attic Inspection Included)  
**Duration:** 30 minutes  
**What happens:**
- Tech visits the property
- Checks existing attic/basement insulation R-value
- Identifies air sealing gaps, thermal bridging risks
- Checks attic hatch (common heat loss point)
- Reviews rebate eligibility with homeowner
- Provides ballpark on-site OR follows up with formal quote within 24 hours

**Why this CTA wins vs "Free Quote":**
- "Free energy assessment" feels like professional service, not sales visit
- Ties directly into Canada Greener Homes language (EnerGuide assessment = same language)
- Positions contractor as advisor, not commodity
- Rebate mention is built into the CTA — attracts rebate-motivated buyers

### 7.2 Booking Form Fields

Required:
- First Name, Last Name
- Email, Phone
- Property Address (used for geo-targeting later)
- Home Type: Detached / Semi / Townhome / Condo / Other
- Year Built (dropdown: pre-1960 / 1960–1979 / 1980–1999 / 2000+)
- Current Concern: High Energy Bills / Drafts & Cold Spots / Planning Renovation / Government Rebate / Selling Home / Other
- Preferred Appointment Day/Time

Optional (increases data quality):
- Current Heating Fuel (Natural Gas / Electric / Oil / Propane / Other)
- Current Attic Insulation (Unknown / Fibreglass Batts / Blown-In / Spray Foam / None)
- How Did You Hear About Us (Google / Facebook / Referral / Enbridge / Other)

**Form Thank You Page:**
- Confirm appointment time
- Set expectations (tech name, arrival window, what they'll bring)
- Link to "What to expect" video or page
- Rebate guide download (PDF)

### 7.3 Calendar Settings

- **Buffer time:** 30 minutes between appointments (drive time + setup)
- **Max daily bookings:** Tied to crew count (typically 4–6 per day per crew)
- **Advance booking window:** 2–14 days (prevents long-lead bookings that lose interest)
- **Reminder sequence:** 24-hour email + 2-hour SMS (auto-fires from calendar workflow)
- **No-show protocol:** Auto-SMS 30 min after missed start time

---

## SECTION 8: GOVERNMENT REBATE CAMPAIGN BUILD

### 8.1 Campaign Architecture

The rebate campaign is the single highest-leverage marketing asset in the snapshot. It works because:

1. Government money removes price objection
2. "Up to $10,000" is a pattern-interrupting headline
3. It positions the contractor as a specialist (not just another insulation guy)
4. It creates urgency — rebate programs have budget limits

**Campaign Components:**
- Dedicated landing page (not the homepage)
- Facebook/Instagram ad set (rebate-specific creative)
- Google Search campaign (keywords: "Enbridge insulation rebate," "Canada Greener Homes contractor," "insulation rebate Ontario")
- Rebate-specific form + pipeline routing
- Rebate Education Sequence (see Section 4.3)

### 8.2 Landing Page Structure

**Headline:** "Get Up to $10,000 Back to Insulate Your [Province] Home — Here's How"  
**Sub-headline:** "The Enbridge Home Efficiency Rebate + Canada Greener Homes Loan are live. We handle the process. You collect the cheque."

**Section 1 — The Opportunity (pain + promise)**
- Explain the programs briefly
- Call out the fear: "Most homeowners lose the rebate because they start the work before getting pre-approval. Don't make that mistake."

**Section 2 — The Process (overcome complexity objection)**
- 3-step visual: Get Your Assessment → We Handle the Paperwork → Collect Your Rebate
- Positions contractor as the expert guide

**Section 3 — Proof (trust)**
- 3 customer testimonials with rebate amounts received
- Google review badge
- BBB / TECA / provincial insulation association logo

**Section 4 — Urgency**
- "Rebate budgets are allocated seasonally. Spots are limited for [Season]."

**Section 5 — CTA**
- Form: "Check if your home qualifies — free, takes 2 minutes"
- Or direct booking CTA: "Book Your Free Assessment"

### 8.3 Ad Creative Library (Facebook)

**Ad 1 — Rebate Hook (Cold Traffic):**
- Visual: Screenshot of a rebate cheque or dollar amount
- Headline: "Ontario homeowners: the government will pay you to insulate your home"
- Body: "$10,000 in available rebates. We handle the paperwork. You collect the cash. Book your free assessment → [Link]"

**Ad 2 — Fear/Problem (Cold Traffic):**
- Visual: Thermal image showing heat escaping through attic
- Headline: "Your attic is costing you $800/year. Here's the fix."
- Body: "Most Ontario homes built before 1990 are under-insulated. With current government rebates, upgrading is often under $1,500 out of pocket. Free assessment → [Link]"

**Ad 3 — Social Proof (Warm Retargeting):**
- Visual: Before/after energy bill or customer photo
- Headline: "[City] families are saving $700/year on heating — here's what they did"
- Body: "Our customers in [Neighbourhood] upgraded their attic insulation last fall and qualified for the Enbridge rebate. See what they paid (and what they got back). → [Link]"

**Ad 4 — Urgency (Retargeting):**
- Headline: "The rebate program has a deadline — did you book yours?"
- Body: "Hi [Name], we noticed you checked out the rebate guide. Fall booking season fills up fast. We still have slots this week → [Link]"

---

## SECTION 9: ENERGY SAVINGS ROI SEQUENCE (DETAILED)

### 9.1 The Payback Period Framework

The #1 price objection in insulation is: "That's a lot of money." The response that closes it is always ROI.

**Standard ROI Script (for reps + automated email sequence):**

```
Average attic insulation upgrade (from R-12 to R-60): $3,500–$5,500

Annual heating savings:
- Heating 2,000 sq ft home in Ontario with natural gas
- Before: $2,400/year
- After (R-60): $1,700/year
- Annual savings: $700/year

Rebates available:
- Canada Greener Homes Loan: interest-free up to $40,000 (no out-of-pocket)
- Enbridge HER+: up to $2,000 grant
- Net cost: often $1,500–$2,000 out of pocket

Payback period:
- Without rebates: 5–8 years
- With rebates: 2–4 years

Beyond payback:
- 20+ more years of savings
- Increased home resale value
- Improved comfort (no more cold spots)
- Reduced carbon footprint (Climate bonus)
```

### 9.2 ROI Sequence Email Templates

**Email 1 — The Math (Subject: "What $4,000 of insulation is actually worth")**

See template in Section 6.2 above.

**Email 2 — The Rising Energy Cost Angle (Subject: "Natural gas prices aren't going down — here's your hedge")**
```
Hi [Name],

Energy costs have increased significantly over the last 5 years, and forecasters don't expect that to reverse.

Here's the thing about insulation: every dollar you invest today locks in a return that gets *more* valuable as energy costs rise.

If your heating bill is $2,500/year today and you save 25% with an attic upgrade, that's $625/year.
In 5 years, if energy costs are 20% higher, you're saving $750/year on the same upgrade.

The investment goes up in value as time goes on. Very few home improvements can say that.

[See your personalized savings estimate → Book Free Assessment]
```

**Email 3 — The Comfort Angle (Subject: "Your family deserves a home that isn't drafty in February")**
```
Hi [Name],

Energy savings are great — but sometimes the best part of upgrading insulation isn't the money.

It's not waking up to a cold bedroom in January.
It's not noticing the floor is warm in the morning.
It's not arguing about the thermostat anymore.

The R-value does more than save money — it changes how your home feels. And it does it year-round: same insulation that keeps heat in during winter keeps it out during summer.

Our customers regularly tell us the comfort difference was immediate and noticeable.

[Book your free assessment and feel the difference this season]
```

---

## SECTION 10: REFERRAL CAMPAIGN ARCHITECTURE

### 10.1 The Neighbour Strategy

Insulation companies have a unique geographic advantage: **houses built in the same era, on the same street, have the same problems.** A street of 1970s split-levels all have the same R-12 attic and the same energy bill problem.

**Campaign Flow:**
1. Job completed on [Street Name]
2. 14 days post-install: client gets referral SMS + email
3. Parallel: Geo-targeted Facebook ad to same postal code
4. Optional: door hanger/mail drop to adjacent properties (offline complement)
5. Any referral lead → tagged "Neighbour Referral" → boosted response time (warmest leads)

### 10.2 Referral Templates

**SMS to Client (Day 14):**
```
Hi [Name]! Hope you're loving the warmer house already. 🏠

Quick favour — do you know any neighbours who might have the same drafty attic problem? If you send us their info and they book a job, we'll send you a $75 gift card as a thank-you.

Just reply with their name and number. That's it!
```

**Email to Client (Subject: "Your neighbours might have the same problem you did"):**
```
Hi [Name],

You made a smart call upgrading your insulation this fall. Based on when your neighbourhood was built, there's a good chance your neighbours are losing just as much heat — and paying for it every month.

If you share our info with a neighbour and they book a job, we'll send you a $75 Tim Hortons gift card as our thank-you. 

Here's a message you can forward: 
---
"Hey! We just had [Business] insulate our attic and it's made a huge difference. They're doing the [Neighbourhood] area right now — they have a government rebate promotion going on and I thought you might want to check it out. [Referral Link]"
---

Thanks again for trusting us. Enjoy the warmth!
[Signature]
```

### 10.3 B2B Referral Network

**Energy Auditors/Advisors:**
- When auditor completes EnerGuide audit → they often see inadequate insulation
- Referral arrangement: auditor refers for insulation; contractor refers clients needing audits back
- Track in GHL: B2B contact record + referral source tag on all incoming leads

**Real Estate Agents:**
- Home inspection flags insulation issues → agent refers to insulation contractor
- Monthly touchpoint: "Inspection season is busy — we're offering priority booking for your clients"

**General Contractors/Renovators:**
- GC doing basement finish → subcontract insulation
- GC doing attic conversion → need spray foam
- Maintain in Builder Pipeline with regular outreach

---

## SECTION 11: WHAT MAKES THIS SNAPSHOT STAND OUT

### 11.1 Feature Differentiation vs Existing Snapshots

| Feature | Generic Home Services Snapshot | 1app Insulation Snapshot |
|---|---|---|
| Industry-specific pipelines | ❌ 1 generic pipeline | ✅ 6 pipelines (attic/basement/spray foam/new build/rebate/commercial) |
| Rebate workflow | ❌ None | ✅ Full rebate education + EnerGuide coordination workflow |
| Speed-to-lead | ⚠️ Basic | ✅ 5-stage speed-to-lead with LSA priority routing |
| Seasonal campaigns | ❌ None | ✅ Pre-season booking campaign + off-season new construction fill |
| Post-install nurture | ❌ Minimal | ✅ Review → Referral → Neighbour campaign chain |
| B2B builder track | ❌ None | ✅ Dedicated builder/GC pipeline with quarterly outreach |
| ROI/objection sequences | ❌ None | ✅ Energy savings ROI sequence + payback period calculator |
| Industry language | ❌ Generic | ✅ R-value, blown-in, batt, spray foam, air sealing, thermal bridging |
| Energy auditor integration | ❌ None | ✅ Auditor referral tracking + reciprocal referral system |
| Neighbour campaign | ❌ None | ✅ Post-install geo-targeted neighbour referral engine |

### 11.2 The 1app Advantage

The 1app snapshot adds three layers no other snapshot provides:

**Layer 1: Rebate Intelligence Engine**
No contractor in the market has automated rebate education built into their CRM. The first company to show up in a homeowner's inbox saying "here's exactly how the Enbridge rebate works and how we handle it" wins the job. This is the single highest-converting angle in Canadian insulation marketing.

**Layer 2: Multi-Pipeline Reality**
A spray foam contractor doing new construction has a completely different workflow than a blown-in residential company. Forcing both into one generic pipeline creates chaos. Separate pipelines with appropriate stages, custom fields, and workflows means each job type is managed correctly.

**Layer 3: The Neighbour Referral Engine**
The post-install referral sequence combined with geo-targeted Facebook ads targeting the same postal code creates a compounding local market penetration effect. Every job generates neighbour leads. Within 18 months of using this system consistently, a contractor can dominate their local market neighbourhood by neighbourhood.

---

## SECTION 12: TECHNICAL BUILD CHECKLIST

### 12.1 Pipelines
- [ ] Pipeline 1: Residential Attic Upgrade (13 stages)
- [ ] Pipeline 2: Basement & Crawlspace (11 stages)
- [ ] Pipeline 3: Spray Foam (13 stages)
- [ ] Pipeline 4: New Construction Builder (8 stages)
- [ ] Pipeline 5: Rebate-Driven Lead (12 stages)
- [ ] Pipeline 6: Commercial/ICI (11 stages)

### 12.2 Workflows
- [ ] Speed-to-Lead (5-step, multi-channel)
- [ ] Assessment Booking Confirmation (6-step)
- [ ] Rebate Education Sequence (7-step, 30-day)
- [ ] Estimate Follow-Up (6-step, 30-day)
- [ ] Post-Install Review + Referral Chain
- [ ] Energy Savings ROI Sequence (3-email + SMS)
- [ ] Neighbour Referral Campaign
- [ ] Builder/GC Nurture Sequence
- [ ] Stalled Estimate Re-Engagement (90-day trigger)
- [ ] Service Recovery (negative review trigger)
- [ ] No-Show Re-Book workflow
- [ ] Seasonal Pre-Campaign trigger (late August/September auto-fire)

### 12.3 Forms & Landing Pages
- [ ] Free Energy Assessment booking form (full field set)
- [ ] Rebate Qualification form (program-specific)
- [ ] Rebate Landing Page (separate from homepage)
- [ ] Referral Submission form
- [ ] Post-Install Feedback form (2-question NPS trigger)

### 12.4 Calendars
- [ ] Free Energy Assessment (30-min)
- [ ] Discovery Call (15-min — for commercial/B2B)
- [ ] Builder Meeting (60-min)

### 12.5 Custom Fields (Global)
- [ ] Property Type
- [ ] Year Built
- [ ] Heating Fuel
- [ ] Current Attic R-Value
- [ ] Target R-Value
- [ ] Square Footage
- [ ] Rebate Program Interest
- [ ] EnerGuide Audit Status
- [ ] Energy Advisor Name
- [ ] Quote Amount
- [ ] Rebate Amount Eligible
- [ ] Install Date
- [ ] Post-Install R-Value
- [ ] Review Link Sent (Y/N)
- [ ] Referral Sent (Y/N)

### 12.6 Tags (Standard Set)
- [ ] LSA / Facebook / Google Organic / Referral / Enbridge / Auditor Referral / Builder
- [ ] Attic / Basement / Spray Foam / New Construction / Commercial
- [ ] Rebate Interested / EnerGuide Needed / EnerGuide Complete
- [ ] Review Requested / Review Received / Referral Made
- [ ] Price Objection / Stalled / Re-Engage Q[X]

### 12.7 Email Templates (Built In CRM)
- [ ] Speed-to-Lead Sequence (5 emails/SMS)
- [ ] Assessment Booking Confirmation + Reminders
- [ ] Rebate Education Sequence (7 emails/SMS)
- [ ] Estimate Follow-Up Sequence (6 emails/SMS)
- [ ] Post-Install Review Request (2 emails + 2 SMS)
- [ ] Referral Request (1 email + 1 SMS)
- [ ] Neighbour Campaign (email + SMS)
- [ ] ROI Sequence (3 emails + 1 SMS)
- [ ] Builder Nurture Sequence (quarterly email)
- [ ] Service Recovery (1 internal alert + 1 client email)

### 12.8 Reporting Dashboards
- [ ] Lead source performance (LSA vs Facebook vs Referral vs Organic)
- [ ] Pipeline velocity by job type
- [ ] Quote-to-close rate by rep
- [ ] Average job value by job type
- [ ] Review acquisition rate
- [ ] Referral conversion rate
- [ ] Rebate-driven lead conversion rate
- [ ] Seasonal booking trends

---

## SECTION 13: PRICING & POSITIONING RECOMMENDATIONS FOR 1APP

### 13.1 Recommended Pricing Tier

**1app Insulation Pro Package**
- **Monthly:** $397–$597 CAD/month
- **Onboarding:** $997–$1,497 one-time setup fee
- **Justification:** A single attic job is $3,500–$7,000. If the system books 2 extra jobs per month (extremely achievable), ROI is 10–20x. Price accordingly.

**What's included:**
- Snapshot install + full configuration
- Lead source integrations (LSA, Facebook)
- 30-day onboarding call series (3 calls)
- Monthly check-in support
- Quarterly rebate program updates (keep the system current as programs change)

### 13.2 The Sales Pitch for This Snapshot

> "Most insulation contractors lose half their leads in the first hour because they're busy on jobs and can't call back fast enough. Our system responds instantly, educates your prospect on the rebates they qualify for, and follows up automatically until they book — so you're focused on jobs, not chasing your phone. We've built this specifically for insulation companies in Canada. It understands R-values, blown-in, spray foam, Enbridge rebates, and Canada Greener Homes. This isn't a generic CRM — it's a complete insulation marketing system."

---

## APPENDIX A: INDUSTRY TERMINOLOGY GLOSSARY

| Term | Definition |
|---|---|
| **R-value** | Measure of thermal resistance. Higher = better insulation. Ontario attic code: R-60 |
| **Blown-in (loose-fill)** | Cellulose or fibreglass insulation blown into attic spaces using a machine. Most common attic upgrade method |
| **Batt insulation** | Pre-cut fibreglass or mineral wool panels installed between studs/joists |
| **Open-cell spray foam** | 0.5 lb/ft³ density. Permeable to moisture vapour. R-3.5–4 per inch. Lower cost |
| **Closed-cell spray foam** | 2 lb/ft³ density. Acts as vapour barrier. R-6–7 per inch. Higher cost. Superior performance |
| **Vapour barrier** | Material (6-mil poly, rigid foam, closed-cell spray foam) that prevents moisture migration |
| **Air sealing** | Sealing gaps, penetrations, and cracks before insulating. Critical for actual thermal performance |
| **Thermal bridging** | Heat loss through structural members (joists, studs) that bypasses insulation |
| **Attic hatch** | The access point to the attic. One of the most common and overlooked heat loss points |
| **EnerGuide audit** | Home energy audit performed by certified NRCan energy advisor. Required for government rebates |
| **Canada Greener Homes** | Federal program offering grants + interest-free loans for qualifying energy retrofits |
| **Enbridge HER+** | Ontario program offering up to $10,000 in incentives for Enbridge gas customers |
| **Energy advisor** | NRCan-certified professional who conducts EnerGuide audits and recommends upgrades |
| **Payback period** | Years until energy savings equal the cost of upgrade |
| **NBC 2020** | National Building Code of Canada 2020 — sets minimum insulation requirements for new construction |
| **TECA** | Thermal Environmental Comfort Association — Canadian insulation industry body |
| **ICF** | Insulated Concrete Form — foundation system with insulation built in |
| **Cellulose** | Recycled paper fibre used in blown-in insulation. Good R-value, excellent air resistance |
| **Mineral wool (Rockwool)** | Stone-based insulation. Fire resistant, moisture resistant, excellent acoustic properties |
| **Rimjoist** | Framing at the perimeter of a floor system — major air leakage point, commonly spray-foamed |

---

## APPENDIX B: CANADIAN REBATE PROGRAM QUICK REFERENCE

| Program | Province | Amount | Key Requirement | Status |
|---|---|---|---|---|
| Canada Greener Homes Grant | All | Up to $5,600 | Pre + post EnerGuide audit | Check current status — had pauses in 2024 |
| Canada Greener Homes Loan | All | Up to $40,000 | Pre + post EnerGuide audit | Interest-free repayable loan |
| Enbridge HER+ | Ontario | Up to $10,000 | Enbridge gas customer + pre-approval | Active |
| BC Hydro EV Ready | BC | Varies | BC Hydro customer | Check current offers |
| Hydro Québec rebates | Québec | Varies by upgrade | Hydro Québec customer | Check current offers |
| Ontario Renovates | Ontario | Up to $25,000 | Low-income homeowners | Municipal program |

*Note: Rebate programs change frequently. 1app should build a process to review and update rebate content quarterly.*

---

*Document end. Version 1.0 — July 2026*  
*Research compiled for 1app Technologies Inc. — Insulation Contractor Vertical*  
*Next step: Build snapshot in GHL staging sub-account, test all workflows end-to-end before client delivery*
