from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class UserLoginForm(BasePage):
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")

    def login_with(self, username, password):
        self.browser.find_element(*self.INPUT_EMAIL).send_keys(username)
        self.browser.find_element(*self.INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()
