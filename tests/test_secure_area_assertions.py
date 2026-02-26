# tests/test_secure_area_assertions.py
import pytest

from src.pages.login_page import LoginPage


@pytest.mark.smoke
def test_secure_area_full_assertions(driver):
    """
    Polished, assertion-heavy test:
    - Login
    - Verify secure URL + header + flash message + logout button
    - Logout
    - Verify redirected to login + logout flash message
    """

    login = LoginPage(driver).load()
    login.load()

    # Login with known-good creds for https://the-internet.herokuapp.com/login
    secure = login.login("tomsmith", "SuperSecretPassword!")

    # --- Secure Area Assertions ---
    current_url = driver.current_url
    assert "/secure" in current_url, f"Expected to be on /secure but URL was: {current_url}"

    header = secure.get_header_text().strip()
    assert header == "Secure Area", f"Expected header 'Secure Area' but got: {header!r}"

    flash = secure.get_flash_message().strip()
    assert "You logged into a secure area!" in flash, f"Expected login success flash, got: {flash!r}"

    assert secure.is_logout_displayed(), "Expected logout button to be displayed, but it was not."

    # --- Logout + Assertions ---
    login_after_logout = secure.logout()

    current_url = driver.current_url
    assert "/login" in current_url, f"Expected to be on /login after logout but URL was: {current_url}"

    flash = login_after_logout.get_flash_message().strip()
    assert "You logged out of the secure area!" in flash, f"Expected logout flash, got: {flash!r}"