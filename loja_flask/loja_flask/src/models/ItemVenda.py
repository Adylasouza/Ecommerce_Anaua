from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Float
from typing import List

from models.Base import Base
from models.Produto import Produto

class ItemVenda (Base):

    __tablename__ = "itens_venda"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    venda_id: Mapped[int] = mapped_column(ForeignKey("vendas.id"))
    quantidade: Mapped[int] = mapped_column()
    preco_unitario: Mapped[Float] = mapped_column(Float())
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id"))

    def __repr__ (self):
        return str({"id": self.id, "quantidade": self.quantidade, "venda_id": self.venda_id,
                "produto_id": self.produto_id, "preco_unitario": self.preco_unitario})