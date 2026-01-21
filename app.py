from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)

# Настройка сценария
BIRTHDATE = date(2009, 1, 27)  # дата рождения Вани
AGE = 17


@app.route("/")
def index():
    test_mode = request.args.get("test") == "1"
    return render_template(
        "index.html",
        birth_iso=BIRTHDATE.isoformat(),
        age=AGE,
        test_mode=test_mode,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
