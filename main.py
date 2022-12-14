import json
import re
import random_responses
import random
from translate import Translator

def add_var():
    print("In progress")

def main():
    # Load JSON data
    def load_json(file):
        with open(file) as responses:
            print(f"Loaded '{file}' successfully!")
            return json.load(responses)


    # Store JSON data
    response_data = load_json("responses.json")


    def get_response(input_string):
        split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
        score_list = []

        # Check all the responses
        for response in response_data:
            response_score = 0
            required_score = 0
            required_words = response["required_words"]

            # Check if there are any required words
            if required_words:
                for word in split_message:
                    if word in required_words:
                        required_score += 1

            # Amount of required words should match the required score
            if required_score == len(required_words):
                # print(required_score == len(required_words))
                # Check each word the user has typed
                for word in split_message:
                    # If the word is in the response, add to the score
                    if word in response["user_input"]:
                        response_score += 1

            # Add score to list
            score_list.append(response_score)
            # Debugging: Find the best phrase

        # Find the best response and return it if they're not all 0
        best_response = max(score_list)
        response_index = score_list.index(best_response)

        # Check if input is empty
        if input_string == "":
            return "Please type something so we can chat :("

    # If there is no good response, return a random one.
        if best_response != 0:
            return random.choice(list(response_data[response_index]["bot_response"]))

        return random_responses.random_string()

    commands = "-addvar(in progress): Used for if you want the bot to react a certain way to your message \n -repeat: Used for if you want the bot to complete your sentence \n -translate(in progress): Used for if you want to translate text into spanish \n Type '-help' if you forget"



    while True:
        user_input = input("You: ")
        gr = get_response(user_input)
        translator= Translator(to_lang="Spanish")
        translation = translator.translate(user_input)
        if '-repeat' in user_input:
            print ("Bot:", user_input.replace('-repeat', ''))
        elif '-translate' in user_input:
            print("Bot:", translation.replace('-translate', ''))
        elif '-addvar' in user_input:
            add_var()
        elif '-help' in user_input:
            print("Bot:", commands)
        else:
            print("Bot:", gr)

if __name__ == '__main__':
    main()