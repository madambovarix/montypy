import json

def preprocess_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    processed_dialogues = []

    for episode in data:
        if 'script' in episode:
            for scene in episode['script']:
                if 'dialogue' in scene:
                    current_dialogue = []
                    for entry in scene['dialogue']:
                        if entry['speaker'] and entry['text']:
                            current_dialogue.append({
                                'speaker': entry['speaker'],
                                'text': entry['text']
                            })
                    if current_dialogue:
                        processed_dialogues.append(current_dialogue)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_dialogues, f, ensure_ascii=False, indent=2)

    print(f"Preprocessed {len(processed_dialogues)} dialogues and saved to {output_file}")

if __name__ == "__main__":
    input_file = "../monty_python_scraper/montypython.json"
    output_file = "../monty_python_scraper/processed_montypython.json"
    preprocess_json(input_file, output_file)
