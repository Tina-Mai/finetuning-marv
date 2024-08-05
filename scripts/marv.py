import openai

# use the fine-tuned model


def use_finetuned_model(prompt, model_name):
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']


# example use
model_name = 'Marv'
prompt = "What's the weather like today?"
response = use_finetuned_model(prompt, model_name)
print(response)
