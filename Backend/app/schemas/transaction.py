from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionCreate(BaseModel):
    user_id: Optional[int]
    amount: float
    description: Optional[str]

class TransactionOut(TransactionCreate):
    id: int
    status: str
    timestamp: datetime

    class Config:
        orm_mode = True
