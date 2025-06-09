from models import db
from models.User import User
from werkzeug.security import generate_password_hash

class UserService:
    def listarUsers(self):
        return [u.to_dict() for u in User.query.all()]

    def listarUserPorId(self, id):
        user = User.query.get(id)
        return user.to_dict() if user else None

    def listarUserPorUsername(self, username):
        user = User.query.filter_by(username=username).first()
        return user.to_dict() if user else None

    def inserirUser(self, data_dict):
        try:
            user = User(
                username=data_dict['username'],
                password_hash=generate_password_hash(data_dict['password']),
                name=data_dict.get('name', '')
            )
            db.session.add(user)
            db.session.commit()
            return user.id
        except Exception as e:
            db.session.rollback()
            raise e

    def atualizarUser(self, id, data_dict):
        try:
            user = User.query.get(id)
            if user:
                user.username = data_dict['username']
                if 'password' in data_dict:
                    user.password_hash = generate_password_hash(data_dict['password'])
                user.name = data_dict.get('name', user.name)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e

    def removerUserPorId(self, id):
        try:
            user = User.query.get(id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e