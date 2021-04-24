from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserPage:

    def __init__(self, browser):
        self.browser = browser

    def login_with(self, username, password):
        self.browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(username)
        self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "input[value=Login]").click()

    def click_link(self, link_text):
        self.browser.find_element(By.LINK_TEXT, link_text).click()

    def verify_pay_form(self):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))

    def verify_product_link(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
