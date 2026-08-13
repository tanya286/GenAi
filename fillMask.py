from transformers import pipeline

unmasker = pipeline("fill-mask")

text = "The capital of France is <mask>."
print(unmasker(text))