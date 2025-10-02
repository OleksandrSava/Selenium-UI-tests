import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Base.Base_page import BasePage
from Config.Links import Links

class CheckoutCompletePage(BasePage):

    page_url = Links.checkout_complete

    BACK_BUTTON = (By.XPATH, '//div/button[@id="back-to-products"]')

    @allure.step('Click back button')
    def click_back_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BACK_BUTTON)).click()
