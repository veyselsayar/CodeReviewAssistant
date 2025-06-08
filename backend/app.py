from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ollama_client import analyze_code
import os

app = Flask(__name__, static_folder='../frontend')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    code = data.get('code')
    if not code:
        return jsonify({'error': 'Kod gönderilmedi'}), 400

    try:
        result = analyze_code(code)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
