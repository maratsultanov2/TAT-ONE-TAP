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

TAT outperforms classic ML by 26–31% while keeping model size <2MB.

## License
- Code (scripts, notebook, ONNX export): **AGPL‑3.0**
- Data files (TAT_BRAIN.json, weights): **CC BY‑NC‑ND 4.0**

You may use the code for any purpose, but if you distribute modified versions, you must disclose your source code under the same AGPL license. Commercial use of the data files is forbidden. See `LICENSE-CODE` and `LICENSE-DATA`.
