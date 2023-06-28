# import streamlit as st
# from st_files_connection import FilesConnection

# "# Minimal FilesConnection example"
# with st.echo():
#     conn = st.experimental_connection('my_connection', type=FilesConnection)

# # Write a file to local directory if it doesn't exist
# test_file = "test.txt"
# try:
#     _ = conn.read(test_file, input_format='text')
# except FileNotFoundError:
#     with conn.open(test_file, "wt") as f:
#         f.write("Hello, world!")

# with st.echo():
#     # Read back the contents of the file
#     st.write(conn.read(test_file, input_format='text'))