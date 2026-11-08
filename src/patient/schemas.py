"""
AyuMitra

Patient API Schemas

These schemas are used by FastAPI endpoints.

They define the request and response payloads.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from .models import PatientContext


# ----------------------------
# Create Patient
# ----------------------------

class PatientCreateRequest(BaseModel):

    patient: PatientContext


class PatientCreateResponse(BaseModel):

    success: bool

    message: str

    patient_id: UUID


# ----------------------------
# Get Patient
# ----------------------------

class PatientResponse(BaseModel):

    success: bool

    patient: PatientContext


# ----------------------------
# Update Patient
# ----------------------------

class PatientUpdateRequest(BaseModel):

    patient: PatientContext


class PatientUpdateResponse(BaseModel):

    success: bool

    message: str


# ----------------------------
# Delete Patient
# ----------------------------

class PatientDeleteResponse(BaseModel):

    success: bool

    message: str


# ----------------------------
# Timeline
# ----------------------------

class TimelineEvent(BaseModel):

    title: str

    description: str

    timestamp: datetime

    event_type: str


class TimelineResponse(BaseModel):

    success: bool

    events: list[TimelineEvent]


# ----------------------------
# Health Goals
# ----------------------------

class HealthGoalResponse(BaseModel):

    success: bool

    goals: list[str]


# ----------------------------
# API Status
# ----------------------------

class APIResponse(BaseModel):

    success: bool

    message: str