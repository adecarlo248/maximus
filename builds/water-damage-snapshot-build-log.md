# Water Damage Restoration — GHL Snapshot Build Log
**Sub-account:** Water damage restoration  
**Location ID:** MLnGRbznjwLmJ517s340  
**Built:** 2026-07-21  
**API Token:** pit-558faf87-cd54-4fba-91b1-84346eead871  
**Status:** COMPLETE (Phases 1–4 built via API; Phase 5 documented for manual build)

---

## PHASE 1: CUSTOM FIELDS ✅ COMPLETE

All 21 custom fields created via REST API.

| # | Field Name | Type | GHL ID |
|---|-----------|------|--------|
| 1 | Lead Source WD | SINGLE_OPTIONS | IyxmL5CRovQfart9XJfF |
| 2 | Job Type | SINGLE_OPTIONS | iNWBOToLz6PIHu33IgW9 |
| 3 | Water Category | SINGLE_OPTIONS | c21xGHncAhnva8YIIcDI |
| 4 | Water Class | SINGLE_OPTIONS | vDBR2QREz1LYofGdnt5b |
| 5 | Insurance Claim | RADIO | KRaf0FaROA9swBHcXg5N |
| 6 | Insurance Company | TEXT | 51g6EM5YqjR2lU92tpeW |
| 7 | Claim Number | TEXT | rlvZAIStnyTmF9J6zoeZ |
| 8 | Adjuster Name | TEXT | IvshpNw6k811pzBOXBBF |
| 9 | Adjuster Phone | PHONE | f64yGfs8VvUVJM7ckEYt |
| 10 | AOB Signed | RADIO | ULbxJlzcKuQz96Jpsyw3 |
| 11 | Current Moisture Reading | TEXT | se7uL9fEd2Zx2PJwy0wm |
| 12 | Target Moisture | TEXT | tSsRVK7rPCIpDr8bAQ4k |
| 13 | Equipment on Site | RADIO | 6B2GjC5ZKR3YIeognZYj |
| 14 | Days Drying | NUMERICAL | nQtFBpEFTaLgXurqP1TA |
| 15 | Estimate Amount | MONETORY | W1Jwq09rKqpY4yTXCpjz |
| 16 | Invoice Amount | MONETORY | UNhfqPvtslozu3tQBY9F |
| 17 | Technician Assigned | TEXT | lsfUERRvvlfqPlDoMUTE |
| 18 | Reconstruction Needed | RADIO | LcAw5AOFIE3q3v3ig9AS |
| 19 | Review Requested | RADIO | 9VWSdRmcXBRIaRQSHbcl |
| 20 | Review Received | RADIO | 7RRsjMHfe25abKZsXGe0 |
| 21 | Plumber Partner Referral | RADIO | mhAhwkzjOO6AjsqWKRv7 |

### Custom Field Options Reference

**Lead Source WD options:** Google Emergency Search, Insurance Adjuster, Plumber Referral, Property Manager, Restoration Network, Repeat Customer, Referral, Facebook Ad

**Job Type options:** Water Extraction, Structural Drying, Sewage Backup, Flood Restoration, Burst Pipe Cleanup, Basement Flooding, Appliance Leak, Roof Leak Water Damage, Contents Pack-Out, Reconstruction

**Water Category options:** Category 1 - Clean, Category 2 - Grey, Category 3 - Black/Sewage, Unknown

**Water Class options:** Class 1 - Minor, Class 2 - Significant, Class 3 - Extensive, Class 4 - Specialty, Unknown

**All RADIO fields:** Yes / No options

---

## PHASE 2: PIPELINES ✅ COMPLETE

All 4 pipelines created via REST API.

### Pipeline 1: Water Damage - Emergency Response
**ID:** q8cidTXIiRy4K4VzNnnr

Stages:
1. New Emergency Call
2. Dispatched
3. On-Site Assessment
4. Containment/Extraction Started
5. Equipment Set
6. Daily Monitoring
7. Drying Complete
8. Equipment Removed
9. Job Complete
10. Invoice to Insurance
11. Paid
12. Review Requested
13. Reconstruction Referral

### Pipeline 2: Water Damage - Insurance Claim
**ID:** orgbwQ1Z6Gxv8gsxBVw7

