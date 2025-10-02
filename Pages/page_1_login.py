import allure
from Base.Base_page import BasePage
from Config.Links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    page_url = Links.host

    ERROR_LOCATOR = (By.XPATH, '//div/h3[@data-test="error"]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="user-name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@name="login-button"]')

    @allure.step('Enter login')
    def enter_login(self, login):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_INPUT)).send_keys(login)

    @allure.step('Enter password')
    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)

    @allure.step('Click submit button')
    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step('Check the error text')
    def get_error_message_text(self):
        try:
            Error = self.wait.until(EC.visibility_of_element_located(self.ERROR_LOCATOR))
            return Error.text
        except:
            return None