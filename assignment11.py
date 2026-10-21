import streamlit as st

st.title("Course Registration Portal")

st.header("Personal Information")

#st.write("Student's Full Name")
st.text_input("Enter Your Name")
st.text_input("Email ")
st.number_input("Age")
st.text_area("Learning Goals")


st.header("Course Selection")
st.selectbox("Your Primary Course",["Python","Java","C++","Web Development","Generative AI"])
st.multiselect("Topics Of Interest",["SQL","HTML","CSS","DSA","ML","React"])
st.radio("Preferred Learning Mode",["Online","Offline","Hybrid"])
st.select_slider("Skill Level",["Beginner","Intermediate","Advanced","Expert"])


st.header("Learning Preferences")
st.slider("Preferred Study Hours",1,8)
st.toggle("Weekend Classes")
st.checkbox("I agree to the terms and conditions")