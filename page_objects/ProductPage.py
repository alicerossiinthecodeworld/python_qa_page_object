import time

from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, browser):
        self.browser = browser

    def add_to_wish_list(self):
        self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']").click()

    def add_to_cart(self):
        time.sleep(1)  # Page loading problem
        self.browser.find_element(By.CSS_SELECTOR, "#button-cart").click()

    def add_to_comparison(self):
        self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Compare this Product']").click()
