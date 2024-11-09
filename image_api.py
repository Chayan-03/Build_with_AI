import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
import uuid

# Load environment variables from the .env file
load_dotenv()

# Configure the Generative API client
genai.configure(api_key=os.environ['API_KEY'])

# Create a unique session ID for each user
session_id = str(uuid.uuid4())

# Create a dictionary to store user data
user_data = {
    session_id: {
        'images': [],
        'documents': [],
        'chat_history': [],
        'code_assistant_history': []
    }
}

# Streamlit app layout
st.set_page_config(page_title="Build with AI", layout="wide")
st.title("Build with AI")

# Image upload and description
st.subheader("Image Upload and Description")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_image is not None:
    image_path = os.path.join("uploads", uploaded_image.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_image.getbuffer())

    image_description = st.text_area("Describe the image")
    if st.button("Summarize Image"):
        summary = summarize_image(image_path, image_description)
        st.write(f"The summary for the image is: {summary}")

    # Store the image and description in the user's data
    user_data[session_id]['images'].append((image_path, image_description))

# Document upload and chatbot interaction
st.subheader("Document Upload and Chatbot")
uploaded_document = st.file_uploader("Upload a document", type=["pdf", "txt"])
if uploaded_document is not None:
    document_path = os.path.join("uploads", uploaded_document.name)
    with open(document_path, "wb") as f:
        f.write(uploaded_document.getbuffer())

    document_prompt = st.text_area("Ask a question about the document")
    if st.button("Get Document Summary"):
        summary = generate_summary(document_path, document_prompt)
        st.write(f"The summary is: {summary}")

    # Store the document and chat history in the user's data
    user_data[session_id]['documents'].append((document_path, document_prompt, summary))
    user_data[session_id]['chat_history'].append({"user": document_prompt, "assistant": summary})

# Code assistant
st.subheader("Code Assistant")
code_prompt = st.text_area("Describe what you need help with")
if st.button("Get Code Assistance"):
    code_response = generate_code_assistance(code_prompt)
    st.code(code_response, language="python")

    # Store the code prompt and response in the user's data
    user_data[session_id]['code_assistant_history'].append({"user": code_prompt, "assistant": code_response})


# Clear user data when the app is closed
@st.experimental_singleton
def clear_user_data():
    user_data[session_id] = {
        'images': [],
        'documents': [],
        'chat_history': [],
        'code_assistant_history': []
    }


# Call the clear_user_data function when the app is closed
st.session_state.get("clearData", False)
if st.session_state.get("clearData", False):
    clear_user_data()
    st.session_state.clearData = False


# Helper functions
def summarize_image(image_path, prompt):
    myfile = genai.upload_file(image_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content([myfile, "\n\n", prompt])
    return result.text


def generate_summary(file_path, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    sample_pdf = genai.upload_file(file_path)
    response = model.generate_content([prompt, sample_pdf])
    return response.text


def generate_code_assistance(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response.text