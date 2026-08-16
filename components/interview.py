import streamlit as st


def render_interview_questions(interview_questions):

    st.divider()

    st.subheader("🎤 AI Interview Questions")

    st.caption("Practice these questions before your interview.")

    for i, question in enumerate(interview_questions, start=1):

        with st.expander(f"Question {i}"):

            st.write(question)