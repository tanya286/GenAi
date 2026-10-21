from multiprocessing import connection
from typing import TypedDict ,Annotated
import operator
import mysql.connector
from langgraph.graph import StateGraph,START,END
from langgraph.types import Send


db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="db1"
)

cursor = db.cursor(dictionary=True)

cursor.execute("SELECT * FROM students1")
results = cursor.fetchall()

cursor.close()
db.close()

class OverallaState(TypedDict):
    students:list[dict]
    reports:Annotated[list[str],operator.add]

class WorkerState(TypedDict):
    student:dict
    report:Annotated[list[str],operator.add]

def planner(state:OverallaState):
    print("\n Planner is creating parallel tasks...\n")

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

    total=(
        student["java"]+
        student["python"]+
        student["cpp"]+
        student["c"]
    )

    percentage= total/4

    if percentage >= 90:
        grade= "A"

    elif percentage >=75:
        grade="B"

    elif percentage >=60:
        grade="C"

    else:
        grade="D"   

    report=f"""
    ----------------------------------------
Student ID : {student['id']}
Name : {student['name']}

Java :{student['java']}
Python:{student['python']}
C:{student['c']}
CPP:{student['cpp']}
total:{total}
Percentage:{percentage:.2f}%
Grade:{grade}
----------------------------------------------
"""   
    print(f"Report Generated For {student['name']}")

    return{
        "reports":[report]
    }
graph= StateGraph(OverallaState)

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
        "students":results,
        "reports":[]
    }
)

print("\n=====FINAL REPORT=======\n")

for report in result["reports"]:
    print(report)