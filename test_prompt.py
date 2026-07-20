from llm.prompt import build_prompt

requirements = """
The user should login using email and password.

If password is incorrect,
display an error.

User should reset password using email verification.
"""

prompt = build_prompt(requirements)

print(prompt)