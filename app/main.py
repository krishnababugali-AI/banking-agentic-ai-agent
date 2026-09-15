from fastapi import FastAPI

from app.core.config import settings
from app.core.exceptions import global_exception_handler
from app.core.logging import configure_logging
from app.middleware.request_context import request_context_middleware
from app.routers.chat import router as chat_router


configure_logging()


app = FastAPI(
    title=settings.app_name,
    description="Backend API for the Banking Agentic AI Assistant",
    version=settings.app_version,
)


app.add_exception_handler(
    Exception,
    global_exception_handler,
)

app.middleware("http")(request_context_middleware)

app.include_router(chat_router)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": settings.app_name,
        "environment": settings.app_env,
    }

@app.get("/test-error")
async def test_error():
    raise RuntimeError("Database password=super-secret")