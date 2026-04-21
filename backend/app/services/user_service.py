from ..repositories.user_repository import create_user, get_user_by_id, update_user, delete_user

def create_user_service(data):
    if "name" not in data:
        raise ValueError("Name é obrigatório")
    if "email" not in data:
        raise ValueError("Email é obrigatório")
    if "password" not in data:
        raise ValueError("Password é obrigatório")

    return create_user(data)

def update_user_service(user_id, data):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("Usuário não encontrado") 
    
    return update_user(user, data)

def delete_user_service(user_id):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("Usuário não encontrado")
    delete_user(user)