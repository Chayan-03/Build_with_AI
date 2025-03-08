import streamlit as st
from dotenv import load_dotenv
import os
from datetime import datetime
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ['API_KEY'])

st.set_page_config(
    page_title="Generative Assistant",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Folder to upload the data
if not os.path.exists("uploads"):
    os.makedirs("uploads")

def summarize_file(image_path, prompt):
    myfile = genai.upload_file(image_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(
        [myfile, "\n\n", prompt]
    )
    return result.text

def code_assistant(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response.text

def main():
    # Title
    st.title("💬 Generative Assistant")

    # Form for input
    with st.form("input_form", clear_on_submit=True, enter_to_submit=True):
        prompt = st.text_area("Enter your prompt here:", key="input_text", height=100, label_visibility="collapsed")
        uploaded_file = st.file_uploader("Click to upload a file", label_visibility="collapsed")
        button = st.form_submit_button("Submit")

        file_path = ""
        if uploaded_file is not None:
            file_path = os.path.join("uploads", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        if button:
            # If button is clicked
            if uploaded_file and prompt is not None:
                st.write(f"{summarize_file(file_path, prompt)}")
            else:
                st.write(f"{code_assistant(prompt)}")

if __name__ == "__main__":
    main()
