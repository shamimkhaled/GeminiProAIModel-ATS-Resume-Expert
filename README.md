
# [Gemini Pro Vision AI Model ATS - Resume Tracking System](https://geminiproaimodel-ats-resume-expert.streamlit.app/)


#### Purpose:

- This code creates a Streamlit application that serves as an ATS (Applicant Tracking System) with resume evaluation capabilities.
- It leverages Google's Gemini Pro AI model to analyze resumes and provide insights based on different prompts and job descriptions.
#### Deployment Site on Streamlit Cloud
[https://geminiproaimodel-ats-resume-expert.streamlit.app/](https://geminiproaimodel-ats-resume-expert.streamlit.app/)

#### Key Features:
- Resume Upload: Users can upload their resumes in PDF format.
- Job Description Input: Users can enter the job description they're applying for.
#### Three Functionalities:
- Tell Me About the Resume: Provides an overall evaluation of the resume's alignment with the job description.
- How Can I Improvise My Skills: Offers specific recommendations on how the candidate can improve their skills and experience to better match the job requirements.
- Percentage Match: Calculates the percentage of match between the resume and job description, highlights missing keywords, and provides final thoughts.
#### Functionality Breakdown:
##### Import Necessary Libraries:

- base64: For encoding/decoding data.
- streamlit: For creating the web app interface.
- os: For interacting with the operating system.
- io: For handling input/output operations.
- PIL: For image processing.
- pdf2image: For converting PDFs to images.
- google.generativeai: For interacting with Google's generative AI models.
- dotenv: For loading environment variables.

#### Configuration:
- Load environment variables (including Google API key).
- Configure the Maker Suite Google API.
#### Functions:
- get_gemini_response: Calls the Gemini Pro AI model to generate content based on provided inputs and prompts.
- resume_pdf_setup: Converts a uploaded PDF resume to a list of images.

#### Streamlit App Setup:
- Sets page title and header.
- Creates text input for job description.
- Creates file uploader for resume.
- Creates buttons for the three functionalities.
- Defines prompts for each functionality.

#### Button Actions:
- Each button triggers a conditional block that calls get_gemini_response with appropriate inputs and prompts.
- The generated response is then displayed on the Streamlit app.


## Running the Code Locally:

#### Prerequisites:

- Ensure you have Python installed on your system.
- Install the requirements.txt file using pip:
```bash
 pip install -r rquirements.txt
```
- Install the [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) library (instructions vary based on your operating system).
- Create a .env file in the same directory as your code and add your Google API key as 
```bash
GOOGLE_API_KEY=your_api_key 
```

#### Running the App:
- Navigate to the directory containing your code in your terminal.
- Run the command: (replace with your actual filename).
```bash
 streamlit run app.py

```
- The app will open in your web browser.

#### Additional Notes:
- The code requires a valid Google API key with access to Gemini Pro. Get API KEY from [Google AI Studio](https://makersuite.google.com/app/apikey)
- The pdf2image library requires the [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) library to be installed.

