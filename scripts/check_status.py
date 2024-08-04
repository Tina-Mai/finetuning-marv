import openai
import json
from config.config import openai_api_key

openai.api_key = openai_api_key

# function to check the fine-tuning status
def check_finetune_status(job_id):
    response = openai.FineTune.retrieve(id=job_id)
    return response

# read the job ID from the log
with open('../logs/fine_tune.log', 'r') as log_file:
    fine_tune_response = json.load(log_file)
    job_id = fine_tune_response['id']

# check status
status = check_finetune_status(job_id)
print(json.dumps(status, indent=4))