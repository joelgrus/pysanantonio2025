from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system", 
            "content": (
                "You are puro San Antonio. "
                "Answer questions from that perspective."
            )
        },
        {
            "role": "user",
            "content": (
                "I am driving on the freeway. "
                "Do I need to secure the items in the back of my truck?"
            )
        },
    ],
)

print(completion.choices[0].message.content)