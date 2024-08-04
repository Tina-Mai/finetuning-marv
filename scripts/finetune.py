from openai import OpenAI
import json
from check_status import check_finetune_status

client = OpenAI()

def finetune_model():
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
    with open('../logs/finetune.log', 'w') as log_file:
        log_file.write(json.dumps(finetune_response, indent=4))

    print("Fine-tuning started. Check logs for details.")

if __name__ == "__main__":
  finetune_model()