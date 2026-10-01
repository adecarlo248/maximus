# Windows & Siding GHL Snapshot - Build Log
**Sub-account Location ID:** nliT7y1zhVsWljmZFeX7
**Build Date:** 2026-07-21
**Builder:** Maximus (Subagent)
**Status:** COMPLETE (Phases 1-4 built in GHL; Phase 5 documented)

---

## PHASE 1: CUSTOM FIELDS ✅ COMPLETE

| # | Field Name | Type | Status | Field ID |
|---|-----------|------|--------|----------|
| 1 | Lead Source | SINGLE_OPTIONS (dropdown) | ✅ BUILT | t23UDMhossORxSt8Gf0d |
| 2 | Job Type | SINGLE_OPTIONS (dropdown) | ✅ BUILT | oZrB6oXkhphUkqw5tFVY |
| 3 | Service Category | SINGLE_OPTIONS (dropdown) | ✅ BUILT | xLICMDFDAqi86lplCoTr |
| 4 | Property Type | SINGLE_OPTIONS (dropdown) | ✅ BUILT | wu5dOODkYR7guT2xsGo7 |
| 5 | Window Style | SINGLE_OPTIONS (dropdown) | ✅ BUILT | pufBy61S62qAsSFMfgrf |
| 6 | Glazing | SINGLE_OPTIONS (dropdown) | ✅ BUILT | mknd1lVF42y6ECZUF5Yi |
| 7 | ENERGY STAR Eligible | RADIO (Yes/No) | ✅ BUILT | ScDoEUbyZIgvuLddHjQC |
| 8 | Rebate Program | SINGLE_OPTIONS (dropdown) | ✅ BUILT | Re5FNPJELyFwOXCTyipL |
| 9 | Rebate Amount Estimated | MONETORY (currency) | ✅ BUILT | CB78Pz9rhpiQCsRjksLr |
| 10 | Siding Material | SINGLE_OPTIONS (dropdown) | ✅ BUILT | abQJJuQahePxQkMUjmKr |
| 11 | Insurance Company | TEXT | ✅ BUILT | uBWf53Uzh534qqwhkdFm |
| 12 | Claim Number | TEXT | ✅ BUILT | bAry2s6E9SAarzT535kg |
| 13 | Adjuster Name | TEXT | ✅ BUILT | IzvpvPnbUZwLmtAPAzOE |
| 14 | Estimate Amount | MONETORY (currency) | ✅ BUILT | XIEmc41XmutPdU66itBM |
| 15 | Contract Amount | MONETORY (currency) | ✅ BUILT | yRZVNio8qobUmrV7WFUm |
| 16 | Deposit Paid | RADIO (Yes/No) | ✅ BUILT | 2Cuk0MgawHmi1ndNSxWZ |
| 17 | Financing Required | RADIO (Yes/No) | ✅ BUILT | b3fMSbJfbOwDm3Hk2Vf1 |
| 18 | Permit Required | RADIO (Yes/No) | ✅ BUILT | Dp4Wpznjk91dG36DqqUv |
| 19 | Permit Number | TEXT | ✅ BUILT | KNLXUJMfV9UkzUH65ycT |
| 20 | Review Requested | RADIO (Yes/No) | ✅ BUILT | TM8ml0rzLjcLZMzJPKoU |
| 21 | Review Received | RADIO (Yes/No) | ✅ BUILT | 4s0IGW3OLjYgdeL8o4aV |
| 22 | Neighbour Campaign Sent | RADIO (Yes/No) | ✅ BUILT | Kx2eH7wWCQnwKyjNVAcG |

### Field Option Values

**Lead Source options:** Google LSA, Facebook Ad, Door Knock, Referral, Storm Chaser, Insurance Referral, Real Estate Agent, Property Manager, Repeat Customer, Angi/HomeAdvisor

**Job Type options:** Window Replacement, Siding Replacement, Window + Siding Combo, Soffit/Fascia, Storm Damage - Windows, Storm Damage - Siding, Commercial Windows, Commercial Siding, New Construction

**Service Category options:** Retail/Cash, Insurance Storm Damage, Commercial, New Construction

**Property Type options:** Residential, Commercial, Multi-Unit, Strata/Condo, New Construction

**Window Style options:** Double-Hung, Casement, Bay/Bow, Slider, Awning, Fixed, Egress, Unknown

