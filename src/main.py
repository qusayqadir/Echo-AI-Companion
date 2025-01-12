import os
import pandas as pd
import importlib.util
import openai 

import cohere 
from cohere.finetuning import Settings, FinetunedModel, BaseModel 
from cohere.finetuning import (
    BaseModel,
    FinetunedModel,
    Settings,
)


openai_api_key = "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"
cohere_api_key = "DJ2IaSIlgQIGZuk1WNuV1yP1B5nuP9w7qIvBFoe6"



def callOpenAI_throughMain(uploaded_chat):
    openai_call_filepath = "../chatbot-model/openai_call.py"
    module_name = "openai_call"

    # Load the module dynamically
    spec = importlib.util.spec_from_file_location(module_name, openai_call_filepath)
    openai_call = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(openai_call)

    uploaded_chat_file_path = "../data/uploaded_data"
    uploaded_chat_file = os.path.join(uploaded_chat_file_path, uploaded_chat)

    # Create cleaned and output file paths
    cleaned_data_file_name = uploaded_chat.split('_')[0] + "_cleaned_chat.txt"
    cleaned_chat_file_path = os.path.join(uploaded_chat_file_path, cleaned_data_file_name)
    output_chat_file = os.path.join(
        "../data/uploaded_data", uploaded_chat.split('_')[0] + "_coherefriendly.jsonl"
    )

    # Ensure the cleaned chat file exists
    if not os.path.exists(cleaned_chat_file_path):
        open(cleaned_chat_file_path, "a").close()

    # Process the data
    chatbot, user = openai_call.processdata(uploaded_chat_file, cleaned_chat_file_path)

    openai.api_key = openai_api_key


    # Call OpenAI and process output
    openai_call.callOpenAI(
        open_api_key=openai_api_key,
        cleaned_chat=cleaned_chat_file_path,
        output_file=output_chat_file,
        chatbot=chatbot,
        user=user,
    )
    openai_call.cleanOpenAIResponse(output_chat_file)
    openai_call.convert_to_json1(output_chat_file)

    return cleaned_chat_file_path, output_chat_file

def uploadtoCohere(botname): 
    openai_upload_filepath = "../chatbot-model/cohereapi_call_upload.py"
    module_name = "cohere"

    # Load the module dynamically
    spec = importlib.util.spec_from_file_location(module_name, openai_upload_filepath)
    cohere = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cohere)

    dataset_ID = cohere.uploadCohere(botname) 

    return dataset_ID 

if __name__ == "__main__":
    new_file_uploaded = False
    new_file_name = ""

    # Paths to the uploaded data directory and metadata CSV
    uploaded_data = "../data/uploaded_data"
    metadata_cohere_path = "../data/metadata_cohere.csv"

    # Load metadata CSV
    if not os.path.exists(metadata_cohere_path):
        print(f"Metadata CSV not found at {metadata_cohere_path}. Exiting.")
        exit(1)

    metadata_cohere_df = pd.read_csv(metadata_cohere_path)

    # Define the column name for uploaded files
    uploaded_column = "uploaded_chat_file"

    # Ensure the column exists
    if uploaded_column not in metadata_cohere_df.columns:
        print(f"Error: Column '{uploaded_column}' not found in metadata CSV.")
        exit(1)

    # Get the list of uploaded chat files from the metadata
    metadata_uploaded_column_list = metadata_cohere_df[uploaded_column].tolist()

    # Iterate over files in the uploaded data directory
    for file_name in os.listdir(uploaded_data):
        if file_name in metadata_uploaded_column_list:
            continue
        else:
            # Mark the file for processing
            new_file_uploaded = True
            new_file_name = file_name
            break

    # If a new file is found, process it
    if new_file_uploaded:
        # Initial row with placeholders
        new_row = {
            "chatBotName": new_file_name.split('_')[0], 
            "uploaded_chat_file": new_file_name,
            "cleaned_chat_file": "",  
            "output_chat_file": "",  
            "dataSetID": "",  
            "modelID": ""  
        }

        try:
            # Call the function to process the file
            cleaned_chat_file_path, output_chat_file = callOpenAI_throughMain(uploaded_chat=new_file_name)
            botname = new_file_name.split('_')[0]

            dataset_ID = uploadtoCohere(botname)

            # Update the row with the new values
            new_row["cleaned_chat_file"] = cleaned_chat_file_path
            new_row["output_chat_file"] = output_chat_file
            new_row["dataSetID"] = dataset_ID 

            # Convert the updated row to a DataFrame
            new_row_df = pd.DataFrame([new_row])

            # Append the updated row to the metadata DataFrame
            metadata_cohere_df = pd.concat([metadata_cohere_df, new_row_df], ignore_index=True)

            # Save the updated metadata to the CSV file
            metadata_cohere_df.to_csv(metadata_cohere_path, index=False)

            print(f"Processed and updated metadata for '{new_file_name}'.")
        except Exception as e:
            print(f"Error processing file '{new_file_name}': {e}")
    else:
        print("No new files found. Metadata is up-to-date.")
