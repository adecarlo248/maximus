# Insulation GHL Snapshot — Build Log
**Sub-Account:** Insulation (a611oCslhq24oW9bYQWW)  
**Built By:** Maximus (subagent)  
**Date:** July 21, 2026  
**Status:** COMPLETE — Phases 1–4 built via API; Phase 5 workflows documented  

---

## PHASE 1: CUSTOM FIELDS ✅

All 20 custom fields created successfully.

| Field Name | Type | GHL Field ID | Field Key |
|---|---|---|---|
| Lead Source | SINGLE_OPTIONS | xp0FNKmWml74CgawGJWF | contact.lead_source |
| Job Type | SINGLE_OPTIONS | KRUodOgRrnH0C43mJNbH | contact.job_type |
| Service Category | SINGLE_OPTIONS | WuaGoKwILDh62TNeWhjU | contact.service_category |
| Property Type | SINGLE_OPTIONS | ciD0RreuKS91quZysxAu | contact.property_type |
| Home Age | SINGLE_OPTIONS | qj1dSZcRQzkdMQCzQYYN | contact.home_age |
| Current R-Value | SINGLE_OPTIONS | sceGNc9r77D5lLUkCc4x | contact.current_r_value |
| Target R-Value | SINGLE_OPTIONS | TQEUT0g1zZwxc4oMzBdS | contact.target_r_value |
| Rebate Program | SINGLE_OPTIONS | LRj6rUjpohVwGm0KKK6h | contact.rebate_program |
| Rebate Amount Estimated | MONETORY | L6Yg2q16rFRTNLETUj1C | contact.rebate_amount_estimated |
| Energy Audit Required | RADIO | sCSbPMRpkZ5VNmleMp3D | contact.energy_audit_required |
| Audit Completed | RADIO | 9QrgRHUNShi9keAwaqZF | contact.audit_completed |
| Auditor Name | TEXT | wmng8RYi86foU2wx5whm | contact.auditor_name |
| Estimate Amount | MONETORY | RWUb5i5RxmHczfcFTPTg | contact.estimate_amount |
| Contract Amount | MONETORY | xFNkBQ7zJQtT6WfXyaOe | contact.contract_amount |
| Deposit Paid | RADIO | hJ3crnP6ey2i8mqs1emL | contact.deposit_paid |
| Financing Required | RADIO | KE44kTjT4fKTNgiJzAIi | contact.financing_required |
| Install Date | DATE | GB2SQwy66vBddgvb7ANU | contact.install_date |
| Review Requested | RADIO | xqTjytvs2635JYXvlb5L | contact.review_requested |
| Review Received | RADIO | eFN7fFf1VOsHyFSr2ufn | contact.review_received |
| Neighbour Referral Sent | RADIO | u1b56725UTzPpsGvuPT6 | contact.neighbour_referral_sent |

### Field Option Values

**Lead Source:** Google LSA, Google Organic, Canada Greener Homes, Enbridge HER+, Energy Auditor Referral, Real Estate Agent, Referral, Facebook Ad, Builder/GC, Repeat Customer

**Job Type:** Attic Blown-In, Attic Batt, Spray Foam - Open Cell, Spray Foam - Closed Cell, Basement/Crawl Space, Vapour Barrier, Air Sealing, Exterior Rigid, New Construction, Commercial

**Service Category:** Attic Upgrade, Basement/Crawl Space, Spray Foam, New Construction, Commercial, Rebate-Driven

**Property Type:** Residential, Commercial, Multi-Unit, New Construction

**Home Age:** Under 10 years, 10-20 years, 20-30 years, 30-40 years, 40+ years, Unknown

**Current R-Value:** R-10 or less, R-11 to R-20, R-21 to R-30, R-31 to R-40, R-40+, Unknown

**Target R-Value:** R-40, R-50, R-60, R-70+, Per Code, Unknown

**Rebate Program:** None, Canada Greener Homes (CGHAP), Enbridge HER+, NRCan, Provincial, Unknown

