from fastapi import APIRouter
from sqlalchemy import text
from app.database import SessionLocal

router = APIRouter()

@router.get("/")
def get_properties():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT id, nombre, tokens_disponibles, precio_token FROM housegur.propiedades;"))
        return [dict(row._mapping) for row in result]
    finally:
        db.close()
