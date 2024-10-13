# import json
# import random

# class BankingChatbot:
#     def __init__(self, responses):
#         self.responses = responses
#         self.user_data = {
#             'balance': 1000,
#             'transaction_history': [],
#         }

#     def create_transaction(self, amount, transaction_type):
#         self.user_data['balance'] += amount
#         self.user_data['transaction_history'].append({'type': transaction_type, 'amount': amount})

#     def read_balance(self):
#         return random.choice(self.responses['balance']['responses']).format(self.user_data['balance'])

#     def read_transaction_history(self):
#         if not self.user_data['transaction_history']:
#             return "No transactions available in your history."
#         else:
#             transaction = random.choice(self.user_data['transaction_history'])
#             return random.choice(self.responses['transaction_history']['responses']).format(transaction['type'], transaction['amount'])

#     def update_balance(self, amount):
#         self.user_data['balance'] += amount
#         transaction_type = 'deposit' if amount > 0 else 'withdrawal'
#         self.user_data['transaction_history'].append({'type': transaction_type, 'amount': amount})

#     def delete_transaction_history(self):
#         self.user_data['transaction_history'] = []

#     def get_response(self, user_input):
#         user_input = user_input.lower()

#         for key, options in self.responses.items():
#             if any(keyword in user_input for keyword in options['keywords']):
#                 if key == 'create':
#                     # Simulate a deposit
#                     amount = int(input("Enter the deposit amount: "))
#                     self.create_transaction(amount, 'deposit')
#                     return f"Deposit of ${amount} successful. New balance: ${self.user_data['balance']}."
#                 elif key == 'update':
#                     # Simulate a withdrawal
#                     amount = int(input("Enter the withdrawal amount: "))
#                     self.update_balance(-amount)
#                     return f"Withdrawal of ${amount} successful. New balance: ${self.user_data['balance']}."
#                 elif key == 'delete':
#                     self.delete_transaction_history()
#                     return "Transaction history deleted."
#                 else:
#                     return random.choice(options['responses'])

#         return "I'm sorry, I didn't understand that. Please ask another question or type 'help' for assistance."

# def load_responses(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data['responses']

# def main():
#     responses = load_responses('responses.json')
#     chatbot = BankingChatbot(responses)
#     print("Welcome to the Banking Chatbot!")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'exit':
#             print("Goodbye!")
#             break

#         response = chatbot.get_response(user_input)
#         print("Chatbot:", response)

# if __name__ == "__main__":
#     main()
# {
#     "responses": {
#       "greeting": {
#         "keywords": ["hello", "hi", "hey"],
#         "responses": ["Hello! How can I help you today?", "Hi there! What can I assist you with?", "Welcome! What do you need help with?"]
#       },
#       "balance": {
#         "keywords": ["balance", "account balance", "how much money"],
#         "responses": ["Your current balance is ${}.", "You have ${} in your account.", "The balance in your account is ${}."]
#       },
#       "transaction_history": {
#         "keywords": ["transaction history", "recent transactions", "history"],
#         "responses": ["Your last transaction was on {} for ${}.", "You made a withdrawal of ${} on {}.", "The most recent transaction in your account was a deposit of ${} on {}."]
#       },
#       "help": {
#         "keywords": ["help", "assistance", "what can you do"],
#         "responses": ["You can ask about your balance, transaction history, or anything else you need assistance with.", "Feel free to inquire about your account balance or recent transactions.", "I'm here to help with any banking-related queries."]
#       },
#       "create": {
#         "keywords": ["create", "deposit"],
#         "responses": []
#       },
#       "update": {
#         "keywords": ["update", "withdrawal"],
#         "responses": []
#       },
#       "delete": {
#         "keywords": ["delete", "clear", "reset"],
#         "responses": []
#       }
#     }
#   }
  
  

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
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['responses']

def save_responses(file_path, responses):
    with open(file_path, 'w') as file:
        json.dump({'responses': responses}, file, indent=2)

def main():
    print("Welcome to the Banking Chatbot!")

    try:
        responses = load_responses('responses.json')
    except FileNotFoundError:
        print("No responses file found. Creating a new one.")
        responses = {}

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
