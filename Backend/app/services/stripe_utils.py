from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

def process_fake_payment(data: TransactionCreate, db: Session):
    transaction = Transaction(**data.dict(), status="SUCCESS")
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction
