from sqlalchemy import select
from sqlalchemy.orm import Session
from models.Categoria import Categoria
from repository.Repository import Repository

class CategoriaService ():

  def __init__(self):
    self.repository = Repository ()

  #CRUD de categorias

  def listarCategoria (self):
    session = Session(self.repository.engine)
    stmt = select(Categoria) # SELECT * FROM categorias;
    listResp = session.scalars(stmt).all()
    session.close()
    return listResp

  def listarCategoriaPorId (self, id):
    session = Session(self.repository.engine)
    stmt = select(Categoria).where(Categoria.id, id) # SELECT * FROM categorias WHERE categoria.id = id;
    resp = session.scalars(stmt).one()
    session.close()
    return resp

  def inserirCategoria (self, categorias):
    session = Session(self.repository.engine)
    session.add(categorias) # INSERT INTO categorias VALUES (ID = , QUANTIDADE =, DATA =, PRECO =, QUANTIDADE, );
    session.commit()
    session.close()

  def atualizarCategoria (self, categorias):    
    session = Session(self.repository.engine)
    stmt = select(Categoria).where(Categoria.id, id) # SELECT * FROM categorias WHERE categorias.id = id;
    categoriasExiste = session.scalars(stmt).one()
    if (categoriasExiste):
      categoriasExiste.nome = categorias.nome
      categoriasExiste.descricao = categorias.descricao
      categoriasExiste.codigo = categorias.codigo
      categoriasExiste.produtos = categorias.produtos
      session.commit() # UPDATE .... 
    session.close()
  
  def removerCategoriaPorId (self, id):
    session = Session(self.repository.engine)
    produtoExiste = session.query(Categoria).filter(Categoria.id == 3).delete() # DELETE FROM categorias WHERE categorias.id = id;
    session.commit()