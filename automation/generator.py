def generate_selenium_script(test_cases):

    return """
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://example.com")

time.sleep(3)

driver.quit()
"""