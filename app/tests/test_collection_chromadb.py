# scripts/create_chroma_collection.py

from fastembed import TextEmbedding
import chromadb
from typing import List
import numpy as np

class FastEmbedEmbeddingFunction:
    """Wrapper para usar FastEmbed como embedding function no ChromaDB"""
    
    def __init__(self):
        self.embedding_model = TextEmbedding()
        self._name = "fastembed-default"
    
    def __call__(self, input: List[str]) -> List[List[float]]:
        """Converte lista de textos para embeddings"""
        embeddings = list(self.embedding_model.embed(input))
        return [embedding.tolist() for embedding in embeddings]
    
    def name(self) -> str:
        """Nome da função de embedding (requerido pelo ChromaDB)"""
        return self._name

def test_making_embeddings():
    # Parâmetros da coleção
    collection_name = "agno_docs"

    # Cria cliente ChromaDB persistente
    client = chromadb.PersistentClient(
        path="tmp/chromadb_store"  # Corrigido: tmp em vez de temp
    )

    # Cria função de embedding compatível
    embedding_function = FastEmbedEmbeddingFunction()

    # Cria a coleção com função de embedding
    chromadb_collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )
    print(f'✅ Coleção "{collection_name}" pronta em tmp/chromadb_store.')

    # Adiciona documento de teste
    docs = ["Este é um teste de inicialização da coleção."]
    ids = ["doc_init"]
    
    chromadb_collection.add(documents=docs, ids=ids)
    print("✅ Documento de teste inserido.")

    # Teste de busca
    results = chromadb_collection.query(
        query_texts=["teste inicialização"],
        n_results=1
    )
    print(f"✅ Teste de busca: {results['documents'][0]}")

if __name__ == "__main__":
    test_making_embeddings()