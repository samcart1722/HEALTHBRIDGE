"""Password hashing utilities."""

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Return a bcrypt hash for a plain password."""
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """Validate a plain password against a stored bcrypt hash."""
    return pwd_context.verify(password, password_hash)
