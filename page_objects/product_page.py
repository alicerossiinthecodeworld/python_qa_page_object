from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import logging

from page_objects.elements.product_locators import ProductLocators
from page_objects.admin_page import AdminPage


class ProductPage(AdminPage):

    def __init__(self, browser):
        self.browser, self.url = browser
        self.driver = self.browser
        self._config_logger()
        self.browser.get(self.url + '/admin')
        AdminPage(browser).login_to_admin()
        self.go_to_product_page()

    def input_product_name_field(self, product_name):
        self._send_keys(ProductLocators.PRODUCT_NAME_FIELD, product_name)

    def input_meta_title(self, meta_title):
        self._send_keys(ProductLocators.PRODUCT_META_TITLE, meta_title)

    def input_model(self, model):
        self._send_keys(ProductLocators.PRODUCT_MODEL, model)

    def open_data_section(self):
        self._click(ProductLocators.PRODUCT_DATA_BUTTON)

    def go_to_product_page(self):
        self._click(ProductLocators.CATALOG_MENU)
        self._click(ProductLocators.PRODUCT_BUTTON)

    def go_to_add_new_product_form(self):
        self._click(ProductLocators.ADD_NEW)
        self._verify_element_presence(ProductLocators.PRODUCT_NAME_FIELD)

    def save(self):
        self._click(ProductLocators.SAVE)

    def delete_element(self, locator):
        self._click(locator)
        self._click(ProductLocators.DELETE)
        self.confirm_alert()
