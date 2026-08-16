import streamlit as st

def render_sidebar():

    with st.sidebar:

        st.markdown("# 🤖 AI Resume Analyzer")

        st.caption("AI-powered Resume Review")

        st.divider()

        st.subheader("🚀 Features")

        st.markdown("""
✅ Resume Analysis

✅ ATS Score

✅ Job Match

✅ AI Suggestions

✅ Keyword Analysis

✅ Interview Questions

✅ Cover Letter Generator

✅ Resume Checklist

✅ PDF Report
""")

        st.divider()

        st.subheader("⚙️ Powered By")

        st.markdown("""
- Groq AI
- Streamlit
- Plotly
- PDFPlumber
""")

        st.divider()

        st.caption("Made with ❤️ by Reshma")