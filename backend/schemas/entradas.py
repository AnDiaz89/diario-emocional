from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class EntradaCrear(BaseModel):
    """Lo que el usuario envia al escribir en su diario."""
    texto: str = Field(min_length=1, max_length=5000)


class EntradaRespuesta(BaseModel):
    """Lo que la API devuelve."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    texto: str
    estado: str
    creado_en: datetime