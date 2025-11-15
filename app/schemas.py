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
    # Accept both Spanish canonical names and common frontend variants
    usuario_id: int = Field(validation_alias="user_id")
    propiedad_id: int = Field(validation_alias="property_id")
    cantidad_tokens: int = Field(validation_alias="tokens")
    precio_unitario: Decimal = Field(validation_alias="price_per_token")

class TransactionResponse(BaseModel):
    status: str
    message: str
    cantidad_tokens: int
    propiedad_id: int
