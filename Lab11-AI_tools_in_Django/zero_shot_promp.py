from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash-lite', # Find a model that exists and is not giving time out error
    contents='We are a small local business that owns a food truck, we need to came up with a plan to survive winter time in Minnesota' # This is prompt
)

print(response.text)