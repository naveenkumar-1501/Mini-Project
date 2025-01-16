"""
test_login_logout.py

Testing the GUVI application using valid credentialing login or not and once login logout or not.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject.common import Config
from MiniProject.GuviAutomation.home_page import HomePage
from MiniProject.GuviAutomation.login_page import LoginPage
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

@pytest.mark.parametrize("email, password", [("naveenkumar15012001@gmail.com", "Naveenkumar@$15")])
def test_login_logout(driver, email, password):
    """Test to verify the login and logout functionality."""
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    # Open the home page and verify login button visibility
    home_page.open_url(Config.url)
    assert home_page.is_login_button_visible(), f"Login button is not visible on {Config.url}"
    home_page.click_login_button()
    # Perform login action
    login_page.login(email, password)
    try:
        # Wait until the dropdown button is clickable
        dropdown_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, Config.DROPDOWN_BUTTON)))
        print("Dropdown button text:", dropdown_button.text)
        print("Dropdown button enabled:", dropdown_button.is_enabled())
        #click on the dropdown button
        login_page.click_element(dropdown_button)
        # Wait for the signout button to be clickable and click it
        signout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Config.SIGNOUT_BUTTON)))
        login_page.click_element(signout_button)
        # Assert that login button is visible after logout
        assert home_page.is_login_button_visible(), "Logout failed; login button not visible after logout."
    except TimeoutException as error:
        pytest.fail(f"Login failed: {error}.")
    except ElementClickInterceptedException as error:
        pytest.fail(f"Element click intercepted:{error}")

