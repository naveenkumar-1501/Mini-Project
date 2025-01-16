"""
home_page.py

HomePage class represents the homepage of GUVI
"""
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject.GuviAutomation.base_page import BasePage
from MiniProject.common import Config

class HomePage(BasePage, Config):
    """HomePage class to interact with elements on the homepage."""
    def is_login_button_visible(self):
        """Check if the login button is visible on the homepage."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
            print("Login button is visible.")
            return True
        except Exception as error:
            logging.error(f"Login button is not visible: {error}")
            return False

    def is_signup_button_visible(self):
        """Check if the sign-up button is visible on the homepage."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.SIGNUP_BUTTON)))
            print("Signup button is visible.")
            return True
        except Exception as error:
            logging.error(f"Signing is not visible: {error}")
            return False

    def click_login_button(self):
        """Click the login button on the homepage."""
        try:
            login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON)))
            self.click_element(login_button)
        except Exception as error:
            logging.error(f"Failed to click login button: {error}")
            raise

    def click_signup_button(self):
        """Click the signup button on the homepage."""
        try:
            signup_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SIGNUP_BUTTON)))
            self.click_element(signup_button)
        except Exception as error:
            logging.error(f"Failed to click signup button: {error}")
            raise
