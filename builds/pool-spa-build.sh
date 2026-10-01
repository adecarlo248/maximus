#!/bin/bash
# Pool & Spa GHL Snapshot Build Script
# Location: lqHFFe4zxaoMPysaTPAQ
# API Token: pit-9720e63a-8354-4b54-af00-5e56a44e3adb

LOC="lqHFFe4zxaoMPysaTPAQ"
TOKEN="pit-9720e63a-8354-4b54-af00-5e56a44e3adb"
BASE="https://services.leadconnectorhq.com"
LOG="/home/maximus/.openclaw/workspace/builds/pool-spa-snapshot-build-log.md"

create_custom_field() {
  local name="$1"
  local type="$2"
  local options="$3"  # JSON array string or empty
  
  if [ -n "$options" ]; then
    payload="{\"name\":\"$name\",\"dataType\":\"$type\",\"picklistOptions\":$options,\"locationId\":\"$LOC\"}"
  else
    payload="{\"name\":\"$name\",\"dataType\":\"$type\",\"locationId\":\"$LOC\"}"
  fi
  
  curl -s -X POST "$BASE/locations/$LOC/customFields" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "$payload"
}

create_pipeline() {
  local name="$1"
  local stages_json="$2"
  
  payload="{\"name\":\"$name\",\"stages\":$stages_json,\"locationId\":\"$LOC\"}"
  
  curl -s -X POST "$BASE/opportunities/pipelines" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "$payload"
}

echo "Build script loaded. LOC=$LOC"
