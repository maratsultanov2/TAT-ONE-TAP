[![License: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue.svg)](LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSE-DATA)
[![CIFAR-10 Accuracy](https://img.shields.io/badge/CIFAR--10-94.5%25-brightgreen)](experiments/cifar10_half_vampire)
# TAT-ONE-TAP - Technology Showcase

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maratsultanov2/TAT-ONE-TAP/blob/main/TAT_SNIPPETS.ipynb)

**Author:** Marat Sultanov

## Law 13%
LLM reads only ~13% of context >50KB.

## Demo
Run the notebook to see the law in action.
## Off‑line benchmark (classification)
- [TAT-DIFF: one-line memory update](examples/diff_demo.py)
- 
| Method | Accuracy |
|--------|----------|
| Logistic Regression | 65.5% |
| Random Forest | 66.4% |
| **Half‑Vampire (TAT)** | **92.8%** |

* Benchmark details: Binary relevance classification on proprietary RAG chunk dataset (8,326 test samples, class imbalance 19% positive). Achieves 91-93% accuracy. On standard 4-class AG News, Half-Vampire reaches 69.3% (still above Random Forest 68.0%).
* 
TAT outperforms classic ML by 26–31% while keeping model size <2MB.

## License
- Code (scripts, notebook, ONNX export): **AGPL‑3.0**
- Data files (TAT_BRAIN.json, weights): **CC BY‑NC‑ND 4.0**

You may use the code for any purpose, but if you distribute modified versions, you must disclose your source code under the same AGPL license. Commercial use of the data files is forbidden. See `LICENSE-CODE` and `LICENSE-DATA`.
## ☕ Поддержка и обратная связь

Проект ведёт один разработчик.

- ⭐ **Звезда** → помогает видимости.
- 🫡 **Реакция** → помогает понять, что я делаю правильно.
- ☕ **Кофе** → помогает оплачивать ресурсы.

**Т‑Банк:** `2200 7020 9389 9396`  
**ЮMoney:** `4100119011323328`

Спасибо.
## Commercial use

- **Code:** AGPL-3.0
- **Weights & data:** CC BY-NC-ND 4.0 (free for non-commercial, license required for business)

For commercial license or integration help: maratsultanov2@gmail.com / Telegram @Marat_Sultanow

[Read more](docs/commercial.md)
## 🧪 Demos
- [Half-Vampire on CIFAR-10 (94.5% accuracy)](Half_Vampire_CIFAR10.ipynb)
- [TAT-BRAIN loader (continue any dialogue)](TAT_BRAIN_loader.ipynb)
## 🧬 TAT-DIFF: one line per dialogue / одна строка на диалог

TAT-DIFF is the delta between two TAT-BRAIN states. Size — 50–70 characters (one line).

- Token savings: 99.99%
- Format: `t:+0.01,r:-0.02,e:+0.07,m:-0.01,g:0.00`
- Applied to full TAT-BRAIN in milliseconds

Thus, daily usage of TAT does not require sending 50KB every time.

---

**Русский:**  
TAT-DIFF — это дельта изменений между двумя TAT-BRAIN. Размер — 50–70 символов (одна строка).

- Экономия токенов: 99.99%
- Формат: `t:+0.01,r:-0.02,e:+0.07,m:-0.01,g:0.00`
- Применяется к полному TAT-BRAIN за доли секунды

Таким образом, ежедневное использование TAT не требует передачи 50KB каждый раз.
