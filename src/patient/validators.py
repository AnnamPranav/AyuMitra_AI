"""
AyuMitra

Patient Validators

Centralized validation and utility functions for
patient-related data.

These validators are used across services,
APIs, and AI agents.
"""

from __future__ import annotations

import math
import re
from datetime import date
from typing import List, Optional


class PatientValidator:
    """
    Validation utilities for patient information.
    """

    PHONE_PATTERN = re.compile(r"^\+?[1-9]\d{7,14}$")

    @staticmethod
    def validate_age(age: int) -> bool:
        """Validate patient age."""
        return 0 <= age <= 120

    @staticmethod
    def validate_height(height_cm: float) -> bool:
        """Validate height in centimeters."""
        return 30 <= height_cm <= 300

    @staticmethod
    def validate_weight(weight_kg: float) -> bool:
        """Validate weight in kilograms."""
        return 1 <= weight_kg <= 500

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validate international phone number.

        Examples:
            +919876543210
            919876543210
        """
        return bool(PatientValidator.PHONE_PATTERN.match(phone))

    @staticmethod
    def validate_sleep(hours: float) -> bool:
        """Validate sleep hours."""
        return 0 <= hours <= 24

    @staticmethod
    def validate_water_intake(liters: float) -> bool:
        """Validate daily water intake."""
        return 0 <= liters <= 20

    @staticmethod
    def validate_steps(steps: int) -> bool:
        """Validate daily step count."""
        return 0 <= steps <= 100000

    @staticmethod
    def validate_stress_level(level: int) -> bool:
        """Validate stress level (1-10)."""
        return 1 <= level <= 10

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Basic email validation.

        Pydantic already validates emails, but this
        is useful in services or AI preprocessing.
        """
        return "@" in email and "." in email


class HealthCalculator:
    """
    Healthcare calculation utilities.
    """

    @staticmethod
    def calculate_bmi(
        height_cm: float,
        weight_kg: float,
    ) -> Optional[float]:
        """
        Calculate BMI.

        Formula:
            weight / (height in meters)^2
        """
        if height_cm <= 0 or weight_kg <= 0:
            return None

        height_m = height_cm / 100

        bmi = weight_kg / math.pow(height_m, 2)

        return round(bmi, 2)

    @staticmethod
    def bmi_category(bmi: float) -> str:
        """
        Return BMI category.
        """
        if bmi < 18.5:
            return "Underweight"

        if bmi < 25:
            return "Normal"

        if bmi < 30:
            return "Overweight"

        return "Obese"

    @staticmethod
    def calculate_age(date_of_birth: date) -> int:
        """
        Calculate age from date of birth.
        """
        today = date.today()

        age = (
            today.year
            - date_of_birth.year
            - (
                (today.month, today.day)
                < (date_of_birth.month, date_of_birth.day)
            )
        )

        return age


class ProfileValidator:
    """
    Validate profile completeness.
    """

    @staticmethod
    def profile_completion(profile: dict) -> float:
        """
        Calculate profile completion percentage.
        """

        if not profile:
            return 0.0

        total_fields = len(profile)

        completed_fields = sum(
            value not in (
                None,
                "",
                [],
                {},
            )
            for value in profile.values()
        )

        return round(
            (completed_fields / total_fields) * 100,
            2,
        )


class MedicationValidator:
    """
    Medication validation utilities.
    """

    @staticmethod
    def remove_duplicate_medications(
        medications: List[str],
    ) -> List[str]:
        """
        Remove duplicate medication names.
        """
        unique = []

        seen = set()

        for medicine in medications:

            normalized = medicine.strip().lower()

            if normalized not in seen:

                seen.add(normalized)

                unique.append(medicine.strip())

        return unique

    @staticmethod
    def has_medications(
        medications: List[str],
    ) -> bool:
        return len(medications) > 0


class GoalValidator:
    """
    Health goal validation.
    """

    @staticmethod
    def validate_goal(goal: str) -> bool:
        """
        Ensure goal text is meaningful.
        """
        return len(goal.strip()) >= 3