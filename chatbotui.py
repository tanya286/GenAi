import streamlit as st
from google import genai


st.set_page_config(
    page_title="Ai chatbot",
    page_icon="🤖",
)

st.title("tanya's AI chatbot")

st.write("ASK ME anything")

client= genai.Client(
    api_key="AQ.Ab8RN6K2RCtRib5zRP3b7XX_iDOxZOVm7oo4QsfI_B0zqmHPoA"
    )

if"messages" not in st.session_state:
    st.session_state.messages= []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("type your question..")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)             

    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })    

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    answer= response.text

    with st.chat_message("assistant"):
        st.write(answer)    

    st.session_state.messages.append({
        "role":"assistant",
        "content":answer
    })    