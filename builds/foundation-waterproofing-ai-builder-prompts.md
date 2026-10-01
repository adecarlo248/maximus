# Foundation / Waterproofing Workflow AI Builder Prompts

Use these in GHL Automation → Workflows → Create Workflow → AI Builder.

Workflow 1 is NOT a workflow. Enable native Missed Call Text Back under Settings → Phone Numbers → Voicemail & Missed Call TextBack.

---

## WORKFLOW 1 — Missed Call Text Back — Native Setting

```text
Do not build this as a workflow. Enable GHL native Missed Call Text Back under Settings → Phone Numbers → Voicemail & Missed Call TextBack. Use this message: "Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — wet basement or foundation issue? Reply YES for a free inspection and we'll call you right back 👋"
```

---

## WORKFLOW 2 — New Lead Speed to Response

```text
Build a workflow called "FOUNDATION — Speed to Response" for a foundation repair and basement waterproofing company. Trigger: Contact Created OR Opportunity Created in any pipeline. Step 1: Immediately add tag "new-lead". Step 2: Immediately send SMS — "Hi {{contact.firstName}}! It's {{custom_values.owner_name}} from {{custom_values.company_name}} — we received your request about your basement. Water issues can escalate fast, especially this time of year. I'd love to get you a FREE inspection this week — what day works best? Reply here or call {{custom_values.owner_phone}}. We respond 7 days/week." Step 3: Wait 2 minutes, create internal task — "PRIORITY CALL: New foundation/waterproofing lead {{contact.firstName}} {{contact.lastName}} — {{contact.phone}}. Call now. Speed to lead is critical." Step 4: Wait 1 hour with no reply or booking, send SMS — "{{contact.firstName}} — just following up. We have inspection slots available tomorrow and Thursday. Unchecked foundation cracks can let in litres of water per day. Takes 30 min and costs nothing. Want to lock in a time? Reply YES and I'll send options. — {{custom_values.owner_name}}" Step 5: Wait 3 hours, send email with subject "Your free basement inspection — we're ready when you are" explaining that the free inspection covers foundation walls, floor cracks, cold joints, weeping tile/drainage, sump pump function, moisture entry points, and risk assessment. Include booking link {{custom_values.booking_link}} and direct phone {{custom_values.owner_phone}}. Step 6: Wait 24 hours with no reply or booking, send SMS — "Hey {{contact.firstName}}, still here when you're ready. A lot of our clients say they waited too long — and by then the repair cost doubled. No pressure, just want to make sure your home is protected. Free inspection, 30 minutes. Reply BOOK to schedule. — {{custom_values.company_name}}" Step 7: Wait 3 days, send SMS — "{{contact.firstName}} — we helped a neighbour recently with a crack that turned into a full interior drain system because it was left too long. Caught early = smaller fix. Caught late = major project. Free inspection — no commitment: {{custom_values.booking_link}}" Step 8: Wait 7 days, send email with subject "One more thing before we close your file" explaining that foundation issues rarely get better on their own, freeze-thaw cycles can worsen cracks, and they can book a free look at {{custom_values.booking_link}} or call {{custom_values.owner_phone}}. Step 9: If no reply or booking after sequence, add tag "cold-lead" and move opportunity to Follow-Up Active or Closed Lost. Stop workflow if contact replies or books.
```

## WORKFLOW 3 — Free Inspection Confirmation

```text
Build a workflow called "FOUNDATION — Free Inspection Confirmation" for a foundation repair and basement waterproofing company. Trigger: Appointment booked on the "Free Basement Inspection" calendar OR pipeline stage changes to "Free Inspection Scheduled". Step 1: Immediately remove tag "new-lead" and add tag "inspection-booked". Step 2: Immediately send SMS — "✅ Confirmed! Your free basement inspection with {{custom_values.company_name}} is booked for {{appointment.start_time}}. Our inspector will assess your foundation, weeping tile, sump pump, and any visible cracks. See you then! Questions? Text {{custom_values.owner_phone}}." Step 3: Immediately send email with subject "Your Free Basement Inspection is Confirmed ✓" explaining what to expect: foundation wall assessment, floor cracks, weeping tile condition, sump pump check, visible cracks or water entry points, 30–45 minute visit, no pressure/no obligation. Include prep instructions: have photos of water entry/cracks ready, note efflorescence or staining, and identify sump pump location. Step 4: 24 hours before appointment, send SMS — "Hi {{contact.firstName}}, quick reminder: your FREE basement inspection with {{custom_values.company_name}} is TOMORROW at {{appointment.start_time}}. See you then! Any questions? Call/text {{custom_values.owner_phone}}." Step 5: 2 hours before appointment, send SMS — "Hey {{contact.firstName}} — we're seeing you in about 2 hours for your basement inspection! Our inspector will be there at {{appointment.start_time}}. If anything comes up, text us right away: {{custom_values.owner_phone}}."
```

