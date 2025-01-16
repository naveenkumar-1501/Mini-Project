"""
base_page.py

BasePage class includes common methods like find_element, click, send_keys
"""
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for all pages to share common functions."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait for elements for up to 10 seconds

    def open_url(self, url):
        """Open the URL in the browser."""
        print(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self, by):
        """Find an element on the page."""
        try:
            return self.wait.until(EC.presence_of_element_located((by)))
        except Exception as error:
            logging.error(f"Element not found: {by}, Error: {error}")
            return None

    def click_element(self, element):
        """Click on a given element."""
        try:
            element.click()
            logging.info(f"Clicked on element: {element}")
        except Exception as error:
            logging.error(f"Error while clicking element: {error}")






