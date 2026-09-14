"""Задание № 2: Flask-страница с формой «имя → приветствие»."""

# Flask создаёт приложение, request читает форму, render_template_string строит HTML.
from flask import Flask, render_template_string, request

# Создаём Flask-приложение. __name__ помогает Flask найти текущий модуль.
app = Flask(__name__)

# HTML хранится прямо в файле задания, чтобы пример был самостоятельным.
PAGE = """
<!doctype html>
<html lang="ru">
  <head><meta charset="utf-8"><title>Форма приветствия</title></head>
  <body>
    <h1>Введите имя</h1>
    <form method="post">
      <input name="name" required>
      <button type="submit">Поприветствовать</button>
    </form>
    {% if name %}<p>Привет, {{ name }}!</p>{% endif %}
  </body>
</html>
"""


# methods разрешает открытие страницы через GET и отправку формы через POST.
@app.route("/", methods=["GET", "POST"])
def greeting() -> str:
    """Показать форму и приветствие после её отправки."""
    # При POST читаем поле name; при GET используем пустую строку.
    name = request.form.get("name", "").strip() if request.method == "POST" else ""
    # Jinja2 подставит имя в шаблон и автоматически экранирует опасный HTML.
    return render_template_string(PAGE, name=name)


if __name__ == "__main__":
    # debug=True перезапускает сервер после изменений во время разработки.
    app.run(debug=True)
