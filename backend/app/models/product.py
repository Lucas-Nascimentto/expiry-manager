from ..extensions import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100))
    barcode = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

