from enum import Enum


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    PREFER_NOT_TO_SAY = "Prefer not to say"


class BloodGroup(str, Enum):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"


class Language(str, Enum):
    ENGLISH = "English"
    TELUGU = "Telugu"
    HINDI = "Hindi"


class SmokingStatus(str, Enum):
    NEVER = "Never"
    FORMER = "Former"
    OCCASIONAL = "Occasional"
    REGULAR = "Regular"


class AlcoholStatus(str, Enum):
    NEVER = "Never"
    OCCASIONAL = "Occasional"
    REGULAR = "Regular"


class DietType(str, Enum):
    VEGETARIAN = "Vegetarian"
    VEGAN = "Vegan"
    OMNIVORE = "Omnivore"


class ActivityLevel(str, Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"