from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import os
import sys

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "✅ Flask backend is running!"

@app.route("/start-keyboard", methods=["GET"])
def start_keyboard():
    try:
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keyboard.py")
        subprocess.Popen([sys.executable, script_path])
        return jsonify({"status": "success", "message": "keyboard.py started"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