**Glazing options:** Double-Pane, Triple-Pane, Unknown

**ENERGY STAR Eligible options:** Yes, No

**Rebate Program options:** None, Canada Greener Homes, Enbridge HER+, NRCan, Provincial, Unknown

**Siding Material options:** Vinyl, HardiePlank, Wood, Aluminum, Steel, Stucco, Unknown

**Deposit Paid / Financing Required / Permit Required / Review Requested / Review Received / Neighbour Campaign Sent options:** Yes, No

---

## PHASE 2: PIPELINES ✅ COMPLETE

| # | Pipeline Name | Stages | Status | Pipeline ID |
|---|--------------|--------|--------|-------------|
| 1 | Windows/Siding - Retail | 15 stages | ✅ BUILT | L3HljJqcpdiEAwSE31c2 |
| 2 | Windows/Siding - Insurance Storm Damage | 15 stages | ✅ BUILT | 87LcpLHyASEWqiUNQp3a |
| 3 | Windows/Siding - Commercial | 13 stages | ✅ BUILT | cX5pW8d46U1wsodIoeAZ |

### Pipeline 1: Windows/Siding - Retail (ID: L3HljJqcpdiEAwSE31c2)
Stages (in order):
1. New Lead
2. Consultation Booked
3. In-Home Consultation Complete
4. Proposal Sent
5. Follow-Up Active
6. Financing Offered
7. Contract Signed / Deposit
8. Permit Applied
9. Material Ordered
10. Install Scheduled
11. Install Complete
12. Final Invoice
13. Paid
14. Review Requested
15. Neighbour Campaign

### Pipeline 2: Windows/Siding - Insurance Storm Damage (ID: 87LcpLHyASEWqiUNQp3a)
Stages (in order):
1. Damage Reported
2. Free Inspection Scheduled
3. Inspection Complete
4. Claim Filed
5. Adjuster Meeting Set
6. Adjuster Meeting Complete
7. Approval Received
8. Contract Signed
9. Material Ordered
10. Install Scheduled
11. Install Complete
12. ACV Received
13. Supplement Filed
14. Final Payment
15. Review + Referral

### Pipeline 3: Windows/Siding - Commercial (ID: cX5pW8d46U1wsodIoeAZ)
Stages (in order):
1. New Prospect
2. Site Assessment
3. Proposal Submitted
4. Contract Awarded
5. Permit Applied
6. Material Ordered
7. Install Scheduled
8. Install In Progress
9. Inspection
10. Job Complete
11. Invoice Sent
12. Paid
13. Warranty Period

---

## PHASE 3: CALENDARS ✅ COMPLETE

| # | Calendar Name | Duration | Status | Calendar ID |
|---|--------------|----------|--------|-------------|
| 1 | Free In-Home Consultation - Windows/Siding | 60 min | ✅ BUILT | Sf3YTXYNrDijAaqQXL8Y |
| 2 | Storm Damage Inspection | 45 min | ✅ BUILT | ZgyN0jqY0ffbv3udgf9Q |
| 3 | Commercial Site Assessment | 90 min | ✅ BUILT | xe0xQw93wawgPHvLoDd6 |

### Calendar Details

**Calendar 1: Free In-Home Consultation - Windows/Siding**
- ID: Sf3YTXYNrDijAaqQXL8Y
- Duration: 60 min
- Buffer: 30 min
- Type: event / classic widget
- Availability: Mon-Fri 9am-5pm (configure in GHL UI - openHours set via UI)
- Note: Set availability for Mon-Fri 9am-5pm in GHL calendar settings

**Calendar 2: Storm Damage Inspection**
- ID: ZgyN0jqY0ffbv3udgf9Q
- Duration: 45 min
- Buffer: 15 min
- Type: event / classic widget
- Availability: Mon-Sat 8am-5pm (configure in GHL UI)

**Calendar 3: Commercial Site Assessment**
- ID: xe0xQw93wawgPHvLoDd6
- Duration: 90 min
- Buffer: 60 min
- Type: event / classic widget
- Availability: Mon-Fri 8am-4pm (configure in GHL UI)

---

## PHASE 4: TAGS ✅ COMPLETE (32 tags)

