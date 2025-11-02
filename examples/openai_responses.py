import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-5-mini",
    reasoning={"effort": "minimal"},
    instructions=(
        "You are puro San Antonio. "
        "Answer questions from that perspective."
    ),
    input=(
        "I am driving on the freeway. "
        "Do I need to secure the items in the back of my truck?"
    )
)

print(response.output_text)