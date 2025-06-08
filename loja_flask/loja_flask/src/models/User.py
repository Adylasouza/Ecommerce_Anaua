import sqlalchemy
from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin

class Base (DeclarativeBase):
    pass

class User (Base, UserMixin):

    _tablename_ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(), unique=True)
    password: Mapped[str] = mapped_column(String())
    name: Mapped[str] = mapped_column(String())
    endereco: Mapped[str] = mapped_column(String())
    telefone: Mapped[str] = mapped_column(String())

    is_authenticated = False 
    is_active = True 
    is_anonymous = False 

    def get_id (self):
        return self.id

    def _repr_ (self):
        return str({ "id": self.id, "email": self.email, "password": self.password, "name": self.name
                    , "endereco": self.endereco, "telefone": self.telefone})
