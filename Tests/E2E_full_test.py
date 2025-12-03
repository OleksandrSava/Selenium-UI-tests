import allure
import pytest
from Base.Base_test import BaseTest

@allure.feature('E2E test for purchase')
class TestFullPurchase(BaseTest):

    @allure.title("Purchase")
    @allure.severity("Blocker")
    def test_purchase(self, prepare_checkout):
        info = ('Name', 'LastName', '30-500')

        self.checkout_step_1_page.fill_checkout_form(*info)
        self.checkout_step_1_page.click_continue()

        self.checkout_step_2_page.open_check()
        self.checkout_step_2_page.click_finish_button()

        self.checkout_step_complete_page.open_check()
        self.checkout_step_complete_page.click_back_button()

        self.products_page.open_check()
