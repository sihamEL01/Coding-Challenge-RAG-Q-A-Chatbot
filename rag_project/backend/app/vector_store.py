# backend/app/vector_store.py
import chromadb
from chromadb.config import Settings

CHROMA_DIR = "chroma_data"
COLLECTION_NAME = "documents"

# Initialize Chroma client (persistent)
chroma_client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_DIR,
        anonymized_telemetry=False
    )
)

def get_collection():
    return chroma_client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )


def save_documents(embeddings, documents, ids=None):
    """
    embeddings: List[List[float]]
    documents: List[str]
    ids: Optional[List[str]]
    """
    collection = get_collection()

    if ids is None:
        ids = [f"doc_{i}" for i in range(len(documents))]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )

    chroma_client.persist()


def query_documents(query_embedding, top_k=5):
    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results
