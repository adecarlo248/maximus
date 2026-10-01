# Save / Backup Audit — 2026-10-01

Read-only audit. **Nothing was committed, pulled, pushed, or overwritten.**

---

## 1. Repos that are SAFE (no real work at risk)

### `claude-learning-lab/sacredwaterswomen.ca`
- In sync with `origin/main`, zero uncommitted changes. Clean.

### `claude-learning-lab/use1app.com` → `github.com/adecarlo248/1APP`
- Shows 30 modified files, but `git diff --summary` proves they are **file-mode changes only** (`100644 => 100755`) with `0 insertions(+), 0 deletions(-)`.
- Cause: Windows/WSL drive mount flipping the executable bit, with `core.fileMode = true`.
- **No content is at risk.** Local clone is 28 commits *behind* origin — the real work (Revenue Reactivation Sprint, A2P chat widget, Sept blog posts) is already safe on GitHub.
- Correction to an earlier claim: the blog cron is **healthy**. Live site has posts on Sept 14, 21, 28 (weekly Sunday cadence). The stale `last-blog-run.txt` dated 2026-08-17 lives only in this behind-by-28 local mirror.

### `claude-learning-lab/deploy-tntoperators` and `deploy-littlenestnaturals`
- Diffs are pure CRLF/LF line-ending flips — equal counts (1351/1351 and 852/852 insert/delete).
- Content is byte-identical to committed state. **Nothing to save.**

---

## 2. REAL unsaved work — OpenClaw workspace (`~/.openclaw/workspace` → `adecarlo248/maximus`)

### a) 794 untracked files, ~2.0 GB, never committed anywhere
Never pushed to GitHub. Highlights:
- `1app/` — 54 files, 1.2 GB, including today's `1APP-Business-Revenue-Audit-2026-10-01.md`, the Associate Sales Program v1/v2, 30-Day Client Acquisition Business Plan, PagePros/LeadPRO handoff briefs, Make automated-onboarding scenario
- `memory/` — 564 files including `2026-09-30.md` and all `dreaming/{light,deep,rem}/` entries
- `clients/` — 34 MB
- Peterborough Waterproofing leave-behinds, QBO e-transfer blueprint, onboarding question sets
- 674 of these are documents (md/html/pdf/csv/py/svg) — actual work product

### b) Uncommitted content edits to tracked files
- `AGENTS.md` — **+112 lines**
- `MEMORY.md` — **+27 lines**
- `SOUL.md` — **+20 lines**
- `USER.md` — +1 line
- `memory/2026-08-14.md` — +5/-3
- `tntoperators/index.html` — +1143/-1101

### c) 8 tracked files DELETED from working tree, deletion not committed
- `HEARTBEAT.md` ← AGENTS.md still instructs reading this on heartbeats
- `TOOLS.md` ← content was migrated into AGENTS.md
- `.openclaw/workspace-state.json`
- `memory/.dreams/` — `daily-ingestion.json`, `events.jsonl`, `phase-signals.json`, `session-ingestion.json`, `short-term-recall.json`
- All still recoverable via `git checkout -- <file>` since the deletion is unstaged.

### d) No `.gitignore` at all (file exists but is empty)
Three virtualenvs sit untracked and would be swept in by a blind `git add .`:
- `.venv-video-edit` 402 MB, `.venv-card` 185 MB, `.venv-video` 184 MB (**771 MB total**)
- Plus `tmp/` (6.4 MB), `video_frames/`, `__pycache__`, and a `.migrated` state artifact

---

## 3. VS Code folder is NOT under version control

`/mnt/c/Users/tony/Desktop/claude-learning-lab/` has **no `.git` at its top level.** Only the four subfolders are repos. These top-level files are versioned nowhere:

- `CLAUDE.md`, `Context.md`, `AGENTS.md`, `USER.md`, `IDENTITY.md`, `HEARTBEAT.md`, `TOOLS.md`
- `HOW_MONEY_WORKS.md`, `PRIMERICA_CANADA.md`, `REFERENCES.md`, `SHADOW_OPERATOR.md`, `TEACHING_GUIDE.md`
- `1APP-Elevator-Pitch.pdf`, `1APP-Elevator-Pitch-tightened.pdf`, `generate_1app_pitch_pdf.py`
- `lab1.py`, `lab3.py`, `lab2-primerica-vector-db.ipynb`
- `booking.html`, TNT Instagram post assets, Little Nest bundle images
- `memory/`, `docs/`, `chroma_db/`, `Peterborough-Waterproofing-Onboarding/`, `littlenestnaturals/`

A disk failure or a bad folder delete loses all of it. Note a `.env` also sits at this level.

---

## 4. SECURITY — needs action

The workspace repo's `origin` remote has a **GitHub personal access token embedded in plaintext in the URL**, stored in `.git/config`:

```
https://<TOKEN>@github.com/adecarlo248/maximus.git
```

Anyone who reads that file, or any backup/screenshot/sync of it, gets push access to the repo. The token value is not reproduced here.

Recommended: revoke that token at github.com/settings/tokens, then re-point the remote at SSH (`git@github.com:adecarlo248/maximus.git`) or use a credential helper so no secret lives in the repo.

---

## 5. Proposed plan — NOT executed, awaiting Tony's approval

1. Write a real `.gitignore` for the workspace: `.venv*/`, `__pycache__/`, `tmp/`, `video_frames/`, `node_modules/`, `*.migrated.*`
2. Decide on `HEARTBEAT.md` + `TOOLS.md` — restore from git, or commit the deletion deliberately
3. Decide on `memory/.dreams/` — runtime state, likely belongs in `.gitignore` rather than the repo
4. Commit the real content edits (`AGENTS.md`, `MEMORY.md`, `SOUL.md`, `USER.md`) in one clearly-labeled commit
5. Commit the untracked work product in batches by area (`1app/`, `memory/`, `clients/`) — check whether the 1.2 GB of `1app/` media belongs in git or in separate storage
6. Rotate the GitHub token and switch the remote to SSH
7. Make `claude-learning-lab` its own repo, or at minimum sync its top-level docs into the workspace repo
8. For `use1app.com`: `git pull` to catch up the 28 commits. Set `core.fileMode false` to stop the phantom mode churn. Nothing needs saving first.
