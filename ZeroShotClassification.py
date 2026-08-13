from transformers import pipeline

classifier = pipeline("zero-shot-classification")

labels=["politics","sports","technology","food"]

text= "the new smartphone has a great camera and long battery life"

result = classifier(text,candidate_labels=labels)

print("Top label:", result['labels'][0])