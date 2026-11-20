from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash-lite', # Find a model that exists and is not giving time out error
    contents='What are the top 5 music artist in the US?' # This is prompt
)

print(response.text)