from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY", os.environ.get("GOOGLE_API_KEY")))

# Initialize the Gemini Vision model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image):
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Image Application")

# Text input for the user prompt
input_text = st.text_input("Input Prompt:", key="input")

# File uploader for the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None  # Initialize image as None

if uploaded_file is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.",  use_container_width=True)

# Button to trigger the analysis
submit = st.button("Tell me about the image")

# When the button is clicked
if submit:
    if image is None:
        st.error("Please upload an image.")
    else:
        try:
            # Get the response from the Gemini model
            response = get_gemini_response(input_text, image)
            st.subheader("The response is:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")