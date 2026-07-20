# TAT 架构总览

## 模块化系统
TAT 采用层次化模块系统（位于 `/content/drive/MyDrive/TAT_Modular_System`）。

### 层次
| 目录 | 用途 | 关键模块 |
|------|------|----------|
| `00_core/` | 核心数学内核 | `tat_core.py`（散度、和谐、复空间）、`tat_complex.py` |
| `01_basic/` | 基础扩展 | `tat_anchors.py`（自适应锚点、镜像增强）、`tat_mirror.py`、`tat_noise.py` |
| `02_diagnostics/` | 结构诊断 | `tat_defense.py`（异常检测）、`tat_monitor.py`（对话回滚检测）、`tat_diff.py`（增量记忆） |
| `03_multi_agent/` | 多智能体架构 | `tat_modular.py`（DNA/RNA/Protein）、`tat_triumvirate.py`、`tat_fractal.py`、`tat7.py`（完整 TAT‑7） |
| `04_integrations/` | 外部集成 | CERN、DMRG、Agent 流水线 |
| `05_private/` | 专有模块 | 限制访问 |

## 仓库
| 仓库 | 用途 |
|------|------|
| [TAT-ROOT](https://github.com/maratsultanov2/TAT-ROOT) | 文档、术语表、校准 |
| [TAT-ONE-TAP](https://github.com/maratsultanov2/TAT-ONE-TAP) | 核心模块：Defence、Monitor、Diff |
| [TAT-DEMO](https://github.com/maratsultanov2/TAT-DEMO) | 可视化、Colab 笔记本 |
| [TAT7-logistics](https://github.com/maratsultanov2/TAT7-logistics) | 仓库工业原型 |