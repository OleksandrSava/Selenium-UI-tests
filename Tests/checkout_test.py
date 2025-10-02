import allure
import pytest
from Base.Base_test import BaseTest
from Tests.conftest import prepare_checkout


@allure.feature("Tests for checkout")
class TestCheckout(BaseTest):

    @allure.severity("Critical")
    @pytest.mark.smoke
    @pytest.mark.parametrize(

        'name, lastname, post_code, status',
    [
        ('', '', '', False),
        ('name', '', '', False),
        ('', 'lastname', '', False),
        ('', '', '31-000', False),
        ('name', 'lastname', '31-000', True),
    ],
        ids=[f"Checkout test {i + 1}" for i in range(5)]
    )
    def test_checkout(self,prepare_checkout, name, lastname, post_code, status):

        self.checkout_step_1_page.fill_checkout_form(name, lastname, post_code)
        self.checkout_step_1_page.click_continue()

        if status:
            self.checkout_step_2_page.open_check()
        else:
            error = self.checkout_step_1_page.get_error_box_text()
            assert error is not None, "Expected error message, but none was displayed"
            allure.attach(error, "Error message")