Stages:
1. Claim Opened
2. Adjuster Assigned
3. Adjuster Meeting Set
4. Scope Agreed
5. Work Authorized
6. Mitigation In Progress
7. Mitigation Complete
8. Invoice Submitted
9. Supplement Filed
10. ACV Payment Received
11. Depreciation Released
12. Final Payment
13. Closed

### Pipeline 3: Water Damage - Reconstruction
**ID:** nRJapluMKJUkVH92wQn2

Stages:
1. Referral Received
2. Scope Review
3. Proposal Sent
4. Contract Signed
5. Permit Applied
6. Demo Complete
7. Rough-Ins
8. Drywall/Finishes
9. Job Complete
10. Invoice Sent
11. Paid
12. Review + Referral

### Pipeline 4: Water Damage - Referral Partners
**ID:** qUkxzzzJXuih09PC0lw9

Stages:
1. Partner Identified
2. Outreach Sent
3. Partnership Active
4. Referral Received
5. Job Complete
6. Partner Thanked
7. VIP Partner

---

## PHASE 3: CALENDARS ✅ COMPLETE

All 3 calendars created via REST API.

| Calendar | ID | Duration | Hours |
|----------|-----|----------|-------|
| Emergency Water Damage Response | zCRqy1ZKBKd4Zko4KnNK | 60 min | 24/7 (set availability manually) |
| Insurance Adjuster Meeting | jh3YiPX0jooWPiEa0V0D | 60 min | Mon-Fri 8am-5pm (set manually) |
| Reconstruction Consultation | XNbapqDtQmysiSEnc7Ob | 60 min | Mon-Fri 8am-5pm (set manually) |

**Note:** GHL calendar API creates with default availability. Go to Settings → Calendars to set specific open hours for each.

---

## PHASE 4: TAGS ✅ COMPLETE

All 31 tags created via REST API.

| Tag | ID |
|-----|-----|
| new-emergency | mB3fj5PRFi125JejO2Ym |
| water-extraction | 0KwN45YonaBvUHXsgzBy |
| structural-drying | 1s8JBNF92qTKO5ViG8Pp |
| sewage-backup | hYFpDrt3t47WcjhxKfaY |
| flood-restoration | U56ZYN9pTUUxDpL9TVsG |
| burst-pipe | Ho76g9XdYfcetbr7HxEM |
| basement-flooding | NCNbApJWtt1M0BRy1XQH |
| appliance-leak | AhKUXSu8NaDPccwpfYyj |
| contents-packout | rKP9e8CiGK5P8pZAUq0I |
| reconstruction-needed | mxIfOmc9ToNG5LM79wUF |
| category-1 | TxtUukBb00tEPSqplL26 |
| category-2 | Ph6tUh1J2XkhLVJK6BW6 |
| category-3-sewage | 0xhk9cQWE5Mshfyk7EDv |
| insurance-claim | ty91FrnrvbV9T2G095OB |
| adjuster-assigned | Rf7YKuUWwuJYqSciulSq |
| aob-signed | dsuYnQ8u5wKaqwgBIPOs |
| equipment-on-site | 7dHimy2iD609u08lsZLI |
| drying-active | bYekHuovCsV5ao5OIWjk |
| drying-complete | ZFm6HeBFWAH7TMMquOv3 |
| invoice-to-insurance | otcC9PRtclstnzB3vifF |
| supplement-filed | h3dJU3DRWYuOHMps59Tq |
| plumber-referral | U8Mjq6QtvauIibjhj2lr |
| property-manager | zKXhrQyXXkUYhK1FCC0N |
| restoration-network | jbZGpQSK2lcisUejkLxL |
| review-requested | l9qeebKFbZneDyGHC8qK |
| review-received | t2hWalKVQjPanqCZsj2Z |
| referral | cbsFcQZoWyt9iCybHGym |
| repeat-customer | 1kLSoOtSxkpwTSpEu10P |
| google-emergency | r8Uyr4qZLv8FpRU3fcIh |
| vip-partner | kDMs6UJhYzby0Cp3mT9B |
| cold-lead | ICCwWwBCkzmg5qJNfVEO |

---

## PHASE 5: WORKFLOWS — FULL SPECIFICATIONS

> **Note:** GHL Public API does not expose workflow creation endpoints. All 12 workflows below are fully documented with exact SMS/email copy, triggers, timing, and logic for manual build inside the GHL Automation builder.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — water damage emergency? Reply YES and we'll dispatch immediately. Available 24/7 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Emergency — Speed to Dispatch

