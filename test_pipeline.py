from retrieval.retriever import retrieve_chunks
from llm.prompt import build_prompt
from llm.generator import generate_test_cases
from automation.generator import generate_selenium_script


# Step 1
query = "Generate login test cases"


# Step 2
results = retrieve_chunks(query)

documents = results["documents"][0]

requirements = "\n\n".join(documents)


print("="*80)
print("RETRIEVED REQUIREMENTS")
print("="*80)

print(requirements)



# Step 3
prompt = build_prompt(requirements)



# Step 4
test_cases = generate_test_cases(prompt)


print("\n"+"="*80)
print("GENERATED TEST CASES")
print("="*80)

print(test_cases)



# Step 5
selenium_code = generate_selenium_script(test_cases)


print("\n"+"="*80)
print("GENERATED SELENIUM CODE")
print("="*80)

print(selenium_code)