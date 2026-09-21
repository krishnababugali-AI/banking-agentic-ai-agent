from decimal import Decimal

from app.models.transaction.models import TransactionResult


async def get_recent_transaction(
    customer_id: str,
) -> TransactionResult:
    """
    Retrieve the most recent transaction for a customer.

    Development implementation.
    A repository/database will replace the hardcoded data later.
    """

    return TransactionResult(
        transaction_id="TXN-10001",
        customer_id=customer_id,
        merchant="Amazon",
        amount=Decimal("149.00"),
        currency="USD",
        status="completed",
    )