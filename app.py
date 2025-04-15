from dotenv import load_dotenv
import os
load_dotenv() # Load environment variables from .env file
import streamlit as st
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY", os.environ.get("GOOGLE_API_KEY")))

## function load  Gemini Pro model and get response

model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")
def get_gemini_response(question):
    response= model.generate_content(question)
    return response.text

## initialize Streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input:",key="input")

submit=st.button("Ask a question")

## When the button is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)
   