import os
from PIL import Image
import speech_recognition as sr
import streamlit as st
from googletrans import LANGUAGES
from streamlit_option_menu import option_menu
from transformers import pipeline  # Import from transformers library
from gemini_utility import load_gemini_pro_model, gemini_pro_response, gemini_pro_vision_response, \
    embeddings_model_response
from text_translate import translate_text  # Import the translate_text function
import pyttsx3  # For text-to-speech


# Sidebar menu options with speech recognition toggle
with st.sidebar:
    st.markdown("# Navigation")
    selected_page = st.radio("Go to", ["Home", "About", "Features/Specifications"])

if selected_page == "Home":
    st.title("Home Page")
    st.write("Welcome to the Query Agent application!")
    st.write("This app utilizes advanced AI technologies to provide a versatile set of functionalities, catering to various user needs. Whether you're looking to interact with an AI assistant, analyze sentiment, translate text, or generate captions for images, Query Agent has you covered.")

    st.header("Key Features:")
    st.markdown("- **ChatBot:** Engage in conversations with an AI assistant powered by Gemini-Pro.")
    st.markdown("- **Image Captioning:** Generate descriptive captions for uploaded images.")
    st.markdown("- **Text Translation:** Seamlessly translate text into multiple languages using Google Translate.")
    st.markdown("- **Sentiment Analysis:** Analyze the sentiment of text inputs in real-time.")
    st.markdown("- **Embeddings:** Obtain embeddings for textual data to facilitate advanced search and retrieval tasks.")
    st.markdown("- **Speech Recognition:** Optionally enable speech recognition for hands-free interaction.")

    st.header("How to Use:")
    st.markdown("1. **Navigation:** Use the sidebar to navigate between different sections.")
    st.markdown("2. **Interaction:** Explore each section to experience the capabilities of Query Agent.")
    st.markdown("3. **Customization:** Configure options like speech recognition and speaking responses as per your preference.")

    st.header("Why Choose Query Agent?")
    st.markdown("- **Efficiency:** Perform complex tasks quickly with AI-driven automation.")
    st.markdown("- **Versatility:** Handle a wide range of tasks from language translation to sentiment analysis.")
    st.markdown("- **User-friendly:** Simple interface designed for intuitive use by all users.")
    st.markdown("- **Cutting-edge Technology:** Leveraging state-of-the-art AI models to ensure accurate and reliable results.")

    st.header("Get Started")
    st.markdown("Ready to explore Query Agent? Navigate to the sidebar and select a section to begin.")

elif selected_page == "About":
    st.title("About Page")
    st.write("Welcome to the About page of the Query Agent application!")
    st.write("Query Agent is an innovative AI-powered application designed to assist users with a variety of tasks using cutting-edge technologies.")

    st.header("Mission Statement")
    st.markdown("Our mission is to simplify complex tasks through the application of AI, making everyday interactions smarter and more efficient.")

    st.header("Key Objectives")
    st.markdown("- **Enhanced User Experience:** Provide seamless interaction through intuitive interfaces.")
    st.markdown("- **AI Integration:** Integrate advanced AI models to deliver accurate and timely results.")
    st.markdown("- **Continuous Improvement:** Evolve with user feedback and technological advancements to stay ahead.")

    st.header("Our Team")
    st.markdown("The development team behind Query Agent comprises passionate individuals dedicated to pushing the boundaries of AI applications.")
    st.markdown("Meet the minds behind Query Agent who strive to deliver excellence in every interaction.")

    st.header("Contact Us")
    st.markdown("Have questions or feedback? We'd love to hear from you!")
    st.markdown("- Email: queryagent@example.com")
    st.markdown("- Website: [www.queryagent.com](http://www.queryagent.com)")
    st.markdown("- Social Media: Follow us on Twitter, Facebook, and LinkedIn for updates.")



elif selected_page == "Features/Specifications":
    st.title("Features and Specifications")
    st.write("Here are the detailed features and specifications of Query Agent:")

    st.header("ChatBot")
    st.write("- **Functionality:** Interact with an AI-powered assistant.")
    st.write("- **Description:** Engage in conversations and receive responses generated by the Gemini-Pro model.")
    st.write("- **Technology:** Utilizes natural language processing (NLP) and generative AI for dialogue generation.")

    st.header("Image Captioning")
    st.write("- **Functionality:** Automatically generate captions for uploaded images.")
    st.write("- **Description:** Uses computer vision techniques to analyze and describe visual content.")
    st.write("- **Technology:** Powered by Gemini-Pro-Vision model for image understanding and text generation.")

    st.header("Embed Text")
    st.write("- **Functionality:** Obtain embeddings for textual data.")
    st.write("- **Description:** Converts text into numerical representations for semantic similarity and information retrieval.")
    st.write("- **Technology:** Uses embedding models trained on large text corpora for encoding text into vector spaces.")

    st.header("Ask me anything")
    st.write("- **Functionality:** Provides responses to general queries and questions.")
    st.write("- **Description:** Uses advanced AI capabilities to understand and generate relevant responses.")
    st.write("- **Technology:** Driven by the Gemini-Pro model for text generation and information retrieval.")

    st.header("Text Translation")
    st.write("- **Functionality:** Translate text into different languages.")
    st.write("- **Description:** Facilitates communication across language barriers.")
    st.write("- **Technology:** Integrates with Google Translate API for accurate and efficient language translation.")

    st.header("Sentiment Analysis")
    st.write("- **Functionality:** Analyze sentiment of text inputs.")
    st.write("- **Description:** Determines the emotional tone expressed in textual content.")
    st.write("- **Technology:** Uses Hugging Face Transformers pipeline for sentiment classification.")

    st.write("The Query Agent application integrates various AI models and libraries to deliver these functionalities, ensuring robust performance and accurate results.")

# Display footer or additional information
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by [AI ASPIRANT]")