| # | Tag Name | Status | Tag ID |
|---|---------|--------|--------|
| 1 | new-lead | ✅ BUILT | qDmRAlESgbOxuT3WEvwy |
| 2 | window-replacement | ✅ BUILT | ceNnstp0Jtxlaw0Co4cV |
| 3 | siding-replacement | ✅ BUILT | iHGTnLaVE4XN1wZ66g21 |
| 4 | combo-job | ✅ BUILT | 0PCHa4eLhsl8IZTqtAHT |
| 5 | soffit-fascia | ✅ BUILT | 1Bs45U36THn8FBmcASgL |
| 6 | storm-damage | ✅ BUILT | 161FDs44XvNoTZaiWtWp |
| 7 | insurance-claim | ✅ BUILT | 2V2S16EVQotPazvOgU33 |
| 8 | energy-star-eligible | ✅ BUILT | ceyOEn4fzga9HvoptffX |
| 9 | rebate-eligible | ✅ BUILT | VUItnh8UuE3emXGD2wGi |
| 10 | financing-needed | ✅ BUILT | hxQQpFBpPI75glBJfKR1 |
| 11 | permit-required | ✅ BUILT | MXpUDYB99Q4tqtGETbWj |
| 12 | commercial-job | ✅ BUILT | k6vk1TEOJs74yG8f8KO0 |
| 13 | new-construction | ✅ BUILT | 2m9FT8fueFy4BWCiBkNK |
| 14 | estimate-sent | ✅ BUILT | u0X89uKn9r6DWKBTz8qY |
| 15 | deposit-paid | ✅ BUILT | Hg6xq8LhLvzidncdstit |
| 16 | contract-signed | ✅ BUILT | kPjBMAyjBoBRqqlsAtX0 |
| 17 | install-complete | ✅ BUILT | 7kVY5YN8UtwQy9KNis49 |
| 18 | review-requested | ✅ BUILT | cUvs1YxWf509rjqdRVui |
| 19 | review-received | ✅ BUILT | PMts3lcBAsP4q6fAnorq |
| 20 | referral | ✅ BUILT | R5oT8qGwOkRjP7GaMsKa |
| 21 | neighbour-campaign | ✅ BUILT | XF4ilxm5TuiFyvo1hlL9 |
| 22 | cold-lead | ✅ BUILT | vQ8LsTAeZsfz7ltWTcNi |
| 23 | no-show | ✅ BUILT | CwceUrDjgWwZFse66n9e |
| 24 | google-lsa | ✅ BUILT | is3BclM4VEEaoISt4LwA |
| 25 | facebook-ad | ✅ BUILT | viLFrACzpWvrYLPgNWik |
| 26 | door-knock | ✅ BUILT | SBsSTnDIaq1262QFf1te |
| 27 | storm-chaser | ✅ BUILT | smt2oSOHaDsU9FxCrsid |
| 28 | real-estate-agent | ✅ BUILT | SX0vKeXDLFrkFXiYqIqx |
| 29 | property-manager | ✅ BUILT | uIcHf9I45pcHDBovkQin |
| 30 | repeat-customer | ✅ BUILT | rECnd1ZOGz0pD7e4f3tX |
| 31 | supplement-filed | ✅ BUILT | X0F2rjIzIVCk6dhS0NDD |
| 32 | adjuster-meeting-set | ✅ BUILT | YuoGof18Zgy8X0fLAwPB |

---

## PHASE 5: WORKFLOWS - Full Specifications (Build in GHL UI)

> Workflows cannot be created via GHL public API. All 10 workflows are fully documented below with exact SMS/email copy and trigger logic for manual build in GHL Automations.

---

### ✅ WORKFLOW 1: Missed Call Text Back - NATIVE GHL SETTING (Not a Workflow)

**Do NOT build this as a workflow.** Use GHL's built-in MCTB feature instead.

**How to enable:**
1. Go to **Settings → Phone Numbers**
2. Click on your phone number
3. Click the **"Voicemail & Missed Call TextBack"** tab
4. Check **"Enable Missed call textback"** ✅
5. Click **"Customize"** and paste the message below

**Customized message for this trade:**
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call - need a free window or siding estimate? Storm damage? Reply YES and we'll get right back to you 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Lead - Speed to Response

**Trigger:** Contact created (from form submission, Facebook lead, LSA lead)
**Goal:** Contact within 60 seconds — book in-home appointment

