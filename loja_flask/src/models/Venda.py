from .Base import db
from datetime import datetime

class Venda(db.Model):
    __tablename__ = 'venda'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data_venda = db.Column(db.DateTime, default=datetime.utcnow)
    valor_total = db.Column(db.Numeric(10, 2))

    itens = db.relationship('ItemVenda', back_populates='venda', lazy=True)

    def __repr__(self):
        return f"<Venda {self.id}>"