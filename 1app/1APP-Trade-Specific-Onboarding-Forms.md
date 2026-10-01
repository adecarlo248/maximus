# 1APP — Trade-Specific Client Onboarding Forms

## Recommendation
Build **one master onboarding form** with conditional trade sections instead of 20 separate forms.

Why:
- Easier to maintain
- One Make.com scenario trigger
- One client onboarding URL
- Trade field routes the form data to the right AI prompt pack
- Less duplicate work inside GHL

If GHL conditional logic becomes messy, duplicate the master into trade-specific forms later.

---

# MASTER FORM — 1APP Client Onboarding

## Form Name
`1APP Client Onboarding Form`

## Form Purpose
Collect everything needed to configure:
- Client profile
- Snapshot/trade setup
- AI Voice agent
- Conversation AI agent
- Booking calendar
- Service area
- Escalation rules
- Review/referral links

---

## SECTION 1 — Business Basics

1. Business Name
2. Owner / Main Contact Name
3. Main Email
4. Main Phone Number
5. Business Address
6. Website URL
7. Facebook Page URL
8. Instagram URL
9. Google Business Profile URL
10. Google Review Link
11. Upload Logo
12. Brand Colours, optional
13. Preferred brand tone
   - Professional
   - Friendly
   - Casual
   - Premium
   - Emergency-first
   - No-nonsense / tradesman style

---

## SECTION 2 — Trade Selection

Question: `What trade/category best describes your business?`

Options:
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

This answer controls the Make.com route and AI prompt pack.

---

## SECTION 3 — Service Area + Operations

1. What cities/towns do you serve?
2. How far will you travel from your main location?
3. Business hours
4. Do you offer emergency / after-hours service?
   - Yes
   - No
   - Only for existing customers
5. Emergency phone number
6. Average response time promise
   - Under 15 minutes
   - Under 1 hour
   - Same day
   - Next business day
   - Custom
7. Current booking lead time
   - Same day
   - 1–3 days
   - 1 week
   - 2–4 weeks
   - 4+ weeks
8. Preferred appointment length
   - 15 minutes
   - 30 minutes
   - 45 minutes
   - 60 minutes
   - 90 minutes
9. Do you want AI to book directly or collect info first?
   - Book directly
   - Qualify first, then book
   - Send to owner for approval

---

## SECTION 4 — Booking + Calendar Setup

1. Booking link, if already created
2. Calendar name to use
3. Who should be assigned to new appointments?
4. Appointment types offered
   - Free estimate
   - Phone consultation
   - On-site inspection
   - Emergency visit
   - Service call
   - Design consultation
5. Do you charge a diagnostic / service call fee?
   - Yes
   - No
   - Depends on location/job
6. If yes, what is the fee?
7. What should the AI say about pricing?
8. What should the AI never promise?

---

# TRADE-SPECIFIC SECTIONS

Each trade section should appear only when that trade is selected.

---

## Roofing Onboarding Section

1. What roofing services do you offer?
   - Roof replacement
   - Roof repair
   - Emergency leak repair
   - Storm damage
   - Insurance claims
   - Metal roofing
   - Flat roofing
   - Eavestrough/gutters
   - Skylights
2. Do you handle insurance claims?
3. Do you offer emergency tarp/leak service?
4. What roofing materials do you install?
5. Do you offer financing?
6. Do you work with adjusters?
7. What questions should AI ask for storm/leak calls?
   - Is water actively coming in?
   - When did the damage happen?
   - Is it safe to access the attic?
   - Has insurance been notified?
8. What roof types do you NOT work on?
9. Warranty details
10. Escalation rules
   - Active leak
   - Tree through roof
   - Electrical hazard
   - Structural collapse risk

---

## Plumbing Onboarding Section

1. Services offered
   - Drain cleaning
   - Leak repair
   - Water heater
   - Sewer line
   - Fixture install
   - Bathroom/kitchen plumbing
   - Emergency plumbing
   - Gas lines
2. Do you offer 24/7 emergency service?
3. Do you handle gas-related calls?
4. Do you install tankless water heaters?
5. Do you offer camera inspections?
6. Do you charge dispatch/diagnostic fees?
7. What should AI do if caller smells gas?
8. Water heater intake questions
   - Tank or tankless?
   - Age?
   - Leaking or no hot water?
   - Gas or electric?
