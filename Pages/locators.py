from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, '#messages')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:first-of-type  strong')
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info  strong')
