from flask import Flask, request, jsonify
import argparse
import os

app = Flask(__name__)

# ————— Stubbed out Llama code —————
# from gradientai import Gradient
# base_model = None
#
# token = 'LXkZBp5a1nGCP16xM7QieYKNz2Ns0tOW'
# workspace_id = 'b5f958d9-ffd4-41bb-a492-704114e02c8e_workspace'
# os.environ['GRADIENT_ACCESS_TOKEN'] = token
# os.environ['GRADIENT_WORKSPACE_ID'] = workspace_id
#
# def prepareLlamaBot():
#     global base_model
#     gradient = Gradient()
#     base_model = gradient.get_base_model(base_model_slug="llama3-8b-chat")
# ————————————————————————————

@app.route('/')
def index():
    return "Welcome to the Flask API!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)

    # Validate inputs
    if 'userMessage' not in data or not isinstance(data['userMessage'], str):
        return jsonify({'error': 'userMessage must be a string'}), 400
    if 'chatHistory' not in data or not isinstance(data['chatHistory'], list):
        return jsonify({'error': 'chatHistory must be a list'}), 400
    if not all(isinstance(item, dict) and 'User' in item and 'Llama' in item
               for item in data['chatHistory']):
        return jsonify({'error': 'chatHistory items must have User and Llama'}), 400

    # Echo stub
    user_message = data['userMessage']
    return jsonify({'message': f'Echo: {user_message}'}), 200

    # ————— Real Llama-2 call (disabled for now) —————
    # chat_history = data['chatHistory']
    # chat_history_str = '\n'.join(f"{item['User']} – {item['Llama']}" 
    #                              for item in chat_history)
    # QUERY = (
    #     "[INST]GIVEN THE CHAT HISTORY:\n"
    #     f"{chat_history_str}\n"
    #     "AND THE LATEST MESSAGE FROM USER:\n"
    #     f"{user_message}\n"
    #     "GIVE A RESPONSE TO THE USER\n[/INST]"
    # )
    # response = base_model.complete(query=QUERY,
    #                                max_generated_token_count=500
    #                               ).generated_output
    # return jsonify({'message': response}), 200
    # ——————————————————————————————

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port', type=int, default=5000,
        help='Port number to bind the Flask app'
    )
    args = parser.parse_args()

    port_num = args.port
    print("Starting stubbed Llama bot…")
    # prepareLlamaBot()    # disabled
    print(f"App running on 0.0.0.0:{port_num}")
    # Bind to all interfaces so emulator can reach via 10.0.2.2
    app.run(host="0.0.0.0", port=port_num)
