from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.User import User
from src.repository.Repository import Repository

class UserService:
    
    def __init__(self):
        self.engine = Repository().engine

    # LISTAR TODOS OS USUÁRIOS
    def get_all_users(self):
        session = Session(self.engine)
        stmt = select(User)
        userList = session.scalars(stmt).all()
        session.close()
        return userList

    # LISTAR USUÁRIO POR ID
    def get_user_by_id(self, id):
        session = Session(self.engine)
        stmt = select(User).where(User.id == id)
        user = session.scalars(stmt).first()
        session.close()
        return user

    # LISTAR USUÁRIO POR USERNAME
    def get_user_by_username(self, username):
        session = Session(self.engine)
        stmt = select(User).where(User.username == username)
        user = session.scalars(stmt).first()
        session.close()
        return user

    # INSERIR NOVO USUÁRIO
    def create_user(self, data_dict):
        session = Session(self.engine)
        try:
            new_user = User(
                username=data_dict['username'],
                password=data_dict['password'],
                name=data_dict.get('name', ''),
                is_authenticated=False,
                is_active=True,
                is_anonymous=False
            )
            session.add(new_user)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # ATUALIZAR USUÁRIO EXISTENTE
    def update_user(self, data_dict):
        session = Session(self.engine)
        try:
            user_exists = self.get_user_by_id(data_dict['id'])
            if user_exists:
                user_exists.username = data_dict['username']
                user_exists.password = data_dict['password']
                user_exists.name = data_dict.get('name', user_exists.name)
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
