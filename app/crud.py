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


def get_user_holdings(usuario_id: int):
    db = SessionLocal()
    try:
        result = db.execute(text("""
            SELECT 
                p.id as propiedad_id,
                p.titulo,
                p.ciudad,
                p.precio_token,
                p.moneda,
                SUM(CASE WHEN t.tipo='COMPRA' THEN t.cantidad_tokens ELSE -t.cantidad_tokens END) as tokens_owned
            FROM housegur.transacciones t
            JOIN housegur.propiedades p ON t.propiedad_id = p.id
            WHERE t.usuario_id = :usuario_id
            GROUP BY p.id, p.titulo, p.ciudad, p.precio_token, p.moneda
            HAVING tokens_owned > 0
            ORDER BY p.id;
        """), {"usuario_id": usuario_id})
        
        holdings = []
        for row in result:
            valor_actual = Decimal(str(row.tokens_owned)) * row.precio_token
            holdings.append({
                "propiedad_id": row.propiedad_id,
                "titulo": row.titulo,
                "ciudad": row.ciudad,
                "tokens_owned": row.tokens_owned,
                "precio_token": row.precio_token,
                "valor_actual": valor_actual,
                "moneda": row.moneda
            })
        
        return holdings
    finally:
        db.close()
