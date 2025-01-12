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
    openai.api_key = open_api_key

    # Read the content of the .txt file
    with open(cleaned_chat, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Build the OpenAI prompt dynamically with chatbot and user names
    prompt = f"""
    You are a helpful assistant processing chat logs. Please analyze the following chat logs between {user} (User) and {chatbot} (Chatbot).

    Input:
    {file_content}

    Instructions:
    - Extract the conversation into JSONL format.
    - Each conversation starts with the "User" and alternates between "User" and "Chatbot".
    - Format each conversation as:
        {{
            "messages": [
                {{
                    "role": "User",
                    "content": "User's message here"
                }},
                {{
                    "role": "Chatbot",
                    "content": "Chatbot's response here"
                }}
            ]
        }}
    - Ensure each conversation is separated into individual JSON objects on new lines.

    Return only the processed JSONL content.
    """

    # Call the OpenAI API with the prompt
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.5
    )

    # Extract the response content
    processed_content = response['choices'][0]['message']['content']

    # Validate and write the response to the output file
    if processed_content.strip():  # Ensure the response is not empty
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(processed_content)
        print(f"Output written to {output_file}")
    else:
        raise ValueError("OpenAI returned an empty response.")



def cleanOpenAIResponse(output_file):
    try:
        # Read the file content
        with open(output_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Validate each line as JSON
        cleaned_lines = []
        for line in lines:
            try:
                json_data = json.loads(line.strip())  # Validate JSON
                cleaned_lines.append(json_data)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line.strip()}")

        # Overwrite the file with valid JSON lines
        with open(output_file, 'w', encoding='utf-8') as file:
            for json_obj in cleaned_lines:
                file.write(json.dumps(json_obj) + '\n')  # Write valid JSONL

        print("File cleaned and overwritten successfully.")
    except Exception as e:
        print(f"Error occurred during cleaning: {e}")


 
def convert_to_json1(output_file):
    try:
        with open(output_file, 'r', encoding='utf-8') as infile:
            data = [json.loads(line) for line in infile]  # Load JSONL lines

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for conversation in data:
                json.dump(conversation, outfile)
                outfile.write('\n')  # Ensure proper JSONL format

        print("Conversion to JSONL complete.")
    except Exception as e:
        print(f"Error during JSONL conversion: {e}")


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
