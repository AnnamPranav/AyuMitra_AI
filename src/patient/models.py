"""
AyuMitra
Patient Domain Models

This module aggregates all patient-related domain models
into a single context object that is shared with the AI agents.
"""

from pydantic import BaseModel

from .patient import Patient
from .medical_profile import MedicalProfile
from .lifestyle_profile import LifestyleProfile
from .family_history import FamilyHistory
from .health_goal import HealthGoal
from .emergency_contact import EmergencyContact
from .preferences import Preferences
from .metadata import Metadata


class PatientContext(BaseModel):
    """
    Complete patient context.

    This object is passed to the Orchestrator Agent so every
    AI agent has access to the same patient information.
    """

    patient: Patient

    medical_profile: MedicalProfile

    lifestyle_profile: LifestyleProfile

    family_history: FamilyHistory

    health_goal: HealthGoal

    emergency_contact: EmergencyContact

    preferences: Preferences

    metadata: Metadata