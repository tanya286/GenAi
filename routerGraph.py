from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash" ,
    api_key="AQ.Ab8RN6K2RCtRib5zRP3b7XX_iDOxZOVm7oo4QsfI_B0zqmHPoA")


class ChatState(TypedDict):
    query:str
    response:str

def router(state:ChatState):
    prompt=f"""
You are a routing assistant.
Classify the following query into ONLY ONE category.
weather
maths
Query:{state['query']}
Return ONLY the category name.
"""    
    category = llm.invoke(prompt).content[0]["text"].strip().lower()
    print("\n[Router Selected]:",category)
    return category

def weather_node(state:ChatState):
    state["response"]=(
        "Weather Service\n"
        "Todays weather is Sunny\n"
        "Temperature: 31c"
    )
    return state

def math_node(state:ChatState):
    try:
       answer= eval(state["query"])
       state["response"]=f"Calculator\nAnswer ={answer}"
    except:
        state["response"]="Invalid mathematical expression"
    return state


graph= StateGraph(ChatState)
graph.add_node("weather",weather_node)
graph.add_node("maths",math_node)

graph.add_conditional_edges(
    START,
    router,
    path_map={
        "weather":"weather",
        "maths":"maths"
    }
)
graph.add_edge("weather",END)
graph.add_edge("maths",END)

app=graph.compile()

png_data= app.get_graph().draw_mermaid_png()
with open("workflow2.png","wb") as file:
    file.write(png_data)

while True:
    query= input("\n You: ")
    if query.lower()=="exit":
        break
    result= app.invoke(
        {
            "query":query,
            "response":""
        }
    )

    print("\n AI: ", result["response"])

    