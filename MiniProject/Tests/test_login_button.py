"""
test_login_button.py

Testing in GUVI web application login button is visible and clickable or not
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

def test_login_button_visible(home_page):
    """Test to verify the visibility of the login button on the homepage."""
    print("Checking if the login button is visible on the homepage.")
    assert home_page.is_login_button_visible(), "Login button is not visible on the homepage."

def test_login_button_clickable(home_page):
    """Test to verify if the login button is clickable."""
    print("Checking if the login button is clickable.")
    assert home_page.is_login_button_visible(), "Login button is not visible on the homepage."
    home_page.click_login_button()

