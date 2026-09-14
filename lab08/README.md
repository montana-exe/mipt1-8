# Лабораторная работа № 8. Экосистема Python

Вариант 2, средний уровень:

- `task_02.py` — зависимость `requests` добавлена в `pyproject.toml` и общий
  `requirements.txt`;
- `task_04.py` — калькулятор разработан по TDD: сначала создан коммит с тестами
  `test(lab8): define calculator behavior`, затем написана реализация;
- `task_07.py` — пример работы со стандартным модулем `logging`.

Установка зависимостей лабораторной с Poetry:

```bash
poetry install -C lab08
poetry show -C lab08 requests
```

Проверка всего проекта и запуск примера:

```bash
python -m pytest
python -m lab08.task_02
python -m lab08.task_04
python -m lab08.task_07
```
