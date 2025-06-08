from sqlalchemy import select
from sqlalchemy.orm import Session

from models.Venda import Venda
from repository.Repository import Repository

class VendaService ():

  def __init__(self):
    self.repository = Repository ()

  #CRUD de venda
  
  def listarVendas (self):
    session = Session(self.repository.engine)
    stmt = select(Venda) # SELECT * FROM venda;
    listResp = session.scalars(stmt).all()
    session.close()
    return listResp

  def listarVendaPorId (self, id):
    session = Session(self.repository.engine)
    stmt = select(Venda).where(Venda.id, id) # SELECT * FROM venda WHERE venda.id = id;
    resp = session.scalars(stmt).one()
    session.close()
    return resp

  def inserirVenda(self, venda):
    session = Session(self.repository.engine)
    session.add(venda) # INSERT INTO venda VALUES (ID = , DATAVENDA =, QUANTIDADE = , PRODUTO = );
    session.commit()
    session.close()

  def atualizarVenda (self, venda):    
    session = Session(self.repository.engine)
    stmt = select(Venda).where(Venda.id, id) # SELECT * FROM venda WHERE venda.id = id;
    vendaExiste = session.scalars(stmt).one()
    if (vendaExiste):
      vendaExiste.nome = venda.nome
      vendaExiste.descrição = venda.descricao
      vendaExiste.preco = venda.preco
      vendaExiste.quantidade = venda.quantidade
      session.commit() # UPDATE .... 
    session.close()
  
  def removerVendaPorId (self, id):
    session = Session(self.repository.engine)
    produtoExiste = session.query(Venda).filter(Venda.id == id).delete() # DELETE FROM venda WHERE venda.id = id;
    session.commit()