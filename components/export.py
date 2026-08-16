import streamlit as st


def render_export(
    resume_score,
    ats_score,
    match_score,
    result
):

    st.divider()

    st.subheader("📥 Export Report")

    st.caption(
        "Download your AI-generated resume analysis as a PDF."
    )

    with open("AI_Resume_Report.pdf", "rb") as pdf_file:

        st.download_button(
            label="📄 Download Professional PDF",
            data=pdf_file,
            file_name="AI_Resume_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )