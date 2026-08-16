import streamlit as st


def render_checklist(checklist):

    st.divider()

    st.subheader("✅ Resume Improvement Checklist")

    st.caption(
        "Complete these tasks to improve your resume for this role."
    )

    for task in checklist:
        st.checkbox(task, value=False)