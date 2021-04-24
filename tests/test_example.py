import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.MainPage import MainPage
from page_objects.UserPage import UserPage


def test_add_to_wish_list(browser):
    # Клик по первому товару и сохранение имени
    product_name = MainPage(browser).click_featured_product(1)
    # Добавление товара в вишлист пользователя
    browser.find_element(By.CSS_SELECTOR, "[data-original-title='Add to Wish List']").click()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, 'login').click()
    # Авторизация пользователем
    UserPage(browser).login_with("test2@mail.ru", "test")
    # Перейти в вишлист раздел пользователя
    browser.find_element(By.LINK_TEXT, 'Wish List').click()
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


def test_add_to_cart(browser):
    # Клик по первому товару и сохранение имени
    product_name = MainPage(browser).click_featured_product(1)
    # Добавление товара в корзину пользователя
    time.sleep(1)  # Page loading problem
    browser.find_element(By.CSS_SELECTOR, "#button-cart").click()
    # Переход по ссылке в алерте
    browser.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "shopping cart").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element(By.CSS_SELECTOR, ".buttons").find_element(By.LINK_TEXT, "Checkout").click()
    # Авторизация пользователем
    UserPage(browser).login_with("test2@mail.ru", "test")
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))


def test_add_to_cart_from_comparison(browser):
    # Клик по первому товару и сохранение имени
    product_name = MainPage(browser).click_featured_product(1)
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
    UserPage(browser).login_with("test2@mail.ru", "test")
    # Проверка наличия ссылки на продукт
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))
