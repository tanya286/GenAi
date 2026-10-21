import streamlit as st
import datetime
##st.subheader("Text Input")
##st.text_input("Enter Your Name")

##st.subheader("Text Area")
##st.text_area("Enter Your Name")

##st.subheader("Chat Input")
##st.chat_input("Enter Your Name")

##st.subheader("Number Input")
##st.number_input("Enter Your number",min_value=10,max_value=100,value=50,step=5)

##st.subheader("Slider")
##st.slider("Temperature")

##st.subheader("Slider")
##st.slider("Temperature",10,90)

##st.subheader("Select Slider")
##st.select_slider("Select your skill level",options=["Beginner","inter","Advance","pro","expert"],value="Advance")

#st.subheader("Select Box")
#st.selectbox("Select Your course",["Python","Java","C++","C#","JavaScript"])

#st.subheader("Multi Select Box")
#st.multiselect("Select Your course",["Python","Java","C++","C#","JavaScript"])

#st.subheader("Radio")
#st.radio("Select Gender",["male","female","other"])

#st.checkbox("I agree to the terms",value=True)

#st.toggle("Dark Mode")

if st.button("Click me"):
    st.write("Button was clicked")

text="hello from streamlit"

st.download_button(
    label="Download",
    data=text,
    file_name="hello.txt"
)

#st.link_button("visit xansa","https://xansa.net")

#st.date_input("Select a date")

#date=st.date_input("select your date",value=datetime.date(2026,8,21))

#st.date_input("select appointment date",min_value=datetime.date(2024,1,1),max_value=datetime.date(2024,12,31))

#st.time_input("select a time")

#st.time_input("select meeting time",value=datetime.time(17,30))

#color=st.color_picker("Select a color")

colors=st.color_picker("choose a bg clr","#FFFFFF")
st.markdown(f"<div style='background-color:{colors};padding:50px;'>Hellooooo</div>",
            unsafe_allow_html=True)

feedback= st.feedback("thumbs")
if feedback==1:
    st.write("thanks")
elif feedback==0:
    st.write("sorry")    

feedback= st.feedback("faces")
if feedback==1:
    st.write("thanks")
elif feedback==0:
    st.write("sorry")   
elif feedback==2:
    st.write("tahnksss") 
elif feedback==3:
    st.write("thankasssssss")         