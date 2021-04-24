from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    FEATURE_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    FEATURE_PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")

    def click_featured_product(self, number):
        index = number - 1
        feature_product = self.browser.find_elements(*self.FEATURE_PRODUCT)[index]
        product_name = feature_product.find_element(*self.FEATURE_PRODUCT_NAME).text
        feature_product.click()
        return product_name
