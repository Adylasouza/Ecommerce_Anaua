from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from models.Base import Base

class Produto (Base):

  __tablename__ = "produto"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  nome: Mapped[String] = mapped_column(String())
  descricao: Mapped[String] = mapped_column(String())
  preco: Mapped[Float] = mapped_column(Float())
  quantidade: Mapped[int] = mapped_column()

  def __repr__ (self):
    return str ({"id": self.id, "nome": self.nome, "descricao": self.descricao, 
                 "preco": self.preco, "quantidade": self.quantidade })