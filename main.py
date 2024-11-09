import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
# Load environment variables from the .env file
load_dotenv()
genai.configure(api_key=os.environ['API_KEY'])
j = 0
def summarize_image(image_path,prompt):
    myfile = genai.upload_file(image_path)
    #print(f"{myfile=}")

    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(
        [myfile, "\n\n", prompt]
    )
    return result.text
    #print(f"{result.text=}")

def generate_summary(file_path,prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    sample_pdf = genai.upload_file(file_path)
    response = model.generate_content([prompt, sample_pdf])
    #print(response.text)
    return response.text
def code_assistant(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response.text
def add_history(prompt):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.question_history.append({
        'question': prompt,
        'timestamp': timestamp
    })