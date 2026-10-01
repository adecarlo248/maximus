#!/bin/bash
# Create Pipelines for Deck & Patio Snapshot
TOKEN="pit-34762dfe-6b1f-4363-b679-09f75923296b"
LOCATION_ID="AVeFEPk8yZ1yiaWgfOOP"
BASE_URL="https://services.leadconnectorhq.com"

ghl_post() {
  local endpoint="$1"
  local body="$2"
  curl -s -X POST "${BASE_URL}${endpoint}" \
    -H "Authorization: Bearer ${TOKEN}" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "${body}"
}

echo "=== PHASE 2: PIPELINES ==="

# Pipeline 1: Deck - New Build
echo "Creating Pipeline 1: Deck - New Build..."
RESULT=$(ghl_post "/opportunities/pipelines" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck - New Build\",
  \"stages\": [
    {\"name\": \"New Lead\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Design Consultation Scheduled\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Consultation Complete\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Design Approved\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Proposal Sent\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Follow-Up Active\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Contract Signed / Deposit\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Permit Applied\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Permit Approved\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Materials Ordered\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build Start\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Framing\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Decking\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Railing/Finishing\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Job Complete\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Invoice Sent\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Paid\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Review Requested\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Neighbour Campaign\", \"showInFunnel\": true, \"showInPieChart\": true}
  ]
}")
P1_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id','ERROR'))")
echo "Pipeline 1 ID: $P1_ID"
sleep 1

# Pipeline 2: Deck - Repair & Refinishing
echo "Creating Pipeline 2: Deck - Repair & Refinishing..."
RESULT=$(ghl_post "/opportunities/pipelines" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck - Repair & Refinishing\",
  \"stages\": [
    {\"name\": \"New Lead\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Estimate Scheduled\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Estimate Complete\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Proposal Sent\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Follow-Up Active\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Work Scheduled\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Work In Progress\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Job Complete\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Invoice Sent\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Paid\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Review + Composite Upsell\", \"showInFunnel\": true, \"showInPieChart\": true}
  ]
}")
P2_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id','ERROR'))")
echo "Pipeline 2 ID: $P2_ID"
sleep 1

# Pipeline 3: Deck - Pergola / Outdoor Structure
echo "Creating Pipeline 3: Deck - Pergola / Outdoor Structure..."
RESULT=$(ghl_post "/opportunities/pipelines" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck - Pergola / Outdoor Structure\",
  \"stages\": [
    {\"name\": \"New Inquiry\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Design Consultation\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Proposal Sent\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Follow-Up Active\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Contract Signed / Deposit\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Permit Applied\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Materials Ordered\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build Start\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build Complete\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Invoice Sent\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Paid\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Review + Referral\", \"showInFunnel\": true, \"showInPieChart\": true}
  ]
}")
P3_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id','ERROR'))")
echo "Pipeline 3 ID: $P3_ID"
sleep 1

# Pipeline 4: Deck - Commercial / HOA
echo "Creating Pipeline 4: Deck - Commercial / HOA..."
RESULT=$(ghl_post "/opportunities/pipelines" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck - Commercial / HOA\",
  \"stages\": [
    {\"name\": \"New Prospect\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Site Assessment\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Proposal Submitted\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Contract Awarded\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Permit Applied\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build Scheduled\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build In Progress\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Inspection\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Job Complete\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Invoice Sent\", \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Paid\", \"showInFunnel\": true, \"showInPieChart\": true}
  ]
}")
P4_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id','ERROR'))")
echo "Pipeline 4 ID: $P4_ID"

echo ""
echo "=== PIPELINES COMPLETE ==="
echo "P1 (New Build): $P1_ID"
echo "P2 (Repair/Refinishing): $P2_ID"
echo "P3 (Pergola/Outdoor): $P3_ID"
echo "P4 (Commercial/HOA): $P4_ID"
