from pydantic import BaseModel, Field

from fastapi import APIRouter

router = APIRouter(prefix="/api/reservas", tags=["reservas"])

# Placeholder en memoria - se reemplaza por la base de datos (SQLModel) en el
# siguiente paso.
reservas: list[dict] = []


class CrearReserva(BaseModel):
    clase_id: str = Field(min_length=1)
    nombre_cliente: str = Field(min_length=2)


@router.get("/")
def listar_reservas():
    return reservas


@router.post("/", status_code=201)
def crear_reserva(datos: CrearReserva):
    nueva = {"id": str(len(reservas) + 1), **datos.model_dump()}
    reservas.append(nueva)
    return nueva
