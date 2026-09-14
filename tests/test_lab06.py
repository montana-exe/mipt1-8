from fastapi.testclient import TestClient

from lab06.fastapi_app import app as fastapi_app
from lab06.flask_app import create_app


def test_flask_greeting_form() -> None:
    client = create_app().test_client()
    response = client.post("/", data={"name": "Анна"})
    assert response.status_code == 200
    assert "Привет, Анна!" in response.get_data(as_text=True)


def test_flask_escapes_user_input() -> None:
    client = create_app().test_client()
    response = client.post("/", data={"name": "<script>alert(1)</script>"})
    body = response.get_data(as_text=True)
    assert "<script>" not in body
    assert "&lt;script&gt;" in body


def test_flask_table() -> None:
    client = create_app().test_client()
    response = client.get("/students")
    assert response.status_code == 200
    assert "Анна Петрова" in response.get_data(as_text=True)


def test_fastapi_json_endpoint() -> None:
    response = TestClient(fastapi_app).get("/api/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "laboratory": 6, "variant": 2}
