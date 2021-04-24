import time

from selenium.webdriver.common.by import By


class ProductPage:
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    ADD_TO_COMPARISON = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")

    def __init__(self, browser):
        self.browser = browser

    def add_to_wish_list(self):
        self.browser.find_element(*self.WISH_LIST_BUTTON).click()

    def add_to_cart(self):
        time.sleep(1)  # Page loading problem
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()

    def add_to_comparison(self):
        self.browser.find_element(*self.ADD_TO_COMPARISON).click()
