# Лабораторная работа № 6. Веб-программирование

Вариант 2, средний уровень:

- № 2 — Flask-страница с формой «имя → приветствие»;
- № 4 — Flask-страница с таблицей данных;
- № 7 — FastAPI endpoint, возвращающий JSON.

Установка выполняется из корня проекта: `pip install -r requirements.txt`.

Flask:

```bash
flask --app lab06.flask_app run --debug
```

Откройте `http://127.0.0.1:5000/` для формы и
`http://127.0.0.1:5000/students` для таблицы.

FastAPI:

```bash
uvicorn lab06.fastapi_app:app --reload
```

JSON доступен по адресу `http://127.0.0.1:8000/api/status`, интерактивная
документация — по адресу `http://127.0.0.1:8000/docs`.
