"""
test_navigation_signup.py

Testing using the GUVI web application navigation to signup button.
"""

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject.common import Config
from MiniProject.GuviAutomation.home_page import HomePage

def test_navigation_to_signup(driver):
    """Test to verify the navigation to the signup page."""
    home_page = HomePage(driver)
    home_page.open_url(Config.url)
    assert home_page.is_login_button_visible(), "Signin button is not visible on the homepage."
    home_page.click_login_button()
    WebDriverWait(driver, 10).until(EC.url_contains("sign-in"))
    current_url = driver.current_url
    expected_url = "https://www.guvi.in/sign-in/"
    assert current_url == expected_url, f"Excepted URL '{expected_url}', but got'{driver.current_url}'."
    page_title = driver.title
    expected_url = "GUVI | Login"
    assert page_title == expected_url, f"Excepted title '{expected_url}', but got'{page_title}'."

