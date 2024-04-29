
from transformers import pipeline

tts_pipeline = pipeline("text-to-speech", model="facebook/fastspeech2-en-ljspeech")

def synthesize_speech(text):
    speech = tts_pipeline(text)
    audio_data = speech[0]['file']
    return audio_data
