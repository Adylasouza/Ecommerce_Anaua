from .Base import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    codigo = db.Column(db.String(100), unique=True)

    produtos = db.relationship('Produto', back_populates='categoria', lazy=True)

    def __repr__(self):
        return f"<Categoria {self.nome}>"