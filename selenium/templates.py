def selenium_prompt(test_cases):

    return f"""
Generate Selenium Python automation code.

Test Cases:

{test_cases}

Rules:
- Use Selenium WebDriver
- Use Chrome browser
- Use By selectors
- Add proper waits
- Return only Python code

"""