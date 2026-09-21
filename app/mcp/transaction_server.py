from mcp.server import MCPServer

from app.models.transaction.models import TransactionResult
from app.services.transaction.service import get_recent_transaction


mcp = MCPServer(
    name="transaction-mcp-server",
)


@mcp.tool()
async def fetch_recent_transaction(
    customer_id: str,
) -> TransactionResult:
    """
    Retrieve the most recent transaction for a banking customer.

    Args:
        customer_id: Unique identifier for the banking customer.

    Returns:
        The customer's most recent transaction information.
    """

    return await get_recent_transaction(customer_id)


if __name__ == "__main__":
    mcp.run()