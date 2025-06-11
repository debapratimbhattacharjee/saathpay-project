from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.session import base

class Transaction(base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)  # Optional: tie to logged-in user
    amount = Column(Float, nullable=False)
    status = Column(String, default="SUCCESS")
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
