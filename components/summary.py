import streamlit as st


def render_summary(
    resume_score,
    ats_score,
    match_score,
    match_value,
    verdict,
    recommendation
):

    st.info(f"""
### 📝 Quick Summary

📄 **Resume Score:** {resume_score}

🎯 **ATS Score:** {ats_score}

💼 **Match Score:** {match_score}

---

{verdict}

### 🚀 Recommendation

{recommendation}
""")

    st.subheader("⭐ Ideal Candidate Score")

    st.progress(match_value / 100)

    st.caption(
        f"You currently match approximately **{match_value}%** of the ideal candidate profile."
    )