from fastapi import APIRouter
from app.schemas import LoginRequest, LoginResponse
from app.crud import login_user

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest):
    return login_user(req.nombre, req.email)
