"""
AyuMitra Health Goal Model
"""

import uuid
from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class HealthGoal(Base):
    __tablename__ = "health_goals"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    patient_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("patients.id", ondelete="CASCADE"),
        nullable=False,
    )

    goal_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    target_value: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    target_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="In Progress",
        nullable=False,
    )

    patient = relationship(
        "Patient",
        back_populates="health_goals",
    )