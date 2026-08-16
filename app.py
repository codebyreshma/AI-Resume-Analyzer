import streamlit as st
import re
from components.sidebar import render_sidebar
from components.header import render_header
from components.styles import load_css
from components.keyword_analysis import render_keyword_analysis
from components.interview import render_interview_questions
from components.cover_letter import render_cover_letter
from components.checklist import render_checklist
from components.insights import render_insights
from components.dashboard import render_dashboard
from components.summary import render_summary
from components.export import render_export
from components.history import render_history
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.pdf_reader import extract_text
from utils.gemini import (
    analyze_resume,
    generate_interview_questions,
    generate_cover_letter,
    generate_checklist
)
from utils.analyzer import extract_score
from utils.skills import extract_skills
from utils.pdf_report import generate_pdf
from utils.keyword_matcher import compare_keywords
import pandas as pd




# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

load_css()
if "history" not in st.session_state:
    st.session_state.history = []



# =====================================
# Sidebar
# =====================================

render_sidebar()




# =====================================
# Main Page
# =====================================


render_header()
st.divider()

st.subheader("📄 Upload Your Resume")

st.caption("Upload your resume in PDF format to begin AI analysis.")

uploaded_file = st.file_uploader(
    "",
    type=["pdf"]
)
st.subheader("💼 Job Description")

st.caption("Paste the job description to compare it with your resume.")

job_description = st.text_area(
    "",
    height=200,
    placeholder="Paste the complete job description here..."
)

# =====================================
# Helper Functions
# =====================================

# =====================================
# Resume Processing
# =====================================

if uploaded_file is not None:

    resume_text = extract_text(uploaded_file)

    st.markdown(f"""
    <div style="
        background:#ECFDF5;
        border:1px solid #10B981;
        border-radius:15px;
        padding:18px;
        margin-bottom:20px;
    ">
        <h4 style="color:#065F46;margin:0;">
            ✅ Resume Uploaded Successfully
        </h4>
        <p style="margin:8px 0 0 0;color:#065F46;">
            <b>File:</b> {uploaded_file.name}
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📄 View Extracted Resume", expanded=False):

        st.code(
            resume_text,
            language=None
        )

    st.divider()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
       "🚀 Analyze Resume",
        use_container_width=True,
        type="primary"
    ):
        try:

            with st.spinner("🤖 AI is reviewing your resume against the job description..."):

                result = analyze_resume(
                    resume_text,
                    job_description
                )

                interview_questions = generate_interview_questions(
                    resume_text,
                    job_description
                )
                 
                cover_letter = generate_cover_letter(
                    resume_text,
                    job_description
                )

                matched_keywords, missing_keywords = compare_keywords(
                    resume_text,
                    job_description
                )
                
                checklist = generate_checklist(
                    resume_text,
                    job_description
                )

            st.success("🎉 Analysis completed successfully!")
           
            # =====================================
            # Extract Scores
            # =====================================

            resume_score = f"{result['resume_score']}/100"
            ats_score = f"{result['ats_score']}/100"
            match_score = f"{result['match_score']}%"

            resume_value = result["resume_score"]
            ats_value = result["ats_score"]
            match_value = result["match_score"]

            # =====================================
            # Resume Verdict
            # =====================================

            if match_value >= 85:
                verdict = "🟢 Excellent! Your resume is a strong match for this role."
                recommendation = "✅ You can confidently apply for this role."

            elif match_value >= 70:
                verdict = "🟡 Good match. A few improvements can make it stronger."
                recommendation = "🛠 Improve the missing skills and tailor your resume before applying."

            else:
                verdict = "🔴 Your resume needs significant improvements for this role."
                recommendation = "📚 Focus on gaining the required skills and strengthening your resume first."

            # =====================================
            # Quick Summary
            # =====================================

            render_summary(
                resume_score,
                ats_score,
                match_score,
                match_value,
                verdict,
                recommendation
            )

            # =====================================
            # Score Dashboard
            # =====================================

            render_dashboard(
                resume_score,
                ats_score,
                match_score,
                resume_value,
                ats_value,
                match_value
            )

            st.session_state.history.append({
                "Resume Score": resume_score,
                "ATS Score": ats_score,
                "Match Score": match_score
            })
            
            

            # =====================================
            # AI Report
            # =====================================

            st.divider()

            st.markdown("""
            <h2 style="
                text-align:center;
                color:#2563EB;
                margin-top:20px;
                margin-bottom:5px;
            ">
                🤖 AI Analysis
            </h2>

            <p style="
                text-align:center;
                color:#6B7280;
                margin-bottom:25px;
            ">
                Detailed insights generated by AI
            </p>
            """, unsafe_allow_html=True)

            matching_skills = result["matching_skills"]
            missing_skills = result["missing_skills"]

            if matching_skills:
                st.subheader("✅ Matching Skills")

                cols = st.columns(4)

                for i, skill in enumerate(matching_skills):
                    cols[i % 4].success(skill)

            if missing_skills:
                st.subheader("❌ Missing Skills")

                cols = st.columns(4)

                for i, skill in enumerate(missing_skills):
                    cols[i % 4].error(skill)

            # ---------- Display AI Report ----------

            render_insights(result)
                       
            render_keyword_analysis(
            matched_keywords,
            missing_keywords

            )
            render_interview_questions(
                interview_questions
            )
            
            render_checklist(
                checklist
            ) 
        

 

            generate_pdf(
                 "AI_Resume_Report.pdf",
                 resume_score,
                 ats_score,
                 match_score,
                 str(result)
            )
            render_export(
                resume_score,
                ats_score,
                match_score,
                result
            )

            render_history(
                st.session_state.history
            )

        except Exception as e:

            st.error("❌ Something went wrong while analyzing the resume.")

            with st.expander("Technical Details"):
                st.code(str(e))

st.divider()

st.markdown("""
<div style="
text-align:center;
padding:20px;
color:#6B7280;
font-size:14px;
">

Built with ❤️ by <b>Reshma</b><br>

AI Resume Analyzer • Powered by Groq AI • Streamlit

</div>
""", unsafe_allow_html=True)      
 