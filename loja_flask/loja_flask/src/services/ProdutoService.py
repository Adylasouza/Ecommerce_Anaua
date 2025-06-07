from sqlalchemy import select
from sqlalchemy.orm import Session

from models.Produto import Produto
from repositories.Repository import Repository

class ProdutoService ():

  def __init__(self):
    self.repository = Repository ()

  #CRUD de produto

  def listarProdutos (self):
    session = Session(self.repository.engine)
    stmt = select(Produto) # SELECT * FROM produto;
    listResp = session.scalars(stmt).all()
    session.close()
    return listResp

  def listarProdutoPorId (self, id):
    session = Session(self.repository.engine)
    stmt = select(Produto).where(Produto.id, id) # SELECT * FROM produto WHERE produto.id = id;
    resp = session.scalars(stmt).one()
    session.close()
    return resp

  def inserirProduto (self, produto):
    session = Session(self.repository.engine)
    session.add(produto) # INSERT INTO produto VALUES (ID = , QUANTIDADE =, DATA =, PRECO =, QUANTIDADE, );
    session.commit()
    session.close()

  def atualizarProduto (self, produto):    
    session = Session(self.repository.engine)
    stmt = select(Produto).where(Produto.id, id) # SELECT * FROM produto WHERE produto.id = id;
    produtoExiste = session.scalars(stmt).one()
    if (produtoExiste):
      produtoExiste.nome = produto.nome
      produtoExiste.descrição = produto.descricao
      produtoExiste.preco = produto.preco
      produtoExiste.quantidade = produto.quantidade
      session.commit() # UPDATE .... 
    session.close()
  
  def removerProdutoPorId (self, id):
    session = Session(self.repository.engine)
    produtoExiste = session.query(Produto).filter(Produto.id == 3).delete() # DELETE FROM produto WHERE produto.id = id;
    session.commit()