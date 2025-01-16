"""
test_page_title.py

Testing the GUVI web application the title is valid or not and testing the invalid title.
"""

import pytest
from MiniProject.conftest import driver
from MiniProject.common import Config

pytest.fixture(scope="function")
def test_valid_page_title(driver):
    driver.get(Config.url)
    print(f"Page title: {Config.LOGIN_PAGE_TITLE}")

def test_invalid_page_title(driver):
    url = "https://www.google.com"
    driver.get(url)
    assert driver.title != Config.LOGIN_PAGE_TITLE
    print(f"Invalid page title: {driver.title != Config.url}")

