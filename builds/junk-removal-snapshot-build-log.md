# Junk Removal GHL Snapshot — Build Log
**Sub-account:** Junk removal (Peterborough, ON)
**Location ID:** `5kSsYpEfVDnIkH3Jz0q4`
**Bearer Token:** `pit-cc82fc93-4551-4345-9023-06bf43736817`
**Build Date:** 2026-07-21
**Built by:** Maximus (subagent)

---

## BUILD STATUS

| Phase | Status | Count |
|-------|--------|-------|
| Phase 1: Custom Fields | ✅ COMPLETE | 15/15 |
| Phase 2: Pipelines | ✅ COMPLETE | 4/4 |
| Phase 3: Calendars | ✅ COMPLETE | 2/2 |
| Phase 4: Tags | ✅ COMPLETE | 35/35 |
| Phase 5: Workflows (documented) | ✅ COMPLETE | 10/10 |

---

## PHASE 1: CUSTOM FIELDS

All created under model: `contact` | Endpoint: `GET/POST /locations/{locationId}/customFields`

| # | Field Name | Type | GHL DataType | Field ID |
|---|-----------|------|-------------|---------|
| 1 | Lead Source | Dropdown | SINGLE_OPTIONS | `g5yY2G0mE8w3N8xQ5bmA` |
| 2 | Job Type | Dropdown | SINGLE_OPTIONS | `rvPybPEbgc4YpaHwj3Ll` |
| 3 | Service Category | Dropdown | SINGLE_OPTIONS | `LBNX99s4gXCnVNnAwRUp` |
| 4 | Property Type | Dropdown | SINGLE_OPTIONS | `iIWZWTpP25szNb12ZQ59` |
| 5 | Load Size | Dropdown | SINGLE_OPTIONS | `ujcywDDulVUymGOZIoRz` |
| 6 | Same Day Available | Yes/No | RADIO | `hcCuC9pDHk0m1rbiwXZW` |
| 7 | Donation Items Present | Yes/No | RADIO | `MQiMMdeOJbjN59P8s2vk` |
| 8 | Hazardous Materials | Yes/No | RADIO | `2o27iUAzUPsb6BOMJvmr` |
| 9 | Estimate Amount | Currency | MONETORY | `yE2jdMCf3R0FjFpj4EUY` |
| 10 | Invoice Amount | Currency | MONETORY | `Um4lU0cDRSCXBUAxUDFy` |
| 11 | Crew Size | Dropdown | SINGLE_OPTIONS | `6nvBkHM0qiTxEfHhlpZX` |
| 12 | Job Date | Date | DATE | `cI5aCHUE9o16XqkdBJAp` |
| 13 | Review Requested | Yes/No | RADIO | `6jFXJZebCNWU6DsdCRpZ` |
| 14 | Review Received | Yes/No | RADIO | `Z14NY5Bk6gWTd5s1MUjb` |
| 15 | Referral Partner Type | Dropdown | SINGLE_OPTIONS | `yGTGEfJYYWaAnS0hI1qd` |

### Custom Field Option Values

**Lead Source options:**
Google LSA, Google Organic, Kijiji/Craigslist, Facebook Marketplace, Referral, Real Estate Agent, Property Manager, Moving Company, Renovation Contractor, Repeat Customer

**Job Type options:**
Residential Cleanout, Estate Cleanout, Hoarder Cleanout, Appliance Removal, Furniture Removal, Demolition Debris, E-Waste, Garage Cleanout, Basement Cleanout, Commercial Cleanout, Moving Haul-Away, Construction Debris

**Service Category options:**
Residential, Commercial, Estate, Moving, Demolition/Construction

**Property Type options:**
Residential, Commercial, Multi-Unit, Storage Unit, Industrial

**Load Size options:**
Minimum Load, 1/4 Truck, 1/2 Truck, 3/4 Truck, Full Truck, Multiple Trucks, Unknown

**Same Day Available / Donation Items Present / Hazardous Materials / Review Requested / Review Received options:**
Yes, No

**Crew Size options:**
1 Person, 2 Person, 3+ Person

**Referral Partner Type options:**
None, Real Estate Agent, Property Manager, Moving Company, Renovation Contractor

---

## PHASE 2: PIPELINES

All created via `POST /opportunities/pipelines`

