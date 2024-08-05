import openai
import json

# function to check the fine-tuning status


def check_finetune_status(job_id):
    response = openai.fine_tuning.jobs.retrieve(job_id)
    # convert to JSON-serializable dictionary
    response_dict = {
        "id": response.id,
        "status": response.status,
        "created_at": response.created_at,
        "model": response.model,
        # add other attributes as needed
    }
    return response_dict


# read the job ID from the log
with open('./logs/finetune.log', 'r') as log_file:
    finetune_response = json.load(log_file)
    job_id = finetune_response['id']

# check status
status = check_finetune_status(job_id)
print(json.dumps(status, indent=4))
