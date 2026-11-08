"""
Patient Profile Service

Handles CRUD operations for patient profiles.
"""

from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session, joinedload

from src.database.models.patient import Patient
from src.patient.schemas import (
    PatientCreateRequest,
    PatientUpdate,
    PatientResponse,
)


class PatientService:
    """Business logic for Patient operations."""

    def __init__(self, db: Session):
        self.db = db

    # ------------------------------------------------------------------
    # Create
    # ------------------------------------------------------------------

    def create_patient(self, patient_data: PatientCreate) -> Patient:
        """Create a new patient."""

        existing_email = (
            self.db.query(Patient)
            .filter(Patient.email == patient_data.email)
            .first()
        )

        if existing_email:
            raise ValueError("Patient with this email already exists.")

        if hasattr(patient_data, "phone"):
            existing_phone = (
                self.db.query(Patient)
                .filter(Patient.phone == patient_data.phone)
                .first()
            )

            if existing_phone:
                raise ValueError("Patient with this phone number already exists.")

        try:
            patient = Patient(**patient_data.model_dump())

            self.db.add(patient)
            self.db.commit()
            self.db.refresh(patient)

            return patient

        except Exception:
            self.db.rollback()
            raise

    # ------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------

    def get_patient_by_id(self, patient_id: UUID) -> Patient | None:
        """Get patient by UUID."""

        query = self.db.query(Patient)

        # Load relationships if they exist
        if hasattr(Patient, "medical_profile"):
            query = query.options(joinedload(Patient.medical_profile))

        if hasattr(Patient, "lifestyle_profile"):
            query = query.options(joinedload(Patient.lifestyle_profile))

        if hasattr(Patient, "family_history"):
            query = query.options(joinedload(Patient.family_history))

        if hasattr(Patient, "emergency_contact"):
            query = query.options(joinedload(Patient.emergency_contact))

        if hasattr(Patient, "health_goals"):
            query = query.options(joinedload(Patient.health_goals))

        return (
            query.filter(Patient.id == patient_id)
            .first()
        )

    def get_patient(self, patient_id: UUID) -> Patient | None:
        """Alias for get_patient_by_id()."""
        return self.get_patient_by_id(patient_id)

    def get_patient_by_email(self, email: str) -> Patient | None:
        """Get patient using email."""

        return (
            self.db.query(Patient)
            .filter(Patient.email == email)
            .first()
        )

    def list_patients(
        self,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Patient]:
        """Return all patients."""

        return (
            self.db.query(Patient)
            .offset(skip)
            .limit(limit)
            .all()
        )

    # ------------------------------------------------------------------
    # Update
    # ------------------------------------------------------------------

    def update_patient(
        self,
        patient_id: UUID,
        patient_data: PatientUpdate,
    ) -> Patient:
        """Update patient."""

        patient = self.get_patient_by_id(patient_id)

        if patient is None:
            raise ValueError("Patient not found.")

        update_data = patient_data.model_dump(exclude_unset=True)

        try:
            for field, value in update_data.items():
                setattr(patient, field, value)

            self.db.commit()
            self.db.refresh(patient)

            return patient

        except Exception:
            self.db.rollback()
            raise

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------

    def delete_patient(self, patient_id: UUID) -> bool:
        """Delete patient."""

        patient = self.get_patient_by_id(patient_id)

        if patient is None:
            return False

        try:
            self.db.delete(patient)
            self.db.commit()

            return True

        except Exception:
            self.db.rollback()
            raise

    # ------------------------------------------------------------------
    # BMI
    # ------------------------------------------------------------------

    @staticmethod
    def calculate_bmi(
        height_cm: float,
        weight_kg: float,
    ) -> dict:
        """
        Calculate BMI.

        Args:
            height_cm: Height in centimeters
            weight_kg: Weight in kilograms
        """

        if height_cm <= 0:
            raise ValueError("Height must be greater than zero.")

        height_m = height_cm / 100

        bmi = weight_kg / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return {
            "bmi": round(bmi, 2),
            "category": category,
        }

    # ------------------------------------------------------------------
    # Profile Completion
    # ------------------------------------------------------------------

    @staticmethod
    def profile_completion(patient: Patient) -> dict:
        """
        Calculate profile completion percentage.
        """

        total_sections = 6
        completed_sections = 0

        # Personal Information
        if patient.first_name and patient.last_name:
            completed_sections += 1

        # Medical Profile
        if getattr(patient, "medical_profile", None):
            completed_sections += 1

        # Lifestyle Profile
        if getattr(patient, "lifestyle_profile", None):
            completed_sections += 1

        # Family History
        if getattr(patient, "family_history", None):
            completed_sections += 1

        # Emergency Contact
        if getattr(patient, "emergency_contact", None):
            completed_sections += 1

        # Health Goals
        health_goals = getattr(patient, "health_goals", None)

        if health_goals:
            if len(health_goals) > 0:
                completed_sections += 1

        percentage = round(
            (completed_sections / total_sections) * 100,
            2,
        )

        return {
            "completed_sections": completed_sections,
            "total_sections": total_sections,
            "completion_percentage": percentage,
        }