import allure
from Base.Base_page import BasePage
from Config.Links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):

    page_url = Links.inventory

    DROPDOWN = (By.XPATH, '//div//select')
    OPTION_ZA = (By.XPATH, '//div//select/option[@value="za"]')
    OPTION_HILO = (By.XPATH, '//div//select/option[@value="hilo"]')
    CART_BUTTON = (By.XPATH, '//div/a[@class="shopping_cart_link"]')
    PRODUCTS_NAME = (By.XPATH, '//div[@class="inventory_item_name "]')
    PRODUCTS_PRICE = (By.XPATH, '//div[@class="inventory_item_price"]')
    ADD_FIRST_BUTTON = (By.XPATH, '(//button[@class="btn btn_primary btn_small btn_inventory "])[1]')
    ADD_SECOND_BUTTON = (By.XPATH, '(//button[@class="btn btn_primary btn_small btn_inventory "])[2]')

    def add_to_cart(self):
        locators = (self.ADD_FIRST_BUTTON, self.ADD_SECOND_BUTTON)
        for idx, locator in enumerate(locators, start=1):
            with allure.step(f'Adding {idx} locator to cart'):
                self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Click on dropdown menu')
    def click_dropdown_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN)).click()

    @allure.step('Click on option ZA')
    def click_option_za(self):
        self.wait.until(EC.element_to_be_clickable(self.OPTION_ZA)).click()

    @allure.step('Click on option HILO')
    def click_option_hilo(self):
        self.wait.until(EC.element_to_be_clickable(self.OPTION_HILO)).click()

    @allure.step('Click cart')
    def click_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()

    @allure.step('Find all product names')
    def return_all_product_names(self):
        all_locators = self.driver.find_elements(*self.PRODUCTS_NAME)
        all_names = [el.text for el in all_locators]
        return all_names

    @allure.step('Find all product prices')
    def return_all_product_prices(self):
        all_locators = self.driver.find_elements(*self.PRODUCTS_PRICE)
        all_prices = [float(el.text.replace('$', '').strip()) for el in all_locators]
        return all_prices



