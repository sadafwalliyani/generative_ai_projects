
import speech_recognition as sr

recognizer = sr.Recognizer()

def transcribe_audio(audio_file_path):
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Audio could not be understood"
        except sr.RequestError as e:
            return f"Could not request results; {e}"
