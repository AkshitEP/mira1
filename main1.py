import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("MIRA_API_KEY")

# Initialize MiraClient
client = MiraClient(config={"API_KEY": api_key})

# Streamlit UI
st.title("Mira AI Chatbot")

# User Input
user_message = st.text_input("You:", "")

if st.button("Send"):
    if user_message:
        input_data = {"user_input": user_message}
        response = client.flow.execute("akshit/ChatBot", input_data)  
        st.write("Bot:", response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please enter a message.")
