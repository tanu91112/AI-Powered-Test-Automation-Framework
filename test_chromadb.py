from chunking.splitter import split_text
from embeddings.embedding import create_embeddings
from vectordb.chroma_db import store_embeddings

text = """
The user should login using email and password.

If password is incorrect,
system should display error message.

User should reset password using email verification.
"""

chunks = split_text(text)

embeddings = create_embeddings(chunks)

store_embeddings(
    chunks,
    embeddings,
    source="sample_requirement.txt"
)