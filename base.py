"""Shared SQLAlchemy declarative base."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class reserved for future ORM models."""

    pass


from app.users.models import User  # noqa: E402,F401