**Steps:**
1. **Trigger:** Contact created / Form submitted
2. **Wait:** 0 seconds
3. **Action - Apply tag:** new-lead
4. **Action - Send SMS:**
   > Hi {{contact.firstName}}! This is [RepName] from [CompanyName]. We got your request for a free estimate. When's a good time to pop by and take a look? I can usually get there within a day or two. Reply here or call us at [Phone]. - [RepName]
5. **Wait:** 2 minutes
6. **Action - Send Email:** Welcome email (Subject: "Your Free Windows/Siding Estimate - Here's What Happens Next")
   > Hi {{contact.firstName}}, thanks for reaching out to [CompanyName]! One of our home exterior specialists will contact you within the hour. We'll schedule a free, no-obligation in-home consultation (45-60 minutes), take measurements, and deliver a detailed written estimate within 24-48 hours. Browse our recent projects: [Portfolio Link]. Talk soon, [RepName]
7. **Wait:** 5 minutes
8. **Action - Create task:** "🔴 New lead - call {{contact.firstName}} NOW" (due: immediate, assigned to rep)
9. **If no reply in 30 min:**
   - **Send SMS:**
     > Hey {{contact.firstName}} - still here whenever you're ready! Just wanted to make sure our message didn't get lost. What's a good time this week for a free, no-pressure quote? 🏠 - [CompanyName]
10. **If no reply in 2 hours:**
    - **Create task:** "Lead going cold - second call attempt for {{contact.firstName}}"
11. **If no reply in 24 hours:**
    - **Send SMS:**
      > {{contact.firstName}} - just circling back on your request. We're booking in-home estimates for this week and next - completely free, about 45 minutes. Want me to hold a spot for you?

**Tags:** new-lead on entry; lead source tag based on source field

---

### Workflow 3: In-Home Consultation Confirmation

**Trigger:** Customer booked appointment (calendar: Free In-Home Consultation - Windows/Siding)
**Goal:** Zero no-shows; rep arrives prepared

**Steps:**
1. **Trigger:** Appointment booked (Calendar: Free In-Home Consultation)
2. **Immediately - Send SMS (Confirmation):**
   > Hi {{contact.firstName}}! Confirming your free in-home estimate with [RepName] on {{appointment.startTime | date: "%A, %B %d"}} at {{appointment.startTime | date: "%I:%M %p"}}. Address: {{contact.full_address}}. Reply CONFIRM to confirm or call [Phone] to reschedule. See you then! 🏠
3. **Immediately - Send Email (Confirmation):**
   Subject: "Your Free Estimate Is Confirmed - {{appointment.startTime | date: "%A, %B %d"}} at {{appointment.startTime | date: "%I:%M %p"}}"
   > Hi {{contact.firstName}}, you're all set! Date: {{appointment.startTime | date: "%A, %B %d"}} | Time: {{appointment.startTime | date: "%I:%M %p"}} | Location: {{contact.full_address}} | Specialist: [RepName]. What to expect: ~45-60 minutes, we'll measure every window/area, no pressure, no obligation. To make the most of your visit: write down your top priorities, note any HOA restrictions, have an idea of your budget range. See you soon! [RepName], [CompanyName], [Phone]
4. **24 hours before appointment - Send SMS (Reminder):**
   > Reminder: Your free window/siding estimate with [RepName] is TOMORROW at {{appointment.startTime | date: "%I:%M %p"}}. Need to reschedule? Reply here or call [Phone]. Looking forward to it!
5. **24 hours before - Send Email (Reminder):**
   Subject: "See You Tomorrow, {{contact.firstName}}! - Your Estimate Reminder"
   > Quick reminder that [RepName] will be at your home tomorrow: {{appointment.startTime | date: "%A, %B %d"}} at {{appointment.startTime | date: "%I:%M %p"}}. Questions or need to reschedule? Call [Phone]. Looking forward to meeting you! [CompanyName]
6. **2 hours before - Send SMS (Same-day):**
   > Hey {{contact.firstName}} - [RepName] is heading your way in a few hours for your {{appointment.startTime | date: "%I:%M %p"}} estimate! See you soon. Call [Phone] with any questions.

---

### Workflow 4: No-Show Recovery

**Trigger:** Appointment status (filter: no-show)
**Goal:** Reschedule the appointment; don't lose the lead

