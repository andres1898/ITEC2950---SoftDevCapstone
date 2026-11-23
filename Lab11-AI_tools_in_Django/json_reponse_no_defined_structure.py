from google import genai
from google.genai.types import  GenerateContentConfig

client = genai.Client()

# AI model is free to interpreter the prompt so you will get different responses
response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents="""I have leftover chicken, cheese and broccoli. Suggest a quick recipe?""",
    config=GenerateContentConfig(
        response_mime_type="application/json",
    )
)
print(response.text)