from retrieval.retriever import retrieve_chunks
from llm.prompt import build_prompt
from llm.generator import generate_test_cases

# User query
query = "Generate functional test cases for the login feature"

# Step 1: Retrieve relevant chunks from ChromaDB
results = retrieve_chunks(query)

documents = results["documents"][0]

print("=" * 80)
print("RETRIEVED REQUIREMENTS")
print("=" * 80)

for i, doc in enumerate(documents, start=1):
    print(f"\nChunk {i}:")
    print(doc)

# Step 2: Combine retrieved chunks
requirements = "\n\n".join(documents)

# Step 3: Build prompt
prompt = build_prompt(requirements)

print("\n" + "=" * 80)
print("PROMPT SENT TO LLM")
print("=" * 80)
print(prompt)

# Step 4: Generate test cases
response = generate_test_cases(prompt)

print("\n" + "=" * 80)
print("GENERATED TEST CASES")
print("=" * 80)
print(response)