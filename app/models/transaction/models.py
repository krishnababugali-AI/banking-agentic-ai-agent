from decimal import Decimal

from pydantic import BaseModel


class TransactionResult(BaseModel):
    transaction_id: str
    customer_id: str
    merchant: str
    amount: Decimal
    currency: str
    status: str