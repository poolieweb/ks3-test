# Bertie's Revision Game

A Sparx-style adaptive revision game built for Year 8 end-of-year Progress Tests at Chorlton High School. Targets four subjects (Science, History, Geography, Computing) with ~530 hand-vetted, Knowledge-Map-aligned questions.

## Run it locally

The app uses `fetch()` to load question banks, so opening `index.html` directly from disk (`file://`) won't work in most browsers. Serve it via a simple HTTP server:

```bash
cd revision-game
python3 -m http.server 8000
# then visit http://localhost:8000/
```

For the parent verifier: open `http://localhost:8000/parent.html`.

## Host it for real

Drop the whole `revision-game/` folder onto:

- **Netlify** (drag-and-drop on [app.netlify.com/drop](https://app.netlify.com/drop)) — gives you a URL like `bertie-revision.netlify.app` in 30 seconds
- **GitHub Pages** — push to a repo, enable Pages on the `main` branch
- **Cloudflare Pages** — same drill, free
- **Any static host you have** (S3, your own server, etc.)

Nothing server-side is needed. Question banks are static JSON.

## File layout

```
revision-game/
├── index.html              # The game Bertie plays
├── parent.html             # The verifier you use
├── profile.json            # Bertie's name, mascot, theme, personal context
├── QUESTION_SCHEMA.md      # Spec for the JSON question format
├── README.md               # This file
└── questions/
    ├── science/
    │   ├── _index.json
    │   ├── organisms.json              (41 questions)
    │   ├── acids-alkalis.json          (44)
    │   ├── waves-light-sound.json      (38)
    │   ├── rocks-climate-universe.json (39)
    │   └── separating-techniques.json  (15)
    ├── history/
    │   ├── _index.json
    │   ├── stuart-era.json             (25)
    │   ├── slave-trade.json            (25)
    │   ├── industrial-revolution.json  (35)
    │   └── british-empire.json         (35)
    ├── geography/
    │   ├── _index.json
    │   ├── ten-billion-people.json     (71)
    │   └── asia-transformed.json       (71)
    └── computing/
        ├── _index.json
        ├── networks-hardware.json      (25)
        ├── binary-data.json            (25)
        ├── cyber-security.json         (15)
        └── computational-thinking.json (25)
```

**529 questions total.**

## The reward / code system

When Bertie finishes a session, the app generates one of four codes:

| Code | When | Real-world meaning |
|---|---|---|
| `SM-...` | Solid session (≥12 min, ≥65% accuracy, ≥1 working check) | Evening treat |
| `BIG-...` | Strong session (≥25 min, ≥80% accuracy, ≥2 working checks, ≥2 skills levelled) | Full-day treat |
| `WIN-...` | 7-day streak of small-or-better | £5 extra pocket money |
| `RP-...` | Session happened but didn't hit the bar | No treat, but visible report |

Bertie sees the code on screen, copies it, sends/reads it to you. You paste it into `parent.html`:

- The verifier checks the HMAC signature so Bertie can't forge or replay codes
- It decodes session stats (minutes, questions, accuracy, skills levelled, working checks)
- It applies the thresholds you configure (under "Treat thresholds and rewards" on the verifier page)
- A **two-smalls-in-a-weekend** accumulator unlocks the Big treat too, by default

All thresholds are tunable from the verifier UI. Settings are saved in the verifier's localStorage.

## Change the HMAC secret (IMPORTANT before sharing)

Both `index.html` and `parent.html` ship with:

```js
HMAC_SECRET: "change-me-bertie-2026-revision"
```

Before letting anyone else use this, change that string in **both files** to something only you know. If you change the secret after Bertie has earned codes, those old codes will stop verifying (which is fine — wipe his localStorage if you want a clean slate).

## Adding new questions

Drop new files into `questions/<subject>/` and add them to that subject's `_index.json`. The engine picks them up next session. Because mastery scores attach to `skill_tags` (not topics), Bertie's existing scores are preserved — new questions just introduce new skills at the default 50/100 mastery.

### Generating new questions with Claude

The pipeline:

1. Open Cowork. Tell Claude: "Generate 30 questions on `<topic>` for Year 8 `<subject>`, following the schema in `revision-game/QUESTION_SCHEMA.md`. Source: `<knowledge map reference or upload>`."
2. Claude produces a JSON file matching the schema.
3. Skim-review (look for any factual howlers, weird phrasings, broken `accepted` arrays).
4. Drop the file into `questions/<subject>/<topic>.json`.
5. Add the unit to `_index.json` if it's new.
6. Re-deploy (or just reload locally).

### Editing existing questions

Edit the JSON. **Bump `version` if you change the answer or scoring logic** — Bertie's old correct attempts stay valid against the previous version.

## Adding a new subject

1. Make `questions/<newsubject>/_index.json` with the same shape as the existing ones.
2. Add one or more topic files.
3. Add the subject to the `SUBJECTS` array near the top of `index.html` (about 10 lines down) — pick a colour and icon.
4. Add a matching CSS class block for `.subject-card.<newsubject>`.

## Adding another child

Two approaches:
- **Same device, different profile:** save the current `profile.json` and `localStorage` somewhere (use the "Export progress" button), edit `profile.json` for the new child, clear localStorage. Repeat to switch back.
- **Separate hosted instance:** deploy the folder twice with different `profile.json` files (e.g. `bertie.netlify.app` and `<sibling>.netlify.app`). Each child gets their own URL and own localStorage.

A built-in profile switcher is straightforward to add later but not in this MVP.

## State storage and exports

All progress is in browser `localStorage` under the key `revisionGameState`. The "Export progress" button on the home page downloads it as JSON — keep a copy somewhere if you're worried about browser data loss.

Codes themselves carry all session info, so even if state is wiped, the parent verifier's history reflects every code you've ever verified.

## Boss Battle mode ⚔️

Each subject card has a **⚔️ Boss** button. A boss battle is:
- 10 questions drawn diverse across all units in the subject (no repeats from recent normal sessions)
- **No hints, no retries** — one shot per question
- Higher-difficulty questions weighted in
- Pass = 70%+ accuracy → earns a `BOSS-...` code that counts as a Big-tier treat + 100 bonus XP
- Fail = `RP` code, no treat

Eligibility:
- Subject must be ≥30% mastered (so Bertie's practised something first)
- One boss battle per subject per day

The parent verifier recognises BOSS codes and applies the Big-tier reward automatically. The Boss Slayer achievement triggers on the first win.

## Mastery tree 🌳

Three-level hierarchy: **Subject → Unit → Topic → Skill**. Each node shows:
- Aggregated mastery score (avg of underlying skills)
- Total attempts across that branch
- Coloured progress bar

Click any node to expand. On the skill leaves, a **Practise** button starts a focused session restricted to just that skill — useful for drilling weak spots flagged at the bottom of the tree (skills are sorted weakest-first within each topic).

## Achievements 🏆

14 achievements covering streaks, question counts, mastery milestones, boss wins, working-check streaks, and variety. Triggered automatically at session end with a toast popup. View progress from the home page.

## Session-history viewer 📜

Home → 📜 History shows the last 50 sessions: tier badge, subject, date/time, length, accuracy, and code prefix. Useful for spotting patterns ("Bertie always tanks on Wednesday evenings") and for cross-checking codes against the parent verifier ledger.

## What's NOT in this MVP (easy to add later)

- QR-code generation for codes (one library swap and it's there)
- Multiple profiles in one app
- Cross-device sync (would need a backend)
- Audio prompts for MFL listening
- Image-based questions (would need an image hosting story)

## Adaptive engine notes

The mastery model is a lightweight Elo. Each skill tag has a score 0–100. Per answer:

- Expected probability of correct = sigmoid of (mastery − difficulty target) / 15
- Score moves by `k * (actual − expected)`, where `k = 6` by default
- Hint-assisted correct counts as 0.7 (not full 1.0)
- Two wrongs in a row drops to easier questions next session

Spaced review schedules mastered skills (≥90) for re-test at 3 → 7 → 21 → 60 days. Session composer mixes current-focus questions with "needs strengthening" and "due for review", weighted so Bertie sees variety.

## Curriculum sources

Every question has a `source` field. Most reference the Chorlton High Year 8 Knowledge Map for the relevant unit; where the Knowledge Map was thin, content was augmented from the UK National Curriculum KS3 (tagged `UK NC KS3` in the source field). This is documented per-subject in the question-gen reports — ask Claude if you want a summary.

## Troubleshooting

**Code "doesn't verify" but looks right** — confirm the HMAC secret in `parent.html` matches the one in `index.html`.

**"No questions available"** — `_index.json` for that subject points to topic files that didn't load. Open the browser console (F12) to see what failed.

**Canvas doesn't draw** — make sure you're using a recent browser. Pointer events are required.

**Mastery scores feel off** — give it 3–4 sessions to settle. The default `k=6` is conservative; bump it in `index.html` (`ELO_K_FACTOR`) if you want it to react faster.

---

Built for Bertie · May 2026 · Target: Summer Progress Test 16–26 June 2026