**Trigger:** Contact created (from emergency web form submission) OR Contact tag (filter: tag added = new-emergency)
**Goal:** Immediate acknowledgment + 5-minute human callback  
**Internal 5-minute response SLA**

**Step 1 — Immediate (0 min): SMS to Contact**
```
{{contact.firstName}} — we got your message. Water damage emergency? Our team is standing by 24/7. We're calling you right now. — [Company Name]
```

**Step 2 — Immediate (0 min): Internal Escalation Alert**
```
🚨 NEW EMERGENCY LEAD — WEB FORM
Name: {{contact.firstName}} {{contact.lastName}}
Phone: {{contact.phone}}
Address: {{contact.address1}}
Submitted: {{now}}

CALL WITHIN 5 MINUTES. Record: [CRM link]
```

**Step 3 — Create Task:** "Call {{contact.firstName}} NOW — web form emergency lead" (Due: 5 min)

**Step 4 — 2 min (if internal callback not logged): Escalation to Owner**
```
⚠️ Emergency lead NOT called back. {{contact.firstName}} at {{contact.phone}}. 2 minutes elapsed. Take action NOW.
```

**Step 5 — Move Pipeline:** Water Damage - Emergency Response → "New Emergency Call"

**Step 6 — 5 min (after job confirmed — pipeline stage move trigger separately):**
SMS to contact:
```
✅ Great news, {{contact.firstName}}! [Tech Name] is heading to you now. ETA: approximately [X] minutes. He'll arrive in a [Company] vehicle, assess the damage, and get extraction started immediately. Questions? Call or reply here. — [Company Name]
```

---

### Workflow 3: Daily Drying Update

**Trigger:** Scheduler (daily at 6:00 PM) for all contacts tagged `drying-active`
**Goal:** Proactive moisture reading updates to reduce inbound calls, build trust

**Step 1 — 4:00 PM daily: SMS to Technician**
```
📋 Time to log drying readings for {{contact.firstName}} at {{contact.address1}}.

Log your readings here: [Tech Daily Log Form URL]

Required: RH%, GPP, equipment count, status. Takes 2 minutes.
```

**Step 2 — 6:00 PM daily: SMS to Homeowner**
```
📊 {{contact.firstName}} — Day {{contact.days_drying}} Drying Update

📍 Property: {{contact.address1}}
💧 Moisture Reading: {{contact.current_moisture_reading}} (target: {{contact.target_moisture}})
🔧 Equipment Running: On site ✅
📅 Status: On Track

We'll update you again tomorrow. Questions? Reply anytime. — [Company Name] | 24/7: [phone]
```

**Branch Logic:**
- If Days Drying > 10 AND Moisture still above target: Add note to contact, create task for supervisor review
- If Moisture Reading hits target: Move to "Drying Complete" stage, trigger Workflow 4 (Post-Job Review Request)

---

### Workflow 4: Post-Job Review Request

**Trigger:** Pipeline stage changed (filter: new stage = Equipment Removed, Emergency Response Pipeline)
**Wait:** 24 hours after equipment removed  
**Goal:** Capture 5-star Google reviews at peak satisfaction moment

**Step 1 — 24 hours after trigger: SMS Touch 1**
```
Hi {{contact.firstName}} — hope you're settling back in after everything. Our team worked hard to get your home back to normal as fast as possible, and we're glad it's done.

One quick favor: would you mind leaving us a Google review? It takes 60 seconds and helps other families in the area find us when they need help.

[Google Review Link]

Thank you — genuinely means a lot to our team. — [Owner Name]
```

**Step 2 — Add Tag:** `review-requested`
**Step 3 — Update Custom Field:** Review Requested = Yes

**Step 4 — Day 3 (if no review received): SMS Touch 2**
```
Hi {{contact.firstName}} — just a quick follow-up. If you had a good experience with [Company Name], a Google review goes a long way. Helps us keep our local team busy and helps families find us in emergencies.

[Google Review Link]

No pressure — but it's appreciated. — [Company Name]
```

**Step 5 — Day 7 (if no review received): SMS Touch 3 (Final)**
```
Last reach out, {{contact.firstName}} — if you got good service from us, 60 seconds on Google makes a real difference. [Google Review Link]. No worries if not. 👍 — [Company Name]
```

