# TAT-ONE-TAP

## Управление памятью для LLM

TAT-ONE-TAP — модульная система памяти для LLM (DeepSeek, GPT, Claude).

## Модули

| Модуль | Описание |
|---|---|
| **TAT-BRAIN** | Слепок личности/контекста (≤50 КБ) |
| **TAT-INDEX** | Индекс всех диалогов с поиском |
| **TAT-DIFF** | Дельта состояний (экономия 99.99% токенов) |
| **TAT-PRIORITY** | Управление памятью по важности |
| **TAT-ACHIEVEMENTS** | История достижений и прогресса |

## Установка

```bash
git clone https://github.com/maratsultanov2/TAT-ONE-TAP.git
cd TAT-ONE-TAP
pip install -r requirements.txt
```

## Быстрый старт

```python
from src.tat_memory import TATMemory

memory = TATMemory()
memory.save_session({'id': 'session_1', 'topics': 'TAT'})
brain = memory.restore()
print(brain)
```

## Лицензия

- Код: AGPL-3.0
- Данные: CC BY-NC-ND 4.0

## Автор

Марат Султанов