### Pipeline 1: Junk Removal - Residential
**Pipeline ID:** `SZDAv9yGSnYtHCBCIU0o`

| Stage | ID |
|-------|----|
| New Lead | `8900d674-644f-4dfe-9b44-5e9346fd8a90` |
| Quote Sent | `686e1564-d6b5-433d-b11f-1ff6eae11318` |
| Follow-Up | `3edae40e-efda-4e62-805f-ddc8f60b1add` |
| Job Scheduled | `7bd8bafa-6fac-4d0e-a6e6-5aaad83f3d44` |
| Confirmed | `e8dd4ae1-1099-45fc-8033-af0a20508709` |
| Job In Progress | `669ab2cd-8e6e-4dfc-afe8-f6139aad39d8` |
| Job Complete | `c8dd8e5d-0f1a-400c-a767-747eee978532` |
| Invoice Sent | `32a9ae07-3ffd-4be6-a07d-9799a1b0c8fe` |
| Paid | `274ed7ed-73af-45ab-aec0-61f851b108b8` |
| Review Requested | `80fdc58c-e232-41be-aeb3-a5d40d5d2554` |
| Repeat/Referral | `070537f6-210b-470b-b7e4-0b2f3eb07da6` |

### Pipeline 2: Junk Removal - Estate Cleanout
**Pipeline ID:** `u84X0ZuS9n9g0xAWooFB`

Stages: New Inquiry → Sensitivity Check → On-Site Assessment → Proposal Sent → Follow-Up → Contract Signed → Job Scheduled → Day 1 Cleanout → Cleanout Complete → Invoice Sent → Paid → Review + Referral

### Pipeline 3: Junk Removal - Commercial
**Pipeline ID:** `PljLqLU5JZCCDijPsxCI`

Stages: New Prospect → Site Assessment → Proposal Sent → Contract Signed → Job Scheduled → Job Complete → Invoice Sent → Paid → Recurring Account

### Pipeline 4: Junk Removal - Referral Partners
**Pipeline ID:** `iTkrrc4vSkCn2TZzCPIZ`

Stages: Partner Identified → Outreach Sent → Partnership Active → Referral Received → Job Complete → Partner Thanked → VIP Partner

---

## PHASE 3: CALENDARS

Created via `POST /calendars/`

| Calendar | ID | Duration | Hours |
|---------|----|----------|-------|
| Same-Day Junk Removal Booking | `4pqW1xv8DCm9wj0FyKdX` | 60 min | Mon-Sat 7am-6pm (configure in UI) |
| Estate/Commercial Assessment | `gN1oWsYAjaVWU52BIx06` | 60 min | Mon-Fri 8am-5pm (configure in UI) |

**Note:** Calendar open hours must be configured manually in the GHL UI (Calendar Settings → Availability). The GHL REST API v2021-07-28 does not accept `openHours` array directly on calendar creation — the `daysOfTheWeek` format in the API returns validation errors. Set hours in UI after creation.

---

## PHASE 4: TAGS

All 35 tags created via `POST /locations/{locationId}/tags`

