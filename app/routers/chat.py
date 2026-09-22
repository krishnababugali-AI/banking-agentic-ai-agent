from fastapi import APIRouter, Depends

from app.auth.dependencies import get_security_context
from app.auth.security_context import SecurityContext
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_chat


router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
    security_context: SecurityContext = Depends(
        get_security_context
    ),
):
    return await process_chat(
        request,
        security_context,
    )