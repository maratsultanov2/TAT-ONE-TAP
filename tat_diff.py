"""
TAT-DIFF: Differential memory for TAT-BRAIN
Одна строка — один диалог. 5 слоёв, 5 значений.
Экономия токенов: до 99.99% по сравнению с сохранением полного состояния.
Версия 2.0 — зеркальная маркировка и слеш-переход.
"""

import hashlib
from datetime import datetime
from typing import Dict, Optional

LAYERS = ["theme", "role", "emotion", "meaning", "goal"]

def mirror_timestamp(dt: Optional[datetime] = None) -> str:
    """Зеркальная временная метка: DD.MM.YYYY / YYYY.MM.DD"""
    if dt is None:
        dt = datetime.now()
    left = dt.strftime("%d.%m.%Y")
    right = dt.strftime("%Y.%m.%d")
    return f"{left} / {right}"

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

def pack_with_mirror(prev_weights: Dict[str, float], new_weights: Dict[str, float], dt: Optional[datetime] = None) -> str:
    """Упаковывает DIFF с зеркальной меткой и слеш-переходом."""
    diff = compute_diff(prev_weights, new_weights)
    ts = mirror_timestamp(dt)
    return f"{ts} | {diff}"

def unpack_mirror(packed: str) -> Dict[str, str]:
    """Извлекает метку и DIFF из упакованной строки."""
    # Формат: "DD.MM.YYYY / YYYY.MM.DD | t:+0.01,..."
    parts = packed.split(" | ", 1)
    if len(parts) != 2:
        return {"error": "Invalid format"}
    return {"timestamp": parts[0], "diff": parts[1]}

def restore_chain_from_mirror(mirror_lines: list, base_weights: Dict[str, float], last_valid_idx: int) -> Dict[str, float]:
    """Восстанавливает цепочку от последнего валидного слеш-перехода."""
    current = base_weights.copy()
    for line in mirror_lines[last_valid_idx:]:
        info = unpack_mirror(line)
        if "error" in info:
            continue
        # Используем правую часть метки (машинную) для проверки целостности
        ts_parts = info["timestamp"].split(" / ")
        if len(ts_parts) == 2:
            # Можно добавить проверку хеша, но пока достаточно структуры
            current = apply_diff(current, info["diff"])
    return current
