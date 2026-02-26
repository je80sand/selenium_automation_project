from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- Navigation ----------
    def load(self):
        self.driver.get(self.URL)
        # Wait until the username field is visible (page is ready)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        return self

    # ---------- Actions ----------
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

        user_el.clear()
        user_el.send_keys(username)

        pass_el.clear()
        pass_el.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

        # Wait for either success redirect OR flash message to appear.
        self.wait.until(lambda d: "/secure" in d.current_url or d.find_elements(*self.FLASH))

        if "/secure" in self.driver.current_url:
            # Local import to avoid circular import
            from src.pages.secure_page import SecurePage
            return SecurePage(self.driver)

        return self

    # ---------- Reads ----------
    def get_flash_message(self) -> str:
        flash = self.wait.until(EC.visibility_of_element_located(self.FLASH))
        return flash.text.strip()