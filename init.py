
from sentence_transformers import SentenceTransformer, losses, util
from sentence_transformers.readers import InputExample
import pickle
import pandas as pd
import torch
import hnswlib
import numpy as np

model_name = 'all-mpnet-base-v2'
file_path_embeddings = r'C:\Users\ganesh\fastapi-env\k2k\hashtag_embeddings_food.pkl'
model = SentenceTransformer(model_name)


with open(file_path_embeddings, 'rb') as f:
    word_embeddings = pickle.load(f)


df = pd.DataFrame(word_embeddings, columns=['Word', 'Embedding'])
hashtags = df["Word"].tolist()
corpus_embeddings = np.asarray(df['Embedding'].tolist())
corpus_embeddings = torch.from_numpy(corpus_embeddings)
dimension = corpus_embeddings.shape[1]
num_neighbors = 10
p = hnswlib.Index(space='l2', dim=dimension)  
p.init_index(max_elements=len(corpus_embeddings), ef_construction=200, M=16)
p.add_items(corpus_embeddings)
p.set_ef(50)
