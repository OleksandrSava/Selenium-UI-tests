import allure
import pytest
from Config.Data import Data
from Base.Base_test import BaseTest


@allure.feature("Tests for login")
class TestLogin(BaseTest):

    @allure.severity("Blocker")
    @pytest.mark.smoke
    @pytest.mark.parametrize(

        'login, password, status',
    [
        (Data.LOGIN, 'Wrong password', False),
        ('Wrong login', Data.PASSWORD, False),
        ('', '', False),
        (Data.LOGIN, Data.PASSWORD, True),
    ],

        ids = [f"Login test {i + 1}" for i in range(4)]
    )
    def test_login(self, login, password, status):
        self.login_page.open()
        self.login_page.open_check()

        self.login_page.enter_login(login)
        self.login_page.enter_password(password)

        self.login_page.click_submit()

        if status:
            self.products_page.open_check()
        else:
            error = self.login_page.get_error_message_text()
            assert error is not None, "Expected error message, but none was displayed"
            allure.attach(error, "Error message")



