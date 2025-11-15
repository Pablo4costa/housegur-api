from fastapi import APIRouter
from app.schemas import TransactionRequest, TransactionResponse, HoldingResponse
from app.crud import comprar_tokens, vender_tokens, get_user_holdings
from typing import List

router = APIRouter()

@router.post("/buy", response_model=TransactionResponse)
def buy_tokens(req: TransactionRequest):
    return comprar_tokens(req.usuario_id, req.propiedad_id, req.cantidad_tokens, req.precio_unitario)

@router.post("/sell", response_model=TransactionResponse)
def sell_tokens(req: TransactionRequest):
    return vender_tokens(req.usuario_id, req.propiedad_id, req.cantidad_tokens, req.precio_unitario)

@router.get("/holdings", response_model=List[HoldingResponse])
def get_holdings(user_id: int):
    return get_user_holdings(user_id)
