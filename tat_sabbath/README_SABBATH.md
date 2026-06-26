# 🕯️ TAT-SABBATH

## Что это

TAT-SABBATH — это слой верификации для LLM. Проверяет когеренцию между запросом и ответом.
При C < 0.3 возвращает SABBATH (тишина).

## Лицензия

TAT-SABBATH is released under **AGPL-3.0** for open-source and non-commercial use.

**For commercial use**, a separate commercial license is required.

Contact: maratsultanov2@gmail.com

## Установка
```bash
pip install -r tat_sabbath/requirements_sabbath.txt
```

## Пример
```python
from tat_sabbath import TATSABBATH
sabbath = TATSABBATH()
result = sabbath.verify('Что такое когеренция?', 'Когеренция — это мера смыслового сходства.')
print(result)
```

## Авторские права

Copyright (C) 2026 Marat Sultanov