# flask app with templates and static files

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="localhost", port="3000", debug=True)
