from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Basket is not empty"

    def presence_hint_in_empty_basket_located(self):
        assert self.browser.find_element(By.XPATH, "//div[@id='content_inner']/p"), \
            "Hint about empty basket is not located"