import pytest
from Config.Data import Data
from Pages.page_1_login import LoginPage
from Pages.page_2_products import ProductsPage
from Pages.page_3_cart import CardPage
from Pages.page_4_checkout_step_one import CheckoutStepOnePage
from Pages.page_5_checkout_step_two import CheckoutStepTwoPage
from Pages.page_6_checkout_step_complete import CheckoutCompletePage

class BaseTest:

    data: Data

    login_page: LoginPage
    products_page: ProductsPage
    cart_page: CardPage
    checkout_step_1_page: CheckoutStepOnePage
    checkout_step_2_page: CheckoutStepTwoPage
    checkout_step_complete_page: CheckoutCompletePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.products_page = ProductsPage(driver)
        request.cls.cart_page = CardPage(driver)
        request.cls.checkout_step_1_page = CheckoutStepOnePage(driver)
        request.cls.checkout_step_2_page = CheckoutStepTwoPage(driver)
        request.cls.checkout_step_complete_page = CheckoutCompletePage(driver)
