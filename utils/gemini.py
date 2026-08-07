import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Compare the resume with the provided Job Description.

Return your response in EXACTLY this format.

Resume Score: XX/100

ATS Score: XX/100

Resume Match Score: XX%

Interview Readiness: High / Medium / Low

---

## ✅ Matching Skills
Return ONLY a comma-separated list.

Example:
Python, SQL, Git, HTML

## ❌ Missing Skills
Return ONLY a comma-separated list.

Example:
Docker, AWS, Kubernetes

## 💪 Strengths
- Point
- Point

## ⚠ Weaknesses
- Point
- Point

## 💡 Suggestions
- Point
- Point
Resume:

{resume_text}

Job Description:

{job_description}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return completion.choices[0].message.content