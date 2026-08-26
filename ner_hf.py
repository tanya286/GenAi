from huggingface_hub import InferenceClient
client = InferenceClient(token="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")
result= client.token_classification(
    "During her journey, Aarav Sharma met Emma Williams in New York City, where they visited Central Park and discussed their plans to travel to Paris, France. Later, they met Rohan Mehta and Sophia Johnson near the Eiffel Tower, before flying to Tokyo, Japan, where they explored Shibuya Crossing. Their next destination was Sydney, Australia, where Daniel Brown introduced them to his friend Olivia Martin. Eventually, the group returned to New Delhi, India, after visiting London, Mumbai, Rome, Dubai, Singapore, and Toronto.",
    )

#print(result)
for entity in result:
    print(f"{entity['word']}: {entity['entity_group']}")