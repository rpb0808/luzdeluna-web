# Luz de Luna Centro Ecuestre — Web + App

Pagina web / aplicacion web para el centro ecuestre Luz de Luna (Club Hipico
- La Molina, Lima), con reservas y pagos online como nucleo del MVP.

Estado del arte y decisiones de producto: ver el documento del proyecto
"Pagina con aplicacion web" (carpeta `claude/estado-del-arte-resumen.md` y
`claude/plan-tecnico.md`).

## Stack

- **Frontend:** Next.js 14 + TypeScript + Tailwind CSS (obligatorio: es lo
  que corre en el navegador)
- **Backend:** Python + FastAPI, modelos y validacion con SQLModel/Pydantic
- **Base de datos:** PostgreSQL
- **Todo corre en contenedores** con Docker Compose (`postgres`, `backend`,
  `frontend`)

## Como levantar el proyecto (con Docker Desktop abierto)

1. Copia `.env.example` como `.env` en la raiz del proyecto:
   ```
   cp .env.example .env
   ```
   (en Windows, desde PowerShell: `Copy-Item .env.example .env`)
2. En la raiz del proyecto, corre:
   ```
   docker compose up --build
   ```
3. Abre:
   - Frontend: http://localhost:3000
   - Backend (health check): http://localhost:4000/api/health/
   - Documentacion automatica de la API (FastAPI): http://localhost:4000/docs

La primera vez tarda varios minutos (descarga imagenes e instala
dependencias). Las siguientes veces es mucho mas rapido.

Para apagar todo: `docker compose down` (o `Ctrl+C` y luego `docker compose down`).

## Estructura

```
.
├── backend/     API en FastAPI (Python), puerto 4000
├── frontend/    Sitio en Next.js, puerto 3000
└── docker-compose.yml
```

## Estado actual (MVP en construccion)

- [x] Estructura base del proyecto con Docker
- [x] Modelos de base de datos iniciales (usuarios, caballos, clases,
      disciplinas, reservas, pagos) en `backend/app/models.py`
- [x] Endpoint de reservas de prueba (`POST /api/reservas/`), aun en memoria
- [ ] Conectar los endpoints a PostgreSQL con SQLModel (de verdad, no en memoria)
- [ ] Autenticacion de usuarios (registro / login)
- [ ] Pasarela de pagos online
- [ ] Portal de cliente (historial de clases y pagos)
- [ ] Panel de administracion para instructores

## Seguridad (buenas practicas ya aplicadas / pendientes)

- [x] CORS configurado en el backend (solo permite el frontend conocido)
- [x] Limite de peticiones (`rate limiting`) contra abuso
- [x] Validacion de datos de entrada con Pydantic
- [x] Secretos fuera del codigo (`.env`, nunca se sube a git)
- [ ] Hasheo de contrasenas (passlib/bcrypt) al implementar autenticacion
- [ ] HTTPS/TLS en produccion (se configura al desplegar)
