# finetuning-marv

finetuning a model using OpenAI's API to make Marv, a sarcastic little guy

## Setup

1. Install Python and pip.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## To use

Finetune the model
```bash
python scripts/finetune.py
```

Check the status as it finetunes
```bash
python scripts/get_status.py
```

Talk to Marv
```bash
python scripts/use_model.py
```
