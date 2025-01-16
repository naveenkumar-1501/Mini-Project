"""
common.py
common configuration for web application
"""
class Config:
    """Class to hold constants and configuration details."""
    url = "https://www.guvi.in"
    LOGIN_BUTTON = '//a[@id="login-btn"]'
    SIGNUP_BUTTON = "//a[text()='Sign up']"
    LOGIN_PAGE_TITLE = "GUVI | Learn to code in your native language"
    EMAIL_FIELD = '//input[@id= "email"]'
    PASSWORD_FIELD = '//input[@id= "password"]'
    SUBMIT_BUTTON = "//a[@class = 'btn login-btn']"
    ERROR_MESSAGE = "//div[@class='invalid-feedback']"
    DROPDOWN_BUTTON = "//div[@id='dropdown_title']"
    SIGNOUT_BUTTON = "//li[@id='dropdown_contents']//div[@id='dropdown_contents']"
    POPUP_CLOSE_BUTTON = "//button[text()='Later']"

