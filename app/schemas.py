from pydantic import BaseModel

class LoginRequest(BaseModel):
    nombre: str
    email: str

class LoginResponse(BaseModel):
    status: str
    usuario_id: int
    nombre: str

class TransactionRequest(BaseModel):
    user_id: int
    property_id: int
    tokens: int

class TransactionResponse(BaseModel):
    status: str
    message: str
    tokens: int
    propiedad_id: int
