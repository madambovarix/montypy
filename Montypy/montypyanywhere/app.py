from flask import Flask, request, render_template, jsonify, session
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète_ici'  # Nécessaire pour utiliser les sessions

# Chargement du modèle et du tokenizer
def load_model_and_tokenizer(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = model.config.eos_token_id
    
    return model, tokenizer

model_path = "./montypy_model"
model, tokenizer = load_model_and_tokenizer(model_path)

# Prompt système par défaut
DEFAULT_SYSTEM_PROMPT = "You are  achatbot impersonating T.J.Dump, respectable conservative of the United States Of America. Speak as a true Republican."

def generate_response(input_text, system_prompt, max_new_tokens=155):
    # Combine system prompt and user input
    full_input = f"{system_prompt}\n\nUser: {input_text}\nAssistant:"
    
    input_ids = tokenizer.encode(full_input, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    
    generation_config = GenerationConfig(
        max_new_tokens=max_new_tokens,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.7,  # Légèrement augmenté pour plus de créativité
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id
    )
    
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        generation_config=generation_config
    )
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response[len(full_input):].strip()

@app.route('/')
def home():
    if 'system_prompt' not in session:
        session['system_prompt'] = DEFAULT_SYSTEM_PROMPT
    return render_template('index.html', system_prompt=session['system_prompt'])

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    system_prompt = session.get('system_prompt', DEFAULT_SYSTEM_PROMPT)
    
    try:
        response = generate_response(user_message, system_prompt)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/update_prompt', methods=['POST'])
def update_prompt():
    data = request.json
    new_prompt = data.get('system_prompt', DEFAULT_SYSTEM_PROMPT)
    session['system_prompt'] = new_prompt
    return jsonify({'status': 'success', 'prompt': new_prompt})

if __name__ == '__main__':
    app.run(debug=True)