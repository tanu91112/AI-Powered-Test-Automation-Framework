from chunking.splitter import split_text
from embeddings.embedding import create_embeddings

text = """
The user should login using email and password.

If password is incorrect,
system should display error message.

User should reset password using email verification.
"""

chunks = split_text(text)

vectors = create_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Embedding dimension:", len(vectors[0]))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)

    print("\nEmbedding Vector:")
    print(vectors[i])        # Prints all 384 values

    print("\nFirst 10 values:")
    print(vectors[i][:10])   # Prints only the first 10 values

    print("-" * 60)

    print("\nVector Shape:", vectors.shape)
    print("Data Type:", type(vectors))