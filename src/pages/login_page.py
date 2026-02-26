from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object for:
    https://the-internet.herokuapp.com/login
    """

    URL = "https://the-internet.herokuapp.com/login"

    # -------- Locators --------
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")
    HEADING = (By.CSS_SELECTOR, "h2")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # -------- Navigation --------
    def load(self) -> "LoginPage":
        self.driver.get(self.URL)
        # Page is "ready" when username field is visible
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        return self

    # -------- Actions --------
    def login(self, username: str, password: str):
        """
        Enters credentials and clicks login.

        Waits for either:
        - redirect to /secure (success)
        - flash message on /login (failure)

        Returns:
        - SecurePage on success
        - LoginPage (self) on failure
        """
        user_el = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        pass_el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        btn_el = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN))

        user_el.clear()
        user_el.send_keys(username)

        pass_el.clear()
        pass_el.send_keys(password)

        btn_el.click()

        # Wait for either success redirect OR flash message to appear
        self.wait.until(lambda d: "/secure" in d.current_url or d.find_elements(*self.FLASH))

        if "/secure" in self.driver.current_url:
            # Local import avoids circular import at module import time
            from src.pages.secure_page import SecurePage

            return SecurePage(self.driver)

        return self

    # -------- Reads --------
    def get_heading_text(self) -> str:
        heading = self.wait.until(EC.visibility_of_element_located(self.HEADING))
        return heading.text.strip()

    def get_flash_message(self) -> str:
        flash = self.wait.until(EC.visibility_of_element_located(self.FLASH))
        return flash.text.strip()

    def is_flash_visible(self) -> bool:
        try:
            el = self.driver.find_element(*self.FLASH)
            return el.is_displayed()
        except Exception:
            return False