## WORKFLOW 4 — No-Show Recovery

```text
Build a workflow called "FOUNDATION — No-Show Recovery" for a foundation repair and basement waterproofing company. Trigger: Appointment status changes to No Show on the "Free Basement Inspection" calendar. Step 1: Immediately add tag "no-show". Step 2: Immediately send SMS — "Hi {{contact.firstName}}, we missed you at your inspection today. Hope everything's okay! We'd love to reschedule — it's free and takes 30 min. Pick a new time here: {{custom_values.booking_link}} Or text us: {{custom_values.owner_phone}}." Step 3: Wait 15 minutes, create internal task — "No-show: {{contact.firstName}} {{contact.lastName}} missed foundation inspection. Call to reschedule — do not let this lead go cold. Phone: {{contact.phone}}." Step 4: Wait 24 hours with no rebook, send SMS — "{{contact.firstName}} — still want to get that free inspection done? Your basement won't fix itself. 😄 We have openings this week: {{custom_values.booking_link}}" Stop workflow if contact rebooks or replies.
```

## WORKFLOW 5 — Post-Inspection Follow-Up

```text
Build a workflow called "FOUNDATION — Post-Inspection Follow-Up" for a foundation repair and basement waterproofing company. Trigger: Pipeline stage changes to "Inspection Complete" in the residential foundation pipeline. Step 1: Immediately add tag "estimate-sent". Step 2: Immediately send SMS — "Hi {{contact.firstName}}, thanks for having us out today! We'll have your estimate ready within 24 hours. Feel free to text any questions in the meantime: {{custom_values.owner_phone}}." Step 3: Wait 1 day, send email with subject "Your Free Basement Assessment Summary + Estimate" including inspector-filled summary placeholders for findings, recommended solution, estimate amount, next steps, financing available, and direct contact info. Step 4: Wait 3 days, send SMS — "Hey {{contact.firstName}}, just checking in — had a chance to look over the estimate? Happy to answer any questions or walk you through it by phone. {{custom_values.owner_phone}}." Step 5: Wait 5 days, send email with subject "Questions about your estimate? (payment options available)" explaining financing options, 12–24 month payment possibilities OAC, and phased repair options starting with the highest-risk area first. Step 6: Wait 7 days, send SMS — "{{contact.firstName}} — wanted to share something. A client we visited recently had a similar crack to yours. They waited one more winter, and by spring it was three times the problem. Just want to make sure we get you protected before the weather turns. Still happy to chat: {{custom_values.owner_phone}}." Step 7: Wait 14 days, send email with subject "A quick note about your foundation repair" explaining freeze-thaw crack propagation, hydrostatic pressure, mold growth risk, and how repair costs can increase when foundation water issues are left through another season. Keep tone helpful, not pushy. Step 8: Wait 21 days, send SMS — "{{contact.firstName}} — we still have your file open. We know these decisions take time. If you're ready or have questions, we're a text away. If you've decided to wait, just let us know and we'll touch base in the spring. {{custom_values.owner_phone}}." Step 9: Wait 30 days, send email with subject "Still want to protect your home?" saying this is the final follow-up for now, their assessment is on file, and they can rebook at {{custom_values.booking_link}} or call/text {{custom_values.owner_phone}}. Step 10: If no response, add tag "cold-lead" and add to 90-day re-engagement list. Exit workflow if contact replies, signs contract, pays deposit, or moves past Follow-Up Active.
```

## WORKFLOW 6 — Financing Awareness

```text
Build a workflow called "FOUNDATION — Financing Awareness" for a foundation repair and basement waterproofing company. Trigger: Pipeline stage changes to "Financing Offered" OR Estimate Amount custom field is greater than $8,000. Step 1: Immediately add tag "financing-needed". Step 2: Immediately send email with subject "Payment options for your basement project" explaining that waterproofing/foundation repair is a significant investment, flexible payment plans may be available, 0% interest financing OAC may be available through {{custom_values.financing_partner}}, and larger projects can sometimes be phased to prioritize the highest-risk area first. Step 3: Wait 3 days, send SMS — "{{contact.firstName}} — just wanted to mention, we have financing available that makes this project surprisingly manageable monthly. Worth a quick chat? {{custom_values.owner_phone}}." Step 4: Wait 7 days, send email with subject "The math on protecting your basement" explaining the cost context of financing versus water damage deductibles, mold remediation, and home value loss from disclosed water history. Include financing link {{custom_values.financing_url}} and owner phone {{custom_values.owner_phone}}. Stop if financing is declined, contract signed, or contact replies.
```