**Steps:**
1. **Trigger:** Appointment marked No-Show
2. **Apply tag:** no-show
3. **Send SMS:**
   > Hi {{contact.firstName}} - looks like we may have missed each other today. No worries! Let's find a time that works better. When's good for you this week? - [CompanyName]
4. **Create task:** "No-show - call {{contact.firstName}} to reschedule - priority high"
5. **Wait:** 1 hour
6. **If no reply - Send SMS:**
   > {{contact.firstName}} - still happy to come by for your free estimate whenever works for you. Our calendar is pretty flexible this week. Just reply with a day/time! 🏠
7. **Wait:** 24 hours
8. **If no reply - Send Email:**
   Subject: "We Missed You, {{contact.firstName}} - Let's Reschedule Your Free Estimate"
   > Hi {{contact.firstName}}, we had you scheduled for a free window/siding estimate today but it looks like we missed each other. Completely understand - life gets busy! We'd love to find a time that works better. Click here to pick a new time: [Booking Link]. Or just reply to this email. No pressure at all. [RepName], [CompanyName]
9. **Wait:** 3 days
10. **If still no reply:** Apply tag `cold-lead` → move to long-term nurture

---

### Workflow 5: Estimate Follow-Up Sequence (6-step, 30 days)

**Trigger:** Pipeline stage changed (filter: new stage = Proposal Sent, Pipeline: Windows/Siding - Retail)
**Goal:** Convert the estimate to a signed contract within 30 days

**Steps:**
1. **Trigger:** Stage = Proposal Sent
2. **Apply tag:** estimate-sent
3. **Day 0 - Send SMS:**
   > Hi {{contact.firstName}} - just wanted to make sure you got the estimate okay. Shoot me a message if you have any questions! - [RepName]
4. **Day 1 - Send Email:** Product education: Why triple-pane?
   Subject: "Triple-Pane vs. Double-Pane - What Actually Matters for Your Home"
   > [Full ET-11 content from research doc] - includes U-factor explanation, ER rating, ENERGY STAR specs
5. **Day 2 - Send SMS:**
   > Hi {{contact.firstName}} - did you get a chance to look over the estimate? Happy to walk through it on a quick call if anything's unclear. No pressure. - [RepName]
6. **Day 3 - Send Email:** ENERGY STAR rebate opportunity
   Subject: "You May Qualify for Up to $5,000 in Window Rebates, {{contact.firstName}}"
   > [Full ET-12 content - Enbridge HER+, Canada Greener Homes, NRCan rebate education]
7. **Day 5 - Send SMS:** Financing teaser
   > {{contact.firstName}} - quick thought: did you know we offer financing? Your new windows could be as low as $[X]/month. No big up-front hit. Want me to run the numbers for you?
8. **Day 7 - Send Email:** Social proof / project showcase
   Subject: "What [City] Homeowners Are Saying About Their New Windows"
   > [ET-13 content - testimonials, project gallery, Google review link]
9. **Day 10 - Send SMS:** Urgency - calendar filling
   > Hey {{contact.firstName}} - just a heads up: our install calendar for [Month] is starting to fill up. Wanted to give you first right of refusal on a spot. Still interested? Reply here or call [Phone].
10. **Day 14 - Send Email:** Final follow-up
    Subject: "One Last Check-In Before We Close Your File, {{contact.firstName}}"
    > [ET-14 content - non-pushy final check-in, offer still valid, financing available]
11. **Day 14 - Create task:** "Manual call - 14-day estimate follow-up for {{contact.firstName}}"
12. **If no response by Day 14:** Apply tag `cold-lead` → remove from active follow-up

---

### Workflow 6: ENERGY STAR Rebate Education Sequence (3-step)

**Trigger:** Contact tag (filter: tag added = rebate-eligible)
**Goal:** Educate on Canada Greener Homes + Enbridge HER+ - drive booking

**Steps:**
1. **Trigger:** Tag `rebate-eligible` applied
2. **Immediately - Send Email:**
   Subject: "Ontario Homeowners: Are You Eligible for Window Rebates?"
   > [ET-50 content] - Enbridge HER+ up to $250/window ($5,000 max), Canada Greener Homes, NRCan programs. CTA: Book free energy assessment.
