from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from models.Base import Base

class Categorias (Base):

  __tablename__ = "categorias"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  nome: Mapped[String] = mapped_column(String())
  descricao: Mapped[String] = mapped_column(String())
  codigo: Mapped[Float] = mapped_column(Float())
  produtos: Mapped[int] = mapped_column(ForeignKey("produtos.id"))