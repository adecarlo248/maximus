# Foundation & Waterproofing GHL Snapshot — Build Log
**Sub-account:** Foundation/waterproofing  
**Location ID:** k9EKq8nvSBrYfBEqTcdn  
**Build Date:** 2026-07-21  
**Status:** ✅ COMPLETE — All API-buildable phases done; Workflows documented for manual build  

---

## BUILD SUMMARY

| Phase | Item | Count | Status |
|---|---|---|---|
| Phase 1 | Custom Fields | 20 | ✅ Complete |
| Phase 2 | Pipelines | 4 | ✅ Complete |
| Phase 3 | Calendars | 3 | ✅ Complete |
| Phase 4 | Tags | 32 | ✅ Complete |
| Phase 5 | Workflows (specs documented) | 12 | 📋 Manual Build Required |

---

## PHASE 1: CUSTOM FIELDS ✅

All 20 custom fields created on the `contact` model.

| # | Field Name | Type | ID | Field Key |
|---|---|---|---|---|
| 1 | Lead Source | SINGLE_OPTIONS | gEo1oG4DbTby3ZFEIGQs | contact.lead_source |
| 2 | Job Type | SINGLE_OPTIONS | dGWbM79rXRLWI9v0mD0n | contact.job_type |
| 3 | Service Category | SINGLE_OPTIONS | DP804e1rF461eDw1QgLF | contact.service_category |
| 4 | Property Type | SINGLE_OPTIONS | 4pVpsGU30xKg1nMMjQG7 | contact.property_type |
| 5 | Basement Type | SINGLE_OPTIONS | KLNZ6FGp8ibEnQyHq4lw | contact.basement_type |
| 6 | Water Entry Point | SINGLE_OPTIONS | UMmuZ7snqrGhuMXwJICG | contact.water_entry_point |
| 7 | Severity | SINGLE_OPTIONS | fK3Am1q5Ak86wPBVCqxe | contact.severity |
| 8 | Insurance Claim | RADIO | Qch7OKjo4zKzh0ae9L65 | contact.insurance_claim |
| 9 | Insurance Company | TEXT | pmVa0WoeaFrY3sMk5Dvi | contact.insurance_company |
| 10 | Claim Number | TEXT | enmxQCLT7BBGJBEPWILt | contact.claim_number |
| 11 | Home Inspector Referral | RADIO | 8dFoozQWaUB6OLvfvl9p | contact.home_inspector_referral |
| 12 | Inspector Name | TEXT | 9OYNKUtVQYY2LF0J3W1L | contact.inspector_name |
| 13 | Estimate Amount | MONETORY | wGqQC64DnFsv1F2Sfa7m | contact.estimate_amount |
| 14 | Contract Amount | MONETORY | S9jxhahhqZZUpYDGDl9u | contact.contract_amount |
| 15 | Deposit Paid | RADIO | jx4Vp0ZzhVzBdXIa9jeT | contact.deposit_paid |
| 16 | Financing Required | RADIO | gPAgBFSBrPmPgnXJq9WT | contact.financing_required |
| 17 | Permit Required | RADIO | gTzqVzh3qv9j5dkuZ5wy | contact.permit_required |
| 18 | Permit Number | TEXT | 6wWbyxmSR9X4Q7QE5sel | contact.permit_number |
| 19 | Review Requested | RADIO | 85PYXgDO86IDI3Iwq3xG | contact.review_requested |
| 20 | Review Received | RADIO | 9NRooVLa9NM2dpTtEXnb | contact.review_received |

**Dropdown Options:**

- **Lead Source:** Google LSA, Google Organic, Referral, Home Inspector, Real Estate Agent, Insurance Company, Facebook Ad, Repeat Customer, Property Manager
- **Job Type:** Crack Injection, Interior Waterproofing, Exterior Excavation, Sump Pump Install, Weeping Tile, Window Well, Crawl Space Encapsulation, Underpinning, Helical Pier, Vapour Barrier
- **Service Category:** Crack Repair, Interior Waterproofing, Exterior Waterproofing, Structural, Crawl Space, Commercial
- **Property Type:** Residential, Commercial, Multi-Unit, New Construction
- **Basement Type:** Poured Concrete, Block/Stone, ICF, Crawl Space, Unknown
- **Water Entry Point:** Wall Crack, Floor Crack, Cove Joint, Window Well, Multiple Points, Unknown
- **Severity:** Minor - Seepage, Moderate - Active Leak, Severe - Flooding, Structural Concern, Unknown
- **Insurance Claim (RADIO):** Yes / No
- **Home Inspector Referral (RADIO):** Yes / No
- **Deposit Paid (RADIO):** Yes / No
- **Financing Required (RADIO):** Yes / No
- **Permit Required (RADIO):** Yes / No
- **Review Requested (RADIO):** Yes / No
- **Review Received (RADIO):** Yes / No

