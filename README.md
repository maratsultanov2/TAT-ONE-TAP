# TAT-ONE-TAP

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maratsultanov2/TAT-ONE-TAP/blob/main/demo.ipynb)



[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maratsultanov2/TAT-ONE-TAP/blob/main/demo.ipynb)



## Memory Management for LLMs

TAT-ONE-TAP is a modular memory system for LLMs (DeepSeek, GPT, Claude).

## Modules

| Module | Description |
|---|---|
| **TAT-BRAIN** | Persona/context snapshot (≤50 KB) |
| **TAT-INDEX** | Searchable index of all dialogues |
| **TAT-DIFF** | State delta (99.99% token savings) |
| **TAT-PRIORITY** | Importance-based memory management |
| **TAT-ACHIEVEMENTS** | History of progress and milestones |

## Installation

```bash
git clone https://github.com/maratsultanov2/TAT-ONE-TAP.git
cd TAT-ONE-TAP
pip install -r requirements.txt
```

## Quick Start

```python
from src.tat_memory import TATMemory

memory = TATMemory()
memory.save_session({'id': 'session_1', 'topics': 'TAT'})
brain = memory.restore()
print(brain)
```

## License

- Code: AGPL-3.0
- Data: CC BY-NC-ND 4.0

## Author

Marat Sultanov


## Validation

TAT-ONE-TAP is built on the same coherence architecture validated on real-world data. See [docs/VALIDATION.md](docs/VALIDATION.md) for details.

> *"The θ=1.987 threshold mapped to Coherence head divergence — the design principle held on real data, not just synthetic."*
> — qingkong66, DeepSeek-V3 #1285
