from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash" ,
    api_key="AQ.Ab8RN6K2RCtRib5zRP3b7XX_iDOxZOVm7oo4QsfI_B0zqmHPoA")


class UserState(TypedDict):
    query:str
    response:str

def smartAcademicRouter(State:UserState):
    prompt=f"""
you are an smart academic router.
 classifies a student's query into one of the following categories:
• admission
• fees
• courses
• contact
query;{State['query']}
Return ONLY the category name.
"""
    category=llm.invoke(prompt).content[0]["text"].strip().lower()
    print(f"\n[Router Selected]:{category}")
    return category



def admission_node(state:UserState):
    prompt=f"""
You are from a university admission department.
Answer the following question
que:{state['query']}

"""
    state["response"]=llm.invoke(prompt).content[0]["text"]
    return state    

def courses_node(state:UserState):
    prompt=f"""
You are from a university admission department.
Answer the following question
que:{state['query']}

"""
    state["response"]=llm.invoke(prompt).content[0]["text"]
    return state    

def fees_node(state:UserState):
    prompt=f"""
You are from a university fees department.
Answer the following question
que:{state['query']}

"""
    state["response"]=llm.invoke(prompt).content[0]["text"]
    return state   

def contact_node(state:UserState):
    prompt=f"""
You are from a university contact department.
Answer the following question
que:{state['query']}

"""
    state["response"]=llm.invoke(prompt).content[0]["text"]
    return state     


graph=StateGraph(UserState)
graph.add_node("admission",admission_node)
graph.add_node("courses",courses_node)
graph.add_node("fees",fees_node)
graph.add_node("contact",contact_node)

graph.add_conditional_edges(
    START,
    smartAcademicRouter,
    {
        "admission":"admission",
        "fees":"fees",
        "courses":"courses",
        "contact":"contact"
    }
)

graph.add_edge("admission",END)
graph.add_edge("fees",END)
graph.add_edge("courses",END)
graph.add_edge("contact",END)

app=graph.compile()

print("\n ====SMART ACADEMIC ASSISTANT====")
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
