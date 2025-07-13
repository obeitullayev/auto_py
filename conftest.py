import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    language= request.config.getoption("language")
    options = Options()
    options.add_argument('headless')
    options.add_argument('window-size=1920x935')
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print("start")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def main_page(browser ):
    url = "http://selenium1py.pythonanywhere.com/"
    return MainPage(browser, url)

@pytest.fixture
def product_page(browser):
    url= 'http://selenium1py.pythonanywhere.com/catalogue'
    return ProductPage(browser, url)

@pytest.fixture
def login_page(browser):
    url= 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login'
    return LoginPage(browser, url)

@pytest.fixture
def basket_page(browser):
    url= 'https://selenium1py.pythonanywhere.com/en-gb/basket/'
    return BasketPage(browser, url)
