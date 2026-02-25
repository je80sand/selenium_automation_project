from src.pages.login_page import LoginPage


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wrong_user", "wrong_password")

    assert "login" in driver.current_url