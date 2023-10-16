# aplicação basica de flask
from flask import Flask, render_template
# importando o banco de dados






app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port="3000", debug=True)
