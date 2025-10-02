import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Base.Base_page import BasePage
from Config.Links import Links

class CheckoutStepTwoPage(BasePage):

    page_url = Links.checkout_2nd

    FINISH_BUTTON = (By.XPATH, '//div/button[@id="finish"]')

    @allure.step('Click on finish button')
    def click_finish_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
