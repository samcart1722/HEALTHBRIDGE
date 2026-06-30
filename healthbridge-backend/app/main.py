"""FastAPI application entry point."""

from fastapi import FastAPI

from app.core.config import settings


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""
    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    @application.get("/", tags=["System"])
    def root() -> dict[str, str]:
        return {
            "project": settings.project_name,
            "version": settings.app_version,
            "status": "running",
        }

    return application


app = create_application()
