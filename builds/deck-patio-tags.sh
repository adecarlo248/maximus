#!/bin/bash
# Create Tags for Deck & Patio Snapshot
TOKEN="pit-34762dfe-6b1f-4363-b679-09f75923296b"
LOCATION_ID="AVeFEPk8yZ1yiaWgfOOP"
BASE_URL="https://services.leadconnectorhq.com"

create_tag() {
  local name="$1"
  RESULT=$(curl -s -X POST "${BASE_URL}/locations/${LOCATION_ID}/tags" \
    -H "Authorization: Bearer ${TOKEN}" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"${name}\"}")
  TAG_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tag',{}).get('id',d.get('id','ERR')))" 2>/dev/null)
  echo "  Tag '$name': $TAG_ID"
  sleep 0.3
}

echo "=== PHASE 4: TAGS ==="

TAGS=(
  "new-lead"
  "new-deck-build"
  "deck-repair"
  "deck-refinishing"
  "pergola-gazebo"
  "patio-install"
  "outdoor-kitchen"
  "composite-deck"
  "composite-upsell-candidate"
  "cedar-deck"
  "pressure-treated"
  "railing-replacement"
  "permit-required"
  "permit-pending"
  "design-pending"
  "design-approved"
  "material-on-order"
  "estimate-sent"
  "deposit-paid"
  "contract-signed"
  "build-active"
  "job-complete"
  "review-requested"
  "review-received"
  "referral"
  "neighbour-campaign"
  "cold-lead"
  "no-show"
  "google-lsa"
  "houzz-lead"
  "real-estate-agent"
  "repeat-customer"
  "facebook-ad"
  "annual-refinishing-due"
)

for tag in "${TAGS[@]}"; do
  create_tag "$tag"
done

echo ""
echo "=== TAGS COMPLETE (${#TAGS[@]} tags) ==="
