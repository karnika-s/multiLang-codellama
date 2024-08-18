# CodeLlama by Meta (Open Source)
# Build your own assistant with Olama and Gradio frontend

import requests
import json
import gradio as gr  # Gradio for frontend

# URL to interact with Olama server
url = "http://localhost:11434/api/generate"

# HTTP headers for API request
headers = {
    'Content-Type': 'application/json'
}

# Store user prompt history
history = []

# Function to generate responses from Olama
def generate_response(prompt):
    # Append new prompt to history with separation
    history.append(prompt)
    final_prompt = "\n------------------------------------------------------\n".join(history)

    # Prepare data for the request
    data = {
        "model": "MyCoder",  # Specify your model
        "prompt": final_prompt,
        "stream": False  # Disable streaming
    }

    # Make POST request to Olama API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if request was successful
    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data.get('response', 'No response received')
        return actual_response
    else:
        print("Error:", response.text)
        return "An error occurred while generating the response."

# Define Gradio interface
interface = gr.Interface(
    fn=generate_response,  # Function to call when user submits prompt
    inputs=gr.Textbox(lines=5, placeholder="Enter your prompt here...", label="Your Prompt"),  # Input textbox
    outputs=gr.Textbox(label="MyCoder's Response", lines=10),  # Output response
    title="🤖😎 MyCoder Assistant",  # Title of the interface
    description="This AI-powered assistant helps answer your code-related questions.",  # Short description
    theme="compact",  # Use a compact theme for cleaner UI
)

# Launch the Gradio interface
interface.launch()
