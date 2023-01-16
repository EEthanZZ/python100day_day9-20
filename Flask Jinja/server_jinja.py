import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number)


if __name__ == "__main__":
    app.run(debug=True)
