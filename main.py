from agents import Agent,Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
import asyncio

import os


set_tracing_disabled(True)
load_dotenv(find_dotenv(),override=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")
gemine_model = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key=gemini_api_key,base_url=gemini_base_url)
model = OpenAIChatCompletionsModel(openai_client=client, model=str(gemine_model))


agent = Agent(
    name="Gemini Agent",
    instructions="An agent that uses Gemini to answer physics questions" 
        "You are a helpful assistant. Respond concisely and respectfully. "
        "You are participating in a continuous conversation with the user. "
        "Use prior messages to maintain context.",
    model=model
)

async def run_agent(prompt: str,history: list = None):
    history = history or []
    conversation = "\n".join(history + [f"user: {prompt}"])
    result = await Runner.run(agent, conversation)
    return result.final_output
