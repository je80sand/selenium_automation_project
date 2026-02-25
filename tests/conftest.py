import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):
    options = Options()

    # Headless mode for CI
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    # Screenshot on failure
    if request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        driver.save_screenshot(
            f"reports/screenshots/{request.node.name}.png"
        )

    driver.quit()


# Hook to detect test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)