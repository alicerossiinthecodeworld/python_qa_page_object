import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_wish_list(browser):
    # Клик по первому товару и сохранение имени
    feature_product = browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-layout")[0]
    product_name = feature_product.find_element(By.CSS_SELECTOR, ".caption h4 a").text
    feature_product.click()
    # Добавление товара в вишлист пользователя
    browser.find_element(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']").click()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, 'login').click()
    # Авторизация пользователем
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("test2@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("test")
    browser.find_element(By.CSS_SELECTOR, "input[value=Login]").click()
    # Перейти в вишлист раздел пользователя
    browser.find_element(By.LINK_TEXT, 'Wish List').click()
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


def test_add_to_cart(browser):
    # Клик по первому товару и сохранение имени
    feature_product = browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-layout")[1]
    product_name = feature_product.find_element(By.CSS_SELECTOR, ".caption h4 a").text
    feature_product.click()
    # Добавление товара в корзину пользователя
    time.sleep(1)  # Page loading problem
    browser.find_element(By.CSS_SELECTOR, "#button-cart").click()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "shopping cart").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element(By.CSS_SELECTOR, ".buttons").find_element(By.LINK_TEXT, "Checkout").click()
    # Авторизация пользователем
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("test2@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("test")
    browser.find_element(By.CSS_SELECTOR, "input[value=Login]").click()
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))


def test_add_to_cart_from_comparison(browser):
    # Клик по первому товару и сохранение имени
    feature_product = browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-layout")[0]
    product_name = feature_product.find_element(By.CSS_SELECTOR, ".caption h4 a").text
    feature_product.click()
    # Добавление товара в список сравнения пользователя
    browser.find_element(By.CSS_SELECTOR, "[data-original-title='Compare this Product']").click()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "product comparison").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Добавление товара в корзину со страницы сравнения
    browser.find_element(By.CSS_SELECTOR, "#content").find_element(By.CSS_SELECTOR,
                                                                   "input[value='Add to Cart']").click()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "shopping cart").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # Клик по кнопке checkout
    browser.find_element(By.CSS_SELECTOR, ".buttons").find_element(By.LINK_TEXT, "Checkout").click()
    # Авторизация пользователем
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("test2@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("test")
    browser.find_element(By.CSS_SELECTOR, "input[value=Login]").click()
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))
