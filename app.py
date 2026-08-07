import streamlit as st
import re
from utils.pdf_reader import extract_text
from utils.gemini import analyze_resume
import pandas as pd

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)
if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("""
<style>

.stButton>button{
    background:#4F46E5;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stDownloadButton>button{
    background:#16A34A;
    color:white;
    border-radius:10px;
    height:45px;
}

div[data-testid="stMetric"]{
    background:#f5f5f5;
    padding:15px;
    border-radius:12px;
    border:1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# Sidebar
# =====================================

with st.sidebar:
    st.title("🤖 AI Resume Analyzer")

    st.markdown("---")

    st.success("### 🚀 Features")

    st.markdown("""
- 📄 Resume Upload
- 💼 Job Description Matching
- 📊 Resume Score
- 🎯 ATS Score
- 💡 AI Suggestions
- 🚀 Interview Readiness
""")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.markdown("""
- Python
- Streamlit
- Groq AI
- PDFPlumber
""")

    st.markdown("---")

    st.caption("Made by Reshma ❤️")

# =====================================
# Main Page
# =====================================

st.title("🤖 AI Resume Analyzer")

st.caption(
    "Upload your resume and compare it with a Job Description using AI."
)

st.divider()

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"],
    help="Only PDF files are supported."
)

st.subheader("💼 Job Description")

job_description = st.text_area(
    "Paste the Job Description",
    height=200,
    placeholder="Paste the company's job description here..."
)

# =====================================
# Helper Functions
# =====================================

def extract_score(pattern, text, suffix):
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if match:
        return match.group(1) + suffix

    return "N/A"

# =====================================
# Resume Processing
# =====================================

if uploaded_file is not None:

    resume_text = extract_text(uploaded_file)

    st.success("✅ Resume uploaded successfully!")

    with st.expander("📄 View Extracted Resume"):
        st.text_area(
            "",
            resume_text,
            height=250
        )

    st.divider()

    if st.button("🚀 Analyze Resume", use_container_width=True):

        try:

            with st.spinner("🤖 AI is analyzing your resume..."):

                result = analyze_resume(
                    resume_text,
                    job_description
                )

            # =====================================
            # Extract Scores
            # =====================================

            resume_score = extract_score(
                r"Resume Score.*?(\d+)\s*/\s*100",
                result,
                "/100"
            )

            ats_score = extract_score(
                r"ATS Score.*?(\d+)\s*/\s*100",
                result,
                "/100"
            )

            match = re.search(
                r"Resume Match Score.*?(\d+)\s*/\s*100|Resume Match Score.*?(\d+)%",
                result,
                re.IGNORECASE | re.DOTALL
            )

            if match:
                match_score = (match.group(1) or match.group(2)) + "%"
            else:
                match_score = "N/A"

            # =====================================
            # Score Cards
            # =====================================

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "📄 Resume Score",
                    resume_score
                )

            with col2:
                st.metric(
                    "🎯 ATS Score",
                    ats_score
                )

            with col3:
                st.metric(
                    "💼 Match Score",
                    match_score
                )

            st.session_state.history.append({
                "Resume Score": resume_score,
                "ATS Score": ats_score,
                "Match Score": match_score
            })
            # =====================================
            # Progress Bars
            # =====================================

            st.subheader("📈 Score Breakdown")

            if resume_score != "N/A":
                st.write(f"📄 Resume Score: **{resume_score}**")
                st.progress(int(resume_score.replace('/100', '')) / 100)

            if ats_score != "N/A":
                st.write(f"🎯 ATS Score: **{ats_score}**")
                st.progress(int(ats_score.replace('/100', '')) / 100)

            if match_score != "N/A":
                st.write(f"💼 Match Score: **{match_score}**")
                st.progress(int(match_score.replace('%', '')) / 100)

            st.divider()

            # =====================================
            # AI Report
            # =====================================

            st.subheader("📊 AI Analysis")

        
            # ---------- Display AI Report ----------

            sections = result.split("##")

            for section in sections:
                section = section.strip()

                if not section:
                    continue

                if "Matching Skills" in section:
                    st.success("✅ " + section)

                elif "Missing Skills" in section:
                    st.error("❌ " + section)

                elif "Strengths" in section:
                    st.info("💪 " + section)

                elif "Weaknesses" in section:
                    st.warning("⚠️ " + section)

                elif "Suggestions" in section:
                    st.success("💡 " + section)

                else:
                    st.markdown("## " + section)

        

 

            st.download_button(
               label="📥 Download AI Report",
               data=result,
               file_name="AI_Resume_Report.txt",
               mime="text/plain",
               use_container_width=True
           )

            if st.session_state.history:

              st.divider()

              st.subheader("📜 Analysis History")

              history_df = pd.DataFrame(st.session_state.history)

              st.dataframe(
              history_df,
              use_container_width=True
            )

        except Exception as e:

            st.error("❌ Something went wrong while analyzing the resume.")

            with st.expander("Technical Details"):
                st.code(str(e))