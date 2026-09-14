# Лабораторная работа № 8. Экосистема Python

Вариант 2, средний уровень:

- № 2 — зависимость `requests` добавлена в `pyproject.toml` и общий
  `requirements.txt`;
- № 4 — калькулятор разработан по TDD: сначала создан коммит с тестами
  `test(lab8): define calculator behavior`, затем написана реализация;
- № 7 — операции калькулятора записываются через стандартный модуль `logging`.

Установка зависимостей лабораторной с Poetry:

```bash
poetry install -C lab08
poetry show -C lab08 requests
```

Проверка всего проекта и запуск примера:

```bash
python -m pytest
python -m lab08.calculator
```