| Tag | ID |
|-----|----|
| new-lead | `a4EAZjymrfOCEDOLCZnk` |
| residential-cleanout | `A0ZpRVhYSPVlmnv43Yx8` |
| estate-cleanout | `iOglio2YbUltHtm0w7Kr` |
| hoarder-cleanout | `LKQUqEEjE3bQqB354bCY` |
| appliance-removal | `xgdArolCxWJjQrY3NXDL` |
| furniture-removal | `TFc9IOtnIkLZEHiXjt3A` |
| demolition-debris | `G4rAzA96zciwVr5Gdqbw` |
| e-waste | `GrzuMpgwQ41avzbAv5Ib` |
| garage-cleanout | `s0pr2Hhg0AbxSjvs0soL` |
| basement-cleanout | `9e96RlwLdBMDhWxkMbwo` |
| commercial-cleanout | `7FFRngw2bPENQv9clt1b` |
| moving-haul | `6SkefUJXeAoeZ8oOMuiW` |
| construction-debris | `uWJOoP3xBQKUlZuHYDno` |
| same-day-available | `inKN8E9Ff3ETUqkoZ413` |
| donation-items | `31bEg0rHLbVwShT9U53E` |
| hazardous-materials | `0JIg8womfK7e02rpZitk` |
| estimate-sent | `RjZ1306UwedL9hxMW4f1` |
| job-scheduled | `3o9Ho9aSDTfPmc02rLX9` |
| job-complete | `KUDP06DnqpHNPbl1dvSj` |
| invoice-sent | `zDuHHTzrDGlex4iBxwuJ` |
| paid | `rh2wEC0A8sr1cYLLTANm` |
| review-requested | `Zr8ryKjOwAHyqx35giT9` |
| review-received | `UYC7MxibDNhpPDuaHjmL` |
| referral | `KM9NB9Ctbdnuso8xc1CS` |
| repeat-customer | `mvpuI99aFEKBHd5gvGq4` |
| cold-lead | `pCNNlkHilrOuTX2dMqr5` |
| no-show | `WIQMgksj31nCyOgy3dZA` |
| google-lsa | `6OL7zFZ5WJxek1afx45A` |
| kijiji-lead | `CrrFPxcRADNcY7oeGoZA` |
| facebook-marketplace | `ry1CA3dwHeqXntBnOQC4` |
| real-estate-agent | `JAQp9sJasDvdZnJMKhlb` |
| property-manager | `7djClZrBLkEAHYOfxBbJ` |
| moving-company | `UomBV1tOBK8vaMtUD4GW` |
| renovation-contractor | `BCXtRfa7GrsSAf0dT8G1` |
| vip-partner | `tKyVVvWgBvjsuRLch33R` |

---

## PHASE 5: WORKFLOWS — FULL SPECIFICATIONS

> **Note:** GHL workflow creation is not available via the public REST API v2021-07-28. Workflows must be built in the GHL UI (Automations → Create Workflow). All 10 workflow specs are documented here in full detail for manual UI build.

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
"Hi {{contact.firstName}}, this is {{location.name}}! Sorry we missed your call — need junk removed? We offer same-day service. Reply YES and we'll get you a quick quote 👋"

This fires automatically on every missed call. No workflow required.

---

### Workflow 2: New Lead — Instant Quote Response

**Trigger:** Contact created (from web form or Facebook Lead Ad) OR Contact tag (filter: tag added = new-lead)
**Goal:** Respond within 60 seconds of inquiry with load-size pricing + booking link

**Step 1 — Immediate SMS (0 min)**
> "Hi {{contact.firstName}}! Got your junk removal request 🚛 Quick pricing guide:
> • Minimum load: starting at $149
> • 1/4 Truck: ~$249
> • 1/2 Truck: ~$349
> • Full Truck: ~$499+
> 
> Same-day available! Book your slot here: [BOOKING LINK]
> Or reply with what you need hauled and we'll confirm a price in minutes."

**Step 2 — Wait 15 min, if no reply**
> "Hey {{contact.firstName}} — just following up on your junk removal request. We have trucks available today/tomorrow. Want to lock in a time? Reply YES and I'll call you right away."

**Step 3 — Wait 1 hour, if no booking**
> "{{contact.firstName}}, last one from us today — schedule is filling up fast. Reply BOOK to lock in your time, or call us at [PHONE]. We'll get it done."

**Step 4 — Wait 24 hours, if no booking**
> "Hey {{contact.firstName}} — still have a junk removal coming up? We're booking this week. Reply and we'll get you a price right away."

**Step 5 — Wait 3 days — Email**
> **Subject:** Still need that haul away done?
> Hi {{contact.firstName}},
> 
> We noticed you reached out about a junk removal recently. We'd love to help — our crew is available most days, including same-day pickups when slots are open.
> 
> Book a time here: [BOOKING LINK]
> Or reply to this email with any questions.
> 
> — [Company Name] Team

**Step 6 — Wait 7 days — SMS reactivation**
> "{{contact.firstName}} — checking in one last time. Still have stuff to haul away? We can usually do same-day. Reply QUOTE to get a price."

**Tags:** `new-lead` → `estimate-sent` on step 1
**Pipeline:** Residential → New Lead

---

### Workflow 3: Booking Confirmation

**Trigger:** Pipeline stage changed (filter: new stage = Job Scheduled) OR Customer booked appointment (calendar: Same-Day Junk Removal Booking)
**Goal:** Confirm booking, reduce no-shows

