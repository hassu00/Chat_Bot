import chainlit as cl
from main import run_agent

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello, I am a physics assistant. How can I help you today?").send()
@cl.on_message
async def on_message(message: cl.Message):
    # retrieve the history from the user session
    history = cl.user_session.get("history", [])
    # append the user message to the history
    history.append(f"user: {message.content}")
    # get the assistant's response
    response = await run_agent(message.content, history=history)
    # append the assistant's response to the history
    history.append(f"assistant: {response}")
    # update the user session with the new history
    await cl.Message(content=f"Received: {message.content}, Response: {response}").send()
