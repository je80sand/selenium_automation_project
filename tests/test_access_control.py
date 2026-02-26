import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
def test_cannot_access_secure_without_login(driver):
    """
    Access control (assertion-heavy):
    - Navigate directly to /secure without logging in
    - Assert redirect to /login
    - Assert flash message indicates login is required
    - Assert login form fields + button are visible
    """

    base_url = "https://the-internet.herokuapp.com"
    secure_url = f"{base_url}/secure"
    login_url = f"{base_url}/login"

    driver.get(secure_url)

    wait = WebDriverWait(driver, 10)

    # 1) URL should become /login (redirect)
    wait.until(EC.url_contains("/login"))
    current_url = driver.current_url
    assert "/login" in current_url, f"Expected redirect to /login, got: {current_url}"
    assert current_url.startswith(login_url), f"Expected URL to start with {login_url}, got: {current_url}"

    # 2) Flash message should mention login requirement
    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text.lower()
    assert "must" in flash, f"Expected 'must' in flash message, got: {flash}"
    assert "login" in flash, f"Expected 'login' in flash message, got: {flash}"

    # 3) Login form should be visible and usable
    username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

    assert username.is_displayed(), "Username field is not displayed"
    assert password.is_displayed(), "Password field is not displayed"
    assert login_btn.is_displayed(), "Login button is not displayed"
    assert login_btn.is_enabled(), "Login button is not enabled"

    # 4) Page content assertions (extra polish)
    heading = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2"))).text.strip()
    assert heading.lower() == "login page", f"Expected heading 'Login Page', got: {heading}"