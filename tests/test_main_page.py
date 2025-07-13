import pytest
import allure

@allure.feature("Навигация")
@allure.story("Переход на страницу логина")
@allure.severity(allure.severity_level.NORMAL)
class TestLoginFromMainPage:

    @allure.title("Гость может перейти на страницу логина с главной")
    def test_guest_can_go_to_login_page(self, main_page, login_page):
        with allure.step("Открываем главную страницу"):
            main_page.open()
        with allure.step("Переходим на страницу логина"):
            main_page.go_to_login_page()
        with allure.step("Проверяем, что это страница логина"):
            login_page.should_be_login_page()

    @allure.title("Гость видит ссылку на логин на главной странице")
    def test_guest_should_see_login_link(self, main_page):
        with allure.step("Открываем главную страницу"):
            main_page.open()
        with allure.step("Проверяем наличие ссылки на логин"):
            main_page.should_be_login_link()


@allure.feature("Корзина")
@allure.story("Проверка пустой корзины")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Гость не видит товар в корзине при переходе с главной страницы")
@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(main_page, basket_page):
    with allure.step("Открываем главную страницу"):
        main_page.open()
    with allure.step("Переходим в корзину"):
        main_page.go_to_basket_page()
    with allure.step("Проверяем, что корзина пуста"):
        basket_page.check_basket_is_empty()
    with allure.step("Проверяем наличие сообщения о пустой корзине"):
        basket_page.presence_hint_in_empty_basket_located()
