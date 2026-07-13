# TAT-ONE-TAP

[![English](https://img.shields.io/badge/English-blue)](README.md)
[![Русский](https://img.shields.io/badge/Русский-green)](README.ru.md)
[![中文](https://img.shields.io/badge/中文-red)](README.zh.md)

**One‑tap memory for LLM** — 用于代理系统中内存管理、结构分析和保护的模块生态系统。

## 🧩 模块

| 模块 | 用途 | 位置 |
|------|------|------|
| **TAT-D (Defense)** | 无需训练的结构异常检测，0 MB 内存，运行于 CPU | [`tat_defense/`](tat_defense/) |
| **TAT-Monitor** | 对话中的回退检测（角色 → 锚点 → 旧值）。F1 0.926，AUROC 0.986 | [`tat_monitor/`](tat_monitor/) |
| **TAT-Diff** | 计算内存状态之间的差异 | [`tat_diff.py`](tat_diff.py) |
| **TAT-Secretary** | 浏览器扩展，DeepSeek 集成 | [`extensions/tat-secretary/`](extensions/tat-secretary/) |
| **TAT-Snippets** | 即用型 Colab 代码片段 | [`TAT_SNIPPETS.ipynb`](TAT_SNIPPETS.ipynb) |
| **TAT-ONE-TAP Core** | LLM 的核心内存管理 | [`core/`](core/) (开发中) |

## 📖 文档

- [TAT-D](tat_defense/README.md) – EN / RU / ZH
- [TAT-Monitor](tat_monitor/README.md) – 监控文档

## 🔒 许可证

**专有** – 商业使用需获得许可。详见 [LICENSE](LICENSE)。

---

© 2026 Marat Sultanov
