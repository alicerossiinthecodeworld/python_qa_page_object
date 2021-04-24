from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ComparisonPage:

    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, "#content") \
            .find_element(By.CSS_SELECTOR, "input[value='Add to Cart']").click()

    def verify_product_link(self, product_name):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
