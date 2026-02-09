"""DevOps Assistant - Chainlit App. Run with: chainlit run app.py"""

import chainlit as cl
from agents import Runner, set_default_openai_key
from config import get_config
from agent_defs import devops_triage_agent
from utils.logging import get_logger

logger = get_logger(__name__)

def _ensure_config():
    cfg = get_config()
    set_default_openai_key(cfg["openai_api_key"])
    return cfg

@cl.on_chat_start
async def on_chat_start():
    try:
        _ensure_config()
        cl.user_session.set("chat_history", None)
        await cl.Message(content="**DevOps Assistant** - CI/CD, ticket escalation, developer productivity. Ask about build failures, PR status, or productivity tips.", author="DevOps").send()
    except ValueError as e:
        await cl.Message(content="Configuration Error: " + str(e), author="System").send()
        raise

@cl.on_message
async def on_message(message: cl.Message):
    user_content = message.content.strip()
    if not user_content:
        await cl.Message(content="Please describe your DevOps question.", author="DevOps").send()
        return
    try:
        _ensure_config()
        logger.info("Processing: %s", user_content[:80])
        result = await Runner.run(devops_triage_agent, input=user_content)
        await cl.Message(content=result.final_output, author="DevOps").send()
        logger.info("Response sent")
    except Exception:
        logger.exception("Query failed")
        await cl.Message(content="Something went wrong. Please try again.", author="DevOps").send()
