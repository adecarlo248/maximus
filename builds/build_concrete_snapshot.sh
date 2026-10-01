#!/bin/bash
# Concrete & Driveway GHL Snapshot Build Script
# Location ID: MomQVDxtFt9XoCktDIbQ
# Sub-account: Concrete and driveway

GHL_TOKEN="pit-b9820699-ae67-4f90-9bfe-f759420b7066"
LOC_ID="MomQVDxtFt9XoCktDIbQ"
LOG="/home/maximus/.openclaw/workspace/builds/concrete-snapshot-build-log.md"
BASE_URL="https://services.leadconnectorhq.com"

# Helper: POST custom field
create_field() {
  local NAME="$1"
  local TYPE="$2"
  local BODY="$3"
  curl -s -X POST "${BASE_URL}/locations/${LOC_ID}/customFields" \
    -H "Authorization: Bearer ${GHL_TOKEN}" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "$BODY"
}

echo "Starting Phase 1: Custom Fields"

# 1. Lead Source (SINGLE_OPTIONS / dropdown)
F1=$(create_field "Lead Source" "SINGLE_OPTIONS" '{
  "name": "Lead Source",
  "dataType": "SINGLE_OPTIONS",
  "options": [
    {"label": "Google LSA"},
    {"label": "Google Organic"},
    {"label": "Referral"},
    {"label": "Door Knock"},
    {"label": "Real Estate Agent"},
    {"label": "Property Manager"},
    {"label": "Kijiji/Craigslist"},
    {"label": "Facebook Ad"},
    {"label": "Repeat Customer"}
  ]
}')
echo "F1 Lead Source: $F1"

# 2. Job Type (SINGLE_OPTIONS)
F2=$(create_field "Job Type" "SINGLE_OPTIONS" '{
  "name": "Job Type",
  "dataType": "SINGLE_OPTIONS",
  "options": [
    {"label": "Driveway Replacement"},
    {"label": "New Driveway"},
    {"label": "Interlock/Patio"},
    {"label": "Stamped Concrete"},
    {"label": "Exposed Aggregate"},
    {"label": "Flatwork/Slab"},
    {"label": "Crack Repair"},
    {"label": "Resurfacing"},
    {"label": "Asphalt"},
    {"label": "Commercial Parking Lot"},
    {"label": "Walkway/Steps"},
    {"label": "Foundation Work"}
  ]
}')
echo "F2 Job Type: $F2"

# 3. Service Category (SINGLE_OPTIONS)
F3=$(create_field "Service Category" "SINGLE_OPTIONS" '{
  "name": "Service Category",
  "dataType": "SINGLE_OPTIONS",
  "options": [
    {"label": "Residential"},
    {"label": "Commercial"},
    {"label": "Repair/Maintenance"},
    {"label": "New Construction"}
  ]
}')
echo "F3 Service Category: $F3"

# 4. Property Type (SINGLE_OPTIONS)
F4=$(create_field "Property Type" "SINGLE_OPTIONS" '{
  "name": "Property Type",
  "dataType": "SINGLE_OPTIONS",
  "options": [
    {"label": "Residential"},
    {"label": "Commercial"},
    {"label": "Multi-Unit"},
    {"label": "Industrial"}
  ]
}')
echo "F4 Property Type: $F4"

# 5. Surface Material (SINGLE_OPTIONS)
F5=$(create_field "Surface Material" "SINGLE_OPTIONS" '{
  "name": "Surface Material",
  "dataType": "SINGLE_OPTIONS",
  "options": [
    {"label": "Concrete"},
    {"label": "Asphalt"},
    {"label": "Interlock/Pavers"},
    {"label": "Stamped Concrete"},
    {"label": "Exposed Aggregate"},
    {"label": "Unknown"}
  ]
}')
echo "F5 Surface Material: $F5"

# 6. Estimated Square Footage (NUMERICAL)
F6=$(create_field "Estimated Square Footage" "NUMERICAL" '{
  "name": "Estimated Square Footage",
  "dataType": "NUMERICAL"
}')
echo "F6 Est Square Footage: $F6"

