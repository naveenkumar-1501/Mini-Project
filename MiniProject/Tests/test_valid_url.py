"""
test_valid_url.py

Testing the GUVI web application the url is valid or not and testing invalid title.
"""

import pytest
from MiniProject.conftest import driver
from MiniProject.common import Config

pytest.fixture(scope="function")
def test_valid_url(driver):
    """Fixture to test valid URL."""
    driver.get(Config.url)
    print(f"URL is valid: {Config.url}")

def test_invalid_url(driver):
    """Test for invalid URL."""
    test_url = "https://www.google.com"
    driver.get(test_url)
    assert driver.current_url != Config.url
    print(f"Invalid url: {test_url !=Config.url}")

