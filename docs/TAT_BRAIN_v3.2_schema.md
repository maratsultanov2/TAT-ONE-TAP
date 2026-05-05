# TAT-BRAIN v3.2 Protocol

## Purpose
Portable memory layer for LLMs.  
Transfers context between sessions **without** cloud storage, fine‑tuning, or API changes.

## Core concepts
- **5 semantic layers:** theme, role, emotion, meaning, goal.
- **Adaptive weights:** each layer gets a weight (0..1). Weights change based on coherence feedback.
- **Plug‑and‑play:** one JSON file (≤50KB) restored in any new dialogue.

## File structure
| Field | Type | Description |
|-------|------|-------------|
| `version` | string | Protocol version (3.2) |
| `weights` | dict | Importance of each layer (sum = 1) |
| `targets` | dict | Short russian phrases used as coherence anchors |
| `avg_scores` | dict | Average coherence scores on training data |
| `instructions` | array | Guidance for the LLM |

## How to use
1. Copy `TAT_BRAIN_v3.2.json` into a new chat.
2. The LLM reads it (≤50KB, fits in context).
3. No extra setup. No API keys. No cloud.

## Integration with TAT-7
- `weights` can be fed into Half‑Vampire classifier (affects head selection).
- `targets` can be replaced with domain‑specific phrases.
- Coherence scores can be updated via user feedback (✅/🚫).

## License
Code: AGPL‑3.0  
Data: CC BY‑NC‑ND 4.0
