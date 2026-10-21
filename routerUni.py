from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash" ,
    api_key="AQ.Ab8RN6K2RCtRib5zRP3b7XX_iDOxZOVm7oo4QsfI_B0zqmHPoA")


class UniversityState(TypedDict):
    query:str
    response:str

def router(state:UniversityState):
    prompt=f"""
You are a university query classifier.
Classify the users query into ONLY ONE category.
academic
finance
placement
admin 
general
Query:
{state["query"]}
Return ONLY the category name.
"""
    category=llm.invoke(prompt).content[0]["text"].strip().lower()
    print(f"\n[Router Selected]:{category}")
    return category

def academic_node(state:UniversityState):
    prompt=f"""
You are a university professor.
AAnswer the following quest
que:{state['query']}

"""
    state["response"]=llm.invoke(prompt).content[0]["text"]
    return state

def finance_node(State:UniversityState):
    prompt=f"""
You are the finance department of a uni.
answer only finance related questions such as:
fees
scholarships
payments
refunds
que:{State['query']}
"""    
    State["response"]=llm.invoke(prompt).content[0]["text"]
    return State

def placement_node(state:UniversityState):
    prompt=f"""
you are a placement cell.
answer que related to 
plaements
compnies
internships
resume
interviews
question:{state['query']}
"""
    state["response"]=llm.invoke(prompt).content[0]["text"]

    return state

def chat(state:UniversityState):
    prompt=f"""
you are a helpfull chat assistant.
if the query doesnt classify into the already known then help user to solve the other query
question:{state['query']} 
"""
    state["response"]=llm.invoke(prompt).content[0]["text"]
    return state


graph=StateGraph(UniversityState)
graph.add_node("academic",academic_node)
graph.add_node("finance",finance_node)
graph.add_node("placement",placement_node)
graph.add_node("general",chat)

graph.add_conditional_edges(
    START,
    router,
    {
        "academic":"academic",
        "finance":"finance",
        "placement":"placement",
        "general":"general"
    }
)

graph.add_edge("academic",END)
graph.add_edge("finance",END)
graph.add_edge("placement",END)
graph.add_edge("general",END)

app=graph.compile()

print("\n ====AI UNIVERSITY ASSISTANT====")
print("\n type 'exit' to quit")

while True:
    query=input("You: ")
    if query.lower()=='exit':
        break
    result=app.invoke(
        {
            "query":query,
            "response":""
        }
    )
    print("\n AI:",result["response"])