# Архитектура TAT

## Модульная система
TAT организован как иерархическая модульная система (расположена в `/content/drive/MyDrive/TAT_Modular_System`).

### Уровни
| Папка | Назначение | Ключевые модули |
|-------|------------|-----------------|
| `00_core/` | Математическое ядро | `tat_core.py` (дивергенция, гармония, комплексное пространство), `tat_complex.py` |
| `01_basic/` | Базовые расширения | `tat_anchors.py` (адаптивные якоря, зеркальное дополнение), `tat_mirror.py`, `tat_noise.py` |
| `02_diagnostics/` | Структурная диагностика | `tat_defense.py` (обнаружение аномалий), `tat_monitor.py` (детекция ревертов), `tat_diff.py` (дельта‑память) |
| `03_multi_agent/` | Многоагентные архитектуры | `tat_modular.py` (DNA/RNA/Protein), `tat_triumvirate.py`, `tat_fractal.py`, `tat7.py` (полный TAT‑7) |
| `04_integrations/` | Внешние интеграции | CERN, DMRG, агентные пайплайны |
| `05_private/` | Приватные модули | Доступ ограничен |

## Репозитории
| Репозиторий | Назначение |
|-------------|------------|
| [TAT-ROOT](https://github.com/maratsultanov2/TAT-ROOT) | Документация, глоссарий, калибровка |
| [TAT-ONE-TAP](https://github.com/maratsultanov2/TAT-ONE-TAP) | Основные модули: Defence, Monitor, Diff |
| [TAT-DEMO](https://github.com/maratsultanov2/TAT-DEMO) | Визуализация, Colab‑ноутбуки |
| [TAT7-logistics](https://github.com/maratsultanov2/TAT7-logistics) | Промышленный прототип для склада |