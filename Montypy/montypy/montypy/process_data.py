import json
from datasets import Dataset

def load_and_process_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processed_data = []
    
    for dialogue in data:
        dialogue_text = ""
        for entry in dialogue:
            dialogue_text += f"{entry['speaker']}: {entry['text']}\n"
        processed_data.append({"text": dialogue_text.strip()})
    
    return Dataset.from_list(processed_data)

if __name__ == "__main__":
    json_file_path = "../monty_python_scraper/processed_montypython.json"
    dataset = load_and_process_data(json_file_path)
    print(f"Processed {len(dataset)} dialogue entries")
    print("Sample entry:", dataset[0] if len(dataset) > 0 else "No entries found")
