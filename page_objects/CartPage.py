from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, browser):
        self.browser = browser

    def go_to_checkout(self):
        self.browser.find_element(By.CSS_SELECTOR, ".buttons") \
            .find_element(By.LINK_TEXT, "Checkout").click()

    def verify_product(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
