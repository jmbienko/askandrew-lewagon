# Streamlit frontend
import streamlit as st
import requests

st.title("AskAndrew - Chatbot")

user_input = st.text_input("Ask a question:")

if user_input:
    response = requests.post("http://127.0.0.1:8000/chat/", json={"question": user_input, "user": "Streamlit User"})
    if response.status_code == 200:
        chat_response = response.json()['response']
        st.text_area("Response:", value=chat_response, height=300)
    else:
        st.write("Error: Failed to get response from the chatbot.")
