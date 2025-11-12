from pydantic import BaseModel
from decimal import Decimal

class LoginRequest(BaseModel):
    nombre: str
    email: str

class LoginResponse(BaseModel):
    status: str
    usuario_id: int
    nombre: str

class TransactionRequest(BaseModel):
    usuario_id: int
    propiedad_id: int
    cantidad_tokens: int
    precio_unitario: Decimal

class TransactionResponse(BaseModel):
    status: str
    message: str
    cantidad_tokens: int
    propiedad_id: int
