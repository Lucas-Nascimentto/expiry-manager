from ..repositories.user_repository import get_user_by_email
from ..extensions import bcrypt

def login_service(data):
    if "email" not in data or "password" not in data:
        raise ValueError("Email e senha são obrigatórios")

    user = get_user_by_email(data["email"])

    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        raise ValueError("Email ou senha inválidos")

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }