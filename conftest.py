import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Start Chrome before each test
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # Close Chrome after each test
    driver.quit()
