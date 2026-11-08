from typing import Optional

from pydantic import BaseModel, EmailStr


class EmergencyContact(BaseModel):

    name: str

    relationship: str

    phone_number: str

    email: Optional[EmailStr] = None