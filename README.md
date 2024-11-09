# Generative Assistant

This project is a simple Generative Assistant application built with [Streamlit](https://streamlit.io/) that allows users to upload images or enter text prompts to receive AI-generated summaries or responses. The app uses Google’s generative AI model, configured via the [google-generativeai](https://pypi.org/project/google-generativeai/) Python package, to process and respond to user inputs.

## Features

- **Text Prompt Responses:** Enter any text prompt, and the model generates an AI-powered response.
- **Document Interaction:** Upload an image/doc along with a prompt, and the app provides a summarized response.
- **Interactive UI:** A simple and user-friendly interface for uploading files and receiving outputs.

## Requirements

- Python 3.10+
- Google Generative AI API Key

## Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/generative-assistant.git
    cd generative-assistant
    ```

2. **Install Dependencies:**

    Ensure you have [pip](https://pip.pypa.io/en/stable/) installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables:**

    - Create a `.env` file in the root directory.
    - Add your Google Generative AI API key:

      ```plaintext
      API_KEY=your_google_genai_api_key
      ```

4. **Run the Application:**

    Start the Streamlit app with the following command:

    ```bash
    streamlit run app.py
    ```

    Replace `app.py` with the actual file name of the main script if it differs.

5. **Access the Application:**

    Open a web browser and go to `http://localhost:8501` to interact with the app.

## Usage

1. **Text Prompts:**
   - Enter a question or prompt in the text area and click **Submit**. The app will display an AI-generated response.

2. **Doc Summarization:**
   - Upload an image/doc and enter a related prompt, then click **Submit**. The app will provide a summary based on the content of the image and prompt.


## Technologies Used

- [Streamlit](https://streamlit.io/) - For creating a user-friendly web interface
- [google-generativeai](https://pypi.org/project/google-generativeai/) - To interact with Google Generative AI
- [Python Dotenv](https://pypi.org/project/python-dotenv/) - For environment variable management



## Acknowledgments

- [Google Generative AI](https://cloud.google.com/generative-ai) for providing the generative model.
- Streamlit for the framework to build this simple UI.


