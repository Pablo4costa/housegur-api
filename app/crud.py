from sqlalchemy import text
from .database import SessionLocal

def login_user(nombre: str, email: str):
    db = SessionLocal()
    try:
        db.execute(text("""
            INSERT INTO housegur.usuarios (nombre, email, password)
            VALUES (:nombre, :email, 'demo123')
            ON DUPLICATE KEY UPDATE nombre = VALUES(nombre);
        """), {"nombre": nombre, "email": email})
        db.commit()

        result = db.execute(text("""
            SELECT id AS usuario_id, nombre
            FROM housegur.usuarios
            WHERE email = :email;
        """), {"email": email}).fetchone()

        return {"status": "ok", "usuario_id": result.usuario_id, "nombre": result.nombre}
    finally:
        db.close()


def comprar_tokens(user_id: int, property_id: int, tokens: int):
    db = SessionLocal()
    try:
        db.execute(text("""
            CALL housegur.sp_comprar_tokens(:user_id, :property_id, :tokens, 0);
        """), {"user_id": user_id, "property_id": property_id, "tokens": tokens})
        db.commit()
        return {"status": "ok", "message": "Compra confirmada", "tokens": tokens, "propiedad_id": property_id}
    finally:
        db.close()


def vender_tokens(user_id: int, property_id: int, tokens: int):
    db = SessionLocal()
    try:
        db.execute(text("""
            CALL housegur.sp_vender_tokens(:user_id, :property_id, :tokens, 0);
        """), {"user_id": user_id, "property_id": property_id, "tokens": tokens})
        db.commit()
        return {"status": "ok", "message": "Venta confirmada", "tokens": tokens, "propiedad_id": property_id}
    finally:
        db.close()
