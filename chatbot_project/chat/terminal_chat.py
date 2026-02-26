from chatbot import bot

def start_chat():
    print("Hello! I am SimpleBot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break

        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    start_chat()