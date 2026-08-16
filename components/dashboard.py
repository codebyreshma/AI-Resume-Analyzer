import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def render_dashboard(
    resume_score,
    ats_score,
    match_score,
    resume_value,
    ats_value,
    match_value
):

    st.subheader("📊 Analysis Dashboard")
    st.caption("Your AI-generated resume performance overview.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📄 Resume Score",
            resume_score
        )

        if resume_value >= 80:
            st.success("Excellent")
        elif resume_value >= 60:
            st.warning("Good")
        else:
            st.error("Needs Improvement")

    with col2:
        st.metric(
            "🎯 ATS Score",
            ats_score
        )

        if ats_value >= 80:
            st.success("ATS Friendly")
        elif ats_value >= 60:
            st.warning("Average")
        else:
            st.error("Poor")

    with col3:
        st.metric(
            "💼 Match Score",
            match_score
        )

        if match_value >= 80:
            st.success("Strong Match")
        elif match_value >= 60:
            st.warning("Moderate Match")
        else:
            st.error("Weak Match")

    st.subheader("📈 Score Breakdown")

    st.write(f"📄 Resume Score: **{resume_score}**")
    st.progress(resume_value / 100)

    st.write(f"🎯 ATS Score: **{ats_score}**")
    st.progress(ats_value / 100)

    st.write(f"💼 Match Score: **{match_score}**")
    st.progress(match_value / 100)

    st.divider()

    st.subheader("📊 Score Visualization")

    fig = make_subplots(
        rows=1,
        cols=3,
        specs=[
            [
                {"type": "indicator"},
                {"type": "indicator"},
                {"type": "indicator"}
            ]
        ]
    )

    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=resume_value,
            title={"text": "Resume"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#2563EB"}
            }
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=ats_value,
            title={"text": "ATS"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#10B981"}
            }
        ),
        row=1,
        col=2
    )

    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=match_value,
            title={"text": "Match"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#8B5CF6"}
            }
        ),
        row=1,
        col=3
    )

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )