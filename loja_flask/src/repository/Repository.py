from sqlalchemy import create_engine

from models.Base import Base

class Repository():
  def __init__ (self):
    self.engine = create_engine("sqlite:///loja.db", echo=True)
    Base.metadata.create_all(self.engine)

r = Repository()