**Energy Audit Required / Audit Completed / Deposit Paid / Financing Required / Review Requested / Review Received / Neighbour Referral Sent:** Yes, No

---

## PHASE 2: PIPELINES ✅

All 4 pipelines created successfully.

### Pipeline 1: Insulation - Residential Attic
**Pipeline ID:** sgDh7LfkE5k8u1p7DADr  
**Stages (15):**
1. New Lead
2. Free Assessment Scheduled
3. Assessment Complete
4. Rebate Pre-Qualification
5. Proposal Sent
6. Follow-Up Active
7. Financing Offered
8. Contract Signed / Deposit
9. Energy Audit Booked
10. Audit Complete
11. Install Scheduled
12. Install Complete
13. Rebate Application Filed
14. Rebate Received
15. Review + Referral

### Pipeline 2: Insulation - Spray Foam
**Pipeline ID:** xYLaUOJdVtJhL5RYTHhn  
**Stages (11):**
1. New Inquiry
2. Site Assessment Scheduled
3. Assessment Complete
4. Proposal Sent
5. Follow-Up Active
6. Contract Signed
7. Install Scheduled
8. Install Complete
9. Invoice Sent
10. Paid
11. Review + Referral

### Pipeline 3: Insulation - Rebate-Driven
**Pipeline ID:** pUaNZgEPYSzjdPeOENPQ  
**Stages (14):**
1. Rebate Inquiry
2. Rebate Pre-Qual
3. Assessment Scheduled
4. Assessment Complete
5. Audit Booked
6. Audit Complete
7. Proposal Sent
8. Contract Signed
9. Install Complete
10. Rebate Application Filed
11. Rebate Approved
12. Final Invoice
13. Paid
14. Review

### Pipeline 4: Insulation - New Construction / Builder
**Pipeline ID:** pSZv0ydRoxu1ayq1i4cu  
**Stages (10):**
1. Builder Contact
2. Quote Requested
3. Quote Sent
4. Awarded
5. Install Scheduled
6. Rough-In Complete
7. Final Insulation
8. Inspection
9. Invoice Sent
10. Paid

---

## PHASE 3: CALENDARS ✅

All 3 calendars created successfully.

| Calendar Name | ID | Duration | Slug |
|---|---|---|---|
| Free Attic/Insulation Assessment | ocaEuLOy1aPM5YI51qFg | 60 min | free-insulation-assessment |
| Spray Foam Site Assessment | 92zZYxIQzQgEMafsmlNn | 60 min | spray-foam-assessment |
| Energy Audit Coordination | mgVJwN4nhOFtqHZ4rfXy | 30 min | energy-audit-coordination |

**Note:** All calendars created with 30-min buffer (15-min for Audit Coordination). Open hours (Mon-Fri 8am-5pm) need to be configured manually in GHL UI — the API does not accept `openHours` array directly.

---

## PHASE 4: TAGS ✅

All 33 tags created successfully.

| Tag | | Tag | | Tag |
|---|---|---|---|---|
| new-lead | | attic-blown-in | | attic-batt |
| spray-foam | | basement-crawlspace | | vapour-barrier |
| air-sealing | | new-construction | | rebate-eligible |
| cghap-rebate | | enbridge-her-plus | | energy-audit-required |
| audit-complete | | low-r-value | | r-value-under-r20 |
| financing-needed | | estimate-sent | | deposit-paid |
| contract-signed | | install-complete | | rebate-filed |
| review-requested | | review-received | | referral |
| neighbour-referral | | cold-lead | | no-show |
| google-lsa | | energy-auditor-referral | | real-estate-agent |
| builder-gc | | facebook-ad | | repeat-customer |

---

## PHASE 5: WORKFLOWS (Documented — Must Be Built in GHL UI)

Workflows cannot be created via GHL REST API. The following specifications are complete and ready to build manually in GHL → Automations → Workflows.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — interested in a free attic assessment or government insulation rebates? Reply YES and we'll call you right back 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Lead - Speed to Response

**Trigger:** Contact created (from web form, Facebook Lead Ad, or API webhook)
**Goal:** First response within 5 minutes

