from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash-lite', # Find a model that exists and is not giving time out error
    contents='We have a small icecream shop in Minneapolis, a very local business. Our work hours during summer are from 9am to 9 pm and we always run out of product. During winter this change completly when we can ahve days with no clients. What strategies can we implement to keep the business and survive the winter time' # This is prompt
)

print(response.text)