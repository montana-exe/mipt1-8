# Лабораторная работа № 6. Веб-программирование

Вариант 2, средний уровень:

- `task_02.py` — Flask-страница с формой «имя → приветствие»;
- `task_04.py` — Flask-страница с таблицей данных;
- `task_07.py` — FastAPI endpoint, возвращающий JSON.

Установка выполняется из корня проекта: `pip install -r requirements.txt`.

Каждое Flask-задание запускается отдельно:

```bash
python -m lab06.task_02
python -m lab06.task_04
```

FastAPI:

```bash
uvicorn lab06.task_07:app --reload
```

JSON доступен по адресу `http://127.0.0.1:8000/api/status`.
