"""JWT helpers for authentication infrastructure."""

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt

from app.auth.schemas import TokenPayload
from app.core.config import settings


DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(
    subject: str,
    expires_delta: timedelta | None = None,
    extra_claims: dict[str, Any] | None = None,
) -> str:
    """Create a signed JWT access token."""
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    payload: dict[str, Any] = {"sub": subject, "exp": expire}

    if extra_claims:
        payload.update(extra_claims)

    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str) -> TokenPayload:
    """Decode and validate a JWT access token."""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError as exc:
        raise ValueError("Invalid access token") from exc

    subject = payload.get("sub")
    if subject is None:
        raise ValueError("Invalid access token payload")

    return TokenPayload(sub=str(subject), exp=payload.get("exp"))
