from pydantic import BaseModel, Field
from pydantic.types import AliasChoices
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
    # e.g. usuario_id | user_id, propiedad_id | property_id, cantidad_tokens | tokens, precio_unitario | price_per_token
    usuario_id: int = Field(validation_alias=AliasChoices("usuario_id", "user_id"))
    propiedad_id: int = Field(validation_alias=AliasChoices("propiedad_id", "property_id"))
    cantidad_tokens: int = Field(validation_alias=AliasChoices("cantidad_tokens", "tokens", "cantidad"))
    precio_unitario: Decimal = Field(validation_alias=AliasChoices("precio_unitario", "price_per_token", "precio"))

class TransactionResponse(BaseModel):
    status: str
    message: str
    cantidad_tokens: int
    propiedad_id: int
