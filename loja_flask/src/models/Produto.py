from .Base import db

class Produto(db.Model):
    __tablename__ = 'produto'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    estoque = db.Column(db.Integer, default=0)
    foto_url = db.Column(db.String(255))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    # Relacionamentos
    categoria = db.relationship('Categoria', back_populates='produtos')
    itens_venda = db.relationship('ItemVenda', back_populates='produto')

    def __repr__(self):
        return f"<Produto {self.nome}>"