#!/bin/bash
# Create Pipelines - with position field in each stage
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

# Pipeline 1: Deck - New Build (19 stages)
echo "Creating Pipeline 1: Deck - New Build..."
RESULT=$(ghl_post "/opportunities/pipelines" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck - New Build\",
  \"stages\": [
    {\"name\": \"New Lead\", \"position\": 0, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Design Consultation Scheduled\", \"position\": 1, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Consultation Complete\", \"position\": 2, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Design Approved\", \"position\": 3, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Proposal Sent\", \"position\": 4, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Follow-Up Active\", \"position\": 5, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Contract Signed / Deposit\", \"position\": 6, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Permit Applied\", \"position\": 7, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Permit Approved\", \"position\": 8, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Materials Ordered\", \"position\": 9, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build Start\", \"position\": 10, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Framing\", \"position\": 11, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Decking\", \"position\": 12, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Railing/Finishing\", \"position\": 13, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Job Complete\", \"position\": 14, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Invoice Sent\", \"position\": 15, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Paid\", \"position\": 16, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Review Requested\", \"position\": 17, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Neighbour Campaign\", \"position\": 18, \"showInFunnel\": true, \"showInPieChart\": true}
  ]
}")
P1_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id','ERROR: ' + str(d.get('message',''))))")
echo "Pipeline 1 ID: $P1_ID"
sleep 1

# Pipeline 2: Deck - Repair & Refinishing (11 stages)
echo "Creating Pipeline 2: Deck - Repair & Refinishing..."
RESULT=$(ghl_post "/opportunities/pipelines" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck - Repair & Refinishing\",
  \"stages\": [
    {\"name\": \"New Lead\", \"position\": 0, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Estimate Scheduled\", \"position\": 1, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Estimate Complete\", \"position\": 2, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Proposal Sent\", \"position\": 3, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Follow-Up Active\", \"position\": 4, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Work Scheduled\", \"position\": 5, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Work In Progress\", \"position\": 6, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Job Complete\", \"position\": 7, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Invoice Sent\", \"position\": 8, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Paid\", \"position\": 9, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Review + Composite Upsell\", \"position\": 10, \"showInFunnel\": true, \"showInPieChart\": true}
  ]
}")
P2_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id','ERROR: ' + str(d.get('message',''))))")
echo "Pipeline 2 ID: $P2_ID"
sleep 1

# Pipeline 3: Deck - Pergola / Outdoor Structure (12 stages)
echo "Creating Pipeline 3: Deck - Pergola / Outdoor Structure..."
RESULT=$(ghl_post "/opportunities/pipelines" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck - Pergola / Outdoor Structure\",
  \"stages\": [
    {\"name\": \"New Inquiry\", \"position\": 0, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Design Consultation\", \"position\": 1, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Proposal Sent\", \"position\": 2, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Follow-Up Active\", \"position\": 3, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Contract Signed / Deposit\", \"position\": 4, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Permit Applied\", \"position\": 5, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Materials Ordered\", \"position\": 6, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build Start\", \"position\": 7, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build Complete\", \"position\": 8, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Invoice Sent\", \"position\": 9, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Paid\", \"position\": 10, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Review + Referral\", \"position\": 11, \"showInFunnel\": true, \"showInPieChart\": true}
  ]
}")
P3_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id','ERROR: ' + str(d.get('message',''))))")
echo "Pipeline 3 ID: $P3_ID"
sleep 1

# Pipeline 4: Deck - Commercial / HOA (11 stages)
echo "Creating Pipeline 4: Deck - Commercial / HOA..."
RESULT=$(ghl_post "/opportunities/pipelines" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck - Commercial / HOA\",
  \"stages\": [
    {\"name\": \"New Prospect\", \"position\": 0, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Site Assessment\", \"position\": 1, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Proposal Submitted\", \"position\": 2, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Contract Awarded\", \"position\": 3, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Permit Applied\", \"position\": 4, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build Scheduled\", \"position\": 5, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Build In Progress\", \"position\": 6, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Inspection\", \"position\": 7, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Job Complete\", \"position\": 8, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Invoice Sent\", \"position\": 9, \"showInFunnel\": true, \"showInPieChart\": true},
    {\"name\": \"Paid\", \"position\": 10, \"showInFunnel\": true, \"showInPieChart\": true}
  ]
}")
P4_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('pipeline',{}).get('id','ERROR: ' + str(d.get('message',''))))")
echo "Pipeline 4 ID: $P4_ID"

echo ""
echo "=== PIPELINES COMPLETE ==="
