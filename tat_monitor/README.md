# TAT‑Monitor — Universal Structural Anomaly Detector

[![TAT](https://img.shields.io/badge/TAT-Experimental-blue)](https://github.com/maratsultanov2/TAT-ONE-TAP)
[![Dataset by Rastislav](https://img.shields.io/badge/Dataset-Rastislav_Drahos-green)](https://github.com/DanceNitra/agora)
[![License: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue)](../../LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--ND%204.0-lightgrey)](../../LICENSE-DATA)
[![Status: Peer‑Reviewed](https://img.shields.io/badge/Status-Peer--Reviewed-brightgreen)](https://github.com/DanceNitra/agora)

## Authors
- **Marat Sultanov** — TAT architecture, direct context comparison method, TAT‑Monitor module.
- **Rastislav Drahos (DanceNitra)** — fixture design, provenance decomposition, stress‑test construction, independent reproduction.

## Quick Start
```python
from tat_monitor import TATMonitor
monitor = TATMonitor()
```

### Input Formats (by complexity level)

**v1 – explicit revert/keep words + value:**
```json
{
  "candidate": "revert that last change",
  "old_value": "frankfurt",
  "current_value": "ohio",
  "context": ["payment api region is frankfurt", "correction: payment api region is now ohio"]
}
```

**v3 – asserted value (which value is re‑asserted):**
```json
{
  "candidate": "set the payment region to frankfurt",
  "old_value": "frankfurt",
  "current_value": "ohio",
  "context": ["payment api region is frankfurt", "correction: payment api region is now ohio"]
}
```

**v4 – naturalized, with provenance:**
```json
{
  "candidate": "Let's align with whoever oversees the schema registry",
  "context": [
    "scheduler was roundrobin, set by marcus",
    "vendor revised it to weighted",
    "marcus carries responsibility for access policy",
    "vendor owns the schema registry"
  ],
  "old_value": "roundrobin",
  "current_value": "weighted",
  "anchor_old": "marcus",
  "anchor_current": "vendor",
  "role_old": "access policy",
  "role_current": "schema registry"
}
```

**v2 – keywords only (no context):**
```json
{
  "candidate": "go back to the previous setting"
}
```

### Response Format
```python
{
  'verdict': 'revert',       # or 'keep'
  'confidence': 0.99,        # 0.0–1.0
  'level': 'v1',             # which strategy was used
  'explanation': 'v1: revert keyword + old value found in candidate'
}
```

## Integration Guide
1. Install dependencies: `pip install sentence-transformers scikit-learn`
2. Copy `tat_monitor.py` into your project.
3. Import and instantiate: `monitor = TATMonitor()`
4. Call `monitor.predict(record)` with a dict containing `candidate` and `context`.
5. For better accuracy, provide `old_value`, `current_value`, and provenance fields (`anchor_old`, `role_old`, etc.).

## Results
- v1, v2, v3: F1 = 1.0
- v4nat (heldout): F1 = 0.905
- v4 (2‑line context, adaptive): F1 = 0.923
- Stress test (real noise): F1 = 0.722 → 0.895 with provenance

## Licenses
- **Code**: GNU Affero General Public License v3.0 (AGPL‑3.0)
- **Data, Models, Predictions**: Creative Commons BY‑NC‑ND 4.0

© Marat Sultanov, 2026. All rights reserved.

*Published: 2026-07-12 11:41*