9. Drain intake questions
   - One fixture or whole home?
   - Sewage backup?
   - Basement drain involved?
10. Escalation rules
   - Gas smell
   - Sewage backup
   - Major active leak
   - No water / burst pipe

---

## HVAC Onboarding Section

1. Services offered
   - Furnace repair
   - AC repair
   - Install/replacement
   - Heat pump
   - Maintenance plans
   - Ductwork
   - Indoor air quality
   - Gas fireplace
2. Emergency service offered?
3. Maintenance agreement name/details
4. Brands serviced
5. Financing offered?
6. Rebate programs mentioned?
7. No-heat / no-cool intake questions
   - Is system running?
   - Any error code?
   - Thermostat working?
   - Filter changed?
   - Age of unit?
8. Carbon monoxide protocol
9. Replacement estimate rules
10. Escalation rules
   - No heat in freezing weather
   - CO alarm
   - Burning smell
   - Vulnerable person in home

---

## Electrical Onboarding Section

1. Services offered
   - Panel upgrades
   - EV chargers
   - Lighting
   - Rewiring
   - Troubleshooting
   - Generators
   - Renovation electrical
   - Commercial electrical
2. Emergency electrical service?
3. Do you pull permits?
4. ESA/inspection process wording
5. EV charger intake
   - Charger type
   - Panel size
   - Garage/driveway location
   - Existing outlet?
6. Safety intake
   - Sparks?
   - Burning smell?
   - Breaker hot?
   - Power out to whole home or area?
7. What should AI never troubleshoot over phone?
8. Escalation rules
   - Smoke/burning smell
   - Sparks/fire
   - Exposed live wire
   - Water near electrical

---

## Landscaping Onboarding Section

1. Services offered
   - Lawn care
   - Garden design
   - Hardscaping
   - Interlock
   - Retaining walls
   - Grading/drainage
   - Irrigation
   - Snow removal
   - Seasonal cleanups
2. Residential/commercial/both?
3. Do you offer recurring maintenance?
4. Minimum job size
5. Snow contract details
6. Design consultation process
7. Estimate seasonality
8. Intake questions
   - Property type
   - One-time or recurring?
   - Approximate size
   - Photos available?
   - Timeline?
9. Escalation rules
   - Drainage/flooding issue
   - Retaining wall failure
   - Commercial contract request

---

## Concrete & Driveway Onboarding Section

1. Services offered
   - Driveways
   - Walkways
   - Patios
   - Garage floors
   - Stamped concrete
   - Concrete repair
   - Sealing
   - Asphalt vs concrete consultation
2. Do you handle permits?
3. Minimum project size
4. Seasonal pour window
5. Current lead time
6. Intake questions
   - New install or replacement?
   - Approximate square footage?
   - Access issues?
   - Drainage concerns?
   - Finish preference?
7. What should AI say about curing time?
8. Escalation rules
   - Trip hazard liability
   - Drainage toward foundation
   - Commercial quote

---

## Windows & Siding Onboarding Section

1. Services offered
   - Window replacement
   - Door replacement
   - Siding
   - Soffit/fascia
   - Eavestrough
   - Storm/insurance work
2. Do you discuss rebates?
3. Brands/materials used
4. Financing offered?
5. Insurance claim support?
6. Intake questions
   - How many windows/doors?
   - Drafts/leaks/condensation?
   - Full house or partial?
   - Siding material?
   - Insurance involved?
7. Escalation rules
   - Active water intrusion
   - Storm damage
   - Broken glass/security issue

---

## Fencing Onboarding Section

1. Services offered
   - Wood fence
   - Vinyl fence
   - Chain link
   - Ornamental iron/aluminum
   - Privacy fence
   - Pool fence
   - Farm/agricultural fence
   - Gates
   - Fence repair
2. Do you handle permits?
3. Do you require property survey?
4. Minimum linear feet/job size
5. Materials offered
6. Intake questions
   - Approximate linear feet?
   - Fence material?
   - Height?
   - Gates needed?
   - Property survey available?
   - Residential, commercial, farm?
7. Escalation rules
   - Pool safety fence
   - Dispute/property line concern
   - Farm livestock containment

---

