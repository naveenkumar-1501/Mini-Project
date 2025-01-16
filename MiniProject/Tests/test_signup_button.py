"""
test_signup_button.py

Testing in GUVI web application signup button is visible and clickable or not
"""

import pytest
from MiniProject.common import Config
from MiniProject.GuviAutomation.home_page import HomePage

@pytest.fixture
def home_page(driver):
    """Fixture to open the homepage URL."""
    home_page=HomePage(driver)
    home_page.open_url(Config.url)
    return home_page

def test_signup_button_visible(home_page):
    """Test to verify the visibility of the signup button on the homepage."""
    print("Checking if the signup button is visible on the homepage.")
    assert home_page.is_signup_button_visible(), "Signup button is not visible on the homepage."

def test_signup_button_clickable(home_page):
    """Test to verify if the signup button is clickable."""
    print("Checking if the signup button is clickable.")
    assert home_page.is_signup_button_visible(), "Signup button is not visible on the homepage."
    home_page.click_signup_button()

