"""User Pydantic schemas."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    """Base user schema shared by future user operations."""

    model_config = ConfigDict(from_attributes=True)

    email: str = Field(max_length=320)
    is_active: bool = True


class UserCreate(BaseModel):
    """Schema for creating a user."""

    email: str = Field(max_length=320)
    password: str = Field(min_length=8, max_length=128)


class UserRead(UserBase):
    """Schema for reading a user without sensitive fields."""

    id: UUID
    created_at: datetime
    updated_at: datetime
