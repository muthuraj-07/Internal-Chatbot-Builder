import json
import random

class BankingChatbot:
    def __init__(self, responses):
        self.responses = responses

    def get_response(self, user_input):
        user_input = user_input.lower()

        for key, options in self.responses.items():
            if any(keyword in user_input for keyword in options['keywords']):
                if options['responses']:
                    return random.choice(options['responses'])
                else:
                    return f"No response defined for '{key}'."

        return "I'm sorry, I didn't understand that. Please ask another question or type 'help' for assistance."

def load_responses(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data['responses']
    except FileNotFoundError:
        print("No responses file found. Creating a new one.")
        return {}

def save_responses(file_path, responses):
    with open(file_path, 'w') as file:
        json.dump({'responses': responses}, file, indent=2)

def main():
    print("Welcome to the Chatbot Portal!")

    responses = load_responses('responses.json')
    chatbot = BankingChatbot(responses)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

        add_response = input("Do you want to add a response? (yes/no): ").lower()
        if add_response == 'yes':
            keyword = input("Enter a keyword for the response: ").lower()
            user_response = input("Enter the response: ")
            if keyword in responses:
                responses[keyword]['responses'].append(user_response)
            else:
                responses[keyword] = {'keywords': [keyword], 'responses': [user_response]}
            
            save_responses('responses.json', responses)
            print(f"Response for '{keyword}' added successfully.")

if __name__ == "__main__":
    main()
