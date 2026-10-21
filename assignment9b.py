from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash" ,
    api_key="AQ.Ab8RN6K2RCtRib5zRP3b7XX_iDOxZOVm7oo4QsfI_B0zqmHPoA")


@tool
def weather(query):
    """Get the weather for a city."""
    response=(
        "Weather Service\n"
        "Todays weather is Sunny\n"
        "Temperature: 31c"
    )
    return response

@tool
def math(query):
    """Get the calculative result for the expression."""
    try:
       answer= eval(query)
       response=f"Calculator\nAnswer ={answer}"
    except:
        response="Invalid mathematical expression"
    return response
@tool
def gk(query):
    """Get information on general knowledge topics."""
    prompt=f"""
you are an helpfull ai assisstant.
help user knowing the general knowledge base on the user query
query:{query}
"""
    response=llm.invoke(prompt).content[0]["text"]
    return response

@tool
def programming(query):
    """Get information on programming topics."""
    prompt=f"""
you are an coding /programming assistant.
help user with the programming questions
question:{query} 
"""
    response=llm.invoke(prompt).content[0]["text"]
    return response
@tool
def travel(query):
    """Get information on travel topics."""
    prompt=f"""
you are a travel assistant.
answer the users questions
question:{query}
"""
    response=llm.invoke(prompt).content[0]["text"]
    return response 

router_prompt= PromptTemplate(
    input_variables=["query"],
    template="""
you are an ai assisstant.
classifies user queries and forwards them to the
correct department.
Categories
• Weather
• Calculator
• General Knowledge
• Programming
• Travel
Return ONLY the department name. 
User Query: {query}

""")

while(True):

    router =router_prompt | llm
    query = input("Enter your query: ")
    if query.lower() == "exit":
        break
    route = router.invoke({"query": query})

    category = route.content[0]["text"].strip().lower()
    print("\nCategory:", category)

    if category == "weather":
        result = weather.invoke({"query": query})
    elif category == "calculator":
        result = math.invoke({"query": query})
    elif category == "general knowledge":
        result = gk.invoke({"query": query})    
    elif category == "programming":
        result = programming.invoke({"query": query})
    elif category == "travel":
        result = travel.invoke({"query": query})


    print("\nResult:", result)