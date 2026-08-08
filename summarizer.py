from groq import Groq

client =Groq(
    api_key="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"
)


text="""The FIFA World Cup is an international association football competition among the senior men's national teams of the members of the Fédération Internationale de Football Association (FIFA), the sport's global governing body. The tournament has been held every four years since the inaugural tournament in 1930, with the exception of 1942 and 1946 during and shortly after World War II. The reigning champion is Spain, who won their second title at the 23rd edition of the competition, the 2026 World Cup, by defeating the holders, Argentina."""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "you are an expert summarizer"
        },
        {
            "role": "user",
            "content": f"Summarize this text in 3 bullet points:\n\n {text}"
        }
    ],
)
print(response.choices[0].message.content)