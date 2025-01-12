from cohere.finetuning import (
    BaseModel,
    BaseType,
    FinetunedModel,
    Settings,
)
import cohere

cohere_api_key_path = "(git_ignore)cohere_api_key.txt"
cohere_api_key = "" 

with open(cohere_api_key_path, 'r') as file: 
    cohere_api_key = file.readline().strip() 

# Initialize the Cohere client with your API key
co = cohere.Client(cohere_api_key)

# Fine-tune the model

def fine_tune_mode(): 
    create_response = co.finetuning.create_finetuned_model(
        request=FinetunedModel(
            # create a new name for the dataset, and replace the "chatbot" with the persons name 
            name="chatbot_datasetv2",  # Name of the fine-tuned 
            settings = Settings(
                base_model=BaseModel(
                    base_type= "BASE_TYPE_CHAT",
                ),
                dataset_id="chatbot-dataset-vwbdxg"
            )
        )
    )

    return create_response

# print(create_response)

# get the fine-tuned model object

get_response = fine_tune_mode() 

