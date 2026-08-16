import streamlit as st


def render_cover_letter(cover_letter):

    st.divider()

    st.subheader("📄 AI Cover Letter")

    st.caption("A personalized cover letter generated for this job.")

    with st.expander("View Cover Letter", expanded=False):
        st.write(cover_letter)

    st.download_button(
        label="📥 Download Cover Letter",
        data=cover_letter,
        file_name="Cover_Letter.txt",
        mime="text/plain",
        use_container_width=True
    )