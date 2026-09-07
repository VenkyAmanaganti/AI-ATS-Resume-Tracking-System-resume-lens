# Resume Lens

Resume Lens compares a candidate resume with a job description using Gemini through LangChain. It reports a match score, strengths, evidence, gaps, and interview focus without making a final hiring decision.

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and set `GOOGLE_API_KEY`.
4. Start the app:

   ```powershell
   streamlit run app.py
   ```

Supported resume formats are PDF, DOCX, and TXT. The application sends the extracted resume text and job description to Gemini for analysis.

# 📄 Resume Lens — AI-Powered Resume Screening

Resume Lens is an **AI-powered resume screening application** built with **Python, Streamlit, LangChain, and Google Gemini**.

It compares a candidate's resume with a provided job description and generates an evidence-based report containing a **match score, strengths, gaps, supporting evidence, and interview focus areas**.

The application supports **PDF, DOCX, and TXT** resume formats.

---

## 🚀 Features

- 📄 Upload resumes in **PDF, DOCX, or TXT** format
- 📝 Paste a job description
- 🤖 Analyze resumes using **Google Gemini**
- 🔗 Use **LangChain** for prompt management and model interaction
- 📊 Generate an overall **resume-job match percentage**
- 💪 Identify candidate **strengths**
- ⚠️ Identify **gaps** based only on supplied evidence
- 🔍 Provide supporting **evidence from the resume**
- 🎯 Generate **interview focus areas**
- 🛡️ Evidence-based screening without making a final hiring decision
- 🖥️ Simple and interactive **Streamlit UI**

---

## 🛠️ Tech Stack

| TechnologyPurpose |                                       |
| ----------------- | ------------------------------------- |
| Python            | Application development               |
| Streamlit         | Web application interface             |
| Google Gemini     | AI-powered resume analysis            |
| LangChain         | LLM integration and prompt management |
| PyPDF             | Extract text from PDF resumes         |
| python-docx       | Extract text from DOCX resumes        |
| python-dotenv     | Manage environment variables          |

---

## 🏗️ Project Architecture
```vbnet
Resume Lens
│
├── Resume Upload
│   ├── PDF
│   ├── DOCX
│   └── TXT
│
├── Text Extraction
│
├── Job Description
│
├── LangChain Prompt
│
├── Google Gemini
│
└── AI Screening Report
    ├── Match Score
    ├── Strengths
    ├── Gaps
    ├── Evidence
    └── Interview Focus
```

---

## 📂 Project Structure
```
resume-lens/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> Rename your Python file to `app.py` if you want to follow this structure.

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/resume-lens.git
```

Move into the project directory:
```
cd resume-lens
```

### 2. Create a virtual environment
```
python -m venv venv
```

Activate it on Windows:
```
venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API Key

Create a `.env` file in the project root:
```ini
GOOGLE_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.6-flash
```

Get your Gemini API key from **Google AI Studio**.

⚠️ **Never upload your&#x20;****`.env`****&#x20;file or API key to GitHub.**

Add this to `.gitignore`:
```
.env
venv/
__pycache__/
*.pyc
```

---

## 📦 requirements.txt

Create a `requirements.txt` file with:
```
streamlit
python-dotenv
langchain-core
langchain-google-genai
pypdf
python-docx
```

You can also generate it from your environment:
```
pip freeze > requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:
```
streamlit run app.py
```

Streamlit will start the application locally.

Open the displayed local URL in your browser.

---

## 🧑‍💻 How to Use

### Step 1 — Upload Resume

Upload a candidate resume in one of the supported formats:
```
PDF
DOCX
TXT
```

### Step 2 — Enter Job Description

Paste the job description into the job description field.

For example:
```sql
We are looking for a Data Analyst with experience in
Python, SQL, Excel, Power BI, data visualization,
and statistical analysis.
```

### Step 3 — Analyze Resume

Click:
```
Analyze resume
```

### Step 4 — Review AI Report

Resume Lens generates:
```
Match Score
Strengths
Gaps
Evidence
Interview Focus
```

---

## 📊 Example Output
```markdown
## Match Score

82%

The resume demonstrates strong alignment with the
technical requirements of the role.

## Strengths

- Strong SQL experience
- Python knowledge
- Experience with Power BI
- Data analysis experience

## Gaps

- Statistical modeling experience is unknown
- Advanced Excel experience is not clearly stated

## Evidence

- SQL mentioned in technical skills
- Power BI projects included in the resume
- Python used for data analysis

## Interview Focus

- SQL joins and window functions
- Python data analysis
- Power BI dashboards
- Data cleaning techniques
```

---

## 🧠 How It Works

The application follows these steps:

### 1. Resume Upload

The user uploads a resume.

### 2. Text Extraction

The application extracts readable text using:

- `PyPDF` for PDF
- `python-docx` for DOCX
- Python file decoding for TXT

### 3. Job Description Input

The recruiter or user provides the job description.

### 4. Prompt Creation

LangChain creates a structured prompt containing:
```
Job Description
+
Resume
```

### 5. Gemini Analysis

Google Gemini analyzes the resume against the job requirements.

### 6. Structured Report

The model returns:
```
Match Score
Strengths
Gaps
Evidence
Interview Focus
```

---

## 🔐 Responsible AI

Resume Lens is designed to provide **evidence-based screening assistance**.

The AI is instructed to:

- Use only information supplied in the resume and job description
- Avoid inferring protected characteristics
- Avoid making a final hiring decision
- Treat missing information as **unknown**
- Explain the reasoning behind the match score

The tool should be used as an **assistive screening tool**, not as the sole basis for employment decisions.

---

## 🔮 Future Improvements

Possible future enhancements include:

- 📊 Resume scoring dashboard
- 📥 Download analysis as PDF
- 📑 Compare multiple resumes
- 🗂️ Resume history
- 📈 Candidate ranking dashboard
- 🔎 Keyword and skill extraction
- 🎯 Job-specific skill matching
- 📊 Visual match-score charts
- 🧠 Semantic similarity using embeddings
- 🗃️ Resume database
- 🔐 User authentication
- ☁️ Deployment using Streamlit Cloud

---

## 🎯 Use Cases

Resume Lens can be useful for:

- Recruiters
- HR teams
- Job seekers
- Career coaches
- Students
- Data analysts
- Developers
- Small hiring teams

Job seekers can also use it to identify **missing skills and areas to improve before applying**.

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Python
- Streamlit
- Generative AI
- Google Gemini
- LangChain
- Prompt Engineering
- API integration
- PDF processing
- DOCX processing
- Environment variables
- AI-assisted document analysis

---

## 👨‍💻 Author

**Venkateswarlu**

Aspiring Data Analyst | Python | SQL | Power BI | Generative AI

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
