import gradio as gr
import requests

# URL of the local API
url = "http://localhost:5000/predict"

# Function to interact with the local API
def get_sentiment(text):
    try:
        data = {"text": text}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        result = response.json()
        return result.get('sentiment', 'Error')
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Create a Gradio interface
iface = gr.Interface(
    fn=get_sentiment,
    inputs="text",
    outputs="text",
    title="Sentiment Analysis",
    description="Enter text to get sentiment from a local API."
)

# Launch the Gradio app
iface.launch()

