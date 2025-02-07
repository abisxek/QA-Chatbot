from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini pro model and get repsonse
model= genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

#to get response from gemini pro model
def get_gemini_response(question):
    response=chat.send_message(question, stream=True) #stream=True to get response in real time
    return response

#initialising streamlit app
st.set_page_config(page_title="Q&A Chatbot", page_icon=":robot:", layout="wide")

st.header("Gemingi LLM Chatbot")

#initialise session state for chat history if it doesnt exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input= st.text_input("Input:", key="input")
submit= st.button("Query")

if submit and input:
    response= get_gemini_response(input)
    ## append user input and response to chat history/ session chat history
    st.session_state['chat_history'].append(("You:",input))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Gemini:",chunk.text))

st.subheader("Chat History:")

## display chat history
for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")