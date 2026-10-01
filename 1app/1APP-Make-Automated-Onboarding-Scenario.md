# 1APP — Make.com Automated Customer Onboarding Scenario

## Goal
Reduce new-client onboarding from a 45-minute phone call to a mostly automated flow where the client submits one smart form, pays, uploads basic company info, and 1APP gets a ready-to-configure fulfillment package.

Tony should only need to review, fix edge cases, and launch.

---

## Core Idea

Client signs up → onboarding form → Make scenario creates/updates everything needed:

1. Create / update client record in GHL
2. Create onboarding task checklist
3. Save company info to a structured folder/database
4. Generate AI Voice + Conversation AI prompts from the correct trade pack
5. Create internal setup notes for Tony/fulfillment
6. Send client confirmation email/SMS
7. Notify Tony/Justin with everything needed to finish setup

---

## Recommended Client Flow

### Step 1 — Buy / Sign Up
Client pays through Stripe or signs up through 1APP checkout.

**Trigger options:**
- Stripe checkout completed
- GHL form submitted
- GHL opportunity moves to “Won”

Best first version: **GHL form submitted** because it is easiest to control.

---

## Step 2 — Onboarding Form

Use one smart onboarding form per client after signup.

### Required Fields
- Business name
- Owner name
- Main email
- Main phone
- Website
- Trade/category
- Service area / cities served
- Business address
- Emergency phone number, if applicable
- Booking calendar preference
- Preferred appointment length
- Business hours
- Services offered
- Services not offered
- Average response time promise
- Current lead time
- Google review link
- Facebook page
- Instagram page
- Logo upload
- Brand colours, optional
- Tone preference: professional, friendly, casual, premium, emergency-first

### Trade-Specific Fields
The form should branch based on trade.

Examples:
- Roofing: retail vs insurance, storm work, active leak handling
- Plumbing: emergency calls, drains, water heaters, gas policy
- HVAC: maintenance agreements, emergency heat/no-cool policy
- Flooring: flooring types, showroom/sample process, installation lead time
- Fencing: residential/farm/commercial, survey/permit policy
- Water damage: 24/7 emergency, insurance process, IICRC language

---

## Step 3 — Make.com Scenario Structure

### Scenario Name
`1APP — New Client Auto-Onboarding`

### Trigger
GHL form submitted: `1APP Client Onboarding Form`

Alternative later: Stripe successful payment → send onboarding form → wait for submission.

---

## Make Modules

### Module 1 — Watch GHL Form Submission
Trigger when onboarding form is submitted.

### Module 2 — Router by Trade
Route based on selected trade:
- Roofing
- Plumbing
- HVAC
- Electrical
- Landscaping
- Concrete & Driveway
- Windows & Siding
- Fencing
- Deck & Patio
- Painting
- Garage Door
- Tree Service
- Pest Control
- Junk Removal
- Flooring
- Foundation Waterproofing
- Insulation
- Pool & Spa
- Water Damage Restoration
- General Contractor

### Module 3 — Create / Update GHL Contact
Upsert contact in the 1APP GHL account.

Tags:
- new-client
- onboarding-submitted
- trade-[trade-name]
- setup-needed

### Module 4 — Create Opportunity
Pipeline: `1APP Client Onboarding`

Stages:
1. Paid / Form Submitted
2. Info Review
3. Snapshot Setup
4. AI Agents Setup
5. Testing
6. Launched
7. Needs Client Info

### Module 5 — Create Client Folder
Create Google Drive folder or local folder:
`1APP Clients / [Business Name] /`

Subfolders:
- Brand Assets
- Onboarding Form
- AI Prompts
- Snapshot Setup
- Testing Notes
- Launch Confirmation

### Module 6 — Generate AI Prompt Package
Use the master AI prompt library:
`/home/maximus/.openclaw/workspace/ai-agent-prompt-packs/MASTER-1APP-trades-ai-agent-prompt-library.md`

Make/OpenAI step should:
- Pull the correct trade prompt section
- Replace placeholders:
  - COMPANY_NAME
  - SERVICE_AREA
  - BOOKING_LINK
  - OWNER_NAME
  - RESPONSE_TIME_HOURS
  - CURRENT_LEAD_TIME
  - EMERGENCY_PHONE
  - GOOGLE_REVIEW_LINK
  - CALENDAR_NAME
- Output:
  - Voice AI welcome message
  - Voice AI system prompt
  - Conversation AI prompt
  - Intake questions
  - Escalation rules
  - Setup checklist

### Module 7 — Save Generated Prompt Package
Save generated prompts as:
`[Business Name] — AI Agent Setup Pack.md`

### Module 8 — Create Tony Fulfillment Task
Create task in GHL:

Title:
`SETUP 1APP CLIENT — [Business Name] — [Trade]`

Task body:
- Business name
- Trade
- Service area
- Website
- Booking link needed?
- AI Voice prompt ready: yes/no
- Conversation AI prompt ready: yes/no
- Missing info
- Recommended snapshot
- Next action

### Module 9 — Notify Tony / Justin
Send internal email/SMS/WhatsApp-style notification:

`New 1APP client onboarding submitted: [Business Name] — [Trade]. Prompt pack generated. Review setup folder and launch snapshot.`

### Module 10 — Client Confirmation
Send client email:

Subject: `We received your 1APP setup info`

Body:
`Hey [Owner Name], we received your onboarding form. Our setup team is preparing your 1APP system now. If we’re missing anything, we’ll reach out. Otherwise, next step is testing and launch confirmation.`

Optional SMS:
`Hey [Owner Name], got your 1APP setup form — we’re building your automation now. We’ll reach out if anything’s missing.`

---

## Advanced Version — Almost Fully Automatic

Once stable, Make can also:

1. Create a new GHL sub-account from template/snapshot if API/access allows
2. Apply the correct trade snapshot
3. Create or update calendars
4. Add AI Voice prompt text into a setup task
5. Add Conversation AI prompt text into a setup task
6. Create default test contact
7. Send Tony a launch QA checklist

Important: if GHL does not expose snapshot install or AI Conversation config through API, Make cannot fully click those UI-only pieces. In that case, Make should prepare everything so Tony only copies/pastes and tests.

---

## Client-Facing Positioning

Use this language:

`Instead of a long onboarding call, we use a guided setup form that collects everything we need to build your automation correctly. Most businesses finish it in 10–15 minutes. If anything is unclear, we’ll follow up — but you don’t need to sit on a 45-minute call just to repeat your business hours and services.`

---

## What Tony Still Does Manually

Minimum manual work after automation:

1. Review onboarding form
2. Confirm snapshot/trade match
3. Install/apply snapshot if not API-supported
4. Paste generated AI Voice prompt into GHL
5. Paste generated Conversation AI prompt into GHL
6. Connect phone/calendar
7. Run test call + test lead
8. Mark client launched

Target time: **10–15 minutes per client**, not 45 minutes.

---

## Best MVP Build Order

### Version 1 — Fastest
- GHL onboarding form
- Make scenario triggered by form
- Generate prompt pack
- Create internal setup task
- Notify Tony
- Send client confirmation

### Version 2
- Add Stripe trigger
- Auto-send onboarding form after payment
- Create client folders
- Generate launch checklist

### Version 3
- Auto-create/update GHL sub-account assets where API allows
- Add QA testing workflow
- Add client launch email

---

## Decision
Build Version 1 first. It gives the biggest time savings with the least technical risk.
