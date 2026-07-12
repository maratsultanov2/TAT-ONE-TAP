# TAT‑Monitor — 通用结构异常检测器

[![TAT](https://img.shields.io/badge/TAT-Experimental-blue)](https://github.com/maratsultanov2/TAT-ONE-TAP)
[![Dataset by Rastislav](https://img.shields.io/badge/Dataset-Rastislav_Drahos-green)](https://github.com/DanceNitra/agora)
[![License: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue)](../../LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--ND%204.0-lightgrey)](../../LICENSE-DATA)
[![Status: Peer‑Reviewed](https://img.shields.io/badge/Status-Peer--Reviewed-brightgreen)](https://github.com/DanceNitra/agora)

## 作者
- **Marat Sultanov** — TAT 架构，直接上下文比较方法，TAT‑Monitor 模块。
- **Rastislav Drahos (DanceNitra)** — 固定装置设计，provenance 分解，压力测试构建，独立复现。

## 结果
- v1, v2, v3: F1 = 1.0
- v4nat (heldout): F1 = 0.905
- v4 (2行上下文，自适应): F1 = 0.923
- 压力测试 (真实数据): F1 = 0.722 → 0.895 (带 provenance)

## 许可证
- **代码**: AGPL‑3.0 — 见 [LICENSE-CODE](../../LICENSE-CODE)
- **数据和模型**: CC BY‑NC‑ND 4.0 — 见 [LICENSE-DATA](../../LICENSE-DATA)

© Marat Sultanov, 2026. 保留所有权利。

*发布日期: 2026-07-12 11:32*