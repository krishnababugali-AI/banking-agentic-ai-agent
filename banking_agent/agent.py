import sys

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from mcp import StdioServerParameters


transaction_mcp = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command=sys.executable,
            args=["-m", "app.mcp.transaction_server"],
        )
    )
)


root_agent = Agent(
    name="banking_assistant",
    model="gemini-2.5-flash",
    description=(
        "A secure banking AI assistant that helps customers "
        "understand their banking information."
    ),
    instruction="""
You are a secure banking assistant.

Your responsibilities:
- Help customers with banking-related questions.
- When customer-specific transaction information is required,
  use the available transaction tool.
- Never invent transaction information.
- Use tool results as the source of truth for transaction data.
- Do not expose unnecessary sensitive information.
- Explain the result clearly and concisely.
""",
    tools=[
        transaction_mcp,
    ],
)