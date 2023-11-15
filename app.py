from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///empresa.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    funcionarios = db.relationship("Funcionario", backref="setor")
    cargos = db.relationship("Cargos", backref="setor")


class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)
    status_funcionario = db.Column(db.Boolean, nullable=False)
    id_setor = db.Column(db.Integer, db.ForeignKey("setor.id"), nullable=False)
    id_cargos = db.Column(db.Integer, db.ForeignKey("cargos.id"))
    cargo = db.relationship("Cargos", backref="funcionario")


class Cargos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    id_setor = db.Column(db.Integer, db.ForeignKey("setor.id"), nullable=False)


@app.route("/")
def index():
    with app.app_context():
        funcionarios = Funcionario.query.all()
        return render_template("index.html", funcionarios=funcionarios)


@app.route("/add_funcionario", methods=["GET", "POST"])
def add_funcionario():
    with app.app_context():
        if request.method == "POST":
            primeiro_nome = request.form["primeiro_nome"]
            sobrenome = request.form["sobrenome"]
            data_admissao_str = request.form["data_admissao"]
            status_funcionario = (
                True if request.form.get("status_funcionario") else False
            )
            id_setor = request.form["id_setor"]
            id_cargos = request.form["id_cargos"]

            data_admissao = datetime.strptime(data_admissao_str, "%Y-%m-%d").date()

            funcionario = Funcionario(
                primeiro_nome=primeiro_nome,
                sobrenome=sobrenome,
                data_admissao=data_admissao,
                status_funcionario=status_funcionario,
                id_setor=id_setor,
                id_cargos=id_cargos,
            )

            db.session.add(funcionario)
            db.session.commit()

            return redirect(url_for("index"))

        setores = Setor.query.all()
        cargos = Cargos.query.all()
        return render_template("add_funcionario.html", setores=setores, cargos=cargos)


@app.route("/add_setor", methods=["GET", "POST"])
def add_setor():
    with app.app_context():
        if request.method == "POST":
            nome = request.form["nome"]

            setor = Setor(nome=nome)
            db.session.add(setor)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("add_setor.html")


@app.route("/add_cargos", methods=["GET", "POST"])
def add_cargos():
    with app.app_context():
        if request.method == "POST":
            nome = request.form["nome"]
            id_setor = request.form["id_setor"]

            cargos = Cargos(nome=nome, id_setor=id_setor)
            db.session.add(cargos)
            db.session.commit()

            return redirect(url_for("index"))

        setores = Setor.query.all()
        return render_template("add_cargos.html", setores=setores)


@app.route("/ficha_funcionario/<int:funcionario_id>")
def ficha_funcionario(funcionario_id):
    with app.app_context():
        funcionario = Funcionario.query.get(funcionario_id)
        if not funcionario:
            return render_template("ficha_nao_encontrada.html")

        return render_template("ficha_funcionario.html", funcionario=funcionario)


@app.route("/admin")
def admin():
    with app.app_context():
        funcionarios = Funcionario.query.all()
        setores = Setor.query.all()
        cargos = Cargos.query.all()
        return render_template(
            "admin.html", funcionarios=funcionarios, setores=setores, cargos=cargos
        )


@app.route("/editar_funcionario/<int:funcionario_id>", methods=["GET", "POST"])
def editar_funcionario(funcionario_id):
    with app.app_context():
        funcionario = Funcionario.query.get(funcionario_id)
        if not funcionario:
            return render_template("ficha_nao_encontrada.html")

        if request.method == "POST":
            funcionario.primeiro_nome = request.form["primeiro_nome"]
            funcionario.sobrenome = request.form["sobrenome"]
            funcionario.data_admissao = datetime.strptime(
                request.form["data_admissao"], "%Y-%m-%d"
            ).date()
            funcionario.status_funcionario = (
                True if request.form.get("status_funcionario") else False
            )
            funcionario.id_setor = request.form["id_setor"]
            funcionario.id_cargos = request.form["id_cargos"]

            db.session.commit()
            return redirect(url_for("admin"))

        setores = Setor.query.all()
        cargos = Cargos.query.all()
        return render_template(
            "editar_funcionario.html",
            funcionario=funcionario,
            setores=setores,
            cargos=cargos,
        )


@app.route("/excluir_funcionario/<int:funcionario_id>")
def excluir_funcionario(funcionario_id):
    with app.app_context():
        funcionario = Funcionario.query.get(funcionario_id)
        if not funcionario:
            return render_template("ficha_nao_encontrada.html")

        db.session.delete(funcionario)
        db.session.commit()
        return redirect(url_for("admin"))


@app.route("/editar_setor/<int:setor_id>", methods=["GET", "POST"])
def editar_setor(setor_id):
    with app.app_context():
        setor = Setor.query.get(setor_id)
        if not setor:
            return render_template("ficha_nao_encontrada.html")

        if request.method == "POST":
            setor.nome = request.form["nome"]

            db.session.commit()
            return redirect(url_for("admin"))

        return render_template("editar_setor.html", setor=setor)


@app.route("/excluir_setor/<int:setor_id>")
def excluir_setor(setor_id):
    with app.app_context():
        setor = Setor.query.get(setor_id)
        if not setor:
            return render_template("ficha_nao_encontrada.html")

        db.session.delete(setor)
        db.session.commit()
        return redirect(url_for("admin"))


@app.route("/editar_cargos/<int:cargo_id>", methods=["GET", "POST"])
def editar_cargos(cargo_id):
    with app.app_context():
        cargo = Cargos.query.get(cargo_id)
        if not cargo:
            return render_template("ficha_nao_encontrada.html")

        if request.method == "POST":
            cargo.nome = request.form["nome"]
            cargo.id_setor = request.form["id_setor"]

            db.session.commit()
            return redirect(url_for("admin"))

        setores = Setor.query.all()
        return render_template("editar_cargos.html", cargo=cargo, setores=setores)


@app.route("/excluir_cargos/<int:cargo_id>")
def excluir_cargos(cargo_id):
    with app.app_context():
        cargo = Cargos.query.get(cargo_id)
        if not cargo:
            return render_template("ficha_nao_encontrada.html")

        db.session.delete(cargo)
        db.session.commit()
        return redirect(url_for("admin"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
