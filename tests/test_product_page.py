import pytest
import allure
import time

@allure.feature("Добавление товара в корзину")
@allure.story("Гость может добавить товар с промо-акцией")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
@allure.title("Гость может добавить товар в корзину с промо: {link}")
def test_guest_can_add_product_to_basket(link, product_page):
    product_page.url = link
    with allure.step("Открываем страницу товара"):
        product_page.open()
    with allure.step("Добавляем товар в корзину"):
        product_page.add_product_to_cart()
    with allure.step("Проходим квиз и получаем код"):
        product_page.solve_quiz_and_get_code()
    with allure.step("Проверяем название товара"):
        product_page.should_be_equal_product_title_()
    with allure.step("Проверяем цену товара"):
        product_page.should_be_equal_price_product()


@allure.feature("Добавление товара")
@allure.story("Промо новая акция")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Гость может добавить товар с промо 'newYear2019'")
def test_add_product_to_basket(product_page):
    product_page.url = f"{product_page.url}/coders-at-work_207/?promo=newYear2019"
    with allure.step("Открываем страницу товара"):
        product_page.open()
    with allure.step("Добавляем товар в корзину"):
        product_page.add_product_to_cart()
    with allure.step("Проходим квиз и получаем код"):
        product_page.solve_quiz_and_get_code()
    with allure.step("Проверяем название товара"):
        product_page.should_be_equal_product_title_()
    with allure.step("Проверяем цену товара"):
        product_page.should_be_equal_price_product()


@allure.feature("Уведомления")
@allure.story("Проверка отсутствия сообщения об успехе")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Гость не видит сообщение об успехе после добавления товара")
@pytest.mark.skip(reason="fixing bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(product_page):
    with allure.step("Открываем страницу товара"):
        product_page.url = f"{product_page.url}/coders-at-work_207"
        product_page.open()
    with allure.step("Добавляем товар в корзину"):
        product_page.add_product_to_cart()
    with allure.step("Проверяем отсутствие сообщения об успехе"):
        product_page.should_not_be_success_message()


@allure.feature("Уведомления")
@allure.story("Проверка исчезновения сообщения")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Сообщение об успехе исчезает после добавления товара")
@pytest.mark.skip(reason="no way of currently testing this")
def test_message_disappeared_after_adding_product_to_basket(product_page):
    with allure.step("Открываем страницу товара"):
        product_page.url = f"{product_page.url}/coders-at-work_207"
        product_page.open()
    with allure.step("Добавляем товар в корзину"):
        product_page.add_product_to_cart()
    with allure.step("Проверяем исчезновение сообщения"):
        product_page.success_message_should_disappear()


@allure.feature("Навигация")
@allure.story("Отображение ссылки на логин")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Гость должен видеть ссылку на логин на странице товара")
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(product_page):
    with allure.step("Открываем страницу товара"):
        product_page.url = f"{product_page.url}/the-city-and-the-stars_95/"
        product_page.open()
    with allure.step("Проверяем наличие ссылки на логин"):
        product_page.should_be_login_link()


@allure.feature("Навигация")
@allure.story("Переход на страницу логина")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Гость может перейти на страницу логина со страницы товара")
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(product_page, login_page):
    with allure.step("Открываем страницу товара"):
        product_page.url = f"{product_page.url}/the-city-and-the-stars_95/"
        product_page.open()
    with allure.step("Переходим на страницу логина"):
        product_page.go_to_login_page()
    with allure.step("Проверяем, что это страница логина"):
        login_page.should_be_login_page()


@allure.feature("Корзина")
@allure.story("Пустая корзина при переходе со страницы товара")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Гость не видит товар в корзине при переходе со страницы товара")
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(main_page, basket_page):
    with allure.step("Открываем страницу товара"):
        main_page.url = f"{main_page.url}catalogue/the-city-and-the-stars_95"
        main_page.open()
    with allure.step("Переходим в корзину"):
        main_page.go_to_basket_page()
    with allure.step("Проверяем, что корзина пуста"):
        basket_page.check_basket_is_empty()
    with allure.step("Проверяем наличие сообщения о пустой корзине"):
        basket_page.presence_hint_in_empty_basket_located()


@allure.feature("Авторизация пользователя")
@allure.story("Добавление товара в корзину авторизованным пользователем")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Авторизация с недействительными учетными данными")
@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, login_page):
        with allure.step("Регистрация нового пользователя"):
            login_page.open()
            login_page.register_new_user(email=str(time.time()) + "@fakemail.org", password='str(time.time())' + '12')
            login_page.should_not_be_alert_register_form()
            login_page.go_to_basket_page()
            login_page.should_be_authorized_user()

    @allure.title("Авторизованный пользователь не видит сообщение об успехе после добавления товара")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, product_page):
        with allure.step("Открываем страницу товара"):
            product_page.url = f"{product_page.url}/coders-at-work_207"
            product_page.open()
        with allure.step("Проверяем отсутствие сообщения об успехе"):
            product_page.should_not_be_success_message()

    @allure.title("Авторизованный пользователь может добавить товар в корзину")
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, product_page):
        with allure.step("Открываем страницу товара"):
            product_page.url = f"{product_page.url}/coders-at-work_207"
            product_page.open()
        with allure.step("Добавляем товар в корзину"):
            product_page.add_product_to_cart()
        with allure.step("Проверяем название товара"):
            product_page.should_be_equal_product_title_()
        with allure.step("Проверяем цену товара"):
            product_page.should_be_equal_price_product()
