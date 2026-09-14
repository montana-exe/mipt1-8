from lab06.task_02 import app as greeting_app
from lab06.task_04 import app as table_app
from lab06.task_07 import app as fastapi_app, status


def test_flask_greeting_form() -> None:
    client = greeting_app.test_client()
    response = client.post("/", data={"name": "Анна"})
    assert response.status_code == 200
    assert "Привет, Анна!" in response.get_data(as_text=True)


def test_flask_escapes_user_input() -> None:
    client = greeting_app.test_client()
    response = client.post("/", data={"name": "<script>alert(1)</script>"})
    body = response.get_data(as_text=True)
    assert "<script>" not in body
    assert "&lt;script&gt;" in body


def test_flask_table() -> None:
    client = table_app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Анна Петрова" in response.get_data(as_text=True)


def test_fastapi_json_endpoint() -> None:
    assert any(route.path == "/api/status" for route in fastapi_app.routes)
    assert status() == {"status": "ok", "laboratory": 6, "variant": 2}
