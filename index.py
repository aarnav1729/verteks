import random

def chatbot(message):
    responses = [
        "I'm sorry, I don't understand.",
        "That's a great question! I'm not sure I know the answer.",
        "I'm not sure what you mean. Can you please rephrase your question?",
        "That's a funny joke! I like it.",
        "I'm not sure I agree with you. What do you think?",
    ]
    return random.choice(responses)

if __name__ == "__main__":
    print(chatbot("What is the meaning of life?"))
    print(chatbot("What is your favorite color?"))
    print(chatbot("What is the capital of France?"))
