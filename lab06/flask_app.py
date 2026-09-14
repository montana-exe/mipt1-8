"""Flask-задания: форма с приветствием и таблица данных."""

from flask import Flask, render_template, request

STUDENTS = (
    {"name": "Анна Петрова", "group": "ПИ-21", "grade": 5},
    {"name": "Иван Соколов", "group": "ПИ-21", "grade": 4},
    {"name": "Ольга Орлова", "group": "ПИ-22", "grade": 5},
)


def create_app() -> Flask:
    """Создать и настроить Flask-приложение."""
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def greeting() -> str:
        name = request.form.get("name", "").strip() if request.method == "POST" else ""
        return render_template("greeting.html", name=name)

    @app.get("/students")
    def students() -> str:
        return render_template("students.html", students=STUDENTS)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