**Step 1 — Immediate SMS**
> "✅ You're booked! [Company Name] will arrive {{appointment.startTime}} on {{appointment.startDate}}. Your crew will text you 30 minutes before arrival. Questions? Reply or call [PHONE]. See you then! 🚛"

**Step 2 — Immediate Email**
> **Subject:** Your junk removal is confirmed — [Date]
> 
> Hi {{contact.firstName}},
> 
> Your junk removal appointment is confirmed!
> 
> 📅 Date: {{appointment.startDate}}
> ⏰ Time Window: {{appointment.startTime}}
> 📍 Address: {{contact.address1}}, {{contact.city}}
> 
> **What to expect:**
> - Your crew will text you 30 minutes before arrival
> - They'll do a quick walkthrough and confirm the load
> - Payment is collected after the job is complete
> - We accept cash, e-transfer, and major credit cards
> 
> **What happens to your stuff:**
> - Reusable items: donated to local charities
> - Recyclables: diverted from landfill
> - Remainder: disposed of responsibly
> 
> Questions? Reply to this email or call [PHONE].
> 
> — [Company Name] Team

**Step 3 — Day before, 5 PM — SMS**
> "Reminder: [Company Name] arrives tomorrow. We'll text you 30 min ahead. If anything changes, reply here or call [PHONE]. See you tomorrow! 🚛"

**Step 4 — Day of job, 7 AM — SMS**
> "Good morning {{contact.firstName}}! Your haul away is today. We'll text you when we're on our way. Ready to clear that space! 💪"

**Tags:** `job-scheduled`

---

### Workflow 4: No-Show Recovery

**Trigger:** Appointment status (filter: no-show)
**Goal:** Recover the booking without burning the lead

**Step 1 — Within 30 min — SMS**
> "Hi {{contact.firstName}} — we stopped by for your junk removal today but couldn't reach you. No worries — things happen! Want to reschedule? We have slots available this week. Reply to pick a new time."

**Step 2 — Wait 24 hours, if no reply**
> "{{contact.firstName}} — [Company Name] here. We missed you yesterday for your haul away. Whenever you're ready to reschedule, just reply or book online: [BOOKING LINK]"

**Step 3 — Wait 3 days — SMS**
> "Last check-in from us — still need that junk hauled away? We can reschedule anytime. Reply REBOOK and we'll get you sorted."

**Action if no rebook in 7 days:** Add tag `cold-lead`, move out of active pipeline

**Tags:** `no-show` applied on trigger; remove if rebooked

---

### Workflow 5: Post-Job Review Request

**Trigger:** Pipeline stage changed (filter: new stage = Job Complete)
**Goal:** Generate Google reviews at volume — this is the review flywheel

**Step 1 — 2 hours after trigger — SMS**
> "{{contact.firstName}} — thanks for choosing [Company Name] today! Hope the space is looking great 🙌 If you have 60 seconds, a Google review helps us a ton: [GOOGLE REVIEW LINK]
> We'd really appreciate it!"

**Step 2 — Wait 24 hours, if no review tag — SMS**
> "Hey {{contact.firstName}}! We hope you're loving the extra space. Would you mind leaving us a quick Google review? It really helps our small business: [GOOGLE REVIEW LINK] — Thanks!"

**Step 3 — Wait 3 days, if no review tag — Email**
> **Subject:** Quick favor from [Company Name]
> 
> Hi {{contact.firstName}},
> 
> We wanted to say thank you again for choosing [Company Name] for your junk removal. Our crew works hard to earn 5-star service every time, and reviews from customers like you help other families find us.
> 
> If you have a moment, we'd be so grateful if you'd leave us a Google review:
> 👉 [GOOGLE REVIEW LINK]
> 
> It takes less than 60 seconds and means the world to our team.
> 
> Thank you,
> [Owner Name]
> [Company Name]

**Stop condition:** If tag `review-received` is applied, end workflow immediately
**Tags applied:** `review-requested` on Step 1; `review-received` manually after confirmed
**On negative feedback:** Internal notification to owner only — remove from review sequence

---

### Workflow 6: Unhappy Customer Recovery

**Trigger:** Customer replied (with keyword filter: bad, terrible, awful, refund, complaint, disappointed, worst) OR Contact tag (filter: tag added = unhappy)
**Goal:** Intercept before they leave a negative review — escalate to owner

