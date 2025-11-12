from sqlalchemy import text
from decimal import Decimal
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


def comprar_tokens(usuario_id: int, propiedad_id: int, cantidad_tokens: int, precio_unitario: Decimal):
    db = SessionLocal()
    try:
        db.execute(text("""
            CALL housegur.sp_comprar_tokens(:usuario_id, :propiedad_id, :cantidad_tokens, :precio_unitario);
        """), {
            "usuario_id": usuario_id,
            "propiedad_id": propiedad_id,
            "cantidad_tokens": cantidad_tokens,
            "precio_unitario": precio_unitario
        })
        db.commit()
        return {
            "status": "ok",
            "message": "Compra confirmada",
            "cantidad_tokens": cantidad_tokens,
            "propiedad_id": propiedad_id
        }
    finally:
        db.close()


def vender_tokens(usuario_id: int, propiedad_id: int, cantidad_tokens: int, precio_unitario: Decimal):
    db = SessionLocal()
    try:
        db.execute(text("""
            CALL housegur.sp_vender_tokens(:usuario_id, :propiedad_id, :cantidad_tokens, :precio_unitario);
        """), {
            "usuario_id": usuario_id,
            "propiedad_id": propiedad_id,
            "cantidad_tokens": cantidad_tokens,
            "precio_unitario": precio_unitario
        })
        db.commit()
        return {
            "status": "ok",
            "message": "Venta confirmada",
            "cantidad_tokens": cantidad_tokens,
            "propiedad_id": propiedad_id
        }
    finally:
        db.close()
