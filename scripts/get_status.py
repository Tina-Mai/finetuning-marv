import openai
import json

# function to check the finetuning status.


def get_finetune_status(job_id):
    response = openai.fine_tuning.jobs.retrieve(job_id)
    return response


# read the job ID from the log
with open('./logs/finetune.log', 'r') as log_file:
    finetune_response = json.load(log_file)
    job_id = finetune_response['id']

# check status and print the details
status = get_finetune_status(job_id).to_dict()
print("id:", status['id'])
print("status:", status['status'])
print("base model:", status['model'])
print("finetuned model:", status['fine_tuned_model'])
