from flask import Flask, render_template, request, redirect
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
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM setor"))
        rows = result.fetchall()

    return render_template("index.html", rows=rows)


@app.route("/inserir", methods=["POST"])
def inserir():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    data_admissao = request.form["data_admissao"]
    status = request.form["status"]

    try:
        with engine.connect() as conn:
            conn.execute(
                text(
                    "INSERT INTO setor (nome, sobrenome, data_admissao, status) VALUES (:nome, :sobrenome, :data_admissao, :status)"
                ),
                {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "data_admissao": data_admissao,
                    "status": status,
                },
            )
    except Exception as e:
        print("Erro ao inserir dados:", e)
        return redirect("/")

    return redirect("/")

@app.route("/atualizar", methods=["POST"])
def atualizar():
    id = request.form["id"]
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    data_admissao = request.form["data_admissao"]
    status = request.form["status"]

    try:
        with engine.connect() as conn:
            conn.execute(text("UPDATE setor SET nome=:nome, sobrenome=:sobrenome, data_admissao=:data_admissao, status=:status WHERE id=:id"), {"id": id, "nome": nome, "sobrenome": sobrenome, "data_admissao": data_admissao, "status": status})
    except Exception as e:
        print("Erro ao atualizar dados:", e)
        return redirect("/")

    return redirect("/")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
