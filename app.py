import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from config import CHAT_PROMPT_TEMPLATE

#This creates the title for the page
st.markdown(
    "<h2 style='text-align: center; color: #4CAF50; font-family: Arial;'>Martin Heidegger</h2>",
    unsafe_allow_html=True,
)

template = CHAT_PROMPT_TEMPLATE
prompt = ChatPromptTemplate.from_template(template)

#Insert Ollama model name here
#Currently using llama3.1
model = OllamaLLM(model="llama3.1")
chain = prompt | model

#Create a message history tied to the session state by adding to a dictionary
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I assist you?"}
    ]

#Display the chat history by iterating through the messages dictionary
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

#Create user input box
if user_input := st.chat_input("Ask me any questions!"):
    #Add the user input message to the session state and display the message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    #Generate the response
    with st.chat_message("assistant"):
        response = chain.invoke({"question": user_input})
        st.markdown(response)

    #Add the response message to the session state
    st.session_state.messages.append({"role": "assistant", "content": response})