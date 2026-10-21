import streamlit as st

#st.file_uploader("Upload a file")

#st.file_uploader("Upload a PDF",type=["pdf"])

#st.file_uploader("Upload documents",type=["pdf","docx","txt"],accept_multiple_files=True)

#picture=st.camera_input("Take a picture")
#if picture:
#    with open("C:/Users/User/Desktop/gate/photo.jpg","wb") as f:
#        f.write(picture.getbuffer())
#audio=st.audio_input("record your message")
#if audio:
#    with open("recording.wav","wb")as f:
#        f.write(audio.getbuffer())
#st.chat_message("user").write("hello")
#st.chat_message("assistant").write("hello, how can i help you")

prompt=st.chat_input("Ask Something...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        st.write("received")    