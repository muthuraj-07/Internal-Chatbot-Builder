import random

class BankingChatbot:
    def __init__(self):
        self.user_data = {
            'balance': 1000,
            'transaction_history': [],
        }
        self.responses = {
            'greeting': ['Hello! How can I help you today?', 'Hi there! What can I assist you with?', 'Welcome! What do you need help with?'],
            'balance': ['Your current balance is ${}.', 'You have ${} in your account.', 'The balance in your account is ${}.'],
            'transaction_history': ['Your last transaction was on {} for ${}.', 'You made a withdrawal of ${} on {}.', 'The most recent transaction in your account was a deposit of ${} on {}.'],
            'help': ['You can ask about your balance, transaction history, or anything else you need assistance with.', 'Feel free to inquire about your account balance or recent transactions.', 'I\'m here to help with any banking-related queries.'],
        }

    def create_transaction(self, amount, transaction_type):
        self.user_data['balance'] += amount
        self.user_data['transaction_history'].append({'type': transaction_type, 'amount': amount})

    def read_balance(self):
        return random.choice(self.responses['balance']).format(self.user_data['balance'])

    def read_transaction_history(self):
        if not self.user_data['transaction_history']:
            return "No transactions available in your history."
        else:
            transaction = random.choice(self.user_data['transaction_history'])
            return random.choice(self.responses['transaction_history']).format(transaction['type'], transaction['amount'])

    def update_balance(self, amount):
        self.user_data['balance'] += amount
        transaction_type = 'deposit' if amount > 0 else 'withdrawal'
        self.user_data['transaction_history'].append({'type': transaction_type, 'amount': amount})

    def delete_transaction_history(self):
        self.user_data['transaction_history'] = []

    def get_response(self, user_input):
        user_input = user_input.lower()

        if 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
            return random.choice(self.responses['greeting'])
        elif 'balance' in user_input:
            return self.read_balance()
        elif 'transaction history' in user_input:
            return self.read_transaction_history()
        elif 'create' in user_input:
            # Simulate a deposit
            amount = int(input("Enter the deposit amount: "))
            self.create_transaction(amount, 'deposit')
            return f"Deposit of ${amount} successful. New balance: ${self.user_data['balance']}."
        elif 'update' in user_input:
            # Simulate a withdrawal
            amount = int(input("Enter the withdrawal amount: "))
            self.update_balance(-amount)
            return f"Withdrawal of ${amount} successful. New balance: ${self.user_data['balance']}."
        elif 'delete' in user_input:
            self.delete_transaction_history()
            return "Transaction history deleted."
        elif 'help' in user_input:
            return random.choice(self.responses['help'])
        else:
            return "I'm sorry, I didn't understand that. Please ask another question or type 'help' for assistance."

def main():
    chatbot = BankingChatbot()
    print("Welcome to the Banking Chatbot!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
