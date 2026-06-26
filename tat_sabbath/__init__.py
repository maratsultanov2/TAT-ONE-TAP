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

from .sabbath import TATSABBATH
from .coherence import quantum_coherence, star_37_73
from .thresholds import thresholds

__version__ = "1.0.0"
__all__ = ['TATSABBATH', 'quantum_coherence', 'star_37_73', 'thresholds']