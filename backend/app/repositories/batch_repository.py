from ..extensions import db
from ..models.batch import Batch

def create_batch(data):
    batch = Batch(
        product_id=data["product_id"],
        quantity=data["quantity"],
        expiration_date=data["expiration_date"]
    )
    db.session.add(batch)
    db.session.commit()
    return batch

def get_batch_by_id(id):
    return Batch.query.get(id)

def get_all_batches():
    return Batch.query.all()

def update_batch(batch, data):
    batch.product_id = data.get("product_id", batch.product_id)
    batch.quantity = data.get("quantity", batch.quantity)
    batch.expiration_date = data.get("expiration_date", batch.expiration_date)
    db.session.commit()
    return batch

def delete_batch(batch):
    db.session.delete(batch)
    db.session.commit()