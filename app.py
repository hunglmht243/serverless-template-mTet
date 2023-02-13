from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    global tokenizer
    device = 0 if torch.cuda.is_available() else -1
    model_name = "VietAI/envit5-translation"
    tokenizer = AutoTokenizer.from_pretrained(model_name)  
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model
    global tokenizer
    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    if prompt == None:
        return {'message': "No prompt provided"}
    
    # Run the model
    result_length = len(prompt)+100
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    outputs = model.generate(inputs["input_ids"], max_length=result_length)
    result = tokenizer.decode(outputs[0],skip_special_tokens=True))

    # Return the results as a dictionary
    return result
