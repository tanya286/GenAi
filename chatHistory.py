from groq import Groq

client =Groq(
    api_key="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"
)

messages=[]

while True:
    question=input("YOU:")

    if question =="exit":
        break

    messages.append({"role":"user","content":question})
    response =client.chat.completions.create(   
        model="llama-3.1-8b-instant",
        messages=messages   
    )
    answer=response.choices[0].message.content
    print("AI:",answer)
    messages.append({"role":"assistant","content":answer})

   
    print(messages)