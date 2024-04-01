import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Load the model
model = tf.keras.models.load_model("D:/Chatbots/Image_to_image_gen/pix2pix.h5")

# Set the page title
st.set_page_config(page_title="Image Generation App", page_icon="🖼️")

# Set the app title
st.title("Image Generation App")

# Load the image from the user's input
image_path = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if image_path is not None:
    image = Image.open(image_path)
    st.image(image, caption="Original Image", use_column_width=True)

    # Preprocess the image
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Generate the image
    generated_image = model.predict(image)

    # Display the generated image
    st.image(np.squeeze(generated_image), caption="Generated Image", use_column_width=True)
