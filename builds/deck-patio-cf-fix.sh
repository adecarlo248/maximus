#!/bin/bash
# Fix custom fields - correct GHL dataType names
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

# First delete the fields that errored and the ones created with wrong names
# Actually they failed so just create them fresh with correct types

echo "=== Creating Dropdown (SINGLE_OPTIONS) fields ==="

# 1. Lead Source
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Lead Source",
  "dataType": "SINGLE_OPTIONS",
  "fieldKey": "lead_source",
  "position": 0,
  "options": ["Google LSA","Referral","Real Estate Agent","Houzz","Pinterest/Instagram","Door Knock","Facebook Ad","Repeat Customer","Property Manager","Builder/Developer"]
}')
echo "Lead Source: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 2. Job Type
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Job Type",
  "dataType": "SINGLE_OPTIONS",
  "fieldKey": "job_type",
  "position": 1,
  "options": ["New Deck Build","Deck Repair","Deck Refinishing/Staining","Pergola/Gazebo","Patio Installation","Outdoor Kitchen","Fence Addition","Composite Upgrade","Railing Replacement","Commercial"]
}')
echo "Job Type: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 3. Service Category
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Service Category",
  "dataType": "SINGLE_OPTIONS",
  "fieldKey": "service_category",
  "position": 2,
  "options": ["New Build","Repair/Restoration","Pergola/Structure","Outdoor Living","Commercial"]
}')
echo "Service Category: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 4. Decking Material
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Decking Material",
  "dataType": "SINGLE_OPTIONS",
  "fieldKey": "decking_material",
  "position": 3,
  "options": ["Pressure Treated","Cedar","Composite (Trex/Fiberon)","PVC","Hardwood","Aluminum","Unknown"]
}')
echo "Decking Material: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 5. Railing Material
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Railing Material",
  "dataType": "SINGLE_OPTIONS",
  "fieldKey": "railing_material",
  "position": 4,
  "options": ["Wood","Composite","Aluminum","Glass","Cable","Wrought Iron","Unknown"]
}')
echo "Railing Material: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

echo ""
echo "=== Creating RADIO fields ==="

# 6. Permit Required (RADIO)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Permit Required",
  "dataType": "RADIO",
  "fieldKey": "permit_required",
  "position": 5,
  "options": ["Yes","No"]
}')
echo "Permit Required: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 8. Design Approval Required (RADIO)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Design Approval Required",
  "dataType": "RADIO",
  "fieldKey": "design_approval_required",
  "position": 7,
  "options": ["Yes","No"]
}')
echo "Design Approval Required: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 9. Design Approved (RADIO)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Design Approved",
  "dataType": "RADIO",
  "fieldKey": "design_approved",
  "position": 8,
  "options": ["Yes","No"]
}')
echo "Design Approved: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 11. Estimate Amount (MONETORY - note GHL typo)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Estimate Amount",
  "dataType": "MONETORY",
  "fieldKey": "estimate_amount",
  "position": 10
}')
echo "Estimate Amount: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 12. Contract Amount (MONETORY)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Contract Amount",
  "dataType": "MONETORY",
  "fieldKey": "contract_amount",
  "position": 11
}')
echo "Contract Amount: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 13. Deposit Paid (RADIO)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Deposit Paid",
  "dataType": "RADIO",
  "fieldKey": "deposit_paid",
  "position": 12,
  "options": ["Yes","No"]
}')
echo "Deposit Paid: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 15. Material Lead Time (SINGLE_OPTIONS dropdown)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Material Lead Time",
  "dataType": "SINGLE_OPTIONS",
  "fieldKey": "material_lead_time",
  "position": 14,
  "options": ["In Stock","1-2 weeks","2-4 weeks","4+ weeks","Unknown"]
}')
echo "Material Lead Time: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 18. Review Requested (RADIO)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Review Requested",
  "dataType": "RADIO",
  "fieldKey": "review_requested",
  "position": 17,
  "options": ["Yes","No"]
}')
echo "Review Requested: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 19. Review Received (RADIO)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Review Received",
  "dataType": "RADIO",
  "fieldKey": "review_received",
  "position": 18,
  "options": ["Yes","No"]
}')
echo "Review Received: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

# 20. Neighbour Campaign Sent (RADIO)
RESULT=$(ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Neighbour Campaign Sent",
  "dataType": "RADIO",
  "fieldKey": "neighbour_campaign_sent",
  "position": 19,
  "options": ["Yes","No"]
}')
echo "Neighbour Campaign Sent: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); cf=d.get('customField',{}); print(cf.get('id','ERROR'), d.get('message',''))")"
sleep 0.5

echo ""
echo "=== ALL CUSTOM FIELDS DONE ==="