---

## PHASE 2: PIPELINES ✅

### Pipeline 1: Foundation - Residential (Main)
**ID:** 6VbWyQXtusuMXBHu2K3l  
**Stages (15):**
1. New Lead
2. Free Inspection Scheduled
3. Inspection Complete
4. Proposal Sent
5. Follow-Up Active
6. Financing Offered
7. Contract Signed / Deposit
8. Permit Applied
9. Work Scheduled
10. Work In Progress
11. Job Complete
12. Invoice Sent
13. Paid
14. Review Requested
15. Referral Ask

---

### Pipeline 2: Foundation - Crack Injection (Fast Track)
**ID:** Jd71Gzsk5p8XYjb5t2Jy  
**Stages (8):**
1. New Lead
2. Quote Sent
3. Follow-Up
4. Repair Scheduled
5. Repair Complete
6. Invoice Sent
7. Paid
8. Review + Upsell

---

### Pipeline 3: Foundation - Commercial
**ID:** qpOcbSWcarE2WrIpEj54  
**Stages (11):**
1. New Prospect
2. Site Assessment
3. Proposal Submitted
4. Contract Awarded
5. Permit Applied
6. Mobilization
7. Work In Progress
8. Job Complete
9. Invoice Sent
10. Paid
11. Warranty Period

---

### Pipeline 4: Foundation - Referral Partners
**ID:** dYKD6q8inm9fPUXbbna3  
**Stages (6):**
1. New Partner
2. Introduction Sent
3. Active Partner
4. Referral Received
5. Referral Converted
6. VIP Partner

---

## PHASE 3: CALENDARS ✅

### Calendar 1: Free Basement Inspection
**ID:** b7Tbk2NEZCK4pGxCy0Ai  
**Duration:** 60 min | **Buffer:** 15 min  
**Availability:** Mon–Fri, 8am–5pm  
**Max per day:** 6  
**Slug:** free-basement-inspection  
**Description:** Free 60-minute basement and foundation inspection. No obligation assessment of your foundation walls, floor, weeping tile, sump pump, and any visible water entry points.

### Calendar 2: Crack Repair Estimate
**ID:** KuleEIxlB8aktimYWegT  
**Duration:** 30 min | **Buffer:** 10 min  
**Availability:** Mon–Fri, 8am–5pm  
**Max per day:** 8  
**Slug:** crack-repair-estimate  
**Description:** Free 30-minute crack repair estimate. Quick assessment and flat-rate quote for foundation cracks. Epoxy and polyurethane injection specialists.

### Calendar 3: Commercial Site Assessment
**ID:** dc41eFOjMYFesntdIvaV  
**Duration:** 90 min | **Buffer:** 15 min  
**Availability:** Mon–Fri, 8am–4pm  
**Max per day:** 3  
**Slug:** commercial-site-assessment  
**Description:** 90-minute commercial site assessment for foundation waterproofing, structural evaluation, and scope development for commercial and multi-unit properties.

---

## PHASE 4: TAGS ✅

All 32 tags created:

`new-lead` | `crack-injection` | `interior-waterproofing` | `exterior-excavation` | `sump-pump` | `weeping-tile` | `window-well` | `crawl-space` | `underpinning` | `helical-pier` | `active-leak` | `structural-concern` | `insurance-claim` | `home-inspector-referral` | `real-estate-referral` | `financing-needed` | `permit-required` | `estimate-sent` | `deposit-paid` | `contract-signed` | `job-complete` | `review-requested` | `review-received` | `referral` | `cold-lead` | `no-show` | `google-lsa` | `facebook-ad` | `repeat-customer` | `property-manager` | `spring-flooding` | `vip-partner`

---

## PHASE 5: WORKFLOWS — FULL SPECS FOR MANUAL BUILD

> **Note:** GHL's API does not support workflow creation. Build these manually in the Workflows section of the sub-account. Each spec below has exact triggers, delays, and copy.

---

### ✅ WORKFLOW 1: Missed Call Text Back — NATIVE GHL SETTING (Not a Workflow)

**Do NOT build this as a workflow.** Use GHL's built-in MCTB feature instead.

**How to enable:**
1. Go to **Settings → Phone Numbers**
2. Click on your phone number
3. Click the **"Voicemail & Missed Call TextBack"** tab
4. Check **"Enable Missed call textback"** ✅
5. Click **"Customize"** and paste the message below

