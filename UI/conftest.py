import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from UI.pages.checkout_page import CheckoutPage
from UI.pages.inventory_page import InventoryPage
from UI.pages.login_page import LoginPage
from UI.pages.confirm_page import ConfirmPage
from UI.pages.success_page import SuccessPage

WEB_BASE_URL =  "https://www.saucedemo.com"


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # не открывать браузер
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(browser):
    return LoginPage(browser, WEB_BASE_URL)

@pytest.fixture
def inventory_page(browser):
    return InventoryPage(browser, WEB_BASE_URL)

@pytest.fixture
def checkout_page(browser):
    return CheckoutPage(browser, WEB_BASE_URL)

@pytest.fixture
def confirm_page(browser):
    return ConfirmPage(browser, WEB_BASE_URL)

@pytest.fixture
def success_page(browser):
    return SuccessPage(browser, WEB_BASE_URL)