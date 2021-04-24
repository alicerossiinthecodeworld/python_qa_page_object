from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class SuccessAlert(BasePage):
    SELF = (By.CSS_SELECTOR, ".alert-success")
    LOGIN = (By.LINK_TEXT, "login")
    SOPPING_CART = (By.LINK_TEXT, "shopping cart")
    PRODUCT_COMPARISON = (By.LINK_TEXT, "product comparison")

    @property
    def it(self):
        return self.browser.find_element(*self.SELF)

    def click_login(self):
        self.it.find_element(*self.LOGIN).click()

    def click_shopping_cart(self):
        self.it.find_element(*self.SOPPING_CART).click()

    def click_product_comparison(self):
        self.it.find_element(*self.PRODUCT_COMPARISON).click()