# 7. Sealer Applied (RADIO Yes/No)
F7=$(create_field "Sealer Applied" "RADIO" '{
  "name": "Sealer Applied",
  "dataType": "RADIO",
  "options": [
    {"label": "Yes"},
    {"label": "No"}
  ]
}')
echo "F7 Sealer Applied: $F7"

# 8. Sealing Due Date (DATE)
F8=$(create_field "Sealing Due Date" "DATE" '{
  "name": "Sealing Due Date",
  "dataType": "DATE"
}')
echo "F8 Sealing Due Date: $F8"

# 9. Permit Required (RADIO Yes/No)
F9=$(create_field "Permit Required" "RADIO" '{
  "name": "Permit Required",
  "dataType": "RADIO",
  "options": [
    {"label": "Yes"},
    {"label": "No"}
  ]
}')
echo "F9 Permit Required: $F9"

# 10. Permit Number (TEXT)
F10=$(create_field "Permit Number" "TEXT" '{
  "name": "Permit Number",
  "dataType": "TEXT"
}')
echo "F10 Permit Number: $F10"

# 11. Estimate Amount (MONETORY)
F11=$(create_field "Estimate Amount" "MONETORY" '{
  "name": "Estimate Amount",
  "dataType": "MONETORY"
}')
echo "F11 Estimate Amount: $F11"

# 12. Contract Amount (MONETORY)
F12=$(create_field "Contract Amount" "MONETORY" '{
  "name": "Contract Amount",
  "dataType": "MONETORY"
}')
echo "F12 Contract Amount: $F12"

# 13. Deposit Paid (RADIO Yes/No)
F13=$(create_field "Deposit Paid" "RADIO" '{
  "name": "Deposit Paid",
  "dataType": "RADIO",
  "options": [
    {"label": "Yes"},
    {"label": "No"}
  ]
}')
echo "F13 Deposit Paid: $F13"

# 14. Crew Assigned (TEXT)
F14=$(create_field "Crew Assigned" "TEXT" '{
  "name": "Crew Assigned",
  "dataType": "TEXT"
}')
echo "F14 Crew Assigned: $F14"

# 15. Pour/Install Date (DATE)
F15=$(create_field "Pour/Install Date" "DATE" '{
  "name": "Pour/Install Date",
  "dataType": "DATE"
}')
echo "F15 Pour/Install Date: $F15"

# 16. Weather Hold (RADIO Yes/No)
F16=$(create_field "Weather Hold" "RADIO" '{
  "name": "Weather Hold",
  "dataType": "RADIO",
  "options": [
    {"label": "Yes"},
    {"label": "No"}
  ]
}')
echo "F16 Weather Hold: $F16"

# 17. Review Requested (RADIO Yes/No)
F17=$(create_field "Review Requested" "RADIO" '{
  "name": "Review Requested",
  "dataType": "RADIO",
  "options": [
    {"label": "Yes"},
    {"label": "No"}
  ]
}')
echo "F17 Review Requested: $F17"

# 18. Review Received (RADIO Yes/No)
F18=$(create_field "Review Received" "RADIO" '{
  "name": "Review Received",
  "dataType": "RADIO",
  "options": [
    {"label": "Yes"},
    {"label": "No"}
  ]
}')
echo "F18 Review Received: $F18"

# 19. Neighbour Campaign Sent (RADIO Yes/No)
F19=$(create_field "Neighbour Campaign Sent" "RADIO" '{
  "name": "Neighbour Campaign Sent",
  "dataType": "RADIO",
  "options": [
    {"label": "Yes"},
    {"label": "No"}
  ]
}')
echo "F19 Neighbour Campaign Sent: $F19"

# 20. Annual Sealing Reminder (RADIO Yes/No)
F20=$(create_field "Annual Sealing Reminder" "RADIO" '{
  "name": "Annual Sealing Reminder",
  "dataType": "RADIO",
  "options": [
    {"label": "Yes"},
    {"label": "No"}
  ]
}')
echo "F20 Annual Sealing Reminder: $F20"

