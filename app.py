from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import json
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
socketio = SocketIO(app)

# Load the Spacy model for NLP
nlp = spacy.load('en_core_web_sm')

# Load the fine-tuned GPT-2 model
model_path = 'models/fine_tuned_gpt/checkpoint-15'
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

with open('data/corpus.json', 'r') as f:
    corpus = json.load(f)

# Preprocess corpus questions
def preprocess(text):
    doc = nlp(text.lower())
    return ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

corpus_questions = [preprocess(q) for intent in corpus['intents'] for q in intent['questions']]

# Fit TF-IDF vectorizer on the corpus questions
vectorizer = TfidfVectorizer().fit(corpus_questions)
corpus_vectors = vectorizer.transform(corpus_questions)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    response = get_response(message)
    emit('response', {'data': response})

def get_response(message):
    preprocessed_message = preprocess(message)
    message_vector = vectorizer.transform([preprocessed_message])
    
    # Compute cosine similarity between user message and corpus questions
    similarities = cosine_similarity(message_vector, corpus_vectors).flatten()
    
    # Find the most similar question
    best_match_index = similarities.argmax()
    best_match_score = similarities[best_match_index]

    if best_match_score > 0.5:  # Threshold for matching
        for intent in corpus['intents']:
            if preprocessed_message in [preprocess(q) for q in intent['questions']]:
                return intent['answers'][0]

    # Generate response using GPT-2 for unmatched questions
    input_ids = tokenizer.encode(message, return_tensors='pt')
    output = model.generate(input_ids, max_length=50, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Check if the generated response is appropriate or should be a fallback
    if "contact customer support" in response.lower():
        return response
    else:
        return "Sorry, I don't have information on that topic. Please contact customer support for assistance."

if __name__ == '__main__':
    socketio.run(app, debug=True)
