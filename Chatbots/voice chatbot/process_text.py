
from transformers import pipeline

model_name = "bert-base-uncased"
nlp_pipeline = pipeline("fill-mask", model=model_name)

def process_text(input_text):
    masked_text = input_text.replace('.', ' .') + " [MASK]"
    results = nlp_pipeline(masked_text)
    return results[0]['sequence']
