from typing import Optional

from pydantic import BaseModel

from .enums import ActivityLevel, AlcoholStatus, DietType, SmokingStatus


class LifestyleProfile(BaseModel):

    occupation: Optional[str] = None

    smoking: SmokingStatus = SmokingStatus.NEVER

    alcohol: AlcoholStatus = AlcoholStatus.NEVER

    exercise_frequency: Optional[int] = None

    sleep_hours: Optional[float] = None

    diet_type: DietType = DietType.OMNIVORE

    water_intake_liters: Optional[float] = None

    stress_level: Optional[int] = None

    average_steps: Optional[int] = None

    activity_level: ActivityLevel = ActivityLevel.MODERATE