from pydantic import BaseModel


class HealthGoal(BaseModel):

    lose_weight: bool = False

    gain_weight: bool = False

    improve_sleep: bool = False

    reduce_blood_sugar: bool = False

    lower_cholesterol: bool = False

    lower_blood_pressure: bool = False

    improve_fitness: bool = False

    medication_adherence: bool = False

    custom_goal: str = ""