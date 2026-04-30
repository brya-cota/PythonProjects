'''
Brya Cota
CSC101
4/28/26
'''

# chatbot.py
# Skeleton code for the Python Chatbot Project
# Follows required project structure and class design
import random

class Chatbot:
    """A simple command-line chatbot framework."""
    def __init__(self, name):
        """Initialize bot name, memory storage, and active flag."""
        self.name = name
        self.memory = {} # Dictionary to store user data
        self.active = True # Controls conversation loop

    def greet_user(self):
        """Greet the user and collect/store their name."""
        # TODO: Print greeting
        self.name = "Zo"
        print(f"Greetings user - my name is {self.name}, your personal chatbot.")

        # TODO: Ask for user's name
        user_name = input("What is your name? ")

        # TODO: Store name in memory dictionary
        self.memory["user_name"] = user_name.title()

        # TODO: Acknowledge user by name
        print(f"Hello {self.memory['user_name']}, welcome! Let's chat.")
        pass

    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.
        Should handle:
        hi → random greeting
        how are you → random status message
        bye → farewell
        name → recall stored user name
        color → ask and store favorite color
        favorite → recall favorite color
        exit → set active=False
        """
        # Greetings and status_message lists to create a random response from
        greetings = ["Hi!", "Howdy!", "Greetings Earthling.", "Hey there!"]
        status_message = ["I'm just peachy!", "I'm doing ok.", "I've had better days.", "I'm fantastic!"]

        # TODO: Clean user_input (lowercase, strip punctuation)
        user_input = user_input.lower().strip()

        # TODO: Write conditional logic for supported commands
        # TODO: Return a chatbot response string
        if "hi" in user_input:
            return random.choice(greetings)
        elif "how are you" in user_input or "how're you" in user_input:
            return random.choice(status_message)
        elif "bye" in user_input:
            return "Farewell friend."
        elif "name" in user_input:
            return f"Your name is {self.memory.get('user_name')}"
        elif "color" in user_input:
            favorite_color = user_input.lower().strip()
            self.memory["color"] = favorite_color.lower()
            return f"I love that color! Although, I prefer pink to all other colors."
        elif "favorite" in user_input:
            return f"I remember! Your favorite color is: {self.memory.get('color')}"
        elif "exit" in user_input:
            self.active = False
            return "Talk to ya later!"
        else:
            return "Sorry, I don't understand."
        pass

    def chat(self):
        """Main conversation loop."""
        # TODO: Start loop while self.active is True
        while self.active:
            # TODO: Prompt user for input
            input_prompt = input("What would you like to do? Start with a greeting, ask me how I'm doing or tell me a"
                                 " color that you like. To end our chat, just type 'exit'. ")
            # TODO: Call get_response()
            response = self.get_response(user_input = input_prompt)
        # TODO: Print bot response with prefix (e.g., PyBot: ...)
            print(f"{self.name}: {response}")
        pass

def main():
    """Create a chatbot instance and begin conversation."""
    # TODO: Instantiate Chatbot (object) with a bot name
    zo = Chatbot("Zo")

    # TODO: Call greet_user()
    zo.greet_user()

    # TODO: Start chat loop
    zo.chat()

pass

if __name__ == "__main__":
    main()
