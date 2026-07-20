from chunking.splitter import split_text

text = """
The user should login using email and password.

If password is incorrect,
system should display error message.

User should reset password using email verification.
"""

chunks = split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nCHUNK {i}")
    print(chunk)