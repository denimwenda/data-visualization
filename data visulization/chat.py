import random

# Define a list of user inputs and corresponding chatbot responses
conversations = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a computer program, so I don't have feelings, but I'm here to help!",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "default": "I'm sorry, I don't understand. Please ask another question or provide more details."
}


# Function to get a response from the chatbot
def get_response(user_input):
    user_input = user_input.lower()
    response = conversations.get(user_input, conversations["default"])
    return response


# Main chatbot loop
print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    response = get_response(user_input)
    print("Chatbot:", response)