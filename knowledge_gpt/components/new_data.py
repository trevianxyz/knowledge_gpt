import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection

"# Streamlit FilesConnection"

"""
A simple demo for Streamlit FilesConnection.
"""

df = pd.DataFrame({"Owner": ["jerry", "barbara", "alex"], "Pet": ["fish", "cat", "puppy"], "Count": [4, 2, 1]})

local, s3, gcs = st.tabs(["Local", "S3", "GCS"])

with local:
    "### Local Access"
    with st.echo():
        conn = st.experimental_connection("local", type=FilesConnection)
        st.help(conn)

    with st.echo():
        with st.expander("View the repo license with help from FilesConnection"):
            license = conn.read('../LICENSE', input_format='text')
            license
# conn.open("path/to/file", mode="rb", *args, **kwargs) -> Iterator[TextIOWrapper | AbstractBufferedFile]