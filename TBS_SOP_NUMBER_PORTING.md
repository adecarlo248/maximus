# TBS — Phone Number Porting SOP
*Non-Twilio → LC Phone (GHL)*
*Saved: 2026-04-23 — use when onboarding clients who want to port their existing number*

---

## When to Use This
- Client has an existing business number with a regular carrier (Bell, Rogers, AT&T, Verizon, etc.)
- You want it hosted in their GHL sub-account using LC Phone
- Their sub-account shows **LC Phone branding** (no Twilio SID/Auth Token fields)

If the number is already in Twilio → that's a different process (Twilio → LC via GHL Support ticket)

---

## Your Client Onboarding Workflow

1. Assign a fresh LC number → get them live immediately
2. Submit port request in parallel
3. When port completes → swap to their real number
4. Client never has downtime, you start billing from day one

---

## Collect From Client

- Phone number in E.164 format (+1XXXXXXXXXX)
- Current carrier name (Bell, Rogers, etc.)
- Account number with carrier
- Account PIN or passcode (or last 4 of SSN if wireless)
- Exact legal name on the account
- Exact service address on the account (no PO Boxes)
- Recent phone bill — PDF, under 4MB, shows name + address + number
- Signed LOA (GHL provides the template)

---

## Submit the Port Request

- Confirm sub-account is LC Phone (Settings → Phone System)
- Get the Location ID (Settings → Business Profile)
- GHL Help Center → search "Porting your phone number (non-Twilio number) to a location/subaccount"
- Fill out the porting form with all documents attached
- If form link is broken → open a GHL Support ticket with Location ID + number list

---

## Critical Rules

- **Do NOT cancel the old carrier** until port is fully confirmed working
- Test inbound calls, outbound calls, AND SMS before cancelling
- Historical call logs and SMS do NOT transfer — download from old carrier first if needed
- Keep old carrier active through the entire 2–4 week process

---

## After Port Completes (FOC Date)

- Test inbound calls → working in GHL?
- Test outbound calls → correct caller ID showing?
- Test SMS in and out → working?
- Once all confirmed → client can cancel old carrier safely

---

## Timeline

2–4 weeks from submission. Monitor email for status updates or rejection notices.

**Common rejection reasons:**
- Name/address mismatch with carrier records
- Wrong account number or PIN
- Numbers not listed on that account

Fix → resubmit with corrected info.
