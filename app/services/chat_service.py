import asyncio
import logging

from app.clients.transaction_client import get_recent_transaction
from app.models.chat import ChatRequest, ChatResponse


logger = logging.getLogger(__name__)

TRANSACTION_TIMEOUT_SECONDS = 2.0


async def process_chat(request: ChatRequest) -> ChatResponse:
    try:
        transaction = await asyncio.wait_for(
            get_recent_transaction(request.customer_id),
            timeout=TRANSACTION_TIMEOUT_SECONDS,
        )

    except TimeoutError:
        logger.warning(
            "Transaction service timed out"
        )

        return ChatResponse(
            customer_id=request.customer_id,
            answer="Transaction information is temporarily unavailable.",
            status="error",
        )

    answer = (
        f"Your recent transaction was "
        f"${transaction['amount']:.2f} "
        f"at {transaction['merchant']}."
    )

    return ChatResponse(
        customer_id=request.customer_id,
        answer=answer,
        status="success",
    )