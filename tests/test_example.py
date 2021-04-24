import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_wish_list(browser):
    # Клик по первому товару и сохранение имени
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-layout")[0]
    product_name = feature_product.find_element_by_css_selector(".caption h4 a").text
    feature_product.click()
    # Добавление товара в вишлист пользователя
    browser.find_element_by_css_selector("[data-original-title='Add to Wish List']").click()
    # Переход по ссылке в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text('login').click()
    # Авторизация пользователем
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("input[value=Login]").click()
    browser.find_element_by_link_text('Wish List').click()
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


def test_add_to_cart(browser):
    # Клик по первому товару и сохранение имени
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-layout")[1]
    product_name = feature_product.find_element_by_css_selector(".caption h4 a").text
    feature_product.click()
    # Добавление товара в корзину пользователя
    time.sleep(1) # Page loading problem
    browser.find_element_by_css_selector("#button-cart").click()
    # Переход по ссылке в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_css_selector(".buttons").find_element_by_link_text("Checkout").click()
    # Авторизация пользователем
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("input[value=Login]").click()
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))


def test_add_to_cart_from_comparison(browser):
    # Клик по первому товару и сохранение имени
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-layout")[0]
    product_name = feature_product.find_element_by_css_selector(".caption h4 a").text
    feature_product.click()
    # Добавление товара в список сравнения пользователя
    browser.find_element_by_css_selector("[data-original-title='Compare this Product']").click()
    # Переход по ссылке в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("product comparison").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Добавление товара в корзину со страницы сравнения
    browser.find_element_by_css_selector("#content").find_element_by_css_selector("input[value='Add to Cart']").click()
    # Переход по ссылке в алерте
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Клик по кнопке checkout
    browser.find_element_by_css_selector(".buttons").find_element_by_link_text("Checkout").click()
    # Авторизация пользователем
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("input[value=Login]").click()
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))
