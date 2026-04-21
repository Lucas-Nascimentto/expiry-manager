from ..repositories.batch_repository import create_batch, get_batch_by_id, get_all_batches, update_batch, delete_batch

def create_batch_service(data):
    if "product_id" not in data:
        raise ValueError("ID do produto é obrigatório")
    if "quantity" not in data:
        raise ValueError("Quantidade é obrigatória")
    if "expiration_date" not in data:
        raise ValueError("Data de expiração é obrigatória")
    batch = create_batch(data)
    return {
        "id": batch.id,
        "product_id": batch.product_id,
        "quantity": batch.quantity,
        "expiration_date": batch.expiration_date
    }

def get_batch_service(id):
    batch = get_batch_by_id(id)
    if not batch:
        raise ValueError("Batch não encontrado")
    return {
        "id": batch.id,
        "product_id": batch.product_id,
        "quantity": batch.quantity,
        "expiration_date": batch.expiration_date
    }

def get_all_batches_service():
    batches = get_all_batches()
    return [
        {
            "id": batch.id,
            "product_id": batch.product_id,
            "quantity": batch.quantity,
            "expiration_date": batch.expiration_date
        }
        for batch in batches
    ]

def update_batch_service(id, data):
    batch = get_batch_by_id(id)
    if not batch:
        raise ValueError("Batch não encontrado")
    batch = update_batch(batch, data)
    return {
        "id": batch.id,
        "product_id": batch.product_id,
        "quantity": batch.quantity,
        "expiration_date": batch.expiration_date
    }

def delete_batch_service(id):
    batch = get_batch_by_id(id)
    if not batch:
        raise ValueError("Batch não encontrado")
    delete_batch(batch)