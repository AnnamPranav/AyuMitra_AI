from pydantic import BaseModel

from .enums import Language


class Preferences(BaseModel):

    language: Language = Language.ENGLISH

    notifications_enabled: bool = True

    reminder_time: str = "09:00"

    measurement_system: str = "metric"

    dark_mode: bool = False

    accessibility_mode: bool = False