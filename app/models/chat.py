from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    customer_id: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Unique customer identifier",
    )

    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Customer banking question",
    )


class ChatResponse(BaseModel):
    customer_id: str
    answer: str
    status: str