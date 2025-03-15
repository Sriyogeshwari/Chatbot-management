import json
import datetime

class Chatbot:
    def __init__(self, bot_name, response_file="responses.json"):
        self.bot_name = bot_name
        self.conversations = []
        self.response_file = r'C:\projects\ChatBot\responses.json'
        self.responses = self.load_responses()

    def load_responses(self):
        """Load responses from a JSON file."""
        try:
            with open(self.response_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_responses(self):
        """Save responses back to the JSON file."""
        with open(self.response_file, 'w') as file:
            json.dump(self.responses, file, indent=4)

    def respond(self, user_input):
        return self.responses.get(user_input.lower(), "I'm not sure about that. Can you rephrase?")

    def update_response(self, user_input, bot_response):
        """Update or add a new response dynamically."""
        self.responses[user_input.lower()] = bot_response
        self.save_responses()
        print(f"Response updated: '{user_input}' → '{bot_response}'")

    def log_conversation(self, user_input, response):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conversations.append({"timestamp": timestamp, "user": user_input, "bot": response})

    def save_logs(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.conversations, file, indent=4)

class ChatbotManager:
    def __init__(self):
        self.chatbots = {}

    def create_chatbot(self, bot_name):
        if bot_name in self.chatbots:
            print(f"Chatbot '{bot_name}' already exists.")
        else:
            self.chatbots[bot_name] = Chatbot(bot_name)
            print(f"Chatbot '{bot_name}' created successfully.")

    def get_chatbot(self, bot_name):
        return self.chatbots.get(bot_name, None)

    def list_chatbots(self):
        return list(self.chatbots.keys())

if __name__ == "__main__":
    manager = ChatbotManager()
    manager.create_chatbot("SupportBot")
    bot = manager.get_chatbot("SupportBot")

    if bot:
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                bot.save_logs("chat_logs.json")
                print("Chat logs saved. Exiting...")
                break
            elif user_input.startswith("train:"):
                # Training format: train:question|answer
                try:
                    _, data = user_input.split(":", 1)
                    question, answer = data.split("|", 1)
                    bot.update_response(question.strip(), answer.strip())
                except ValueError:
                    print("Invalid training format. Use: train:question|answer")
            else:
                response = bot.respond(user_input)
                bot.log_conversation(user_input, response)
                print(f"{bot.bot_name}: {response}")
