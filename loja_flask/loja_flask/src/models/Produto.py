from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.Base import Base

class Produto (Base):

  __tablename__ = "produto"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  nome: Mapped[String] = mapped_column(String())
  descricao: Mapped[String] = mapped_column(String())
  preco: Mapped[Float] = mapped_column(Float())
  estoque: Mapped[int] = mapped_column(nullable=False, default=0)
  foto_url: Mapped[String] = mapped_column(String())
  categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"), nullable=False)


  def __repr__ (self):
    return str ({"id": self.id, "nome": self.nome, "descricao": self.descricao, 
                  "preco": self.preco, "estoque": self.estoque, "foto_url": self.foto_url, "categoria_id": self.categoria_id })