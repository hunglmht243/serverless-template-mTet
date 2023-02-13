# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    model_name = "VietAI/envit5-translation"
    tokenizer = AutoTokenizer.from_pretrained(model_name)  
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

if __name__ == "__main__":
    download_model()