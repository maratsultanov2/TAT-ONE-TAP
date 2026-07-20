# TAT Architecture Overview

## Modular System
TAT is organized as a hierarchical modular system (located at `/content/drive/MyDrive/TAT_Modular_System`).

### Layers
| Directory | Purpose | Key Modules |
|-----------|---------|-------------|
| `00_core/` | Core mathematical kernel | `tat_core.py` (divergence, harmony, complex space), `tat_complex.py` |
| `01_basic/` | Basic extensions | `tat_anchors.py` (adaptive anchors, mirror augmentation), `tat_mirror.py`, `tat_noise.py` |
| `02_diagnostics/` | Structural diagnostics | `tat_defense.py` (anomaly detection), `tat_monitor.py` (revert detection), `tat_diff.py` (delta memory) |
| `03_multi_agent/` | Multi-agent architectures | `tat_modular.py` (DNA/RNA/Protein), `tat_triumvirate.py`, `tat_fractal.py`, `tat7.py` (full TAT‑7) |
| `04_integrations/` | External integrations | CERN, DMRG, agent pipelines |
| `05_private/` | Proprietary modules | Restricted access |

## Repositories
| Repository | Purpose |
|-------------|------------|
| [TAT-ROOT](https://github.com/maratsultanov2/TAT-ROOT) | Documentation, glossary, calibration |
| [TAT-ONE-TAP](https://github.com/maratsultanov2/TAT-ONE-TAP) | Core modules: Defence, Monitor, Diff |
| [TAT-DEMO](https://github.com/maratsultanov2/TAT-DEMO) | Visualization, Colab notebooks |
| [TAT7-logistics](https://github.com/maratsultanov2/TAT7-logistics) | Industrial warehouse prototype |