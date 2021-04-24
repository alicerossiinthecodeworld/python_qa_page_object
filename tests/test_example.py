import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.MainPage import MainPage
from page_objects.UserPage import UserPage
from page_objects.ProductPage import ProductPage
from page_objects.ComparisonPage import ComparisonPage
from page_objects.CartPage import CartPage


def test_add_to_wish_list(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_wish_list()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, 'login').click()
    UserPage(browser).login_with("test2@mail.ru", "test")
    UserPage(browser).click_link('Wish List')
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


def test_add_to_cart(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "shopping cart").click()
    CartPage(browser).verify_product(product_name)
    CartPage(browser).go_to_checkout()
    UserPage(browser).login_with("test2@mail.ru", "test")
    # Проверка наличия формы оплаты
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))


def test_add_to_cart_from_comparison(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_comparison()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "product comparison").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    ComparisonPage(browser).add_to_cart()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "shopping cart").click()
    CartPage(browser).verify_product(product_name)
    CartPage(browser).go_to_checkout()
    UserPage(browser).login_with("test2@mail.ru", "test")
    # Проверка наличия формы оплаты
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))
