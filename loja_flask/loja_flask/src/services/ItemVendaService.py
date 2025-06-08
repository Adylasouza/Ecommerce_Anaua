from sqlalchemy import select
from sqlalchemy.orm import Session
from models.ItemVenda import ItemVenda
from repository.Repository import Repository

class ItemVendaService ():

  def __init__(self):
    self.repository = Repository ()

  #CRUD de item_venda
  
  def listarItemVendas (self):
    session = Session(self.repository.engine)
    stmt = select(ItemVenda) # SELECT * FROM ItemVenda;
    listResp = session.scalars(stmt).all()
    session.close()
    return listResp

  def listarItemVendaPorId (self, id):
    session = Session(self.repository.engine)
    stmt = select(ItemVenda).where(ItemVenda.id, id) # SELECT * FROM itemvenda WHERE itemvenda.id = id;
    resp = session.scalars(stmt).one()
    session.close()
    return resp

  def inserirItemVenda(self, itens_venda):
    session = Session(self.repository.engine)
    session.add(itens_venda) # INSERT INTO itemvenda VALUES (ID = , DATAVENDA =, QUANTIDADE = , PRODUTO = );
    session.commit()
    session.close()

  def atualizarItemVenda (self, itens_venda):    
    session = Session(self.repository.engine)
    stmt = select(itens_venda).where(itens_venda.id, id) # SELECT * FROM itemvenda WHERE venda.id = id;
    itens_vendaExiste = session.scalars(stmt).one()
    if (itens_vendaExiste):
      itens_vendaExiste.venda_id = itens_venda.venda_id
      itens_vendaExiste.preco_unitario = itens_venda.preco_unitario
      itens_vendaExiste.produto_id = itens_venda.produto_id
      itens_vendaExiste.quantidade = itens_venda.quantidade
      session.commit() # UPDATE .... 
    session.close()
  
  def removerItemVendaPorId (self, id):
    session = Session(self.repository.engine)
    produtoExiste = session.query(ItemVenda).filter(ItemVenda.id == id).delete() # DELETE FROM venda WHERE venda.id = id;
    session.commit()