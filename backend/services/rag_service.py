import faiss
import numpy as np

from backend.utils.pdf_loader import DocumentLoader
from backend.utils.chunking import TextChunker
from backend.utils.embeddings import EmbeddingGenerator


class RAGService:

    def __init__(self):

        print("=" * 60)
        print("Building Medical Knowledge Base...")
        print("=" * 60)

        # Load embedding model ONCE
        self.embedder = EmbeddingGenerator()

        # Load documents
        loader = DocumentLoader()
        documents = loader.load_documents()

        # Split documents
        chunker = TextChunker()
        self.chunks = chunker.split_documents(documents)

        # Create embeddings once
        self.chunks = self.embedder.create_embeddings(self.chunks)

        vectors = np.array(
            [chunk["embedding"] for chunk in self.chunks],
            dtype=np.float32
        )

        self.index = faiss.IndexFlatL2(vectors.shape[1])
        self.index.add(vectors)

        print(f"\nIndexed {len(self.chunks)} document chunks.")

    def search(self, query, top_k=3):

        query_embedding = self.embedder.model.encode(
            [query],
            convert_to_numpy=True
        ).astype(np.float32)

        _, indices = self.index.search(query_embedding, top_k)

        return [self.chunks[i] for i in indices[0]]