**Customized message for this trade:**
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — wet basement or foundation issue? Reply YES for a free inspection and we'll call you right back 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Lead — Speed to Response

**Trigger:** Contact created OR Opportunity created (in any pipeline)
**Goal:** First contact within 2 minutes, book free inspection  
**Tags to add on trigger:** `new-lead`

**Action 1 — Immediate SMS (0 min):**
> Hi {{contact.firstName}}! It's {{custom_values.owner_name}} from {{custom_values.company_name}} — we received your request about your basement. Water issues can escalate fast, especially this time of year. I'd love to get you a FREE inspection this week — what day works best? Reply here or call {{custom_values.owner_phone}}. We respond 7 days/week.

**Action 2 — Internal Task (2 min):**
> PRIORITY CALL: New lead {{contact.firstName}} {{contact.lastName}} — {{contact.phone}}. They requested basement/foundation help. Call now — speed to lead is critical.

**Action 3 — SMS (1 hour, if no reply):**
> {{contact.firstName}} — just following up. We have inspection slots available tomorrow and Thursday. Unchecked foundation cracks can let in litres of water per day. Takes 30 min and costs nothing. Want to lock in a time? Reply YES and I'll send you options. — {{custom_values.owner_name}}

**Action 4 — Email (3 hours):**  
Subject: Your free basement inspection — we're ready when you are

> Hi {{contact.firstName}},
>
> We received your request and want to make sure we connect with you before your schedule fills up.
>
> Here's what our free inspection covers:
> - Foundation walls (poured concrete, block, or ICF)
> - Floor cracks and cold joints
> - Weeping tile / drainage system condition
> - Sump pump function and capacity
> - Moisture entry points and risk assessment
>
> It takes 30–45 minutes and there's zero obligation.
>
> To book online: {{custom_values.booking_link}}
>
> Or call/text us directly: {{custom_values.owner_phone}}
>
> Water issues don't fix themselves — the sooner we see it, the more options you have.
>
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

**Action 5 — SMS (24 hours):**
> Hey {{contact.firstName}}, still here when you're ready. A lot of our clients say they waited too long — and by then the repair cost doubled. No pressure, just want to make sure your home is protected. Free inspection, 30 minutes. Reply BOOK to schedule. — {{custom_values.company_name}}

**Action 6 — SMS (3 days):**
> {{contact.firstName}} — we helped a neighbour 2 streets over last week with a crack that turned into a full interior drain system because it was left 18 months. Caught early = $1,200 fix. Caught late = $14,000. Free inspection — no commitment. {{custom_values.booking_link}}

**Action 7 — Email (7 days):**  
Subject: One more thing before we close your file

> Hi {{contact.firstName}},
>
> We don't want to be pushy — but before we close your file, I want to leave you with one thought:
>
> Foundation issues are one of the few home repair problems that almost never get better on their own. The soil isn't getting less saturated. The crack isn't going to seal itself. Freeze-thaw cycles this winter will expand it by 1–2mm. By spring, what's a minor seepage issue today could be an active flood.
>
> If you're not ready yet, that's okay. Just save our number: {{custom_values.owner_phone}}.
>
> If you want to book that free look: {{custom_values.booking_link}}
>
> Either way — we're here.
>
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

**End of sequence:** Add tag `cold-lead`, move to Closed-Lost or keep in Follow-Up Active.

---

### Workflow 3: Free Inspection Confirmation

**Trigger:** Customer booked appointment (calendar: Free Basement Inspection)
**Goal:** Reduce no-shows, build trust pre-inspection  
**Tags to add:** `estimate-sent` (remove `new-lead`)

**Action 1 — Immediate SMS:**
> ✅ Confirmed! Your free basement inspection with {{custom_values.company_name}} is booked for {{appointment.start_time}}. Our inspector will assess your foundation, weeping tile, sump pump, and any visible cracks. See you then! Questions? Text {{custom_values.owner_phone}}.

**Action 2 — Immediate Email:**  
Subject: Your Free Basement Inspection is Confirmed ✓

> Hi {{contact.firstName}},
>
> You're confirmed for your free basement inspection on **{{appointment.start_time}}** with {{custom_values.company_name}}.
>
> **What to expect:**
> - Our inspector will assess your foundation walls, floor, weeping tile condition, sump pump, and any visible cracks or water entry points
> - Takes about 30–45 minutes
> - We'll walk you through our findings on-site and answer every question
> - No pressure, no obligation — just an honest assessment
>
> **To prepare:**
> - If you have any photos of water entry or cracks, have them ready
> - Note any areas where you've seen efflorescence (white chalky deposits) or staining
> - Let us know if there's a sump pump we should check
>
> Questions? Text us at {{custom_values.owner_phone}} anytime.
>
> See you {{appointment.start_time}},  
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

