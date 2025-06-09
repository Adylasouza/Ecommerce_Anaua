from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.Venda import Venda
from src.repository.Repository import Repository
from datetime import datetime

class VendaService():

    def __init__(self):
        self.repository = Repository()

    # LISTAR TODAS AS VENDAS
    def listarVendas(self):
        session = Session(self.repository.engine)
        stmt = select(Venda)
        listResp = session.scalars(stmt).all()
        session.close()
        return listResp

    # LISTAR UMA VENDA POR ID
    def listarVendaPorId(self, id):
        session = Session(self.repository.engine)
        stmt = select(Venda).where(Venda.id == id)
        resp = session.scalars(stmt).first()
        session.close()
        return resp

    # INSERIR NOVA VENDA
    def inserirVenda(self, data_dict):
        session = Session(self.repository.engine)
        try:
            nova_venda = Venda(
                usuario_id=data_dict['usuario_id'],
                data_venda=data_dict.get('data_venda', datetime.utcnow()),
                produto_id=data_dict['produto_id'],
                quantidade=data_dict['quantidade']
            )
            session.add(nova_venda)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # ATUALIZAR VENDA EXISTENTE
    def atualizarVenda(self, data_dict):
        session = Session(self.repository.engine)
        try:
            stmt = select(Venda).where(Venda.id == data_dict['id'])
            vendaExiste = session.scalars(stmt).first()
            if vendaExiste:
                vendaExiste.usuario_id = data_dict['usuario_id']
                vendaExiste.data_venda = data_dict.get('data_venda', vendaExiste.data_venda)
                vendaExiste.produto_id = data_dict['produto_id']
                vendaExiste.quantidade = data_dict['quantidade']
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # REMOVER VENDA POR ID
    def removerVendaPorId(self, id):
        session = Session(self.repository.engine)
        try:
            session.query(Venda).filter(Venda.id == id).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
