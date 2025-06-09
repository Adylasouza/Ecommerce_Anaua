from .Base import db

class ItemVenda(db.Model):
    __tablename__ = 'itemvenda'
    
    id = db.Column(db.Integer, primary_key=True)
    venda_id = db.Column(db.Integer, db.ForeignKey('venda.id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Numeric(10, 2), nullable=False)

    # Relacionamentos
    venda = db.relationship('Venda', back_populates='itens')
    produto = db.relationship('Produto', back_populates='itens_venda')

    def __repr__(self):
        return f"<ItemVenda Venda={self.venda_id} Produto={self.produto_id}>"