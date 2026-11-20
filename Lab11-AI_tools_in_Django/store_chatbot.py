from google import genai
import rich
from google.genai.types import GenerateContentConfig
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-3.5-flash-lite')

while True:
    question = input('Message for Louis ')
    response = chat.send_message(
        question,
        config=GenerateContentConfig( # set the behavior of the AI agent
        system_instruction="""You are Louis, the chatbot for this company Lucky Number Clothing.
        You are a young, active, on trend chatbot. You are always upbeat, helpful and happy. Your job is to help
        customers find the perfect style and size in our cloth"""
        )
    )
    rich.print(Markdown(response.text))