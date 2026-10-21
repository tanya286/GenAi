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

cursor.execute("SELECT * FROM employees1")
results = cursor.fetchall()

cursor.close()
db.close()

class OverallaState(TypedDict):
    employees:list[dict]
    reports:Annotated[list[str],operator.add]

class WorkerState(TypedDict):
    employee:dict
    report:Annotated[list[str],operator.add]

def planner(state:OverallaState):
    print("\n Planner is creating parallel tasks...\n")

    return[
        Send(
            "worker",
            {
                "employee":employee
            }
        )
        for employee in state["employees"]
    ]


def worker(state:WorkerState):
    employee= state["employee"]

    total=(
        employee["task_score"]+
        employee["attendance_score"]+
        employee["feedback_score"]
    )

    percentage= total/3

    if percentage >= 80:
        category="Excellent"

    elif percentage >=60:
        category="Good"

    else:
        category="Needs Improvement" 

    if category =="Excellent":
        recommendation="Consider for promotion"

    elif category=="Good":
        recommendation="Continue current development plan"

    else:
        recommendation="Schedule performance review"        
        

    report=f"""
    ----------------------------------------
Employee ID : {employee['emp_id']}
Name : {employee['emp_name']}
Department:{employee['department']}
Task Completion Score:{employee['task_score']}
Attendance Score:{employee['attendance_score']}
Feedback Score:{employee['feedback_score']}
Performance Score:{total}
Percentage:{percentage:.2f}%
Performance category:{category}
Recommendation:{recommendation}
----------------------------------------------
"""   
    print(f"Report Generated For {employee['emp_name']}")

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
        "employees":results,
        "reports":[]
    }
)

print("\n=====FINAL REPORT=======\n")

for report in result["reports"]:
    print(report)