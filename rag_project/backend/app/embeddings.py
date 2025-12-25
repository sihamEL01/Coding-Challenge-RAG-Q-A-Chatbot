# backend/app/embeddings.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts):
    """
    Input: list of text chunks
    Output: numpy array of embeddings
    """
    embeddings = model.encode(texts, show_progress_bar=True)
    return np.array(embeddings)
