"""Authentication Pydantic schemas."""

from pydantic import BaseModel


class AccessToken(BaseModel):
    """Serialized access token response shape."""

    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Decoded JWT payload used by authentication dependencies."""

    sub: str
    exp: int | None = None
