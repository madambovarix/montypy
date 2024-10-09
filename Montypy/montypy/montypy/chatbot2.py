from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch

def load_model_and_tokenizer(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    
    # Configurer les tokens spéciaux si nécessaire
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = model.config.eos_token_id
    
    return model, tokenizer

def generate_response(model, tokenizer, input_text, max_new_tokens=50):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    
    # Créer une configuration de génération
    generation_config = GenerationConfig(
        max_new_tokens=max_new_tokens,  # Utiliser max_new_tokens au lieu de max_length
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.5,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id
    )
    
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        generation_config=generation_config
    )
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response[len(input_text):].strip()

def main():
    model_path = "./montypy_model"
    model, tokenizer = load_model_and_tokenizer(model_path)
    
    print("Welcome to the Monty Python Chatbot!")
    print("Type 'quit' to exit the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        try:
            response = generate_response(model, tokenizer, user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Une erreur s'est produite : {str(e)}")
    
    print("Thank you for chatting with the Monty Python Chatbot!")

if __name__ == "__main__":
    main()