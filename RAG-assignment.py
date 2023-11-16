from openai import OpenAI
client = OpenAI()

import streamlit as st
from streamlit.logger import get_logger

st.title('Wolf Cove Labs')
st.subheader('My Heading')


file_path = "https://abc.xyz/assets/4a/3e/3e08902c4a45b5cf530e267cf818/2023q3-alphabet-earnings-release.pdf"

file = client.files.create(
  file=open(file_path, "rb"),
  purpose='assistants'
)

st.header("GPT 4 Retriever Assistants")
user_message = st.text_input("Pls enter your question:")
submit = st.button("submit", type="primary")
