class InternalChatBot:
    def __init__(self):
        self.intents = {}
        self.datasets = self.load_intents_from_file()

    def load_intents_from_file(self):
        try:
            with open('responses.txt', 'r') as file:
                datasets = eval(file.read())
                return datasets
        except FileNotFoundError:
            return {}

    def save_datasets_to_file(self):
        with open('responses.txt', 'w') as file:
            file.write(str(self.datasets))

    def create_dataset(self, keyword):
        self.datasets[keyword.lower()] = {'intents': {}}
        print(f"Dataset with keyword '{keyword}' created")

    def create_intent(self, keyword, intent, responses):
        if keyword.lower() in self.datasets:
            if intent.lower() in self.datasets[keyword.lower()]['intents']:
                print(f"Intent '{intent}' already exists in dataset '{keyword}'. Response: {self.datasets[keyword.lower()]['intents'][intent.lower()]}")
            else:
                self.datasets[keyword.lower()]['intents'][intent.lower()] = responses
                print(f"Intent '{intent}' added to dataset '{keyword}' with responses '{responses}'")
                self.save_datasets_to_file()
        else:
            print(f"Dataset '{keyword}' does not exist. Use create_dataset to add.")

    def update_intent(self, keyword, intent, responses):
        if keyword.lower() in self.datasets and intent.lower() in self.datasets[keyword.lower()]['intents']:
            self.datasets[keyword.lower()]['intents'][intent.lower()] = responses
            print(f"Intent '{intent}' in dataset '{keyword}' updated to '{responses}'")
            self.save_datasets_to_file()
        else:
            print(f"Dataset '{keyword}' or intent '{intent}' does not exist.")

    def read_intent(self, keyword, intent):
        if keyword.lower() in self.datasets and intent.lower() in self.datasets[keyword.lower()]['intents']:
            return self.datasets[keyword.lower()]['intents'][intent.lower()]
        else:
            return f"No response found for intent '{intent}' in dataset '{keyword}'"

    def delete_intent(self, keyword, intent):
        if keyword.lower() in self.datasets and intent.lower() in self.datasets[keyword.lower()]['intents']:
            del self.datasets[keyword.lower()]['intents'][intent.lower()]
            print(f"Intent '{intent}' in dataset '{keyword}' deleted")
            self.save_datasets_to_file()
        else:
            print(f"No intent found for '{intent}' in dataset '{keyword}'")

    def train_chatbot(self, keyword):
        loaded_datasets = self.load_intents_from_file()

        if keyword.lower() in loaded_datasets:
            self.datasets = loaded_datasets
            print(f"Chatbot trained successfully with dataset keyword '{keyword}'.")
            self.save_datasets_to_file()
        else:
            print(f"Unknown dataset keyword: {keyword}")

    def test_chatbot_intent(self, keyword, test_sentence):
        matched_intents = []
        matched_responses = []

        if keyword.lower() in self.datasets:
            sentence_lower = test_sentence.lower()

            for intent, responses in self.datasets[keyword.lower()]['intents'].items():
                intent_keywords = intent.lower().split()
                if any(keyword in sentence_lower for keyword in intent_keywords):
                    matched_intents.append((intent, responses))

            if not matched_intents:
                for responses in self.datasets[keyword.lower()]['intents'].values():
                    for response in responses:
                        response_keywords = response.lower().split()
                        if any(keyword in sentence_lower for keyword in response_keywords):
                            matched_responses.append(('(Response Match)', response))

            if matched_intents:
                for intent, responses in matched_intents:
                    print(f"Intent: '{intent}', Responses: {responses}")
            elif matched_responses:
                for _, response in matched_responses:
                    print(f"Intent: '(Response Match)', Responses: {response}")
            else:
                print(f"No matching intents or responses found in the test sentence for dataset '{keyword}'.")
        else:
            print(f"Dataset '{keyword}' does not exist.")

    def get_datasets(self):
        return self.datasets

def display_menu():
    print("\nMenu:")
    print("1. Create Dataset")
    print("2. Create Intent in Dataset")
    print("3. Read Intent in Dataset")
    print("4. Update Intent in Dataset")
    print("5. Delete Intent in Dataset")
    print("6. Train Chatbot with Dataset")
    print("7. Test Chatbot Intent in Dataset")
    print("8. Get Datasets")
    print("9. Exit")

chatbot_builder = InternalChatBot()

while True:
    display_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        keyword = input("Enter the dataset keyword: ")
        chatbot_builder.create_dataset(keyword)
    elif choice == '2':
        keyword = input("Enter the dataset keyword: ")
        intent = input("Enter the intent: ")
        responses = input("Enter responses (comma-separated): ").split(',')
        chatbot_builder.create_intent(keyword, intent, responses)
    elif choice == '3':
        keyword = input("Enter the dataset keyword: ")
        intent = input("Enter the intent to read: ")
        response = chatbot_builder.read_intent(keyword, intent)
        print(f"Intent '{intent}' response in dataset '{keyword}': {response}")
    elif choice == '4':
        keyword = input("Enter the dataset keyword: ")
        intent = input("Enter the intent to update: ")
        responses = input("Enter new responses (comma-separated): ").split(',')
        chatbot_builder.update_intent(keyword, intent, responses)
    elif choice == '5':
        keyword = input("Enter the dataset keyword: ")
        intent = input("Enter the intent to delete: ")
        chatbot_builder.delete_intent(keyword, intent)
    elif choice == '6':
        keyword = input("Enter the dataset keyword to train the chatbot: ")
        chatbot_builder.train_chatbot(keyword)
    elif choice == '7':
        keyword = input("Enter the dataset keyword: ")
        test_sentence = input("Enter a test intent: ")
        chatbot_builder.test_chatbot_intent(keyword, test_sentence)
    elif choice == '8':
        datasets = chatbot_builder.get_datasets()
        print("\nStored Datasets:")
        for key, dataset in datasets.items():
            print(f"Dataset Keyword: {key}")
            for intent, responses in dataset['intents'].items():
                print(f"  Intent: {intent}, Responses: {responses}")
    elif choice == '9':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
