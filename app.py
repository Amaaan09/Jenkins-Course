import streamlit as st
import time

def display_message(message):
    placeholder = st.empty()
    placeholder.write(message)
    time.sleep(2)
    placeholder.empty()


st.title("This is a simple Streamlit app.")

stored_inp = st.text_input("Enter your name")

if st.button("Submit"):
    display_message(f"Hello {stored_inp.upper()}!")
