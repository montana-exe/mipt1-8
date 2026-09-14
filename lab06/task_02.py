from flask import Flask, render_template_string, request

app = Flask(__name__)

page = """
<h1>Введите имя</h1>
<form method="post">
    <input name="name" required>
    <button type="submit">Поприветствовать</button>
</form>
{% if name %}<p>Привет, {{ name }}!</p>{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def greeting():
    name = request.form.get("name", "")
    return render_template_string(page, name=name)


if __name__ == "__main__":
    app.run(debug=True)
