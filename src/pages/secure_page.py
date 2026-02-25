from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecurePage:

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.flash.success")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def is_logged_in(self) -> bool:
        """Return True if login succeeded and secure page is visible."""
        wait = WebDriverWait(self.driver, self.timeout)

        # Wait for success flash message
        wait.until(
            EC.presence_of_element_located(self.SUCCESS_MESSAGE)
        )

        return "/secure" in self.driver.current_url