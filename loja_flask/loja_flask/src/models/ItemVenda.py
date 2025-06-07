from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import List

from models.Base import Base
from models.Produto import Produto

class Venda (Base):

  __tablename__ = "item_venda"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  usuario_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
  venda_id: Mapped[DateTime] = mapped_column(DateTime())
  produto_id: Mapped[int] = mapped_column(ForeignKey("produto.id"), )
  quantidade: Mapped[int] = mapped_column()
  preco_unitario: Mapped[float] = mapped_column(float(), unique=False)
  def __repr__ (self):
    return str({"id": self.id, "quantidade": self.quantidade, "data_venda": self.data_venda,
                "produto_id": self.produto_id})