**Action 3 — SMS (24 hours before appointment):**
> Hi {{contact.firstName}}, quick reminder: your FREE basement inspection with {{custom_values.company_name}} is TOMORROW at {{appointment.start_time}}. See you then! Any questions? Call/text {{custom_values.owner_phone}}.

**Action 4 — SMS (2 hours before appointment):**
> Hey {{contact.firstName}} — we're seeing you in about 2 hours for your basement inspection! Our inspector will be there at {{appointment.start_time}}. If anything comes up, text us right away: {{custom_values.owner_phone}}.

---

### Workflow 4: No-Show Recovery

**Trigger:** Appointment status (filter: no-show, calendar: Free Basement Inspection)
**Goal:** Re-book the appointment  
**Tags to add:** `no-show`

**Action 1 — Immediate SMS:**
> Hi {{contact.firstName}}, we missed you at your inspection today. Hope everything's okay! We'd love to reschedule — it's free and takes 30 min. Pick a new time here: {{custom_values.booking_link}} Or text us: {{custom_values.owner_phone}}.

**Action 2 — Internal Task (15 min):**
> No-show: {{contact.firstName}} {{contact.lastName}} missed inspection. Call to reschedule — do not let this lead go cold. Phone: {{contact.phone}}.

**Action 3 — SMS (24 hours later, if no rebook):**
> {{contact.firstName}} — still want to get that free inspection done? Your basement won't fix itself. 😄 We have openings this week: {{custom_values.booking_link}}

---

### Workflow 5: Post-Inspection Follow-Up (6-step, 30 days)

**Trigger:** Pipeline stage changed (filter: new stage = Inspection Complete, Residential pipeline)
**Goal:** Convert inspection into signed contract — large ticket, longer cycle  
**Tags to add:** `estimate-sent`

**Action 1 — Immediate SMS:**
> Hi {{contact.firstName}}, thanks for having us out today! We'll have your estimate ready within 24 hours. Feel free to text any questions in the meantime: {{custom_values.owner_phone}}.

**Action 2 — Email (Day 1 — Estimate Delivery):**  
Subject: Your Free Basement Assessment Summary + Estimate

> Hi {{contact.firstName}},
>
> Thank you for the time today — it was great meeting you.
>
> Here's a summary of what we found and your estimate:
>
> [INSPECTOR FILLS THIS IN — summary of findings, recommended solution, and estimate amount]
>
> **What happens next:**
> 1. Review the estimate
> 2. Ask us any questions — we're happy to explain every line item
> 3. When you're ready, we'll schedule the work (most jobs book 1–2 weeks out)
>
> **Financing available** — payment plans starting at $X/month OAC if that's helpful.
>
> Questions? Call or text {{custom_values.owner_phone}} anytime.
>
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

**Action 3 — SMS (Day 3):**
> Hey {{contact.firstName}}, just checking in — had a chance to look over the estimate? Happy to answer any questions or walk you through it by phone. {{custom_values.owner_phone}}.

**Action 4 — Email (Day 5 — Financing Mention):**  
Subject: Questions about your estimate? (payment options available)

> Hi {{contact.firstName}},
>
> Just following up on your estimate for [repair type].
>
> If the investment is a consideration, we do offer flexible payment options — some clients spread it over 12–24 months with 0% interest (OAC). It's worth a quick conversation.
>
> Also happy to look at phasing the work — starting with the highest-risk area first.
>
> What questions can I answer for you?
>
> {{custom_values.owner_name}} | {{custom_values.owner_phone}}

**Action 5 — SMS (Day 7):**
> {{contact.firstName}} — wanted to share something. A client we visited 2 weeks ago had a similar crack to yours. They waited one more winter, and by April it was three times the problem. Just want to make sure we get you protected before the weather turns. Still happy to chat: {{custom_values.owner_phone}}.

**Action 6 — Email (Day 14 — Fear-Based, Strongest Follow-Up):**  
Subject: A quick note about your foundation repair

