import json, re, numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

class TATMonitor:
    """
    Универсальный детектор структурных аномалий в диалоговых системах.
    Покрывает все четыре уровня сложности (v1–v4) с адаптивной v4-стратегией.
    Поддерживает provenance-поля и возвращает объяснение решения.
    """
    def __init__(self, model_name='all-MiniLM-L6-v2', use_embeddings=True):
        self.use_embeddings = use_embeddings
        if use_embeddings:
            self.model = SentenceTransformer(model_name)
        self.revert_words = {'revert', 'go back', 'undo', 'original', 'before', 
                             'scrap', 'earlier', 'cancel', 'roll back', 'restore', 
                             'prior', 'mistake', 'previous', 'switch was'}
        self.keep_words = {'keep', 'stick with', 'stands', 'leave it', 'latest', 
                           'updated', 'no rollback', 'happy with', 'confirmed', 
                           'final, don', 'right, leave', 'stay with'}

    def _get_similarities(self, candidate, lines):
        if not self.use_embeddings:
            return [0.0] * len(lines)
        emb_cand = self.model.encode([candidate])[0]
        emb_lines = self.model.encode(lines)
        return [cosine_similarity([emb_cand], [emb])[0,0] for emb in emb_lines]

    def predict(self, record):
        candidate = record.get('candidate', '')
        context = record.get('context', [])
        old_value = record.get('old_value', '')
        new_value = record.get('current_value', '')
        cand_lower = candidate.lower()
        has_revert_word = any(w in cand_lower for w in self.revert_words)
        has_keep_word = any(w in cand_lower for w in self.keep_words)

        # v1: явные revert-слова + значение
        if has_revert_word and old_value and old_value in cand_lower:
            return {'verdict': 'revert', 'confidence': 0.99, 'level': 'v1',
                    'explanation': 'v1: revert keyword + old value found in candidate'}
        if has_keep_word and new_value and new_value in cand_lower:
            return {'verdict': 'keep', 'confidence': 0.99, 'level': 'v1',
                    'explanation': 'v1: keep keyword + new value found in candidate'}
        if has_revert_word:
            return {'verdict': 'revert', 'confidence': 0.8, 'level': 'v1',
                    'explanation': 'v1: revert keyword found (no value match)'}
        if has_keep_word:
            return {'verdict': 'keep', 'confidence': 0.8, 'level': 'v1',
                    'explanation': 'v1: keep keyword found (no value match)'}

        # v3: asserted_value
        if old_value and new_value:
            if old_value in cand_lower and new_value not in cand_lower:
                return {'verdict': 'revert', 'confidence': 0.95, 'level': 'v3',
                        'explanation': 'v3: asserted_value is old'}
            if new_value in cand_lower and old_value not in cand_lower:
                return {'verdict': 'keep', 'confidence': 0.95, 'level': 'v3',
                        'explanation': 'v3: asserted_value is new'}

        # v4: адаптивное контекстное сравнение + provenance
        if len(context) >= 2:
            old_lines, new_lines = [], []
            anchor_old = record.get('anchor_old', '')
            anchor_current = record.get('anchor_current', '')
            role_old = record.get('role_old', '')
            role_current = record.get('role_current', '')
            
            if anchor_old or role_old:
                for line in context:
                    line_lower = line.lower()
                    if (anchor_old and anchor_old.lower() in line_lower) or                        (role_old and role_old.lower() in line_lower):
                        old_lines.append(line)
                    elif (anchor_current and anchor_current.lower() in line_lower) or                          (role_current and role_current.lower() in line_lower):
                        new_lines.append(line)
            
            if not old_lines and not new_lines:
                if len(context) >= 4:
                    old_lines = [context[0], context[2]]
                    new_lines = [context[1], context[3]]
                elif len(context) >= 2:
                    old_lines = [context[0]]
                    new_lines = [context[1]]
                else:
                    old_lines = [context[0]]
                    new_lines = context[1:] if len(context) > 1 else []
            
            all_lines = old_lines + new_lines
            if all_lines:
                sims = self._get_similarities(candidate, all_lines)
                sim_old = np.mean(sims[:len(old_lines)]) if old_lines else 0
                sim_new = np.mean(sims[len(old_lines):]) if new_lines else 0
                prob = sim_old / (sim_old + sim_new + 1e-8)
                verdict = 'revert' if prob > 0.5 else 'keep'
                level = 'v4-provenance' if (anchor_old or role_old) else 'v4-adaptive'
                return {'verdict': verdict, 'confidence': float(prob), 'level': level,
                        'explanation': f'v4: candidate closer to {"old" if verdict == "revert" else "new"} context lines'}

        # v2: только ключевые слова
        if has_revert_word:
            return {'verdict': 'revert', 'confidence': 0.7, 'level': 'v2',
                    'explanation': 'v2: revert keyword only'}
        if has_keep_word:
            return {'verdict': 'keep', 'confidence': 0.7, 'level': 'v2',
                    'explanation': 'v2: keep keyword only'}

        return {'verdict': 'keep', 'confidence': 0.5, 'level': 'default',
                'explanation': 'default: no signal detected'}
