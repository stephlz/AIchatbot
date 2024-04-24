import streamlit as st
import json
from textblob import TextBlob

# Load JSON data containing information about EVs
json_file_path = "/Users/stephaniezhang/Desktop/EV_Data.json"

with open(json_file_path, "r") as file:
    ev_data = json.load(file)


# Function to read user emotions using TextBlob
def read_emotion(user_input):
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"


# Chatbot response function
def chatbot_response(user_input):
    # Analyze the user's input and classify their sentiment
    emotion = read_emotion(user_input)

    # Check for keywords and generate responses
    if "buy a car" in user_input.lower() or "i want to buy a car" in user_input.lower():
        response = ("That's great! We have a variety of electric vehicles for you to choose from. "
                    "Would you like to know more about the options we offer?")

    elif "options" in user_input.lower() or "tell me more about the options" in user_input.lower():
        response = ("We offer electric vehicles from top brands with a range of options to suit your needs. "
                    "You can choose from compact cars, sedans, SUVs, and trucks with varying ranges, battery capacities, "
                    "and features. Would you like to hear about the specific models we have available?")

    elif "why buy an ev" in user_input.lower() or "why should i buy an ev" in user_input.lower():
        response = ("There are several reasons to buy an electric vehicle: \n"
                    "- They are environmentally friendly with zero tailpipe emissions. \n"
                    "- EVs have lower operating costs due to reduced fuel and maintenance expenses. \n"
                    "- They offer a smooth and quiet ride. \n"
                    "- You may also be eligible for government incentives and tax credits when purchasing an EV. "
                    "Would you like to know more about the specific EVs we offer?")

    else:
        # Default response if no specific keyword is found
        response = "I'm sorry, I didn't understand that question. Can you please rephrase it?"

    # Add emotional context to the response
    if emotion == "positive":
        response += " It sounds like you are in a good mood!"
    elif emotion == "negative":
        response += " I'm sorry to hear that you might not be in the best mood."
    else:
        response += " Let's find a car that suits you!"

    return response


# Streamlit app title
st.title("EV Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response using chatbot function
    response = chatbot_response(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