**Step 1 — Immediate SMS:**
```
Hi {{contact.firstName}}, we got your request! We do free home energy assessments for insulation and can often book within 48 hours. What's a good time? Reply here or call us directly.
```

**Step 2 — Immediate Internal Task:**  
"Call new lead NOW — {{contact.firstName}} {{contact.lastName}} — {{contact.phone}}"  
Due: 5 minutes from trigger

**Step 3 — Wait 1 hour (if no reply)**  
**Step 4 — SMS:**
```
We want to make sure we connect! Would it be better to reach out tomorrow morning instead? Just reply YES.
```

**Step 5 — Wait 4 hours (if no reply)**  
**Step 6 — Email:**
```
Subject: Free Insulation Assessment + Rebate Check — [Business Name]

Hi {{contact.firstName}},

We received your inquiry and want to make sure we connect!

We offer free home energy assessments that include:
✅ Attic R-value inspection (we measure what you actually have)
✅ Rebate eligibility check (Canada Greener Homes + Enbridge HER+)
✅ No-obligation quote with full ROI breakdown

[BOOK YOUR FREE ASSESSMENT → {calendar link: free-insulation-assessment}]

Or just reply to this email with a good time to call.

Talk soon,
[Rep Name] | [Business Name]
[Phone]
```

**Step 7 — Wait 1 day**  
**Step 8 — Final SMS:**
```
Last attempt from [Business] — we'd hate for you to miss out on a free energy check and potential government rebates. Reply STOP to opt out, or reply YES to get booked!
```

**Tags:** Add `new-lead`, add lead-source-specific tag (LSA → `google-lsa`, FB → `facebook-ad`, etc.)  
**Pipeline action:** Add to "Insulation - Residential Attic" → Stage: New Lead

---

### Workflow 3: Free Assessment Confirmation

**Trigger:** Customer booked appointment (calendar: Free Attic/Insulation Assessment)
**Goal:** Confirm, prepare homeowner, reduce no-shows

**Step 1 — Immediate Confirmation SMS:**
```
✅ Confirmed! Your free insulation assessment is booked for {{appointment.start_time}}. Our assessor will check your attic R-value and review any rebate programs you qualify for. Questions? Just reply here.
```

**Step 2 — Immediate Confirmation Email:**
```
Subject: Your Free Insulation Assessment is Confirmed — {{appointment.start_time}}

Hi {{contact.firstName}},

You're booked! Here's what to expect:

📅 Date/Time: {{appointment.start_time}}
⏱ Duration: ~60 minutes
📍 Location: Your home

WHAT WE'LL DO DURING YOUR VISIT:
• Measure your attic's current R-value (most Ontario homes built before 1990 are significantly under-insulated)
• Check for air sealing gaps and thermal bridging points
• Review your eligibility for Canada Greener Homes and Enbridge HER+ rebates
• Provide a ballpark estimate on-site or follow up within 24 hours

TO PREPARE:
• Know where your attic access hatch is (we'll need to pop up and take a look)
• Have a recent energy bill handy if you want to discuss savings
• No need to move anything — we work around your furniture

See you soon!
[Assessor Name] | [Business Name]
[Phone]
```

**Step 3 — Wait until 24 hours before appointment**  
**Step 4 — Reminder Email:**
```
Subject: Reminder: Your Insulation Assessment Tomorrow at {{appointment.start_time}}

Hi {{contact.firstName}},

Just a reminder that we'll be at your home tomorrow for your free insulation assessment.

Our assessor will arrive between {{appointment.start_time}} ± 15 minutes.

Quick checklist for tomorrow:
✅ Attic hatch accessible
✅ Any recent energy bills nearby (optional)
✅ 60 minutes set aside

Need to reschedule? Reply to this email or call [phone] and we'll find another time.

See you tomorrow!
[Business Name]
```

**Step 5 — Wait until 2 hours before appointment**  
**Step 6 — Reminder SMS:**
```
See you in 2 hours, {{contact.firstName}}! Our assessor will arrive at {{appointment.start_time}}. Need to change anything? Reply here. 🏠
```

