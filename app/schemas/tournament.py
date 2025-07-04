from datetime import datetime
from typing import Any

from pydantic import BaseModel, EmailStr, Field, field_serializer, field_validator


class TournamentCreate(BaseModel):
    name: str = Field(..., description="Chess Cup")
    max_players: int = Field(..., ge=5, le=15, description="players count")
    start_time: datetime = Field(..., description="2025-07-04 12:10:32")

    @field_validator("start_time", mode="before")
    def parse_start_time(cls, value: str | datetime) -> datetime:
        if isinstance(value, str):
            # format: '2025-07-04 11:51:10'
            try:
                return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise ValueError("start_time must be in 'YYYY-MM-DD HH:MM:SS' format")
        return value


class TournamentRead(BaseModel):
    name: str
    max_players: int
    start_time: datetime

    @field_serializer("start_time", when_used="always")
    def serialize_start_time(self, dt: datetime, _info: Any) -> str:
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    class Config:
        from_attributes = True


class PlayerCreate(BaseModel):
    name: str = Field(..., description="John Doe")
    email: EmailStr = Field(..., description="john@example.com")


class PlayerRead(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
