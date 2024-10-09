# MontyPy: A Dumb Chatbot Fine-tuned on Monty Python Dialogues

This project creates a simple chatbot by fine-tuning a small language model (DistilGPT2) on dialogues from Monty Python's Flying Circus.

## Project Structure

```
montypy/
├── montypy/
│   ├── __init__.py
│   ├── preprocess_json.py
│   ├── process_data.py
│   ├── train_model.py
│   └── chatbot.py
├── tests/
│   └── __init__.py
├── pyproject.toml
└── README.md
```

## Installation

1. Make sure you have Anaconda or Miniconda installed.
2. Create and activate the Conda environment:
   ```
   conda create -n montypy python=3.10
   conda activate montypy
   ```
3. Clone this repository and navigate to the `montypy` directory.
4. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Make sure to activate the Conda environment before running any scripts:

```
conda activate montypy
```

Then, follow these steps:

1. Preprocess the JSON file:
   ```
   python montypy/preprocess_json.py
   ```
   This script will read the original JSON file containing Monty Python dialogues and create a preprocessed version with a simpler structure.

2. Process the preprocessed data:
   ```
   python montypy/process_data.py
   ```
   This script will read the preprocessed JSON file and convert it into a format suitable for training.

3. Train the model:
   ```
   python montypy/train_model.py
   ```
   This will fine-tune the DistilGPT2 model on the processed Monty Python dialogues and create a `montypy_model` directory with the fine-tuned model.

4. Run the chatbot:
   ```
   python montypy/chatbot.py
   ```
   This will start an interactive session where you can chat with the Monty Python-inspired chatbot.

## Troubleshooting

If you encounter any issues with processing the data or training the model, please ensure that:

1. The original `montypython.json` file is located in the correct directory (`../monty_python_scraper/montypython.json` relative to the `preprocess_json.py` script).
2. You have activated the Conda environment (`conda activate montypy`) before running any scripts.
3. You have run the preprocessing step before attempting to process the data or train the model.
4. The preprocessed JSON file (`processed_montypython.json`) is created successfully in the `../monty_python_scraper/` directory.

If you continue to experience problems, please check the error messages for more information and ensure all dependencies are correctly installed.

## Note

This chatbot is intended for educational purposes and fun. The responses generated may not always make sense or be coherent, as it's based on the often absurd and surreal dialogues from Monty Python's Flying Circus.

Enjoy your conversations with this dumb Monty Python-inspired chatbot!
