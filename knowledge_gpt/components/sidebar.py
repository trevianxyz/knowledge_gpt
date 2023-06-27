import streamlit as st
import pandas as pd

from knowledge_gpt.components.faq import faq
# from knowledge_gpt.components.new_side import data_df
# from knowledge_gpt.components.new_data import new_data

def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How tnew testo use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=st.session_state.get("OPENAI_API_KEY", "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"),
        )

        if api_key_input:
            set_openai_api_key(api_key_input)

        # st.markdown(
        #     "📖KnowledgeGPT allows you to ask questions about your "
        #     "documents and get accurate answers with instant citations. "
        # )
        st.markdown(
            "Training Data"
        )
        #st.dataframe(data_df)
        # st.markdown("Made by [mmz_001](https://twitter.com/mm_sasmitha)")
        # st.markdown("---")
        #faq()
        #st.dataframe(new_data)


