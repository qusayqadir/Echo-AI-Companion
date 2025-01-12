from cohere.finetuning import (
    BaseModel,
    BaseType,
    FinetunedModel,
    Settings,
)
import cohere
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


    
    # Create the fine-tuned model
    create_response = co.finetuning.create_finetuned_model(
        request=FinetunedModel(
            name=model_name,  # Name of the fine-tuned model
            settings=Settings(
                base_model=BaseModel(
                    base_type="BASE_TYPE_CHAT",
                ),
                dataset_id=dataset_ID
            )
        )
    )

    model_id = create_response.id
    print(f"Fine-tuning initiated. Model ID: {model_id}")

    # Polling for fine-tuned model training status
    while True:
        model_status_response = co.finetuning.get_finetuned_model(model_id)
        status = model_status_response.status  # Training status field

        print(f"Training status: {status}")

        if status == "STATUS_READY":
            print(f"Model training completed. Model ID: {model_id}")
            return model_id
            break
        elif status == "STATUS_FAILED":
            raise Exception(f"Model training failed. Model ID: {model_id}")

        # Wait before polling again
        time.sleep(300)
