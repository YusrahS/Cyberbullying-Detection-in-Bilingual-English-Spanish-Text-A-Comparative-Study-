import pandas as pd, re

def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)   
    text = re.sub(r'@\w+', ' ', text)                
    text = re.sub(r'#(\w+)', r'\1', text)               
    text = re.sub(r'\s+', ' ', text).strip()
    return text
