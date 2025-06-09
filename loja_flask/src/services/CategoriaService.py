from models import db
from models.Categoria import Categoria

class CategoriaService:
    def listarCategoria(self):
        return [c.to_dict() for c in Categoria.query.all()]

    def listarCategoriaPorId(self, id):
        categoria = Categoria.query.get(id)
        return categoria.to_dict() if categoria else None

    def inserirCategoria(self, data_dict):
        try:
            categoria = Categoria(
                nome=data_dict['nome'],
                descricao=data_dict.get('descricao'),
                codigo=data_dict['codigo']
            )
            db.session.add(categoria)
            db.session.commit()
            return categoria.id
        except Exception as e:
            db.session.rollback()
            raise e

    def atualizarCategoria(self, id, data_dict):
        try:
            categoria = Categoria.query.get(id)
            if categoria:
                categoria.nome = data_dict['nome']
                categoria.descricao = data_dict.get('descricao', categoria.descricao)
                categoria.codigo = data_dict['codigo']
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e

    def removerCategoriaPorId(self, id):
        try:
            categoria = Categoria.query.get(id)
            if categoria:
                db.session.delete(categoria)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e