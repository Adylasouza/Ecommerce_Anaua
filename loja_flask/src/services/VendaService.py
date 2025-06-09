from models import db
from models.Venda import Venda
from datetime import datetime

class VendaService:
    def listarVendas(self):
        return [v.to_dict() for v in Venda.query.all()]

    def listarVendaPorId(self, id):
        venda = Venda.query.get(id)
        return venda.to_dict() if venda else None

    def inserirVenda(self, data_dict):
        try:
            venda = Venda(
                usuario_id=data_dict['usuario_id'],
                valor_total=data_dict['valor_total'],
                forma_pagamento=data_dict['forma_pagamento']
            )
            db.session.add(venda)
            db.session.commit()
            return venda.id
        except Exception as e:
            db.session.rollback()
            raise e

    def atualizarVenda(self, id, data_dict):
        try:
            venda = Venda.query.get(id)
            if venda:
                venda.forma_pagamento = data_dict['forma_pagamento']
                venda.valor_total = data_dict['valor_total']
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e

    def removerVendaPorId(self, id):
        try:
            venda = Venda.query.get(id)
            if venda:
                db.session.delete(venda)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e