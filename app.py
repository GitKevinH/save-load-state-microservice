import json
from pathlib import Path
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save_data(request):
    """Saves JSON data to '<username>_<application_name>.txt'."""
    payload = request.get_json(silent=True) or {}

    username = payload.get("username")
    application_name = payload.get("application_name")
    data = payload.get("data")

    if not username or not application_name or data is None:
        return jsonify({
            "error": "Request must include 'username', 'application_name', and 'data'."
        }), 400

    filepath = Path(f"{username}_{application_name}.txt")
    filepath.write_text(json.dumps(data, indent=2), encoding="utf-8")

    return jsonify({
        "status": "saved",
        "filename": filepath.name
    }), 201