## WORKFLOW 7 — Insurance Claim Nurture

```text
Build a workflow called "FOUNDATION — Insurance Claim Nurture" for a foundation repair and basement waterproofing company. Trigger: Insurance Claim custom field changes to Yes OR tag "insurance-claim" is added. Step 1: Immediately add tag "insurance-claim". Step 2: Immediately send email with subject "Navigating your insurance claim — what to know first" explaining that many policies cover sudden and accidental water damage but may not cover gradual seepage, weeping tile failure over time, or hydrostatic pressure intrusion. Explain that sewer backup/overland water may depend on policy riders. Recommend calling the broker before the adjuster, documenting everything with photos/video, avoiding permanent repairs before adjuster approval, and getting a written contractor assessment. Step 3: Wait 2 days, send SMS — "{{contact.firstName}} — do you have your insurance policy number handy? Once your adjuster visit is confirmed, let us know the date and we can coordinate our assessment to complement theirs. {{custom_values.owner_phone}}." Step 4: Wait 5 days, send email with subject "Documentation checklist for your insurance claim" listing photos, video walkthrough, damaged item list, date first noticed, previous repairs/history, and contractor assessment. Explain that the written assessment includes cause of water entry, extent of damage, and recommended permanent solution. Create internal task — "Follow insurance claim lead: confirm adjuster date and documentation for {{contact.firstName}}." Stop if claim is closed or opportunity moves forward.
```

## WORKFLOW 8 — Post-Job Review and Referral Request

```text
Build a workflow called "FOUNDATION — Post-Job Review and Referral Request" for a foundation repair and basement waterproofing company. Trigger: Pipeline stage changes to "Paid" OR "Job Complete". Step 1: Immediately add tags "job-complete" and "review-requested" and update Review Requested field to Yes. Step 2: Immediately send SMS — "Hi {{contact.firstName}}! The team just finished up — we hope everything looks great. Could you spare 2 minutes to leave us a Google review? It means the world to a small local business: {{custom_values.google_review_link}} Thank you! — {{custom_values.company_name}}" Step 3: Wait 1 day, send email with subject "Thank you {{contact.firstName}} — one small favour?" thanking them for trusting the company, asking for a Google review, and suggesting they mention the problem, what was done, and whether they'd recommend the company. Step 4: Wait 14 days, send SMS — "{{contact.firstName}} — hope the basement has been dry! 🏠 If any friends, neighbours, or family mention water issues, wet basements, or cracks — we'd love the referral. We'll take great care of anyone you send our way. {{custom_values.company_name}} | {{custom_values.owner_phone}}" Step 5: Wait 90 days, send email with subject "Quick check-in from {{custom_values.company_name}}" asking how the basement is holding up, reminding them to report minor seepage/efflorescence early, and asking for referrals. Stop review reminders if Review Received field is Yes or tag "review-received" is added.
```

## WORKFLOW 9 — Unhappy Customer Recovery

```text
Build a workflow called "FOUNDATION — Unhappy Customer Recovery" for a foundation repair and basement waterproofing company. Trigger: Tag "unhappy-customer" is added. This workflow must be internal only and must not send customer-facing messages. Step 1: Immediately create internal task — "⚠️ PRIORITY: Unhappy customer — {{contact.firstName}} {{contact.lastName}}. Phone: {{contact.phone}}. DO NOT send automated messages. Owner must call personally within 1 hour to resolve." Step 2: Immediately send internal email to owner with subject "⚠️ Customer Issue — Immediate Attention Required" including contact name, phone, email, contact record link, and instruction to call personally within 1 hour. Step 3: Pause or suppress all other automated sequences for this contact until resolved. Step 4: Create follow-up internal task after 24 hours — "Confirm customer issue resolved and remove unhappy-customer/automation-hold tags if safe."
```

## WORKFLOW 10 — Home Inspector Referral Partner Onboarding

