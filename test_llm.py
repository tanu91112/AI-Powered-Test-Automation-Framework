from llm.prompt import build_prompt
from llm.generator import generate_test_cases

requirements = """
The user should login using email and password.

If password is incorrect,
display an error.

User should reset password using email verification.
"""

prompt = build_prompt(requirements)

output = generate_test_cases(prompt)

print(output)