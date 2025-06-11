from fastapi import FastAPI
from app.api import auth, fake_payment  # ✅ include fake_payment here
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import base, engine
from app.models.User import User
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Create DB tables
base.metadata.create_all(bind=engine)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(fake_payment.router, prefix="/fake-payment", tags=["Fake Payment"])  # ✅ Add this line

@app.get("/")
def home():
    return {"message": "API is live"}