## Deck & Patio Onboarding Section

1. Services offered
   - Deck build
   - Deck repair
   - Composite deck
   - Pressure-treated deck
   - Patio
   - Pergola
   - Railings
   - Stairs
2. Do you handle permits?
3. Design consultation process
4. Materials used
5. Minimum project size
6. Intake questions
   - New build or repair?
   - Approximate size?
   - Height off ground?
   - Material preference?
   - Railing/stairs needed?
   - Permit status?
7. Escalation rules
   - Unsafe deck
   - Structural movement
   - Railing/stair failure

---

## Painting Onboarding Section

1. Services offered
   - Interior painting
   - Exterior painting
   - Cabinet painting
   - Commercial painting
   - Staining
   - Drywall repair
   - Colour consultation
2. Do you provide paint/materials?
3. Brands used
4. Minimum job size
5. Exterior weather policy
6. Intake questions
   - Interior or exterior?
   - Rooms/areas?
   - Walls/trim/ceilings/cabinets?
   - Current condition?
   - Colour selected?
   - Timeline?
7. Escalation rules
   - Lead paint possibility
   - Water damage/mold visible
   - Exterior safety/access issue

---

## Garage Door Onboarding Section

1. Services offered
   - Spring repair
   - Cable repair
   - Opener repair/install
   - New doors
   - Track repair
   - Emergency service
   - Commercial overhead doors
2. Emergency service offered?
3. Brands serviced
4. Diagnostic fee?
5. Intake questions
   - Door stuck open/closed?
   - Spring broken?
   - Cable off?
   - Opener issue?
   - Door size/material?
   - Vehicle trapped?
6. Escalation rules
   - Vehicle trapped
   - Door stuck open/security risk
   - Commercial bay blocked
   - Door hanging/unsafe

---

## Tree Service Onboarding Section

1. Services offered
   - Tree removal
   - Trimming/pruning
   - Stump grinding
   - Emergency storm cleanup
   - Arborist assessment
   - Lot clearing
2. Emergency service offered?
3. Certified arborist?
4. Insurance info wording
5. Intake questions
   - Tree type/size if known
   - Near house/power lines?
   - Dead/damaged/leaning?
   - Storm-related?
   - Access for equipment?
   - Photos available?
6. Escalation rules
   - Tree on house/car
   - Power lines involved
   - Blocking driveway/road
   - Risk of falling

---

## Pest Control Onboarding Section

1. Services offered
   - Ants
   - Wasps/hornets
   - Rodents
   - Bed bugs
   - Cockroaches
   - Spiders
   - Wildlife exclusion
   - Commercial pest control
2. Emergency service offered?
3. Recurring plans?
4. Pet/child safety policy
5. Intake questions
   - Pest type
   - Where seen?
   - How long active?
   - Inside/outside?
   - Children/pets/sensitivities?
   - Landlord/property manager involved?
6. Escalation rules
   - Severe allergic risk
   - Bed bug hotel/multi-unit
   - Active wasp nest near entrance
   - Wildlife in living space

---

## Junk Removal Onboarding Section

1. Services offered
   - Furniture removal
   - Appliance removal
   - Construction debris
   - Estate cleanout
   - Hoarding cleanup
   - Yard waste
   - Donation runs
   - Commercial cleanout
2. Items not accepted
3. Minimum charge
4. Same-day availability?
5. Intake questions
   - What needs removed?
   - Approximate volume?
   - Stairs/elevator?
   - Photos available?
   - Hazardous material?
   - Donation/salvage items?
6. Escalation rules
   - Biohazard
   - Hoarding/estate sensitivity
   - Heavy commercial job
   - Hazardous waste

---

## Flooring Onboarding Section

1. Services offered
   - Hardwood install
   - LVP/Laminate
   - Tile
   - Carpet
   - Hardwood refinishing
   - Subfloor repair
   - Commercial flooring
   - Water damage replacement
2. Do you offer showroom/sample process?
3. Materials supplied by company or customer?
4. Minimum job size
5. Current material lead times
6. Intake questions
   - Flooring type?
   - Approximate square footage?
   - Rooms/areas?
   - Existing flooring?
   - Subfloor issues?
   - Water damage/insurance?
   - Timeline?
