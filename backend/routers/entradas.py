from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from database import get_db
from models import Entrada
from schemas.entradas import EntradaCrear, EntradaRespuesta

router = APIRouter(prefix="/entradas", tags=["Entradas"])

# TEMPORAL: hasta la Fase 3 (login), todas las entradas seran del usuario 1
USUARIO_TEMPORAL = 1


@router.post("/", response_model=EntradaRespuesta, status_code=201)
def crear_entrada(datos: EntradaCrear, db: Session = Depends(get_db)):
    entrada = Entrada(texto=datos.texto, usuario_id=USUARIO_TEMPORAL)
    db.add(entrada)
    db.commit()
    db.refresh(entrada)
    return entrada


@router.get("/", response_model=list[EntradaRespuesta])
def listar_entradas(db: Session = Depends(get_db)):
    return db.scalars(select(Entrada).order_by(Entrada.creado_en.desc())).all()


@router.get("/{entrada_id}", response_model=EntradaRespuesta)
def obtener_entrada(entrada_id: int, db: Session = Depends(get_db)):
    entrada = db.get(Entrada, entrada_id)
    if entrada is None:
        raise HTTPException(status_code=404, detail="Entrada no encontrada")
    return entrada