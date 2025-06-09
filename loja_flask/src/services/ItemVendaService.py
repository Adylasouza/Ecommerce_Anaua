from models import db
from models.ItemVenda import ItemVenda

class ItemVendaService:
    def listarItemVendas(self):
        return [i.to_dict() for i in ItemVenda.query.all()]

    def listarItemVendaPorId(self, id):
        item = ItemVenda.query.get(id)
        return item.to_dict() if item else None

    def inserirItemVenda(self, data_dict):
        try:
            item = ItemVenda(
                venda_id=data_dict['venda_id'],
                produto_id=data_dict['produto_id'],
                quantidade=data_dict['quantidade'],
                preco_unitario=data_dict['preco_unitario']
            )
            db.session.add(item)
            db.session.commit()
            return item.id
        except Exception as e:
            db.session.rollback()
            raise e

    def atualizarItemVenda(self, id, data_dict):
        try:
            item = ItemVenda.query.get(id)
            if item:
                item.venda_id = data_dict['venda_id']
                item.produto_id = data_dict['produto_id']
                item.quantidade = data_dict['quantidade']
                item.preco_unitario = data_dict['preco_unitario']
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e

    def removerItemVendaPorId(self, id):
        try:
            item = ItemVenda.query.get(id)
            if item:
                db.session.delete(item)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e