**Step 6 — Remove from review sequence after Touch 3. Do not message again.**

---

### Workflow 5: Unhappy Customer Recovery

**Trigger:** Customer replied (with keyword filter: unhappy, terrible, awful, disappointed, complaint, ridiculous, worst) OR New review received (filter: rating ≤ 3)
**Goal:** Internal escalation only — no public dispute

**Step 1 — Immediate: Internal Alert to Owner**
```
⚠️ UNHAPPY CUSTOMER ALERT
Contact: {{contact.firstName}} {{contact.lastName}}
Phone: {{contact.phone}}
Message: {{last_message_body}}

DO NOT send any automated messages. Personal call from owner required within 1 hour.
```

**Step 2 — Add Tag:** `cold-lead` (removes from automated sequences)
**Step 3 — Create Task:** "Personal call to {{contact.firstName}} — unhappy customer. DO NOT auto-message." (Due: 1 hour)
**Step 4 — Remove from all automated nurture sequences**
**Step 5 — NO customer-facing automated messages fire in this workflow**

---

### Workflow 6: Insurance Claim Nurture

**Trigger:** Contact tag (filter: tag added = insurance-claim) OR Contact changed (filter: Insurance Claim field updated to Yes)
**Goal:** Guide homeowner through claim process, coordinate with adjuster, accelerate approval

**Day 0 (Immediate): SMS — Claim Number Capture**
```
Hi {{contact.firstName}} — quick question: do you have your insurance claim number handy? Once we have it, we can coordinate directly with your adjuster and keep your claim moving. Reply with the number whenever you have it. — [Company Name]
```

**Day 1: Email — Full Insurance Process Guide**
Subject: "Your water damage claim — here's exactly what happens next"
```
Hi {{contact.firstName}},

We know dealing with insurance on top of a water emergency is stressful. Here's exactly what to expect so there are no surprises:

📋 YOUR CLAIM TIMELINE:
• Day 1-3: Adjuster is assigned by your insurance company
• Day 3-7: We submit our full documentation package (photos, moisture maps, scope of work, Xactimate estimate)
• Day 7-14: Adjuster reviews and approves scope
• Day 14-21: Invoice submitted; payment issued (often to you + your mortgage holder jointly)

✅ WHAT WE HANDLE:
• All communication with your adjuster
• Complete documentation package (IICRC-compliant)
• Xactimate estimate preparation
• Supplement filing if initial approval is incomplete

📌 WHAT YOU NEED TO DO:
1. Save your claim number (text it to us at [phone])
2. If your adjuster contacts you directly, forward their number/email to us immediately
3. Do NOT agree to any scope changes without consulting us first

Questions? Reply to this email or call [phone] anytime.

— [Owner Name] | [Company Name]
```

**Day 3: SMS — Documentation Sent**
```
{{contact.firstName}} — update on your claim:

📁 We've sent your adjuster a complete documentation package:
• Moisture mapping photos
• Daily drying logs  
• IICRC-compliant scope of work
• Xactimate estimate

Typical review time: 5–10 business days. We're following up on our end. Questions? Reply or call [phone]. — [Company Name]
```

**Day 7 (if still in "Adjuster Assigned" stage): SMS — Status Update**
```
Quick update, {{contact.firstName}} — we're in active communication with your adjuster ({{contact.adjuster_name}}). Adjuster reviews can take 7–14 days. Nothing you need to do today — we've got it covered. — [Company Name]
```

**Day 14 (if no approval yet): SMS + Email**
SMS:
```
{{contact.firstName}} — still working on your claim. We've submitted a complete Xactimate estimate and documentation package. Adjuster: {{contact.adjuster_name}}. We're following up today. If you hear from your insurance company, please forward any emails to us at [email]. — [Company Name]
```

**Day 21 (if still pending): Email — Escalation Guidance**
Subject: "Your claim is taking longer than usual — here's what to do"
```
Hi {{contact.firstName}},

Your claim approval has taken longer than expected. Here's what we recommend:

1. Call your insurance company's claims line and ask for an escalation supervisor
2. Reference claim number: {{contact.claim_number}}
3. Ask: "What is the status of my claim and what's causing the delay?"
4. Forward any response to us immediately

If the delay continues, you have the right to request a public adjuster — an independent claims expert who works for YOU, not the insurance company. We can refer you to a trusted one in your area.

We're fighting for your full claim. — [Owner Name]
```

