from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello everyone"


@app.route("/about")
def about():
    return "It is information about you"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
