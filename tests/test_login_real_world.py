import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver).load()

    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")

    # Extra safety wait (CI / slower machines)
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))

    assert "/secure" in driver.current_url
    assert secure_page.get_header_text() == "Secure Area"
    assert "You logged into a secure area!" in secure_page.get_flash_message()
    assert secure_page.is_logout_displayed() is True