**Day 28+: Monthly check-in SMS until resolved:**
```
{{contact.firstName}} — monthly check-in on your claim ({{contact.claim_number}}). Any updates from your insurance company? We're still actively following up on our end. — [Company Name]
```

---

### Workflow 7: Supplement Filed Notification

**Trigger:** Pipeline stage changed (filter: new stage = Supplement Filed, Insurance Claim Pipeline) OR Contact tag (filter: tag added = supplement-filed)
**Goal:** Explain supplement to homeowner, manage expectations

**Step 1 — Immediate: SMS**
```
{{contact.firstName}} — important update on your claim:

We've identified additional scope that wasn't included in the initial approval and have filed a supplement with your insurance company.

What this means: We found more damage during restoration that needs to be properly compensated. This is normal and common.

What happens next: Your adjuster will review the supplement (typically 7–14 days). We'll keep you posted. — [Company Name]
```

**Step 2 — Day 3: Email**
Subject: "Supplement filed — here's what that means for your claim"
```
Hi {{contact.firstName}},

A supplement is a formal request to your insurance company to cover additional scope discovered during restoration work.

WHAT WE FOUND:
[Technician manually fills in specific notes before sending]

WHY IT MATTERS:
Your initial claim may have been approved based on visible damage. Structural drying often reveals hidden moisture behind walls, under floors, and in ceiling cavities that requires additional remediation.

YOUR RIGHTS:
You are entitled to full restoration to pre-loss condition under your policy. If the supplement is denied, we can assist with an appeal or public adjuster referral.

TIMELINE:
Most supplements are resolved within 14–21 days of filing. We'll notify you immediately when there's an update.

Thank you for your patience. — [Owner Name]
```

---

### Workflow 8: Plumber Referral Partner Onboarding

**Trigger:** Contact tag (filter: tag added = plumber-referral) AND Pipeline stage changed (filter: new stage = Partnership Active, Referral Partners Pipeline)
**Goal:** Onboard plumber partner with clear referral instructions

**Step 1 — Immediate: SMS Welcome**
```
Welcome aboard, {{contact.firstName}}! 

Here's how the referral works:
📞 When you hit a water damage job — call or text [Company Name] at [phone]
📍 We'll dispatch within [X] minutes
💼 You focus on your plumbing work; we handle everything else
🤝 Every referral tracked — we'll follow up on outcomes

Referral card on its way. Looking forward to working together! — [Owner Name] | [Company Name]
```

**Step 2 — Immediate: Email — Full Partner Welcome Package**
Subject: "Welcome to the [Company Name] referral network — here's how it works"
```
Hey {{contact.firstName}},

Every burst pipe call you can't fix is revenue for us, and we'll make sure you look like a hero to your customer every single time.

HOW TO REFER:
When you respond to a burst pipe and see water damage, call or text us at [phone] before you leave the property.

Tell us:
• The homeowner's name and number
• The address
• What you found (burst pipe location, standing water, approx. affected area)

We'll take it from there — dispatch within [X] minutes, keep the homeowner updated, handle all insurance paperwork.

WHAT YOUR CUSTOMER GETS:
✅ 24/7 emergency response
✅ Professional structural drying (IICRC-certified process)
✅ Insurance claim coordination from start to finish
✅ Daily updates so they're never left guessing

WHAT YOU GET:
✅ Your customer handled professionally (protects your reputation)
✅ We refer plumbing work back when homeowners ask us for recommendations
✅ Quarterly check-ins to strengthen the relationship

Any questions? Call me directly at [Owner phone]. — [Owner Name]
```

**Step 3 — Day 3: SMS Check-in**
```
Hey {{contact.firstName}} — any questions about how the referral works? Happy to do a quick 5-minute walkthrough anytime. — [Owner Name]
```

**Step 4 — Day 14: Task — Physical Referral Cards**
Internal task: "Drop off referral cards to {{contact.firstName}} at {{contact.company}} — {{contact.address1}}"

**Step 5 — Day 30: SMS — First Check-in**
```
Hey {{contact.firstName}} — [Owner Name] from [Company]. Checking in. Had any burst pipe calls lately? Our team is standing by — we dispatch in [X] minutes. Give us a call whenever you need us. — [Owner Name]
```

