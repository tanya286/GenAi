import ollama

response= ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"""
Analyze the sentiment of this sentence.
sentence:"i absolutely love this product!"
return only:
sentiment:positive or negative

"""
        }
    ]
)
print(response["message"]["content"])