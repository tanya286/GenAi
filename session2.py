import streamlit as st

if"courses" not in st.session_state:
    st.session_state.courses =[
        "c","cpp","java","python"
    ]
new_course= st.text_input("add a course")

if st.button("add course"):
    if new_course:
        if new_course not in st.session_state.courses:
            st.session_state.courses.append(new_course)
            st.success("course added!")

        else:
            st.warning("course already exists!")

course = st.selectbox(
    "select course",st.session_state.courses
)                