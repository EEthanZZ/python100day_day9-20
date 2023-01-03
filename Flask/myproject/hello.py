from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sayhi")
def say_hi():
    return "<p>Hi!!</p>"


@app.route("/<name>")
def greeting(name):
    return f"Hi, {name}"
if __name__ == "__main__":
    app.run(debug=True)
