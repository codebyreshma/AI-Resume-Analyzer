import streamlit as st


def render_keyword_analysis(matched_keywords, missing_keywords):

    st.divider()

    st.subheader("🔍 Keyword Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### ✅ Keywords Found")

        if matched_keywords:
            for keyword in matched_keywords:
                st.success(keyword.title())
        else:
            st.info("No matching keywords found.")

    with col2:

        st.markdown("### ❌ Missing Keywords")

        if missing_keywords:
            for keyword in missing_keywords:
                st.error(keyword.title())
        else:
            st.success("No missing keywords 🎉")