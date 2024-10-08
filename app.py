from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return jsonify(response.choices[0].text.strip())

import requests

@app.route('/proxy', methods=['POST'])
def proxy():
    prompt = request.json.get('prompt')
    response = requests.get(f"https://openai-worker.tonton-tremblay.workers.dev/?prompt={prompt}")
    return jsonify(response.text)
    app.run(debug=True)
