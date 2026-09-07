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

# Resume Lens 🔍

Evidence-based resume screening powered by LangChain and Google Gemini.

## Overview

Resume Lens is a Streamlit app that compares a candidate's resume against a job description and returns a structured, evidence-backed screening report. It's built to support — not replace — human recruiting judgment: it cites evidence from the resume, avoids inferring protected characteristics, and never renders a final hiring decision.

## Features

- **Multi-format resume parsing** — PDF, DOCX, and TXT support
- **Evidence-based screening** — Gemini compares resume text to the job description using only the supplied evidence
- **Structured markdown report** — every analysis returns the same five sections: Match Score, Strengths, Gaps, Evidence, Interview Focus
- **Bias-aware prompting** — the system prompt explicitly avoids inferring protected characteristics and treats missing information as "unknown" rather than a weakness
- **Configurable model** — swap Gemini models via an environment variable without touching code

## Tech Stack

| Layer | Tool |
|---|---|
| UI | [Streamlit](https://streamlit.io/) |
| Prompt orchestration | [LangChain](https://python.langchain.com/) (`ChatPromptTemplate`) |
| LLM | [Gemini](https://ai.google.dev/) via `langchain-google-genai` |
| PDF parsing | [pypdf](https://pypdf.readthedocs.io/) |
| DOCX parsing | [python-docx](https://python-docx.readthedocs.io/) |
| Config | [python-dotenv](https://pypi.org/project/python-dotenv/) |

## Project Structure

```
resume-lens/
├── app.py              # Main Streamlit application
├── .env                # Environment variables (not committed)
└── requirements.txt    # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.9+
- A Google Gemini API key ([get one here](https://ai.google.dev/))

### Installation

```bash
git clone https://github.com/VenkyAmanaganti/resume-lens.git
cd resume-lens
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

`GEMINI_MODEL` is optional and defaults to `gemini-2.5-flash` if not set.

### Running the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## How It Works

1. Upload a resume (PDF, DOCX, or TXT) in the sidebar.
2. Paste the job description into the text area.
3. Click **Analyze resume**.
4. The app extracts plain text from the resume, sends it to Gemini alongside the job description using a screening-focused system prompt, and renders the structured report inline.

## Report Structure

Every analysis returns markdown with five fixed headings:

| Section | Description |
|---|---|
| **Match Score** | Whole-number percentage, with a brief explanation of the score |
| **Strengths** | Candidate strengths backed by resume evidence |
| **Gaps** | Requirements the resume doesn't clearly meet |
| **Evidence** | Specific details pulled from the resume supporting the assessment |
| **Interview Focus** | Suggested areas to probe further in an interview |

## Design Principles

- **Evidence-only** — the model is instructed to rely solely on the supplied resume and job description, not assumptions.
- **Bias-aware** — the system prompt explicitly avoids inferring protected characteristics and stops short of a hiring recommendation.
- **Fair to missing data** — information the resume doesn't cover is flagged as "unknown" rather than counted against the candidate.

## Requirements

```
streamlit
python-dotenv
langchain-core
langchain-google-genai
pypdf
python-docx
```

## Roadmap Ideas

- Batch screening for multiple resumes at once
- Exportable PDF/DOCX report
- Support for additional LLM providers

## License

MIT — feel free to update this section to match your preferred license.

## Author

**Venkatesh** (Amanaganti Venkateswarlu)
- GitHub: [@VenkyAmanaganti](https://github.com/VenkyAmanaganti)
- LinkedIn: [amanagantivenkateswarlu](https://www.linkedin.com/in/amanagantivenkateswarlu)
