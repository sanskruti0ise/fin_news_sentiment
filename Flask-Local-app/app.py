import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Specify the directory where your model is saved
model_directory = './models/tiny-bert'

# Load the fine-tuned model and tokenizer
model_name = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_directory)

# Define a function to preprocess and predict the sentiment
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()
    sentiment = ['negative', 'neutral', 'positive'][prediction]
    return sentiment

# Define the root endpoint
@app.route('/')
def home():
    return "Welcome to the Sentiment Analysis API. Use the /predict endpoint to get predictions."

# Define the predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        app.logger.debug("Received data: %s", data)
        if not data or 'text' not in data:
            return jsonify({'error': 'No text field provided'}), 400
        text = data['text']
        sentiment = predict_sentiment(text)
        return jsonify({'sentiment': sentiment})
    except Exception as e:
        app.logger.error("Error occurred: %s", str(e))
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

