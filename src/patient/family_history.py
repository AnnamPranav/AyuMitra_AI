from pydantic import BaseModel


class FamilyHistory(BaseModel):

    diabetes: bool = False

    hypertension: bool = False

    heart_disease: bool = False

    cancer: bool = False

    stroke: bool = False

    kidney_disease: bool = False

    genetic_disorders: bool = False

    notes: str = ""