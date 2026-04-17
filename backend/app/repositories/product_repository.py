from app.extensions import db
from app.models.product import Product

def create_product(data):
    product = Product(
        name=data["name"],
        category=data.get("category"),
        barcode=data.get("barcode")
    )
    db.session.add(product)
    db.session.commit()
    return product