import json, re, numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

class TATMonitor:
    """
    Универсальный детектор структурных аномалий в диалоговых системах.
    Покрывает все четыре уровня сложности (v1–v4) с адаптивной v4-стратегией.
    """
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.revert_words = {'revert', 'go back', 'undo', 'original', 'before', 
                             'scrap', 'earlier', 'cancel', 'roll back', 'restore', 
                             'prior', 'mistake', 'previous', 'switch was'}
        self.keep_words = {'keep', 'stick with', 'stands', 'leave it', 'latest', 
                           'updated', 'no rollback', 'happy with', 'confirmed', 
                           'final, don', 'right, leave', 'stay with'}

    def _get_similarities(self, candidate, lines):
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
            return {'verdict': 'revert', 'confidence': 0.99, 'level': 'v1'}
        if has_keep_word and new_value and new_value in cand_lower:
            return {'verdict': 'keep', 'confidence': 0.99, 'level': 'v1'}
        if has_revert_word:
            return {'verdict': 'revert', 'confidence': 0.8, 'level': 'v1'}
        if has_keep_word:
            return {'verdict': 'keep', 'confidence': 0.8, 'level': 'v1'}

        # v3: asserted_value (из кандидата напрямую)
        if old_value and new_value:
            if old_value in cand_lower and new_value not in cand_lower:
                return {'verdict': 'revert', 'confidence': 0.95, 'level': 'v3'}
            if new_value in cand_lower and old_value not in cand_lower:
                return {'verdict': 'keep', 'confidence': 0.95, 'level': 'v3'}

        # v4: адаптивное контекстное сравнение
        if len(context) >= 2:
            # Определяем, какие линии использовать для старого и нового
            old_lines = []
            new_lines = []
            
            # Если есть 4 строки — используем стандартную схему: 0,2 = old; 1,3 = new
            if len(context) >= 4:
                old_lines = [context[0], context[2]]
                new_lines = [context[1], context[3]]
            # Если 2 строки — используем только их
            elif len(context) >= 2:
                old_lines = [context[0]]
                new_lines = [context[1]]
            # Если нечётное количество — первый к старому, остальные к новому
            else:
                old_lines = [context[0]]
                new_lines = context[1:] if len(context) > 1 else []
            
            # Вычисляем сходство с объединёнными старыми и новыми линиями
            all_lines = old_lines + new_lines
            if all_lines:
                sims = self._get_similarities(candidate, all_lines)
                sim_old = np.mean(sims[:len(old_lines)]) if old_lines else 0
                sim_new = np.mean(sims[len(old_lines):]) if new_lines else 0
                prob = sim_old / (sim_old + sim_new + 1e-8)
                verdict = 'revert' if prob > 0.5 else 'keep'
                return {'verdict': verdict, 'confidence': float(prob), 'level': f'v4-adaptive (context lines: {len(context)})'}

        # v2: только ключевые слова
        if has_revert_word:
            return {'verdict': 'revert', 'confidence': 0.7, 'level': 'v2'}
        if has_keep_word:
            return {'verdict': 'keep', 'confidence': 0.7, 'level': 'v2'}

        # default
        return {'verdict': 'keep', 'confidence': 0.5, 'level': 'default (no signal)'}
