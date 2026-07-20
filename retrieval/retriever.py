import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_storage")

collection = client.get_collection(
    name="requirements"
)


def retrieve_chunks(query, top_k=5):
    """
    Retrieve the most relevant chunks from ChromaDB.
    """

    # Convert the user's question into an embedding
    query_embedding = model.encode(query).tolist()

    # Perform semantic search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results