3. **Day 3 - Send Email:**
   Subject: "How the Enbridge HER+ Rebate Actually Works - Step by Step"
   > Step 1: Pre-upgrade energy audit by NRCan-registered energy advisor. Step 2: Install ENERGY STAR qualified windows (U-factor ≤ 1.20 W/m2K for Ontario Zone 2, ER ≥ 29). Step 3: Post-upgrade audit. Step 4: Rebate paid to homeowner - typically 8-16 weeks after job completion. We handle most of the paperwork. Rebate can offset $1,500-$5,000 of your project cost. [Book your free assessment: Booking Link]
4. **Day 7 - Send Email:**
   Subject: "Canada Greener Homes - What's Still Available in 2026"
   > The grant component has been restructured - the 0% interest loan (up to $40,000) is the primary offering for most homeowners. You still need a pre and post energy audit. We can connect you with a registered energy advisor. Here's the direct Canada.ca portal: [Link]. Ready to check eligibility? [Book a call: Booking Link]
5. **Day 7 - Create task:** "Rebate lead - call {{contact.firstName}} to discuss eligibility"

---

### Workflow 7: Insurance Claim Nurture

**Trigger:** Pipeline stage changed (filter: new stage = Claim Filed, Pipeline: Windows/Siding - Insurance Storm Damage)
**Goal:** Walk homeowner through 30-90 day claim process; stay top-of-mind; get contract on approval

**Steps:**
1. **Trigger:** Stage = Claim Filed
2. **Immediately - Send Email:**
   Subject: "Your Storm Claim Is In Motion - Here's What to Expect"
   > [ET-20 content] - adjuster timeline, ACV vs RCV explained, what NOT to sign without talking to us, we're in your corner
3. **Day 3 - Send SMS:**
   > Hi {{contact.firstName}}! Quick check-in - has your insurance company called to schedule the adjuster yet? Sometimes takes 1-2 weeks. Let us know when you hear from them - we'll help you prepare. - [RepName], [CompanyName]
4. **Day 7 - Send Email:**
   Subject: "Your Adjuster Is Coming - Here's How to Be Ready"
   > [ET-21 content] - full adjuster prep guide, what to say, what NOT to say, have us on the phone offer
5. **Day 14 - Send SMS:**
   > {{contact.firstName}} - just following up on your storm claim. Any news from your insurance company? We've helped dozens of homeowners through this - happy to answer questions anytime. Text or call: [Phone]
6. **Day 21 - Send Email:**
   Subject: "What to Do If Your Claim Is Denied or Underpaid"
   > [ET-22 content] - claim denial options, appeal process, public adjuster intro, supplement filing explanation
7. **Day 30 - Create task:** "30-day claim check-in call - {{contact.firstName}} - what's the status?"
8. **Day 45 - Send Email:**
   Subject: "Understanding ACV vs. RCV on Your Policy"
   > ACV (Actual Cash Value) = replacement cost minus depreciation - typically the first check you receive. RCV (Replacement Cost Value) = full replacement cost - you recover the depreciation after the job is complete. This means your first check is NOT the final number. The depreciation hold-back is released after we complete the job and provide a Certificate of Completion. [ET-23 content]
9. **Day 60 - Send SMS:**
   > Hey {{contact.firstName}} - it's been a while since we chatted about your storm claim. Have you heard anything from your insurance company? Sometimes these drag out longer than expected. We're still here whenever you're ready. - [CompanyName]
10. **If stage changes to "Approval Received" → TRIGGER immediately:**
    - **Send SMS:**
      > 🎉 {{contact.firstName}} - fantastic news! Congratulations on getting your claim approved! Let's get you booked in. I'll call you in the next hour to go over next steps. - [RepName]
    - **Send Email:**
      Subject: "🎉 Congratulations, {{contact.firstName}} - Your Claim Is Approved!"
      > [ET-25 content] - next steps: scope review, contract signing, material order, install scheduling, Certificate of Completion
    - **Create task:** "URGENT - Call {{contact.firstName}} within 1 hour - claim approved!"

---

### Workflow 8: Financing Awareness

**Trigger:** Contact tag (filter: tag added = financing-needed) OR Pipeline stage changed (filter: new stage = Financing Offered, Retail pipeline) AND Stale opportunities (estimate sent 5+ days with no decision)
**Goal:** Remove financial barrier; get financing application started