> Hi {{contact.firstName}},
>
> I wanted to follow up on the estimate we sent for your basement.
>
> I know it's a big decision — and I respect that you're thinking it through. I just want to share something we see often:
>
> When foundation issues are left unaddressed through one more winter, a few things tend to happen:
>
> - **Crack propagation** — freeze-thaw cycles expand existing cracks by 1–2mm per season
> - **Hydrostatic pressure buildup** — saturated soil pushes against your foundation wall constantly
> - **Mold growth** — even 2–3mm of moisture intrusion through a hairline crack creates mold conditions within 48–72 hours
> - **Repair costs increase** — what's a $1,200 crack injection today can become a $15,000 interior drain system next year if water undermines the footing
>
> I'm not saying this to pressure you. I'm saying it because our job is to protect homes, and the families in them.
>
> If you have questions about the estimate, the process, or your payment options — I'm here. Just reply to this email or text me directly at {{custom_values.owner_phone}}.
>
> Your home is worth protecting.
>
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

**Action 7 — SMS (Day 21):**
> {{contact.firstName}} — we still have your file open. We know these decisions take time. If you're ready or have questions, we're a text away. If you've decided to wait, just let us know and we'll touch base in the spring. {{custom_values.owner_phone}}.

**Action 8 — Email (Day 30 — Final):**  
Subject: Still want to protect your home?

> Hi {{contact.firstName}},
>
> This is our last follow-up for now — we don't want to flood your inbox.
>
> Your assessment is on file with us. Whenever you're ready — this spring, next fall, or right now — just reach out and we'll pick up exactly where we left off.
>
> {{custom_values.booking_link}} to rebook, or call/text {{custom_values.owner_phone}}.
>
> Take care,  
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

**End:** Add tag `cold-lead` if no response. Add to 90-day re-engagement list.

---

### Workflow 6: Financing Awareness

**Trigger:** Pipeline stage changed (filter: new stage = Financing Offered) OR Contact changed (filter: Estimate Amount field > $8,000)
**Goal:** Remove price objection before it kills the deal  
**Tags to add:** `financing-needed`

**Action 1 — Email (Immediate):**  
Subject: Payment options for your basement project

> Hi {{contact.firstName}},
>
> We know a waterproofing or foundation project is a significant investment — and we want to make sure money isn't the reason your home doesn't get the protection it needs.
>
> **Here's what we offer:**
>
> - **Flexible payment plans** — spread your project over 12–24 months
> - **0% interest financing** (OAC) through {{custom_values.financing_partner}}
> - **Partial phasing** — for larger projects, we can prioritize the highest-risk areas first and phase the rest
>
> A properly waterproofed basement also increases your home's value and protects it from the kind of damage that makes homes unsellable.
>
> Want to discuss options? I can put together a phased plan or connect you with our financing partner today — no application fee, decision in minutes.
>
> {{custom_values.owner_name}} | {{custom_values.owner_phone}}

**Action 2 — SMS (Day 3):**
> {{contact.firstName}} — just wanted to mention, we have financing available that makes this project surprisingly manageable monthly. Worth a quick chat? {{custom_values.owner_phone}}.

**Action 3 — Email (Day 7):**  
Subject: The math on protecting your basement

> Hi {{contact.firstName}},
>
> Quick note on the financing side of things.
>
> A $12,000 interior drainage system at 0% over 24 months = $500/month.
>
> The average home insurance deductible for water damage: $2,000–$5,000.
> Average mold remediation cost (if water intrusion causes mold): $5,000–$30,000.
> Average home value reduction from disclosed water history: $15,000–$40,000.
>
> The monthly payment starts to look different in context.
>
> Apply here (takes 3 minutes, no credit hit for checking): {{custom_values.financing_url}}
>
> Or call me and I'll walk you through it: {{custom_values.owner_phone}}.
>
> {{custom_values.owner_name}}

---

### Workflow 7: Insurance Claim Nurture

**Trigger:** Contact changed (filter: Insurance Claim field updated to Yes) OR Contact tag (filter: tag added = insurance-claim)
**Goal:** Position contractor as trusted advisor during the claim process  
**Tags to add:** `insurance-claim`

**Action 1 — Email (Immediate):**  
Subject: Navigating your insurance claim — what to know first

> Hi {{contact.firstName}},
>
> We understand you may be looking at an insurance claim for water damage. We work with insurance companies regularly and want to help you understand the process.
>
> **The most important thing to know:**
>
> Most standard home insurance policies (in Ontario) cover **sudden and accidental** water damage (burst pipe, appliance leak). They typically do NOT cover:
> - Gradual seepage through foundation cracks
> - Weeping tile failure over time
> - Hydrostatic pressure water intrusion
>
> **What IS often covered:**
> - Sewer backup (if you have this rider)
> - Overland water flooding (if you have this rider — check your policy)
> - Sudden structural failure
>
> **What we recommend:**
> 1. Call your insurance broker BEFORE calling the adjuster — they'll advise on your specific policy
> 2. Document everything with photos and video before any cleanup
> 3. Do not do any permanent repairs before the adjuster visits (temporary mitigation is fine)
> 4. Get our written assessment — adjusters respond well to professional contractor documentation
>
> We'll provide a full written report of the damage and recommended repairs. This documentation helps your claim.
>
> Questions? Call or text {{custom_values.owner_phone}} — we navigate this with homeowners regularly.
>
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

