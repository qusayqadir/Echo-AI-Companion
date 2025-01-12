import cohere 
from cohere.finetuning import Settings, FinetunedModel, BaseModel 
from cohere.finetuning import (
    BaseModel,
    FinetunedModel,
    Settings,
)

def uploadCohere(botname): 

    cohere_api_key_path = "../data/(git_ignore)cohere_api_key.txt"
    cohere_api_key = "" 

    with open(cohere_api_key_path, 'r') as file: 
        cohere_api_key = file.readline().strip() 

    co = cohere.ClientV2(cohere_api_key) 

    # find a file that ends with the json file

    chat_dataset = co.datasets.create(
        name = f"{botname}_chatbot_dataset",
        data = open(f"../data/uploaded_data/{botname}_coherefriendly.jsonl", "rb"),
        type = "chat-finetune-input"
    )

    dataset_id = chat_dataset.id
    return dataset_id 




# print(chat_dataset)

#return a dataset_id ??? 









