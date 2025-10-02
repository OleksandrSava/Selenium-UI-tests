import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Base.Base_page import BasePage
from Config.Links import Links


class CardPage(BasePage):

    page_url = Links.cart

    REMOVE_BUTTON = (By.XPATH, f'(//div//button[@class="btn btn_secondary btn_small cart_button"])[2]')
    CHECKOUT_BUTTON = (By.XPATH, '//div//button[@id="checkout"]')

    @allure.step('Removing product from cart')
    def remove_product(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BUTTON)).click()

    @allure.step('Click checkout button')
    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()






