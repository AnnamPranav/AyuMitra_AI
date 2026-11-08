"""
AyuMitra Medical Profile ORM Model
"""

import uuid

from sqlalchemy import Float, ForeignKey, JSON, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class MedicalProfile(Base):
    __tablename__ = "medical_profiles"

    # Primary Key
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Relationship
    patient_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("patients.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    # Basic Health Information
    height_cm: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    weight_kg: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    bmi: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    blood_pressure: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    heart_rate: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    oxygen_saturation: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    body_temperature: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # Medical History
    allergies: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    known_conditions: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    current_medications: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    surgeries: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    vaccinations: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    disabilities: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    primary_physician: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    # ORM Relationship
    patient = relationship(
        "Patient",
        back_populates="medical_profile",
    )