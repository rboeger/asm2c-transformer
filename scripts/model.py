from transformers import AutoModelForSeq2SeqLM

def load_model(model_name="t5-small"):
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model