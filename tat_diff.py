"""
TAT-DIFF: Differential memory for TAT-BRAIN
Одна строка — один диалог. 5 слоёв, 5 значений.
Экономия токенов: до 99.99% по сравнению с сохранением полного состояния.
"""

import hashlib
from typing import Dict

LAYERS = ["theme", "role", "emotion", "meaning", "goal"]

def weights_to_string(weights: Dict[str, float]) -> str:
    parts = [f"{layer[0]}:{weights[layer]:.2f}" for layer in LAYERS]
    return ",".join(parts)

def string_to_weights(s: str) -> Dict[str, float]:
    layer_map = {"t": "theme", "r": "role", "e": "emotion", "m": "meaning", "g": "goal"}
    weights = {}
    for part in s.split(","):
        if ":" not in part:
            continue
        code, value = part.split(":")
        if code in layer_map:
            weights[layer_map[code]] = float(value)
    return weights

def compute_diff(prev_weights: Dict[str, float], new_weights: Dict[str, float]) -> str:
    diff_parts = []
    for layer in LAYERS:
        old = round(prev_weights.get(layer, 0.0), 2)
        new = round(new_weights.get(layer, 0.0), 2)
        delta = round(new - old, 2)
        sign = "+" if delta > 0 else ""
        diff_parts.append(f"{layer[0]}:{sign}{delta:.2f}")
    return ",".join(diff_parts)

def apply_diff(base_weights: Dict[str, float], diff_str: str) -> Dict[str, float]:
    result = {}
    for layer in LAYERS:
        result[layer] = round(base_weights.get(layer, 0.0), 2)

    layer_map = {"t": "theme", "r": "role", "e": "emotion", "m": "meaning", "g": "goal"}
    for part in diff_str.split(","):
        if ":" not in part:
            continue
        code, delta_str = part.split(":")
        full_name = layer_map.get(code)
        if full_name and full_name in result:
            delta = float(delta_str)
            new_val = round(result[full_name] + delta, 2)
            result[full_name] = max(0.0, min(1.0, new_val))
    return result

def hash_weights(weights: Dict[str, float]) -> str:
    s = weights_to_string(weights)
    return hashlib.sha256(s.encode()).hexdigest()[:8]
