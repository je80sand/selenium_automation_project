import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.login_page import LoginPage


@pytest.mark.smoke
def test_secure_area_full_assertions(driver):
    """
    Polished, assertion-heavy test:
    - Load login page and assert key elements
    - Login with known-good creds
    - Assert we are on /secure + header + flash + logout visible
    - Logout
    - Assert redirected to /login + logout flash message

    NOTE:
    CI/headless can be slightly slower on redirects, so we explicitly WAIT
    for the URL to change after logout before asserting.
    """

    # --- Load login page ---
    login_page = LoginPage(driver).load()

    # --- Login page assertions (extra polish) ---
    assert "/login" in driver.current_url, f"Expected to be on /login, got: {driver.current_url}"

    heading = login_page.get_heading_text()
    assert heading == "Login Page", f"Expected heading 'Login Page', got: {heading!r}"

    # Ensure core inputs/buttons are present + usable
    username_el = driver.find_element(*LoginPage.USERNAME)
    password_el = driver.find_element(*LoginPage.PASSWORD)
    login_btn_el = driver.find_element(*LoginPage.LOGIN_BTN)

    assert username_el.is_displayed(), "Username field is not displayed"
    assert password_el.is_displayed(), "Password field is not displayed"
    assert login_btn_el.is_displayed(), "Login button is not displayed"
    assert login_btn_el.is_enabled(), "Login button is not enabled"

    # --- Login with known-good creds ---
    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")

    # --- Secure area assertions ---
    current_url = driver.current_url
    assert "/secure" in current_url, f"Expected to be on /secure, got: {current_url}"

    header = secure_page.get_header_text().strip()
    assert header == "Secure Area", f"Expected header 'Secure Area', got: {header!r}"

    flash = secure_page.get_flash_message().strip()
    assert "You logged into a secure area!" in flash, f"Expected login success flash, got: {flash!r}"

    assert secure_page.is_logout_displayed(), "Expected logout button to be visible"

    # --- Logout + assertions ---
    login_after_logout = secure_page.logout()

    # IMPORTANT: wait for redirect to /login (CI/headless can lag slightly)
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

    current_url = driver.current_url
    assert "/login" in current_url, f"Expected to be back on /login after logout, got: {current_url}"

    flash = login_after_logout.get_flash_message().strip()
    assert "You logged out of the secure area!" in flash, f"Expected logout flash, got: {flash!r}"