import os

from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://luzdeluna:cambia_esta_clave@postgres:5432/luzdeluna"
)

# echo=False en produccion; ponlo en True si necesitas ver el SQL que se ejecuta
engine = create_engine(DATABASE_URL, echo=False)


def crear_tablas() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
