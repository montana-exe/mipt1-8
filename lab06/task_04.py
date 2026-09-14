"""Задание № 4: Flask-страница с таблицей данных."""

from flask import Flask, render_template_string

# Создаём отдельное приложение для этого задания.
app = Flask(__name__)

# Данные представлены списком словарей: один словарь соответствует одной строке.
STUDENTS = [
    {"name": "Анна Петрова", "group": "ПИ-21", "grade": 5},
    {"name": "Иван Соколов", "group": "ПИ-21", "grade": 4},
    {"name": "Ольга Орлова", "group": "ПИ-22", "grade": 5},
]

# Цикл Jinja2 создаёт строку таблицы для каждого студента.
PAGE = """
<!doctype html>
<html lang="ru">
  <head><meta charset="utf-8"><title>Таблица студентов</title></head>
  <body>
    <h1>Результаты студентов</h1>
    <table border="1" cellpadding="8">
      <tr><th>Имя</th><th>Группа</th><th>Оценка</th></tr>
      {% for student in students %}
        <tr>
          <td>{{ student.name }}</td>
          <td>{{ student.group }}</td>
          <td>{{ student.grade }}</td>
        </tr>
      {% endfor %}
    </table>
  </body>
</html>
"""


# Декоратор связывает адрес / с функцией students_table.
@app.get("/")
def students_table() -> str:
    """Вернуть HTML-страницу с таблицей студентов."""
    # Передаём список STUDENTS внутрь HTML-шаблона.
    return render_template_string(PAGE, students=STUDENTS)


if __name__ == "__main__":
    app.run(debug=True)
