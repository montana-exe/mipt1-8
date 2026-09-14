"""Задание № 7: FastAPI endpoint, который возвращает JSON."""

# Импортируем основной класс веб-фреймворка FastAPI.
from fastapi import FastAPI

# Создаём приложение и задаём название для страницы документации.
app = FastAPI(title="Лабораторная № 6 — задание № 7")


# Декоратор создаёт GET endpoint по адресу /api/status.
@app.get("/api/status")
def status() -> dict[str, object]:
    """Вернуть словарь, который FastAPI преобразует в JSON."""
    # Ключи словаря станут полями JSON-объекта.
    return {"status": "ok", "laboratory": 6, "variant": 2}
