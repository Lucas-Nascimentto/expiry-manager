from app.repositories.product_repository import create_product

def create_product_service(data):
    if "name" not in data:
        raise ValueError("Nome é obrigatório")

    return create_product(data)