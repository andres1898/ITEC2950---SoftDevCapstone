from google import genai
import rich
from google.genai.types import GenerateContentConfig
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-3.5-flash-lite')

while True:
    response = chat.send_message(
    """Write a program to calculate the area of a circle""",
    config=GenerateContentConfig( # set the behavior of the AI agent
        system_instruction="""You are a helpful programming tutor for a Java introduction class. You can explain but 
        not give straight answers"""
    )
    )
    rich.print(Markdown(response.text))