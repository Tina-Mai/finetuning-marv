from openai import OpenAI
import json
from get_status import get_finetune_status

client = OpenAI()

# get job ID from log
with open('./logs/finetune.log', 'r') as log_file:
    finetune_response = json.load(log_file)
    job_id = finetune_response['id']
# get finetuned model ID from get_status.py
finetuned_model = get_finetune_status(job_id).to_dict()['fine_tuned_model']

# run this after finetuning has succeeded to use the model
# you can converse with it in your terminal like a chatbot


def use_finetuned_model(prompt):
    completion = client.chat.completions.create(
        model=finetuned_model,
        messages=[
            {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
            {"role": "user", "content": prompt}
        ]
    )
    # extract and return the assistant's response
    return completion.choices[0].message.content


def main():
    print("————————————————")
    print("Chatbot started. Type 'EXIT' to quit.")
    while True:
        # take user input
        user_input = input("You: ")

        # exit the chat if the user types 'exit'
        if user_input.strip().lower() == 'exit':
            print("————————————————")
            print("Chatbot terminated.")
            break

        # get the response from the model
        response = use_finetuned_model(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    main()
