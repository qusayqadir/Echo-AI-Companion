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
            name=model_name,
            settings=Settings(
                base_model=BaseModel(
                    base_type="BASE_TYPE_CHAT",
                ),
                dataset_id=f"{dataset_ID}"
            )
        )
    )

    print(f"Fine-tuning initiated for model: {model_name}. Waiting 20 minutes before fetching the model ID.")
    time.sleep(1200)  # Wait for 20 minutes

    # Attempt to retrieve the model ID
    model_id = create_response.id
    if not model_id:
        raise Exception(f"Failed to retrieve Model ID for model: {model_name} after 20 minutes.")

    return model_id
