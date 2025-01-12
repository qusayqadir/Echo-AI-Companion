from flask import Flask, request, jsonify
import os
from flask_cors import CORS

from ChatbotModel.ChatWithBot import chat_with_bot
#from ChatbotModel.TrainBot import fine_tune_mode
#from ChatbotModel.UploadData import upload_data_cohere

import csv
import re

app = Flask(__name__)

CORS(app)

# "f97b173f-5615-42df-beff-f8f15f31fd27-ft"

# Store conversations with chat_id as keys
chats = {}

chats["12345"] = {"modelID" : "f97b173f-5615-42df-beff-f8f15f31fd27-ft", "messages" : []}

metaDataPath = "data/metadata_cohere.csv"

# A dummy getID function that generates a chat_id from the filename

def getID(filepath: str):
    # Generate a simple chat_id (you can replace this with a more complex ID generation logic)
    chat_id = filepath.split('.')[0]  # Use the filename (without extension) as the chat_id
    
    # Open and read the CSV file
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        lowest_value = float('inf')  # Set initial value to positive infinity
        lowest_row = None
        
        # Iterate through rows and find the row with the lowest value (assuming numeric values in a specific column)
        for row in csv_reader:
            try:
                # Assuming you want to find the lowest value in the 1st column (index 0)
                value = float(row[0])  # Change the index as needed
                if value < lowest_value:
                    lowest_value = value
                    lowest_row = row
            except ValueError:
                # Skip rows where the value can't be converted to a float
                continue
        
        # Return the 5th value in the lowest row (index 4)
        if lowest_row is not None and len(lowest_row) >= 5:
            return lowest_row[0], lowest_row[4]
        else:
            return None  # Return None if no row is found or the 5th value doesn't exist


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

    #call function to train

    # Get the chat ID using the filename
    #chat_id, model_id = getID(metaDataPath)

    chat_id = "54321"
    model_id = "f97b173f-5615-42df-beff-f8f15f31fd27-ft"

    # Initialize the conversation for the new chat
    chats[chat_id] = {"modelID": model_id, "messages": []}

    return jsonify({"chat_id": chat_id, "model_id": model_id, "message": "New chat created."})

# Route to handle messages in a chat
@app.route('/chat/<chat_id>', methods=['POST'])
def chat(chat_id):
    # Validate if chat_id exists
    if chat_id not in chats:
        return jsonify({"error": "Chat ID not found"}), 404

    # Get the user's message from the request
    data = request.get_json()
    user_prompt = data.get('prompt', '')

    model_id = chats[chat_id]["modelID"]

    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Add user's message to the chat conversation
    chats[chat_id]["messages"].append({"role": "User", "content": user_prompt})

    # Placeholder bot response
    bot_response = chat_with_bot(user_prompt, model_id, chats[chat_id]["messages"])
    bot_response = re.sub(r'\b(user|assistant|chatbot):', '', bot_response, flags=re.IGNORECASE).strip()
    chats[chat_id]["messages"].append({"role": "Chatbot", "content": bot_response})

    # Return the updated conversation
    return jsonify({"conversation": chats[chat_id]["messages"]})

# Route to fetch a conversation
@app.route('/conversation/<chat_id>', methods=['GET'])
def get_conversation(chat_id):
    # Validate if chat_id exists
    if chat_id not in chats:
        return jsonify({"error": "Chat ID not found"}), 404

    return jsonify({"conversation": chats[chat_id]["messages"]})

# Route to reset or delete a chat
@app.route('/reset_chat/<chat_id>', methods=['DELETE'])
def reset_chat(chat_id):
    # Validate if chat_id exists
    if chat_id not in chats:
        return jsonify({"error": "Chat ID not found"}), 404

    # Remove the chat
    chats[chat_id]["messages"].clear()
    return jsonify({"message": f"Chat {chat_id} has been reset."})

if __name__ == "__main__":
    app.run(debug=True)
