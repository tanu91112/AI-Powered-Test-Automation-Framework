from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from torch.jit import script


def execute_test(script):

    driver = None

    try:
        options = Options()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)

        exec(
            script,
            {
                "driver": driver
            }
        )

        time.sleep(5)

        driver.quit()

        return "PASS"

    except Exception as e:

        if driver:
            driver.save_screenshot(
                "failure.png"
            )
            driver.quit()

        return f"FAIL: {str(e)}"
    
print("CODE TO EXECUTE:")
print(script)