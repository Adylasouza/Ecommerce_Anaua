from models import db
from models.Produto import Produto

class ProdutoService:
    def listarProdutos(self):
        return [p.to_dict() for p in Produto.query.all()]

    def listarProdutoPorId(self, id):
        produto = Produto.query.get(id)
        return produto.to_dict() if produto else None

    def inserirProduto(self, data_dict):
        try:
            produto = Produto(
                nome=data_dict['nome'],
                descricao=data_dict.get('descricao'),
                preco=data_dict['preco'],
                estoque=data_dict.get('estoque', 0),
                foto_url=data_dict.get('foto_url'),
                categoria_id=data_dict['categoria_id']
            )
            db.session.add(produto)
            db.session.commit()
            return produto.id
        except Exception as e:
            db.session.rollback()
            raise e

    def atualizarProduto(self, data_dict):
        try:
            produto = Produto.query.get(data_dict['id'])
            if produto:
                produto.nome = data_dict['nome']
                produto.descricao = data_dict.get('descricao', produto.descricao)
                produto.preco = data_dict['preco']
                produto.estoque = data_dict.get('estoque', produto.estoque)
                produto.foto_url = data_dict.get('foto_url', produto.foto_url)
                produto.categoria_id = data_dict['categoria_id']
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e

    def removerProdutoPorId(self, id):
        try:
            produto = Produto.query.get(id)
            if produto:
                db.session.delete(produto)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e