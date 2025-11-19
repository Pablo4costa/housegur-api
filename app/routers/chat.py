from fastapi import APIRouter
from app.schemas import ChatMessageRequest, ChatMessageResponse, ChatHistorialItem
from app.crud import guardar_mensaje_chat, obtener_historial_chat
from typing import List

router = APIRouter()

@router.post("/guardar", response_model=ChatMessageResponse)
def guardar_chat(req: ChatMessageRequest):
    """Guardar un mensaje de chat en el historial."""
    return guardar_mensaje_chat(
        req.usuario_id,
        req.tipo_mensaje,
        req.contenido,
        req.respuesta_asistente,
        req.accion_realizada
    )

@router.get("/historial", response_model=List[ChatHistorialItem])
def get_historial(user_id: int, limit: int = 50, offset: int = 0):
    """Obtener historial de conversaciones del usuario."""
    return obtener_historial_chat(user_id, limit, offset)
