#!/bin/bash
# Create Calendars for Deck & Patio Snapshot
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

echo "=== PHASE 3: CALENDARS ==="

# First, let's check what calendar groups exist
echo "Checking existing calendar groups..."
curl -s -X GET "${BASE_URL}/calendars/groups?locationId=${LOCATION_ID}" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Version: 2021-07-28" | python3 -c "import sys,json; d=json.load(sys.stdin); groups=d.get('groups',[]); [print(f'Group: {g[\"name\"]} | ID: {g[\"id\"]}') for g in groups]; print(f'Total groups: {len(groups)}')"

echo ""

# Calendar 1: Free Design Consultation - Deck/Patio (60 min, Mon-Fri 9am-5pm)
echo "Creating Calendar 1: Free Design Consultation - Deck/Patio..."
RESULT=$(ghl_post "/calendars/" '{
  "locationId": "AVeFEPk8yZ1yiaWgfOOP",
  "name": "Free Design Consultation - Deck/Patio",
  "description": "Free 60-minute on-site design consultation for decks, patios, pergolas, and outdoor living spaces.",
  "slotDuration": 60,
  "slotBuffer": 30,
  "appoinmentPerSlot": 1,
  "calendarType": "EVENT",
  "availabilities": [
    {
      "date": "2026-01-05",
      "hours": [{"openHour": 9, "openMinute": 0, "closeHour": 17, "closeMinute": 0}],
      "deleted": false
    }
  ],
  "openHours": [
    {
      "daysOfTheWeek": [1, 2, 3, 4, 5],
      "hours": [{"openHour": 9, "openMinute": 0, "closeHour": 17, "closeMinute": 0}]
    }
  ]
}')
echo "Calendar 1 Raw: $(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2))")" 2>&1 | head -20

# Try simpler calendar create
echo "Trying simpler Calendar 1 create..."
RESULT=$(ghl_post "/calendars/" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Free Design Consultation - Deck/Patio\",
  \"description\": \"Free 60-minute on-site design consultation for decks, patios, pergolas, and outdoor living spaces.\",
  \"slotDuration\": 60,
  \"slotBuffer\": 30,
  \"calendarType\": \"EVENT\"
}")
C1_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('calendar',{}).get('id','ERROR: ' + str(d.get('message',d.get('error','')))))")
echo "Calendar 1 ID: $C1_ID"
sleep 1

# Calendar 2: Deck Repair Estimate (45 min, Mon-Fri 8am-5pm)
echo "Creating Calendar 2: Deck Repair Estimate..."
RESULT=$(ghl_post "/calendars/" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Deck Repair Estimate\",
  \"description\": \"Free 45-minute on-site estimate for deck repair, board replacement, and refinishing projects.\",
  \"slotDuration\": 45,
  \"slotBuffer\": 15,
  \"calendarType\": \"EVENT\"
}")
C2_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('calendar',{}).get('id','ERROR: ' + str(d.get('message',d.get('error','')))))")
echo "Calendar 2 ID: $C2_ID"
sleep 1

# Calendar 3: Commercial Site Assessment (90 min, Mon-Fri 8am-4pm)
echo "Creating Calendar 3: Commercial Site Assessment..."
RESULT=$(ghl_post "/calendars/" "{
  \"locationId\": \"${LOCATION_ID}\",
  \"name\": \"Commercial Site Assessment\",
  \"description\": \"90-minute on-site assessment for commercial deck, HOA, and multi-unit outdoor living projects.\",
  \"slotDuration\": 90,
  \"slotBuffer\": 30,
  \"calendarType\": \"EVENT\"
}")
C3_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('calendar',{}).get('id','ERROR: ' + str(d.get('message',d.get('error','')))))")
echo "Calendar 3 ID: $C3_ID"

echo ""
echo "=== CALENDARS COMPLETE ==="
echo "C1 (Design Consultation): $C1_ID"
echo "C2 (Repair Estimate): $C2_ID"
echo "C3 (Commercial Site Assessment): $C3_ID"
