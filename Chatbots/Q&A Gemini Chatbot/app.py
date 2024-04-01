import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables from .env file
load_dotenv('.env')

# Get the genai API key from the environment variables
genai_api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key is available
if not genai_api_key:
    st.error("genai API key not found. Please set the genai_API_KEY environment variable.")
else:
    # Initialize the genai model
    llm = genai.Chatgenai(genai_api_key=genai_api_key, temperature=0.5)

    # Streamlit app
    st.set_page_config(page_title="Q&A Demo")
    st.header("Langchain Application")

    input_text = st.text_input("Input:", key="input")
    submit_button = st.button("Ask the Question")

    if submit_button:
        response_text = llm(input_text)
        st.subheader("The Response is:")
        st.write(response_text)
