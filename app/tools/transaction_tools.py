def get_recent_transaction(customer_id: str) -> dict:
    """
    Get the most recent transaction for a banking customer.

    Args:
        customer_id: Unique identifier of the banking customer.

    Returns:
        The customer's most recent transaction.
    """

    return {
        "customer_id": customer_id,
        "transaction_id": "TXN-10001",
        "merchant": "Amazon",
        "amount": 149.00,
        "currency": "USD",
        "status": "completed",
    }