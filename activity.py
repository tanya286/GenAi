from groq import Groq

client =Groq(
    api_key="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"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "you are a sports commantator, explain rainbows to a 5 year old"
        }
    ]
)
#print(response)
print(response.choices[0].message.content)