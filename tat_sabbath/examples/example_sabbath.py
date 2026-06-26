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


from tat_sabbath import TATSABBATH

sabbath = TATSABBATH()

test_cases = [
    ('Что такое когеренция?', 'Когеренция — это мера смыслового сходства.'),
    ('Что такое TAT-7?', 'TAT-7 — это версия TAT с 7 головами.'),
    ('Что такое бесконечность?', 'Я не знаю.'),
]

for query, answer in test_cases:
    result = sabbath.verify(query, answer)
    print(f'\\n❓ {query}')
    print(f'💬 {answer}')
    print(f'📊 {result}')