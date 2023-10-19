from flask import Flask, render_template
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from servicos.check_db import *


engine = create_engine("sqlite:///funcionarios.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM setor"))
    for row in result:
        print(row)

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
