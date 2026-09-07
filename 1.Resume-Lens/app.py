import os
from io import BytesIO

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pypdf import PdfReader

load_dotenv()

st.set_page_config(page_title="Resume Lens", page_icon="RL", layout="wide")


def extract_resume_text(uploaded_file) -> str:
    """Extract readable text from the supported resume formats."""
    file_name = uploaded_file.name.lower()
    file_bytes = uploaded_file.getvalue()

    if file_name.endswith(".pdf"):
        reader = PdfReader(BytesIO(file_bytes))
        return "\n".join(page.extract_text() or "" for page in reader.pages).strip()

    if file_name.endswith(".txt"):
        return file_bytes.decode("utf-8", errors="replace").strip()

    if file_name.endswith(".docx"):
        from docx import Document

        document = Document(BytesIO(file_bytes))
        return "\n".join(paragraph.text for paragraph in document.paragraphs).strip()

    raise ValueError("Unsupported file type. Upload a PDF, DOCX, or TXT file.")


def screen_resume(resume_text: str, job_description: str) -> str:
    model = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        temperature=0.1,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a careful recruiting assistant. Compare the resume to the job description using only evidence in the supplied text. Do not infer protected characteristics or make a final hiring decision. Return markdown with exactly these headings: ## Match Score, ## Strengths, ## Gaps, ## Evidence, ## Interview Focus. Give Match Score as a whole-number percentage and explain the score briefly. Flag missing information as unknown instead of treating it as a weakness.""",
            ),
            (
                "human",
                "Job description:\n{job_description}\n\nResume:\n{resume_text}",
            ),
        ]
    )
    response = (prompt | model).invoke(
        {"job_description": job_description, "resume_text": resume_text}
    )
    return response.content if isinstance(response.content, str) else str(response.content)


st.title("Resume Lens")
st.caption("Evidence-based resume screening with Gemini")

with st.sidebar:
    st.header("Screen a candidate")
    uploaded_file = st.file_uploader(
        "Resume", type=["pdf", "docx", "txt"], help="PDF, DOCX, or plain text"
    )
    job_description = st.text_area(
        "Job description", height=280, placeholder="Paste the role requirements here..."
    )
    screen_button = st.button(
        "Analyze resume", type="primary", use_container_width=True
    )

if not os.getenv("GOOGLE_API_KEY"):
    st.info("Add GOOGLE_API_KEY to .env before running an analysis.")

if screen_button:
    if not uploaded_file:
        st.error("Upload a resume first.")
    elif not job_description.strip():
        st.error("Paste a job description first.")
    else:
        try:
            resume_text = extract_resume_text(uploaded_file)
            if not resume_text:
                st.error("No readable text was found in that resume.")
            else:
                with st.spinner("Comparing resume evidence with the role..."):
                    report = screen_resume(resume_text, job_description)
                st.markdown(report)
        except Exception as error:
            st.error(f"Analysis failed: {error}")
else:
    st.markdown(
        "Upload a resume and paste a job description to see the candidate's match score, strengths, gaps, evidence, and interview focus."
    )
