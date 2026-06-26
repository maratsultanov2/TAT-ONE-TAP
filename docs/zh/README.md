# TAT-ONE-TAP

## LLM 记忆管理

TAT-ONE-TAP 是一个用于 LLM（DeepSeek、GPT、Claude）的模块化记忆系统。

## 模块

| 模块 | 描述 |
|---|---|
| **TAT-BRAIN** | 人格/上下文快照（≤50 KB） |
| **TAT-INDEX** | 可搜索的所有对话索引 |
| **TAT-DIFF** | 状态增量（节省 99.99% token） |
| **TAT-PRIORITY** | 基于重要性的记忆管理 |
| **TAT-ACHIEVEMENTS** | 进度和里程碑历史 |

## 安装

```bash
git clone https://github.com/maratsultanov2/TAT-ONE-TAP.git
cd TAT-ONE-TAP
pip install -r requirements.txt
```

## 快速开始

```python
from src.tat_memory import TATMemory

memory = TATMemory()
memory.save_session({'id': 'session_1', 'topics': 'TAT'})
brain = memory.restore()
print(brain)
```

## 许可证

- 代码: AGPL-3.0
- 数据: CC BY-NC-ND 4.0

## 作者

Marat Sultanov
