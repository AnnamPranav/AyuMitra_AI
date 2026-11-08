from datetime import datetime

from pydantic import BaseModel, Field


class Metadata(BaseModel):

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)

    last_login: datetime | None = None

    last_profile_update: datetime | None = None

    profile_completion: float = 0.0

    profile_version: str = "1.0.0"