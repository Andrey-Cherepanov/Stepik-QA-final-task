from pages.product_page import ProductPage

LINK_PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_guest_can_add_product_to_basket(browser):
    link = LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_messages()
    page.should_be_product_name_in_alert_success()
    page.should_be_product_price_in_basket_info()
    
