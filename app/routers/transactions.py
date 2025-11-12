from fastapi import APIRouter
from app.schemas import TransactionRequest, TransactionResponse
from app.crud import comprar_tokens, vender_tokens

router = APIRouter()

@router.post("/buy", response_model=TransactionResponse)
def buy_tokens(req: TransactionRequest):
    return comprar_tokens(req.usuario_id, req.propiedad_id, req.cantidad_tokens, req.precio_unitario)

@router.post("/sell", response_model=TransactionResponse)
def sell_tokens(req: TransactionRequest):
    return vender_tokens(req.usuario_id, req.propiedad_id, req.cantidad_tokens, req.precio_unitario)
