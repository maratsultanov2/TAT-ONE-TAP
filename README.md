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
