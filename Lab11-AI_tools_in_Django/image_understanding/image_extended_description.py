from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel

client = genai.Client()

class Produce(BaseModel):
    name: str
    color: str
    fruit_or_veggie: str # the AI have to decide if is a fruit or veggie

with open('Stop&Shop.jpg', 'rb') as f:
    image_bytes = f.read() # this will save the image as information in each bite not the image per se

response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents=[ #the content is a list of text, each byte's information from the image
        types.Part.from_bytes(data=image_bytes, mime_type='image/jpg'),
        'What produce is in this picture?'
    ],
    config=GenerateContentConfig( # we use this field to specified what our output should look like
        system_instruction="""Identify produce items as you can, Include color and if it is a 'Fruit' or a 'Vegetable'""", #This extra instruction will help the agent to do a better job
        response_mime_type='application/json',
        response_schema=list[Produce] #this will return a list of produce
    )
)

print(response.parsed) #return the list object not the whole Json format

for produce_item in response.parsed:
    print(produce_item.name)