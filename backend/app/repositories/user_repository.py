from ..extensions import db, bcrypt
from ..models.user import User

def create_user(data):
    user = User(
        name=data["name"],
        email=data["email"],
        password=bcrypt.generate_password_hash(data["password"]).decode("utf-8")
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

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()