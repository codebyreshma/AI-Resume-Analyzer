import streamlit as st
import pandas as pd


def render_history(history):

    if history:

        st.divider()

        with st.expander("📜 Previous Analyses"):

            history_df = pd.DataFrame(history)

            history_df.index = history_df.index + 1

            st.dataframe(
                history_df,
                use_container_width=True,
                hide_index=False
            )