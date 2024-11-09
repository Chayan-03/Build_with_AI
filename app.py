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

# folder to upload the data
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# store history
if 'question_history' not in st.session_state:
    st.session_state.question_history = []

def add_question_to_history(prompt):
    """Add a new question to the history with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.question_history.append({
        'question': prompt,
        'timestamp': timestamp
    })

def summarize_image(image_path,prompt):
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
    # title
    st.title("💬 Generative Assistant")
    # sidebar
    st.sidebar.title("📜 Conversation History")
    if len(st.session_state.question_history) > 0:
        for i, item in enumerate(reversed(st.session_state.question_history), 1):
            with st.sidebar.expander(f"Question {i}"):
                st.write(f"**Asked at:** {item['timestamp']}")
                st.write(f"**Question:** {item['question']}")
    else:
        st.sidebar.info("No questions asked yet!")
    with st.form("input_form", clear_on_submit=True,enter_to_submit=True):
        prompt = st.text_area("Enter your prompt here:", key="input_text", height=100 ,label_visibility="collapsed" )
        uploaded_image = st.file_uploader("click to upload  a fiile",label_visibility="collapsed")
        button = st.form_submit_button("Submit")
        image_path = ""
        if uploaded_image is not None:
            image_path = os.path.join("uploads", uploaded_image.name)
            with open(image_path, "wb") as f:
                f.write(uploaded_image.getbuffer())
        if button:
            #buton clicked
            add_question_to_history(prompt)
            if uploaded_image and prompt is not None:
                st.write(f"{summarize_image(image_path,prompt)}")
            else:
                st.write(f"{code_assistant(prompt)}")
    if st.sidebar.button("Clear History"):
        st.session_state.question_history = []
if __name__ == "__main__":
    main()