# AGENTS ROADMAP — TNT Operators Multi-Agent System
*Parked idea — 2026-05-05. Build when Tony is ready.*

---

## The Vision

A network of specialist AI agents that run the back-end of Tony's Shadow Operator business automatically. Tony focuses on relationships and closing deals. Agents handle research, writing, tracking, and follow-up.

---

## Planned Agents

### 1. 🔍 Prospect Scout
**Role:** Find creators that match TNT Operators' ideal partner profile
**How it runs:** Scheduled cron job — daily or on-demand
**What it does:**
- Searches hashtags and niches for creators with 10K–500K followers
- Scores them on engagement rate, content consistency, niche fit
- Logs prospects to a tracker file with platform, handle, follower count, niche, notes
- Flags top picks for Tony to review

**Output:** `prospects/YYYY-MM-DD.md` — daily prospect list

---

### 2. ✍️ Outreach Writer
**Role:** Write personalized DM pitches for each creator prospect
**How it runs:** On-demand — Tony feeds it a creator profile, it writes the pitch
**What it does:**
- Reviews the creator's niche, content style, and audience
- Writes a natural, non-salesy DM tailored to that specific creator
- Outputs 2–3 variants (casual / professional / curiosity-hook)
- Tony picks one, copies, sends manually

**Output:** Ready-to-send DM in WhatsApp message or workspace file

---

### 3. 📊 Pipeline Manager
**Role:** Track every creator deal from first contact to live revenue
**How it runs:** On-demand updates + weekly summary cron
**Pipeline stages:**
1. Prospect identified
2. DM sent
3. Reply received
4. Call booked
5. Deal agreed
6. Product in build
7. Store live
8. Revenue generating

**Output:** `pipeline/pipeline.md` — deal tracker with stage, next action, last contact date

---

### 4. 📅 Follow-up Agent
**Role:** Make sure no creator lead goes cold
**How it runs:** Daily heartbeat check
**What it does:**
- Reviews pipeline for any contact not followed up in 3+ days
- Drafts a follow-up message for Tony to send
- Flags urgent re-engagements (7+ days no contact = cold alert)

**Output:** WhatsApp message to Tony with follow-up tasks for the day

---

### 5. 📈 Revenue Reporter (Future)
**Role:** Weekly snapshot of TNT Operators business performance
**How it runs:** Every Monday morning cron
**What it does:**
- Summarizes active deals and pipeline value
- Tracks revenue by creator deal
- Flags what's working and what needs attention

---

## Architecture

```
Tony (WhatsApp)
     |
     v
Maximus (Main Agent / Orchestrator)
     |
     +---> Prospect Scout (isolated cron agent)
     |
     +---> Outreach Writer (isolated on-demand agent)
     |
     +---> Pipeline Manager (isolated on-demand agent)
     |
     +---> Follow-up Agent (daily heartbeat)
     |
     +---> Revenue Reporter (weekly cron)
```

All agents:
- Spawn as isolated sessions via `sessions_spawn`
- Read/write shared workspace files for continuity
- Report results back to Tony via WhatsApp
- Tony approves anything that goes external (DMs, emails)

---

## Dependencies to Install

Run these when ready to build:

```bash
# Playwright for web browsing / hashtag research
npm install -g playwright
npx playwright install chromium

# Cheerio for lightweight HTML scraping
npm install cheerio

# Puppeteer (backup browser automation)
npm install puppeteer

# CSV / spreadsheet handling
npm install csv-parser csv-writer

# Date utilities
npm install date-fns

# HTTP requests
npm install axios
```

---

## Files to Create When Building

- `prospects/` — daily prospect logs
- `pipeline/pipeline.md` — master deal tracker
- `agents/scout.md` — scout agent instructions
- `agents/outreach.md` — outreach writer instructions
- `agents/pipeline.md` — pipeline manager instructions
- `agents/followup.md` — follow-up agent instructions

---

## When to Build This

Tony's signal to start: **after first Shadow Operator deal is closed and live.**
That's the proof of concept. Then we automate the prospecting pipeline.

---

*Reference: discussed 2026-05-05. Tony said "save for later."*