**Step 1 — Immediate — Internal Alert**
> **Internal SMS to Owner:** "⚠️ UNHAPPY CUSTOMER: {{contact.firstName}} {{contact.lastName}} — {{contact.phone}}. Review their conversation and call within 1 hour."

**Step 2 — Remove from review request workflow**
(Add tag `unhappy` which stops Workflow 5)

**Step 3 — Wait for owner action — no automated outreach**
(Owner handles personally)

**No automated customer messages in this workflow** — owner contact only

---

### Workflow 7: Estate Cleanout Sensitive Intake

**Trigger:** Contact tag (filter: tag added = estate-cleanout or hoarder-cleanout)
**Goal:** Begin relationship with empathy, not urgency — slower, softer pace

**Step 1 — Immediate SMS (gentle, no urgency)**
> "Hi {{contact.firstName}} — thank you for reaching out to [Company Name]. We understand estate cleanouts can be a difficult time. We're here to help make it as easy as possible. When would be a good time for a brief call so we can learn more about your situation?"

**Step 2 — Immediate Email**
> **Subject:** What to expect from your estate cleanout
> 
> Hi {{contact.firstName}},
> 
> Thank you for reaching out. We understand that estate cleanouts often come during challenging life moments, and we approach every job with care and discretion.
> 
> **Here's how we work:**
> 
> **1. Initial Consultation**
> We start with a conversation — by phone or in person — to understand the scope of the project, your timeline, and any special considerations (sentimental items, items to donate, specialty pieces like pianos or antiques).
> 
> **2. Written Proposal**
> We provide a clear, written quote with the scope of work, timeline, and pricing. No surprises.
> 
> **3. Donation Coordination**
> We work with local charities to donate usable items — furniture, clothing, household goods. We handle the coordination so you don't have to.
> 
> **4. Responsible Disposal**
> Everything else is disposed of responsibly — recycling where possible, landfill only as a last resort.
> 
> **5. Final Walkthrough**
> When we're done, we do a walkthrough with you to make sure everything is as expected. You'll receive before/after photos.
> 
> There's no rush on our end. We're here when you're ready.
> 
> — [Owner Name], [Company Name]
> [PHONE]

**Step 3 — Wait 24 hours, if no response — SMS (soft follow-up)**
> "{{contact.firstName}} — just checking in. Whenever you're ready, we're here. Estate cleanouts are a specialty of ours — we handle everything with care and discretion. No rush. [PHONE]"

**Step 4 — Wait 5 days — SMS**
> "Hi {{contact.firstName}}, [Company Name] here. We're available whenever you're ready to talk through your cleanout project. We work with families in all kinds of situations — you're in good hands."

**Pipeline:** Estate Cleanout → New Inquiry
**Booking link in email:** Estate/Commercial Assessment calendar

---

### Workflow 8: Real Estate Agent Referral Partner Outreach

**Trigger:** Contact tag (filter: tag added = real-estate-agent) AND Pipeline stage changed (filter: new stage = Outreach Sent, Referral Partners pipeline)
**Goal:** Build B2B referral relationships — "we make your listings move-ready"

**Step 1 — Day 1 — Email**
> **Subject:** Junk removal referrals for your listings in [City]
> 
> Hi {{contact.firstName}},
> 
> My name is [Owner Name] — I run [Company Name], and we work with several real estate agents in [City] who refer us to clients who need furniture, appliances, or full cleanouts done before listing a property.
> 
> **What we offer your clients:**
> - Pre-listing cleanouts — clear clutter to maximize showing appeal
> - Estate cleanouts — full home, basement, garage, attic
> - Same-week availability in most cases
> - Donation coordination for items clients want donated
> - Professional crews — no mess left behind
> - Before/after photos for your records
> 
> We'd love to be your go-to junk removal referral. We treat your clients like they're our best clients — because they are.
> 
> Interested in a quick 10-minute call? [BOOKING LINK — Estate/Commercial Assessment calendar]
> 
> — [Owner Name]
> [Company Name] | [Phone]

**Step 2 — Day 7 — SMS**
> "Hi {{contact.firstName}} — sent you an email last week about junk removal referrals for your listings. [Company Name] helps agents get homes ready to show. Worth a quick call? — [Name]"

