import random
from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def start():
    random_number = random.randint(1, 10)
    this_year = datetime.date.today().year
    return render_template("index.html", num=random_number, year=this_year)


if __name__ == "__main__":
    app.run(debug=True)
