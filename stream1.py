import streamlit as st

st.title("My First Streamlit App")
st.header("Introduction")
st.subheader("Getting Started")

#st.write("Welcome to Streamlit!!")
#st.write(100)
#st.write(["python","langChain"])
#st.write({"model":"gpt","temp":7})

st.markdown("## This is a markdown text")
st.markdown("# this is large heading")
st.markdown("**This is bold**")
st.markdown("streamlit makes *gen ai *easy")
st.markdown('`print("hello")`')
st.markdown("- Apple")
code= """

def hello():
    print("hello genai")
    """

st.code(code,language="python")