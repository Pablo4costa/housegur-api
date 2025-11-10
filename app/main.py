from fastapi import FastAPI
from app.routers import auth, properties, transactions

app = FastAPI(title="HOUSEGUR API v1.0")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(properties.router, prefix="/properties", tags=["Properties"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])

@app.get("/")
def root():
    return {"message": "HOUSEGUR API is running 🚀"}
