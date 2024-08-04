from openai import OpenAI
import json
from config.config import openai_api_key

# openai.api_key = openai_api_key
client = OpenAI()

# upload training data
training_file_path = "../data/marv_dataset.jsonl"
file = client.files.create(
  file=open(training_file_path, "rb"),
  purpose="fine-tune"
)

# start fine-tuning job
finetune_response = client.fine_tuning.jobs.create(
  training_file=file.id,
  model="gpt-4o-mini"
)

# log the fine-tune job details
with open('../logs/fine_tune.log', 'w') as log_file:
    log_file.write(json.dumps(finetune_response, indent=4))

print("Fine-tuning started. Check logs for details.")