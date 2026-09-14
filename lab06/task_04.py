from flask import Flask, render_template_string

app = Flask(__name__)

students = [
    {"name": "Анна", "group": "ПИ-21", "grade": 5},
    {"name": "Иван", "group": "ПИ-21", "grade": 4},
    {"name": "Ольга", "group": "ПИ-22", "grade": 5},
]

page = """
<h1>Таблица студентов</h1>
<table border="1">
    <tr><th>Имя</th><th>Группа</th><th>Оценка</th></tr>
    {% for student in students %}
    <tr>
        <td>{{ student.name }}</td>
        <td>{{ student.group }}</td>
        <td>{{ student.grade }}</td>
    </tr>
    {% endfor %}
</table>
"""


@app.route("/")
def show_table():
    return render_template_string(page, students=students)


if __name__ == "__main__":
    app.run(debug=True)
