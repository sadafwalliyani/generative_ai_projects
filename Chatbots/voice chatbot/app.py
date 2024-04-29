
import streamlit as st
from speech_to_text import transcribe_audio
from process_text import process_text
from text_to_speech import synthesize_speech

st.set_page_config(page_title="Voice Bot", page_icon="🤖", layout="wide")

def main():
    st.title("Voice Bot")
    st.write("This is a simple voice bot that converts your speech to text, processes it, and responds with synthesized speech.")
    
    audio_input = st.file_uploader("Upload your audio file (in WAV format)", type=["wav"])
    
    if audio_input is not None:
        with st.spinner('Processing...'):
            text = transcribe_audio(audio_input)
            st.write("You said:", text)
            response = process_text(text)
            st.write("Bot's response:", response)
            audio_response = synthesize_speech(response)
            st.audio(audio_response)

if __name__ == "__main__":
    main()
