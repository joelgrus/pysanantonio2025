import dspy

lm = dspy.LM(
    model="openai/gpt-5-mini", 
    temperature=1.0,
    max_tokens=16_000,    
    reasoning_effort="minimal"
)
dspy.configure(lm=lm)

reviews = [
    "I absolutely loved this movie! The plot was thrilling and the characters were so well developed.",
    "The movie was okay, not great but not terrible either. It had some good moments.",
    "I didn't like this movie at all. The story was boring and the acting was subpar."
]

signature = "review -> sentiment: Literal['Positive', 'Negative', 'Neutral']"

categorize = dspy.Predict(signature=signature)

for review in reviews:
    prediction = categorize(review=review)
    print(f"Review: {review}")
    print(f"Sentiment: {prediction.sentiment}\n")