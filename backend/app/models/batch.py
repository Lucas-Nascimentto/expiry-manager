from app.extensions import db

class Batch(db.Model):
    __tablename__ = "batches"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())