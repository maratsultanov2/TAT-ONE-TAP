# ============================================================
# TAT-BRAIN v3.2 - Обучение весов на ваших диалогах
# ============================================================
# Запуск: python train_tat_brain.py --path /path/to/dialogs

import json
import glob
import argparse
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def train_tat_brain(data_path, output_path):
    print("🔄 Загрузка эмбеддера...")
    donor = SentenceTransformer('all-MiniLM-L6-v2')
    
    targets = {
        "theme": "обсуждение архитектуры TAT-7, памяти для LLM, когерентности",
        "role": "Marat предлагает идеи, помощник помогает с кодом",
        "emotion": "ирония, усталость, раздражение от повторов",
        "meaning": "сохранить контекст, чтобы не начинать с нуля",
        "goal": "создать портативный формат памяти"
    }
    target_embs = {k: donor.encode(v) for k, v in targets.items()}
    
    files = glob.glob(f"{data_path}/**/*.txt", recursive=True) + \
            glob.glob(f"{data_path}/**/*.json", recursive=True)
    print(f"📂 Найдено файлов: {len(files)}")
    
    layer_scores = {k: [] for k in targets}
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            if len(text) < 100:
                continue
            text_emb = donor.encode(text[:3000])
            for layer, target_emb in target_embs.items():
                sim = cosine_similarity([text_emb], [target_emb])[0][0]
                layer_scores[layer].append(float(sim))
        except:
            continue
    
    avg_scores = {k: np.mean(v) for k, v in layer_scores.items()}
    weights = {k: 0.2 for k in targets}
    for k in weights:
        delta = (avg_scores[k] - 0.5) * 0.2
        weights[k] = max(0.05, min(0.95, weights[k] + delta))
    total = sum(weights.values())
    weights = {k: v/total for k, v in weights.items()}
    
    output = {
        "version": "3.2",
        "method": "TAT-7 layer detector",
        "files_analyzed": len(files),
        "avg_scores": avg_scores,
        "weights": weights,
        "targets": targets
    }
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"✅ Сохранён: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Путь к папке с диалогами")
    parser.add_argument("--output", default="TAT_BRAIN_v3.2.json", help="Файл для сохранения")
    args = parser.parse_args()
    train_tat_brain(args.path, args.output)
