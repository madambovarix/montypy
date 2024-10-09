from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_model_and_tokenizer(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    return model, tokenizer

def generate_response(model, tokenizer, input_text, max_length=255):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.5
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
        
        response = generate_response(model, tokenizer, user_input)
        print(f"Chatbot: {response}")
    
    print("Thank you for chatting with the Monty Python Chatbot!")

if __name__ == "__main__":
    main()
