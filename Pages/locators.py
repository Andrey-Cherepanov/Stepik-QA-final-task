from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL_INPUT = (By.ID, 'id_registration-email')
    REGISTRATION_EMAIL_PASSWORD1_INPUT = (By.ID, 'id_registration-password1')
    REGISTRATION_EMAIL_PASSWORD2_INPUT = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, '#messages')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:first-of-type  strong')
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info  strong')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_EMPTY_TEXT_LINK = (By.CSS_SELECTOR, '#content_inner p a')
