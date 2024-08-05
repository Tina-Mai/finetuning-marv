from openai import OpenAI
import json

client = OpenAI()


def finetune_model(training_file_path, model, suffix):
    try:
        # upload training data
        file = client.files.create(
            file=open(training_file_path, "rb"),
            purpose="fine-tune"
        )
        print("File uploaded:", file.id)

        # start finetuning job
        response = client.fine_tuning.jobs.create(
            training_file=file.id,
            model=model,
            suffix=suffix,
        )
        print("Finetuning job created:", response.id)

        # log the finetune job details
        with open("./logs/finetune.log", "w") as log_file:
            log_file.write(response.to_json())

        print("Response:", response.to_json())
        print("Fine-tuning started. Run `python scripts/get_status.py` for details.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    finetune_model(training_file_path="./data/marv_dataset.jsonl",
                   model="gpt-3.5-turbo", suffix="marv")
