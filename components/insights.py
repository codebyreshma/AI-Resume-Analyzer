import streamlit as st


def render_insights(result):

    st.divider()

    st.subheader("📊 AI Analysis")

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

    st.subheader("🤖 AI Insights")

    tab1, tab2, tab3, tab4 = st.tabs([
        "💪 Strengths",
        "⚠️ Weaknesses",
        "💡 Suggestions",
        "🎤 Interview"
    ])

    with tab1:
        for item in result["strengths"]:
            st.markdown(f"✅ {item}")

    with tab2:
        for item in result["weaknesses"]:
            st.markdown(f"⚠️ {item}")

    with tab3:
        for item in result["suggestions"]:
            st.markdown(f"💡 {item}")

    with tab4:
        st.metric(
            "Interview Readiness",
            result["interview_readiness"]
        )
        