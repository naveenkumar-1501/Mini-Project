"""
login_page.py

The LoginPage class handles interactions on the login page.
"""
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MiniProject.GuviAutomation.base_page import BasePage
from MiniProject.common import Config

class LoginPage(BasePage):
    """LoginPage class for login-related actions."""
    def login(self, email, password):
        """Login to the application using provided credentials."""
        try:
            email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Config.EMAIL_FIELD)))
            password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Config.PASSWORD_FIELD)))
            email_field.send_keys(email)
            password_field.send_keys(password)
            print(f"Entered email: {email} and password: {password}")
            submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Config.SUBMIT_BUTTON)))
            self.click_element(submit_button)
            logging.info(f"Login attempt with email:{email}")
        except Exception as error:
            logging.error(f"Login failed with error:{error}")
            raise

    def get_error_message(self):
        """Fetch the error message if login fails."""
        try:
            error_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Config.ERROR_MESSAGE)))
            print(f"Error message: {error_element.text}")
            return error_element.text
        except Exception as error:
            logging.error(f"Error while fetching error message:{error}")
            return None
