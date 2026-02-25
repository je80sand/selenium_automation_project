from src.pages.login_page import LoginPage
from src.pages.secure_page import SecurePage
from selenium.webdriver.common.by import By


def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")

    secure_page = SecurePage(driver)

    # Click logout button
    driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

    assert "login" in driver.current_url