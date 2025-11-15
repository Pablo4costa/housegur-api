from pydantic import BaseModel, Field
from decimal import Decimal

class LoginRequest(BaseModel):
    nombre: str
    email: str

class LoginResponse(BaseModel):
    status: str
    usuario_id: int
    nombre: str

class TransactionRequest(BaseModel):
    # Accept both English (from legacy frontend) and Spanish field names
    usuario_id: int = Field(alias="user_id")
    propiedad_id: int = Field(alias="property_id")
    cantidad_tokens: int = Field(alias="tokens")
    precio_unitario: Decimal

class TransactionResponse(BaseModel):
    status: str
    message: str
    cantidad_tokens: int
    propiedad_id: int

class HoldingResponse(BaseModel):
    propiedad_id: int
    titulo: str
    ciudad: str
    tokens_owned: int
    precio_token: Decimal
    valor_actual: Decimal
    moneda: str
