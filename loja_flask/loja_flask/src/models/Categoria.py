from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from models.Base import Base

class Categoria(Base):

    __tablename__ = 'categorias'
    
    id = Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[String] = mapped_column(String())
    descricao: Mapped[String] = mapped_column(String())
    codigo = Mapped[String] = mapped_column(String())
    produtos = Mapped[int] = mapped_column(ForeignKey("produto.id"))

def __repr__ (self):
    return str ({"id": self.id, "nome": self.nome, "descricao": self.descricao, 
                 "codigo": self.preco})
