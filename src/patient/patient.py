from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field

from .enums import BloodGroup, Gender, Language


class Patient(BaseModel):
    patient_id: UUID = Field(default_factory=uuid4)

    first_name: str
    last_name: str

    date_of_birth: date
    age: int = Field(ge=0, le=120)

    gender: Gender

    email: EmailStr

    phone_number: str

    blood_group: Optional[BloodGroup] = None

    preferred_language: Language = Language.ENGLISH

    profile_photo: Optional[str] = None

    emergency_contact_id: Optional[UUID] = None