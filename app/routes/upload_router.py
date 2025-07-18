from fastapi import APIRouter, Request
from app.utils.config import settings

router = APIRouter()

@router.post("/upload_file")
async def upload_router(request: Request):
    return {"message": "File uploaded successfully"}