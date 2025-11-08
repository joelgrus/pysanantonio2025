import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


reviews = [
    "I absolutely loved this movie! The plot was thrilling and the characters were so well developed.",
    "The movie was okay, not great but not terrible either. It had some good moments.",
    "I didn't like this movie at all. The story was boring and the acting was subpar."
]

instructions = """
I am going to give you a movie review.
I need you to categorize it as Positive, Negative, or Neutral.
Please just respond with one of those three words.
"""

def categorize(review: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=instructions,
        input=review
    )
    return response.output_text.strip()


for review in reviews:
    category = categorize(review)
    print(f"Review: {review}\nCategory: {category}\n")