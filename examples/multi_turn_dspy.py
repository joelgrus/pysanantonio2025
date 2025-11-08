import dspy

lm = dspy.LM(
    model="openai/gpt-4.1-mini", 
    reasoning_effort="minimal"
)
dspy.configure(lm=lm)


class Signature(dspy.Signature):
    """
    You are the organizer of a Python conference.
    Your only goal is to get people to attend.
    Everything you say should be in pursuit of that goal.   
    """
    conversation_history: list = dspy.InputField()
    response: str = dspy.OutputField()

ask = dspy.Predict(signature=Signature)

messages = []

while True:
    user_input = input("User: ")

    messages.append({"role": "user", "content": user_input})
    prediction = ask(conversation_history=messages)
    response = prediction.response
    messages.append({"role": "assistant", "content": response})

    print(f"\nAssistant: {response}\n")