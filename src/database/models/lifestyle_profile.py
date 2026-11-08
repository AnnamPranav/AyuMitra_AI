"""
AyuMitra Lifestyle Profile Model
"""

import uuid

from sqlalchemy import (
    Boolean,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class LifestyleProfile(Base):
    __tablename__ = "lifestyle_profiles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    patient_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("patients.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    occupation: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    smoking: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    alcohol: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    exercise_frequency: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
        comment="Days exercised per week",
    )

    sleep_hours: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    diet_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    water_intake: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
        comment="Liters per day",
    )

    activity_level: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    patient = relationship(
        "Patient",
        back_populates="lifestyle_profile",
    )