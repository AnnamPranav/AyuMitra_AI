"""
AyuMitra Database Models

Import all SQLAlchemy ORM models so they are registered with SQLAlchemy's
metadata. This is required for Alembic migrations and table creation.
"""

from .patient import Patient
from .medical_profile import MedicalProfile
from .lifestyle_profile import LifestyleProfile
from .family_history import FamilyHistory
from .health_goal import HealthGoal
from .emergency_contact import EmergencyContact


__all__ = [
    "Patient",
    "MedicalProfile",
    "LifestyleProfile",
    "FamilyHistory",
    "HealthGoal",
    "EmergencyContact",
]