**Action 2 — SMS (Day 2):**
> {{contact.firstName}} — do you have your insurance policy number handy? Once your adjuster visit is confirmed, let us know the date and we can coordinate our assessment to complement theirs. {{custom_values.owner_phone}}.

**Action 3 — Email (Day 5):**  
Subject: Documentation checklist for your insurance claim

> Hi {{contact.firstName}},
>
> Here's a quick checklist to help your insurance claim go smoothly:
>
> ☐ Photos of all affected areas (walls, floor, belongings)  
> ☐ Video walkthrough of the basement before cleanup  
> ☐ List of damaged items with estimated values  
> ☐ Date you first noticed the problem  
> ☐ Any previous repairs or history  
> ☐ Contractor assessment (we provide this in writing)  
>
> Our written assessment includes: cause of water entry, extent of damage, and recommended permanent solution. This is exactly what adjusters want to see.
>
> Let us know how the adjuster visit goes. We're here to support the process.
>
> {{custom_values.owner_name}} | {{custom_values.owner_phone}}

---

### Workflow 8: Post-Job Review + Referral Request

**Trigger:** Pipeline stage changed (filter: new stage = Paid or Job Complete)
**Goal:** Google review + referral within 48 hours of job completion  
**Tags to add:** `job-complete`, `review-requested`  
**Update field:** Review Requested = Yes

**Action 1 — Immediate SMS:**
> Hi {{contact.firstName}}! The team just finished up — we hope everything looks great. Could you spare 2 minutes to leave us a Google review? It means the world to a small local business: {{custom_values.google_review_link}} Thank you! — {{custom_values.company_name}}

**Action 2 — Email (Day 1):**  
Subject: Thank you {{contact.firstName}} — one small favour?

> Hi {{contact.firstName}},
>
> It was a pleasure working on your home. Protecting families from foundation and water issues is what we do — and it's even more rewarding when we get to see the end result.
>
> If you're happy with the work, could you leave us a quick Google review? It takes about 2 minutes and helps other homeowners find a contractor they can trust:
>
> {{custom_values.google_review_link}}
>
> Not sure what to say? Just mention: what the problem was, what we did, and whether you'd recommend us.
>
> Thank you in advance,  
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

**Action 3 — SMS (Day 14 — Referral Ask):**
> {{contact.firstName}} — hope the basement has been dry! 🏠 If any friends, neighbours, or family mention water issues, wet basements, or cracks — we'd love the referral. We'll take great care of anyone you send our way. {{custom_values.company_name}} | {{custom_values.owner_phone}}

**Action 4 — Email (Day 90 — Seasonal Check-in):**  
Subject: Quick check-in from {{custom_values.company_name}}

> Hi {{contact.firstName}},
>
> Just reaching out to see how the basement has been holding up.
>
> If you've noticed anything — even minor seepage or new efflorescence — let us know sooner rather than later. Small issues caught early save thousands.
>
> And if you know anyone dealing with basement water problems, we'd love the introduction. We treat every referral like family.
>
> Enjoy the season,  
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}  
> {{custom_values.owner_phone}}

---

### Workflow 9: Unhappy Customer Recovery

**Trigger:** Contact tag (filter: tag added = unhappy-customer)
**Goal:** Internal alert ONLY — do not send to customer automatically  

**Action 1 — Internal Task (Immediate):**
> ⚠️ PRIORITY: Unhappy customer — {{contact.firstName}} {{contact.lastName}}. Phone: {{contact.phone}}. DO NOT send automated messages. Owner must call personally within 1 hour to resolve.

**Action 2 — Internal Email to Owner (Immediate):**  
Subject: ⚠️ Customer Issue — Immediate Attention Required

> {{contact.firstName}} {{contact.lastName}} has flagged a concern with their job.
>
> Contact: {{contact.phone}} | {{contact.email}}
>
> Please call personally within 1 hour. Do not send automated follow-up until resolved.
>
> Job notes: [link to contact record]

**NOTE:** Pause all other automated sequences for this contact until resolved.

---

### Workflow 10: Home Inspector Referral Partner Onboarding

**Trigger:** Pipeline stage changed (filter: new stage = New Partner, Foundation - Referral Partners pipeline)
**Goal:** Onboard home inspector as referral partner, explain the program  
**Tags to add:** `home-inspector-referral`