---

### Workflow 9: Plumber Partner Monthly Nurture

**Trigger:** Scheduler (1st of each month) for all contacts tagged `plumber-referral` in Partnership Active or VIP Partner stage
**Goal:** Stay top-of-mind without being annoying

**Month 1 SMS:**
```
Hey {{contact.firstName}} — [Company] here. Water damage season is picking up. Give us a call whenever you hit a flood — we dispatch in [X] minutes. — [Owner Name]
```

**Month 2 SMS:**
```
Quick tip for your homeowners: after a burst pipe, running a dehumidifier for 1–2 days is NOT enough. Structural drying takes 5–10 days minimum. We do it right, IICRC-certified. Call us anytime — [Owner Name]
```

**Month 3 SMS:**
```
{{contact.firstName}} — wanted to say thanks. Every referral you send helps a family in a tough spot get taken care of the right way. Appreciate you. Anything we can do for you? — [Owner Name]
```

**Month 4 SMS:**
```
Hey {{contact.firstName}} — reminder that we handle ALL water damage types: burst pipes, basement flooding, sewage backup, appliance leaks, roof leaks. Any water in a home, call us. 24/7. — [Owner Name]
```

**Month 5 SMS:**
```
Quick one — do you ever run into homeowners asking about mold after a water event? We handle mold assessment and remediation too. Good to know for your customers. — [Owner Name]
```

**Month 6 SMS:**
```
{{contact.firstName}} — halfway through the year. How's business? Anything we can do to make the referral process smoother for you? Your feedback helps us get better. — [Owner Name]
```

*Cycle repeats monthly with variation*

---

### Workflow 10: Reconstruction Referral

**Trigger:** Pipeline stage changed (filter: new stage = Drying Complete or Certificate Issued, Emergency Response Pipeline)
**Goal:** Capture reconstruction revenue opportunity, facilitate partner referral

**Step 1 — Immediate: SMS to Homeowner**
```
🎉 Great news, {{contact.firstName}}!

Your property has reached drying standard per IICRC S500 guidelines.

✅ Moisture readings: at target
✅ Certificate of Completion: being prepared now
✅ Equipment removal: within 24 hours

Next step: reconstruction of affected materials (drywall, flooring, etc.). We work with trusted local contractors — want us to connect you? Reply YES and we'll make the intro today.

Thank you for trusting [Company Name]. — [Owner Name]
```

**Step 2 — If homeowner replies YES:**
SMS:
```
We'll connect you with [Contractor Name] today. They specialize in exactly this type of restoration work and coordinate directly with insurance. Expect a call from [number] within 2 hours. — [Company Name]
```

Internal Task: "Notify reconstruction partner of referral — {{contact.firstName}}, {{contact.address1}}, scope: [notes]"
Move Contact: → Water Damage - Reconstruction Pipeline, Stage: "Referral Received"

**Step 3 — Day 3 after referral: SMS to homeowner**
```
{{contact.firstName}} — did [Contractor] connect with you? Just making sure you're taken care of. — [Company Name]
```

**Step 4 — Update Custom Field:** Reconstruction Needed = Yes

---

### Workflow 11: Property Manager Account Outreach

**Trigger:** Contact tag (filter: tag added = property-manager) AND Pipeline stage changed (filter: new stage = Partner Identified)
**Goal:** Pitch priority response SLA to property managers (high-volume account target)

**Step 1 — Immediate: SMS**
```
Hi {{contact.firstName}} — [Owner Name] from [Company Name]. Question: when a tenant calls you about water damage, what happens in the first hour?

We offer property managers a dedicated priority response — guaranteed dispatch within [X] minutes, direct billing coordination, and daily written updates. Would a 10-minute call be worth your time? — [Owner Name]
```

**Step 2 — Day 3 (if no response): Follow-up SMS**
```
{{contact.firstName}} — following up. One water damage job that gets ahead of mold = a lot of headache prevented. Our priority SLA is designed specifically for property managers. 10 minutes? — [Owner Name]
```

