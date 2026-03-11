import os

# Create directory if it doesn't exist
os.makedirs('src/visualization', exist_ok=True)

%%writefile src/visualization/plot.py
"""
Plotting functions for EDA and visualizations.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_label_distribution(df, title="Label Distribution", save_path=None):
    """
    Plot distribution of binary labels.
    """
    plt.figure(figsize=(8, 6))
    
    label_counts = df['binary_label'].value_counts().sort_index()
    colors = ['#2ecc71', '#e74c3c']
    bars = plt.bar(['Non-Abusive (0)', 'Abusive (1)'], label_counts.values, color=colors)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}', ha='center', va='bottom', fontsize=12)
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.ylabel('Count', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def plot_text_length(df, title="Text Length Distribution", save_path=None):
    """
    Plot distribution of text lengths by language and label.
    """
    df = df.copy()
    df['text_length'] = df['text'].astype(str).apply(len)
    
    plt.figure(figsize=(12, 6))
    
    ax = sns.boxplot(x='language', y='text_length', hue='binary_label', data=df,
                     palette=['#2ecc71', '#e74c3c'])
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Language', fontsize=12)
    plt.ylabel('Text Length (characters)', fontsize=12)
    plt.legend(title='Label', labels=['Non-Abusive', 'Abusive'])
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def plot_class_distribution_by_language(df, save_path=None):
    """
    Plot class distribution for each language.
    """
    # Create contingency table
    ct = pd.crosstab(df['language'], df['binary_label'], normalize='index') * 100
    ct.columns = ['Non-Abusive %', 'Abusive %']
    
    # Plot
    ax = ct.plot(kind='bar', figsize=(10, 6), 
                 color=['#2ecc71', '#e74c3c'], edgecolor='black')
    
    plt.title('Class Distribution by Language', fontsize=14, fontweight='bold')
    plt.xlabel('Language', fontsize=12)
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.legend(title='Label')
    plt.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=0)
    
    # Add value labels
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def plot_confusion_matrix(cm, labels=['Non-Abusive', 'Abusive'], title='Confusion Matrix', save_path=None):
    """
    Plot confusion matrix.
    """
    plt.figure(figsize=(8, 6))
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=labels, yticklabels=labels)
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.ylabel('True Label', fontsize=12)
    plt.xlabel('Predicted Label', fontsize=12)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def plot_training_history(history, save_path=None):
    """
    Plot training history from model training.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot accuracy
    axes[0].plot(history.history['accuracy'], label='Train Accuracy')
    if 'val_accuracy' in history.history:
        axes[0].plot(history.history['val_accuracy'], label='Val Accuracy')
    axes[0].set_title('Model Accuracy', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Accuracy')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Plot loss
    axes[1].plot(history.history['loss'], label='Train Loss')
    if 'val_loss' in history.history:
        axes[1].plot(history.history['val_loss'], label='Val Loss')
    axes[1].set_title('Model Loss', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Loss')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

print("✅ plot.py created successfully!")
