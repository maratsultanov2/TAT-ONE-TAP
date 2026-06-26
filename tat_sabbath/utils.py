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

def format_result(result):
    status = result.get('status', 'UNKNOWN')
    coherence = result.get('coherence', 0.0)
    geometry = result.get('geometry', 'UNKNOWN')
    message = result.get('message', '')

    if status == 'SABBATH':
        return f'🕯️ SABBATH: {message} (C={coherence:.3f})'
    else:
        return f'✅ OK: {message} (C={coherence:.3f}, {geometry})'