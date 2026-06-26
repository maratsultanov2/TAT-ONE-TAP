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

class AdaptiveThresholds:
    def __init__(self):
        self.silence = 0.3
        self.search = 0.6
        self.link = 0.7
        self.compress = 0.85

    def for_query(self, query):
        if len(query.split()) < 5:
            return {'silence': 0.25, 'search': 0.5, 'link': 0.6, 'compress': 0.8}
        if len(query.split()) > 20:
            return {'silence': 0.35, 'search': 0.7, 'link': 0.8, 'compress': 0.9}
        return {'silence': self.silence, 'search': self.search, 'link': self.link, 'compress': self.compress}

thresholds = AdaptiveThresholds()