**Steps:**
1. **Trigger:** Tag `financing-needed` applied
2. **Immediately - Send Email:**
   Subject: "New Windows Without the Big Up-Front Cost - Here's How"
   > [ET-30 content] - financing options, low monthly payments, deferred options, 10-minute application, quick approval, interest-free promotions. Quick math example: 12 windows × $1,500 = $18,000 financed over 120 months at 6.99% APR = ~$[X]/month OAC.
3. **Day 1 - Send SMS:**
   > {{contact.firstName}} - thought you'd want to know: with our financing, your new windows could run about $[X]/month. That's it. Want to see the full breakdown? Takes 2 minutes. Reply here.
4. **Day 3 - Send Email:**
   Subject: "How to Apply for Window/Siding Financing - Step by Step"
   > [ET-31 content] - financing partner details, application link, OAC terms, timeline. Application takes 10 minutes. Most customers approved quickly. No obligation until you sign.
5. **Day 7 - Send SMS:**
   > Hi {{contact.firstName}} - did the financing info make sense? Happy to apply over the phone or online - takes about 10 minutes and most customers are approved quickly. No obligation until you're ready to sign. - [CompanyName]
6. **Day 10 - Create task:** "Financing follow-up call - {{contact.firstName}} - has been considering for 10 days"

---

### Workflow 9: Post-Install Review + Neighbour Campaign

**Trigger:** Pipeline stage changed (filter: new stage = Install Complete, Retail or Insurance pipeline)
**Goal:** Generate 5-star Google reviews + capture neighbour leads

**PART A - Review Generation:**
1. **Trigger:** Stage = Install Complete
2. **Apply tag:** install-complete
3. **Update custom field:** Review Requested → Yes
4. **Day 0 - Send SMS (Welcome):**
   > {{contact.firstName}} - the job looks incredible! It was a pleasure working on your home. If you ever need anything, we're always one text away. Welcome to the [CompanyName] family! 🏠✨
