import streamlit as st
from anyio import value

st.title("Cold Mail Generator")
url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-39343?from=job%20search%20funnel")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager, I am from AnBiz", language='markdown')



