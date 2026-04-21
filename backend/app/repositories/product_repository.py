from ..extensions import db
from ..models.product import Product

def create_product(data):
    product = Product(
        name=data["name"],
        category=data.get("category"),
        barcode=data.get("barcode")
    )
    db.session.add(product)
    db.session.commit()
    return product

def get_all_products():
    products = Product.query.all()
    return products

def get_product_by_id(id):
    return Product.query.get(id)

def update_product(product, data):
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.barcode = data.get("barcode", product.barcode)
    db.session.commit()
    return product

def delete_product(product):
    db.session.delete(product)
    db.session.commit()