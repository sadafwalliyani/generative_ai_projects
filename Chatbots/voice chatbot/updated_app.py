
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables from .env file
load_dotenv('.env')
import os
os.environ["OPENAI_API_KEY"] = "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"

openai_api_key = os.getenv("OPENAI_API_KEY")

# chat=ChatOpenAI(temperature=0.5)
llm=OpenAI(openai_api_key=os.environ["OPEN_API_KEY"],temperature=0.5)

# Check if the API key is available
if not openai_api_key:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
else:
    # Initialize OpenAI model
    llm = OpenAI(model_name="text-davinci-003", temperature=0.5, openai_api_key=openai_api_key)

    # Streamlit app
    st.set_page_config(page_title="Q&A Demo")
    st.header("Langchain Application")

    input_text = st.text_input("Input:", key="input")
    submit_button = st.button("Ask the Question")

    if submit_button:
        response_text = llm(input_text)
        st.subheader("The Response is:")
        st.write(response_text)


import openai

# Function to convert speech to text
def speech_to_text(audio_file):
    response = openai.Speech.create(
        model="whisper-large",
        file=audio_file,
        language="en"
    )
    return response['text']

# Function to convert text to speech
def text_to_speech(text):
    response = openai.Audio.create(
        model="tts",
        input=text,
        voice="alloy"
    )
    return response['audio']

# Streamlit widgets to capture and play audio
st.audio("audio_input.wav")
audio_input = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
if audio_input is not None:
    text_from_audio = speech_to_text(audio_input)
    response_text = llm.generate(text_from_audio)
    audio_response = text_to_speech(response_text)
    st.audio(audio_response)
