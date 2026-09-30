from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings

# El "motor": la conexion central con PostgreSQL
engine = create_engine(settings.database_url)

# Fabrica de sesiones: cada peticion HTTP usara una sesion propia
SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    """Clase madre de todos los modelos (tablas). La heredaran en el siguiente paso."""
    pass


def get_db():
    """Presta una sesion de BD y la cierra al terminar (pase lo que pase)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()