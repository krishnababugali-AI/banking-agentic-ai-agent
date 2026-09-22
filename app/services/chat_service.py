import logging

from app.auth.security_context import SecurityContext
from app.models.chat import ChatRequest, ChatResponse
from app.services.agent_service import run_banking_agent


logger = logging.getLogger(__name__)


async def process_chat(
    request: ChatRequest,
    security_context: SecurityContext,
) -> ChatResponse:

    answer = await run_banking_agent(
        user_id=security_context.user_id,
        message=request.message,
    )

    return ChatResponse(
        customer_id=security_context.customer_id,
        answer=answer,
        status="success",
    )