from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from banking_agent.agent import root_agent


APP_NAME = "banking_agentic_ai"

session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)


async def run_banking_agent(
    user_id: str,
    message: str,
) -> str:
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
    )

    user_message = types.Content(
        role="user",
        parts=[
            types.Part(text=message)
        ],
    )

    final_response = None

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session.id,
        new_message=user_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response = event.content.parts[0].text

    if final_response is None:
        return "I couldn't generate a response."

    return final_response