import random
from flask import Flask, render_template
import datetime
import requests
app = Flask(__name__)

@app.route("/")
def start():
    random_number = random.randint(1, 10)
    this_year = datetime.date.today().year
    return render_template("index.html", num=random_number, year=this_year)


@app.route("/guess/<name>")
def guess(name):
    respond = requests.get(f"https://api.agify.io?name={name}")
    age = respond.json()["age"]
    return render_template("james.html", person_name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