**Step 3 — Day 14 — Email (value-add)**
> **Subject:** Pre-listing checklist for sellers (free resource for your clients)
> 
> Hi {{contact.firstName}},
> 
> Here's something that might be useful for your listing clients — a pre-listing declutter and cleanout checklist they can use to prepare their home for showings.
> 
> [LINK TO RESOURCE or inline checklist]
> 
> We created this for real estate agents to share with sellers. Feel free to use it with your clients — no strings attached.
> 
> If any of them need help with the physical haul away, we're here.
> 
> — [Owner Name], [Company Name]

**Step 4 — Day 30 — Final SMS**
> "{{contact.firstName}} — last follow-up from [Company Name]. We handle pre-listing cleanouts and estate haul away for agents in [City]. If you ever need a reliable crew on short notice, save our number: [PHONE]. We pick up."

**If partner responds positively:** Move to "Partnership Active" stage, apply tag `real-estate-agent`

---

### Workflow 9: Property Manager Recurring Account Nurture

**Trigger:** Contact tag (filter: tag added = property-manager) AND Opportunity created (filter: Referral Partners pipeline)
**Goal:** Build recurring commercial relationship — tenant turnovers, bulk trash, eviction cleanouts

**Step 1 — Day 1 — Email**
> **Subject:** Reliable junk removal for your properties in [City]
> 
> Hi {{contact.firstName}},
> 
> My name is [Owner Name] — I run [Company Name], and we specialize in tenant turnover cleanouts, bulk trash removal, and property cleanouts for property managers in [City/Region].
> 
> **What sets us apart for property managers:**
> - Fast scheduling — often same week or next week
> - Before/after photos sent to you after every job
> - We handle everything: furniture, appliances, demolition debris, e-waste
> - Professional, insured crews — no day labor or subcontractors
> - Simple invoicing — we can work with NET 30 for established accounts
> 
> We work with property management companies in [Area] and would love to introduce ourselves.
> 
> Would you be open to a 10-minute call this week?
> [BOOKING LINK]
> 
> — [Owner Name]
> [Company Name] | [Phone]

**Step 2 — Day 4 — SMS**
> "Hi {{contact.firstName}} — sent you an email earlier this week about property cleanouts and haul away. [Company Name] works with property managers in [City]. Quick 10-minute chat to see if we'd be a fit? — [Name]"

**Step 3 — Day 10 — Email (pain-point focused)**
> **Subject:** One thing most property managers hate about junk removal companies
> 
> Hi {{contact.firstName}},
> 
> Here's the #1 complaint we hear from property managers who've worked with other junk removal companies:
> 
> **They don't show up when they say they will.**
> 
> A unit sits empty. The new tenant is waiting. The turn is delayed. And the junk removal company is unreachable.
> 
> We built [Company Name] around one principle: if we book it, we show up. Every time.
> 
> Our property manager clients get:
> ✅ Confirmed time windows (not 4-hour guesstimates)
> ✅ Before/after photos sent same day
> ✅ Direct line to the owner if anything comes up
> ✅ Consistent crews — same people, every time
> 
> If you're tired of unreliable crews, let's talk.
> [BOOKING LINK] — 10 minutes, no sales pitch.
> 
> — [Owner Name]

**Step 4 — Day 21 — Final SMS**
> "{{contact.firstName}} — last follow-up from [Company Name]. We handle tenant turnover cleanouts and property haul away in [Area]. If you ever need a reliable crew on short notice, save our number: [PHONE]. We pick up."

**If no response after 21 days:** Move to quarterly check-in list
**Quarterly SMS (90-day cadence):**
> "Hi {{contact.firstName}} — [Company Name] checking in. Still looking for a reliable junk removal company for your properties? We're booking well and still have capacity. [PHONE]"

---

### Workflow 10: Seasonal Campaign — Spring Cleanout Push

**Trigger:** Scheduler (April 1 annually, or manual launch)
**Audience:** All contacts tagged `new-lead` OR `cold-lead` OR `repeat-customer` who have NOT been active in 60+ days
**Goal:** Capture spring cleaning surge — highest booking season for junk removal

**Step 1 — SMS Broadcast**
> "🌱 Spring cleanout time! [Company Name] is booking garage, basement, and yard cleanouts for April/May. Spots fill fast this time of year. Book now: [BOOKING LINK] or reply SPRING to get on the schedule."

