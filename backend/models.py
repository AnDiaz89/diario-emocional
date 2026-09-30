from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    creado_en: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    entradas: Mapped[list["Entrada"]] = relationship(back_populates="usuario")


class Entrada(Base):
    __tablename__ = "entradas"

    id: Mapped[int] = mapped_column(primary_key=True)
    texto: Mapped[str] = mapped_column(Text)
    estado: Mapped[str] = mapped_column(String(20), default="pendiente")
    creado_en: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), index=True)
    usuario: Mapped["Usuario"] = relationship(back_populates="entradas")