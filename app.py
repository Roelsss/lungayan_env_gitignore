from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Load greeting message from environment variable
Message = os.getenv("Message", "Hello, Roels")


@app.route('/Message')
def home():
    return jsonify({"message": Message})

if __name__ == '__main__':
    app.run(debug=True)
