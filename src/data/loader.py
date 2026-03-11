"""
Date: 11/03/2026
Dataset loading functions
"""

import pandas as pd
import os

#loading the bilingual dataset
def load_bilingual_dataset(path='Datasets/processed/bilingual_merged.csv'):
    if os.path.exists(path):
        df = pd.read_csv(path)
        return df
    else:
        print(f" File not found: {path}")
        return None

def load_combined_spanish_dataset(path='Datasets/processed/spanish_merged.csv'):
    if os.path.exists(path):
        df = pd.read_csv(path)
        return df
    else:
        print(f" File not found: {path}")
        return None

def load_offendes_dataset(data_path='Datasets/processed/offendes_dataset_reformatted.csv'):
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        return df
    else:
        print(f" File not found: {data_path}")
        return None

def load_colombian_dataset(data_path='Datasets/processed/colombian_dataset_reformatted.csv'):
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        return df
    else:
        print(f" File not found: {data_path}")
        return None

def load_english_dataset(data_path='Datasets/processed/english_dataset_reformatted.csv'):
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        return df
    else:
        print(f" File not found: {data_path}")
        return None
