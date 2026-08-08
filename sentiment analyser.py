from groq import Groq
import json

client =Groq(
    api_key="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"
)

complaint = input("Enter customer complaint:\n")

promt=f"""you are an ai customer support analyser.
 analyse the following customer complaint and provide output in json format with the following keys:
   sentiment,
   issue_category, 
   urgency, professional_response. 
   The customer complaint is: {complaint}
example json format:{{"sentiment:"negative","issue_category":"product defect","urgency":"high","professional_response":"We apologize for the inconvenience..."}}"""

#print(promt)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
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
print
print(ai_output)

try:
    result=json.loads(ai_output)
    print(type(result))
    print(type(ai_output))
    print("\n=================================")
    print("CUSTOMER SUPPORT ANALYSIS")
    print("=================================")
    print(f"\nSentiment: {result['sentiment']}")
    print(f"Issue Category: {result['issue_category']}")
    print(f"Urgency: {result['urgency']}") 
    print(f"\nProfessional Response: ")
    print(result['professional_response']) 
except Exception as e:
    print("Error parsing JSON output:")
    print(e)