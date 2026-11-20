from google import genai
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_name: str
    ingredient: list[str]
    instructions: list[str]

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents="""I have leftover chicken, cheese and broccoli. Suggest a quick recipe?""",
    config=GenerateContentConfig(
        system_instruction='Include US and metric units',
        response_mime_type='application/json',
        response_schema=Recipe
    )
)
print(response.text)

recipe = response.parsed #make the json response into an object
print(recipe.ingredient)

for ingredient in recipe.ingredient:
    print(ingredient)