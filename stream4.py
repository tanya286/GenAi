import streamlit as st

date= st.date_input("select date",format="DD-MM-YYYY")
time= st.time_input("select time",format="12h")

st.write(date)
st.write(time)