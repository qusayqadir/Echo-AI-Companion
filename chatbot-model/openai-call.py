import json
import codecs
import os
import openai
import re 

def processdata(uploaded_chat, cleaned_chat):
    with open(uploaded_chat, 'r') as file: 
        # Determine the chatbot from the first line
        first_line = file.readline()
        chatbot = first_line.split(']')[1].split(':')[0].strip()

        # Initialize user as None
        user = None

        # Determine the user (the first speaker who isn't the chatbot)
        while user is None:
            next_line = file.readline()
            if ']' in next_line:  # Ensure it's a valid line with a timestamp
                temp_speaker = next_line.split(']')[1].split(':')[0].strip()
                if temp_speaker != chatbot:
                    user = temp_speaker

        # Process the rest of the lines
    with open (uploaded_chat, 'r') as file, open(cleaned_chat, 'w') as output_file: 
        remove_line = file.readline()
        lines = file.readlines() 
    
        for line in lines:
            if ']' in line:  # Ensure it's a valid line
                line_content = line.split(']', 1)[1]
                output_file.write(line_content)

    
        return chatbot, user


def callOpenAI(open_api_key, cleaned_chat, output_file, chatbot, user):
    with open(cleaned_chat, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Build the OpenAI prompt dynamically with chatbot and user names
    prompt = f"""
    Please process the following file contents as described:

    Input:
    {file_content}

    Instructions:
    1. This is a conversation between {user} (the user) and {chatbot} (the chatbot). User talks first. 
    2. Determine where each conversation begins and ends. Save the conversations in the format:
    {{
        "messages": [
            {{
                "role": "System",
                "content": "You are a chatbot trained to answer the user's questions."
            }},
            {{
                "role": "User",
                "content": "Hello"
            }},
            {{
                "role": "Chatbot",
                "content": "Greetings! How can I help you?"
            }},
            {{
                "role": "User",
                "content": "What makes a good running route?"
            }},
            {{
                "role": "Chatbot",
                "content": "A sidewalk-lined road is ideal so that you’re up and off the road away from vehicular traffic."
            }}
        ]
    }}

    3. Associate the content with the correct role (user or chatbot) as labeled in the .txt file.
    4. For each new conversation, create a new JSON object and append it to the output file.

    Output: Only the processed JSONL file, and I need at least 2 conversatoins to be returned, I need full conversations returned.
    Each conversation should have follow the same format as the example given. I need the file as a JSONL file, each line to be an individual JSON object
    """

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.7
    )

    processed_content = response['choices'][0]['message']['content']

    # Write the processed content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(processed_content)
    
def cleanOpenAIResponse(output_file): 

    try:
        # Read the file content
        with open(output_file, 'r') as file:
            content = file.read()
        
        # Extract the content within the outermost square brackets
        match = re.search(r'\[.*\]', content, re.DOTALL)
        if match:
            cleaned_content = match.group(0)  # Extract matched text
            
            # Overwrite the file with cleaned content
            with open(output_file, 'w') as file:
                file.write(cleaned_content)
            print("File cleaned and overwritten successfully.")
        else:
            print("No content found within square brackets.")
    
    except Exception as e:
        print(f"Error occurred: {e}")

 
def convert_to_json1(output_file): 
    with open(output_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for conversation in data:  # Each conversation is written as a single line
            json.dump(conversation, outfile)
            outfile.write('\n')  # Add a newline after each JSON object


def utf8_encoding(input_file):
    temp_file_path = input_file + ".tmp"

    with codecs.open(input_file, 'r', encoding='utf-8', errors='replace') as infile, \
            codecs.open(temp_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line)

    os.replace(temp_file_path, input_file)


if __name__ == "__main__":
    uploaded_chat = "../data/Ryan_uploaded_chat.txt"
    cleaned_chat = "../data/Ryan_cleaned_chat.txt"
    output_file = "../data/Ryan_coherefriendly.jsonl"

    uploaded_chat_path = "../data" 
    cleaned_chat_path = "../data" 
    output_file_path = "../data"


    chatbot, user = processdata(uploaded_chat, cleaned_chat)
    
    output_file = f"../data/{chatbot}_coherefriendly.jsonl" 

    for file in os.listdir(uploaded_chat): 
        if file.endswith(f"{chatbot}_uploaded_chat.txt"): 
            uploaded_chat = os.path.join(uploaded_chat_path, file) 
        elif file.endswith(f"{chatbot}_cleaned_chat.txt"): 
            uploaded_chat = os.path.join(cleaned_chat_path, file) 
    
    output_file = os.path.join(output_file_path, f"{chatbot}_coherefriendly.jsonl") 


    open_api_key_file = "(git_ignore)openai_api_key.txt"

    with open(open_api_key_file, 'r') as file:
        open_api_key = file.readline().strip()
        openai.api_key = open_api_key

    # Process data and get chatbot and user names
    chatbot, user = processdata(uploaded_chat, cleaned_chat)

    # Call OpenAI and generate JSONL output
    # callOpenAI(open_api_key, cleaned_chat, output_file, chatbot, user)
    # cleanOpenAIResponse(output_file)

    convert_to_json1(output_file)




    # Ensure the output JSONL file is UTF-8 encoded
    # utf8_encoding(output_file)
