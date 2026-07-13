# TAT-ONE-TAP

[![English](https://img.shields.io/badge/English-blue)](README.md)
[![Русский](https://img.shields.io/badge/Русский-green)](README.ru.md)
[![中文](https://img.shields.io/badge/中文-red)](README.zh.md)

**One‑tap memory for LLM** — экосистема модулей для управления памятью, структурного анализа и защиты в агентных системах.

## 🧩 Модули

| Модуль | Назначение | Расположение |
|--------|------------|--------------|
| **TAT-D (Defense)** | Обнаружение структурных аномалий без обучения, 0 МБ RAM, работает на CPU | [`tat_defense/`](tat_defense/) |
| **TAT-Monitor** | Детекция ревертов в диалогах (роль → якорь → старое значение). F1 0.926, AUROC 0.986 | [`tat_monitor/`](tat_monitor/) |
| **TAT-Diff** | Вычисление разницы между состояниями памяти | [`tat_diff.py`](tat_diff.py) |
| **TAT-Secretary** | Расширение для браузера, интеграция с DeepSeek | [`extensions/tat-secretary/`](extensions/tat-secretary/) |
| **TAT-Snippets** | Готовые сниппеты для Colab | [`TAT_SNIPPETS.ipynb`](TAT_SNIPPETS.ipynb) |
| **TAT-ONE-TAP Core** | Ядро управления памятью для LLM | [`core/`](core/) (в разработке) |

## 📖 Документация

- [TAT-D](tat_defense/README.md) – EN / RU / ZH
- [TAT-Monitor](tat_monitor/README.md) – документация по мониторингу

## 🔒 Лицензия

**Проприетарная** – коммерческое использование только по лицензии. Подробнее в [LICENSE](LICENSE).

---

© 2026 Marat Sultanov
