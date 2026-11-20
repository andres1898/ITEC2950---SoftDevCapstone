from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash-lite', # Find a model that exists and is not giving time out error
    contents='We are a small local business that owns a food truck, we need to came up with a plan to '
             'survive winter time in Minnesota. Last year we work with at least 10 companies to offer '
             'lunch on friday out in their parking lot, we barely made our budget and had to cut back on '
             'our staff hours. Two years ago we focus on catering, we offer our staff hours as server and prep cooks.'
             'Some of the people being asking for merch but we are not sure where to start and also we want to be '
             'more present in festivals and events'
    # This is prompt
)

print(response.text)