from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "the capital of France is"

result = generator(prompt, max_length=50, do_sample=True, temperature=0.7)

print(f"\nPROMPT: {prompt}")
print(f"RESULT: {result[0]['generated_text']}")