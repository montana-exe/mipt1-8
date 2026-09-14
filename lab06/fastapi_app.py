"""FastAPI endpoint, возвращающий JSON."""

from fastapi import FastAPI

app = FastAPI(title="Лабораторная работа № 6", version="1.0.0")


@app.get("/api/status")
def status() -> dict[str, object]:
    """Вернуть сведения о состоянии API в формате JSON."""
    return {"status": "ok", "laboratory": 6, "variant": 2}
