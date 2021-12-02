from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        'Basket is not empty, but should be'

    def should_be_empty_basket_text(self, language):

        languages_empty_basket = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
        "en-US": "Your basket is empty."
        }

        empty_basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        empty_basket_text_link = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT_LINK).text
        empty_basket_text = empty_basket_text.strip(f' {empty_basket_text_link}')
        assert empty_basket_text == languages_empty_basket[language], \
        f'Text in page should be {languages_empty_basket[language]}, not {empty_basket_text}'
