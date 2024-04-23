#import json

# Provide the specific path to your JSON file
json_file_path = "/Users/stephaniezhang/Desktop/EV_Data.json"

# Load the JSON file
#with open(json_file_path, "r") as file:
    ev_data = json.load(file)


# Function to get available EV brands
def get_ev_brands():
    return [ev['brand'] for ev in ev_data['electric_vehicles']]

# Function to get models for a specific brand
def get_ev_models(brand):
    models = [ev['model'] for ev in ev_data['electric_vehicles'] if ev['brand'] == brand]
    return models

# Function to get main features of a specific model
def get_ev_features(brand, model):
    for ev in ev_data['electric_vehicles']:
        if ev['brand'] == brand and ev['model'] == model:
            return ev['main_features']
    return None

# Function to get pricing of a specific model
def get_ev_price(brand, model):
    for ev in ev_data['electric_vehicles']:
        if ev['brand'] == brand and ev['model'] == model:
            return ev['price']
    return None

# Function to get offers for a specific model
def get_ev_offers(brand, model):
    for ev in ev_data['electric_vehicles']:
        if ev['brand'] == brand and ev['model'] == model:
            return ev['applicable_offers']
    return None


import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")


# Chatbot response function
def chatbot_response(user_input):
    # Process user input
    doc = nlp(user_input)

    # Check for EV brands mentioned in user input
    brand = None
    model = None
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT"]:
            brand = ent.text
            if brand in get_ev_brands():
                model = None
                # Check if user asked about a specific model of this brand
                model = next((m for m in get_ev_models(brand) if m in user_input), None)
                break

    # Handle various types of user queries
    if "brand" in user_input.lower() or "makes" in user_input.lower():
        brands = get_ev_brands()
        return f"We offer EVs from the following brands: {', '.join(brands)}."

    if "model" in user_input.lower() and brand:
        models = get_ev_models(brand)
        return f"{brand} offers the following models: {', '.join(models)}."

    if model:
        # Provide details about the model
        features = get_ev_features(brand, model)
        price = get_ev_price(brand, model)
        offers = get_ev_offers(brand, model)

        features_str = f"Battery capacity: {features['battery_capacity_kWh']} kWh, " \
                       f"range: {features['range_miles']} miles, " \
                       f"0-60 mph acceleration: {features['acceleration_0_60_mph']} seconds, " \
                       f"fast charging time: {features['charging_time_hours']['fast_charge']} hours, " \
                       f"normal charging time: {features['charging_time_hours']['normal_charge']} hours, " \
                       f"seating capacity: {features['seating_capacity']}"

        offers_str = ", ".join([f"{key.replace('_', ' ').title()}: ${value}" for key, value in offers.items()])

        return f"{brand} {model}: {features_str}. Price: ${price}. Offers: {offers_str}."

    # Default response
    return "I'm sorry, I didn't understand that question. Can you please rephrase it?"


### 4. **Chat Interface**

#Here's how you can set up a chat interface for interacting with the chatbot:

#```python
print("Chatbot: Hey, how can I help you with electric vehicles today?")
while True:
    # Get user input
    user_input = input("User: ")

    # Exit if the user types "exit"
    if user_input.lower() == "exit":
        print("Chatbot: Thanks for chatting! Let me know if you need more help!")
        break

    # Get the chatbot's response
    response = chatbot_response(user_input)

    # Display the chatbot's response
    print(f"Chatbot: {response}")

