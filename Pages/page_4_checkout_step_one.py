import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Base.Base_page import BasePage
from Config.Links import Links

class CheckoutStepOnePage(BasePage):

    page_url = Links.checkout_1th

    FIRST_INPUT_FIELD = (By.XPATH, '//div/input[@id="first-name"]')
    SECOND_INPUT_FIELD = (By.XPATH, '//div/input[@id="last-name"]')
    POST_INPUT_FIELD = (By.XPATH, '//div/input[@id="postal-code"]')
    ERROR_BOX = (By.XPATH, '//div/h3[@data-test="error"]')
    CONTINUE_BUTTON = (By.XPATH, '//div/input[@id="continue"]')

    @allure.step('Fill the form')
    def fill_checkout_form(self, first_name, last_name, postal_code):
        fields = [
            (self.FIRST_INPUT_FIELD, first_name),
            (self.SECOND_INPUT_FIELD, last_name),
            (self.POST_INPUT_FIELD, postal_code)
        ]
        for locator, value in fields:
            self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    @allure.step('Check error box text')
    def get_error_box_text(self):
        try:
            Error = self.wait.until(EC.visibility_of_element_located(self.ERROR_BOX))
            return Error.text
        except:
            return None


    @allure.step('Click continue button')
    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()



