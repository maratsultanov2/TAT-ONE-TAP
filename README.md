# TAT-ONE-TAP

[![English](https://img.shields.io/badge/English-blue)](README.md)
[![Русский](https://img.shields.io/badge/Русский-green)](README.ru.md)
[![中文](https://img.shields.io/badge/中文-red)](README.zh.md)

**One‑tap memory for LLM** — ecosystem of modules for memory management, structural analysis, and protection in agentic systems.

## 🧩 Modules

| Module | Purpose | Location |
|--------|---------|----------|
| **TAT-D (Defense)** | Structural anomaly detection without training, 0 MB RAM, runs on CPU | [`tat_defense/`](tat_defense/) |
| **TAT-Monitor** | Revert detection in dialogues (role → anchor → old value). F1 0.926, AUROC 0.986 | [`tat_monitor/`](tat_monitor/) |
| **TAT-Diff** | Compute difference between memory states | [`tat_diff.py`](tat_diff.py) |
| **TAT-Secretary** | Browser extension, DeepSeek integration | [`extensions/tat-secretary/`](extensions/tat-secretary/) |
| **TAT-Snippets** | Ready‑to‑use Colab snippets | [`TAT_SNIPPETS.ipynb`](TAT_SNIPPETS.ipynb) |
| **TAT-ONE-TAP Core** | Core memory management for LLM | [`core/`](core/) (in development) |

## 📖 Documentation

- [TAT-D](tat_defense/README.md) – EN / RU / ZH
- [TAT-Monitor](tat_monitor/README.md) – monitoring documentation

## 🔒 License

**Proprietary** – commercial use only under license. See [LICENSE](LICENSE) for details.

---

© 2026 Marat Sultanov


## Installation

You can install TAT-ONE-TAP as a package:
```bash
pip install git+https://github.com/maratsultanov2/TAT-ONE-TAP.git
```
For development:
```bash
git clone https://github.com/maratsultanov2/TAT-ONE-TAP.git
cd TAT-ONE-TAP
pip install -e .
```

## Quick Start

```python
from tat import TAT

# For structural anomaly detection
tat_defense = TAT(mode='defense')
anomalies = tat_defense.detect_anomaly(data, window=10, block_sizes=[6,7,7])

# For revert detection in dialogues
tat_monitor = TAT(mode='monitor')
result = tat_monitor.detect_anomaly(context, candidate)
```

## Contact & Support

For commercial licensing, support, or partnership inquiries:
- Email: marat.sultanov@example.com
- Telegram: @maratsultanov2
- GitHub Issues: [create an issue](https://github.com/maratsultanov2/TAT-ONE-TAP/issues)

We aim to respond to commercial inquiries within 24 hours.
