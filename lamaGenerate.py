import ollama

response=ollama.generate(
    model="llama3.2",
    prompt="AI is"
)
print(response["response"])