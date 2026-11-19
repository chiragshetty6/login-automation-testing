from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    # Check that the Products heading appears
    heading = driver.find_element(By.CLASS_NAME, "title").text
    assert heading == "Products"


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_username("wrong_user")
    login.enter_password("wrong_password")
    login.click_login()

    error = login.get_error_message()
    assert "Username and password do not match" in error
