import streamlit as st


def render_header():

    st.markdown("""
    <div style="
    background:#2563EB;
    padding:35px;
    border-radius:20px;
    text-align:center;
    margin-bottom:25px;
    ">

    <h1 style="color:white;margin:0;">
    🤖 AI Resume Analyzer
    </h1>

    <p style="color:#E5E7EB;font-size:18px;margin-top:10px;">
    Land your dream job with AI-powered resume analysis
    </p>

    </div>
    """, unsafe_allow_html=True)