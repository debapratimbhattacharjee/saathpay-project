from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.services.stripe_utils import process_fake_payment
from app.models.transaction import Transaction

router = APIRouter(
    prefix="/fake-payment",
    tags=["Fake Payment"]
)

@router.post("/pay", response_model=TransactionOut)
def fake_pay(data: TransactionCreate, db: Session = Depends(get_db)):
    return process_fake_payment(data, db)

@router.get("/transactions", response_model=list[TransactionOut])
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()
