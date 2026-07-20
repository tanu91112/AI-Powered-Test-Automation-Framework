def clean_code(code):

    if "```python" in code:
        code = code.replace("```python", "")

    if "```" in code:
        code = code.replace("```", "")

    return code.strip()