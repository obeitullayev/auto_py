from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_button.click()

    def should_be_equal_product_title_(self):
        product_title_page= self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_PAGE)
        product_title_hint  = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_HINT)
        assert product_title_page.text != product_title_hint.text, "product not in cart"

    def should_be_equal_price_product(self):
        product_price_page= self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_PRODUCT_PAGE)
        product_price_hint  = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_HINT)
        assert product_price_page.text == product_price_hint.text, "price not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
