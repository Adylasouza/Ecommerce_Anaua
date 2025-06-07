from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import User
from flask_login import LoginManager
from repository import repository

class UserService:
    
    def __init__ (self):
        self.engine = repository().engine # type: ignore

    def get_all_users (self):
        session = Session (self.engine)
        stmt = select(User)
        userList = session.scalars(stmt).all()
        session.close()
        return userList

    def get_user_by_id (self, id):
        session = Session (self.engine)
        stmt = select(User).where(User.id == id)
        user = session.scalars(stmt).one()
        session.close()
        return user

    def get_user_by_username (self, username):
        session = Session (self.engine)
        stmt = select(User).where(User.username == username)
        user = session.scalars(stmt).one()
        session.close()
        return user

    def create_user (self, user):
            session = Session (self.engine)
            newUser = user (
            username = user.username,
            password = user.password,
            name = user.name,
        )
            session.add(newUser)
            session.close()


def update_user (self, user):
     session = Session (self.engine)
     user_exists = self.get_user_by_id (User.id)
     if (user_exists is not None):
          user_exists.User.username = user.username
          user_exists.User.password = user.password
          user_exists.User.name = user.name
    session.close()

#explicação

def update_user (self, user):
     session = Session (self.engine)
     user_exists = self.get_user_by_id (User.id)
     if (user_exists is not None):
          user_exists.User.username = user.username
          user_exists.User.password = user.password
          user_exists.User.name = user.name
    session.close()