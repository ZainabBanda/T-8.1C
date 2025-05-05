from flask import Flask, request, jsonify
import argparse

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask API!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)
    if 'userMessage' not in data or not isinstance(data['userMessage'], str):
        return jsonify({'error': 'userMessage must be a string'}), 400
    if 'chatHistory' not in data or not isinstance(data['chatHistory'], list):
        return jsonify({'error': 'chatHistory must be a list'}), 400
    if not all(isinstance(item, dict) and 'User' in item and 'Llama' in item
               for item in data['chatHistory']):
        return jsonify({'error': 'chatHistory items must have User and Llama'}), 400

    # echo back immediately
    return jsonify({'message': f'Echo: {data["userMessage"]}'}), 200

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()

    print("Starting stubbed Llama bot…")
    # prepareLlamaBot()  # disabled
    print(f"App running on 0.0.0.0:{args.port}")
    app.run(host="0.0.0.0", port=args.port)
