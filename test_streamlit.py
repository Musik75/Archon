import streamlit as st

st.title("Streamlit Test App")
st.write("Hello, world! This is a test Streamlit app.")

# Display some information about the environment
st.subheader("Environment Information")
import sys
st.write(f"Python version: {sys.version}")
st.write(f"Streamlit version: {st.__version__}")
