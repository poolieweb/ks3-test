# Question Schema — v1

All question files use this schema. Files live at `/questions/<subject>/<topic-slug>.json` and contain a JSON array of question objects.

## Question object

```json
{
  "id": "sci.org.dig.001",
  "subject": "science",
  "unit": "organisms",
  "topic": "digestion",
  "skill_tags": ["digestion", "enzymes"],
  "tier": "introduce",
  "difficulty": 2,
  "type": "mcq",
  "prompt": "Which enzyme breaks down proteins in the stomach?",
  "options": ["Amylase", "Pepsin", "Lipase", "Maltase"],
  "answer": "Pepsin",
  "accepted": null,
  "hint": "Stomach acid + enzyme — name starts with P",
  "explanation": "Pepsin is the protein-digesting enzyme produced in the stomach. It works best in the acidic environment.",
  "working_required": false,
  "estimated_seconds": 30,
  "source": "CHS Y8 Science KM, Unit 1 Organisms",
  "version": 1
}
```

## Field reference

| Field | Type | Notes |
|---|---|---|
| `id` | string | Namespaced — `<sub3>.<unit3>.<topic3>.<NNN>`. Must be globally unique. |
| `subject` | string | `science`, `history`, `geography`, `computing` |
| `unit` | string | Slug, e.g. `organisms`, `acids-alkalis`, `british-empire` |
| `topic` | string | Slug — finer-grained, e.g. `digestion`, `respiratory` |
| `skill_tags` | array<string> | 1–3 skill tags that mastery attaches to. Reuse tags across questions! |
| `tier` | enum | `introduce` (entry-level), `strengthen` (consolidation), `deepen` (extension) |
| `difficulty` | int 1–5 | 1 = very easy recall, 5 = applied / extended thinking |
| `type` | enum | See "Question types" below |
| `prompt` | string | The question. Plain text. Use \n for line breaks. |
| `options` | array<string> | For `mcq`, `multi-select`, `order`. Else null. |
| `answer` | string \| array | For `mcq`/`numeric`/`text`: string. For `multi-select`/`order`: array. |
| `accepted` | array<string> \| null | Alt acceptable forms for `text`/`numeric`. e.g. ["1/2", "0.5", "½"] |
| `hint` | string | One-line hint. Used after a wrong attempt. |
| `explanation` | string | 1–3 sentence explanation shown after answering. |
| `working_required` | bool | If true, this question triggers a bookwork-style check |
| `estimated_seconds` | int | Realistic time for a Y8 to answer |
| `source` | string | Curriculum source — Knowledge Map unit or "UK NC KS3" |
| `version` | int | Bump if you edit. Old answers stay valid against old version. |
| `further_learning` | array<{title,url}> \| null | Links shown after answering. Each entry: `{"title": "...", "url": "..."}`. Use Oak National Academy unit pages as primary, BBC Bitesize KS3 subject pages as secondary. Populated automatically by `add_further_learning.py` from `skill_tags`. |

## Question types

### `mcq` — single-correct multiple choice
- `options`: 3–5 distractors
- `answer`: string matching one of `options` exactly

### `multi-select` — multiple correct
- `options`: 4–6 options
- `answer`: array of correct option strings

### `numeric` — number answer
- `options`: null
- `answer`: string representation of number
- `accepted`: optional array of equivalent forms (e.g. `["0.5", "1/2", "50%"]`)

### `text` — short text answer
- `options`: null
- `answer`: canonical spelling
- `accepted`: optional array of alternatives (UK/US spelling, abbrevs, capitalisation variants)

### `order` — drag to put in order
- `options`: items in scrambled (display) order
- `answer`: array of items in correct order

## Tier and difficulty guidance

- **Tier `introduce`** — first exposure to the skill. Difficulty 1–2. Lots of mcq, basic recall.
- **Tier `strengthen`** — practising and consolidating. Difficulty 2–4. Mix types, mild application.
- **Tier `deepen`** — extension and synthesis. Difficulty 3–5. Multi-step, multi-concept, applied.

Aim for a roughly 4 : 4 : 2 ratio (introduce : strengthen : deepen) per topic.

## Skill tags — reuse them!

Mastery scores attach to **skill_tags**, not topics. So if "photosynthesis" appears in both biology and chemistry units, use the same `photosynthesis` tag in both. The mastery engine will treat them as the same skill.

Good tag names:
- `digestion`, `enzymes`, `respiration`, `gas-exchange`
- `acids`, `alkalis`, `pH`, `neutralisation`, `reactivity-series`, `salts`
- `waves`, `reflection`, `refraction`, `sound`, `electromagnetic-spectrum`
- `rock-cycle`, `solar-system`, `gravity`
- `population`, `migration`, `urbanisation`, `development`
- `monsoon`, `biomes`, `karnataka`
- `industrial-revolution`, `british-empire`, `slave-trade`, `cottonopolis`
- `networks`, `binary`, `cyber-security`, `algorithms`, `abstraction`

Bad tag names: ones that are too narrow (`digestion-stomach-pepsin`) or too broad (`science`).

## File structure

Each topic file:
```json
{
  "subject": "science",
  "unit": "organisms",
  "topic": "digestion",
  "questions": [
    { ...question 1... },
    { ...question 2... }
  ]
}
```

Index files at `/questions/<subject>/_index.json`:
```json
{
  "subject": "science",
  "units": [
    {
      "slug": "organisms",
      "name": "Organisms",
      "topics": ["digestion", "respiration", "exercise"]
    }
  ]
}
```
