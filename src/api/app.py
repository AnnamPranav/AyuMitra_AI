from fastapi import FastAPI

from src.api.router import router as api_router

app = FastAPI(
    title="AyuMitra API",
    version="1.0.0",
    description="Patient Profile APIs"
)

app.include_router(api_router)