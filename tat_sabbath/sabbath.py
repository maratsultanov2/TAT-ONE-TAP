# ============================================================
# TAT-SABBATH — ВЕРИФИКАЦИЯ ОТВЕТОВ LLM
# ============================================================
# Copyright (C) 2026 Marat Sultanov
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# 
# For commercial licensing, contact: maratsultanov2@gmail.com
# ============================================================

import numpy as np
from sentence_transformers import SentenceTransformer
from .coherence import quantum_coherence, star_37_73

class TATSABBATH:
    """
    TAT-SABBATH — слой верификации для LLM.
    Copyright (C) 2026 Marat Sultanov
    Commercial use requires a separate license.
    Contact: maratsultanov2@gmail.com
    """

    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.THETA = 1.987
        self.SILENCE_THRESHOLD = 0.3
        self.SEARCH_THRESHOLD = 0.6
        self.LINK_THRESHOLD = 0.7
        self.COMPRESS_THRESHOLD = 0.85

    def verify(self, query, answer):
        if not query or not answer:
            return {
                'status': 'SABBATH',
                'coherence': 0.0,
                'geometry': 'SABBATH',
                'message': 'Пустой запрос или ответ'
            }

        q_emb = self.model.encode(query)
        a_emb = self.model.encode(answer)

        coherence = quantum_coherence(q_emb, a_emb)
        geometry = star_37_73(coherence)

        if coherence < self.SILENCE_THRESHOLD:
            return {
                'status': 'SABBATH',
                'coherence': coherence,
                'geometry': geometry,
                'message': 'Низкая когеренция — тишина'
            }

        return {
            'status': 'OK',
            'coherence': coherence,
            'geometry': geometry,
            'message': 'Ответ прошёл проверку'
        }