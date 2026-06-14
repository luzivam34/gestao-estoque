from flask import Blueprint, render_template, request,redirect,url_for
from app.models.produto_model import Produto
from app.extension_service.extension_service import db

produto_bp = Blueprint('produtobp', __name__)


@produto_bp.route("/lista")
def lista_produtos():
    produtos = Produto.query.order_by(Produto.id).all()
    return render_template("lista_produtos.html", produtos=produtos)


@produto_bp.route("/cadastro", methods=["POST", "GET"])
def cadastro_produtos():
    if request.method == "POST":
        nome = request.form["nome"]
        quantidade = request.form["quantidade"]
        valor= request.form["valor"]

        new_produto = Produto(
            nome=nome,
            quantidade=quantidade,
            valor=valor
        )
        db.session.add(new_produto)
        db.session.commit()
        return redirect(url_for("produtobp.lista_produtos"))
    return render_template("cadastro_produtos.html")
