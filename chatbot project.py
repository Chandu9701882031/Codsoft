def chatbot(question):
    if question.lower() == "hi" or question.lower() == "hello":
        return "Hello there! How can I help you?"
    elif question.lower() == "how are you?":
        return "I'm just a program, but thanks for asking!"
    elif question.lower() == "what is your name?":
        return "I'm a chatbot, you can call me ChatBot."
    elif question.lower() == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that question."

# Example usage:
while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print("ChatBot:", response)
