"""Environment-based application settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    project_name: str = "HealthBridge"
    app_name: str = "HealthBridge API"
    app_version: str = "1.0.0"
    environment: str = "development"
    debug: bool = True

    database_url: str = (
        "postgresql+psycopg://healthbridge:healthbridge@localhost:5432/healthbridge"
    )
    database_echo: bool = False

    secret_key: str = "change_me"
    algorithm: str = "HS256"


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance."""
    return Settings()


settings = get_settings()
