"""
test_invalid_login.py

Testing the GUVI web application using the invalid credential.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject.common import Config
from MiniProject.GuviAutomation.home_page import HomePage
from MiniProject.GuviAutomation.login_page import LoginPage

def test_invalid_login(driver):
    """Test invalid login scenario."""
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    home_page.open_url(Config.url)
    assert home_page.is_login_button_visible(), "Login button is not visible on the homepage."
    home_page.click_login_button()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Config.EMAIL_FIELD)))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Config.PASSWORD_FIELD)))
    invalid_email = "naveen@gmail.com"
    invalid_password = "Guvi123"
    login_page.find_element((By.XPATH, Config.EMAIL_FIELD)).send_keys(invalid_email)
    login_page.find_element((By.XPATH, Config.PASSWORD_FIELD)).send_keys(invalid_password)
    print(f"Trying to login with email: {invalid_email} and password: {invalid_password}")
    login_page.click_element(login_page.find_element((By.XPATH, Config.SUBMIT_BUTTON)))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Config.ERROR_MESSAGE)))
    error_message = login_page.get_error_message()
    expected_error_message = "Incorrect Email or Password"
    assert error_message == expected_error_message, f"Expected error message '{expected_error_message}', but got '{error_message}'."

