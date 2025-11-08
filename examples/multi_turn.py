from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "developer", 
        "content": (
            "You are the organizer of a Python conference. "
            "Your only goal is to get people to attend. "
            "Everything you say should be in pursuit of that goal."
        )
    }
]

while True:
    user_input = input("User: ")

    messages.append({
        "role": "user",
        "content": user_input
    })

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
    )

    assistant_message = completion.choices[0].message
    print(f"\nAssistant: {assistant_message.content}\n")

    messages.append({
        "role": "assistant",
        "content": assistant_message.content
    })
