from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Store conversations with chat_id as keys
chats = {}

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
    # Validate if chat_id exists
    if chat_id not in chats:
        return jsonify({"error": "Chat ID not found"}), 404

    # Get the user's message from the request
    data = request.get_json()
    user_prompt = data.get('prompt', '')

    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Add user's message to the chat conversation
    chats[chat_id].append({"role": "user", "content": user_prompt})

    # Placeholder bot response
    bot_response = f"Echo: {user_prompt}"
    chats[chat_id].append({"role": "assistant", "content": bot_response})

    # Return the updated conversation
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
    del chats[chat_id]
    return jsonify({"message": f"Chat {chat_id} has been reset."})

if __name__ == "__main__":
    app.run(debug=True)
