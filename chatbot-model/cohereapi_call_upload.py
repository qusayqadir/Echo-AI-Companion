import cohere
from cohere.finetuning import Settings, FinetunedModel, BaseModel
import time

def uploadCohere(botname): 
    cohere_api_key_path = "../data/(git_ignore)cohere_api_key.txt"
    cohere_api_key = "" 

    with open(cohere_api_key_path, 'r') as file: 
        cohere_api_key = file.readline().strip() 

    co = cohere.ClientV2(cohere_api_key) 

    # Upload the dataset
    chat_dataset = co.datasets.create(
        name=f"{botname}_chatbot_dataset",
        data=open(f"../data/uploaded_data/{botname}_coherefriendly.jsonl", "rb"),
        type="chat-finetune-input"
    )

    time.sleep(60)
    dataset_id = chat_dataset.id
    print(f"Dataset uploaded. Dataset ID: {dataset_id}")

    return dataset_id