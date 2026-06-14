from app import db
from sqlalchemy import Numeric

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer)
    valor = db.Column(Numeric(10, 2), nullable=False)
