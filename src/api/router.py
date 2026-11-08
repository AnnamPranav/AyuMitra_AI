from fastapi import APIRouter

from src.api.patient import router as patient_router

router = APIRouter()

router.include_router(
    patient_router,
    prefix="/patients",
    tags=["Patients"]
)