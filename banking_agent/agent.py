from google.adk.agents import Agent

from app.tools.transaction_tools import get_recent_transaction


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
- Help customers understand banking-related information.
- Use available tools when customer-specific data is required.
- Never invent customer transaction information.
- If transaction information is required, use the appropriate tool.
- Explain results clearly and concisely.
- Do not expose unnecessary sensitive customer information.
""",

    tools=[
        get_recent_transaction,
    ],
)