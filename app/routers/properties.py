from fastapi import APIRouter
from sqlalchemy import text
from app.database import SessionLocal

router = APIRouter()

@router.get("/", include_in_schema=True)
@router.get("", include_in_schema=False)
def get_properties():
    """Get all properties with their details."""
    db = SessionLocal()
    try:
        result = db.execute(text("""
            SELECT 
                id, 
                ciudad, 
                tipo, 
                titulo, 
                m2, 
                rentabilidad_objetivo, 
                precio_token, 
                total_tokens, 
                tokens_disponibles, 
                riesgo, 
                estado, 
                url, 
                moneda
            FROM housegur.propiedades
            ORDER BY id;
        """))
        return [dict(row._mapping) for row in result]
    finally:
        db.close()
