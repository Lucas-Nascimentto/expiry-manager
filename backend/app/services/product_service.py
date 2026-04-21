from ..repositories.product_repository import create_product, get_all_products, get_product_by_id, update_product, delete_product

def create_product_service(data):
    if "name" not in data:
        raise ValueError("Nome é obrigatório")
    if "category" not in data:
        raise ValueError("Categoria é obrigatória")
    if "barcode" not in data:
        raise ValueError("Código de barras é obrigatório")

    return create_product(data)

def get_all_products_service():
    products = get_all_products()
    return [
        {
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "barcode": p.barcode
        } 
        for p in products
    ]

def get_product_service(id):
    product = get_product_by_id(id)
    if not product:
        raise ValueError("Produto não encontrado")
    return {
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "barcode": product.barcode
    }

def update_product_service(id, data):
    product = get_product_by_id(id)
    if not product:
        raise ValueError("Produto não encontrado")
    product = update_product(product, data)
    return {
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "barcode": product.barcode
    }

def delete_product_service(id):
    product = get_product_by_id(id)
    if not product:
        raise ValueError("Produto não encontrado")

    delete_product(product)