from pydantic import BaseModel, Field


class SecurityContext(BaseModel):
    user_id: str = Field(min_length=1)
    customer_id: str = Field(min_length=1)
    roles: list[str] = []
    scopes: list[str] = []