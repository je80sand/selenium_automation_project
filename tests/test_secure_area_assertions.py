import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.login_page import LoginPage


@pytest.mark.smoke
def test_secure_area_full_assertions(driver):
    """
    CI-stable, assertion-heavy test with robust navigation + logout handling.
    Headless + parallel can be flaky on logout redirects, so we:
      - wait clickable
      - JS-click fallback
      - wait for staleness of a secure-page element
      - wait for login form visibility (not just URL)
    """

    wait = WebDriverWait(driver, 30)

    # --- Load login page ---
    login_page = LoginPage(driver).load()

    wait.until(EC.url_contains("/login"))
    wait.until(EC.visibility_of_element_located(LoginPage.USERNAME))

    assert "/login" in driver.current_url
    assert login_page.get_heading_text() == "Login Page"

    # --- Login ---
    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")

    wait.until(EC.url_contains("/secure"))
    secure_h2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))

    assert "/secure" in driver.current_url
    assert secure_page.get_header_text().strip() == "Secure Area"
    assert "You logged into a secure area!" in secure_page.get_flash_message().strip()
    assert secure_page.is_logout_displayed()

    # --- Logout (robust) ---
    logout_locator = (By.CSS_SELECTOR, "a.button.secondary.radius")
    logout_el = wait.until(EC.element_to_be_clickable(logout_locator))

    # Scroll into view (helps headless)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logout_el)

    # Normal click first, then JS-click fallback
    try:
        logout_el.click()
    except Exception:
        driver.execute_script("arguments[0].click();", logout_el)

    # Strong signal: secure page is gone (navigation happened)
    try:
        wait.until(EC.staleness_of(secure_h2))
    except Exception:
        # If staleness didn't trigger, still continue with strong login waits below
        pass

    # Now wait for login state (prefer element-based over URL-based)
    wait.until(
        lambda d: ("/login" in d.current_url)
        or (
            len(d.find_elements(*LoginPage.USERNAME)) > 0
            and d.find_element(*LoginPage.USERNAME).is_displayed()
        )
    )

    assert "/login" in driver.current_url or driver.find_element(*LoginPage.USERNAME).is_displayed()

    # Login page assertions after logout
    login_heading = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2"))).text.strip()
    assert login_heading == "Login Page"

    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text.strip()
    assert "You logged out of the secure area!" in flash