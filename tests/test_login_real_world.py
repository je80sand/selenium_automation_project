from src.pages.login_page import LoginPage
from src.pages.secure_page import SecurePage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    secure_page = SecurePage(driver)

    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert secure_page.is_logged_in()