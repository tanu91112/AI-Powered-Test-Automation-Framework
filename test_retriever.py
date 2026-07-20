from retrieval.retriever import retrieve_chunks

query = "Generate login test cases"

results = retrieve_chunks(query)

print("=" * 60)
print("User Query:")
print(query)
print("=" * 60)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i in range(len(documents)):
    print(f"\nResult {i+1}")
    print("-" * 40)

    print("Source:")
    print(metadatas[i]["source"])

    print("\nChunk:")
    print(documents[i])

    print("\nDistance:")
    print(distances[i])