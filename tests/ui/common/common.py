from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_button_clickable(self, time_to_wait, button_locator):
        return WebDriverWait(self.driver, time_to_wait).until(
            EC.element_to_be_clickable(button_locator))