```text
Build a workflow called "FOUNDATION — Home Inspector Referral Partner Onboarding" for a foundation repair and basement waterproofing company. Trigger: Pipeline stage changes to "New Partner" in the Foundation Referral Partners pipeline OR tag "home-inspector-referral" is added. Step 1: Immediately add tag "home-inspector-referral". Step 2: Immediately send email with subject "Making your job easier — foundation partnership" introducing {{custom_values.owner_name}} from {{custom_values.company_name}}, explaining the challenge home inspectors face when they find foundation cracks or moisture, and offering same-week assessments, written reports with photos, honest no-pressure assessments, and protection of the inspector's credibility. Ask for a 15-minute call or coffee. Step 3: Wait 3 days with no response, send SMS — "Hi {{contact.firstName}}, {{custom_values.owner_name}} here from {{custom_values.company_name}}. Sent you an email about a referral partnership for foundation/waterproofing. Would love to connect — even just 10 min by phone. {{custom_values.owner_phone}}." Step 4: When partner agrees using manual trigger or stage change to Active Partner, send email with subject "Welcome to the partner program — here's how it works" explaining how to text homeowner name/number and a brief note, promising fast outreach, free inspection, clear written report, and updates. Include direct line {{custom_values.owner_phone}} and booking link {{custom_values.booking_link}}. Step 5: Every 30 days for active partners, send SMS — "Hi {{contact.firstName}}, {{custom_values.owner_name}} here. Quick check-in — any foundation or moisture issues come up in your inspections lately? Happy to do same-week assessments for any clients you'd like to refer. {{custom_values.owner_phone}}."
```

## WORKFLOW 11 — Spring Wet Basement Campaign

```text
Build a workflow called "FOUNDATION — Spring Wet Basement Campaign" for a foundation repair and basement waterproofing company. Trigger: Date/time based every year on April 1 OR manual launch. Audience: past leads who did not close plus past customers. Step 1: Add tag "spring-flooding". Step 2: On launch day, send SMS — "Spring flooding season is here 🌧️ If you saw water in your basement after the snow melted, you're not alone — and it's not going to fix itself. {{custom_values.company_name}} is offering FREE inspections this month. Reply SPRING to book yours." Step 3: Day 1, send email with subject "Why your basement leaked this spring (and how to stop it happening again)" explaining snow melt, frozen ground, hydrostatic pressure, saturated soil pressure, cracks becoming water channels, overwhelmed weeping tile, and sump pumps running nonstop. Include CTA to book free inspection at {{custom_values.booking_link}}. Step 4: Wait 5 days, send SMS — "{{contact.firstName}} — spring flood window is open right now. We're seeing our busiest call volume of the year. Don't wait until there's standing water. Free inspection: {{custom_values.booking_link}}" Stop if contact replies or books.
```

## WORKFLOW 12 — Fall Before the Freeze Campaign

```text
Build a workflow called "FOUNDATION — Fall Before the Freeze Campaign" for a foundation repair and basement waterproofing company. Trigger: Date/time based every year on September 15 OR manual launch. Audience: past leads who did not close, past customers, and current prospect list. Step 1: Launch day, send SMS — "Fall is the last chance for exterior waterproofing before the ground freezes. If your basement had any moisture issues this year, now is the time to fix it permanently. FREE inspection — reply FALL to book. {{custom_values.company_name}}." Step 2: Day 1, send email with subject "The window is closing — basement waterproofing before winter" explaining that exterior waterproofing can be limited once the ground freezes, October is often the last reliable month for exterior work, and warning signs include water staining, efflorescence, cracks, sump pump running often, and musty smell. Include booking link {{custom_values.booking_link}}. Step 3: Wait 7 days, send SMS — "{{contact.firstName}} — one more heads up. Our exterior waterproofing calendar is filling fast before freeze. Once the ground freezes we're interior-only until spring. Last chance: {{custom_values.booking_link}} or call {{custom_values.owner_phone}}." Step 4: Wait 14 days, send email with subject "Last call — exterior waterproofing before freeze" explaining final exterior waterproofing slots, interior work availability year-round, and CTA to book before winter. Stop if contact replies or books.
```

---

## Recommended Build Order

1. Workflow 2 — Speed to Response
2. Workflow 5 — Post-Inspection Follow-Up
3. Workflow 3 — Free Inspection Confirmation
4. Workflow 8 — Post-Job Review + Referral
5. Workflow 9 — Unhappy Customer Recovery
6. Workflow 4 — No-Show Recovery
7. Workflow 6 — Financing Awareness
8. Workflow 7 — Insurance Claim Nurture
9. Workflow 10 — Home Inspector Partner Onboarding
10. Workflow 11 — Spring Campaign
11. Workflow 12 — Fall Campaign