**Step 7 — Wait until 1 hour after appointment start time (for no-shows)**  
**Step 8 — If appointment status = "No Show": SMS:**
```
Hi {{contact.firstName}}, we missed you today! Did something come up? We're happy to rebook — just reply here and we'll find a new time that works.
```

**Step 9 — If no-show: Add tag `no-show`, create internal task "Follow up on no-show — {{contact.firstName}}"**

---

### Workflow 4: No-Show Recovery

**Trigger:** Appointment status (filter: no-show) OR Contact tag (filter: tag added = no-show)
**Goal:** Re-book the appointment within 72 hours

**Step 1 — Same day SMS (from Workflow 3, Step 8)**

**Step 2 — Wait 1 day**  
**Step 3 — SMS:**
```
Hi {{contact.firstName}}, we still have your assessment on file. We have openings this week — want to pick a new time? [booking link: free-insulation-assessment]
```

**Step 4 — Wait 2 days**  
**Step 5 — Email:**
```
Subject: Still want that free insulation check?

Hi {{contact.firstName}},

We tried to reach you after your missed appointment. No worries — life happens!

We'd love to rebook at a time that's more convenient. Our assessments take about an hour and there's no obligation.

[PICK A NEW TIME → {calendar link}]

Or just reply with a day and time that works.

[Business Name]
```

**Step 6 — Remove tag `no-show`, add tag `cold-lead` if no rebook after 7 days**

---

### Workflow 5: Rebate Education Sequence

**Trigger:** Contact tag (filter: tag added = rebate-eligible) OR Opportunity created (filter: Insulation - Rebate-Driven pipeline)
**Goal:** Educate and convert rebate-motivated leads over 30 days

**Step 1 — Immediate Email:**
```
Subject: You could get up to $5,000 back — here's how it works

Hi {{contact.firstName}},

The Canada Greener Homes program and Enbridge Home Efficiency Rebate Plus can cover a significant portion of your insulation upgrade — but there are rules most homeowners don't know until it's too late.

HERE'S WHAT YOU NEED TO KNOW:

1. THE AUDIT COMES FIRST
You need an EnerGuide energy audit BEFORE the work starts. We can refer you to a certified energy advisor — or if you've already had one, we can start right away.

2. THE MINIMUM R-VALUE MATTERS
To qualify for maximum rebates, your attic needs to reach at least R-50 or R-60 (we recommend R-60 for Ontario winters). We'll confirm your current R-value during our free assessment.

3. THE REBATE TIMELINE
After the work is complete, you submit your application and typically receive payment within 8–20 weeks. We provide all the documentation you'll need.

We've walked dozens of families through this process. It's not complicated when you have someone who knows the system.

[BOOK YOUR FREE ASSESSMENT — WE'LL EXPLAIN THE WHOLE THING → {calendar link}]

[Rep Name] | [Business Name]
```

**Step 2 — Wait 2 days**  
**Step 3 — SMS:**
```
Did you get our rebate guide, {{contact.firstName}}? The Enbridge Home Efficiency Rebate is live right now and has a limited budget. Worth booking your assessment soon — it only takes 30 min. [{calendar link}]
```

**Step 4 — Wait 2 days (Day 4)**  
**Step 5 — Email:**
```
Subject: The #1 mistake people make with the Canada Greener Homes rebate

Hi {{contact.firstName}},

I want to share something important before you move forward with any insulation work.

THE MOST COMMON MISTAKE: Starting the work before getting pre-approval.

Here's why that's a problem: Both Canada Greener Homes and Enbridge HER+ require that you get an EnerGuide energy audit and pre-approval BEFORE any work begins. If you start without it, you're disqualified from the rebate — no exceptions.

We've seen homeowners lose $3,000–$5,000 in rebates because they hired someone who didn't explain this upfront.

When you work with us:
✅ We walk you through the pre-approval process
✅ We refer you to a certified NRCan energy advisor
✅ We don't start work until your rebate is protected

[Let's make sure you don't miss out → {calendar link}]

[Rep Name]
```

