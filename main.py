import openai
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify

load_dotenv() #teste123

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_folder=".", static_url_path="")

def ask_openai(prompt, model, temperature=0.5, max_tokens=2048, top_p=1, frequency_penalty=0, presence_penalty=0):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    message = completions.choices[0].text
    return message.strip()

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message")
    response