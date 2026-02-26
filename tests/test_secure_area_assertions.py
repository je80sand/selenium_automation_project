import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.pages.login_page import LoginPage


@pytest.mark.smoke
def test_secure_area_full_assertions(driver):
    """
    Stable, CI-safe version with strong waits.
    """

    wait = WebDriverWait(driver, 15)

    # --- Load login page ---
    login_page = LoginPage(driver).load()

    # Wait for login page to fully load
    wait.until(EC.url_contains("/login"))
    wait.until(EC.visibility_of_element_located(LoginPage.USERNAME))

    assert "/login" in driver.current_url

    heading = login_page.get_heading_text()
    assert heading == "Login Page"

    # --- Login ---
    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")

    # Wait for secure page
    wait.until(EC.url_contains("/secure"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))

    current_url = driver.current_url
    assert "/secure" in current_url

    header = secure_page.get_header_text().strip()
    assert header == "Secure Area"

    flash = secure_page.get_flash_message().strip()
    assert "You logged into a secure area!" in flash

    assert secure_page.is_logout_displayed()

    # --- Logout ---
    secure_page.logout()

    # Wait for logout button to disappear
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "a.button.secondary.radius")))

    # Wait for redirect
    wait.until(EC.url_contains("/login"))

    # Wait for login heading again
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))

    current_url = driver.current_url
    assert "/login" in current_url

    flash = driver.find_element(By.ID, "flash").text.strip()
    assert "You logged out of the secure area!" in flash