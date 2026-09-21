import anyio

from mcp import Client, StdioServerParameters


server = StdioServerParameters(
    command="python",
    args=["-m", "app.mcp.transaction_server"],
)


async def main() -> None:
    async with Client(server) as client:

        # 1. Discover tools exposed by the MCP server.
        tools_result = await client.list_tools()

        print("\nAvailable MCP tools:")

        for tool in tools_result.tools:
            print(f"- {tool.name}")

        # 2. Invoke the transaction tool.
        result = await client.call_tool(
            "fetch_recent_transaction",
            {
                "customer_id": "CUST-1001",
            },
        )

        
        print("\nMCP call result:")
        print("is_error:", result.is_error)
        print("content:", result.content)
        print("structured_content:", result.structured_content)


if __name__ == "__main__":
    anyio.run(main)