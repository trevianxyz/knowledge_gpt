# flake8: noqa
import streamlit as st
import pandas as pd
import os

data_df = pd.DataFrame(
    {
        "data": [
            "Harter_McKenna_elml_2022_2_20_58006.pdf",
            "data/vr-cumulative-pacing-guide.csv",
            "data/qa_community.csv",
            "Vex KB",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.LinkColumn(
            "Trending apps",
            help="The top trending Streamlit apps",
            validate="^https://[a-z]+\.streamlit\.app$",
            max_chars=100,
        )
    },
    hide_index=True,
)

# def josh():
#     basepath = 'data/'
#     with os.scandir(basepath) as entries:
#         for entry in entries:
#             if entry.is_file():
#                 print(entry.name)
