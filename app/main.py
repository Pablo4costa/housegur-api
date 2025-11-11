from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from sqlalchemy import text
from app.routers import auth, properties, transactions
from app.database import SessionLocal
import logging

# Configure logging
logger = logging.getLogger(__name__)

app = FastAPI(title="HOUSEGUR API v1.0")

# =====================
# Handle CORS preflight (OPTIONS) globally
# =====================
@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    """Handle CORS preflight OPTIONS requests."""
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS, PATCH",
            "Access-Control-Allow-Headers": "Content-Type, Authorization, Accept",
            "Access-Control-Max-Age": "3600",
        },
    )

# =====================
# CORS Configuration
# =====================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "*",  # Allow all origins for testing
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================
# Startup Events
# =====================
@app.on_event("startup")
def startup_db_check():
    """Test MySQL connection on app startup."""
    try:
        db = SessionLocal()
        # Try a simple query to verify connection
        db.execute(text("SELECT 1"))
        db.close()
        logger.info("[DB] ✅ Connected successfully to Railway MySQL")
        print("[DB] ✅ Connected successfully to Railway MySQL")
    except Exception as e:
        logger.error(f"[DB] ❌ Connection error: {str(e)}")
        print(f"[DB] ❌ Connection error: {str(e)}")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(properties.router, prefix="/properties", tags=["Properties"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])

@app.get("/")
def root():
    return {"message": "HOUSEGUR API is running 🚀"}

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "API is healthy"}
