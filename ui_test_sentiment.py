import gradio as gr
import requests

# URL of the external API from ngrok and endpoint /predict
url = "http://e8f2-34-23-28-188.ngrok-free.app/predict"

# Function to interact with the external API
def get_sentiment(text):
    data = {"text": text}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)
    return response.json().get('sentiment', 'Error')

# Create a Gradio interface
iface = gr.Interface(
    fn=get_sentiment,
    inputs="text",
    outputs="text",
    title="Sentiment Analysis",
    description="Enter text to get sentiment from an external API."
)

# Launch the Gradio app
iface.launch(share=True)
