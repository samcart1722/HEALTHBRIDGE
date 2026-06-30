"""Persistence operations for users."""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.users.models import User


def get_by_id(db: Session, user_id: UUID) -> User | None:
    """Return a user by primary key."""
    return db.get(User, user_id)


def get_by_email(db: Session, email: str) -> User | None:
    """Return a user by email."""
    statement = select(User).where(User.email == email)
    return db.scalar(statement)


def create(db: Session, user: User) -> User:
    """Persist and return a new user."""
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