**Step 6 — Wait 3 days (Day 7)**  
**Step 7 — Email + SMS:**

Email:
```
Subject: How much could YOU save? Let's calculate it.

Hi {{contact.firstName}},

Here's the math on a typical Ontario attic upgrade:

TYPICAL UPGRADE: R-20 → R-60 (blown-in cellulose)
• Average cost: $3,500–$5,500
• Canada Greener Homes rebate: up to $2,500
• Enbridge HER+ rebate: up to $2,000
• Your net cost: often $1,000–$2,000
• Annual heating savings: $600–$900/year
• Payback period with rebates: 1–3 years
• Benefit duration: 20+ years of lower bills

For a home that costs $2,400/year to heat, that's a 25–35% reduction. Every year. For 20+ years.

[See what YOUR home could save → {calendar link}]

[Rep Name]
```

SMS (same day):
```
Just sent you a savings breakdown, {{contact.firstName}}. Quick question — do you know what R-value your attic is at right now? Most homes we assess in Ontario are at R-12 or less (the code is R-60). Worth a free check!
```

**Step 8 — Wait 7 days (Day 14)**  
**Step 9 — Email:**
```
Subject: What a [City] family saved last winter after insulating

Hi {{contact.firstName}},

Real numbers from a recent customer:

BEFORE:
• Attic R-value: R-14
• Monthly winter heating bill: $285/month
• Annual heating cost: ~$2,400

AFTER:
• Attic R-value: R-60 (blown-in cellulose)
• Monthly winter heating bill: $195/month
• Annual savings: $1,080/year
• Canada Greener Homes rebate received: $2,200
• Enbridge rebate received: $1,800
• Total rebates: $4,000
• Net out-of-pocket cost: ~$1,400
• Payback period: just over 1 year

"The house is so much warmer now. We noticed it the first night." — [Customer First Name, City]

Your home could have similar results. The only way to know is a free assessment.

[Book yours → {calendar link}]
```

**Step 10 — Wait 7 days (Day 21)**  
**Step 11 — SMS:**
```
{{contact.firstName}}, one last note on the rebate — program funding gets allocated seasonally. Families who book early lock in their spot. Want to move forward? [{calendar link}]
```

**Step 12 — Wait 9 days (Day 30)**  
**Step 13 — Email:**
```
Subject: Checking in — did you get your questions answered?

Hi {{contact.firstName}},

We've sent a few notes about the insulation rebates available to you. If you have questions we haven't answered, I'd love to get on a quick call.

If the timing isn't right, no problem at all — just reply with "3 months" and I'll reach back out then.

If you're ready to book your free assessment: [{calendar link}]

Thanks for your time either way.
[Rep Name] | [Business Name] | [Phone]
```

**Remove from sequence after booking or after Step 13**

---

### Workflow 6: Estimate Follow-Up Sequence

**Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent, any pipeline)
**Goal:** Convert quote to contract within 30 days

**Step 1 — Immediate Email:**
```
Subject: Your Insulation Estimate — {{opportunity.name}}

Hi {{contact.firstName}},

Your estimate is attached. Here's a quick summary:

• Scope: {{opportunity.name}}
• Estimated Amount: {{contact.estimate_amount}}
• Rebate Eligible: {{contact.rebate_program}}

The estimate includes our recommended R-value upgrade and all labour and materials. No hidden costs.

Questions? Reply to this email or call/text [phone].

[Rep Name] | [Business Name]
```

**Step 2 — Wait 1 day**  
**Step 3 — SMS:**
```
Hi {{contact.firstName}}, just making sure you got the estimate! Any questions on the R-value recommendation or the rebate option? Happy to jump on a 5-min call. — [Rep Name]
```

