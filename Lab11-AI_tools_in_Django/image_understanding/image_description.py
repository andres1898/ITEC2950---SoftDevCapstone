from google import genai
from google.genai import types

client = genai.Client()

with open('emoji-overload.png', 'rb') as f:
    image_bytes = f.read() # this will save the image as information in each bite not the image per se

response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents=[ #the content is a list of text, each byte's information from the image
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpg'), #data description
        'What is this a picture of?' #the prompt
    ]
)

print(response.text)