from sqlalchemy import DateTime, ForeignKey, Float, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import List

from models.Base import Base
from models.Produto import Produto

class Venda (Base):

  __tablename__ = "venda"

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
  valor_total: Mapped[Float] = mapped_column(Float(), nullable=False)
  data_venda: Mapped[DateTime] = mapped_column(DateTime())
  forma_pagamento: Mapped[String] = mapped_column(String(), nullable=False)

  def __repr__ (self):
    return str({"id": self.id, "usuaio_id": self.usuario_id, "data_venda": self.data_venda,
                "valor_total": self.valor_total, "forma_pagamento": self.forma_pagamento})
  