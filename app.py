
import base64
import streamlit as stl
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the Maker Suit Google API from https://makersuite.google.com/app/apikey
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 
def get_gemini_response(input, resume_pdf_cotent, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, resume_pdf_cotent[0], prompt])
    return response.text

#
def resume_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        current_page = images[0]

        # Convert into bytes
        img_byte_array = io.BytesIO()
        current_page.save(img_byte_array, format='JPEG')
        img_byte_array = img_byte_array.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                # encode to base64
                "data": base64.b64encode(img_byte_array).decode()  
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

#==================== Streamlit App =====================#

stl.set_page_config(page_title="ATS - Resume Builder Expert")
stl.header("ATS - Application Tracking System")
input_text = stl.text_area("Job Description: ", key="input")
uploaded_file = stl.file_uploader("Upload your resume(PDF)...", type=["pdf"])


if uploaded_file is not None:
    stl.write("PDF Uploaded Successfully")


submit1 = stl.button("Tell Me About this Resume")

submit2 = stl.button("How Can I Improvise my Skills")

submit3 = stl.button("Percentage match")


## Write all prompt 
input_prompt1 = """
 You are an experienced AI HR Manager, your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an experienced career coach with expertise in resume optimization.
Review the provided resume and job description, and provide specific recommendations on how the candidate can improve their skills and experience to better match the job requirements.
Focus on actionable steps the candidate can take to enhance their qualifications.
"""


input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science, machine learning, software development, 
backend development, frontend development, data analysis, devops and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt = """
You are an experienced ATS (Applicant Tracking System) scanner specialized in software development, data science, machine learning, software development, 
backend development, frontend development, data analysis, roles. 
Your task is to assess the resume against the given job description for a Software Developer position. 
Provide the percentage match, list any key skills or technologies that are missing, and share your final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        resume_pdf_content = resume_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, resume_pdf_content, input_text)
        stl.subheader("The Repsonse is")
        stl.write(response)
    else:
        stl.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        resume_pdf_content = resume_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, resume_pdf_content, input_text)
        stl.subheader("Skill Improvement Recommendations")
        stl.write(response)
    else:
        stl.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        resume_pdf_content = resume_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt,  resume_pdf_content, input_text)
        stl.subheader("The Repsonse is")
        stl.write(response)
    else:
        stl.write("Please upload the resume") 