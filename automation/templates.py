def selenium_prompt(test_cases):

    return f"""

Convert this test case into Selenium Python code.

Test Case:

{test_cases}

Generate only Python code.

Use:

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://example.com")

"""