7. Escalation rules
   - Active water damage
   - Insurance claim
   - Major subfloor issue
   - Commercial/property manager request

---

## Foundation Waterproofing Onboarding Section

1. Services offered
   - Basement waterproofing
   - Foundation crack repair
   - Sump pump
   - Weeping tile
   - Exterior excavation
   - Interior drainage
   - Mold/moisture assessment
2. Emergency flooding service?
3. Financing offered?
4. Warranty terms
5. Intake questions
   - Active water now?
   - Where is water entering?
   - Finished or unfinished basement?
   - Sump pump present?
   - Crack visible?
   - Mold/smell?
   - Previous repairs?
6. Escalation rules
   - Active flooding
   - Electrical near water
   - Sewer backup
   - Structural wall movement

---

## Insulation Onboarding Section

1. Services offered
   - Attic insulation
   - Spray foam
   - Blown-in insulation
   - Batt insulation
   - Air sealing
   - Crawlspace insulation
   - Removal
2. Rebate programs mentioned?
3. Energy audit partnerships?
4. Asbestos policy
5. Intake questions
   - Area needing insulation?
   - Home age?
   - Existing insulation?
   - Comfort issue or energy bill issue?
   - Moisture/mold present?
   - Renovation or retrofit?
6. Escalation rules
   - Suspected asbestos
   - Mold/moisture
   - Active roof leak
   - Unsafe attic access

---

## Pool & Spa Onboarding Section

1. Services offered
   - Openings/closings
   - Maintenance
   - Repairs
   - Equipment replacement
   - Leak detection
   - Liners
   - Hot tubs
   - New installs
2. Seasonal availability
3. Emergency service?
4. Brands serviced
5. Intake questions
   - Pool or hot tub?
   - Service needed?
   - In-ground/above-ground?
   - Equipment issue?
   - Water condition?
   - Opening/closing date?
6. Escalation rules
   - Electrical/equipment hazard
   - Major leak
   - Green/unsafe water
   - Commercial pool issue

---

## Water Damage Restoration Onboarding Section

1. Services offered
   - Emergency extraction
   - Dry-out
   - Mold remediation
   - Reconstruction
   - Insurance claims
   - Sewage cleanup
2. 24/7 availability?
3. IICRC certified?
4. Insurance billing support?
5. Intake questions
   - Is water still coming in?
   - Source of water?
   - Clean/grey/black water?
   - Affected rooms?
   - Electricity nearby?
   - Insurance notified?
   - Photos available?
6. Escalation rules
   - Active flooding
   - Sewage/black water
   - Electrical hazard
   - Vulnerable occupants
   - Commercial loss

---

## General Contractor Onboarding Section

1. Services offered
   - Renovations
   - Basement finishing
   - Kitchen/bath
   - Additions
   - New builds
   - Commercial projects
   - Repairs
   - Insurance restoration
2. Minimum project size
3. Do you offer design/build?
4. Permit handling
5. Financing offered?
6. Intake questions
   - Project type
   - Budget range
   - Timeline
   - Permit needed?
   - Plans/drawings available?
   - Property type
   - Decision makers
7. Escalation rules
   - Structural concern
   - Insurance restoration
   - Commercial project
   - Urgent safety issue

---

# FINAL SECTION — Client Approval

1. Is all information accurate?
2. Anything AI should never say to your customers?
3. Anything AI should always mention?
4. Who should receive new lead notifications?
5. Who approves final launch?
6. Consent checkbox:
   `I understand 1APP will use this information to configure automation, AI voice, AI chat, calendars, and follow-up systems for my business.`

---

# MAKE.COM ROUTING LOGIC

## If Trade = Roofing
Use `home-core-agent-prompts.md` → Roofing section

## If Trade = Flooring
Use `specialty-agent-prompts.md` → Flooring section

## If Trade = Fencing
Use `exterior-agent-prompts.md` → Fencing section

## If Trade = Water Damage Restoration
Use `remediation-agent-prompts.md` → Water Damage Restoration section

Same pattern for all trades.

---

# MVP BUILD NOTE

Start with these 5 trade conditional sections first because they are most likely to sell quickly:
1. Roofing
2. Plumbing
3. HVAC
4. Flooring
5. Fencing

Then add the remaining trades after the Make scenario is working.
