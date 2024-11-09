import streamlit as st
from dotenv import load_dotenv
import os
from datetime import datetime
import google.generativeai as genai
from main import summarize_image, generate_summary, code_assistant, add_history

# Load environment variables
load_dotenv()
genai.configure(api_key=os.environ['API_KEY'])

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Generative Assistant",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSS for chat-like styling
st.markdown(
    """
    <style>
    .question { color: #3b82f6; font-weight: bold; font-size: 16px; margin-bottom: 10px; }
    .answer { color: #10b981; font-size: 15px; margin-top: 10px; background-color: #f0fdf4; padding: 15px; border-radius: 8px; }
    .sidebar-history { background-color: #f9fafb; border-radius: 10px; padding: 10px; }
    .expander { font-size: 13px; }
    footer { visibility: hidden; } /* Hide default Streamlit footer */
    </style>
    """,
    unsafe_allow_html=True
)

# Directory for uploads
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Store question history
if "question_history" not in st.session_state:
    st.session_state.question_history = []

def add_question_to_history(prompt):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.question_history.append({
        "question": prompt,
        "timestamp": timestamp
    })

# Redefine function calls for image and text summarization
def summarize_image(image_path, prompt):
    myfile = genai.upload_file(image_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content([myfile, "\n\n", prompt])
    return result.text

def code_assistant(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response.text

def main():
    # Title with enhanced styling
    st.title("💬 Generative Assistant")

    # Sidebar history panel
    st.sidebar.title("📜 Conversation History")
    if len(st.session_state.question_history) > 0:
        for i, item in enumerate(reversed(st.session_state.question_history), 1):
            with st.sidebar.expander(f"Question {i}", expanded=False):
                st.markdown(
                    f"<div class='sidebar-history'><strong>Asked at:</strong> {item['timestamp']}<br>"
                    f"<strong>Question:</strong> {item['question']}</div>",
                    unsafe_allow_html=True
                )
    else:
        st.sidebar.info("No questions asked yet!")

    # Input form with a fixed position at the bottom
    with st.form("input_form", clear_on_submit=True,border = False):
        prompt = st.text_area("Enter your prompt here:", height=70, label_visibility="collapsed")
        uploaded_image = st.file_uploader("Click to upload a file", type=["png", "jpg", "jpeg", "pdf"], label_visibility="collapsed")
        button = st.form_submit_button("Submit")

    # Handle uploaded image
    image_path = ""
    if uploaded_image is not None:
        image_path = os.path.join("uploads", uploaded_image.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

    # Process prompt submission
    if button:
        add_question_to_history(prompt)
        if uploaded_image and prompt is not None:
            response = summarize_image(image_path, prompt)
        else:
            response = code_assistant(prompt)

        # Display the question and response in chat format
        st.markdown(f"<div class='question'>📝 {prompt}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='answer'>💡 {response}</div>", unsafe_allow_html=True)
    elif not prompt:
        st.warning("Please enter a prompt to proceed.")

    # Clear history button
    if st.sidebar.button("Clear History"):
        st.session_state.question_history = []
        st.experimental_rerun()

if __name__ == "__main__":
    main()
