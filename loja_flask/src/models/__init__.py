from .Base import db
from .Produto import Produto
from .Venda import Venda
from .Categoria import Categoria
from .ItemVenda import ItemVenda
from .User import User

__all__ = ['db', 'Produto', 'Venda', 'Categoria', 'ItemVenda', 'User']

def init_app(app):
    """Inicializa os modelos com a aplicação Flask"""
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("Banco de dados inicializado com sucesso!")