from fastapi import FastAPI

from app.routers.chat import router as chat_router


app = FastAPI(
    title="Banking Agentic AI API",
    description="Backend API for the Banking Agentic AI Assistant",
    version="1.0.0",
)


app.include_router(chat_router)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "banking-agentic-ai-api",
    }