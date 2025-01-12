from flask import Flask, request, jsonify
import os

from flask_cors import CORS
import re

from ChatbotModel.ChatWithBot import chat_with_bot
#from ChatbotModel.TrainBot import fine_tune_mode
#from ChatbotModel.UploadData import upload_data_cohere



app = Flask(__name__)

CORS(app)

# Store conversations with chat_id as keys
chats = {"12345" : []}

# A dummy getID function that generates a chat_id from the filename
def getID(filename: str) -> str:
    # Generate a simple chat_id (you can replace this with a more complex ID generation logic)
    chat_id = filename.split('.')[0]  # Use the filename (without extension) as the chat_id
    return chat_id

# Route to start a new chat with a text file
@app.route('/new_chat', methods=['POST'])
def new_chat():
    # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    # Retrieve the file from the request
    file = request.files['file']

    # Ensure the file is a valid text file by checking the extension
    if not file.filename.endswith('.txt'):
        return jsonify({"error": "Invalid file type. Only .txt files are allowed."}), 400

    # Get the chat ID using the filename
    chat_id = getID(file.filename)

    # Initialize the conversation for the new chat
    chats[chat_id] = []

    return jsonify({"chat_id": chat_id, "message": "New chat created."})

# Route to handle messages in a chat
@app.route('/chat/<chat_id>', methods=['POST'])
def chat(chat_id):
    print(f"Received Chat ID: {chat_id}")  # Log the received chat ID

    if chat_id not in chats:
        print(f"Chat ID {chat_id} not found in chats.")  # Log missing chat ID
        return jsonify({"error": "Chat ID not found"}), 404

    data = request.get_json()
    print(f"Request data: {data}")  # Log the incoming request payload

    user_prompt = data.get('prompt', '').strip()
    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Append user's message
    chats[chat_id].append({"role": "user", "content": user_prompt})

    # Generate a placeholder response
    bot_response = chat_with_bot(user_prompt, 'f97b173f-5615-42df-beff-f8f15f31fd27-ft', chats[chat_id])
    bot_response = re.sub(r'\b(user|assistant):', '', bot_response, flags=re.IGNORECASE).strip()
    chats[chat_id].append({"role": "assistant", "content": bot_response})

    print(f"Updated chat: {chats[chat_id]}")  # Log the updated chat conversation
    return jsonify({"conversation": chats[chat_id]})


# Route to fetch a conversation
@app.route('/conversation/<chat_id>', methods=['GET'])
def get_conversation(chat_id):
    # Validate if chat_id exists
    if chat_id not in chats:
        return jsonify({"error": "Chat ID not found"}), 404

    return jsonify({"conversation": chats[chat_id]})

# Route to reset or delete a chat
@app.route('/reset_chat/<chat_id>', methods=['DELETE'])
def reset_chat(chat_id):
    # Validate if chat_id exists
    if chat_id not in chats:
        return jsonify({"error": "Chat ID not found"}), 404

    # Remove the chat
    chats[chat_id].clear()
    return jsonify({"message": f"Chat {chat_id} has been reset."})

if __name__ == "__main__":
    app.run(debug=True)
