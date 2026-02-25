import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    headless = os.getenv("HEADLESS", "0") == "1"

    options = Options()

    # Headless mode for CI (GitHub Actions)
    if headless:
        # "new" headless is more stable on modern Chrome
        options.add_argument("--headless=new")

    # These 2 are the big ones that stop CI Chrome crashes
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Helpful stability defaults
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    # Create driver (Selenium Manager will handle driver install)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)

    yield driver

    driver.quit()