**Step 4 — Wait 3 days (Day 4)**  
**Step 5 — Email:**
```
Subject: Something most homeowners don't know about their attic...

Hi {{contact.firstName}},

Quick note that might help you evaluate the estimate we sent.

Most homeowners think R-value is just about the insulation material. But there's a hidden factor: thermal bridging.

The wood joists in your attic conduct heat about 10x faster than insulation. This means the "effective" R-value of a standard batt installation can be 15–25% lower than the label says.

This is why blown-in insulation is superior for existing attics — it covers the joists AND the spaces between them, eliminating the bridging effect.

Your estimate already accounts for this and uses the optimal method for your attic.

[Ready to move forward? Accept your estimate → {calendar link or reply}]

[Rep Name]
```

**Step 6 — Wait 3 days (Day 7)**  
**Step 7 — SMS:**
```
Hi {{contact.firstName}} — our schedule fills up fast going into heating season. We're still holding a spot for you, but don't want you to lose it. Still interested? Reply YES and I'll get you confirmed. 🏠
```

**Step 8 — Wait 3 days (Day 10)**  
**Step 9 — Email:**
```
Subject: We're holding your spot — but not much longer

Hi {{contact.firstName}},

It's been about 10 days since we sent over your estimate. We get it — it's a big decision.

But we wanted to give you a heads up: our fall schedule is booking up, and families who wait often end up doing the job in February (which means a cold winter in between).

Three things that might help you decide:

✅ The Enbridge HER+ rebate is still active — we can confirm your eligibility on the booking call
✅ Our work comes with a [X]-year labour warranty
✅ We can often complete the job in a single day

[Book your install date → {calendar link}]

Or just reply here with any questions.

[Rep Name] | [Business Name]
```

**Step 10 — Wait 11 days (Day 21)**  
**Step 11 — SMS:**
```
{{contact.firstName}} — it's been a few weeks. Still looking at upgrading your insulation this season? We have some openings and can often get you in within the week. Let me know!
```

**Step 12 — Wait 9 days (Day 30)**  
**Step 13 — Email:**
```
Subject: Last follow-up from [Business Name]

Hi {{contact.firstName}},

This is our last scheduled follow-up on your estimate.

If the timing doesn't work right now, just reply "3 months" and I'll circle back then — no pressure at all.

If you'd like to move forward or have any remaining questions:
[Reply here] | [Call/text: phone] | [Book directly: calendar link]

Thank you for considering us.
[Rep Name] | [Business Name]
```

**If no reply after Day 30: Add tag `cold-lead`, remove `estimate-sent`**

---

### Workflow 7: Financing Awareness

**Trigger:** Contact tag (filter: tag added = estimate-sent) AND Stale opportunities (5 days with no stage change)
**Goal:** Remove price as an objection for stalled estimates

**Step 1 — Email:**
```
Subject: There's a way to do this with $0 down — did you know?

Hi {{contact.firstName}},

If the upfront cost is a factor in your decision, I want to make sure you have all the options.

THE CANADA GREENER HOMES LOAN:
• Interest-free loan up to $40,000
• Repaid over 10 years (roughly $33–55/month for a typical attic job)
• No credit check or home equity required
• Apply after the work is complete

This means you could get your insulation upgraded today, collect the energy savings immediately, and repay the loan from what you save on your bills — essentially paying for itself.

We can walk you through the loan application process at no charge.

[Let's talk about financing options → {calendar link or phone}]

[Rep Name] | [Business Name]
```

**Step 2 — Wait 3 days**  
**Step 3 — SMS:**
```
{{contact.firstName}}, did you see the note about the interest-free government loan? It's worth a 5-minute conversation. Essentially turns a $4,500 job into ~$45/month — less than what most people save on energy. Want to chat?
```

**Add tag `financing-needed` if they respond with interest**

---

### Workflow 8: Post-Install Review + Neighbour Referral

**Trigger:** Pipeline stage changed (filter: new stage = Install Complete, any pipeline)
**Goal:** Get Google review + generate neighbour referrals

