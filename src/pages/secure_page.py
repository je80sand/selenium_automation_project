from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecurePage:
    # Locators
    HEADER = (By.CSS_SELECTOR, "div.example h2")
    FLASH = (By.ID, "flash")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # When this page object is created, confirm we're actually on secure page
        self.wait.until(lambda d: "/secure" in d.current_url)

    # ---------- Reads ----------
    def get_header_text(self) -> str:
        header = self.wait.until(EC.visibility_of_element_located(self.HEADER))
        return header.text.strip()

    def get_flash_message(self) -> str:
        flash = self.wait.until(EC.visibility_of_element_located(self.FLASH))
        return flash.text.strip()

    def is_logout_displayed(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BTN)).is_displayed()

    # ---------- Actions ----------
    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()

        # Wait until we're back on /login
        self.wait.until(lambda d: "/login" in d.current_url)

        # Local import to avoid circular import
        from src.pages.login_page import LoginPage
        return LoginPage(self.driver)