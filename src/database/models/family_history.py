"""
AyuMitra Family History Model
"""

import uuid

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class FamilyHistory(Base):
    __tablename__ = "family_histories"

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

    diabetes: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    hypertension: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    heart_disease: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    stroke: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    cancer: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    kidney_disease: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    genetic_disorders: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    other_notes: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    patient = relationship(
        "Patient",
        back_populates="family_history",
    )