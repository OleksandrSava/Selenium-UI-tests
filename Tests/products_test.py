import allure
import pytest
from Base.Base_test import BaseTest

@allure.feature('Sort functionality')
class TestProducts(BaseTest):

    @allure.title("Purchase")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_sort(self, prepare_login):

        self.products_page.open_check()

        sorted_AZ_names = self.products_page.return_all_product_names()

        self.products_page.click_dropdown_menu()
        self.products_page.click_option_za()

        expected_to_be_sorted_ZA = self.products_page.return_all_product_names()

        assert expected_to_be_sorted_ZA == sorted(sorted_AZ_names, reverse=True), "ZA sort doesn't work"

        self.products_page.click_dropdown_menu()
        self.products_page.click_option_hilo()

        all_prices_high_to_low = self.products_page.return_all_product_prices()

        for i in range(len(all_prices_high_to_low) - 1):
            assert all_prices_high_to_low[i] >= all_prices_high_to_low[i+1], "High to low sort doesn't work"