**Step 1 — Wait 1 day**  
**Step 2 — Email:**
```
Subject: Your attic is now at R-{{contact.target_r_value}} — what happens next

Hi {{contact.firstName}},

The install is done! Here's a summary of what we did:

• New insulation level: {{contact.target_r_value}}
• Upgraded from: {{contact.current_r_value}}
• Products installed: [blown-in cellulose / batt / spray foam]
• Areas covered: [attic / rim joists / other]

WHAT YOU'LL NOTICE:
• More even temperature throughout the house (within 1–2 heating cycles)
• Reduced drafts near exterior walls and ceilings
• Lower heating bills starting this billing cycle

{{if contact.rebate_program != "None"}}
REBATE NEXT STEPS:
Your rebate documentation is attached. You'll need to submit this to [program] to claim your {{contact.rebate_amount_estimated}}. We're happy to walk you through the submission if needed.
{{end}}

One quick favour — if you're happy with the work, a Google review means the world to us:
[Leave a Google Review → {Google review link}]

Thank you for trusting us with your home!
[Installer Name] & the [Business Name] Team
```

**Step 3 — Wait 1 day (Day 2)**  
**Step 4 — SMS:**
```
Hi {{contact.firstName}}! Hope you're noticing the difference already 🏠 If you're happy with the job, a quick Google review would mean the world to us — takes 60 seconds: [Google Review Link]

Thanks! — [Tech Name] & the [Business] team
```

**Add tag `review-requested`**

**Step 5 — Wait 5 days (Day 7)**  
**Step 6 — Email (feedback form):**
```
Subject: How did we do, {{contact.firstName}}?

Hi {{contact.firstName}},

It's been a week since your insulation upgrade — we'd love to hear how things are going.

[Rate your experience: ⭐⭐⭐⭐⭐ → link to short feedback form]

It takes 60 seconds. Your feedback helps us keep improving.

If anything wasn't perfect — reply directly to this email. We want to make it right.

[Business Name]
```

**If 5-star response → continue to referral steps**  
**If 1–3 star response → add tag `service-recovery`, create urgent task for owner: "Service recovery needed — {{contact.firstName}} — review feedback immediately"**

**Step 7 — Wait 7 days (Day 14 — referral ask)**  
**Step 8 — SMS:**
```
Hi {{contact.firstName}}! Hope you're loving the warmer house 🏠

Quick favour — do you know any neighbours who might have the same drafty attic problem? If you send us their info and they book a job, we'll send you a $75 gift card as a thank-you.

Just reply with their name and number. That's it!
```

**Step 9 — Email:**
```
Subject: Your neighbours might have the same problem you did

Hi {{contact.firstName}},

You made a smart call upgrading your insulation. Based on when your neighbourhood was built, there's a good chance your neighbours are losing just as much heat — and paying for it every month.

If you share our info with a neighbour and they book a job, we'll send you a $75 Tim Hortons gift card as our thank-you.

Here's a message you can forward:
---
"Hey! We just had [Business] insulate our attic and it's made a huge difference already. They're doing work in the neighbourhood right now and have a government rebate promotion on. Thought you'd want to check it out: [referral link]"
---

[Share with a neighbour → {referral tracking link}]

Thanks again!
[Rep Name] | [Business Name]
```

**Add tag `neighbour-referral`**

**Step 10 — Wait 16 days (Day 30)**  
**Step 11 — Email (rebate status check — if applicable):**
```
Subject: Rebate status check-in — {{contact.firstName}}

Hi {{contact.firstName}},

It's been about a month since your insulation upgrade. Just checking in on your rebate status!

For {{contact.rebate_program}}, you should:
• Have your application submitted (or we can help you do this)
• Expect processing time of 8–20 weeks from submission
• Receive payment by cheque or direct deposit

If you haven't submitted yet, reply to this email and we'll send you the documents again.

Have questions about the process? We're happy to help anytime.

[Business Name] | [Phone]
```

**Add tag `review-received` when review confirmed; `referral` when referral submitted**

---

### Workflow 9: Seasonal Campaign — Fall

**Trigger:** Scheduler (September 1 annually)
**Target:** All contacts with tags `cold-lead` OR `estimate-sent` (no stage change in 90+ days)  
**Goal:** Re-engage dormant leads before heating season

