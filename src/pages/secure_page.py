from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecurePage:
    """
    Page Object for:
    https://the-internet.herokuapp.com/secure
    """

    URL_PART = "/secure"

    # -------- Locators --------
    HEADING = (By.CSS_SELECTOR, "h2")
    FLASH = (By.ID, "flash")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # -------- Verifications --------
    def wait_for_page_to_load(self) -> None:
        self.wait.until(EC.url_contains(self.URL_PART))
        self.wait.until(EC.visibility_of_element_located(self.FLASH))
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN))

    def get_header_text(self) -> str:
        header = self.wait.until(EC.visibility_of_element_located(self.HEADING))
        return header.text.strip()

    def get_flash_message(self) -> str:
        flash = self.wait.until(EC.visibility_of_element_located(self.FLASH))
        return flash.text.strip()

    def is_logout_displayed(self) -> bool:
        logout = self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BTN))
        return logout.is_displayed()

    # -------- Actions --------
    def logout(self):
        logout_btn = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN))
        logout_btn.click()

        # After logout we are back on LoginPage
        from src.pages.login_page import LoginPage

        return LoginPage(self.driver)