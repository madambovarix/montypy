from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForLanguageModeling
from datasets import Dataset
import torch
from process_data import load_and_process_data

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, max_length=128)

if __name__ == "__main__":
    # Load and process the dataset
    json_file_path = "../monty_python_scraper/processed_montypython.json"
    dataset = load_and_process_data(json_file_path)
    
    # Load the tokenizer and model
    model_name = "distilgpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    # Set the pad token
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id
    
    # Tokenize the dataset
    tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=dataset.column_names)
    
    # Create data collator
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    
    # Set up training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        save_steps=1000,
        save_total_limit=2,
        logging_steps=100,
        logging_dir="./logs",
        learning_rate=5e-5,
    )
    
    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
    )
    
    # Start training
    trainer.train()
    
    # Save the fine-tuned model
    trainer.save_model("./montypy_model")
    tokenizer.save_pretrained("./montypy_model")
    
    print("Model training completed and saved.")
