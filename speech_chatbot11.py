import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections
import speech_recognition as sr
from PIL import Image
# Download the NLTK data (if not already downloaded)
nltk.download('punkt')
image = Image.open('C:\\Users\\Dr. Ibrahim Nuhu\\Downloads\\pexels-kindel-media-8566470.jpg')
with open('C:\\Users\\Dr. Ibrahim Nuhu\\Downloads\\Bipolar disorder.txt', 'r', encoding='utf-8') as f:
    pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot.",]
    ],
    # Add more patterns and responses as needed
]

# Define a function to transcribe speech into text using the speech recognition algorithm
def transcribe_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening... Speak something!")
        audio_data = recognizer.listen(source)

    st.success("Speech recognition complete!")
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        st.error("Speech recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Modify the chatbot function to take both text and speech input
def chatbot(input_text):
    chat = Chat(pairs, reflections)
    return chat.respond(input_text)

# Create Streamlit app
def main():
    st.title("Speech-Enabled Chatbot")

    # User input option (text or speech)
    input_option = st.radio("Select input option:", ["Text Input", "Speech Input"])

    if input_option == "Text Input":
        # Text input
        user_input = st.text_input("Enter your message:")
    else:
        # Speech input
        user_input = transcribe_speech()

    if user_input:
        # Get chatbot response
        bot_response = chatbot(user_input)

        # Display user input and chatbot response
        st.text(f"You: {user_input}")
        st.text(f"Chatbot: {bot_response}")

# Run the Streamlit app
if __name__ == "__main__":
    main()