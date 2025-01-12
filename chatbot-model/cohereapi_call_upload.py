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

    dataset_id = chat_dataset.id
    print(f"Dataset uploaded. Dataset ID: {dataset_id}")

    # Polling to check dataset status
    while True: 
        dataset_status = co.datasets.get(dataset_id).status  # Fetch the updated status
        print(f"Dataset status: {dataset_status}")

        if dataset_status == "STATUS_READY":  # Check if the dataset is ready
            print(f"Dataset {dataset_id} is validated and ready for fine-tuning.")
            return dataset_id
        elif dataset_status == "STATUS_FAILED":
            raise Exception(f"Dataset validation failed for Dataset ID: {dataset_id}")
        
        # Wait before polling again
        time.sleep(30)  # Adjust polling interval as need