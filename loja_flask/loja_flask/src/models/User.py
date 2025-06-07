import sqlalchemy
from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin

class Base (DeclarativeBase):
  pass

class User (Base, UserMixin):

  __tablename__ = "user"

  id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] = mapped_column(String(), unique=True)
  password: Mapped[str] = mapped_column(String())
  name: Mapped[str] = mapped_column(String())

  is_authenticated = False # type: ignore
  is_active = True # type: ignore
  is_anonymous = False # type: ignore
  
  def get_id (self):
    return self.id

  def __repr__ (self):
    return str({ "id": self.id, "username": self.username, "password": self.password, "name": self.name })
