import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
genai.configure(api_key=os.environ['API_KEY'])
messages  = ["hello","help me in wrritingn gthe code"]

if 'question_history' not in st.session_state:
    st.session_state.question_history = []


with st.sidebar:
    st.write(for msg in messages;)


"""
if 'question_history' not in st.session_state:
    st.session_state.question_history = []

def add_question_to_history(question):
    """Add a new question to the history with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.question_history.append({
        'question': question,
        'timestamp': timestamp
    })

# Main app layout
def main():
    # Set up the main title
    st.title("Q&A Application")

    # Create the sidebar
    st.sidebar.title("Question History")
    if len(st.session_state.question_history) > 0:
        for i, item in enumerate(reversed(st.session_state.question_history), 1):
            with st.sidebar.expander(f"Question {i}"):
                st.write(f"**Asked at:** {item['timestamp']}")
                st.write(f"**Question:** {item['question']}")
    else:
        st.sidebar.info("No questions asked yet!")

    # Main area for asking questions
    question = st.text_input("Ask your question here:")
    if st.button("Submit"):
        if question.strip():  # Check if question is not empty
            # Add question to history
            add_question_to_history(question)

            # Here you can add your logic to process the question
            st.write(f"Your question: {question}")
            # Add your response logic here

            # Force a rerun to update the sidebar
            st.rerun()
        else:
            st.warning("Please enter a question!")

    # Optional: Add a clear history button
    if st.sidebar.button("Clear History"):
        st.session_state.question_history = []
        st.rerun()

if __name__ == "__main__":
    main()
"""