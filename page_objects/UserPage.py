from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .elements.UserLoginForm import UserLoginForm
from .BasePage import BasePage


class UserPage(BasePage):
    PAYMENT_FORM = (By.CSS_SELECTOR, "#payment-new")

    def login_with(self, username, password):
        UserLoginForm(self.browser).login_with(username, password)

    def click_link(self, link_text):
        self.browser.find_element(By.LINK_TEXT, link_text).click()

    def verify_pay_form(self):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.PAYMENT_FORM))

    def verify_product_link(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
