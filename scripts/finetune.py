from openai import OpenAI
import json

client = OpenAI()


def finetune_model():
    try:
        # upload training data
        training_file_path = "./data/marv_dataset.jsonl"
        file = client.files.create(
            file=open(training_file_path, "rb"),
            purpose="fine-tune"
        )
        print("File uploaded:", file.id)

        # start finetuning job
        response = client.fine_tuning.jobs.create(
            training_file=file.id,
            model="gpt-3.5-turbo",
        )
        print("Finetuning job created:", response.id)

        # convert response to readable format
        response_dict = {
            "id": response.id,
            "status": response.status,
            "created_at": response.created_at,
            "model": response.model,
            # add other attributes as needed
        }
        response_json = json.dumps(response_dict, indent=4)

        # log the finetune job details
        with open("./logs/finetune.log", "w") as log_file:
            log_file.write(response_json)

        print("Response:", response_json)
        print("Finetuning started. Run check logs or run `scripts/check_status.py` for details.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    finetune_model()
