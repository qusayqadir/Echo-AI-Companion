import cohere

# Initialize the Cohere client with your API key
co = cohere.Client('DJ2IaSIlgQIGZuk1WNuV1yP1B5nuP9w7qIvBFoe6')  # Replace with your actual API key

# Model ID
model_id = 'f97b173f-5615-42df-beff-f8f15f31fd27-ft'

# Function to chat with the bot
def chat_with_bot(message, model_id, chat_history):
    
    # Format the chat history into a single string for the API
    formatted_history = "\n".join([f"{entry['role']}: {entry['content']}" for entry in chat_history])
    
    # Call the Cohere API
    co = cohere.Client('DJ2IaSIlgQIGZuk1WNuV1yP1B5nuP9w7qIvBFoe6')

    response = co.chat(
        model=model_id,
        message=formatted_history
    )
    
    # Get the bot's response and append it to the chat history
    bot_response = response.text
    
    return bot_response


