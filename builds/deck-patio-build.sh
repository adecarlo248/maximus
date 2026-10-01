#!/bin/bash
# Deck & Patio GHL Snapshot Build Script
# Location: AVeFEPk8yZ1yiaWgfOOP

TOKEN="pit-34762dfe-6b1f-4363-b679-09f75923296b"
LOCATION_ID="AVeFEPk8yZ1yiaWgfOOP"
BASE_URL="https://services.leadconnectorhq.com"
LOG_FILE="/home/maximus/.openclaw/workspace/builds/deck-patio-snapshot-build-log.md"

# Helper function
ghl_post() {
  local endpoint="$1"
  local body="$2"
  curl -s -X POST "${BASE_URL}${endpoint}" \
    -H "Authorization: Bearer ${TOKEN}" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "${body}"
}

echo "BUILD STARTED: $(date)"

# ===================== PHASE 1: CUSTOM FIELDS =====================

echo "Creating custom fields..."

# 1. Lead Source (dropdown)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Lead Source",
  "dataType": "DROPDOWN",
  "fieldKey": "lead_source",
  "position": 0,
  "picklistOptions": ["Google LSA","Referral","Real Estate Agent","Houzz","Pinterest/Instagram","Door Knock","Facebook Ad","Repeat Customer","Property Manager","Builder/Developer"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Lead Source:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 2. Job Type (dropdown)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Job Type",
  "dataType": "DROPDOWN",
  "fieldKey": "job_type",
  "position": 1,
  "picklistOptions": ["New Deck Build","Deck Repair","Deck Refinishing/Staining","Pergola/Gazebo","Patio Installation","Outdoor Kitchen","Fence Addition","Composite Upgrade","Railing Replacement","Commercial"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Job Type:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 3. Service Category (dropdown)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Service Category",
  "dataType": "DROPDOWN",
  "fieldKey": "service_category",
  "position": 2,
  "picklistOptions": ["New Build","Repair/Restoration","Pergola/Structure","Outdoor Living","Commercial"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Service Category:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 4. Decking Material (dropdown)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Decking Material",
  "dataType": "DROPDOWN",
  "fieldKey": "decking_material",
  "position": 3,
  "picklistOptions": ["Pressure Treated","Cedar","Composite (Trex/Fiberon)","PVC","Hardwood","Aluminum","Unknown"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Decking Material:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 5. Railing Material (dropdown)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Railing Material",
  "dataType": "DROPDOWN",
  "fieldKey": "railing_material",
  "position": 4,
  "picklistOptions": ["Wood","Composite","Aluminum","Glass","Cable","Wrought Iron","Unknown"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Railing Material:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 6. Permit Required (RADIO)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Permit Required",
  "dataType": "RADIO",
  "fieldKey": "permit_required",
  "position": 5,
  "picklistOptions": ["Yes","No"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Permit Required:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 7. Permit Number (text)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Permit Number",
  "dataType": "TEXT",
  "fieldKey": "permit_number",
  "position": 6
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Permit Number:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 8. Design Approval Required (RADIO)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Design Approval Required",
  "dataType": "RADIO",
  "fieldKey": "design_approval_required",
  "position": 7,
  "picklistOptions": ["Yes","No"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Design Approval Required:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 9. Design Approved (RADIO)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Design Approved",
  "dataType": "RADIO",
  "fieldKey": "design_approved",
  "position": 8,
  "picklistOptions": ["Yes","No"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Design Approved:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 10. Estimated Square Footage (number)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Estimated Square Footage",
  "dataType": "NUMERICAL",
  "fieldKey": "estimated_square_footage",
  "position": 9
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Estimated Square Footage:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 11. Estimate Amount (currency)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Estimate Amount",
  "dataType": "MONETARY",
  "fieldKey": "estimate_amount",
  "position": 10
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Estimate Amount:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 12. Contract Amount (currency)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Contract Amount",
  "dataType": "MONETARY",
  "fieldKey": "contract_amount",
  "position": 11
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Contract Amount:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 13. Deposit Paid (RADIO)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Deposit Paid",
  "dataType": "RADIO",
  "fieldKey": "deposit_paid",
  "position": 12,
  "picklistOptions": ["Yes","No"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Deposit Paid:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 14. Crew Assigned (text)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Crew Assigned",
  "dataType": "TEXT",
  "fieldKey": "crew_assigned",
  "position": 13
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Crew Assigned:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 15. Material Lead Time (dropdown)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Material Lead Time",
  "dataType": "DROPDOWN",
  "fieldKey": "material_lead_time",
  "position": 14,
  "picklistOptions": ["In Stock","1-2 weeks","2-4 weeks","4+ weeks","Unknown"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Material Lead Time:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 16. Build Start Date (date)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Build Start Date",
  "dataType": "DATE",
  "fieldKey": "build_start_date",
  "position": 15
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Build Start Date:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 17. Build End Date (date)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Build End Date",
  "dataType": "DATE",
  "fieldKey": "build_end_date",
  "position": 16
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Build End Date:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 18. Review Requested (RADIO)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Review Requested",
  "dataType": "RADIO",
  "fieldKey": "review_requested",
  "position": 17,
  "picklistOptions": ["Yes","No"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Review Requested:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 19. Review Received (RADIO)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Review Received",
  "dataType": "RADIO",
  "fieldKey": "review_received",
  "position": 18,
  "picklistOptions": ["Yes","No"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Review Received:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

sleep 0.5

# 20. Neighbour Campaign Sent (RADIO)
ghl_post "/locations/${LOCATION_ID}/customFields" '{
  "name": "Neighbour Campaign Sent",
  "dataType": "RADIO",
  "fieldKey": "neighbour_campaign_sent",
  "position": 19,
  "picklistOptions": ["Yes","No"]
}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Neighbour Campaign Sent:', d.get('customField',{}).get('id','ERROR'), d.get('message',''))"

echo ""
echo "=== CUSTOM FIELDS COMPLETE ==="
