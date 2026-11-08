"""
AyuMitra Patient ORM Model
"""

import uuid
from datetime import date, datetime

from sqlalchemy import Date, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from src.database.base import Base


class Patient(Base):
    __tablename__ = "patients"

    # Primary Key
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Personal Information
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)

    last_name: Mapped[str] = mapped_column(String(100), nullable=False)

    date_of_birth: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    gender: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    blood_group: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )

    preferred_language: Mapped[str] = mapped_column(
        String(30),
        default="English",
    )

    profile_photo: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # Metadata
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationships
    medical_profile = relationship(
        "MedicalProfile",
        back_populates="patient",
        uselist=False,
        cascade="all, delete-orphan",
    )

    lifestyle_profile = relationship(
        "LifestyleProfile",
        back_populates="patient",
        uselist=False,
        cascade="all, delete-orphan",
    )

    family_history = relationship(
        "FamilyHistory",
        back_populates="patient",
        uselist=False,
        cascade="all, delete-orphan",
    )

    emergency_contact = relationship(
        "EmergencyContact",
        back_populates="patient",
        uselist=False,
        cascade="all, delete-orphan",
    )

    health_goals = relationship(
        "HealthGoal",
        back_populates="patient",
        cascade="all, delete-orphan",
    )

    family_history = relationship(
    "FamilyHistory",
    back_populates="patient",
    uselist=False,
    cascade="all, delete-orphan",
    )

    health_goals = relationship(
    "HealthGoal",
    back_populates="patient",
    cascade="all, delete-orphan",
    )

    emergency_contact = relationship(
    "EmergencyContact",
    back_populates="patient",
    uselist=False,
    cascade="all, delete-orphan",
    )