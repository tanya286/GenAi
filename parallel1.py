from typing import TypedDict ,Annotated
import operator
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph,START,END
from langgraph.types import Send
class OverallaState(TypedDict):
    students:list[str]
    reports:Annotated[list[str],operator.add]

class WorkerState(TypedDict):
    student:str
    repor:Annotated[list[str],operator.add]


def planner(state:OverallaState):
    print("\n Planner is creating parallel tasks.")
    return[
        Send(
            "worker",
            {
                "student":student
            }
        )
        for student in state["students"]
    ]

def worker(state:WorkerState):
    student= state["student"]
    print(f"Generating report for {student}...")
    report=f"{student} -> Report generated"
    return{
        "reports":[report]
    }

graph =StateGraph(OverallaState)

graph.add_node("worker",worker)
graph.add_conditional_edges(
    START,
    planner,
    ["worker"]
)
graph.add_edge("worker",END)

app=graph.compile()

result= app.invoke(
    {
        "students":[
            "Rahul",
            "Amit",
            "Nita",
            "Riya"
            
        ],
        "reports":[]
    }
)

print("\n Final Reports\n ")
for report in result["reports"]:
    print(report)