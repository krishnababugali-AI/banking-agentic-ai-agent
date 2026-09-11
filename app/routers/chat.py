from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_chat


router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"],
)


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return await process_chat(request)