**Step 2 — Wait 2 days, if no reply — Email**
> **Subject:** Spring is the #1 time to finally clear that clutter
> 
> Hi {{contact.firstName}},
> 
> You've probably been meaning to clear out the garage/basement/attic for a while now. Spring is the perfect time — and we're making it easy.
> 
> **[Company Name] Spring Cleanout Special:**
> - Book any load ½ truck or larger and get [OFFER — e.g., free appliance removal OR $25 off]
> - Same-week scheduling available
> - We do all the heavy lifting — literally
> 
> Don't let another spring go by with the clutter still there.
> 
> [BOOKING LINK]
> 
> — [Company Name] Team

**Step 3 — Wait 5 days — SMS (last call)**
> "Last call for spring cleanout slots — [Company Name] is filling up fast. Reply BOOK or call [PHONE] to lock in your time before May fills up. 🚛"

**Tags applied:** `estimate-sent` when they respond to inquiry

---

## API NOTES & LESSONS LEARNED

### Endpoint Reference (Working)
- **Get/Create Pipelines:** `GET/POST /opportunities/pipelines?locationId={id}`
- **Get/Create Custom Fields:** `GET/POST /locations/{locationId}/customFields`
- **Get/Create Tags:** `GET/POST /locations/{locationId}/tags`
- **Get/Create Calendars:** `GET/POST /calendars/?locationId={id}`
- **Get Location:** `GET /locations/{locationId}`

### API Quirks Found
1. **Custom Fields:** Use `SINGLE_OPTIONS` for dropdown (not `DROPDOWN`). Options are a flat string array.
2. **Pipelines:** Use `position` (number), NOT `probability` in stages.
3. **Calendar hours:** `openHours` with `daysOfTheWeek` array causes validation errors in REST API — configure availability in GHL UI after calendar creation.
4. **Custom field type `MONETORY`** (note: GHL spells it without the 'a') for currency fields.
5. **MCP server:** `search_operations` returns empty — fall back to direct REST API immediately.

### What Requires Manual UI Build
1. **Workflows (all 10)** — GHL REST API does not expose workflow creation endpoints
2. **Calendar availability hours** — openHours configuration in REST API has format issues; set in GHL UI
3. **Forms** — 4 forms (Residential, Commercial, Estate, Moving) need UI build
4. **Funnel/Landing Pages** — Requires GHL funnel builder UI

---

## EXISTING PIPELINES (pre-build)
The sub-account had one pre-existing pipeline:
- **Marketing Pipeline** (`uOrAFTaSOAYtZsU2TrmP`) — 7 stages (New Lead, Contacted, Qualified, Proposal Sent, Negotiation, Won, Lost)

This was left in place — client can archive or delete as needed.

---

## NEXT STEPS FOR CLIENT ONBOARDING

1. **Open calendars in GHL UI** → set availability hours:
   - Same-Day Booking: Mon-Sat, 7am-6pm
   - Estate/Commercial Assessment: Mon-Fri, 8am-5pm

2. **Build 10 workflows in Automations** → use specs above as copy-paste source

3. **Build 4 forms** in GHL Form Builder:
   - Residential Quote Request (multi-step)
   - Commercial Cleanout Inquiry
   - Estate Cleanout Consultation Request
   - Moving Quote Request

4. **Connect Google Review link** in Workflow 5 (Post-Job Review Request)

5. **Replace all placeholders** in workflow copy:
   - [Company Name] → actual business name
   - [PHONE] → GHL tracking number
   - [BOOKING LINK] → Same-Day calendar booking URL
   - [GOOGLE REVIEW LINK] → Google Business Profile review link
   - [City] / [Area] → service area
   - [Owner Name] → owner's name
   - [OFFER] in Workflow 10 → actual seasonal promo

6. **Connect Facebook Lead Ads** if running paid social → webhook to GHL

7. **Import past customer list** → tag as `repeat-customer` → enroll in Workflow 10

8. **Set up missed call text back** in GHL Phone Settings (separate from Workflow 1 if using native GHL missed call automation)

---

*Build log created: 2026-07-21 by Maximus*
*Sub-account: Junk removal — 5kSsYpEfVDnIkH3Jz0q4*
