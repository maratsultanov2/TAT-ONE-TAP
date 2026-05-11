"""
TAT-DIFF: Differential memory for TAT-BRAIN
Одна строка — один диалог. 5 слоёв, 5 значений.
"""

import json
import hashlib
from typing import Dict, Tuple, Optional

# Структура TAT-BRAIN (5 слоёв)
LAYERS = ["theme", "role", "emotion", "meaning", "goal"]

def weights_to_string(weights: Dict[str, float]) -> str:
    """
    Превращает веса слоёв в строку.
    Пример: {"theme":0.207, "role":0.198, "emotion":0.197, "meaning":0.201, "goal":0.198}
    -> "t:0.21,r:0.20,e:0.20,m:0.20,g:0.20"
    """
    parts = [
        f"{layer[0]}:{weights[layer]:.2f}"
        for layer in LAYERS
    ]
    return ",".join(parts)

def string_to_weights(s: str) -> Dict[str, float]:
    """
    Восстанавливает веса из строки.
    """
    parts = s.split(",")
    weights = {}
    for part in parts:
        if ":" not in part:
            continue
        code, value = part.split(":")
        # код: t, r, e, m, g
        layer_map = {"t": "theme", "r": "role", "e": "emotion", "m": "meaning", "g": "goal"}
        full_name = layer_map.get(code)
        if full_name:
            weights[full_name] = float(value)
    return weights

def compute_diff(prev_weights: Dict[str, float], new_weights: Dict[str, float]) -> str:
    """
    Вычисляет дельту между двумя состояниями.
    Возвращает строку вида "t:+0.01,r:-0.02,e:0.00,m:0.00,g:+0.01"
    """
    diff_parts = []
    for layer in LAYERS:
        old = prev_weights.get(layer, 0.0)
        new = new_weights.get(layer, 0.0)
        delta = new - old
        sign = "+" if delta > 0 else ""
        diff_parts.append(f"{layer[0]}:{sign}{delta:.2f}")
    return ",".join(diff_parts)

def apply_diff(base_weights: Dict[str, float], diff_str: str) -> Dict[str, float]:
    """
    Применяет дельту к базовым весам.
    Возвращает новые веса.
    """
    result = base_weights.copy()
    parts = diff_str.split(",")
    for part in parts:
        if ":" not in part:
            continue
        code, delta_str = part.split(":")
        layer_map = {"t": "theme", "r": "role", "e": "emotion", "m": "meaning", "g": "goal"}
        full_name = layer_map.get(code)
        if full_name and full_name in result:
            delta = float(delta_str)
            result[full_name] += delta
            # Ограничиваем диапазон [0.0, 1.0]
            result[full_name] = max(0.0, min(1.0, result[full_name]))
    return result

def hash_weights(weights: Dict[str, float]) -> str:
    """
    Хеш весов для верификации целостности.
    """
    s = weights_to_string(weights)
    return hashlib.sha256(s.encode()).hexdigest()[:8]

# ======================= ДЕМОНСТРАЦИЯ =======================

if __name__ == "__main__":
    # Пример: полный TAT-BRAIN (утро)
    morning = {
        "theme": 0.207,
        "role": 0.198,
        "emotion": 0.197,
        "meaning": 0.201,
        "goal": 0.198
    }
    
    # Пример: состояние после диалога (вечер)
    evening = {
        "theme": 0.220,
        "role": 0.190,
        "emotion": 0.250,
        "meaning": 0.200,
        "goal": 0.190
    }
    
    print("=== TAT-DIFF DEMO ===\n")
    
    # 1. Утренняя строка (полный TAT-BRAIN в компактной форме)
    morning_str = weights_to_string(morning)
    print(f"Утро (полный TAT-BRAIN): {morning_str}")
    print(f"Длина: {len(morning_str)} символов\n")
    
    # 2. Вычисляем дельту
    diff = compute_diff(morning, evening)
    print(f"Delta (TAT-DIFF): {diff}")
    print(f"Длина: {len(diff)} символов (Одна строка!)\n")
    
    # 3. Вечером сохраняем только дельту
    # Завтра утром: берём утренний BRAIN и применяем дельту
    restored = apply_diff(morning, diff)
    print(f"Восстановленное вечернее состояние: {weights_to_string(restored)}")
    print(f"Оригинал: {weights_to_string(evening)}")
    print(f"Совпадают: {restored == evening}")
    
    # 4. Хеш для верификации
    print(f"\nХеш утра: {hash_weights(morning)}")
    print(f"Хеш вечера: {hash_weights(evening)}")
