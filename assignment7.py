import json
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash" ,
    api_key="AQ.Ab8RN6K2RCtRib5zRP3b7XX_iDOxZOVm7oo4QsfI_B0zqmHPoA")

os.makedirs("memory", exist_ok=True)
username = input("Enter your username: ").strip()
memory_file = f'memory/{username}.json'
history = []

if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
            data = json.load(f)
    for msg in data:
        if msg["role"] == "user":
                history.append(HumanMessage(content=msg["content"]))
        else:
                history.append(AIMessage(content=msg["content"]))
    print(f'\n Welcome back, {username}!')
else:
     print(f'\n new user created, {username}!')    
                


summary=""

if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        summary = f.read()


print("type 'exit' to quit")

while True:
    query = input("you:")
    if query.lower() == "exit":
        break
    history.append(HumanMessage(content=query))
    response = llm.invoke(history)
    history.append(AIMessage(content=response.content[0]["text"]))
    print(f"AI: {response.content[0]['text'] }")

data = []
for msg in history:
    data.append({"role": msg.type, "content": msg.content})    


with open(memory_file, "w") as f:
    json.dump(data, f , indent=4)

print("\nConversation saved successfully!")    

conversation=""

for msg in history:
     if msg.type=="user":
        conversation+=f"User: {msg.content}\n"

     else:
        conversation+=f"AI: {msg.content}\n"

summary_prompt=f"""
You are an Ai assisstant.
Summarize the following conversation if the length of the converstion is long 
include:
1. Important topics discussed
2. Facts learned about the user
3. Important  decisions
keep the summary within 8 bullet points.
conversation:
{conversation}
and if the conversation is short  save the conversation as it is
keep everything in JSON FORMAT ONLY.
"""

summary_response=llm.invoke(summary_prompt)
summary=summary_response.content[0]["text"]

with open(memory_file, "w") as f:
    f.write(summary)
print("Conversation summary generated")    

           