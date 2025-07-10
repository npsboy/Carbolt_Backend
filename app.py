from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS
import requests
import time
from google import genai


load_dotenv() #loads the environment variables from .env file
app = Flask(__name__) #_name_ tells flask that it is the main module
CORS(app) # Enable CORS for all routes

client = genai.Client(api_key="AIzaSyBFuSbE_SW9hqrbAaKiUyGAXjPA5sm2H_s")


@app.route("/")
def home():
    return "Carbolt Backend is running!"

@app.route("/chat", methods=["POST"])
def chat():
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    )
    return jsonify({"response": response.candidates[0].content})

if __name__ == "__main__":
    app.run(debug=True)