**Step 3 — Day 7: Email**
Subject: "Priority water damage response for property managers — [Company Name]"
```
Hi {{contact.firstName}},

Managing properties means water events happen whether you're ready or not. Here's what we offer property managers:

✅ PRIORITY RESPONSE: Dedicated dispatch line — you call, we move within [X] minutes
✅ DIRECT BILLING: We coordinate insurance or invoice management company directly
✅ DAILY WRITTEN UPDATES: Email/SMS reports on every active job — you're always informed
✅ IICRC-CERTIFIED PROCESS: Documented, defensible restoration for insurance purposes
✅ MOLD PREVENTION: Fast structural drying prevents mold claims down the road

Operators managing 10+ units typically see 2–5 water events per year. Let's talk about setting up a priority account.

Available for a call this week? Reply with a time or book here: [Calendar Link]

— [Owner Name] | [Company Name] | [Phone]
```

**Step 4 — Day 14: Final SMS**
```
Last reach out on this, {{contact.firstName}} — if water damage response for your properties is ever a concern, [Company Name] is the team to have on speed dial. Whenever you're ready. — [Owner Name]
```

**Step 5 — Tag:** `cold-lead` if no response after Day 14

---

### Workflow 12: Post-Job Referral Ask

**Trigger:** Pipeline stage changed (filter: new stage = Paid, any pipeline)
**Wait:** 7 days after trigger  
**Goal:** Generate warm referrals from satisfied customers

**Step 1 — 7 days after "Paid" stage: SMS**
```
Hi {{contact.firstName}} — glad we could get your home back to normal. Quick question:

Do you know anyone else who's dealt with water damage recently — or anyone who might benefit from knowing a reliable 24/7 restoration team?

If you refer someone and we do the job, we'll send you a [gift card / thank-you]. Just have them mention your name when they call.

Thanks again for trusting [Company Name]. — [Owner Name]
```

**Step 2 — Day 10 (if no referral response): No follow-up** *(One touch only for referral ask — don't over-message)*

**Step 3 — Update Contact:** Tag `referral` if they provide a name  
**Step 4 — Create Task:** "Thank {{contact.firstName}} for referral — send gift card" when referral logs

---

## WORKFLOW BUILD PRIORITY (Recommended Order)

Build these first in GHL Automation:
1. **Workflow 1** — Missed Call Text Back (immediate revenue protection)
2. **Workflow 2** — New Emergency Speed to Dispatch (core dispatch logic)
3. **Workflow 3** — Daily Drying Update (homeowner retention)
4. **Workflow 4** — Post-Job Review Request (Google reviews = marketing)
5. **Workflow 6** — Insurance Claim Nurture (longest, most revenue impact)
6. **Workflow 8** — Plumber Partner Onboarding (referral engine)

Build second:
7. **Workflow 5** — Unhappy Customer Recovery
8. **Workflow 7** — Supplement Filed Notification
9. **Workflow 9** — Plumber Partner Monthly Nurture
10. **Workflow 10** — Reconstruction Referral
11. **Workflow 11** — Property Manager Account Outreach
12. **Workflow 12** — Post-Job Referral Ask

---

## OPERATOR SETUP CHECKLIST (After Snapshot Import)

Before going live, the operator needs to:

- [ ] Set calendar open hours for all 3 calendars in Settings → Calendars
- [ ] Connect GHL phone number to Missed Call trigger
- [ ] Add Google Review link to all review request SMS/emails
- [ ] Add company name, owner name, on-call phone to all workflow templates
- [ ] Set up Internal Notification recipient (owner email/phone) in workflows
- [ ] Add Tech Daily Log Form URL in Workflow 3
- [ ] Set up Reconstruction Partner contact and phone number in Workflow 10
- [ ] Connect Google Business Profile for review monitoring (optional)
- [ ] Test Workflow 1 by calling the GHL number and letting it go to voicemail
- [ ] Verify pipeline stages load in Opportunities view

---

## SUMMARY

| Phase | Item | Count | Status |
|-------|------|-------|--------|
| 1 | Custom Fields | 21 | ✅ Built via API |
| 2 | Pipelines | 4 | ✅ Built via API |
| 3 | Calendars | 3 | ✅ Built via API |
| 4 | Tags | 31 | ✅ Built via API |
| 5 | Workflows | 12 | 📄 Documented — manual build required |

**Total automated build:** 59 items created via REST API  
**Workflow specs documented:** 12 workflows with full SMS/email copy  

---

*Build log prepared by Maximus for 1app Technologies Inc.*  
*Sub-account: Water damage restoration | Location: MLnGRbznjwLmJ517s340*
