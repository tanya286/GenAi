import streamlit as st
import pandas as pd
from pypdf import PdfReader

name=st.text_input("Name")
email=st.text_input("Email")
st.write("Name:",name)
st.write("Email:",email)

num1=st.number_input("enter first number")
num2=st.number_input("enter")
st.write("Sum:",num1 + num2)

if st.button("Add"):
    result= num1 + num2
    st.text_input("result:",value=(result))


language=st.selectbox("Choose language",["python","java","C"])
st.text_area(value=language,label="selected language")    


languages=st.multiselect("Choose language",["python","java","C","js","react"])

for lang in languages:
    st.write(lang)


agree= st.checkbox("i agree")
if agree:
    st.success("Thank you")


show=st.toggle("Show advance option")

if show:
    experience=st.slider("years of experience",0,30)


age=st.slider("select your age",1,100,25)
if age>=18:
    str="can vote"
else:
    str="cannot vote"

st.write(str)

#file=st.file_uploader("choose a file",type=["pdf","txt"])

#if file is not None:
#    st.write("file uploaded",file.name)


#file=st.file_uploader("choose a file",type=["csv"])
#df=None
#try:
 #   df=pd.read_csv(file)

#except UnicodeDecodeError:
 #   df=pd.read_csv(file,encoding="latin1")
    
#st.dataframe(df)    

file1=st.file_uploader("choose a file",type=["pdf"])

if file1 is not None:
    reader=PdfReader(file1)
    for page in reader.pages:
        text= page.extract_text()

        if text:
            st.write(text)


feedback= st.feedback("thumbs")
if feedback==1:
    st.write("thanks")
elif feedback==0:
    st.write("sorry")

else:
    st.write("we would love to hear from you")


rating= st.feedback("stars")
if rating is not None:
    st.write("Rating:",rating+1)