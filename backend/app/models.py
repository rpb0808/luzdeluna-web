"""Modelos de datos (equivalen al schema.prisma anterior).

El nucleo del MVP confirmado: reservas y pagos de clases.
"""
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class RolUsuario(str, Enum):
    CLIENTE = "CLIENTE"
    INSTRUCTOR = "INSTRUCTOR"
    ADMIN = "ADMIN"


class EstadoReserva(str, Enum):
    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    COMPLETADA = "COMPLETADA"


class EstadoPago(str, Enum):
    PENDIENTE = "PENDIENTE"
    PAGADO = "PAGADO"
    FALLIDO = "FALLIDO"
    REEMBOLSADO = "REEMBOLSADO"


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str = Field(unique=True, index=True)
    password_hash: str
    telefono: Optional[str] = None
    rol: RolUsuario = Field(default=RolUsuario.CLIENTE)
    creado_en: datetime = Field(default_factory=datetime.utcnow)


class Caballo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    raza: Optional[str] = None
    activo: bool = Field(default=True)


class Disciplina(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True)  # Salto, Adiestramiento, Equinoterapia, Vaulting
    descripcion: Optional[str] = None


class Clase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    disciplina_id: int = Field(foreign_key="disciplina.id")
    caballo_id: Optional[int] = Field(default=None, foreign_key="caballo.id")
    instructor: str
    fecha_hora_ini: datetime
    fecha_hora_fin: datetime
    cupo_maximo: int = Field(default=1)
    precio: Decimal


class Reserva(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id")
    clase_id: int = Field(foreign_key="clase.id")
    estado: EstadoReserva = Field(default=EstadoReserva.PENDIENTE)
    creada_en: datetime = Field(default_factory=datetime.utcnow)


class Pago(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    reserva_id: int = Field(foreign_key="reserva.id", unique=True)
    monto: Decimal
    estado: EstadoPago = Field(default=EstadoPago.PENDIENTE)
    proveedor: Optional[str] = None  # ej. Stripe, Culqi, MercadoPago
    referencia_externa: Optional[str] = None
    creado_en: datetime = Field(default_factory=datetime.utcnow)
