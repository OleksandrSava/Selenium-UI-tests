import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20, 0.5)

    def open(self):
        with allure.step(f"Open page {self.page_url}"):
            self.driver.get(self.page_url)

    def open_check(self):
        try:
            with allure.step(f'Check if {self.page_url} is open'):
                self.wait.until(EC.url_contains(self.page_url))
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Page_load_error",
                          attachment_type=allure.attachment_type.PNG)
            raise RuntimeError(f"Failed to open page {self.page_url}") from e