**Action 1 — Email (Immediate):**  
Subject: Making your job easier — foundation partnership

> Hi {{contact.firstName}},
>
> My name is {{custom_values.owner_name}}, I run {{custom_values.company_name}} here in {{custom_values.city}} — we specialize in foundation repair and basement waterproofing.
>
> I know home inspectors face an awkward moment when they find foundation cracks or moisture issues: you have to report it, but you don't always have someone you trust to recommend.
>
> I'd love to be that contractor for you.
>
> **Here's what I offer to inspectors I partner with:**
> - Same-week turnaround on any assessment your clients need
> - Written report with photos that complements your inspection report
> - Honest, no-pressure assessments — I'll tell homeowners when it's minor and when it's serious
> - I'll never oversell your clients (my reputation depends on yours)
>
> **How referrals work:**
> Simply text me the homeowner's name and phone number with a note about what you found. I'll reach out within the hour, take great care of them, and report back on the outcome.
>
> Would you have 15 minutes for a quick call or coffee? I think it could benefit both of us.
>
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}  
> {{custom_values.owner_phone}}

**Action 2 — SMS (Day 3, no response):**
> Hi {{contact.firstName}}, {{custom_values.owner_name}} here from {{custom_values.company_name}}. Sent you an email about a referral partnership for foundation/waterproofing. Would love to connect — even just 10 min by phone. {{custom_values.owner_phone}}.

**Action 3 — Email (Day 7 — Active Partner Welcome — send after agreement):**  
Subject: Welcome to the partner program — here's how it works

> Hi {{contact.firstName}},
>
> Great to have you on board.
>
> **Referring a client is simple:**
> Text me the homeowner's name and number with a brief note: "Crack in poured concrete wall, top-right corner" or "Sump pump running constantly, visible moisture on block wall."
>
> I'll take it from there — reach out within the hour, book a free inspection, and keep you posted on what we find and what they decide.
>
> **What your clients get:**
> - Free, no-pressure assessment
> - Clear written report they can keep
> - Options at different price points
> - A contractor who respects your credibility
>
> My direct line: {{custom_values.owner_phone}}
> My booking link (if clients prefer to self-book): {{custom_values.booking_link}}
>
> Looking forward to working together.
>
> {{custom_values.owner_name}}

**Action 4 — Monthly Check-in SMS (30 days, recurring for Active Partners):**
> Hi {{contact.firstName}}, {{custom_values.owner_name}} here. Quick check-in — any foundation or moisture issues come up in your inspections lately? Happy to do same-week assessments for any clients you'd like to refer. {{custom_values.owner_phone}}.

---

### Workflow 11: Seasonal Campaign — Spring (Wet Basement / Snow Melt)

**Trigger:** Scheduler (April 1, or manual launch)
**Audience:** Past leads who didn't close + past customers  
**Tags to add:** `spring-flooding`

**Action 1 — SMS (Launch Day):**
> Spring flooding season is here 🌧️ If you saw water in your basement after the snow melted, you're not alone — and it's not going to fix itself. {{custom_values.company_name}} is offering FREE inspections this month. Reply SPRING to book yours.

**Action 2 — Email (Day 1):**  
Subject: Why your basement leaked this spring (and how to stop it happening again)

> The snow melts. The ground is still frozen. Nowhere for the water to go — except against your foundation walls.
>
> This is called **hydrostatic pressure**, and it's the #1 cause of spring basement flooding in {{custom_values.city}}.
>
> **Here's what's happening underground:**
> - Saturated soil creates pressure up to 1,500 lbs per linear foot against your foundation
> - Hairline cracks that were invisible all winter become active water channels
> - Weeping tile systems that worked fine for years get overwhelmed
> - Sump pumps run 24/7 and sometimes fail under the sustained load
>
> The good news: **there are permanent solutions** — interior drainage, crack injection, sump pump upgrades — and they work even in older homes.
>
> We're booking free inspections this week. Click below to grab a slot before they fill up.
>
> [Book Free Inspection]: {{custom_values.booking_link}}
>
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}  
> {{custom_values.owner_phone}}

**Action 3 — SMS (Day 5):**
> {{contact.firstName}} — spring flood window is open right now. We're seeing our busiest call volume of the year. Don't wait until there's standing water. Free inspection: {{custom_values.booking_link}}

---

### Workflow 12: Seasonal Campaign — Fall (Before the Freeze)

**Trigger:** Scheduler (September 15, or manual launch)
**Audience:** Past leads who didn't close + past customers + current prospect list  
**Tags to add:** (none added — informational campaign)

