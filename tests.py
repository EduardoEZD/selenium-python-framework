from pages.login_page import LoginPage
import time

def test_successful_login(setup):
    driver = setup
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login = LoginPage(driver)
    login.login("student", "Password123")

    time.sleep(2)
    assert "logged-in-successfully" in driver.current_url
