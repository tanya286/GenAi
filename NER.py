from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)

text = "Barack Obama was the 44th President of the United States."
result = ner(text)

print("Named Entities:", result)