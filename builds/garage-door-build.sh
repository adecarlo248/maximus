#!/bin/bash
# Garage Door GHL Snapshot Build Script
# Location: 2kw5x1ZAluEpsa48PzYa

TOKEN="pit-5ed7bd00-30ba-45da-aeda-fa0d6142c7fd"
LOC="2kw5x1ZAluEpsa48PzYa"
BASE="https://services.leadconnectorhq.com"
LOG="/home/maximus/.openclaw/workspace/builds/garage-door-snapshot-build-log.md"

# Helper function
ghl_post() {
  local endpoint="$1"
  local body="$2"
  curl -s -X POST "${BASE}${endpoint}" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Version: 2021-07-28" \
    -H "Content-Type: application/json" \
    -d "$body"
}

ghl_get() {
  local endpoint="$1"
  curl -s -X GET "${BASE}${endpoint}" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Version: 2021-07-28"
}

echo "Build script ready"
