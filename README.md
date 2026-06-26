# HealthBridge Backend

Estructura inicial del backend de HealthBridge construida con FastAPI,
PostgreSQL y SQLAlchemy 2.

Esta etapa contiene únicamente infraestructura y organización modular. No
incluye endpoints, modelos ORM, autenticación ni funcionalidades médicas.

## Estructura

```text
healthbridge-backend/
├── app/
│   ├── appointments/
│   ├── auth/
│   ├── consultations/
│   ├── core/
│   │   └── config.py
│   ├── database/
│   │   ├── base.py
│   │   └── session.py
│   ├── doctors/
│   ├── logistics/
│   ├── notifications/
│   ├── patients/
│   ├── payments/
│   ├── pharmacy/
│   ├── prescriptions/
│   ├── users/
│   └── main.py
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

Cada directorio de dominio es un paquete Python aislado y está preparado para
incorporar sus propias capas en fases posteriores.

## Requisitos

- Python 3.13
- PostgreSQL
- Docker, opcional

## Ejecución local

1. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Copia la configuración de ejemplo:

   ```bash
   cp .env.example .env
   ```

4. Ajusta `DATABASE_URL` y ejecuta la aplicación:

   ```bash
   uvicorn app.main:app --reload
   ```

La documentación interactiva estará disponible en `/docs`, aunque permanecerá
vacía hasta que se implementen rutas en una fase posterior.

## Docker

```bash
docker build -t healthbridge-backend .
docker run --rm -p 8000:8000 --env-file .env healthbridge-backend
```

El contenedor espera que la base de datos indicada en `DATABASE_URL` sea
accesible desde su red.
