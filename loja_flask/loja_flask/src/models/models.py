from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db


db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categoria'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    descricao = db.Column(db.Text)
    codigo = db.Column(db.String(100))

    produtos = db.relationship('Produto', backref='categoria', lazy=True)

    def __repr__(self):
        return f"<Categoria {self.nome}>"

class Produto(db.Model):
    __tablename__ = 'produto'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    descricao = db.Column(db.Text)
    preco = db.Column(db.Numeric(10, 2))
    estoque = db.Column(db.Integer)
    foto_url = db.Column(db.Text)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    vendas = db.relationship('Venda', backref='produto', lazy=True)
    itens_venda = db.relationship('ItemVenda', backref='produto', lazy=True)

    def __repr__(self):
        return f"<Produto {self.nome}>"

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    is_authenticated = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    is_anonymous = db.Column(db.Boolean, default=False)

    vendas = db.relationship('Venda', backref='usuario', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class Venda(db.Model):
    __tablename__ = 'venda'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data_venda = db.Column(db.DateTime, default=datetime.utcnow)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    quantidade = db.Column(db.Integer)

    itens = db.relationship('ItemVenda', backref='venda', lazy=True)

    def __repr__(self):
        return f"<Venda {self.id}>"

class ItemVenda(db.Model):
    __tablename__ = 'itemvenda'
    
    id = db.Column(db.Integer, primary_key=True)
    venda_id = db.Column(db.Integer, db.ForeignKey('venda.id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    quantidade = db.Column(db.Integer)
    preco_unitario = db.Column(db.Numeric(10, 2))

    def __repr__(self):
        return f"<ItemVenda Venda={self.venda_id} Produto={self.produto_id}>"