from cohere.finetuning import (
    BaseModel,
    BaseType,
    FinetunedModel,
    Settings,
)
import cohere
import pandas as pd 
import time

# Fine-tune the model

def fine_tune_model(botname, dataset_ID): 
    cohere_api_key_path = "../data/(git_ignore)cohere_api_key.txt"
    cohere_api_key = "" 

    with open(cohere_api_key_path, 'r') as file: 
        cohere_api_key = file.readline().strip() 

    # Initialize the Cohere client with your API key
    co = cohere.Client(cohere_api_key)
    botname_file_name = botname

    model_name = f"{botname_file_name}_chatbot_model".lower().replace(" ", "_")


        # Get the datasetID from the same row
    dataset_id_caller = dataset_ID  # Use `.values[0]` to extract the scalar value


    create_response = co.finetuning.create_finetuned_model(
        request=FinetunedModel(
            # create a new name for the dataset, and replace the "chatbot" with the persons name 
            name= model_name,  # Name of the fine-tuned 
            settings = Settings(
                base_model=BaseModel(
                    base_type= "BASE_TYPE_CHAT",
                ),
                dataset_id= f"{dataset_id_caller}" 
            )
        )
    )

    model_id = create_response.id

    while True:
        # Fetch the fine-tuned model details
        model_status_response = co.finetuning.get_finetuned_model(model_id)
        status = model_status_response.status  # The status field indicates the training status

        print(f"Training status: {status}")
        
        if status == "COMPLETED":
            print(f"Model training completed. Model ID: {model_id}")
            break
        elif status == "FAILED":
            raise Exception(f"Model training failed. Model ID: {model_id}")
        else:
            # Wait before polling again
            time.sleep(12000)  # Adjust polling interval as needed


    return model_id 

    # Return the completed model ID


# print(create_response)

# get the fine-tuned model object


