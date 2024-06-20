import chainlit as cl
import openai
import os

##chainlit run main.py -w
# os.environ['OPENAI_API_KEY'] = 'test'

@cl.on_message
async def main(message: str):
    await cl.message(content=message).send()