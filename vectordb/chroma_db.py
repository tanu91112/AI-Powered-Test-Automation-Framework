import chromadb

client = chromadb.PersistentClient(path="chroma_storage")

collection = client.get_or_create_collection(
    name="requirements"
)


def store_embeddings(chunks, embeddings, source):
    ids = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f"{source}_chunk_{i}")

        metadatas.append({
            "source": source,
            "chunk_number": i
        })

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print(f"✅ Stored {len(chunks)} chunks from {source}")