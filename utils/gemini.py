import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Compare the resume with the Job Description.

Return ONLY valid JSON.

Do NOT write markdown.

Do NOT write explanations.

Return EXACTLY this structure:

{{
    "resume_score": 0,
    "ats_score": 0,
    "match_score": 0,
    "interview_readiness": "",

    "matching_skills": [],

    "missing_skills": [],

    "strengths": [],

    "weaknesses": [],

    "suggestions": []
}}

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
        temperature=0.2,
    )

    response = completion.choices[0].message.content

    return json.loads(response)

def generate_interview_questions(resume_text, job_description):

    prompt = f"""
You are an experienced technical interviewer.

Based on the resume and the job description, generate exactly 5 interview questions.

Return ONLY valid JSON in this format:

[
    "Question 1",
    "Question 2",
    "Question 3",
    "Question 4",
    "Question 5"
]

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

    response = completion.choices[0].message.content

    return json.loads(response)

def generate_cover_letter(resume_text, job_description):

    prompt = f"""
You are a professional career coach.

Write a professional cover letter based on the resume and job description.

Requirements:
- Address it to "Hiring Manager"
- Keep it between 250–350 words
- Be professional and persuasive
- Do not use markdown
- Return only the cover letter text

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
        temperature=0.4,
    )

    return completion.choices[0].message.content

def generate_checklist(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Expert.

Based on the resume and job description, create a checklist.

Return ONLY valid JSON.

Example:

[
    "Add Docker to Skills section",
    "Mention GitHub projects",
    "Improve ATS keywords",
    "Quantify achievements",
    "Add certifications"
]

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

    response = completion.choices[0].message.content

    return json.loads(response)