import streamlit as st

#count=0
# if st.button("click"):
#    count=count+1

#st.subheader(count)

if"count" not in st.session_state:
    st.session_state.count =0

if st.button("click"):
    st.session_state.count += 1

st.write("count:",st.session_state.count)        