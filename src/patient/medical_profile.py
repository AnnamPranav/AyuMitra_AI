from typing import List, Optional

from pydantic import BaseModel, Field


class MedicalProfile(BaseModel):

    height_cm: Optional[float] = Field(None, gt=30, lt=300)

    weight_kg: Optional[float] = Field(None, gt=1, lt=500)

    bmi: Optional[float] = None

    known_conditions: List[str] = []

    allergies: List[str] = []

    current_medications: List[str] = []

    past_surgeries: List[str] = []

    vaccinations: List[str] = []

    disabilities: List[str] = []

    organ_donor: bool = False

    primary_physician: Optional[str] = None