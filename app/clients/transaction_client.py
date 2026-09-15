import asyncio
import logging


logger = logging.getLogger(__name__)


async def get_recent_transaction(customer_id: str) -> dict:
    logger.info(
        "Fetching recent transaction for customer_id=%s",
        customer_id,
    )

    # Simulates waiting for another microservice
    await asyncio.sleep(3)

    return {
        "transaction_id": "TXN-10001",
        "merchant": "Example Merchant",
        "amount": 149.00,
        "currency": "USD",
    }