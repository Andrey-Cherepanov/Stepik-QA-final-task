from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()
        self.solve_quiz_and_get_code()

    def should_be_success_messages(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), 'Success messages is not present'

    def should_be_product_name_in_alert_success(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        messege_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == messege_product_name, f'Product name in message should be {product_name} not {messege_product_name}'

    def should_be_product_price_in_basket_info(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE).text
        assert product_price == message_basket_price, f'Basket price should be {product_price} not {message_basket_price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
        "Success message is presented, but should not be"

    def should_disapeare_success_massege(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
        'Success message is not disappered, but should be'
