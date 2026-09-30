from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/registro")
def registro():
    return {"mensaje": "Registro: en construccion (Fase 3)"}


@router.post("/login")
def login():
    return {"mensaje": "Login: en construccion (Fase 3)"}