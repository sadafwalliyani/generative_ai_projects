import streamlit as st
import torch
import torchaudio
from audiocraft.models import MusicGen
import os
import numpy as np
import base64

genres = ["Pop", "Rock", "Jazz", "Electronic", "Hip-Hop", "Classical", 
          "Lofi", "Chillpop","Country","R&G", "Folk","Heavy Metal", 
          "EDM", "Soil", "Funk","Reggae", "Disco", "Punk Rock", "House",
          "Techno","Indie Rock", "Grunge", "Ambient","Gospel", "Latin Music","Grime" ,"Trap", "Psychedelic Rock"  ]

@st.cache_resource()
def load_model():
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    return model

def generate_music_tensors(descriptions, duration: int):
    model = load_model()
    # model = load_model().to('cpu')


    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=duration
    )

    with st.spinner("Generating Music..."):
        output = model.generate(
            descriptions=descriptions,
            progress=True,
            return_tokens=True
        )

    st.success("Music Generation Complete!")
    return output


def save_audio(samples: torch.Tensor):
    sample_rate = 30000
    save_path = "audio_output" 
    assert samples.dim() == 2 or samples.dim() == 3

    samples = samples.detach().cpu()
    if samples.dim() == 2:
        samples = samples[None, ...]

    for idx, audio in enumerate(samples):
        audio_path = os.path.join(save_path, f"audio_{idx}.wav")
        torchaudio.save(audio_path, audio, sample_rate)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

st.set_page_config(
    page_icon= "musical_note",
    page_title= "Music Gen"
)

def main():
    with st.sidebar:
        st.header("""⚙️Generate Music ⚙️""",divider="rainbow")
        st.text("")
        st.subheader("1. Enter your music description.......")
        bpm = st.number_input("Enter Speed in BPM", min_value=60)

        text_area = st.text_area('Ex : 80s rock song with guitar and drums')
        st.text('')
        # Dropdown for genres
        selected_genre = st.selectbox("Select Genre", genres)
        
        st.subheader("2. Select time duration (In Seconds)")
        time_slider = st.slider("Select time duration (In Seconds)", 0, 60, 10)
        # time_slider = st.slider("Select time duration (In Minutes)", 0,300,10, step=1)


    st.title("""🎵 Song Lab AI 🎵""")
    st.text('')
    left_co,right_co = st.columns(2)
    left_co.write("""Music Generation through a prompt""")
    left_co.write(("""PS : First generation may take some time ......."""))
    
    if st.sidebar.button('Generate !'):
        with left_co:
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('\n\n')
            st.subheader("Generated Music")

            # Generate audio
            # descriptions = [f"{text_area} {selected_genre} {bpm} BPM" for _ in range(5)]
            descriptions = [f"{text_area} {selected_genre} {bpm} BPM" for _ in range(1)]  # Change the batch size to 1
            music_tensors = generate_music_tensors(descriptions, time_slider)

             # Only play the full audio for index 0
            idx = 0
            music_tensor = music_tensors[idx]
            save_music_file = save_audio(music_tensor)
            audio_filepath = f'audio_output/audio_{idx}.wav'
            audio_file = open(audio_filepath, 'rb')
            audio_bytes = audio_file.read()

            # Play the full audio
            st.audio(audio_bytes, format='audio/wav')
            st.markdown(get_binary_file_downloader_html(audio_filepath, f'Audio_{idx}'), unsafe_allow_html=True)


if __name__ == "__main__":
    main()

