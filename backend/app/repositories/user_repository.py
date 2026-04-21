from ..extensions import db
from ..models.user import User

def create_user(data):
    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"]
    )
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_id(user_id):
    return User.query.get(user_id)

def update_user(user, data):
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.password = data.get("password", user.password)
    db.session.commit()
    return user

def delete_user(user):
    db.session.delete(user)
    db.session.commit()