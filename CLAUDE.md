# CLAUDE.md — Session context for picking this project up later

Quick brief to make a future Claude session productive without re-litigating decisions.

## What this is

A Sparx-style adaptive revision game built for **Bertie**, Year 8 at **Chorlton High School, Manchester**. Target: end-of-year **Summer 2026 Progress Tests on 15–26 June 2026**. Static HTML web app, no backend.

**Live:** https://poolieweb.github.io/ks3-test/ (game) and `/parent.html` (verifier)
**Repo:** https://github.com/poolieweb/ks3-test

## Owner / context

- **Parent:** Richard Poole (richard.poole@risksmart.com)
- **Student:** Bertie, Y8 at Chorlton High
- Built across one session in May 2026

## Design philosophy (decisions are locked — don't relitigate)

We borrowed from Sparx Maths research:
- Adaptive Elo-style mastery per skill tag (not per topic — finer-grained)
- Spaced retrieval (3d / 7d / 21d / 60d intervals on mastered skills)
- Three-tier topic progression: Introduce → Strengthen → Deepen
- Interleaving within sessions
- One retry on a wrong answer, then explanation + new variant later
- Working-check loop (Sparx's "bookwork code" mechanic) using built-in scratch canvas

We *avoided* Sparx's pain points:
- No 100%-or-it-doesn't-count gating (causes 3am Sunday-night sessions)
- Equivalent answers accepted via `accepted` array (`1/2` and `0.5` both pass)
- Visible mastery progression (Sparx hides level drift)
- One free streak skip per week

## Locked decisions

| Decision | Value |
|---|---|
| Subjects in scope | Science, History, Geography, Computing (NOT Maths — Sparx owns that) |
| Working pad | Built-in canvas (not physical book) |
| Profile | Single user — Bertie. Personalisation via `profile.json` |
| Treat tiers | Small = evening / Big = full-day / 7-day streak = £5 pocket money / Boss win = Big treat |
| Content additivity | Adding topics never resets scoring (mastery attaches to skill_tags, not topics) |
| Hosting | GitHub Pages on `poolieweb/ks3-test` repo |
| HMAC secret | `change-me-bertie-2026-revision` — **flag for Richard to rotate** before sharing more widely |

## File layout

```
/
├── index.html              # The game Bertie plays (~62 KB, single file with inline JS/CSS)
├── parent.html             # The verifier (~18 KB)
├── profile.json            # Bertie's name, mascot, theme, personal context
├── README.md               # User-facing docs (how to run, deploy, add content)
├── QUESTION_SCHEMA.md      # JSON schema spec for question files
├── CLAUDE.md               # This file
├── .gitignore              # Excludes .DS_Store, *-design.md, etc.
├── .nojekyll               # CRITICAL — without it, GitHub Pages strips files starting with _
└── questions/
    ├── science/            # 5 units, 177 questions
    ├── history/            # 4 units, 120 questions
    ├── geography/          # 2 units, 142 questions
    └── computing/          # 7 units, 160 questions
```

Total: **~599 questions across 18 unit files**.

## How the engine works

`index.html` is a single self-contained file with inline CSS and JS. No build step. Question banks are fetched at boot via relative `fetch('questions/<subject>/_index.json')` then per-unit JSON files.

State lives in `localStorage` under `revisionGameState`. The verifier (`parent.html`) has its own localStorage under `parentLedger` and `parentConfig`.

### Code generation
At session end, app emits a code:
- `SM-...` — small (evening treat)
- `BIG-...` — big (full-day treat)
- `WIN-...` — streak (£5 pocket money)
- `BOSS-...` — boss battle win (counts as big treat + 100 XP)
- `RP-...` — report (didn't hit thresholds, no treat)

Payload is `tier|day|ctr|mins|qs|correct|levels|wpass|wfail`, base64url encoded, HMAC-SHA256 signed (first 8 hex chars). Parent verifier validates signature, rejects replays.

### Mastery engine
- Each `skill_tag` has a 0–100 score, default 50
- Elo-style update with `k = 6`: `score += k * (actual - expected)`
- `expected = sigmoid((score - target_difficulty) / 15)`
- Tiers: 0–40 introduce, 40–70 strengthen, 70–90 deepen, 90+ mastered
- Mastered skills move into spaced-review queue (3d → 7d → 21d → 60d)
- Hint-assisted correct = 0.7 (not full 1.0)
- Two consecutive wrongs drops to easier questions

### Session composition
`pickSessionQuestions(subject, count, opts)` weights by:
- Boost for never-seen questions (+20)
- Penalty for very recently seen (<1 day) (-30)
- Difficulty matched to current mastery (±5 per mismatch)
- +25 if any tag is due for spaced review

Options: `{ boss: true }` for boss mode (diverse difficulty, balanced across units), `{ skillFilter: tag }` to focus on one skill, `{ weakOnly: true }` to drill below-70% skills.

### Features built

- ✅ All 5 question types: mcq, multi-select, numeric, text, order
- ✅ Built-in scratch canvas with pen/eraser, auto-saves per question
- ✅ Working-check loop (every 6 questions in normal mode, skipped in boss)
- ✅ Mastery tree — hierarchical Subject → Unit → Topic → Skill with per-skill Practise button
- ✅ Boss battle mode — 10 Qs, no hints, no retries, 70% to pass, daily cooldown, 30% mastery floor
- ✅ 14 achievements with toast notifications
- ✅ Session history viewer
- ✅ Parent verifier with treat thresholds (configurable per parent), redemption ledger, two-smalls-weekend rule
- ✅ Export progress button (JSON download)
- ✅ Streak tracking with skip days
- ✅ Adaptive Elo mastery + spaced review
- ✅ Visual celebration (different per tier)

## Question schema

See `QUESTION_SCHEMA.md`. Key constraints:
- `skill_tags` should be REUSED across questions where the underlying skill is the same
- `tier` is the pedagogical phase (introduce/strengthen/deepen), `difficulty` (1–5) is the adaptive lever within a tier
- `working_required: true` flags numeric/multi-step questions to trigger the canvas + working-check loop
- `accepted` arrays handle equivalent answers (`1/2`, `0.5`, `50%` etc.)
- ID format is `<sub3>.<unit3>.<topic3>.<NNN>`

## Curriculum sources

Every question's `source` field references the curriculum:
- Most reference the **Chorlton High Y8 Knowledge Map** for the relevant unit (uploaded as PDFs early in the session)
- Where the school KM was thin, content was supplemented from **UK National Curriculum KS3** (tagged `UK NC KS3`)
- For Bertie's specific Progress Test scope, see the "Summer 2026 Progress Test Information" PDF

The full curriculum mapping is in the original (uncommitted) `revision-game-design.md` — that file isn't in the repo by `.gitignore` design. Ask Richard for it if needed.

## Adding more questions

1. Tell Claude: "Generate 30 questions on `<topic>` for Year 8 `<subject>`, following `QUESTION_SCHEMA.md`"
2. Claude produces JSON
3. Skim-review for howlers
4. Drop into `questions/<subject>/<topic>.json`
5. Add the unit to `questions/<subject>/_index.json` if it's a new unit
6. Commit + push — GitHub Pages auto-redeploys

**Underscore-named files** (like `_index.json`) need `.nojekyll` in the repo root or Jekyll will strip them. The `.nojekyll` file is already in place.

## Known issues / TODO

### Issues
- HMAC secret is in source code (public repo) — currently `change-me-bertie-2026-revision`. Threat model is "one Year 8 kid"; not security-critical, but Richard should still rotate it once.
- Some Geography "topics" are coarse-grained (whole unit treated as one topic). Engine handles it fine but the tree view shows fewer subdivisions for Geography.
- No image-based questions (logic-gate symbols described in words; flowchart shapes as text labels). Would need an image hosting decision to upgrade.

### Not yet built (in priority order)
1. **QR code on end screen** — generate a QR of the code so parent can scan from phone instead of typing. One library import.
2. **Multi-profile picker** — current design assumes one Bertie. To add sibling, easiest is duplicate deploy. To add proper switcher, scope `localStorage` keys by profile id.
3. **Cross-device sync** — would need a backend. Out of scope for this MVP.
4. **Boss-battle timer** — currently no per-question timer in boss mode. Designed for it but not implemented.
5. **Audio prompts** — for MFL listening practice. Not needed for Bertie's four subjects.

### Open questions for Richard
- Is Bertie on the Computing rotation this year? Progress Test card said it's opt-in. Currently in scope; remove if not.
- Has he rotated the HMAC secret yet?
- Has Bertie actually tried it? What's the feedback on session length / canvas usability / working-check vibe?

## Common operations

**Run locally:** `cd ks3-test && python3 -m http.server 8000` → http://localhost:8000/

**Deploy:** push to `main` on GitHub. Pages auto-rebuilds. Live in ~30s.

**Add new questions for a topic:** drop JSON file in `questions/<subject>/`, add to `_index.json`, push.

**Add new subject:**
1. New folder `questions/<newsubject>/` with `_index.json` and topic files
2. Add to `SUBJECTS` array near top of `index.html` (~line 95) — pick icon + colour
3. Add a `.subject-card.<newsubject>` CSS rule with a gradient
4. Push

**Change HMAC secret:** update `HMAC_SECRET` constant in both `index.html` and `parent.html`. Already-issued codes will stop verifying; wipe Bertie's localStorage if you want a clean slate.

**Tune treat thresholds:** open `parent.html` → "Treat thresholds and rewards" → edit and Save. Settings persist in parent's localStorage.

## Brand-style cues (if Richard adds branding later)

His domain is `risksmart.com` (he's VP of Product there). If he wants to brand this for RiskSmart kids, use the `rs:brand-guidelines` skill to pull official colours/typography. Not done yet — current style is generic warm/cream palette.
