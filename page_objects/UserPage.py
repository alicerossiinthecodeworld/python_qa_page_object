from selenium.webdriver.common.by import By


class UserPage:

    def __init__(self, browser):
        self.browser = browser

    def login_with(self, username, password):
        self.browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(username)
        self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "input[value=Login]").click()

    def click_link(self, link_text):
        self.browser.find_element(By.LINK_TEXT, link_text).click()
