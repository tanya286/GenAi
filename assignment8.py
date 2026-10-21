from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash" ,
    api_key="AQ.Ab8RN6K2RCtRib5zRP3b7XX_iDOxZOVm7oo4QsfI_B0zqmHPoA")

class StudentState(TypedDict):
    query: str
    query_type: str
    course: str
    information: str
    response: str
    summary: str

def understand_information(State:StudentState):
    prompt=f"""Analyze the student's question and determine:
• Query type: course, fee, career, or general
• Extract the relevant course/topic if mentioned.
return only query type
query{State["query"]}

"""     
    State["query_type"]=llm.invoke(prompt).content[0]["text"].strip()
    return State

def get_information(State: StudentState):
    prompt=f"""
Based on the query type, generate/retrieve appropriate information.
query:{State["query"]}
query type:{State["query_type"]}
course:{State["course"]}
For example:
"What is the fee for Python?"
 ↓
Query Type: fee
 ↓
Course: Python
↓
Retrieve Python fee information

return the information
"""

    State["information"]=llm.invoke(prompt).content[0]["text"].strip()
    print(State["information"])
    return State

def generate_response(State:StudentState):
    prompt=f"""Create a clear response for the student using the information stored in the shared state.
   query:{State["query"]}
query type:{State["query_type"]}
course:{State["course"]}
information:{State["information"]} 
"""

    State["response"]=llm.invoke(prompt).content[0]["text"].strip()
    print(State["response"])
    return State

def summarize(State:StudentState):
    prompt = f"""
Create a short summary of the interaction.
query:{State['query']}
response:{State['response']}
"""
    State["summary"]=llm.invoke(prompt).content[0]["text"].strip()
    return State

graph=StateGraph(StudentState)
graph.add_node("UINFO",understand_information)
graph.add_node("GINFO",get_information)
graph.add_node("response",generate_response)
graph.add_node("summary",summarize)

graph.add_edge(START,"UINFO")
graph.add_edge("UINFO","GINFO")
graph.add_edge("GINFO","response")
graph.add_edge("response","summary")
graph.add_edge("summary",END)

app=graph.compile()

query= input("Enter your Query:")
result= app.invoke(
    {
        "query":query,
        "query_type":"",
        "course": "",
        "information":"" ,
        "response":"",
        "summary": "" 
    }
)

print("\n Final Response\n")
print(result["response"])
print("=================================")
print(result["summary"])



