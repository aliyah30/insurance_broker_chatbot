import streamlit as st #this is supposed to help import the streamlit 

with st.chat_message(name = "assistant"): #this is a container , putting the write element
    st.write("Hello Aajimatics") #this displays a welcome message.

st.title("Aliyah's internship Assignment") #this shows up as the title 

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:  #it displays the chat messages from history 
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("How can i help you?"): #this shows the chatbox below 
    with st.chat_message("user"): #it also help to react to user input 
         st.markdown(prompt)