echo ""
echo "=== PHASE 1 COMPLETE ==="
echo ""
echo "Starting Phase 2: Pipelines"

# Helper: create pipeline
create_pipeline() {
  local NAME="$1"
  curl -s -X POST "${BASE_URL}/opportunities/pipelines" \
    -H "Authorization: Bearer ${GHL_TOKEN}" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"${NAME}\", \"locationId\": \"${LOC_ID}\"}"
}

# Pipeline 1: Concrete - Residential Driveway
P1=$(create_pipeline "Concrete - Residential Driveway")
echo "Pipeline 1 (Residential Driveway): $P1"
P1_ID=$(echo "$P1" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id',''))" 2>/dev/null)

# Pipeline 2: Concrete - Interlock / Stamped / Premium
P2=$(create_pipeline "Concrete - Interlock / Stamped / Premium")
echo "Pipeline 2 (Interlock/Stamped): $P2"
P2_ID=$(echo "$P2" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id',''))" 2>/dev/null)

# Pipeline 3: Concrete - Repair & Resurfacing
P3=$(create_pipeline "Concrete - Repair & Resurfacing")
echo "Pipeline 3 (Repair/Resurfacing): $P3"
P3_ID=$(echo "$P3" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id',''))" 2>/dev/null)

# Pipeline 4: Concrete - Commercial / Parking Lot
P4=$(create_pipeline "Concrete - Commercial / Parking Lot")
echo "Pipeline 4 (Commercial): $P4"
P4_ID=$(echo "$P4" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id',''))" 2>/dev/null)

echo "Pipeline IDs: P1=$P1_ID P2=$P2_ID P3=$P3_ID P4=$P4_ID"

# Helper: add stage to pipeline
add_stage() {
  local PID="$1"
  local SNAME="$2"
  local POS="$3"
  curl -s -X POST "${BASE_URL}/opportunities/pipelines/${PID}/stages" \
    -H "Authorization: Bearer ${GHL_TOKEN}" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"${SNAME}\", \"position\": ${POS}}"
}

echo ""
echo "--- Pipeline 1 Stages ---"
S1_0=$(add_stage "$P1_ID" "New Lead" 0); echo "P1 Stage 0: $(echo $S1_0 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_1=$(add_stage "$P1_ID" "Estimate Scheduled" 1); echo "P1 Stage 1: $(echo $S1_1 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_2=$(add_stage "$P1_ID" "Estimate Complete" 2); echo "P1 Stage 2: $(echo $S1_2 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_3=$(add_stage "$P1_ID" "Proposal Sent" 3); echo "P1 Stage 3: $(echo $S1_3 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_4=$(add_stage "$P1_ID" "Follow-Up Active" 4); echo "P1 Stage 4: $(echo $S1_4 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_5=$(add_stage "$P1_ID" "Contract Signed / Deposit" 5); echo "P1 Stage 5: $(echo $S1_5 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_6=$(add_stage "$P1_ID" "Weather Window Confirmed" 6); echo "P1 Stage 6: $(echo $S1_6 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_7=$(add_stage "$P1_ID" "Prep/Demo" 7); echo "P1 Stage 7: $(echo $S1_7 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_8=$(add_stage "$P1_ID" "Pour/Install Day" 8); echo "P1 Stage 8: $(echo $S1_8 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_9=$(add_stage "$P1_ID" "Cure Period" 9); echo "P1 Stage 9: $(echo $S1_9 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_10=$(add_stage "$P1_ID" "Sealing Complete" 10); echo "P1 Stage 10: $(echo $S1_10 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_11=$(add_stage "$P1_ID" "Job Complete" 11); echo "P1 Stage 11: $(echo $S1_11 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_12=$(add_stage "$P1_ID" "Invoice Sent" 12); echo "P1 Stage 12: $(echo $S1_12 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_13=$(add_stage "$P1_ID" "Paid" 13); echo "P1 Stage 13: $(echo $S1_13 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_14=$(add_stage "$P1_ID" "Review Requested" 14); echo "P1 Stage 14: $(echo $S1_14 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S1_15=$(add_stage "$P1_ID" "Neighbour Campaign" 15); echo "P1 Stage 15: $(echo $S1_15 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"

echo ""
echo "--- Pipeline 2 Stages ---"
S2_0=$(add_stage "$P2_ID" "New Inquiry" 0); echo "P2 Stage 0: $(echo $S2_0 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_1=$(add_stage "$P2_ID" "Site Visit Scheduled" 1); echo "P2 Stage 1: $(echo $S2_1 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_2=$(add_stage "$P2_ID" "Design Consultation" 2); echo "P2 Stage 2: $(echo $S2_2 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_3=$(add_stage "$P2_ID" "Proposal Sent" 3); echo "P2 Stage 3: $(echo $S2_3 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_4=$(add_stage "$P2_ID" "Follow-Up Active" 4); echo "P2 Stage 4: $(echo $S2_4 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_5=$(add_stage "$P2_ID" "Contract Signed / Deposit" 5); echo "P2 Stage 5: $(echo $S2_5 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_6=$(add_stage "$P2_ID" "Materials Ordered" 6); echo "P2 Stage 6: $(echo $S2_6 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_7=$(add_stage "$P2_ID" "Prep/Excavation" 7); echo "P2 Stage 7: $(echo $S2_7 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_8=$(add_stage "$P2_ID" "Base Work" 8); echo "P2 Stage 8: $(echo $S2_8 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_9=$(add_stage "$P2_ID" "Install In Progress" 9); echo "P2 Stage 9: $(echo $S2_9 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_10=$(add_stage "$P2_ID" "Polymeric Sand/Sealing" 10); echo "P2 Stage 10: $(echo $S2_10 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_11=$(add_stage "$P2_ID" "Job Complete" 11); echo "P2 Stage 11: $(echo $S2_11 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_12=$(add_stage "$P2_ID" "Invoice Sent" 12); echo "P2 Stage 12: $(echo $S2_12 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_13=$(add_stage "$P2_ID" "Paid" 13); echo "P2 Stage 13: $(echo $S2_13 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S2_14=$(add_stage "$P2_ID" "Review + Referral" 14); echo "P2 Stage 14: $(echo $S2_14 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"

echo ""
echo "--- Pipeline 3 Stages ---"
S3_0=$(add_stage "$P3_ID" "New Lead" 0); echo "P3 Stage 0: $(echo $S3_0 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_1=$(add_stage "$P3_ID" "Estimate Booked" 1); echo "P3 Stage 1: $(echo $S3_1 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_2=$(add_stage "$P3_ID" "Estimate Complete" 2); echo "P3 Stage 2: $(echo $S3_2 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_3=$(add_stage "$P3_ID" "Proposal Sent" 3); echo "P3 Stage 3: $(echo $S3_3 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_4=$(add_stage "$P3_ID" "Follow-Up Active" 4); echo "P3 Stage 4: $(echo $S3_4 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_5=$(add_stage "$P3_ID" "Repair Scheduled" 5); echo "P3 Stage 5: $(echo $S3_5 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_6=$(add_stage "$P3_ID" "Repair Complete" 6); echo "P3 Stage 6: $(echo $S3_6 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_7=$(add_stage "$P3_ID" "Invoice Sent" 7); echo "P3 Stage 7: $(echo $S3_7 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_8=$(add_stage "$P3_ID" "Paid" 8); echo "P3 Stage 8: $(echo $S3_8 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S3_9=$(add_stage "$P3_ID" "Review + Sealing Upsell" 9); echo "P3 Stage 9: $(echo $S3_9 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"

echo ""
echo "--- Pipeline 4 Stages ---"
S4_0=$(add_stage "$P4_ID" "New Prospect" 0); echo "P4 Stage 0: $(echo $S4_0 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_1=$(add_stage "$P4_ID" "Site Assessment" 1); echo "P4 Stage 1: $(echo $S4_1 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_2=$(add_stage "$P4_ID" "Proposal Submitted" 2); echo "P4 Stage 2: $(echo $S4_2 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_3=$(add_stage "$P4_ID" "Contract Awarded" 3); echo "P4 Stage 3: $(echo $S4_3 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_4=$(add_stage "$P4_ID" "Permit Applied" 4); echo "P4 Stage 4: $(echo $S4_4 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_5=$(add_stage "$P4_ID" "Mobilization" 5); echo "P4 Stage 5: $(echo $S4_5 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_6=$(add_stage "$P4_ID" "Work In Progress" 6); echo "P4 Stage 6: $(echo $S4_6 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_7=$(add_stage "$P4_ID" "Inspection" 7); echo "P4 Stage 7: $(echo $S4_7 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_8=$(add_stage "$P4_ID" "Job Complete" 8); echo "P4 Stage 8: $(echo $S4_8 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_9=$(add_stage "$P4_ID" "Invoice Sent" 9); echo "P4 Stage 9: $(echo $S4_9 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_10=$(add_stage "$P4_ID" "Paid" 10); echo "P4 Stage 10: $(echo $S4_10 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"
S4_11=$(add_stage "$P4_ID" "Maintenance Contract" 11); echo "P4 Stage 11: $(echo $S4_11 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('stage',{}).get('id','ERR'))" 2>/dev/null)"

echo ""
echo "=== PHASE 2 COMPLETE ==="
echo ""
echo "Starting Phase 3: Calendars"

create_calendar() {
  local CAL_NAME="$1"
  local DURATION="$2"
  curl -s -X POST "${BASE_URL}/calendars/" \
    -H "Authorization: Bearer ${GHL_TOKEN}" \
    -H "Version: 2021-04-15" \
    -H "Content-Type: application/json" \
    -d "{
      \"name\": \"${CAL_NAME}\",
      \"locationId\": \"${LOC_ID}\",
      \"description\": \"${CAL_NAME}\",
      \"slotDuration\": ${DURATION},
      \"slotInterval\": ${DURATION},
      \"isActive\": true,
      \"autoConfirm\": true,
      \"calendarType\": \"event\"
    }"
}

CAL1=$(create_calendar "Free Estimate - Concrete/Driveway" 45)
echo "Calendar 1 (Free Estimate): $CAL1"

CAL2=$(create_calendar "Design Consultation - Premium Concrete" 60)
echo "Calendar 2 (Design Consultation): $CAL2"

CAL3=$(create_calendar "Commercial Site Assessment" 60)
echo "Calendar 3 (Commercial Site Assessment): $CAL3"

echo ""
echo "=== PHASE 3 COMPLETE ==="
echo ""
echo "Starting Phase 4: Tags"

create_tag() {
  local TAG_NAME="$1"
  curl -s -X POST "${BASE_URL}/locations/${LOC_ID}/tags" \
    -H "Authorization: Bearer ${GHL_TOKEN}" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"${TAG_NAME}\"}"
}

TAGS=(
  "new-lead"
  "driveway-replacement"
  "new-driveway"
  "interlock"
  "stamped-concrete"
  "exposed-aggregate"
  "flatwork"
  "crack-repair"
  "resurfacing"
  "asphalt"
  "commercial-parking"
  "walkway-steps"
  "weather-hold"
  "permit-required"
  "estimate-sent"
  "deposit-paid"
  "contract-signed"
  "cure-period"
  "job-complete"
  "sealing-done"
  "annual-sealing-due"
  "review-requested"
  "review-received"
  "referral"
  "neighbour-campaign"
  "cold-lead"
  "no-show"
  "google-lsa"
  "real-estate-agent"
  "property-manager"
  "repeat-customer"
  "facebook-ad"
  "sealing-upsell-candidate"
)

for TAG in "${TAGS[@]}"; do
  RESULT=$(create_tag "$TAG")
  TAG_ID=$(echo "$RESULT" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('tag',{}).get('id','ERR'))" 2>/dev/null)
  echo "Tag '$TAG': $TAG_ID"
  sleep 0.3
done

echo ""
echo "=== PHASE 4 COMPLETE ==="
echo "Build complete! Saving log..."
