from groq import Groq
import json

client =Groq(
    api_key=""
)
with open(r"c:\Users\User\Documents\samplw.txt") as file:
    for line in file:
        if line=="\n":
            continue
        complaint=line.strip()
        promt=f"""you are an ai customer support analyser.
 analyse the following customer complaint and provide output in json format with the following keys:
    mood, urgency,  required actions 
   The customer complaint is: {complaint}
example json format:{{"mood":"Complaint","urgency":"High","required_actions":"Escalation"}}"""

        
        response = client.chat.completions.create(
         model="openai/gpt-oss-120b",
        messages=[
        {
            "role": "system",
            "content":" you are an expert ai customer support assistant. Reply in JSON only "
        },
        {
            "role": "user",
            "content": promt
        }
        ],
        max_tokens=500
        )

        ai_output=response.choices[0].message.content.strip()
        ai_output= ai_output.replace("```json","")
        ai_output= ai_output.replace("```","")
        ai_output= ai_output.strip()

        try:
            result=json.loads(ai_output)
            print("=================================")
            print("Review:")
            print("=================================")
            print(complaint)
            print(f"\nMood: {result['mood']}")
            print(f"Urgency: {result['urgency']}")
            print(f"Required Actions: {result['required_actions']}")
        except Exception as e:
            print("Error parsing JSON output:")
            print(e)
file.close()            