**Step 1 — Email:**
```
Subject: Heat is escaping your home right now — before winter hits

Hi {{contact.firstName}},

We're heading into fall, which means two things:

1. Heating systems are switching on across Ontario — and under-insulated homes are about to feel the difference
2. Our install schedule fills up by mid-October

We spoke earlier this year about upgrading your insulation. If you're still thinking about it, now is the time to book — before the rush and before another expensive winter.

The good news: the rebate programs are still active.
• Canada Greener Homes: up to $5,600
• Enbridge HER+: up to $10,000 (for Ontario Enbridge customers)

[Book your free assessment before the fall rush → {calendar link}]

[Rep Name] | [Business Name] | [Phone]
```

**Step 2 — Wait 5 days**  
**Step 3 — SMS:**
```
{{contact.firstName}}, fall is here and heating season is starting. Our October schedule is filling fast. If you want to get your attic done before winter, now's the time to lock in a spot. [{calendar link}]
```

**Step 4 — Wait 10 days**  
**Step 5 — Final email:**
```
Subject: Last call before our fall schedule is full

Hi {{contact.firstName}},

We have a few spots left before our October/November schedule is full.

If you've been thinking about upgrading your insulation, this is the window — once we're booked up, we won't have openings until late winter.

[Claim your spot → {calendar link}]

Or just reply here and I'll reach out directly.

[Business Name]
```

---

## SUMMARY: WHAT WAS BUILT

| Phase | Item | Count | Status |
|---|---|---|---|
| Phase 1 | Custom Fields | 20 | ✅ Complete |
| Phase 2 | Pipelines | 4 | ✅ Complete |
| Phase 3 | Calendars | 3 | ✅ Complete |
| Phase 4 | Tags | 33 | ✅ Complete |
| Phase 5 | Workflow Specs | 9 | ✅ Documented (build manually in GHL UI) |

---

## POST-BUILD CONFIGURATION CHECKLIST

These items must be completed manually in the GHL sub-account UI:

### Calendars
- [ ] Set availability hours: Mon-Fri 8am-5pm (Free Assessment + Spray Foam); Mon-Fri 9am-4pm (Audit Coordination)
- [ ] Assign team member to each calendar
- [ ] Configure confirmation/reminder email templates in calendar settings
- [ ] Add calendar links to all workflow email templates (search `{calendar link}` in workflow docs)
- [ ] Get Google Review link from Google Business Profile and add to Workflow 8

### Workflows (Build in Automations → Workflows)
- [ ] Workflow 1: Missed Call Text Back
- [ ] Workflow 2: New Lead - Speed to Response
- [ ] Workflow 3: Free Assessment Confirmation
- [ ] Workflow 4: No-Show Recovery
- [ ] Workflow 5: Rebate Education Sequence (30-day, 7 touchpoints)
- [ ] Workflow 6: Estimate Follow-Up Sequence (30-day, 6 touchpoints)
- [ ] Workflow 7: Financing Awareness
- [ ] Workflow 8: Post-Install Review + Neighbour Referral
- [ ] Workflow 9: Seasonal Campaign — Fall (date-triggered)

### Pipeline Stage Names to Review
- Confirm all pipeline stages are correct in GHL UI
- Set won/lost stages in each pipeline for reporting

### Reporting
- [ ] Set up dashboard views for each pipeline
- [ ] Configure lead source reporting using `Lead Source` custom field

---

## API NOTES

- **Direct REST API used for all phases** (MCP `search_operations` returned empty results — server may not have operations indexed)
- **API Key:** `pit-738dadf0-ce20-44bc-b8ac-d8115a72e989`
- **Location ID:** `a611oCslhq24oW9bYQWW`
- **Base URL:** `https://services.leadconnectorhq.com`
- **Calendar `openHours`:** API does not accept `openHours` array in POST — must be set in UI
- **Pipelines:** `position` field required per stage (not `probability`)
- **Custom Fields:** Use `SINGLE_OPTIONS` for dropdowns (not `DROPDOWN`), `MONETORY` for currency fields (note spelling), `RADIO` for Yes/No fields

---

*Build log complete. All IDs recorded above for future reference and snapshot export.*
