import cohere 
from cohere.finetuning import Settings, FinetunedModel, BaseModel 
from cohere.finetuning import (
    BaseModel,
    FinetunedModel,
    Settings,
)


def upload_data_cohere(cohere_api_key): 

    co = cohere.ClientV2(cohere_api_key) 

    # find a file that ends with the json file

    chat_dataset = co.datasets.create(
        name = "chatbot_dataset",
        data = open("../data/Ryan_coherefriendly.jsonl", "rb"),
        type = "chat-finetune-input"
    )
# print(chat_dataset)

#return a dataset_id ??? 

if __name__ == "__main__": 

    cohere_api_key_path = "(git_ignore)cohere_api_key.txt"
    cohere_api_key = "" 

    with open(cohere_api_key_path, 'r') as file: 
        cohere_api_key = file.readline().strip() 










