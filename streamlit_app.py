import streamlit as st
import gfu
import google.generativeai as genai

# Configure the Google API key
GOOGLE_API_KEY = 'AIzaSyDk71ZfWHqL6A2MoyqQVsVTz3s9L4Dtk_I'
genai.configure(api_key=GOOGLE_API_KEY)

# Create the GenerativeModel
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_and_summarize():
    question = st.text_input("Enter your question:")
    if not '.' in question:
        response1 = model.generate_content("No additional text, just the best search query for " + question)
        url = response1.text  # Extract the first URL
    else:
        url = question

    # Concatenate the strings correctly
    summary_query = "Can you summarize " + gfu.get_first_url(url) + " and answer the question: " + question
    response2 = model.generate_content(summary_query)
    summary_text = response2.text + url

    # Display the summary
    st.write(summary_text)

# Main app
st.title("Google Gemini Content Generator")
generate_and_summarize()
