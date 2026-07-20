"""
LLM Router

Choose which LLM to use by changing LLM_PROVIDER.

Options:
- flan
- gemini
- openai
"""

LLM_PROVIDER = "flan"  # Change to: flan | gemini | openai


if LLM_PROVIDER == "flan":
    from llm.flan_t5 import generate_with_flan

    def generate_test_cases(prompt):
        return generate_with_flan(prompt)


elif LLM_PROVIDER == "gemini":
    from llm.gemini import generate_with_gemini

    def generate_test_cases(prompt):
        return generate_with_gemini(prompt)


elif LLM_PROVIDER == "openai":
    from llm.openai import generate_with_openai

    def generate_test_cases(prompt):
        return generate_with_openai(prompt)


else:
    raise ValueError(
        "Invalid LLM_PROVIDER. Choose from: flan, gemini, openai."
    )