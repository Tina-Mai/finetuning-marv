import openai
import json

# function to check the fine-tuning status
def check_finetune_status(job_id):
    response = openai.FineTune.retrieve(id=job_id)
    return response

# read the job ID from the log
with open('../logs/finetune.log', 'r') as log_file:
    finetune_response = json.load(log_file)
    job_id = finetune_response['id']

# check status
status = check_finetune_status(job_id)
print(json.dumps(status, indent=4))