import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config.Data import Data


@pytest.fixture(scope="function", autouse=True)
def driver(request):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    yield driver

    driver.quit()


@pytest.fixture
def prepare_login(request):

    prepare_login = request.cls

    prepare_login.login_page.open()
    prepare_login.login_page.open_check()

    prepare_login.login_page.enter_login(Data.LOGIN)
    prepare_login.login_page.enter_password(Data.PASSWORD)
    prepare_login.login_page.click_submit()

    prepare_login.products_page.open_check()

    return prepare_login


@pytest.fixture
def prepare_checkout(prepare_login):

    prepare_checkout = prepare_login

    prepare_checkout.products_page.open_check()
    prepare_checkout.products_page.add_to_cart()
    prepare_checkout.products_page.click_cart()

    prepare_checkout.cart_page.open_check()
    prepare_checkout.cart_page.click_checkout()

    prepare_checkout.checkout_step_1_page.open_check()

    return prepare_checkout