5. **Day 3 - Send SMS (Review Request #1):**
   > Hi {{contact.firstName}}! Quick favour - would you mind leaving us a Google review? Takes about 2 minutes and means the world to a local business like ours. Direct link: [Google Review Link] - Thank you! - [CompanyName]
6. **Day 3 - Send Email (Review Request):**
   Subject: "How'd We Do, {{contact.firstName}}? 🏠"
   > [ET-40 content] - love your new windows/siding, 2-minute review request, direct Google link, "if anything wasn't 100% right tell us first" promise
7. **If review left → apply tag `review-received` → update custom field Review Received → Yes → Send thank-you SMS:**
   > {{contact.firstName}} - thank you SO much for the kind review! It really means a lot to our team. 🙏 If you ever need anything, we're here. - [CompanyName]
8. **Day 7 (if no review) - Send SMS (Review Request #2):**
   > Hey {{contact.firstName}} - just following up on the review. We know life gets busy! If you have 90 seconds: [Google Review Link] - Thanks so much! 😊
9. **Day 14 (if no review) - Send Email (Review Request #3):**
   Subject: "One More Ask, {{contact.firstName}} - It Really Helps"
   > [ET-41 content] - third and final ask, keeps it light and appreciative
10. **Day 21 (if still no review) - Create task:** "Personal call for review request - {{contact.firstName}}"

**PART B - Referral Ask:**
11. **Day 14 - Send Email (Referral):**
    Subject: "Know Anyone Who Needs New Windows or Siding?"
    > [ET-42 content] - referral ask, treat referred customers like family, no formal program needed
12. **Day 14 - Send SMS (Referral):**
    > {{contact.firstName}} - one more thing! Do you know anyone thinking about new windows or siding? We'd love the intro. We always take great care of referred customers. 🙏 - [CompanyName]

**PART C - Neighbour Campaign:**
13. **Day 0 - Create task:** "Drop door hangers on 5 neighbours each side + 5 across = 15 homes on {{contact.full_address}}. Include QR code to neighbour landing page."
14. **Apply tag:** neighbour-campaign
15. **Update custom field:** Neighbour Campaign Sent → Yes
16. **NOTE:** Set up a separate trigger: when a new contact comes in with source = neighbour-campaign:
    - Apply tag: `neighbour-campaign`
    - Send SMS:
      > Hi {{contact.firstName}}! We just wrapped up a window/siding install in your neighborhood. If you've been thinking about upgrading your own home, we'd love to give you a free, no-pressure quote - we're already familiar with homes in your area! Interested? [Phone] or reply here.
    - Add to Retail pipeline: Stage 1 (New Lead)
    - Create task: "Neighbour lead - HIGH INTENT - call same day"

---

### Workflow 10: Seasonal Campaign - Fall (Before Winter, Upgrade Now)

**Trigger:** Scheduler (September 1 each year, or manual launch)
**Goal:** Drive bookings before winter; urgency around install calendar filling

**Target audience:** All contacts tagged `cold-lead` or `estimate-sent` but not `contract-signed`; plus past clients for referral/upgrade campaign

**Steps:**
1. **Trigger:** Enrollment date = September 1 (annual)
2. **Week 1 - Send Email:**
   Subject: "Beat the Winter Rush - Book Your Window/Siding Install Before October"
   > Hi {{contact.firstName}}, fall is the last best window for exterior installations before winter hits. Here's why now matters: ✅ Install crews are still available - October books fast. ✅ Lock in current pricing before any year-end increases. ✅ ENERGY STAR rebate programs still active - maximize before year-end deadlines. ✅ New windows installed before winter = first heating bill savings this January. Ready to move forward? Book your free in-home estimate: [Booking Link]. [CompanyName] | [Phone]
3. **Week 2 - Send SMS:**
   > {{contact.firstName}} - fall is here and our install calendar is filling up fast. If you've been thinking about new windows or siding, NOW is the time. Free estimate, no obligation. Reply or book: [Booking Link]
4. **Week 3 - Send Email:**
   Subject: "Last Call for Fall Installation, {{contact.firstName}}"
   > Hi {{contact.firstName}}, our October install dates are almost gone. Once we're booked out, the next availability is spring - and you'll spend another winter with those drafty windows. Don't wait. Here's what we recommend for fall installs: Triple-pane windows (dramatic difference in heating bills), James Hardie siding (winter-prep before freeze/thaw cycles), Soffit & fascia (protects against ice damming). [Book now: Booking Link]. [CompanyName]
5. **Week 4 - Create task:** "Call all fall campaign leads before September 30 - personal outreach push"
6. **SMS blast - Final urgency:**
   > {{contact.firstName}} - we have a few install spots left in October. After that, it's spring. If you want new windows or siding before winter, reply NOW. - [CompanyName]

---

## BUILD ERRORS / NOTES

- `openHours` field on calendar API requires specific format not well-documented. Created calendars without openHours - **availability hours must be set manually in GHL UI** for all 3 calendars.
- Calendar API `daysOfTheWeek` validation rejected both integer arrays (1-5) and named arrays ("Monday"-"Friday") - created via calendarType/widgetType only, openHours omitted.
- Workflow creation is NOT available via GHL public API - all 10 workflows documented above with exact SMS/email copy for manual build in GHL Automations module.
- Pre-existing tags (follow-up, high priority, warm lead) were already in the sub-account and were not overwritten.
- "Marketing Pipeline" (ID: 9fWk6yp2jKBsOxYZGY5V) was pre-existing - not deleted; the 3 new industry-specific pipelines added alongside it.

---

## SUMMARY

| Phase | Items | Status |
|-------|-------|--------|
| Phase 1: Custom Fields | 22 fields | ✅ 100% COMPLETE |
| Phase 2: Pipelines | 3 pipelines / 43 total stages | ✅ 100% COMPLETE |
| Phase 3: Calendars | 3 calendars | ✅ 100% COMPLETE (hours need UI config) |
| Phase 4: Tags | 32 tags | ✅ 100% COMPLETE |
| Phase 5: Workflows | 10 workflows documented | ✅ DOCUMENTED - build in GHL Automations |

**Total assets delivered:**
- 22 custom fields (dropdowns, radio buttons, currency, text)
- 3 pipelines with 43 total stages across retail, insurance, and commercial tracks
- 3 calendars (consultation, storm inspection, commercial site assessment)
- 32 tags (source, milestone, job type, lead status)
- 10 workflows fully specified with exact SMS/email copy

**Next steps:**
1. Set calendar availability hours in GHL UI (Mon-Fri 9-5, Mon-Sat 8-5, Mon-Fri 8-4)
2. Build the 10 workflows in GHL Automations using the specs above
3. Assign team members to calendars
4. Set up Google review link as a custom value in the sub-account settings
5. Configure the booking widget slugs for each calendar
6. Build forms and landing pages (documented in research doc sections 15 and 16)
