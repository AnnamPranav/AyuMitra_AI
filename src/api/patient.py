from fastapi import APIRouter
from uuid import UUID

from fastapi import HTTPException
from fastapi import status

from src.services.patient_service import PatientService

router = APIRouter()



@router.get("/")
async def test():
    return {
        "message": "Patient API is working"
    }

patient_service = PatientService()
@router.get("/{patient_id}")
def get_patient(patient_id: UUID):
    patient = patient_service.get_patient(patient_id)

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    return {
        "success": True,
        "message": "Patient retrieved successfully",
        "data": patient
    }