**Action 1 — SMS (Launch Day):**
> Fall is the last chance for exterior waterproofing before the ground freezes. If your basement had any moisture issues this year, now is the time to fix it permanently. FREE inspection — reply FALL to book. {{custom_values.company_name}}.

**Action 2 — Email (Day 1):**  
Subject: The window is closing — basement waterproofing before winter

> Every fall, we have homeowners call us in November wanting exterior waterproofing. And we have to tell them the same thing: **we can't excavate frozen ground.**
>
> October is the last reliable month for exterior work in {{custom_values.city}}. After that, we're limited to interior solutions.
>
> **If you've seen any of these this year, call us now:**
> - Water staining along basement walls (efflorescence — white chalky deposits)
> - Cracks in your poured concrete or block foundation
> - Sump pump running more than usual during rain
> - Musty smell in the basement after wet weather
>
> These are warning signs that **one more winter will make worse.**
>
> We still have openings this week and next. After that, we're booking into November for interior work only.
>
> [Book Free Inspection]: {{custom_values.booking_link}}
>
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}  
> {{custom_values.owner_phone}}

**Action 3 — SMS (Day 7):**
> {{contact.firstName}} — one more heads up. Our exterior waterproofing calendar is filling fast before freeze. Once the ground freezes we're interior-only until spring. Last chance: {{custom_values.booking_link}} or call {{custom_values.owner_phone}}.

**Action 4 — Email (Day 14 — Urgency Close):**  
Subject: Last call — exterior waterproofing before freeze

> Hi {{contact.firstName}},
>
> This is it — we're down to our last few exterior waterproofing slots before the ground freezes.
>
> Interior work (crack injection, sump pump, interior drainage) is available year-round. But if your issue requires exterior excavation and membrane work, now is the last window until spring.
>
> Book by [DATE] and we'll get you on the calendar before winter locks us out.
>
> {{custom_values.booking_link}} | {{custom_values.owner_phone}}
>
> Stay dry this winter,  
> {{custom_values.owner_name}}  
> {{custom_values.company_name}}

---

## CUSTOM VALUES TO SET ON CLIENT ONBOARDING

When deploying to a client sub-account, set these custom values:

| Custom Value Key | Description | Example |
|---|---|---|
| company_name | Business name | "Peterborough Foundation Pros" |
| owner_name | Owner's first name | "Mike" |
| owner_phone | Direct owner cell for personalized SMS | "+1 705-555-0100" |
| office_phone | Main office line | "+1 705-555-0101" |
| booking_link | Free inspection calendar URL | "https://..." |
| google_review_link | Direct Google review link | "https://g.page/r/..." |
| website_url | Company website | "https://pbwaterproofing.ca" |
| city | Primary service city | "Peterborough" |
| service_area | Service area description | "Peterborough, Lindsay, Cobourg" |
| financing_partner | Financing company name | "Financeit" |
| financing_url | Financing application link | "https://financeit.io/..." |
| warranty_length | Warranty offered | "25 years" |

---

## NOTES FOR MANUAL WORKFLOW BUILD

1. **Start with Workflow 2 (Speed to Response)** — this is the highest-revenue workflow and should be live day 1
2. **Workflow 5 (Post-Inspection Follow-Up)** — build second; this is the revenue engine for large-ticket jobs
3. **Workflow 8 (Post-Job Review)** — build third; this is the growth flywheel
4. **Workflows 11 + 12 (Seasonal)** — can be built as manual-launch broadcast campaigns using GHL's Campaign tool instead of full workflows
5. **Workflow 9 (Unhappy Customer)** — internal only; keep simple with just task + internal email
6. **All workflows should have a "Stop Automation" action** at the top triggered by: any reply received OR opportunity moved past relevant stage

---

## WHAT'S INSTALLED AND READY

✅ **20 Custom Fields** — all contact fields with correct types and dropdown options  
✅ **4 Pipelines** — Residential (15 stages), Crack Injection (8 stages), Commercial (11 stages), Referral Partners (6 stages)  
✅ **3 Calendars** — Free Inspection (60 min), Crack Repair (30 min), Commercial Assessment (90 min)  
✅ **32 Tags** — complete tag library for segmentation, automations, and reporting  
📋 **12 Workflow Specs** — full trigger, delay, and copy documented above; build manually in GHL Workflows  

**Total build time:** ~30 minutes (API) + est. 2–4 hours to manually build workflows  
**Snapshot is production-ready** once workflows and custom values are set.

---

*Build log prepared by Maximus AI | 1app Foundation Snapshot | 2026-07-21*
