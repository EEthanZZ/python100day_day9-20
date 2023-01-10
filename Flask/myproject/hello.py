from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapped():
        return "<b>" + function() + "</b>"
    return wrapped


def make_em(function):
    def wrapped():
        return "<em>" + function() + "</em>"
    return wrapped




@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>this is a second line</p>" \
           '<img src="https://media.giphy.com/media/V3Z76ctCO3jG0/giphy.gif" width=200>'


@app.route("/sayhi")
@make_bold
@make_em
def say_hi():
    return "<p>Hi!!</p>"


@app.route("/<name>/<number>")
def greeting(name, number):
    return f"Hi, {name}, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
