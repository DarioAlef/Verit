import uvicorn
from fastapi import FastAPI
from app.utils.config import settings
from app.routes import upload_router

app = FastAPI(title=settings.project_name)
app.include_router(upload_router.router)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.fast_api_port,
        reload=True
    )