import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Chatbot response function
def chatbot_response(user_input):
    # Process the user input
    doc = nlp(user_input)

    # Define responses based on keywords and topics
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Hello! How can I help you with electric vehicles today?"

    if "electric vehicle" in user_input.lower() or "ev" in user_input.lower():
        return "Electric vehicles are environmentally friendly and cost-effective in the long run. They offer great performance and a quiet ride."

    if "range" in user_input.lower():
        return "The average range of electric vehicles varies depending on the model, but many EVs can travel between 200 to 300 miles on a single charge."

    if "charging" in user_input.lower():
        return "Charging an electric vehicle can be done at home or at public charging stations. Fast chargers can recharge an EV in about 30 minutes to an hour."

    if "price" in user_input.lower():
        return "The price of electric vehicles varies depending on the make and model. Some EVs start as low as $35,000, while others can cost over $100,000."

    if "warranty" in user_input.lower():
        return "Most electric vehicles come with a warranty of around 8 years or 100,000 miles on the battery. Other components are typically covered for 3 to 5 years."

    if "bye" in user_input.lower():
        return "Goodbye! Let me know if you need any more help with electric vehicles."

    # Default response
    return "I'm sorry, I didn't understand that question. Can you please rephrase it?"

# Chat interface
print("Chatbot: Hello! How can I help you with electric vehicles today?")
while True:
    # Get user input
    user_input = input("User: ")

    # Exit if the user types "exit" or "bye"
    if user_input.lower() in ["exit", "bye"]:
        print("Chatbot: Goodbye! Let me know if you need any more help!")
        break

    # Get the chatbot's response
    response = chatbot_response(user_input)

    # Display the chatbot's response
    print(f"Chatbot: {response}")
