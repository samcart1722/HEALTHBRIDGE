"""User domain services."""

from sqlalchemy.orm import Session

from app.auth.security import hash_password
from app.users.models import User
from app.users.repositories import user_repository


class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user with an existing email."""


def create_user(db: Session, email: str, password: str) -> User:
    """Create a user after enforcing domain rules."""
    existing_user = user_repository.get_by_email(db, email)
    if existing_user is not None:
        raise UserAlreadyExistsError("A user with this email already exists.")

    user = User(email=email, password_hash=hash_password(password))
    return user_repository.create(db, user)
