from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingGenerator:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def create_embeddings(self, chunks):

        texts = [

            chunk["content"]

            for chunk in chunks

        ]

        embeddings = self.model.encode(

            texts,

            convert_to_numpy=True,

            show_progress_bar=True

        )

        for chunk, embedding in zip(

            chunks,

            embeddings

        ):

            chunk["embedding"] = embedding

        return chunks