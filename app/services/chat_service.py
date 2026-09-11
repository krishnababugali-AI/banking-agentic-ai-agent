from app.models.chat import ChatRequest, ChatResponse


async def process_chat(request: ChatRequest) -> ChatResponse:
    return ChatResponse(
        customer_id=request.customer_id,
        answer=f"Received your banking question: {request.message}",
        status="success",
    )