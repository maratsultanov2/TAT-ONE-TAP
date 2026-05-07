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
