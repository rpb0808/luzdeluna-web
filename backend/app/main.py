import logging

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from app.database import crear_tablas
from app.routers import health, reservas

load_dotenv()
logger = logging.getLogger("luzdeluna")

app = FastAPI(title="Luz de Luna API")

# --- Seguridad basica ---
# CORS: en desarrollo se permite el frontend local; en produccion se
# restringe al dominio real del sitio.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Limite de peticiones para evitar abuso (fuerza bruta, scraping, etc.)
limiter = Limiter(key_func=get_remote_address, default_limits=["300/15minutes"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# --- Rutas ---
app.include_router(health.router)
app.include_router(reservas.router)


@app.on_event("startup")
def on_startup():
    try:
        crear_tablas()
    except Exception as exc:  # la base de datos puede no estar lista aun
        logger.warning("No se pudieron crear las tablas todavia: %s", exc)


@app.exception_handler(404)
async def not_found_handler(_request: Request, _exc):
    return JSONResponse(status_code=404, content={"error": "Ruta no encontrada"})
