import tkinter as tk
import gfu
import google.generativeai as genai
import streamlit as st

# Configure the Google API key
GOOGLE_API_KEY = 'AIzaSyDk71ZfWHqL6A2MoyqQVsVTz3s9L4Dtk_I'
genai.configure(api_key=GOOGLE_API_KEY)

# Create the GenerativeModel
model = genai.GenerativeModel('gemini-pro')

def generate_and_summarize():
    question = input_entry.get()
    if not '.' in question:
        response1 = model.generate_content("No additional text, just the best search query for " + question)
        url = response1.text  # Extract the first URL
    else:
        url = question
    response2 = model.generate_content("Can you summarize " + gfu.get_first_url(url) + "And answer the question" + question)
    summary_text = response2.text + url

    # Display the summary in the UI
    summary_label.config(text=summary_text)

# Create the main UI window
root = tk.Tk()
root.title("Google Gemini Content Generator")

# Input field
input_label = tk.Label(root, text="Enter your question:")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate and Summarize", command=generate_and_summarize)
generate_button.pack()

# Summary label
summary_label = tk.Label(root, text="", wraplength=300)
summary_label.pack()

root.mainloop()
