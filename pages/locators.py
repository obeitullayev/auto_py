from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON=(By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK= (By.XPATH, "//span[contains(@class, 'btn-group')]//a[contains(@href, 'basket/')]")

class LoginPageLocators():
    LOGIN_FORM= (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD=(By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD=(By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_APROOVE_FIELD=(By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_BUTTON=(By.CSS_SELECTOR, "#register_form > button")
    REGISTER_FORM_ALERT=(By.CSS_SELECTOR, ".register_form .alert-danger")

class ProductPageLocators():
    ADD_TO_CART_BUTTON= (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME_IN_PRODUCT_PAGE=(By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME_IN_HINT = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner>strong")
    PRODUCT_PRICE_IN_PRODUCT_PAGE=(By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_IN_HINT=(By.CSS_SELECTOR, "#messages  .alertinner :nth-child(1) strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner>strong")

class BasketPageLocators():
    PRODUCTS_IN_BASKET=(By.CSS_SELECTOR, '.basket_summary .basket-items')
    HINT_IN_EMPTY_BASKET=(By.CSS_SELECTOR, "//div[@id='messages']//p[contains(text(), 'Your basket is now empty')]")

