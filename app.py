from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    global tokenizer
   
    model_name = "VietAI/envit5-translation"
    tokenizer = AutoTokenizer.from_pretrained(model_name)  
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to("cuda")

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
    inputs = tokenizer(prompt, return_tensors="pt",padding=True).input_ids.to("cuda")
    outputs = model.generate(inputs, max_length=512)
    result = tokenizer.batch_decode(outputs,skip_special_tokens=True)

    # Return the results as a dictionary
    return result[0]
