import os
import sys
import uuid
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from src.main import setup_adk, run_agent_query

app = FastAPI(title="MediGuide AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

_runner = None
_session_service = None

def get_runtime():
    global _runner, _session_service
    if _runner is None or _session_service is None:
        _runner, _session_service = setup_adk()
    return _runner, _session_service

@app.get("/")
async def root():
    return {
        "name": "MediGuide AI",
        "status": "running",
        "message": "Multi-agent healthcare navigation API",
    }

@app.get("/health")
async def health():
    return {"status": "ok", "service": "mediguide-ai"}

@app.post("/chat")
async def chat(
    query: str = Form(...),
    image: UploadFile | None = File(default=None),
):
    runner, session_service = get_runtime()
    user_id = f"user_{uuid.uuid4().hex[:12]}"
    session_id = f"session_{uuid.uuid4().hex[:12]}"

    await session_service.create_session(
        app_name="mediguide_ai",
        user_id=user_id,
        session_id=session_id,
    )

    image_path = None
    try:
        if image is not None:
            suffix = Path(image.filename or "upload.jpg").suffix or ".jpg"
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(await image.read())
                image_path = tmp.name

        response = await run_agent_query(
            runner=runner,
            session_service=session_service,
            user_id=user_id,
            session_id=session_id,
            query=query,
            image_path=image_path,
        )
        return {"status": "success", "response": response, "session_id": session_id}
    finally:
        if image_path:
            try:
                os.unlink(image_path)
            except OSError:
                pass
